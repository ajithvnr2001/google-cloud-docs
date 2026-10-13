---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc
title: Class DeveloperKnowledgeGrpc (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:12.668463+00:00
---

# Class DeveloperKnowledgeGrpc (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeveloperKnowledgeGrpc (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public final class DeveloperKnowledgeGrpc

The Developer Knowledge API provides programmatic access to Google's public developer documentation, enabling you to integrate this knowledge base into your own applications and workflows. The API is designed to be the canonical source for machine-readable access to Google's developer documentation. A typical use case is to first use DeveloperKnowledge.SearchDocumentChunks to find relevant page URIs based on a query, and then use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full content of the top results. All document content is provided in Markdown format.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeveloperKnowledgeGrpc

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(DeveloperKnowledgeGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(DeveloperKnowledgeGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[DeveloperKnowledgeGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAnswerQueryMethod()
    
    
    public static MethodDescriptor<AnswerQueryRequest,AnswerQueryResponse> getAnswerQueryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryRequest),[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryResponse)>` |   
  
### getBatchGetDocumentsMethod()
    
    
    public static MethodDescriptor<BatchGetDocumentsRequest,BatchGetDocumentsResponse> getBatchGetDocumentsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchGetDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsRequest),[BatchGetDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsResponse)>` |   
  
### getGetDocumentMethod()
    
    
    public static MethodDescriptor<GetDocumentRequest,Document> getGetDocumentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.GetDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)>` |   
  
### getSearchDocumentChunksMethod()
    
    
    public static MethodDescriptor<SearchDocumentChunksRequest,SearchDocumentChunksResponse> getSearchDocumentChunksMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SearchDocumentChunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequest),[SearchDocumentChunksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### newBlockingStub(Channel channel)
    
    
    public static DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static DeveloperKnowledgeGrpc.DeveloperKnowledgeFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeGrpc.DeveloperKnowledgeFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static DeveloperKnowledgeGrpc.DeveloperKnowledgeStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeGrpc.DeveloperKnowledgeStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
