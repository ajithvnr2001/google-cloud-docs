---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadataOrBuilder
title: Interface ExplanationMetadata.InputMetadataOrBuilder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:52.426564+00:00
---

# Interface ExplanationMetadata.InputMetadataOrBuilder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExplanationMetadata.InputMetadataOrBuilder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ExplanationMetadata.InputMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDenseShapeTensorName()
    
    
    public abstract String getDenseShapeTensorName()

Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: <https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor>.

`string dense_shape_tensor_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The denseShapeTensorName.  
  
### getDenseShapeTensorNameBytes()
    
    
    public abstract ByteString getDenseShapeTensorNameBytes()

Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: <https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor>.

`string dense_shape_tensor_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for denseShapeTensorName.  
  
### getEncodedBaselines(int index)
    
    
    public abstract Value getEncodedBaselines(int index)

A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor.

`repeated .google.protobuf.Value encoded_baselines = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getEncodedBaselinesCount()
    
    
    public abstract int getEncodedBaselinesCount()

A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor.

`repeated .google.protobuf.Value encoded_baselines = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEncodedBaselinesList()
    
    
    public abstract List<Value> getEncodedBaselinesList()

A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor.

`repeated .google.protobuf.Value encoded_baselines = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getEncodedBaselinesOrBuilder(int index)
    
    
    public abstract ValueOrBuilder getEncodedBaselinesOrBuilder(int index)

A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor.

`repeated .google.protobuf.Value encoded_baselines = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getEncodedBaselinesOrBuilderList()
    
    
    public abstract List<? extends ValueOrBuilder> getEncodedBaselinesOrBuilderList()

A list of baselines for the encoded tensor.

The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor.

`repeated .google.protobuf.Value encoded_baselines = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.ValueOrBuilder>` |   
  
### getEncodedTensorName()
    
    
    public abstract String getEncodedTensorName()

Encoded tensor is a transformation of the input tensor. Must be provided if choosing Integrated Gradients attribution or XRAI attribution and the input tensor is not differentiable.

An encoded tensor is generated if the input tensor is encoded by a lookup table.

`string encoded_tensor_name = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The encodedTensorName.  
  
### getEncodedTensorNameBytes()
    
    
    public abstract ByteString getEncodedTensorNameBytes()

Encoded tensor is a transformation of the input tensor. Must be provided if choosing Integrated Gradients attribution or XRAI attribution and the input tensor is not differentiable.

An encoded tensor is generated if the input tensor is encoded by a lookup table.

`string encoded_tensor_name = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for encodedTensorName.  
  
### getEncoding()
    
    
    public abstract ExplanationMetadata.InputMetadata.Encoding getEncoding()

Defines how the feature is encoded into the input tensor. Defaults to IDENTITY.

`.google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.Encoding encoding = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationMetadata.InputMetadata.Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadata.Encoding)` | The encoding.  
  
### getEncodingValue()
    
    
    public abstract int getEncodingValue()

Defines how the feature is encoded into the input tensor. Defaults to IDENTITY.

`.google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.Encoding encoding = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for encoding.  
  
### getFeatureValueDomain()
    
    
    public abstract ExplanationMetadata.InputMetadata.FeatureValueDomain getFeatureValueDomain()

The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.FeatureValueDomain feature_value_domain = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationMetadata.InputMetadata.FeatureValueDomain](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadata.FeatureValueDomain)` | The featureValueDomain.  
  
### getFeatureValueDomainOrBuilder()
    
    
    public abstract ExplanationMetadata.InputMetadata.FeatureValueDomainOrBuilder getFeatureValueDomainOrBuilder()

The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.FeatureValueDomain feature_value_domain = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationMetadata.InputMetadata.FeatureValueDomainOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadata.FeatureValueDomainOrBuilder)` |   
  
### getGroupName()
    
    
    public abstract String getGroupName()

Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in Attribution.feature_attributions, keyed by the group name.

`string group_name = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The groupName.  
  
### getGroupNameBytes()
    
    
    public abstract ByteString getGroupNameBytes()

Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in Attribution.feature_attributions, keyed by the group name.

`string group_name = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for groupName.  
  
### getIndexFeatureMapping(int index)
    
    
    public abstract String getIndexFeatureMapping(int index)

A list of feature names for each index in the input tensor. Required when the input InputMetadata.encoding is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR.

`repeated string index_feature_mapping = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The indexFeatureMapping at the given index.  
  
### getIndexFeatureMappingBytes(int index)
    
    
    public abstract ByteString getIndexFeatureMappingBytes(int index)

A list of feature names for each index in the input tensor. Required when the input InputMetadata.encoding is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR.

`repeated string index_feature_mapping = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the indexFeatureMapping at the given index.  
  
### getIndexFeatureMappingCount()
    
    
    public abstract int getIndexFeatureMappingCount()

A list of feature names for each index in the input tensor. Required when the input InputMetadata.encoding is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR.

`repeated string index_feature_mapping = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of indexFeatureMapping.  
  
### getIndexFeatureMappingList()
    
    
    public abstract List<String> getIndexFeatureMappingList()

A list of feature names for each index in the input tensor. Required when the input InputMetadata.encoding is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR.

`repeated string index_feature_mapping = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the indexFeatureMapping.  
  
### getIndicesTensorName()
    
    
    public abstract String getIndicesTensorName()

Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: <https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor>.

`string indices_tensor_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The indicesTensorName.  
  
### getIndicesTensorNameBytes()
    
    
    public abstract ByteString getIndicesTensorNameBytes()

Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: <https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor>.

`string indices_tensor_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for indicesTensorName.  
  
### getInputBaselines(int index)
    
    
    public abstract Value getInputBaselines(int index)

Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions.

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the instance[]. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value input_baselines = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getInputBaselinesCount()
    
    
    public abstract int getInputBaselinesCount()

Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions.

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the instance[]. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value input_baselines = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInputBaselinesList()
    
    
    public abstract List<Value> getInputBaselinesList()

Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions.

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the instance[]. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value input_baselines = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getInputBaselinesOrBuilder(int index)
    
    
    public abstract ValueOrBuilder getInputBaselinesOrBuilder(int index)

Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions.

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the instance[]. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value input_baselines = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getInputBaselinesOrBuilderList()
    
    
    public abstract List<? extends ValueOrBuilder> getInputBaselinesOrBuilderList()

Baseline inputs for this feature.

If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions.

For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor.

For custom images, the element of the baselines must be in the same format as the feature's input in the instance[]. The schema of any single instance may be specified via Endpoint's DeployedModels' Model's PredictSchemata's instance_schema_uri.

`repeated .google.protobuf.Value input_baselines = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.ValueOrBuilder>` |   
  
### getInputTensorName()
    
    
    public abstract String getInputTensorName()

Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow.

`string input_tensor_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inputTensorName.  
  
### getInputTensorNameBytes()
    
    
    public abstract ByteString getInputTensorNameBytes()

Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow.

`string input_tensor_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inputTensorName.  
  
### getModality()
    
    
    public abstract String getModality()

Modality of the feature. Valid values are: numeric, image. Defaults to numeric.

`string modality = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modality.  
  
### getModalityBytes()
    
    
    public abstract ByteString getModalityBytes()

Modality of the feature. Valid values are: numeric, image. Defaults to numeric.

`string modality = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modality.  
  
### getVisualization()
    
    
    public abstract ExplanationMetadata.InputMetadata.Visualization getVisualization()

Visualization configurations for image explanation.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.Visualization visualization = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationMetadata.InputMetadata.Visualization](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadata.Visualization)` | The visualization.  
  
### getVisualizationOrBuilder()
    
    
    public abstract ExplanationMetadata.InputMetadata.VisualizationOrBuilder getVisualizationOrBuilder()

Visualization configurations for image explanation.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.Visualization visualization = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ExplanationMetadata.InputMetadata.VisualizationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationMetadata.InputMetadata.VisualizationOrBuilder)` |   
  
### hasFeatureValueDomain()
    
    
    public abstract boolean hasFeatureValueDomain()

The domain details of the input feature value. Like min/max, original mean or standard deviation if normalized.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.FeatureValueDomain feature_value_domain = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the featureValueDomain field is set.  
  
### hasVisualization()
    
    
    public abstract boolean hasVisualization()

Visualization configurations for image explanation.

` .google.cloud.vertexai.v1.ExplanationMetadata.InputMetadata.Visualization visualization = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the visualization field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
