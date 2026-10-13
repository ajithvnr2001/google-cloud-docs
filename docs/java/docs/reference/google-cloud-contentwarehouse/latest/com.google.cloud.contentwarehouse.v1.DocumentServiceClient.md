---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient
title: Class DocumentServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:47.404831+00:00
---

# Class DocumentServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-contentwarehouse/google-cloud-contentwarehouse/src/main/java/com/google/cloud/contentwarehouse/v1/DocumentServiceClient.java)| [Product Reference](https://cloud.google.com/document-warehouse/docs/overview)  
---|---  
  
Service Description: This service lets you manage document.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Document document = Document.newBuilder().build();
       CreateDocumentResponse response = documentServiceClient.createDocument(parent, document);
     }
     

Note: close() needs to be called on the DocumentServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDocument |  Creates a document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDocument(CreateDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDocument(LocationName parent, Document document) 
  * createDocument(String parent, Document document) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDocumentCallable() 

  
GetDocument |  Gets a document. Returns NOT_FOUND if the document does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDocument(GetDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDocument(DocumentName name) 
  * getDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDocumentCallable() 

  
UpdateDocument |  Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDocument(UpdateDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDocument(DocumentName name, Document document) 
  * updateDocument(String name, Document document) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDocumentCallable() 

  
DeleteDocument |  Deletes a document. Returns NOT_FOUND if the document does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDocument(DeleteDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDocument(DocumentName name) 
  * deleteDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDocumentCallable() 

  
SearchDocuments |  Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchDocuments(SearchDocumentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchDocuments(LocationName parent) 
  * searchDocuments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchDocumentsPagedCallable() 
  * searchDocumentsCallable() 

  
LockDocument |  Lock the document so the document cannot be updated by other users. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lockDocument(LockDocumentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * lockDocument(DocumentName name) 
  * lockDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lockDocumentCallable() 

  
FetchAcl |  Gets the access control policy for a resource. Returns NOT_FOUND error if the resource does not exist. Returns an empty policy if the resource exists but does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchAcl(FetchAclRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchAcl(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchAclCallable() 

  
SetAcl |  Sets the access control policy for a resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setAcl(SetAclRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setAcl(String resource, Policy policy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setAclCallable() 

  
  
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
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient)` |   
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
`settings` | `[DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient)` |   
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
`stub` | `[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient)` |   
  
## Constructors 

### DocumentServiceClient(DocumentServiceSettings settings)
    
    
    protected DocumentServiceClient(DocumentServiceSettings settings)

Constructs an instance of DocumentServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceSettings)`  
  
  
### DocumentServiceClient(DocumentServiceStub stub)
    
    
    protected DocumentServiceClient(DocumentServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentServiceStub)`  
  
  
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

### createDocument(@Nullable LocationName parent, Document document)
    
    
    public final CreateDocumentResponse createDocument(@Nullable LocationName parent, Document document)

Creates a document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Document document = Document.newBuilder().build();
       CreateDocumentResponse response = documentServiceClient.createDocument(parent, document);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)`  
Required. The document to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentResponse)` |   
  
### createDocument(CreateDocumentRequest request)
    
    
    public final CreateDocumentResponse createDocument(CreateDocumentRequest request)

Creates a document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDocument(Document.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setPolicy(Policy.newBuilder().build())
               .setCloudAiDocumentOption(CloudAIDocumentOption.newBuilder().build())
               .setCreateMask(FieldMask.newBuilder().build())
               .build();
       CreateDocumentResponse response = documentServiceClient.createDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentResponse)` |   
  
### createDocument(String parent, Document document)
    
    
    public final CreateDocumentResponse createDocument(String parent, Document document)

Creates a document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Document document = Document.newBuilder().build();
       CreateDocumentResponse response = documentServiceClient.createDocument(parent, document);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)`  
Required. The document to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentResponse)` |   
  
### createDocumentCallable()
    
    
    public final UnaryCallable<CreateDocumentRequest,CreateDocumentResponse> createDocumentCallable()

Creates a document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       CreateDocumentRequest request =
           CreateDocumentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDocument(Document.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setPolicy(Policy.newBuilder().build())
               .setCloudAiDocumentOption(CloudAIDocumentOption.newBuilder().build())
               .setCreateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CreateDocumentResponse> future =
           documentServiceClient.createDocumentCallable().futureCall(request);
       // Do something.
       CreateDocumentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentRequest),[CreateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentResponse)>` |   
  
### deleteDocument(@Nullable DocumentName name)
    
    
    public final void deleteDocument(@Nullable DocumentName name)

Deletes a document. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       documentServiceClient.deleteDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document to delete. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
  
### deleteDocument(DeleteDocumentRequest request)
    
    
    public final void deleteDocument(DeleteDocumentRequest request)

Deletes a document. Returns NOT_FOUND if the document does not exist.

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
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       documentServiceClient.deleteDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDocument(String name)
    
    
    public final void deleteDocument(String name)

Deletes a document. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       documentServiceClient.deleteDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to delete. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
  
### deleteDocumentCallable()
    
    
    public final UnaryCallable<DeleteDocumentRequest,Empty> deleteDocumentCallable()

Deletes a document. Returns NOT_FOUND if the document does not exist.

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
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<Empty> future = documentServiceClient.deleteDocumentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### fetchAcl(FetchAclRequest request)
    
    
    public final FetchAclResponse fetchAcl(FetchAclRequest request)

Gets the access control policy for a resource. Returns NOT_FOUND error if the resource does not exist. Returns an empty policy if the resource exists but does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       FetchAclRequest request =
           FetchAclRequest.newBuilder()
               .setResource("resource-341064690")
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setProjectOwner(true)
               .build();
       FetchAclResponse response = documentServiceClient.fetchAcl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclResponse)` |   
  
### fetchAcl(String resource)
    
    
    public final FetchAclResponse fetchAcl(String resource)

Gets the access control policy for a resource. Returns NOT_FOUND error if the resource does not exist. Returns an empty policy if the resource exists but does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String resource = "resource-341064690";
       FetchAclResponse response = documentServiceClient.fetchAcl(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. REQUIRED: The resource for which the policy is being requested. Format for document: projects/{project_number}/locations/{location}/documents/{document_id}. Format for collection: projects/{project_number}/locations/{location}/collections/{collection_id}. Format for project: projects/{project_number}.  
**Returns**  
---  
**Type** | **Description**  
`[FetchAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclResponse)` |   
  
### fetchAclCallable()
    
    
    public final UnaryCallable<FetchAclRequest,FetchAclResponse> fetchAclCallable()

Gets the access control policy for a resource. Returns NOT_FOUND error if the resource does not exist. Returns an empty policy if the resource exists but does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       FetchAclRequest request =
           FetchAclRequest.newBuilder()
               .setResource("resource-341064690")
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setProjectOwner(true)
               .build();
       ApiFuture<FetchAclResponse> future =
           documentServiceClient.fetchAclCallable().futureCall(request);
       // Do something.
       FetchAclResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclRequest),[FetchAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclResponse)>` |   
  
### getDocument(@Nullable DocumentName name)
    
    
    public final Document getDocument(@Nullable DocumentName name)

Gets a document. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       Document response = documentServiceClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document to retrieve. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### getDocument(GetDocumentRequest request)
    
    
    public final Document getDocument(GetDocumentRequest request)

Gets a document. Returns NOT_FOUND if the document does not exist.

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
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       Document response = documentServiceClient.getDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### getDocument(String name)
    
    
    public final Document getDocument(String name)

Gets a document. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       Document response = documentServiceClient.getDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to retrieve. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### getDocumentCallable()
    
    
    public final UnaryCallable<GetDocumentRequest,Document> getDocumentCallable()

Gets a document. Returns NOT_FOUND if the document does not exist.

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
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<Document> future = documentServiceClient.getDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)>` |   
  
### getSettings()
    
    
    public final @Nullable DocumentServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentServiceSettings` |   
  
### getStub()
    
    
    public DocumentServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentServiceStub)` |   
  
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
  
### lockDocument(@Nullable DocumentName name)
    
    
    public final Document lockDocument(@Nullable DocumentName name)

Lock the document so the document cannot be updated by other users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       Document response = documentServiceClient.lockDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document to lock. Format: projects/{project_number}/locations/{location}/documents/{document}.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### lockDocument(LockDocumentRequest request)
    
    
    public final Document lockDocument(LockDocumentRequest request)

Lock the document so the document cannot be updated by other users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       LockDocumentRequest request =
           LockDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setCollectionId("collectionId1636075609")
               .setLockingUser(UserInfo.newBuilder().build())
               .build();
       Document response = documentServiceClient.lockDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LockDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LockDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### lockDocument(String name)
    
    
    public final Document lockDocument(String name)

Lock the document so the document cannot be updated by other users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       Document response = documentServiceClient.lockDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to lock. Format: projects/{project_number}/locations/{location}/documents/{document}.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)` |   
  
### lockDocumentCallable()
    
    
    public final UnaryCallable<LockDocumentRequest,Document> lockDocumentCallable()

Lock the document so the document cannot be updated by other users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       LockDocumentRequest request =
           LockDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setCollectionId("collectionId1636075609")
               .setLockingUser(UserInfo.newBuilder().build())
               .build();
       ApiFuture<Document> future = documentServiceClient.lockDocumentCallable().futureCall(request);
       // Do something.
       Document response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LockDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LockDocumentRequest),[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)>` |   
  
### searchDocuments(@Nullable LocationName parent)
    
    
    public final DocumentServiceClient.SearchDocumentsPagedResponse searchDocuments(@Nullable LocationName parent)

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SearchDocumentsResponse.MatchingDocument element :
           documentServiceClient.searchDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent, which owns this collection of documents. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse)` |   
  
### searchDocuments(SearchDocumentsRequest request)
    
    
    public final DocumentServiceClient.SearchDocumentsPagedResponse searchDocuments(SearchDocumentsRequest request)

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       SearchDocumentsRequest request =
           SearchDocumentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setDocumentQuery(DocumentQuery.newBuilder().build())
               .setOffset(-1019779949)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .addAllHistogramQueries(new ArrayList<HistogramQuery>())
               .setRequireTotalSize(true)
               .setQaSizeLimit(142059404)
               .build();
       for (SearchDocumentsResponse.MatchingDocument element :
           documentServiceClient.searchDocuments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse)` |   
  
### searchDocuments(String parent)
    
    
    public final DocumentServiceClient.SearchDocumentsPagedResponse searchDocuments(String parent)

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SearchDocumentsResponse.MatchingDocument element :
           documentServiceClient.searchDocuments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of documents. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient.SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse)` |   
  
### searchDocumentsCallable()
    
    
    public final UnaryCallable<SearchDocumentsRequest,SearchDocumentsResponse> searchDocumentsCallable()

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       SearchDocumentsRequest request =
           SearchDocumentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setDocumentQuery(DocumentQuery.newBuilder().build())
               .setOffset(-1019779949)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .addAllHistogramQueries(new ArrayList<HistogramQuery>())
               .setRequireTotalSize(true)
               .setQaSizeLimit(142059404)
               .build();
       while (true) {
         SearchDocumentsResponse response =
             documentServiceClient.searchDocumentsCallable().call(request);
         for (SearchDocumentsResponse.MatchingDocument element :
             response.getMatchingDocumentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest),[SearchDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsResponse)>` |   
  
### searchDocumentsPagedCallable()
    
    
    public final UnaryCallable<SearchDocumentsRequest,DocumentServiceClient.SearchDocumentsPagedResponse> searchDocumentsPagedCallable()

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       SearchDocumentsRequest request =
           SearchDocumentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setDocumentQuery(DocumentQuery.newBuilder().build())
               .setOffset(-1019779949)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .addAllHistogramQueries(new ArrayList<HistogramQuery>())
               .setRequireTotalSize(true)
               .setQaSizeLimit(142059404)
               .build();
       ApiFuture<SearchDocumentsResponse.MatchingDocument> future =
           documentServiceClient.searchDocumentsPagedCallable().futureCall(request);
       // Do something.
       for (SearchDocumentsResponse.MatchingDocument element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest),[SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse)>` |   
  
### setAcl(SetAclRequest request)
    
    
    public final SetAclResponse setAcl(SetAclRequest request)

Sets the access control policy for a resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       SetAclRequest request =
           SetAclRequest.newBuilder()
               .setResource("resource-341064690")
               .setPolicy(Policy.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setProjectOwner(true)
               .build();
       SetAclResponse response = documentServiceClient.setAcl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SetAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclResponse)` |   
  
### setAcl(String resource, Policy policy)
    
    
    public final SetAclResponse setAcl(String resource, Policy policy)

Sets the access control policy for a resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String resource = "resource-341064690";
       Policy policy = Policy.newBuilder().build();
       SetAclResponse response = documentServiceClient.setAcl(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. REQUIRED: The resource for which the policy is being requested. Format for document: projects/{project_number}/locations/{location}/documents/{document_id}. Format for collection: projects/{project_number}/locations/{location}/collections/{collection_id}. Format for project: projects/{project_number}.  
`policy` | `com.google.iam.v1.Policy`  
Required. REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. This refers to an Identity and Access (IAM) policy, which specifies access controls for the Document. You can set ACL with condition for projects only. Supported operators are: `=`, `!=`, `<`, `<=`, `>`, and `>=` where the left of the operator is `DocumentSchemaId` or property name and the right of the operator is a number or a quoted string. You must escape backslash (\\) and quote (") characters. Boolean expressions (AND/OR) are supported up to 3 levels of nesting (for example, "((A AND B AND C) OR D) AND E"), a maximum of 10 comparisons are allowed in the expression. The expression must be < 6000 bytes in length. Sample condition: `"DocumentSchemaId = "some schema id" OR SchemaId.floatPropertyName >= 10"`  
**Returns**  
---  
**Type** | **Description**  
`[SetAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclResponse)` |   
  
### setAclCallable()
    
    
    public final UnaryCallable<SetAclRequest,SetAclResponse> setAclCallable()

Sets the access control policy for a resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       SetAclRequest request =
           SetAclRequest.newBuilder()
               .setResource("resource-341064690")
               .setPolicy(Policy.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setProjectOwner(true)
               .build();
       ApiFuture<SetAclResponse> future = documentServiceClient.setAclCallable().futureCall(request);
       // Do something.
       SetAclResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclRequest),[SetAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDocument(@Nullable DocumentName name, Document document)
    
    
    public final UpdateDocumentResponse updateDocument(@Nullable DocumentName name, Document document)

Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       DocumentName name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       Document document = Document.newBuilder().build();
       UpdateDocumentResponse response = documentServiceClient.updateDocument(name, document);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document to update. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)`  
Required. The document to update.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentResponse)` |   
  
### updateDocument(UpdateDocumentRequest request)
    
    
    public final UpdateDocumentResponse updateDocument(UpdateDocumentRequest request)

Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setCloudAiDocumentOption(CloudAIDocumentOption.newBuilder().build())
               .setUpdateOptions(UpdateOptions.newBuilder().build())
               .build();
       UpdateDocumentResponse response = documentServiceClient.updateDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentResponse)` |   
  
### updateDocument(String name, Document document)
    
    
    public final UpdateDocumentResponse updateDocument(String name, Document document)

Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       String name =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       Document document = Document.newBuilder().build();
       UpdateDocumentResponse response = documentServiceClient.updateDocument(name, document);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document to update. Format: projects/{project_number}/locations/{location}/documents/{document_id} or projects/{project_number}/locations/{location}/documents/referenceId/{reference_id}.  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)`  
Required. The document to update.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentResponse)` |   
  
### updateDocumentCallable()
    
    
    public final UnaryCallable<UpdateDocumentRequest,UpdateDocumentResponse> updateDocumentCallable()

Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
       UpdateDocumentRequest request =
           UpdateDocumentRequest.newBuilder()
               .setName(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setDocument(Document.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .setCloudAiDocumentOption(CloudAIDocumentOption.newBuilder().build())
               .setUpdateOptions(UpdateOptions.newBuilder().build())
               .build();
       ApiFuture<UpdateDocumentResponse> future =
           documentServiceClient.updateDocumentCallable().futureCall(request);
       // Do something.
       UpdateDocumentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentRequest),[UpdateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
