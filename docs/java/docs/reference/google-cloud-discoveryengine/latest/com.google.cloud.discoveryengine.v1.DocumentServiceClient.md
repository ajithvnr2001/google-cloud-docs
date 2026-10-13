---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient
title: Class DocumentServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:38.827080+00:00
---

# Class DocumentServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/DocumentServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for ingesting Document information of the customer's website.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDataStoreBranchDocumentName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
       Document response = documentServiceClient.getDocument(name);
     }
     

Note: close() needs to be called on the DocumentServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDocument |  Gets a Document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDocument(GetDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDocument(DocumentName name) 
  * getDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDocumentCallable() 

  
ListDocuments |  Gets a list of Documents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDocuments(ListDocumentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDocuments(BranchName parent) 
  * listDocuments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDocumentsPagedCallable() 
  * listDocumentsCallable() 

  
CreateDocument |  Creates a Document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDocument(CreateDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDocument(BranchName parent, Document document, String documentId) 
  * createDocument(String parent, Document document, String documentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDocumentCallable() 

  
UpdateDocument |  Updates a Document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDocument(UpdateDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDocument(Document document, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDocumentCallable() 

  
DeleteDocument |  Deletes a Document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDocument(DeleteDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDocument(DocumentName name) 
  * deleteDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDocumentCallable() 

  
ImportDocuments |  Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created.  Note: It is possible for a subset of the Documents to be successfully updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDocumentsAsync(ImportDocumentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDocumentsOperationCallable() 
  * importDocumentsCallable() 

  
PurgeDocuments |  Permanently deletes all selected Documents in a branch.  This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments.  To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeDocumentsAsync(PurgeDocumentsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeDocumentsOperationCallable() 
  * purgeDocumentsCallable() 

  
BatchGetDocumentsMetadata |  Gets index freshness metadata for Documents. Supported for website search only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchGetDocumentsMetadata(BatchGetDocumentsMetadataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchGetDocumentsMetadata(BranchName parent) 
  * batchGetDocumentsMetadata(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchGetDocumentsMetadataCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DocumentServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentServiceSettings documentServiceSettings =
         DocumentServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DocumentServiceClient documentServiceClient =
         DocumentServiceClient.create(documentServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentServiceSettings documentServiceSettings =
         DocumentServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DocumentServiceClient documentServiceClient =
         DocumentServiceClient.create(documentServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentServiceSettings documentServiceSettings =
         DocumentServiceSettings.newHttpJsonBuilder().build();
     DocumentServiceClient documentServiceClient =
         DocumentServiceClient.create(documentServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentServiceClient

## Static Methods 

### create()
    
    
    public static final DocumentServiceClient create()

Constructs an instance of DocumentServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentServiceSettings settings)
    
    
    public static final DocumentServiceClient create(DocumentServiceSettings settings)

Constructs an instance of DocumentServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentServiceStub stub)
    
    
    public static final DocumentServiceClient create(DocumentServiceStub stub)

Constructs an instance of DocumentServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DocumentServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DocumentServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient)` |   
  
## Constructors 

### DocumentServiceClient(DocumentServiceSettings settings)
    
    
    protected DocumentServiceClient(DocumentServiceSettings settings)

Constructs an instance of DocumentServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceSettings)`  
  
  
### DocumentServiceClient(DocumentServiceStub stub)
    
    
    protected DocumentServiceClient(DocumentServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DocumentServiceStub)`  
  
  
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
  
### batchGetDocumentsMetadata(@Nullable BranchName parent)
    
    
    public final BatchGetDocumentsMetadataResponse batchGetDocumentsMetadata(@Nullable BranchName parent)

Gets index freshness metadata for Documents. Supported for website search only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       BranchName parent =
           BranchName.ofProjectLocationDataStoreBranchName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
       BatchGetDocumentsMetadataResponse response =
           documentServiceClient.batchGetDocumentsMetadata(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.BranchName`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse)` |   
  
### batchGetDocumentsMetadata(BatchGetDocumentsMetadataRequest request)
    
    
    public final BatchGetDocumentsMetadataResponse batchGetDocumentsMetadata(BatchGetDocumentsMetadataRequest request)

Gets index freshness metadata for Documents. Supported for website search only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       BatchGetDocumentsMetadataRequest request =
           BatchGetDocumentsMetadataRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setMatcher(BatchGetDocumentsMetadataRequest.Matcher.newBuilder().build())
               .build();
       BatchGetDocumentsMetadataResponse response =
           documentServiceClient.batchGetDocumentsMetadata(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse)` |   
  
### batchGetDocumentsMetadata(String parent)
    
    
    public final BatchGetDocumentsMetadataResponse batchGetDocumentsMetadata(String parent)

Gets index freshness metadata for Documents. Supported for website search only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String parent =
           BranchName.ofProjectLocationDataStoreBranchName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
               .toString();
       BatchGetDocumentsMetadataResponse response =
           documentServiceClient.batchGetDocumentsMetadata(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse)` |   
  
### batchGetDocumentsMetadataCallable()
    
    
    public final UnaryCallable<BatchGetDocumentsMetadataRequest,BatchGetDocumentsMetadataResponse> batchGetDocumentsMetadataCallable()

Gets index freshness metadata for Documents. Supported for website search only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       BatchGetDocumentsMetadataRequest request =
           BatchGetDocumentsMetadataRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setMatcher(BatchGetDocumentsMetadataRequest.Matcher.newBuilder().build())
               .build();
       ApiFuture<BatchGetDocumentsMetadataResponse> future =
           documentServiceClient.batchGetDocumentsMetadataCallable().futureCall(request);
       // Do something.
       BatchGetDocumentsMetadataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest),[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse)>` |   
  
### close()
    
    
    public final void close()

### createDocument(@Nullable BranchName parent, Document document, String documentId)
    
    
    public final Document createDocument(@Nullable BranchName parent, Document document, String documentId)

Creates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       BranchName parent =
           BranchName.ofProjectLocationDataStoreBranchName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
       Document document = Document.newBuilder().build();
       String documentId = "documentId-814940266";
       Document response = documentServiceClient.createDocument(parent, document, documentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.BranchName`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)`  
Required. The Document to create.  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Document, which becomes the final component of the Document.name. If the caller does not have permission to create the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all Documents with the same parent. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### createDocument(CreateDocumentRequest request)
    
    
    public final Document createDocument(CreateDocumentRequest request)

Creates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .setDocumentId("documentId-814940266")
               .build();
       Document response = documentServiceClient.createDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### createDocument(String parent, Document document, String documentId)
    
    
    public final Document createDocument(String parent, Document document, String documentId)

Creates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String parent =
           BranchName.ofProjectLocationDataStoreBranchName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
               .toString();
       Document document = Document.newBuilder().build();
       String documentId = "documentId-814940266";
       Document response = documentServiceClient.createDocument(parent, document, documentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)`  
Required. The Document to create.  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Document, which becomes the final component of the Document.name. If the caller does not have permission to create the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all Documents with the same parent. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### createDocumentCallable()
    
    
    public final UnaryCallable<CreateDocumentRequest,Document> createDocumentCallable()

Creates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .setDocumentId("documentId-814940266")
               .build();
       ApiFuture<Document> future =
           documentServiceClient.createDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)>` |   
  
### deleteDocument(@Nullable DocumentName name)
    
    
    public final void deleteDocument(@Nullable DocumentName name)

Deletes a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDataStoreBranchDocumentName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
       documentServiceClient.deleteDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DocumentName`  
Required. Full resource name of Document, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the Document to delete does not exist, a `NOT_FOUND` error is returned.  
  
### deleteDocument(DeleteDocumentRequest request)
    
    
    public final void deleteDocument(DeleteDocumentRequest request)

Deletes a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DeleteDocumentRequest request =
           DeleteDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
                       .toString())
               .build();
       documentServiceClient.deleteDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDocument(String name)
    
    
    public final void deleteDocument(String name)

Deletes a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
               .toString();
       documentServiceClient.deleteDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Document, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the Document to delete does not exist, a `NOT_FOUND` error is returned.  
  
### deleteDocumentCallable()
    
    
    public final UnaryCallable<DeleteDocumentRequest,Empty> deleteDocumentCallable()

Deletes a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DeleteDocumentRequest request =
           DeleteDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<Empty> future = documentServiceClient.deleteDocumentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDocumentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDocument(@Nullable DocumentName name)
    
    
    public final Document getDocument(@Nullable DocumentName name)

Gets a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDataStoreBranchDocumentName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
       Document response = documentServiceClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DocumentName`  
Required. Full resource name of Document, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested Document does not exist, a `NOT_FOUND` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### getDocument(GetDocumentRequest request)
    
    
    public final Document getDocument(GetDocumentRequest request)

Gets a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
                       .toString())
               .build();
       Document response = documentServiceClient.getDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### getDocument(String name)
    
    
    public final Document getDocument(String name)

Gets a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
               .toString();
       Document response = documentServiceClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Document, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested Document does not exist, a `NOT_FOUND` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### getDocumentCallable()
    
    
    public final UnaryCallable<GetDocumentRequest,Document> getDocumentCallable()

Gets a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       GetDocumentRequest request =
           GetDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDataStoreBranchDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]")
                       .toString())
               .build();
       ApiFuture<Document> future = documentServiceClient.getDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DocumentServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DocumentServiceSettings` |   
  
### getStub()
    
    
    public DocumentServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DocumentServiceStub)` |   
  
### importDocumentsAsync(ImportDocumentsRequest request)
    
    
    public final OperationFuture<ImportDocumentsResponse,ImportDocumentsMetadata> importDocumentsAsync(ImportDocumentsRequest request)

Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the Documents to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutoGenerateIds(true)
               .setIdField("idField1629396127")
               .setForceRefreshContent(true)
               .build();
       ImportDocumentsResponse response = documentServiceClient.importDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsMetadata)>` |   
  
### importDocumentsCallable()
    
    
    public final UnaryCallable<ImportDocumentsRequest,Operation> importDocumentsCallable()

Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the Documents to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutoGenerateIds(true)
               .setIdField("idField1629396127")
               .setForceRefreshContent(true)
               .build();
       ApiFuture<Operation> future =
           documentServiceClient.importDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDocumentsOperationCallable()
    
    
    public final OperationCallable<ImportDocumentsRequest,ImportDocumentsResponse,ImportDocumentsMetadata> importDocumentsOperationCallable()

Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the Documents to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAutoGenerateIds(true)
               .setIdField("idField1629396127")
               .setForceRefreshContent(true)
               .build();
       OperationFuture<ImportDocumentsResponse, ImportDocumentsMetadata> future =
           documentServiceClient.importDocumentsOperationCallable().futureCall(request);
       // Do something.
       ImportDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest),[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsMetadata)>` |   
  
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
  
### listDocuments(@Nullable BranchName parent)
    
    
    public final DocumentServiceClient.ListDocumentsPagedResponse listDocuments(@Nullable BranchName parent)

Gets a list of Documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       BranchName parent =
           BranchName.ofProjectLocationDataStoreBranchName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
       for (Document element : documentServiceClient.listDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.BranchName`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list Documents under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.ListDocumentsPagedResponse)` |   
  
### listDocuments(ListDocumentsRequest request)
    
    
    public final DocumentServiceClient.ListDocumentsPagedResponse listDocuments(ListDocumentsRequest request)

Gets a list of Documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Document element : documentServiceClient.listDocuments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.ListDocumentsPagedResponse)` |   
  
### listDocuments(String parent)
    
    
    public final DocumentServiceClient.ListDocumentsPagedResponse listDocuments(String parent)

Gets a list of Documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String parent =
           BranchName.ofProjectLocationDataStoreBranchName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
               .toString();
       for (Document element : documentServiceClient.listDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list Documents under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.ListDocumentsPagedResponse)` |   
  
### listDocumentsCallable()
    
    
    public final UnaryCallable<ListDocumentsRequest,ListDocumentsResponse> listDocumentsCallable()

Gets a list of Documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDocumentsResponse response =
             documentServiceClient.listDocumentsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDocumentsRequest),[ListDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDocumentsResponse)>` |   
  
### listDocumentsPagedCallable()
    
    
    public final UnaryCallable<ListDocumentsRequest,DocumentServiceClient.ListDocumentsPagedResponse> listDocumentsPagedCallable()

Gets a list of Documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       ListDocumentsRequest request =
           ListDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Document> future =
           documentServiceClient.listDocumentsPagedCallable().futureCall(request);
       // Do something.
       for (Document element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDocumentsRequest),[ListDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.ListDocumentsPagedResponse)>` |   
  
### purgeDocumentsAsync(PurgeDocumentsRequest request)
    
    
    public final OperationFuture<PurgeDocumentsResponse,PurgeDocumentsMetadata> purgeDocumentsAsync(PurgeDocumentsRequest request)

Permanently deletes all selected Documents in a branch.

This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments.

To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       PurgeDocumentsRequest request =
           PurgeDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setFilter("filter-1274492040")
               .setErrorConfig(PurgeErrorConfig.newBuilder().build())
               .setForce(true)
               .build();
       PurgeDocumentsResponse response = documentServiceClient.purgeDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsResponse),[PurgeDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsMetadata)>` |   
  
### purgeDocumentsCallable()
    
    
    public final UnaryCallable<PurgeDocumentsRequest,Operation> purgeDocumentsCallable()

Permanently deletes all selected Documents in a branch.

This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments.

To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       PurgeDocumentsRequest request =
           PurgeDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setFilter("filter-1274492040")
               .setErrorConfig(PurgeErrorConfig.newBuilder().build())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           documentServiceClient.purgeDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeDocumentsOperationCallable()
    
    
    public final OperationCallable<PurgeDocumentsRequest,PurgeDocumentsResponse,PurgeDocumentsMetadata> purgeDocumentsOperationCallable()

Permanently deletes all selected Documents in a branch.

This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments.

To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       PurgeDocumentsRequest request =
           PurgeDocumentsRequest.newBuilder()
               .setParent(
                   BranchName.ofProjectLocationDataStoreBranchName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                       .toString())
               .setFilter("filter-1274492040")
               .setErrorConfig(PurgeErrorConfig.newBuilder().build())
               .setForce(true)
               .build();
       OperationFuture<PurgeDocumentsResponse, PurgeDocumentsMetadata> future =
           documentServiceClient.purgeDocumentsOperationCallable().futureCall(request);
       // Do something.
       PurgeDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest),[PurgeDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsResponse),[PurgeDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDocument(Document document, FieldMask updateMask)
    
    
    public final Document updateDocument(Document document, FieldMask updateMask)

Updates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       Document document = Document.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Document response = documentServiceClient.updateDocument(document, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)`  
Required. The document to update/create. If the caller does not have permission to update the Document, regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the Document to update does not exist and allow_missing is not set, a `NOT_FOUND` error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### updateDocument(UpdateDocumentRequest request)
    
    
    public final Document updateDocument(UpdateDocumentRequest request)

Updates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setAllowMissing(true)
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Document response = documentServiceClient.updateDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)` |   
  
### updateDocumentCallable()
    
    
    public final UnaryCallable<UpdateDocumentRequest,Document> updateDocumentCallable()

Updates a Document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setAllowMissing(true)
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Document> future =
           documentServiceClient.updateDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Document)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
