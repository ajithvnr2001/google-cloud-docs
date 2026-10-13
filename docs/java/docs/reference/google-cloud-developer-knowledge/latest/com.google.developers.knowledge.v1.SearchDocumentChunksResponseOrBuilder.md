---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksResponseOrBuilder
title: Interface SearchDocumentChunksResponseOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:12.166367+00:00
---

# Interface SearchDocumentChunksResponseOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchDocumentChunksResponseOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public interface SearchDocumentChunksResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNextPageToken()
    
    
    public abstract String getNextPageToken()

Optional. Provides a token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

Optional. Provides a token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getResults(int index)
    
    
    public abstract DocumentChunk getResults(int index)

Contains the search results for the given query. Each DocumentChunk in this list contains a snippet of content relevant to the search query. Use the DocumentChunk.parent field of each result with DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to retrieve the full document content.

`repeated .google.developers.knowledge.v1.DocumentChunk results = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentChunk)` |   
  
### getResultsCount()
    
    
    public abstract int getResultsCount()

Contains the search results for the given query. Each DocumentChunk in this list contains a snippet of content relevant to the search query. Use the DocumentChunk.parent field of each result with DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to retrieve the full document content.

`repeated .google.developers.knowledge.v1.DocumentChunk results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResultsList()
    
    
    public abstract List<DocumentChunk> getResultsList()

Contains the search results for the given query. Each DocumentChunk in this list contains a snippet of content relevant to the search query. Use the DocumentChunk.parent field of each result with DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to retrieve the full document content.

`repeated .google.developers.knowledge.v1.DocumentChunk results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DocumentChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentChunk)>` |   
  
### getResultsOrBuilder(int index)
    
    
    public abstract DocumentChunkOrBuilder getResultsOrBuilder(int index)

Contains the search results for the given query. Each DocumentChunk in this list contains a snippet of content relevant to the search query. Use the DocumentChunk.parent field of each result with DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to retrieve the full document content.

`repeated .google.developers.knowledge.v1.DocumentChunk results = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentChunkOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DocumentChunkOrBuilder)` |   
  
### getResultsOrBuilderList()
    
    
    public abstract List<? extends DocumentChunkOrBuilder> getResultsOrBuilderList()

Contains the search results for the given query. Each DocumentChunk in this list contains a snippet of content relevant to the search query. Use the DocumentChunk.parent field of each result with DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to retrieve the full document content.

`repeated .google.developers.knowledge.v1.DocumentChunk results = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.developers.knowledge.v1.DocumentChunkOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
