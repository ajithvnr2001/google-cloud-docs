---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Schema-TrainingJob-Definition-AutoMlImageClassificationInputs/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:57.417864+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Schema-TrainingJob-Definition-AutoMlImageClassificationInputs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #base_model_id
    
    
    def base_model_id() -> ::String

**Returns**

  * (::String) — The ID of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType. 



### #base_model_id=
    
    
    def base_model_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType. 



**Returns**

  * (::String) — The ID of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType. 



### #budget_milli_node_hours
    
    
    def budget_milli_node_hours() -> ::Integer

**Returns**

  * (::Integer) — The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 8,000 and 800,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time, considering 8 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1`, the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used. 



### #budget_milli_node_hours=
    
    
    def budget_milli_node_hours=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 8,000 and 800,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time, considering 8 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1`, the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used. 



**Returns**

  * (::Integer) — The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 8,000 and 800,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time, considering 8 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1`, the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used. 



### #disable_early_stopping
    
    
    def disable_early_stopping() -> ::Boolean

**Returns**

  * (::Boolean) — Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Classification might stop training before the entire training budget has been used. 



### #disable_early_stopping=
    
    
    def disable_early_stopping=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Classification might stop training before the entire training budget has been used. 



**Returns**

  * (::Boolean) — Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Classification might stop training before the entire training budget has been used. 



### #model_type
    
    
    def model_type() -> ::Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs::ModelType

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs::ModelType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Schema-TrainingJob-Definition-AutoMlImageClassificationInputs-ModelType)) 



### #model_type=
    
    
    def model_type=(value) -> ::Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs::ModelType

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs::ModelType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Schema-TrainingJob-Definition-AutoMlImageClassificationInputs-ModelType)) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition::AutoMlImageClassificationInputs::ModelType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Schema-TrainingJob-Definition-AutoMlImageClassificationInputs-ModelType)) 



### #multi_label
    
    
    def multi_label() -> ::Boolean

**Returns**

  * (::Boolean) — If false, a single-label (multi-class) Model will be trained (i.e. assuming that for each image just up to one annotation may be applicable). If true, a multi-label Model will be trained (i.e. assuming that for each image multiple annotations may be applicable). 



### #multi_label=
    
    
    def multi_label=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If false, a single-label (multi-class) Model will be trained (i.e. assuming that for each image just up to one annotation may be applicable). If true, a multi-label Model will be trained (i.e. assuming that for each image multiple annotations may be applicable). 



**Returns**

  * (::Boolean) — If false, a single-label (multi-class) Model will be trained (i.e. assuming that for each image just up to one annotation may be applicable). If true, a multi-label Model will be trained (i.e. assuming that for each image multiple annotations may be applicable). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
