---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplainResponseOrBuilder
title: Interface ExplainResponseOrBuilder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:57.955619+00:00
---

# Interface ExplainResponseOrBuilder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplainResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExplainResponseOrBuilder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ExplainResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDeployedModelId()
    
    
    public abstract String getDeployedModelId()

ID of the Endpoint's DeployedModel that served this explanation.

`string deployed_model_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deployedModelId.  
  
### getDeployedModelIdBytes()
    
    
    public abstract ByteString getDeployedModelIdBytes()

ID of the Endpoint's DeployedModel that served this explanation.

`string deployed_model_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deployedModelId.  
  
### getExplanations(int index)
    
    
    public abstract Explanation getExplanations(int index)

The explanations of the Model's PredictResponse.predictions.

It has the same number of elements as instances to be explained.

`repeated .google.cloud.vertexai.v1.Explanation explanations = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)` |   
  
### getExplanationsCount()
    
    
    public abstract int getExplanationsCount()

The explanations of the Model's PredictResponse.predictions.

It has the same number of elements as instances to be explained.

`repeated .google.cloud.vertexai.v1.Explanation explanations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExplanationsList()
    
    
    public abstract List<Explanation> getExplanationsList()

The explanations of the Model's PredictResponse.predictions.

It has the same number of elements as instances to be explained.

`repeated .google.cloud.vertexai.v1.Explanation explanations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Explanation)>` |   
  
### getExplanationsOrBuilder(int index)
    
    
    public abstract ExplanationOrBuilder getExplanationsOrBuilder(int index)

The explanations of the Model's PredictResponse.predictions.

It has the same number of elements as instances to be explained.

`repeated .google.cloud.vertexai.v1.Explanation explanations = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExplanationOrBuilder)` |   
  
### getExplanationsOrBuilderList()
    
    
    public abstract List<? extends ExplanationOrBuilder> getExplanationsOrBuilderList()

The explanations of the Model's PredictResponse.predictions.

It has the same number of elements as instances to be explained.

`repeated .google.cloud.vertexai.v1.Explanation explanations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.ExplanationOrBuilder>` |   
  
### getPredictions(int index)
    
    
    public abstract Value getPredictions(int index)

The predictions that are the output of the predictions call. Same as PredictResponse.predictions.

`repeated .google.protobuf.Value predictions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` |   
  
### getPredictionsCount()
    
    
    public abstract int getPredictionsCount()

The predictions that are the output of the predictions call. Same as PredictResponse.predictions.

`repeated .google.protobuf.Value predictions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPredictionsList()
    
    
    public abstract List<Value> getPredictionsList()

The predictions that are the output of the predictions call. Same as PredictResponse.predictions.

`repeated .google.protobuf.Value predictions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)>` |   
  
### getPredictionsOrBuilder(int index)
    
    
    public abstract ValueOrBuilder getPredictionsOrBuilder(int index)

The predictions that are the output of the predictions call. Same as PredictResponse.predictions.

`repeated .google.protobuf.Value predictions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getPredictionsOrBuilderList()
    
    
    public abstract List<? extends ValueOrBuilder> getPredictionsOrBuilderList()

The predictions that are the output of the predictions call. Same as PredictResponse.predictions.

`repeated .google.protobuf.Value predictions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.ValueOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
