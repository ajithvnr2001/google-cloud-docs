---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunk.RetrievedContextOrBuilder
title: Interface GroundingChunk.RetrievedContextOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:08.492924+00:00
---

# Interface GroundingChunk.RetrievedContextOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunk.RetrievedContextOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GroundingChunk.RetrievedContextOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface GroundingChunk.RetrievedContextOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContextDetailsCase()
    
    
    public abstract GroundingChunk.RetrievedContext.ContextDetailsCase getContextDetailsCase()

**Returns**  
---  
**Type** | **Description**  
`[GroundingChunk.RetrievedContext.ContextDetailsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GroundingChunk.RetrievedContext.ContextDetailsCase)` |   
  
### getDocumentName()
    
    
    public abstract String getDocumentName()

Output only. The full document name for the referenced Vertex AI Search document.

`optional string document_name = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The documentName.  
  
### getDocumentNameBytes()
    
    
    public abstract ByteString getDocumentNameBytes()

Output only. The full document name for the referenced Vertex AI Search document.

`optional string document_name = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for documentName.  
  
### getRagChunk()
    
    
    public abstract RagChunk getRagChunk()

Additional context for the RAG retrieval result. This is only populated when using the RAG retrieval tool.

`.google.cloud.aiplatform.v1.RagChunk rag_chunk = 4;`

**Returns**  
---  
**Type** | **Description**  
`[RagChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagChunk)` | The ragChunk.  
  
### getRagChunkOrBuilder()
    
    
    public abstract RagChunkOrBuilder getRagChunkOrBuilder()

Additional context for the RAG retrieval result. This is only populated when using the RAG retrieval tool.

`.google.cloud.aiplatform.v1.RagChunk rag_chunk = 4;`

**Returns**  
---  
**Type** | **Description**  
`[RagChunkOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RagChunkOrBuilder)` |   
  
### getText()
    
    
    public abstract String getText()

Text of the attribution.

`optional string text = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public abstract ByteString getTextBytes()

Text of the attribution.

`optional string text = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getTitle()
    
    
    public abstract String getTitle()

Title of the attribution.

`optional string title = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public abstract ByteString getTitleBytes()

Title of the attribution.

`optional string title = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### getUri()
    
    
    public abstract String getUri()

URI reference of the attribution.

`optional string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

URI reference of the attribution.

`optional string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasDocumentName()
    
    
    public abstract boolean hasDocumentName()

Output only. The full document name for the referenced Vertex AI Search document.

`optional string document_name = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentName field is set.  
  
### hasRagChunk()
    
    
    public abstract boolean hasRagChunk()

Additional context for the RAG retrieval result. This is only populated when using the RAG retrieval tool.

`.google.cloud.aiplatform.v1.RagChunk rag_chunk = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ragChunk field is set.  
  
### hasText()
    
    
    public abstract boolean hasText()

Text of the attribution.

`optional string text = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
### hasTitle()
    
    
    public abstract boolean hasTitle()

Title of the attribution.

`optional string title = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the title field is set.  
  
### hasUri()
    
    
    public abstract boolean hasUri()

URI reference of the attribution.

`optional string uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
