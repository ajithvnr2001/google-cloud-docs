---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeStub
title: Class DeveloperKnowledgeGrpc.DeveloperKnowledgeStub (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:12.993114+00:00
---

# Class DeveloperKnowledgeGrpc.DeveloperKnowledgeStub (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeveloperKnowledgeGrpc.DeveloperKnowledgeStub (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public static final class DeveloperKnowledgeGrpc.DeveloperKnowledgeStub extends AbstractAsyncStub<DeveloperKnowledgeGrpc.DeveloperKnowledgeStub>

A stub to allow clients to do asynchronous rpc calls to service DeveloperKnowledge.

The Developer Knowledge API provides programmatic access to Google's public developer documentation, enabling you to integrate this knowledge base into your own applications and workflows. The API is designed to be the canonical source for machine-readable access to Google's developer documentation. A typical use case is to first use DeveloperKnowledge.SearchDocumentChunks to find relevant page URIs based on a query, and then use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full content of the top results. All document content is provided in Markdown format.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > DeveloperKnowledgeGrpc.DeveloperKnowledgeStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### answerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)
    
    
    public void answerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)

Answers a query using grounded generation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryResponse)>`  
  
  
### batchGetDocuments(BatchGetDocumentsRequest request, StreamObserver<BatchGetDocumentsResponse> responseObserver)
    
    
    public void batchGetDocuments(BatchGetDocumentsRequest request, StreamObserver<BatchGetDocumentsResponse> responseObserver)

Retrieves multiple documents, each with its full Markdown content.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchGetDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsResponse)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected DeveloperKnowledgeGrpc.DeveloperKnowledgeStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeGrpc.DeveloperKnowledgeStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeGrpc.DeveloperKnowledgeStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### getDocument(GetDocumentRequest request, StreamObserver<Document> responseObserver)
    
    
    public void getDocument(GetDocumentRequest request, StreamObserver<Document> responseObserver)

Retrieves a single document with its full Markdown content.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.GetDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)>`  
  
  
### searchDocumentChunks(SearchDocumentChunksRequest request, StreamObserver<SearchDocumentChunksResponse> responseObserver)
    
    
    public void searchDocumentChunks(SearchDocumentChunksRequest request, StreamObserver<SearchDocumentChunksResponse> responseObserver)

Searches for developer knowledge across Google's developer documentation. Returns DocumentChunks based on the user's query. There may be many chunks from the same Document. To retrieve full documents, use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments with the DocumentChunk.parent returned in the SearchDocumentChunksResponse.results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchDocumentChunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchDocumentChunksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
