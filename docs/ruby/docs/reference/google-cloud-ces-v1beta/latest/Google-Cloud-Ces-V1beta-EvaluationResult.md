---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::EvaluationResult (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:33.405983+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::EvaluationResult (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::EvaluationResult (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::EvaluationResult.

An evaluation result represents the output of running an Evaluation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_version
    
    
    def app_version() -> ::String

**Returns**

  * (::String) — Output only. The app version used to generate the conversation that resulted in this result. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`



### #app_version_display_name
    
    
    def app_version_display_name() -> ::String

**Returns**

  * (::String) — Output only. The display name of the `app_version` that the evaluation ran against. 



### #changelog
    
    
    def changelog() -> ::String

**Returns**

  * (::String) — Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft. 



### #changelog_create_time
    
    
    def changelog_create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft. 



### #config
    
    
    def config() -> ::Google::Cloud::Ces::V1beta::EvaluationConfig

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationConfig)) — Output only. The configuration used in the evaluation run that resulted in this result. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the evaluation result was created. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — 

Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: "

    * 


### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: "

    * 


**Returns**

  * (::String) — 

Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: "

    * 


### #error
    
    
    def error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Rpc-Status)) — Output only. Deprecated: Use `error_info` instead. Errors encountered during execution. 



### #error_info
    
    
    def error_info() -> ::Google::Cloud::Ces::V1beta::EvaluationErrorInfo

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationErrorInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationErrorInfo)) — Output only. Error information for the evaluation result. 



### #evaluation_metrics_thresholds
    
    
    def evaluation_metrics_thresholds() -> ::Google::Cloud::Ces::V1beta::EvaluationMetricsThresholds

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationMetricsThresholds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationMetricsThresholds)) — Output only. The evaluation thresholds for the result. 



### #evaluation_run
    
    
    def evaluation_run() -> ::String

**Returns**

  * (::String) — Output only. The evaluation run that produced this result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`



### #evaluation_status
    
    
    def evaluation_status() -> ::Google::Cloud::Ces::V1beta::EvaluationResult::Outcome

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationResult::Outcome](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult-Outcome)) — Output only. The outcome of the evaluation. Only populated if execution_state is COMPLETE. 



### #execution_state
    
    
    def execution_state() -> ::Google::Cloud::Ces::V1beta::EvaluationResult::ExecutionState

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationResult::ExecutionState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult-ExecutionState)) — Output only. The state of the evaluation result execution. 



### #golden_result
    
    
    def golden_result() -> ::Google::Cloud::Ces::V1beta::EvaluationResult::GoldenResult

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationResult::GoldenResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult-GoldenResult)) — Output only. The outcome of a golden evaluation.

Note: The following fields are mutually exclusive: `golden_result`, `scenario_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #golden_run_method
    
    
    def golden_run_method() -> ::Google::Cloud::Ces::V1beta::GoldenRunMethod

**Returns**

  * ([::Google::Cloud::Ces::V1beta::GoldenRunMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-GoldenRunMethod)) — Output only. The method used to run the golden evaluation. 



### #initiated_by
    
    
    def initiated_by() -> ::String

**Returns**

  * (::String) — Output only. The user who initiated the evaluation run that resulted in this result. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`



**Returns**

  * (::String) — Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`



### #persona
    
    
    def persona() -> ::Google::Cloud::Ces::V1beta::EvaluationPersona

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationPersona](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationPersona)) — Output only. The persona used to generate the conversation for the evaluation result. 



### #scenario_result
    
    
    def scenario_result() -> ::Google::Cloud::Ces::V1beta::EvaluationResult::ScenarioResult

**Returns**

  * ([::Google::Cloud::Ces::V1beta::EvaluationResult::ScenarioResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationResult-ScenarioResult)) — Output only. The outcome of a scenario evaluation.

Note: The following fields are mutually exclusive: `scenario_result`, `golden_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
