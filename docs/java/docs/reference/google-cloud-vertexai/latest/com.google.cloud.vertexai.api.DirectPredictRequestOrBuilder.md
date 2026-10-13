---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.DirectPredictRequestOrBuilder
title: Interface DirectPredictRequestOrBuilder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:39.524091+00:00
---

# Interface DirectPredictRequestOrBuilder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.DirectPredictRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DirectPredictRequestOrBuilder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DirectPredictRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndpoint()
    
    
    public abstract String getEndpoint()

Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpoint.  
  
### getEndpointBytes()
    
    
    public abstract ByteString getEndpointBytes()

Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

` string endpoint = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpoint.  
  
### getInputs(int index)
    
    
    public abstract Tensor getInputs(int index)

The prediction input.

`repeated .google.cloud.vertexai.v1.Tensor inputs = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Tensor)` |   
  
### getInputsCount()
    
    
    public abstract int getInputsCount()

The prediction input.

`repeated .google.cloud.vertexai.v1.Tensor inputs = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInputsList()
    
    
    public abstract List<Tensor> getInputsList()

The prediction input.

`repeated .google.cloud.vertexai.v1.Tensor inputs = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Tensor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Tensor)>` |   
  
### getInputsOrBuilder(int index)
    
    
    public abstract TensorOrBuilder getInputsOrBuilder(int index)

The prediction input.

`repeated .google.cloud.vertexai.v1.Tensor inputs = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TensorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.TensorOrBuilder)` |   
  
### getInputsOrBuilderList()
    
    
    public abstract List<? extends TensorOrBuilder> getInputsOrBuilderList()

The prediction input.

`repeated .google.cloud.vertexai.v1.Tensor inputs = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vertexai.api.TensorOrBuilder>` |   
  
### getParameters()
    
    
    public abstract Tensor getParameters()

The parameters that govern the prediction.

`.google.cloud.vertexai.v1.Tensor parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Tensor](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Tensor)` | The parameters.  
  
### getParametersOrBuilder()
    
    
    public abstract TensorOrBuilder getParametersOrBuilder()

The parameters that govern the prediction.

`.google.cloud.vertexai.v1.Tensor parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TensorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.TensorOrBuilder)` |   
  
### hasParameters()
    
    
    public abstract boolean hasParameters()

The parameters that govern the prediction.

`.google.cloud.vertexai.v1.Tensor parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parameters field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
