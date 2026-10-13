---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-Evaluation/
title: AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::Evaluation (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:13.988771+00:00
---

# AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::Evaluation (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-Evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::Evaluation (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.0 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the AI Platform Data Labeling Service V1beta1 API class Google::Cloud::DataLabeling::V1beta1::Evaluation.

Describes an evaluation between a machine learning model's predictions and ground truth labels. Created when an [EvaluationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationJob "Google::Cloud::DataLabeling::V1beta1::EvaluationJob \(class\)") runs successfully.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotation_type
    
    
    def annotation_type() -> ::Google::Cloud::DataLabeling::V1beta1::AnnotationType

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::AnnotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-AnnotationType)) — Output only. Type of task that the model version being evaluated performs, as defined in the

[evaluationJobConfig.inputConfig.annotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationJobConfig#Google__Cloud__DataLabeling__V1beta1__EvaluationJobConfig_input_config_instance_ "Google::Cloud::DataLabeling::V1beta1::EvaluationJobConfig#input_config \(method\)") field of the evaluation job that created this evaluation. 




### #annotation_type=
    
    
    def annotation_type=(value) -> ::Google::Cloud::DataLabeling::V1beta1::AnnotationType

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::AnnotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-AnnotationType)) — Output only. Type of task that the model version being evaluated performs, as defined in the

[evaluationJobConfig.inputConfig.annotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationJobConfig#Google__Cloud__DataLabeling__V1beta1__EvaluationJobConfig_input_config_instance_ "Google::Cloud::DataLabeling::V1beta1::EvaluationJobConfig#input_config \(method\)") field of the evaluation job that created this evaluation. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::AnnotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-AnnotationType)) — Output only. Type of task that the model version being evaluated performs, as defined in the

[evaluationJobConfig.inputConfig.annotationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationJobConfig#Google__Cloud__DataLabeling__V1beta1__EvaluationJobConfig_input_config_instance_ "Google::Cloud::DataLabeling::V1beta1::EvaluationJobConfig#input_config \(method\)") field of the evaluation job that created this evaluation. 




### #config
    
    
    def config() -> ::Google::Cloud::DataLabeling::V1beta1::EvaluationConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EvaluationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationConfig)) — Output only. Options used in the evaluation job that created this evaluation. 



### #config=
    
    
    def config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::EvaluationConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::EvaluationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationConfig)) — Output only. Options used in the evaluation job that created this evaluation. 



**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EvaluationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationConfig)) — Output only. Options used in the evaluation job that created this evaluation. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when this evaluation was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when this evaluation was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when this evaluation was created. 



### #evaluated_item_count
    
    
    def evaluated_item_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. 



### #evaluated_item_count=
    
    
    def evaluated_item_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. 



**Returns**

  * (::Integer) — Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. 



### #evaluation_job_run_time
    
    
    def evaluation_job_run_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when the evaluation job that created this evaluation ran. 



### #evaluation_job_run_time=
    
    
    def evaluation_job_run_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when the evaluation job that created this evaluation ran. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp for when the evaluation job that created this evaluation ran. 



### #evaluation_metrics
    
    
    def evaluation_metrics() -> ::Google::Cloud::DataLabeling::V1beta1::EvaluationMetrics

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EvaluationMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationMetrics)) — Output only. Metrics comparing predictions to ground truth labels. 



### #evaluation_metrics=
    
    
    def evaluation_metrics=(value) -> ::Google::Cloud::DataLabeling::V1beta1::EvaluationMetrics

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::EvaluationMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationMetrics)) — Output only. Metrics comparing predictions to ground truth labels. 



**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EvaluationMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EvaluationMetrics)) — Output only. Metrics comparing predictions to ground truth labels. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of an evaluation. The name has the following format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}' 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. Resource name of an evaluation. The name has the following format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}' 




**Returns**

  * (::String) — Output only. Resource name of an evaluation. The name has the following format:

"projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}' 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
