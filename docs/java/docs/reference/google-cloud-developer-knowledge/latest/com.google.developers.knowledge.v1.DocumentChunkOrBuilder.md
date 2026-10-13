---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentChunkOrBuilder
title: Interface DocumentChunkOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:11.929509+00:00
---

# Interface DocumentChunkOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentChunkOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DocumentChunkOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public interface DocumentChunkOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContent()
    
    
    public abstract String getContent()

Output only. Contains the content of the document chunk.

`string content = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The content.  
  
### getContentBytes()
    
    
    public abstract ByteString getContentBytes()

Output only. Contains the content of the document chunk.

`string content = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for content.  
  
### getDocument()
    
    
    public abstract Document getDocument()

Output only. Represents metadata about the Document this chunk is from. The DocumentView of this Document message will be set to `DOCUMENT_VIEW_BASIC`. It is included here for convenience so that clients do not need to call DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments if they only need the metadata fields. Otherwise, clients should use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full document content.

` .google.developers.knowledge.v1.Document document = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)` | The document.  
  
### getDocumentOrBuilder()
    
    
    public abstract DocumentOrBuilder getDocumentOrBuilder()

Output only. Represents metadata about the Document this chunk is from. The DocumentView of this Document message will be set to `DOCUMENT_VIEW_BASIC`. It is included here for convenience so that clients do not need to call DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments if they only need the metadata fields. Otherwise, clients should use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full document content.

` .google.developers.knowledge.v1.Document document = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentOrBuilder)` |   
  
### getId()
    
    
    public abstract String getId()

Output only. Specifies the ID of this chunk within the document. The chunk ID is unique within a document, but not globally unique across documents. The chunk ID is not stable and may change over time.

`string id = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. Specifies the ID of this chunk within the document. The chunk ID is unique within a document, but not globally unique across documents. The chunk ID is not stable and may change over time.

`string id = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getParent()
    
    
    public abstract String getParent()

Output only. Contains the resource name of the document this chunk is from. Format: `documents/{uri_without_scheme}` Example: `documents/docs.cloud.google.com/storage/docs/creating-buckets`

` string parent = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Output only. Contains the resource name of the document this chunk is from. Format: `documents/{uri_without_scheme}` Example: `documents/docs.cloud.google.com/storage/docs/creating-buckets`

` string parent = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasDocument()
    
    
    public abstract boolean hasDocument()

Output only. Represents metadata about the Document this chunk is from. The DocumentView of this Document message will be set to `DOCUMENT_VIEW_BASIC`. It is included here for convenience so that clients do not need to call DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments if they only need the metadata fields. Otherwise, clients should use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full document content.

` .google.developers.knowledge.v1.Document document = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the document field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
