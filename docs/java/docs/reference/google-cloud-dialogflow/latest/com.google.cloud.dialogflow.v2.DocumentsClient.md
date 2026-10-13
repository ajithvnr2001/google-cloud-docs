---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient
title: Class DocumentsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:37.129761+00:00
---

# Class DocumentsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/DocumentsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing knowledge Documents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DocumentName name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
               "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]");
       Document response = documentsClient.getDocument(name);
     }
     

Note: close() needs to be called on the DocumentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListDocuments |  Returns the list of all documents of the knowledge base. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDocuments(ListDocumentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDocuments(KnowledgeBaseName parent) 
  * listDocuments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDocumentsPagedCallable() 
  * listDocumentsCallable() 

  
GetDocument |  Retrieves the specified document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDocument(GetDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDocument(DocumentName name) 
  * getDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDocumentCallable() 

  
CreateDocument |  Creates a new document.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: Document |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDocumentAsync(CreateDocumentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDocumentAsync(KnowledgeBaseName parent, Document document) 
  * createDocumentAsync(String parent, Document document) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDocumentOperationCallable() 
  * createDocumentCallable() 

  
ImportDocuments |  Creates documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: ImportDocumentsResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDocumentsAsync(ImportDocumentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDocumentsOperationCallable() 
  * importDocumentsCallable() 

  
DeleteDocument |  Deletes the specified document.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDocumentAsync(DeleteDocumentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDocumentAsync(DocumentName name) 
  * deleteDocumentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDocumentOperationCallable() 
  * deleteDocumentCallable() 

  
UpdateDocument |  Updates the specified document.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: Document |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDocumentAsync(UpdateDocumentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDocumentAsync(Document document, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDocumentOperationCallable() 
  * updateDocumentCallable() 

  
ReloadDocument |  Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: Document Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reloadDocumentAsync(ReloadDocumentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * reloadDocumentAsync(DocumentName name, String contentUri) 
  * reloadDocumentAsync(String name, String contentUri) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reloadDocumentOperationCallable() 
  * reloadDocumentCallable() 

  
ExportDocument |  Exports a smart messaging candidate document into the specified destination.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: KnowledgeOperationMetadata \- `response`: Document |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDocumentAsync(ExportDocumentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDocumentOperationCallable() 
  * exportDocumentCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DocumentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentsSettings documentsSettings =
         DocumentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DocumentsClient documentsClient = DocumentsClient.create(documentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentsSettings documentsSettings =
         DocumentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     DocumentsClient documentsClient = DocumentsClient.create(documentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentsSettings documentsSettings = DocumentsSettings.newHttpJsonBuilder().build();
     DocumentsClient documentsClient = DocumentsClient.create(documentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentsClient

## Static Methods 

### create()
    
    
    public static final DocumentsClient create()

Constructs an instance of DocumentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentsSettings settings)
    
    
    public static final DocumentsClient create(DocumentsSettings settings)

Constructs an instance of DocumentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentsStub stub)
    
    
    public static final DocumentsClient create(DocumentsStub stub)

Constructs an instance of DocumentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(DocumentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.DocumentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient)` |   
  
## Constructors 

### DocumentsClient(DocumentsSettings settings)
    
    
    protected DocumentsClient(DocumentsSettings settings)

Constructs an instance of DocumentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsSettings)`  
  
  
### DocumentsClient(DocumentsStub stub)
    
    
    protected DocumentsClient(DocumentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.DocumentsStub)`  
  
  
## Methods 

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
  
### close()
    
    
    public final void close()

### createDocumentAsync(@Nullable KnowledgeBaseName parent, Document document)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> createDocumentAsync(@Nullable KnowledgeBaseName parent, Document document)

Creates a new document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       KnowledgeBaseName parent =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]");
       Document document = Document.newBuilder().build();
       Document response = documentsClient.createDocumentAsync(parent, document).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.KnowledgeBaseName`  
Required. The knowledge base to create a document for. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)`  
Required. The document to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### createDocumentAsync(CreateDocumentRequest request)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> createDocumentAsync(CreateDocumentRequest request)

Creates a new document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .build();
       Document response = documentsClient.createDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### createDocumentAsync(String parent, Document document)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> createDocumentAsync(String parent, Document document)

Creates a new document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       String parent =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]").toString();
       Document document = Document.newBuilder().build();
       Document response = documentsClient.createDocumentAsync(parent, document).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The knowledge base to create a document for. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)`  
Required. The document to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### createDocumentCallable()
    
    
    public final UnaryCallable<CreateDocumentRequest,Operation> createDocumentCallable()

Creates a new document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .build();
       ApiFuture<Operation> future = documentsClient.createDocumentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDocumentOperationCallable()
    
    
    public final OperationCallable<CreateDocumentRequest,Document,KnowledgeOperationMetadata> createDocumentOperationCallable()

Creates a new document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .build();
       OperationFuture<Document, KnowledgeOperationMetadata> future =
           documentsClient.createDocumentOperationCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### deleteDocumentAsync(@Nullable DocumentName name)
    
    
    public final OperationFuture<Empty,KnowledgeOperationMetadata> deleteDocumentAsync(@Nullable DocumentName name)

Deletes the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DocumentName name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
               "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]");
       documentsClient.deleteDocumentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.DocumentName`  
Required. The name of the document to delete. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### deleteDocumentAsync(DeleteDocumentRequest request)
    
    
    public final OperationFuture<Empty,KnowledgeOperationMetadata> deleteDocumentAsync(DeleteDocumentRequest request)

Deletes the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DeleteDocumentRequest request =
           DeleteDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .build();
       documentsClient.deleteDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### deleteDocumentAsync(String name)
    
    
    public final OperationFuture<Empty,KnowledgeOperationMetadata> deleteDocumentAsync(String name)

Deletes the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       String name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
                   "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
               .toString();
       documentsClient.deleteDocumentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to delete. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### deleteDocumentCallable()
    
    
    public final UnaryCallable<DeleteDocumentRequest,Operation> deleteDocumentCallable()

Deletes the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DeleteDocumentRequest request =
           DeleteDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future = documentsClient.deleteDocumentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDocumentOperationCallable()
    
    
    public final OperationCallable<DeleteDocumentRequest,Empty,KnowledgeOperationMetadata> deleteDocumentOperationCallable()

Deletes the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DeleteDocumentRequest request =
           DeleteDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .build();
       OperationFuture<Empty, KnowledgeOperationMetadata> future =
           documentsClient.deleteDocumentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteDocumentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### exportDocumentAsync(ExportDocumentRequest request)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> exportDocumentAsync(ExportDocumentRequest request)

Exports a smart messaging candidate document into the specified destination.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ExportDocumentRequest request =
           ExportDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setExportFullContent(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       Document response = documentsClient.exportDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ExportDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### exportDocumentCallable()
    
    
    public final UnaryCallable<ExportDocumentRequest,Operation> exportDocumentCallable()

Exports a smart messaging candidate document into the specified destination.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ExportDocumentRequest request =
           ExportDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setExportFullContent(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       ApiFuture<Operation> future = documentsClient.exportDocumentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ExportDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDocumentOperationCallable()
    
    
    public final OperationCallable<ExportDocumentRequest,Document,KnowledgeOperationMetadata> exportDocumentOperationCallable()

Exports a smart messaging candidate document into the specified destination.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ExportDocumentRequest request =
           ExportDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setExportFullContent(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       OperationFuture<Document, KnowledgeOperationMetadata> future =
           documentsClient.exportDocumentOperationCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ExportDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### getDocument(@Nullable DocumentName name)
    
    
    public final Document getDocument(@Nullable DocumentName name)

Retrieves the specified document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DocumentName name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
               "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]");
       Document response = documentsClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.DocumentName`  
Required. The name of the document to retrieve. Format `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)` |   
  
### getDocument(GetDocumentRequest request)
    
    
    public final Document getDocument(GetDocumentRequest request)

Retrieves the specified document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .build();
       Document response = documentsClient.getDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)` |   
  
### getDocument(String name)
    
    
    public final Document getDocument(String name)

Retrieves the specified document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       String name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
                   "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
               .toString();
       Document response = documentsClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to retrieve. Format `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)` |   
  
### getDocumentCallable()
    
    
    public final UnaryCallable<GetDocumentRequest,Document> getDocumentCallable()

Retrieves the specified document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<Document> future = documentsClient.getDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = documentsClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = documentsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DocumentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.DocumentsSettings` |   
  
### getStub()
    
    
    public DocumentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.DocumentsStub)` |   
  
### importDocumentsAsync(ImportDocumentsRequest request)
    
    
    public final OperationFuture<ImportDocumentsResponse,KnowledgeOperationMetadata> importDocumentsAsync(ImportDocumentsRequest request)

Creates documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: ImportDocumentsResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocumentTemplate(ImportDocumentTemplate.newBuilder().build())
               .setImportGcsCustomMetadata(true)
               .build();
       ImportDocumentsResponse response = documentsClient.importDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportDocumentsResponse),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### importDocumentsCallable()
    
    
    public final UnaryCallable<ImportDocumentsRequest,Operation> importDocumentsCallable()

Creates documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: ImportDocumentsResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocumentTemplate(ImportDocumentTemplate.newBuilder().build())
               .setImportGcsCustomMetadata(true)
               .build();
       ApiFuture<Operation> future = documentsClient.importDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDocumentsOperationCallable()
    
    
    public final OperationCallable<ImportDocumentsRequest,ImportDocumentsResponse,KnowledgeOperationMetadata> importDocumentsOperationCallable()

Creates documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: ImportDocumentsResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setDocumentTemplate(ImportDocumentTemplate.newBuilder().build())
               .setImportGcsCustomMetadata(true)
               .build();
       OperationFuture<ImportDocumentsResponse, KnowledgeOperationMetadata> future =
           documentsClient.importDocumentsOperationCallable().futureCall(request);
       // Do something.
       ImportDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportDocumentsRequest),[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportDocumentsResponse),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
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
  
### listDocuments(@Nullable KnowledgeBaseName parent)
    
    
    public final DocumentsClient.ListDocumentsPagedResponse listDocuments(@Nullable KnowledgeBaseName parent)

Returns the list of all documents of the knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       KnowledgeBaseName parent =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]");
       for (Document element : documentsClient.listDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.KnowledgeBaseName`  
Required. The knowledge base to list all documents for. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListDocumentsPagedResponse)` |   
  
### listDocuments(ListDocumentsRequest request)
    
    
    public final DocumentsClient.ListDocumentsPagedResponse listDocuments(ListDocumentsRequest request)

Returns the list of all documents of the knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Document element : documentsClient.listDocuments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListDocumentsPagedResponse)` |   
  
### listDocuments(String parent)
    
    
    public final DocumentsClient.ListDocumentsPagedResponse listDocuments(String parent)

Returns the list of all documents of the knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       String parent =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]").toString();
       for (Document element : documentsClient.listDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The knowledge base to list all documents for. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListDocumentsPagedResponse)` |   
  
### listDocumentsCallable()
    
    
    public final UnaryCallable<ListDocumentsRequest,ListDocumentsResponse> listDocumentsCallable()

Returns the list of all documents of the knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDocumentsResponse response = documentsClient.listDocumentsCallable().call(request);
         for (Document element : response.getDocumentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListDocumentsRequest),[ListDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListDocumentsResponse)>` |   
  
### listDocumentsPagedCallable()
    
    
    public final UnaryCallable<ListDocumentsRequest,DocumentsClient.ListDocumentsPagedResponse> listDocumentsPagedCallable()

Returns the list of all documents of the knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Document> future = documentsClient.listDocumentsPagedCallable().futureCall(request);
       // Do something.
       for (Document element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListDocumentsRequest),[ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListDocumentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DocumentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : documentsClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = documentsClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,DocumentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = documentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.ListLocationsPagedResponse)>` |   
  
### reloadDocumentAsync(@Nullable DocumentName name, String contentUri)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> reloadDocumentAsync(@Nullable DocumentName name, String contentUri)

Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       DocumentName name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
               "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]");
       String contentUri = "contentUri264542771";
       Document response = documentsClient.reloadDocumentAsync(name, contentUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.DocumentName`  
Required. The name of the document to reload. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`  
`contentUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The path of gcs source file for reloading document content. For now, only gcs uri is supported. For documents stored in Google Cloud Storage, these URIs must have the form `gs://<bucket-name>/<object-name>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### reloadDocumentAsync(ReloadDocumentRequest request)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> reloadDocumentAsync(ReloadDocumentRequest request)

Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ReloadDocumentRequest request =
           ReloadDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setImportGcsCustomMetadata(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       Document response = documentsClient.reloadDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReloadDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ReloadDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### reloadDocumentAsync(String name, String contentUri)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> reloadDocumentAsync(String name, String contentUri)

Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       String name =
           DocumentName.ofProjectKnowledgeBaseDocumentName(
                   "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
               .toString();
       String contentUri = "contentUri264542771";
       Document response = documentsClient.reloadDocumentAsync(name, contentUri).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to reload. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`  
`contentUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The path of gcs source file for reloading document content. For now, only gcs uri is supported. For documents stored in Google Cloud Storage, these URIs must have the form `gs://<bucket-name>/<object-name>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### reloadDocumentCallable()
    
    
    public final UnaryCallable<ReloadDocumentRequest,Operation> reloadDocumentCallable()

Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ReloadDocumentRequest request =
           ReloadDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setImportGcsCustomMetadata(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       ApiFuture<Operation> future = documentsClient.reloadDocumentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReloadDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ReloadDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### reloadDocumentOperationCallable()
    
    
    public final OperationCallable<ReloadDocumentRequest,Document,KnowledgeOperationMetadata> reloadDocumentOperationCallable()

Reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       ReloadDocumentRequest request =
           ReloadDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectKnowledgeBaseDocumentName(
                           "[PROJECT]", "[KNOWLEDGE_BASE]", "[DOCUMENT]")
                       .toString())
               .setImportGcsCustomMetadata(true)
               .setSmartMessagingPartialUpdate(true)
               .build();
       OperationFuture<Document, KnowledgeOperationMetadata> future =
           documentsClient.reloadDocumentOperationCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReloadDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ReloadDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDocumentAsync(Document document, FieldMask updateMask)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> updateDocumentAsync(Document document, FieldMask updateMask)

Updates the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       Document document = Document.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Document response = documentsClient.updateDocumentAsync(document, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document)`  
Required. The document to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Not specified means `update all`. Currently, only `display_name` can be updated, an InvalidArgument will be returned for attempting to update other fields.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### updateDocumentAsync(UpdateDocumentRequest request)
    
    
    public final OperationFuture<Document,KnowledgeOperationMetadata> updateDocumentAsync(UpdateDocumentRequest request)

Updates the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Document response = documentsClient.updateDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
### updateDocumentCallable()
    
    
    public final UnaryCallable<UpdateDocumentRequest,Operation> updateDocumentCallable()

Updates the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = documentsClient.updateDocumentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDocumentOperationCallable()
    
    
    public final OperationCallable<UpdateDocumentRequest,Document,KnowledgeOperationMetadata> updateDocumentOperationCallable()

Updates the specified document.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: KnowledgeOperationMetadata \- `response`: Document

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentsClient documentsClient = DocumentsClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Document, KnowledgeOperationMetadata> future =
           documentsClient.updateDocumentOperationCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document),[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
