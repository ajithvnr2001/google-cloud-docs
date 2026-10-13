---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Attribution (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:42.972267+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Attribution (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::Attribution (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::Attribution.

Attribution that explains a particular prediction output.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #approximation_error
    
    
    def approximation_error() -> ::Float

**Returns**

  * (::Float) — Output only. Error of [feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)") caused by approximation used in the explanation method. Lower value means more precise attributions.

    * For Sampled Shapley [attribution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationParameters#Google__Cloud__AIPlatform__V1__ExplanationParameters_sampled_shapley_attribution_instance_ "Google::Cloud::AIPlatform::V1::ExplanationParameters#sampled_shapley_attribution \(method\)"), increasing [path_count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SampledShapleyAttribution#Google__Cloud__AIPlatform__V1__SampledShapleyAttribution_path_count_instance_ "Google::Cloud::AIPlatform::V1::SampledShapleyAttribution#path_count \(method\)") might reduce the error.
    * For Integrated Gradients [attribution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationParameters#Google__Cloud__AIPlatform__V1__ExplanationParameters_integrated_gradients_attribution_instance_ "Google::Cloud::AIPlatform::V1::ExplanationParameters#integrated_gradients_attribution \(method\)"), increasing [step_count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IntegratedGradientsAttribution#Google__Cloud__AIPlatform__V1__IntegratedGradientsAttribution_step_count_instance_ "Google::Cloud::AIPlatform::V1::IntegratedGradientsAttribution#step_count \(method\)") might reduce the error.
    * For [XRAI attribution][google.cloud.aiplatform.v1.ExplanationParameters.xrai_attribution], increasing [step_count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-XraiAttribution#Google__Cloud__AIPlatform__V1__XraiAttribution_step_count_instance_ "Google::Cloud::AIPlatform::V1::XraiAttribution#step_count \(method\)") might reduce the error.

See [this introduction](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) for more information. 




### #baseline_output_value
    
    
    def baseline_output_value() -> ::Float

**Returns**

  * (::Float) — Output only. Model predicted output if the input instance is constructed from the baselines of all the features defined in [ExplanationMetadata.inputs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata_inputs_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata#inputs \(method\)"). The field name of the output is determined by the key in [ExplanationMetadata.outputs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata_outputs_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata#outputs \(method\)").

If the Model's predicted output has multiple dimensions (rank > 1), this is the value in the output located by [output_index](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_output_index_instance_ "Google::Cloud::AIPlatform::V1::Attribution#output_index \(method\)").

If there are multiple baselines, their output values are averaged. 




### #feature_attributions
    
    
    def feature_attributions() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)) — Output only. Attributions of each explained feature. Features are extracted from the [prediction instances][google.cloud.aiplatform.v1.ExplainRequest.instances] according to [explanation metadata for inputs][google.cloud.aiplatform.v1.ExplanationMetadata.inputs].

The value is a struct, whose keys are the name of the feature. The values are how much the feature in the [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplainRequest#Google__Cloud__AIPlatform__V1__ExplainRequest_instances_instance_ "Google::Cloud::AIPlatform::V1::ExplainRequest#instances \(method\)") contributed to the predicted result.

The format of the value is determined by the feature's input format:

    * If the feature is a scalar value, the attribution value is a [floating number](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value#Google__Protobuf__Value_number_value_instance_ "Google::Protobuf::Value#number_value \(method\)").

    * If the feature is an array of scalar values, the attribution value is an [array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value#Google__Protobuf__Value_list_value_instance_ "Google::Protobuf::Value#list_value \(method\)").

    * If the feature is a struct, the attribution value is a [struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value#Google__Protobuf__Value_struct_value_instance_ "Google::Protobuf::Value#struct_value \(method\)"). The keys in the attribution value struct are the same as the keys in the feature struct. The formats of the values in the attribution struct are determined by the formats of the values in the feature struct.

The [ExplanationMetadata.feature_attributions_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata_feature_attributions_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata#feature_attributions_schema_uri \(method\)") field, pointed to by the [ExplanationSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationSpec "Google::Cloud::AIPlatform::V1::ExplanationSpec \(class\)") field of the [Endpoint.deployed_models](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Endpoint#Google__Cloud__AIPlatform__V1__Endpoint_deployed_models_instance_ "Google::Cloud::AIPlatform::V1::Endpoint#deployed_models \(method\)") object, points to the schema file that describes the features and their attribution values (if it is populated). 




### #instance_output_value
    
    
    def instance_output_value() -> ::Float

**Returns**

  * (::Float) — Output only. Model predicted output on the corresponding [explanation instance][ExplainRequest.instances]. The field name of the output is determined by the key in [ExplanationMetadata.outputs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata_outputs_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata#outputs \(method\)").

If the Model predicted output has multiple dimensions, this is the value in the output located by [output_index](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_output_index_instance_ "Google::Cloud::AIPlatform::V1::Attribution#output_index \(method\)"). 




### #output_display_name
    
    
    def output_display_name() -> ::String

**Returns**

  * (::String) — Output only. The display name of the output identified by [output_index](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_output_index_instance_ "Google::Cloud::AIPlatform::V1::Attribution#output_index \(method\)"). For example, the predicted class name by a multi-classification Model.

This field is only populated iff the Model predicts display names as a separate field along with the explained output. The predicted display name must has the same shape of the explained output, and can be located using output_index. 




### #output_index
    
    
    def output_index() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — Output only. The index that locates the explained prediction output.

If the prediction output is a scalar value, output_index is not populated. If the prediction output has multiple dimensions, the length of the output_index list is the same as the number of dimensions of the output. The i-th element in output_index is the element index of the i-th dimension of the output vector. Indices start from 0. 




### #output_name
    
    
    def output_name() -> ::String

**Returns**

  * (::String) — Output only. Name of the explain output. Specified as the key in [ExplanationMetadata.outputs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata_outputs_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata#outputs \(method\)"). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
