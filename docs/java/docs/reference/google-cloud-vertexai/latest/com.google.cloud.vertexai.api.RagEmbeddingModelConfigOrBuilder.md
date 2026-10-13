---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.RagEmbeddingModelConfigOrBuilder
title: Interface RagEmbeddingModelConfigOrBuilder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:51.242148+00:00
---

# Interface RagEmbeddingModelConfigOrBuilder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.RagEmbeddingModelConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RagEmbeddingModelConfigOrBuilder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface RagEmbeddingModelConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getModelConfigCase()
    
    
    public abstract RagEmbeddingModelConfig.ModelConfigCase getModelConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[RagEmbeddingModelConfig.ModelConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.RagEmbeddingModelConfig.ModelConfigCase)` |   
  
### getVertexPredictionEndpoint()
    
    
    public abstract RagEmbeddingModelConfig.VertexPredictionEndpoint getVertexPredictionEndpoint()

The Vertex AI Prediction Endpoint that either refers to a publisher model or an endpoint that is hosting a 1P fine-tuned text embedding model. Endpoints hosting non-1P fine-tuned text embedding models are currently not supported. This is used for dense vector search.

` .google.cloud.vertexai.v1.RagEmbeddingModelConfig.VertexPredictionEndpoint vertex_prediction_endpoint = 1; `

**Returns**  
---  
**Type** | **Description**  
`[RagEmbeddingModelConfig.VertexPredictionEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.RagEmbeddingModelConfig.VertexPredictionEndpoint)` | The vertexPredictionEndpoint.  
  
### getVertexPredictionEndpointOrBuilder()
    
    
    public abstract RagEmbeddingModelConfig.VertexPredictionEndpointOrBuilder getVertexPredictionEndpointOrBuilder()

The Vertex AI Prediction Endpoint that either refers to a publisher model or an endpoint that is hosting a 1P fine-tuned text embedding model. Endpoints hosting non-1P fine-tuned text embedding models are currently not supported. This is used for dense vector search.

` .google.cloud.vertexai.v1.RagEmbeddingModelConfig.VertexPredictionEndpoint vertex_prediction_endpoint = 1; `

**Returns**  
---  
**Type** | **Description**  
`[RagEmbeddingModelConfig.VertexPredictionEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.RagEmbeddingModelConfig.VertexPredictionEndpointOrBuilder)` |   
  
### hasVertexPredictionEndpoint()
    
    
    public abstract boolean hasVertexPredictionEndpoint()

The Vertex AI Prediction Endpoint that either refers to a publisher model or an endpoint that is hosting a 1P fine-tuned text embedding model. Endpoints hosting non-1P fine-tuned text embedding models are currently not supported. This is used for dense vector search.

` .google.cloud.vertexai.v1.RagEmbeddingModelConfig.VertexPredictionEndpoint vertex_prediction_endpoint = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vertexPredictionEndpoint field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
