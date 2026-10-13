---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:54.574797+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig.

Configuration defining how to transform batch prediction input instances to the instances that the Model accepts.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #excluded_fields
    
    
    def excluded_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Fields that will be excluded in the prediction instance that is sent to the Model.

Excluded will be attached to the batch prediction output if [key_field](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_key_field_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#key_field \(method\)") is not specified.

When excluded_fields is populated, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




### #excluded_fields=
    
    
    def excluded_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Fields that will be excluded in the prediction instance that is sent to the Model.

Excluded will be attached to the batch prediction output if [key_field](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_key_field_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#key_field \(method\)") is not specified.

When excluded_fields is populated, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




**Returns**

  * (::Array<::String>) — Fields that will be excluded in the prediction instance that is sent to the Model.

Excluded will be attached to the batch prediction output if [key_field](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_key_field_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#key_field \(method\)") is not specified.

When excluded_fields is populated, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




### #included_fields
    
    
    def included_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Fields that will be included in the prediction instance that is sent to the Model.

If [instance_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_instance_type_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#instance_type \(method\)") is `array`, the order of field names in included_fields also determines the order of the values in the array.

When included_fields is populated, [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




### #included_fields=
    
    
    def included_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Fields that will be included in the prediction instance that is sent to the Model.

If [instance_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_instance_type_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#instance_type \(method\)") is `array`, the order of field names in included_fields also determines the order of the values in the array.

When included_fields is populated, [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




**Returns**

  * (::Array<::String>) — Fields that will be included in the prediction instance that is sent to the Model.

If [instance_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_instance_type_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#instance_type \(method\)") is `array`, the order of field names in included_fields also determines the order of the values in the array.

When included_fields is populated, [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)") must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord. 




### #instance_type
    
    
    def instance_type() -> ::String

**Returns**

  * (::String) — 

The format of the instance that the Model accepts. Vertex AI will convert compatible [batch prediction input instance formats][google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.instances_format] to the specified format.

Supported values are:

    * `object`: Each input is converted to JSON object format.

      * For `bigquery`, each row is converted to an object.
      * For `jsonl`, each line of the JSONL input must be an object.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.
    * `array`: Each input is converted to JSON array format.

      * For `bigquery`, each row is converted to an array. The order of columns is determined by the BigQuery column order, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated. [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * For `jsonl`, if each line of the JSONL input is an object, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.

If not specified, Vertex AI converts the batch prediction input as follows:

    * For `bigquery` and `csv`, the behavior is the same as `array`. The order of columns is the same as defined in the file or table, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated.
    * For `jsonl`, the prediction instance format is determined by each line of the input.
    * For `tf-record`/`tf-record-gzip`, each record will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the record.
    * For `file-list`, each file in the list will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the file.



### #instance_type=
    
    
    def instance_type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The format of the instance that the Model accepts. Vertex AI will convert compatible [batch prediction input instance formats][google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.instances_format] to the specified format.

Supported values are:

    * `object`: Each input is converted to JSON object format.

      * For `bigquery`, each row is converted to an object.
      * For `jsonl`, each line of the JSONL input must be an object.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.
    * `array`: Each input is converted to JSON array format.

      * For `bigquery`, each row is converted to an array. The order of columns is determined by the BigQuery column order, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated. [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * For `jsonl`, if each line of the JSONL input is an object, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.

If not specified, Vertex AI converts the batch prediction input as follows:

    * For `bigquery` and `csv`, the behavior is the same as `array`. The order of columns is the same as defined in the file or table, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated.
    * For `jsonl`, the prediction instance format is determined by each line of the input.
    * For `tf-record`/`tf-record-gzip`, each record will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the record.
    * For `file-list`, each file in the list will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the file.



**Returns**

  * (::String) — 

The format of the instance that the Model accepts. Vertex AI will convert compatible [batch prediction input instance formats][google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.instances_format] to the specified format.

Supported values are:

    * `object`: Each input is converted to JSON object format.

      * For `bigquery`, each row is converted to an object.
      * For `jsonl`, each line of the JSONL input must be an object.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.
    * `array`: Each input is converted to JSON array format.

      * For `bigquery`, each row is converted to an array. The order of columns is determined by the BigQuery column order, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated. [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * For `jsonl`, if each line of the JSONL input is an object, [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") must be populated for specifying field orders.
      * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.

If not specified, Vertex AI converts the batch prediction input as follows:

    * For `bigquery` and `csv`, the behavior is the same as `array`. The order of columns is the same as defined in the file or table, unless [included_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_included_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#included_fields \(method\)") is populated.
    * For `jsonl`, the prediction instance format is determined by each line of the input.
    * For `tf-record`/`tf-record-gzip`, each record will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the record.
    * For `file-list`, each file in the list will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the file.



### #key_field
    
    
    def key_field() -> ::String

**Returns**

  * (::String) — The name of the field that is considered as a key.

The values identified by the key field is not included in the transformed instances that is sent to the Model. This is similar to specifying this name of the field in [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)"). In addition, the batch prediction output will not include the instances. Instead the output will only include the value of the key field, in a field named `key` in the output:

    * For `jsonl` output format, the output will have a `key` field instead of the `instance` field.
    * For `csv`/`bigquery` output format, the output will have have a `key` column instead of the instance feature columns.

The input must be JSONL with objects at each line, CSV, BigQuery or TfRecord. 




### #key_field=
    
    
    def key_field=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the field that is considered as a key.

The values identified by the key field is not included in the transformed instances that is sent to the Model. This is similar to specifying this name of the field in [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)"). In addition, the batch prediction output will not include the instances. Instead the output will only include the value of the key field, in a field named `key` in the output:

    * For `jsonl` output format, the output will have a `key` field instead of the `instance` field.
    * For `csv`/`bigquery` output format, the output will have have a `key` column instead of the instance feature columns.

The input must be JSONL with objects at each line, CSV, BigQuery or TfRecord. 




**Returns**

  * (::String) — The name of the field that is considered as a key.

The values identified by the key field is not included in the transformed instances that is sent to the Model. This is similar to specifying this name of the field in [excluded_fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig#Google__Cloud__AIPlatform__V1__BatchPredictionJob__InstanceConfig_excluded_fields_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig#excluded_fields \(method\)"). In addition, the batch prediction output will not include the instances. Instead the output will only include the value of the key field, in a field named `key` in the output:

    * For `jsonl` output format, the output will have a `key` field instead of the `instance` field.
    * For `csv`/`bigquery` output format, the output will have have a `key` column instead of the instance feature columns.

The input must be JSONL with objects at each line, CSV, BigQuery or TfRecord. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
