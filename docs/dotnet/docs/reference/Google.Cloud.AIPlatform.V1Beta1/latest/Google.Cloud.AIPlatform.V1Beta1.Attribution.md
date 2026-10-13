---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution
title: Vertex AI v1beta1 API - Class Attribution (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:27.593080+00:00
---

# Vertex AI v1beta1 API - Class Attribution (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class Attribution (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class Attribution : IMessage<Attribution>, IEquatable<Attribution>, IDeepCloneable<Attribution>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class Attribution.

Attribution that explains a particular prediction output.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Attribution

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Attribution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Attribution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Attribution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### Attribution()
    
    
    public Attribution()

### Attribution(Attribution)
    
    
    public Attribution(Attribution other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Attribution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Attribution)`  
  
  
## Properties 

### ApproximationError
    
    
    public double ApproximationError { get; set; }

Output only. Error of [feature_attributions][google.cloud.aiplatform.v1beta1.Attribution.feature_attributions] caused by approximation used in the explanation method. Lower value means more precise attributions.

  * For Sampled Shapley [attribution][google.cloud.aiplatform.v1beta1.ExplanationParameters.sampled_shapley_attribution], increasing [path_count][google.cloud.aiplatform.v1beta1.SampledShapleyAttribution.path_count] might reduce the error.
  * For Integrated Gradients [attribution][google.cloud.aiplatform.v1beta1.ExplanationParameters.integrated_gradients_attribution], increasing [step_count][google.cloud.aiplatform.v1beta1.IntegratedGradientsAttribution.step_count] might reduce the error.
  * For [XRAI attribution][google.cloud.aiplatform.v1beta1.ExplanationParameters.xrai_attribution], increasing [step_count][google.cloud.aiplatform.v1beta1.XraiAttribution.step_count] might reduce the error.



See [this introduction](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) for more information.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### BaselineOutputValue
    
    
    public double BaselineOutputValue { get; set; }

Output only. Model predicted output if the input instance is constructed from the baselines of all the features defined in [ExplanationMetadata.inputs][google.cloud.aiplatform.v1beta1.ExplanationMetadata.inputs]. The field name of the output is determined by the key in [ExplanationMetadata.outputs][google.cloud.aiplatform.v1beta1.ExplanationMetadata.outputs].

If the Model's predicted output has multiple dimensions (rank > 1), this is the value in the output located by [output_index][google.cloud.aiplatform.v1beta1.Attribution.output_index].

If there are multiple baselines, their output values are averaged.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### FeatureAttributions
    
    
    public Value FeatureAttributions { get; set; }

Output only. Attributions of each explained feature. Features are extracted from the [prediction instances][google.cloud.aiplatform.v1beta1.ExplainRequest.instances] according to [explanation metadata for inputs][google.cloud.aiplatform.v1beta1.ExplanationMetadata.inputs].

The value is a struct, whose keys are the name of the feature. The values are how much the feature in the [instance][google.cloud.aiplatform.v1beta1.ExplainRequest.instances] contributed to the predicted result.

The format of the value is determined by the feature's input format:

  * If the feature is a scalar value, the attribution value is a [floating number][google.protobuf.Value.number_value].

  * If the feature is an array of scalar values, the attribution value is an [array][google.protobuf.Value.list_value].

  * If the feature is a struct, the attribution value is a [struct][google.protobuf.Value.struct_value]. The keys in the attribution value struct are the same as the keys in the feature struct. The formats of the values in the attribution struct are determined by the formats of the values in the feature struct.




The [ExplanationMetadata.feature_attributions_schema_uri][google.cloud.aiplatform.v1beta1.ExplanationMetadata.feature_attributions_schema_uri] field, pointed to by the [ExplanationSpec][google.cloud.aiplatform.v1beta1.ExplanationSpec] field of the [Endpoint.deployed_models][google.cloud.aiplatform.v1beta1.Endpoint.deployed_models] object, points to the schema file that describes the features and their attribution values (if it is populated).

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### InstanceOutputValue
    
    
    public double InstanceOutputValue { get; set; }

Output only. Model predicted output on the corresponding [explanation instance][ExplainRequest.instances]. The field name of the output is determined by the key in [ExplanationMetadata.outputs][google.cloud.aiplatform.v1beta1.ExplanationMetadata.outputs].

If the Model predicted output has multiple dimensions, this is the value in the output located by [output_index][google.cloud.aiplatform.v1beta1.Attribution.output_index].

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### OutputDisplayName
    
    
    public string OutputDisplayName { get; set; }

Output only. The display name of the output identified by [output_index][google.cloud.aiplatform.v1beta1.Attribution.output_index]. For example, the predicted class name by a multi-classification Model.

This field is only populated iff the Model predicts display names as a separate field along with the explained output. The predicted display name must has the same shape of the explained output, and can be located using output_index.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OutputIndex
    
    
    public RepeatedField<int> OutputIndex { get; }

Output only. The index that locates the explained prediction output.

If the prediction output is a scalar value, output_index is not populated. If the prediction output has multiple dimensions, the length of the output_index list is the same as the number of dimensions of the output. The i-th element in output_index is the element index of the i-th dimension of the output vector. Indices start from 0.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### OutputName
    
    
    public string OutputName { get; set; }

Output only. Name of the explain output. Specified as the key in [ExplanationMetadata.outputs][google.cloud.aiplatform.v1beta1.ExplanationMetadata.outputs].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
