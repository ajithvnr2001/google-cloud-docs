---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VertexEmbeddingConfigOrBuilder
title: Interface VertexEmbeddingConfigOrBuilder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:37.077601+00:00
---

# Interface VertexEmbeddingConfigOrBuilder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VertexEmbeddingConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VertexEmbeddingConfigOrBuilder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface VertexEmbeddingConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getModelId()
    
    
    public abstract String getModelId()

Required. Required: ID of the embedding model to use. See <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#embeddings-models> for the list of supported models.

`string model_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The modelId.  
  
### getModelIdBytes()
    
    
    public abstract ByteString getModelIdBytes()

Required. Required: ID of the embedding model to use. See <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#embeddings-models> for the list of supported models.

`string model_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for modelId.  
  
### getTaskType()
    
    
    public abstract EmbeddingTaskType getTaskType()

Optional. Optional: Task type for the embeddings. Required for text-only embedding models, see <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types> Not needed for multi modal embedding models, see <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#specify-task-instructions>

` .google.cloud.vectorsearch.v1.EmbeddingTaskType task_type = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EmbeddingTaskType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.EmbeddingTaskType)` | The taskType.  
  
### getTaskTypeValue()
    
    
    public abstract int getTaskTypeValue()

Optional. Optional: Task type for the embeddings. Required for text-only embedding models, see <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types> Not needed for multi modal embedding models, see <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#specify-task-instructions>

` .google.cloud.vectorsearch.v1.EmbeddingTaskType task_type = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for taskType.  
  
### getTextTemplate()
    
    
    public abstract String getTextTemplate()

Optional. Text template for the input to the model. The template must contain one or more references to fields in the DataObject, e.g.: "Movie Title: {title} ---- Movie Plot: {plot}".

Required when using the text-only path.

`string text_template = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The textTemplate.  
  
### getTextTemplateBytes()
    
    
    public abstract ByteString getTextTemplateBytes()

Optional. Text template for the input to the model. The template must contain one or more references to fields in the DataObject, e.g.: "Movie Title: {title} ---- Movie Plot: {plot}".

Required when using the text-only path.

`string text_template = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for textTemplate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
