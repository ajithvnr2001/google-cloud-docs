---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:08.482295+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata.

Metadata of the input of a feature.

Fields other than [InputMetadata.input_baselines](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata__InputMetadata_input_baselines_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata#input_baselines \(method\)") are applicable only for Models that are using Vertex AI-provided images for Tensorflow.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #dense_shape_tensor_name
    
    
    def dense_shape_tensor_name() -> ::String

**Returns**

  * (::String) — Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



### #dense_shape_tensor_name=
    
    
    def dense_shape_tensor_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



**Returns**

  * (::String) — Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



### #encoded_baselines
    
    
    def encoded_baselines() -> ::Array<::Google::Protobuf::Value>

**Returns**

  * (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor. 




### #encoded_baselines=
    
    
    def encoded_baselines=(value) -> ::Array<::Google::Protobuf::Value>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor. 




**Returns**

  * (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor. 




### #encoded_tensor_name
    
    
    def encoded_tensor_name() -> ::String

**Returns**

  * (::String) — Encoded tensor is a transformation of the input tensor. Must be provided if choosing [Integrated Gradients attribution][google.cloud.aiplatform.v1.ExplanationParameters.integrated_gradients_attribution] or [XRAI attribution][google.cloud.aiplatform.v1.ExplanationParameters.xrai_attribution] and the input tensor is not differentiable.

An encoded tensor is generated if the input tensor is encoded by a lookup table. 




### #encoded_tensor_name=
    
    
    def encoded_tensor_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Encoded tensor is a transformation of the input tensor. Must be provided if choosing [Integrated Gradients attribution][google.cloud.aiplatform.v1.ExplanationParameters.integrated_gradients_attribution] or [XRAI attribution][google.cloud.aiplatform.v1.ExplanationParameters.xrai_attribution] and the input tensor is not differentiable.

An encoded tensor is generated if the input tensor is encoded by a lookup table. 




**Returns**

  * (::String) — Encoded tensor is a transformation of the input tensor. Must be provided if choosing [Integrated Gradients attribution][google.cloud.aiplatform.v1.ExplanationParameters.integrated_gradients_attribution] or [XRAI attribution][google.cloud.aiplatform.v1.ExplanationParameters.xrai_attribution] and the input tensor is not differentiable.

An encoded tensor is generated if the input tensor is encoded by a lookup table. 




### #encoding
    
    
    def encoding() -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Encoding

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Encoding)) — Defines how the feature is encoded into the input tensor. Defaults to IDENTITY. 



### #encoding=
    
    
    def encoding=(value) -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Encoding

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Encoding)) — Defines how the feature is encoded into the input tensor. Defaults to IDENTITY. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Encoding)) — Defines how the feature is encoded into the input tensor. Defaults to IDENTITY. 



### #feature_value_domain
    
    
    def feature_value_domain() -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::FeatureValueDomain

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::FeatureValueDomain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-FeatureValueDomain)) — The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized. 



### #feature_value_domain=
    
    
    def feature_value_domain=(value) -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::FeatureValueDomain

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::FeatureValueDomain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-FeatureValueDomain)) — The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::FeatureValueDomain](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-FeatureValueDomain)) — The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized. 



### #group_name
    
    
    def group_name() -> ::String

**Returns**

  * (::String) — Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)"), keyed by the group name. 



### #group_name=
    
    
    def group_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)"), keyed by the group name. 



**Returns**

  * (::String) — Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)"), keyed by the group name. 



### #index_feature_mapping
    
    
    def index_feature_mapping() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of feature names for each index in the input tensor. Required when the input [InputMetadata.encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata__InputMetadata_encoding_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata#encoding \(method\)") is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR. 



### #index_feature_mapping=
    
    
    def index_feature_mapping=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of feature names for each index in the input tensor. Required when the input [InputMetadata.encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata__InputMetadata_encoding_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata#encoding \(method\)") is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR. 



**Returns**

  * (::Array<::String>) — A list of feature names for each index in the input tensor. Required when the input [InputMetadata.encoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata#Google__Cloud__AIPlatform__V1__ExplanationMetadata__InputMetadata_encoding_instance_ "Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata#encoding \(method\)") is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR. 



### #indices_tensor_name
    
    
    def indices_tensor_name() -> ::String

**Returns**

  * (::String) — Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



### #indices_tensor_name=
    
    
    def indices_tensor_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



**Returns**

  * (::String) — Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. 



### #input_baselines
    
    
    def input_baselines() -> ::Array<::Google::Protobuf::Value>

**Returns**

  * (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)").

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplainRequest#Google__Cloud__AIPlatform__V1__ExplainRequest_instances_instance_ "Google::Cloud::AIPlatform::V1::ExplainRequest#instances \(method\)")[]. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 




### #input_baselines=
    
    
    def input_baselines=(value) -> ::Array<::Google::Protobuf::Value>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)").

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplainRequest#Google__Cloud__AIPlatform__V1__ExplainRequest_instances_instance_ "Google::Cloud::AIPlatform::V1::ExplainRequest#instances \(method\)")[]. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 




**Returns**

  * (::Array<[::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Value)>) — Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in [Attribution.feature_attributions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-Attribution#Google__Cloud__AIPlatform__V1__Attribution_feature_attributions_instance_ "Google::Cloud::AIPlatform::V1::Attribution#feature_attributions \(method\)").

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplainRequest#Google__Cloud__AIPlatform__V1__ExplainRequest_instances_instance_ "Google::Cloud::AIPlatform::V1::ExplainRequest#instances \(method\)")[]. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictSchemata#Google__Cloud__AIPlatform__V1__PredictSchemata_instance_schema_uri_instance_ "Google::Cloud::AIPlatform::V1::PredictSchemata#instance_schema_uri \(method\)"). 




### #input_tensor_name
    
    
    def input_tensor_name() -> ::String

**Returns**

  * (::String) — Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow. 



### #input_tensor_name=
    
    
    def input_tensor_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow. 



**Returns**

  * (::String) — Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow. 



### #modality
    
    
    def modality() -> ::String

**Returns**

  * (::String) — Modality of the feature. Valid values are: numeric, image. Defaults to numeric. 



### #modality=
    
    
    def modality=(value) -> ::String

**Parameter**

  * **value** (::String) — Modality of the feature. Valid values are: numeric, image. Defaults to numeric. 



**Returns**

  * (::String) — Modality of the feature. Valid values are: numeric, image. Defaults to numeric. 



### #visualization
    
    
    def visualization() -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Visualization

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Visualization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Visualization)) — Visualization configurations for image explanation. 



### #visualization=
    
    
    def visualization=(value) -> ::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Visualization

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Visualization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Visualization)) — Visualization configurations for image explanation. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::ExplanationMetadata::InputMetadata::Visualization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ExplanationMetadata-InputMetadata-Visualization)) — Visualization configurations for image explanation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
