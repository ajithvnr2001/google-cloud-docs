---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationOrBuilder
title: Interface ExplanationOrBuilder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:20.224962+00:00
---

# Interface ExplanationOrBuilder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExplanationOrBuilder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ExplanationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttributions(int index)
    
    
    public abstract Attribution getAttributions(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)` |   
  
### getAttributionsCount()
    
    
    public abstract int getAttributionsCount()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributionsList()
    
    
    public abstract List<Attribution> getAttributionsList()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Attribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Attribution)>` |   
  
### getAttributionsOrBuilder(int index)
    
    
    public abstract AttributionOrBuilder getAttributionsOrBuilder(int index)

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.AttributionOrBuilder)` |   
  
### getAttributionsOrBuilderList()
    
    
    public abstract List<? extends AttributionOrBuilder> getAttributionsOrBuilderList()

Output only. Feature attributions grouped by predicted outputs.

For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining.

By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.

If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices.

` repeated .google.cloud.vertexai.v1.Attribution attributions = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.AttributionOrBuilder>` |   
  
### getNeighbors(int index)
    
    
    public abstract Neighbor getNeighbors(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)` |   
  
### getNeighborsCount()
    
    
    public abstract int getNeighborsCount()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNeighborsList()
    
    
    public abstract List<Neighbor> getNeighborsList()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Neighbor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Neighbor)>` |   
  
### getNeighborsOrBuilder(int index)
    
    
    public abstract NeighborOrBuilder getNeighborsOrBuilder(int index)

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NeighborOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.NeighborOrBuilder)` |   
  
### getNeighborsOrBuilderList()
    
    
    public abstract List<? extends NeighborOrBuilder> getNeighborsOrBuilderList()

Output only. List of the nearest neighbors for example-based explanations.

For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated.

` repeated .google.cloud.vertexai.v1.Neighbor neighbors = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.NeighborOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
