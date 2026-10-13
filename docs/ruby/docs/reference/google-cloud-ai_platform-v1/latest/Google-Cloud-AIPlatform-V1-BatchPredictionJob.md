---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:53.919179+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::BatchPredictionJob (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::BatchPredictionJob.

A job that uses a [Model](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_model_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#model \(method\)") to produce predictions on multiple [input instances][google.cloud.aiplatform.v1.BatchPredictionJob.input_config]. If predictions for significant portion of the instances fail, the job may finish without attempting predictions for all remaining instances.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #completion_stats
    
    
    def completion_stats() -> ::Google::Cloud::AIPlatform::V1::CompletionStats

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::CompletionStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CompletionStats)) — Output only. Statistics on completed and failed prediction instances. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the BatchPredictionJob was created. 



### #dedicated_resources
    
    
    def dedicated_resources() -> ::Google::Cloud::AIPlatform::V1::BatchDedicatedResources

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchDedicatedResources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchDedicatedResources)) — The config of resources used by the Model during the batch prediction. If the Model [supports](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_supported_deployment_resources_types_instance_ "Google::Cloud::AIPlatform::V1::Model#supported_deployment_resources_types \(method\)") DEDICATED_RESOURCES this config may be provided (and the job will use these resources), if the Model doesn't support AUTOMATIC_RESOURCES, this config must be provided. 



### #dedicated_resources=
    
    
    def dedicated_resources=(value) -> ::Google::Cloud::AIPlatform::V1::BatchDedicatedResources

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BatchDedicatedResources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchDedicatedResources)) — The config of resources used by the Model during the batch prediction. If the Model [supports](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_supported_deployment_resources_types_instance_ "Google::Cloud::AIPlatform::V1::Model#supported_deployment_resources_types \(method\)") DEDICATED_RESOURCES this config may be provided (and the job will use these resources), if the Model doesn't support AUTOMATIC_RESOURCES, this config must be provided. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchDedicatedResources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchDedicatedResources)) — The config of resources used by the Model during the batch prediction. If the Model [supports](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_supported_deployment_resources_types_instance_ "Google::Cloud::AIPlatform::V1::Model#supported_deployment_resources_types \(method\)") DEDICATED_RESOURCES this config may be provided (and the job will use these resources), if the Model doesn't support AUTOMATIC_RESOURCES, this config must be provided. 



### #disable_container_logging
    
    
    def disable_container_logging() -> ::Boolean

**Returns**

  * (::Boolean) — For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing).

User can disable container logging by setting this flag to true. 




### #disable_container_logging=
    
    
    def disable_container_logging=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing).

User can disable container logging by setting this flag to true. 




**Returns**

  * (::Boolean) — For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing).

User can disable container logging by setting this flag to true. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. The user-defined name of this BatchPredictionJob. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The user-defined name of this BatchPredictionJob. 



**Returns**

  * (::String) — Required. The user-defined name of this BatchPredictionJob. 



### #encryption_spec
    
    
    def encryption_spec() -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options for a BatchPredictionJob. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key. 



### #encryption_spec=
    
    
    def encryption_spec=(value) -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options for a BatchPredictionJob. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key options for a BatchPredictionJob. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key. 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the BatchPredictionJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`. 



### #error
    
    
    def error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Rpc-Status)) — Output only. Only populated when the job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED. 



### #explanation_spec
    
    
    def explanation_spec() -> ::Google::Cloud::AIPlatform::V1::ExplanationSpec

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationSpec)) — Explanation configuration for this BatchPredictionJob. Can be specified only if [generate_explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_generate_explanation_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#generate_explanation \(method\)") is set to `true`.

This value overrides the value of [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)"). All fields of [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") are optional in the request. If a field of the [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") object is not populated, the corresponding field of the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") object is inherited. 




### #explanation_spec=
    
    
    def explanation_spec=(value) -> ::Google::Cloud::AIPlatform::V1::ExplanationSpec

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::ExplanationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationSpec)) — Explanation configuration for this BatchPredictionJob. Can be specified only if [generate_explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_generate_explanation_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#generate_explanation \(method\)") is set to `true`.

This value overrides the value of [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)"). All fields of [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") are optional in the request. If a field of the [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") object is not populated, the corresponding field of the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") object is inherited. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationSpec)) — Explanation configuration for this BatchPredictionJob. Can be specified only if [generate_explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_generate_explanation_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#generate_explanation \(method\)") is set to `true`.

This value overrides the value of [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)"). All fields of [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") are optional in the request. If a field of the [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") object is not populated, the corresponding field of the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") object is inherited. 




### #generate_explanation
    
    
    def generate_explanation() -> ::Boolean

**Returns**

  * (::Boolean) — Generate explanation with the batch prediction results.

When set to `true`, the batch prediction output changes based on the `predictions_format` field of the [BatchPredictionJob.output_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_output_config_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#output_config \(method\)") object:

    * `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `csv`: Generating explanations for CSV format is not supported.

If this field is set to true, either the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") or [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") must be populated. 




### #generate_explanation=
    
    
    def generate_explanation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Generate explanation with the batch prediction results.

When set to `true`, the batch prediction output changes based on the `predictions_format` field of the [BatchPredictionJob.output_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_output_config_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#output_config \(method\)") object:

    * `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `csv`: Generating explanations for CSV format is not supported.

If this field is set to true, either the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") or [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") must be populated. 




**Returns**

  * (::Boolean) — Generate explanation with the batch prediction results.

When set to `true`, the batch prediction output changes based on the `predictions_format` field of the [BatchPredictionJob.output_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_output_config_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#output_config \(method\)") object:

    * `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [Explanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Explanation "Google::Cloud::AIPlatform::V1::Explanation \(class\)") object.
    * `csv`: Generating explanations for CSV format is not supported.

If this field is set to true, either the [Model.explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Model#Google__Cloud__AIPlatform__V1__Model_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::Model#explanation_spec \(method\)") or [explanation_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_explanation_spec_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#explanation_spec \(method\)") must be populated. 




### #input_config
    
    
    def input_config() -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InputConfig

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InputConfig)) — Required. Input configuration of the instances on which predictions are performed. The schema of any single instance may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 



### #input_config=
    
    
    def input_config=(value) -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InputConfig

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InputConfig)) — Required. Input configuration of the instances on which predictions are performed. The schema of any single instance may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InputConfig)) — Required. Input configuration of the instances on which predictions are performed. The schema of any single instance may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 



### #instance_config
    
    
    def instance_config() -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig)) — Configuration for how to convert batch prediction input instances to the prediction instances that are sent to the Model. 



### #instance_config=
    
    
    def instance_config=(value) -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig)) — Configuration for how to convert batch prediction input instances to the prediction instances that are sent to the Model. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::InstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-InstanceConfig)) — Configuration for how to convert batch prediction input instances to the prediction instances that are sent to the Model. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize BatchPredictionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize BatchPredictionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize BatchPredictionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. 




### #manual_batch_tuning_parameters
    
    
    def manual_batch_tuning_parameters() -> ::Google::Cloud::AIPlatform::V1::ManualBatchTuningParameters

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ManualBatchTuningParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ManualBatchTuningParameters)) — Immutable. Parameters configuring the batch behavior. Currently only applicable when [dedicated_resources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_dedicated_resources_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#dedicated_resources \(method\)") are used (in other cases Vertex AI does the tuning itself). 



### #manual_batch_tuning_parameters=
    
    
    def manual_batch_tuning_parameters=(value) -> ::Google::Cloud::AIPlatform::V1::ManualBatchTuningParameters

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::ManualBatchTuningParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ManualBatchTuningParameters)) — Immutable. Parameters configuring the batch behavior. Currently only applicable when [dedicated_resources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_dedicated_resources_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#dedicated_resources \(method\)") are used (in other cases Vertex AI does the tuning itself). 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ManualBatchTuningParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ManualBatchTuningParameters)) — Immutable. Parameters configuring the batch behavior. Currently only applicable when [dedicated_resources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob#Google__Cloud__AIPlatform__V1__BatchPredictionJob_dedicated_resources_instance_ "Google::Cloud::AIPlatform::V1::BatchPredictionJob#dedicated_resources \(method\)") are used (in other cases Vertex AI does the tuning itself). 



### #model
    
    
    def model() -> ::String

**Returns**

  * (::String) — The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set.

The model resource name may contain version id or version alias to specify the version. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` if no version is specified, the default version will be deployed.

The model resource could also be a publisher model. Example: `publishers/{publisher}/models/{model}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`




### #model=
    
    
    def model=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set.

The model resource name may contain version id or version alias to specify the version. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` if no version is specified, the default version will be deployed.

The model resource could also be a publisher model. Example: `publishers/{publisher}/models/{model}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`




**Returns**

  * (::String) — The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set.

The model resource name may contain version id or version alias to specify the version. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` if no version is specified, the default version will be deployed.

The model resource could also be a publisher model. Example: `publishers/{publisher}/models/{model}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`




### #model_parameters
    
    
    def model_parameters() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — The parameters that govern the predictions. The schema of the parameters may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [parameters_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_parameters_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#parameters_schema_uri \(method\)"). 



### #model_parameters=
    
    
    def model_parameters=(value) -> ::Google::Protobuf::Value

**Parameter**

  * **value** ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — The parameters that govern the predictions. The schema of the parameters may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [parameters_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_parameters_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#parameters_schema_uri \(method\)"). 



**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — The parameters that govern the predictions. The schema of the parameters may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [parameters_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_parameters_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#parameters_schema_uri \(method\)"). 



### #model_version_id
    
    
    def model_version_id() -> ::String

**Returns**

  * (::String) — Output only. The version ID of the Model that produces the predictions via this job. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the BatchPredictionJob. 



### #output_config
    
    
    def output_config() -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputConfig

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-OutputConfig)) — Required. The Configuration specifying where output predictions should be written. The schema of any single prediction may be specified as a concatenation of [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)") and [prediction_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_prediction_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#prediction_schema_uri \(method\)"). 



### #output_config=
    
    
    def output_config=(value) -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputConfig

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-OutputConfig)) — Required. The Configuration specifying where output predictions should be written. The schema of any single prediction may be specified as a concatenation of [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)") and [prediction_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_prediction_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#prediction_schema_uri \(method\)"). 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-OutputConfig)) — Required. The Configuration specifying where output predictions should be written. The schema of any single prediction may be specified as a concatenation of [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)") and [prediction_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_prediction_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#prediction_schema_uri \(method\)"). 



### #output_info
    
    
    def output_info() -> ::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputInfo

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::BatchPredictionJob::OutputInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-BatchPredictionJob-OutputInfo)) — Output only. Information further describing the output of this job. 



### #partial_failures
    
    
    def partial_failures() -> ::Array<::Google::Rpc::Status>

**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Rpc-Status)>) — Output only. Partial failures encountered. For example, single files that can't be read. This field never exceeds 20 entries. Status details fields contain standard Google Cloud error details. 



### #resources_consumed
    
    
    def resources_consumed() -> ::Google::Cloud::AIPlatform::V1::ResourcesConsumed

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ResourcesConsumed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ResourcesConsumed)) — Output only. Information about resources that had been consumed by this job. Provided in real time at best effort basis, as well as a final value once the job completes.

Note: This field currently may be not populated for batch predictions that use AutoML Models. 




### #satisfies_pzi
    
    
    def satisfies_pzi() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Reserved for future use. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Reserved for future use. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — The service account that the DeployedModel's container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources.

Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account. 




### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — The service account that the DeployedModel's container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources.

Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account. 




**Returns**

  * (::String) — The service account that the DeployedModel's container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources.

Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account. 




### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the BatchPredictionJob for the first time entered the `JOB_STATE_RUNNING` state. 



### #state
    
    
    def state() -> ::Google::Cloud::AIPlatform::V1::JobState

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::JobState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-JobState)) — Output only. The detailed state of the job. 



### #unmanaged_container_model
    
    
    def unmanaged_container_model() -> ::Google::Cloud::AIPlatform::V1::UnmanagedContainerModel

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::UnmanagedContainerModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UnmanagedContainerModel)) — Contains model information necessary to perform batch prediction without requiring uploading to model registry. Exactly one of model and unmanaged_container_model must be set. 



### #unmanaged_container_model=
    
    
    def unmanaged_container_model=(value) -> ::Google::Cloud::AIPlatform::V1::UnmanagedContainerModel

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::UnmanagedContainerModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UnmanagedContainerModel)) — Contains model information necessary to perform batch prediction without requiring uploading to model registry. Exactly one of model and unmanaged_container_model must be set. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::UnmanagedContainerModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UnmanagedContainerModel)) — Contains model information necessary to perform batch prediction without requiring uploading to model registry. Exactly one of model and unmanaged_container_model must be set. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the BatchPredictionJob was most recently updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
