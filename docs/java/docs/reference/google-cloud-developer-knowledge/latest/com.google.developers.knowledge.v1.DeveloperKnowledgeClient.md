---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient
title: Class DeveloperKnowledgeClient (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:05.012399+00:00
---

# Class DeveloperKnowledgeClient (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeveloperKnowledgeClient (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-developerknowledge/google-cloud-developer-knowledge/src/main/java/com/google/developers/knowledge/v1/DeveloperKnowledgeClient.java)| [Product Reference](https://developers.google.com/knowledge)  
---|---  
  
Service Description: The Developer Knowledge API provides programmatic access to Google's public developer documentation, enabling you to integrate this knowledge base into your own applications and workflows.

The API is designed to be the canonical source for machine-readable access to Google's developer documentation.

A typical use case is to first use DeveloperKnowledge.SearchDocumentChunks to find relevant page URIs based on a query, and then use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments to fetch the full content of the top results.

All document content is provided in Markdown format.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       DocumentName name = DocumentName.of("[DOCUMENT]");
       Document response = developerKnowledgeClient.getDocument(name);
     }
     

Note: close() needs to be called on the DeveloperKnowledgeClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
SearchDocumentChunks |  Searches for developer knowledge across Google's developer documentation. Returns DocumentChunks based on the user's query. There may be many chunks from the same Document. To retrieve full documents, use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments with the DocumentChunk.parent returned in the SearchDocumentChunksResponse.results. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchDocumentChunks(SearchDocumentChunksRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchDocumentChunksPagedCallable() 
  * searchDocumentChunksCallable() 

  
GetDocument |  Retrieves a single document with its full Markdown content. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDocument(GetDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDocument(DocumentName name) 
  * getDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDocumentCallable() 

  
BatchGetDocuments |  Retrieves multiple documents, each with its full Markdown content. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchGetDocuments(BatchGetDocumentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchGetDocumentsCallable() 

  
AnswerQuery |  Answers a query using grounded generation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * answerQuery(AnswerQueryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * answerQueryCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DeveloperKnowledgeSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeveloperKnowledgeSettings developerKnowledgeSettings =
         DeveloperKnowledgeSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeveloperKnowledgeClient developerKnowledgeClient =
         DeveloperKnowledgeClient.create(developerKnowledgeSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeveloperKnowledgeSettings developerKnowledgeSettings =
         DeveloperKnowledgeSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeveloperKnowledgeClient developerKnowledgeClient =
         DeveloperKnowledgeClient.create(developerKnowledgeSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeveloperKnowledgeSettings developerKnowledgeSettings =
         DeveloperKnowledgeSettings.newHttpJsonBuilder().build();
     DeveloperKnowledgeClient developerKnowledgeClient =
         DeveloperKnowledgeClient.create(developerKnowledgeSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeveloperKnowledgeClient

## Static Methods 

### create()
    
    
    public static final DeveloperKnowledgeClient create()

Constructs an instance of DeveloperKnowledgeClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeveloperKnowledgeSettings settings)
    
    
    public static final DeveloperKnowledgeClient create(DeveloperKnowledgeSettings settings)

Constructs an instance of DeveloperKnowledgeClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeveloperKnowledgeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeveloperKnowledgeStub stub)
    
    
    public static final DeveloperKnowledgeClient create(DeveloperKnowledgeStub stub)

Constructs an instance of DeveloperKnowledgeClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeveloperKnowledgeSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeveloperKnowledgeStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.stub.DeveloperKnowledgeStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient)` |   
  
## Constructors 

### DeveloperKnowledgeClient(DeveloperKnowledgeSettings settings)
    
    
    protected DeveloperKnowledgeClient(DeveloperKnowledgeSettings settings)

Constructs an instance of DeveloperKnowledgeClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeveloperKnowledgeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeSettings)`  
  
  
### DeveloperKnowledgeClient(DeveloperKnowledgeStub stub)
    
    
    protected DeveloperKnowledgeClient(DeveloperKnowledgeStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeveloperKnowledgeStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.stub.DeveloperKnowledgeStub)`  
  
  
## Methods 

### answerQuery(AnswerQueryRequest request)
    
    
    public final AnswerQueryResponse answerQuery(AnswerQueryRequest request)

Answers a query using grounded generation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       AnswerQueryRequest request =
           AnswerQueryRequest.newBuilder().setQuery("query107944136").build();
       AnswerQueryResponse response = developerKnowledgeClient.answerQuery(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryResponse)` |   
  
### answerQueryCallable()
    
    
    public final UnaryCallable<AnswerQueryRequest,AnswerQueryResponse> answerQueryCallable()

Answers a query using grounded generation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       AnswerQueryRequest request =
           AnswerQueryRequest.newBuilder().setQuery("query107944136").build();
       ApiFuture<AnswerQueryResponse> future =
           developerKnowledgeClient.answerQueryCallable().futureCall(request);
       // Do something.
       AnswerQueryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryRequest),[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.AnswerQueryResponse)>` |   
  
### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### batchGetDocuments(BatchGetDocumentsRequest request)
    
    
    public final BatchGetDocumentsResponse batchGetDocuments(BatchGetDocumentsRequest request)

Retrieves multiple documents, each with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       BatchGetDocumentsRequest request =
           BatchGetDocumentsRequest.newBuilder()
               .addAllNames(new ArrayList<String>())
               .setView(DocumentView.forNumber(0))
               .build();
       BatchGetDocumentsResponse response = developerKnowledgeClient.batchGetDocuments(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsResponse)` |   
  
### batchGetDocumentsCallable()
    
    
    public final UnaryCallable<BatchGetDocumentsRequest,BatchGetDocumentsResponse> batchGetDocumentsCallable()

Retrieves multiple documents, each with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       BatchGetDocumentsRequest request =
           BatchGetDocumentsRequest.newBuilder()
               .addAllNames(new ArrayList<String>())
               .setView(DocumentView.forNumber(0))
               .build();
       ApiFuture<BatchGetDocumentsResponse> future =
           developerKnowledgeClient.batchGetDocumentsCallable().futureCall(request);
       // Do something.
       BatchGetDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchGetDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsRequest),[BatchGetDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.BatchGetDocumentsResponse)>` |   
  
### close()
    
    
    public final void close()

### getDocument(@Nullable DocumentName name)
    
    
    public final Document getDocument(@Nullable DocumentName name)

Retrieves a single document with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       DocumentName name = DocumentName.of("[DOCUMENT]");
       Document response = developerKnowledgeClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.developers.knowledge.v1.DocumentName`  
Required. Specifies the name of the document to retrieve. Format: `documents/{uri_without_scheme}` Example: `documents/docs.cloud.google.com/storage/docs/creating-buckets`  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)` |   
  
### getDocument(GetDocumentRequest request)
    
    
    public final Document getDocument(GetDocumentRequest request)

Retrieves a single document with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(DocumentName.of("[DOCUMENT]").toString())
               .setView(DocumentView.forNumber(0))
               .build();
       Document response = developerKnowledgeClient.getDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)` |   
  
### getDocument(String name)
    
    
    public final Document getDocument(String name)

Retrieves a single document with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       String name = DocumentName.of("[DOCUMENT]").toString();
       Document response = developerKnowledgeClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Specifies the name of the document to retrieve. Format: `documents/{uri_without_scheme}` Example: `documents/docs.cloud.google.com/storage/docs/creating-buckets`  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)` |   
  
### getDocumentCallable()
    
    
    public final UnaryCallable<GetDocumentRequest,Document> getDocumentCallable()

Retrieves a single document with its full Markdown content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(DocumentName.of("[DOCUMENT]").toString())
               .setView(DocumentView.forNumber(0))
               .build();
       ApiFuture<Document> future =
           developerKnowledgeClient.getDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.GetDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.Document)>` |   
  
### getSettings()
    
    
    public final @Nullable DeveloperKnowledgeSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.developers.knowledge.v1.DeveloperKnowledgeSettings` |   
  
### getStub()
    
    
    public DeveloperKnowledgeStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.stub.DeveloperKnowledgeStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### searchDocumentChunks(SearchDocumentChunksRequest request)
    
    
    public final DeveloperKnowledgeClient.SearchDocumentChunksPagedResponse searchDocumentChunks(SearchDocumentChunksRequest request)

Searches for developer knowledge across Google's developer documentation. Returns DocumentChunks based on the user's query. There may be many chunks from the same Document. To retrieve full documents, use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments with the DocumentChunk.parent returned in the SearchDocumentChunksResponse.results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       SearchDocumentChunksRequest request =
           SearchDocumentChunksRequest.newBuilder()
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DocumentChunk element :
           developerKnowledgeClient.searchDocumentChunks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDocumentChunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeveloperKnowledgeClient.SearchDocumentChunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient.SearchDocumentChunksPagedResponse)` |   
  
### searchDocumentChunksCallable()
    
    
    public final UnaryCallable<SearchDocumentChunksRequest,SearchDocumentChunksResponse> searchDocumentChunksCallable()

Searches for developer knowledge across Google's developer documentation. Returns DocumentChunks based on the user's query. There may be many chunks from the same Document. To retrieve full documents, use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments with the DocumentChunk.parent returned in the SearchDocumentChunksResponse.results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       SearchDocumentChunksRequest request =
           SearchDocumentChunksRequest.newBuilder()
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         SearchDocumentChunksResponse response =
             developerKnowledgeClient.searchDocumentChunksCallable().call(request);
         for (DocumentChunk element : response.getResultsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDocumentChunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequest),[SearchDocumentChunksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksResponse)>` |   
  
### searchDocumentChunksPagedCallable()
    
    
    public final UnaryCallable<SearchDocumentChunksRequest,DeveloperKnowledgeClient.SearchDocumentChunksPagedResponse> searchDocumentChunksPagedCallable()

Searches for developer knowledge across Google's developer documentation. Returns DocumentChunks based on the user's query. There may be many chunks from the same Document. To retrieve full documents, use DeveloperKnowledge.GetDocument or DeveloperKnowledge.BatchGetDocuments with the DocumentChunk.parent returned in the SearchDocumentChunksResponse.results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeveloperKnowledgeClient developerKnowledgeClient = DeveloperKnowledgeClient.create()) {
       SearchDocumentChunksRequest request =
           SearchDocumentChunksRequest.newBuilder()
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DocumentChunk> future =
           developerKnowledgeClient.searchDocumentChunksPagedCallable().futureCall(request);
       // Do something.
       for (DocumentChunk element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDocumentChunksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequest),[SearchDocumentChunksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.DeveloperKnowledgeClient.SearchDocumentChunksPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
