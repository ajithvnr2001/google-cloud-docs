---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient
title: Class DocumentLinkServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:45.974417+00:00
---

# Class DocumentLinkServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentLinkServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-contentwarehouse/google-cloud-contentwarehouse/src/main/java/com/google/cloud/contentwarehouse/v1/DocumentLinkServiceClient.java)| [Product Reference](https://cloud.google.com/document-warehouse/docs/overview)  
---|---  
  
Service Description: This service lets you manage document-links. Document-Links are treated as sub-resources under source documents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DocumentName parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       ListLinkedTargetsResponse response = documentLinkServiceClient.listLinkedTargets(parent);
     }
     

Note: close() needs to be called on the DocumentLinkServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListLinkedTargets |  Return all target document-links from the document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLinkedTargets(ListLinkedTargetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLinkedTargets(DocumentName parent) 
  * listLinkedTargets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLinkedTargetsCallable() 

  
ListLinkedSources |  Return all source document-links from the document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLinkedSources(ListLinkedSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLinkedSources(DocumentName parent) 
  * listLinkedSources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLinkedSourcesPagedCallable() 
  * listLinkedSourcesCallable() 

  
CreateDocumentLink |  Create a link between a source document and a target document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDocumentLink(CreateDocumentLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDocumentLink(DocumentName parent, DocumentLink documentLink) 
  * createDocumentLink(String parent, DocumentLink documentLink) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDocumentLinkCallable() 

  
DeleteDocumentLink |  Remove the link between the source and target documents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDocumentLink(DeleteDocumentLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDocumentLink(DocumentLinkName name) 
  * deleteDocumentLink(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDocumentLinkCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DocumentLinkServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentLinkServiceSettings documentLinkServiceSettings =
         DocumentLinkServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DocumentLinkServiceClient documentLinkServiceClient =
         DocumentLinkServiceClient.create(documentLinkServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentLinkServiceSettings documentLinkServiceSettings =
         DocumentLinkServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DocumentLinkServiceClient documentLinkServiceClient =
         DocumentLinkServiceClient.create(documentLinkServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentLinkServiceSettings documentLinkServiceSettings =
         DocumentLinkServiceSettings.newHttpJsonBuilder().build();
     DocumentLinkServiceClient documentLinkServiceClient =
         DocumentLinkServiceClient.create(documentLinkServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentLinkServiceClient

## Static Methods 

### create()
    
    
    public static final DocumentLinkServiceClient create()

Constructs an instance of DocumentLinkServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentLinkServiceSettings settings)
    
    
    public static final DocumentLinkServiceClient create(DocumentLinkServiceSettings settings)

Constructs an instance of DocumentLinkServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentLinkServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentLinkServiceStub stub)
    
    
    public static final DocumentLinkServiceClient create(DocumentLinkServiceStub stub)

Constructs an instance of DocumentLinkServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DocumentLinkServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentLinkServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentLinkServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient)` |   
  
## Constructors 

### DocumentLinkServiceClient(DocumentLinkServiceSettings settings)
    
    
    protected DocumentLinkServiceClient(DocumentLinkServiceSettings settings)

Constructs an instance of DocumentLinkServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentLinkServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceSettings)`  
  
  
### DocumentLinkServiceClient(DocumentLinkServiceStub stub)
    
    
    protected DocumentLinkServiceClient(DocumentLinkServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentLinkServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentLinkServiceStub)`  
  
  
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

### createDocumentLink(@Nullable DocumentName parent, DocumentLink documentLink)
    
    
    public final DocumentLink createDocumentLink(@Nullable DocumentName parent, DocumentLink documentLink)

Create a link between a source document and a target document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DocumentName parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       DocumentLink documentLink = DocumentLink.newBuilder().build();
       DocumentLink response = documentLinkServiceClient.createDocumentLink(parent, documentLink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. Parent of the document-link to be created. parent of document-link should be a document. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}.  
`documentLink` | `[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)`  
Required. Document links associated with the source documents (source_document_id).  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)` |   
  
### createDocumentLink(CreateDocumentLinkRequest request)
    
    
    public final DocumentLink createDocumentLink(CreateDocumentLinkRequest request)

Create a link between a source document and a target document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       CreateDocumentLinkRequest request =
           CreateDocumentLinkRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setDocumentLink(DocumentLink.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       DocumentLink response = documentLinkServiceClient.createDocumentLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)` |   
  
### createDocumentLink(String parent, DocumentLink documentLink)
    
    
    public final DocumentLink createDocumentLink(String parent, DocumentLink documentLink)

Create a link between a source document and a target document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       String parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       DocumentLink documentLink = DocumentLink.newBuilder().build();
       DocumentLink response = documentLinkServiceClient.createDocumentLink(parent, documentLink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent of the document-link to be created. parent of document-link should be a document. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}.  
`documentLink` | `[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)`  
Required. Document links associated with the source documents (source_document_id).  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)` |   
  
### createDocumentLinkCallable()
    
    
    public final UnaryCallable<CreateDocumentLinkRequest,DocumentLink> createDocumentLinkCallable()

Create a link between a source document and a target document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       CreateDocumentLinkRequest request =
           CreateDocumentLinkRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setDocumentLink(DocumentLink.newBuilder().build())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<DocumentLink> future =
           documentLinkServiceClient.createDocumentLinkCallable().futureCall(request);
       // Do something.
       DocumentLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDocumentLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentLinkRequest),[DocumentLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLink)>` |   
  
### deleteDocumentLink(@Nullable DocumentLinkName name)
    
    
    public final void deleteDocumentLink(@Nullable DocumentLinkName name)

Remove the link between the source and target documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DocumentLinkName name =
           DocumentLinkName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT]", "[DOCUMENT_LINK]");
       documentLinkServiceClient.deleteDocumentLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentLinkName`  
Required. The name of the document-link to be deleted. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}/documentLinks/{document_link_id}.  
  
### deleteDocumentLink(DeleteDocumentLinkRequest request)
    
    
    public final void deleteDocumentLink(DeleteDocumentLinkRequest request)

Remove the link between the source and target documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DeleteDocumentLinkRequest request =
           DeleteDocumentLinkRequest.newBuilder()
               .setName(
                   DocumentLinkName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT]", "[DOCUMENT_LINK]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       documentLinkServiceClient.deleteDocumentLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentLinkRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDocumentLink(String name)
    
    
    public final void deleteDocumentLink(String name)

Remove the link between the source and target documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       String name =
           DocumentLinkName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT]", "[DOCUMENT_LINK]")
               .toString();
       documentLinkServiceClient.deleteDocumentLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document-link to be deleted. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}/documentLinks/{document_link_id}.  
  
### deleteDocumentLinkCallable()
    
    
    public final UnaryCallable<DeleteDocumentLinkRequest,Empty> deleteDocumentLinkCallable()

Remove the link between the source and target documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DeleteDocumentLinkRequest request =
           DeleteDocumentLinkRequest.newBuilder()
               .setName(
                   DocumentLinkName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT]", "[DOCUMENT_LINK]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<Empty> future =
           documentLinkServiceClient.deleteDocumentLinkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDocumentLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentLinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSettings()
    
    
    public final @Nullable DocumentLinkServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentLinkServiceSettings` |   
  
### getStub()
    
    
    public DocumentLinkServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentLinkServiceStub)` |   
  
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
  
### listLinkedSources(@Nullable DocumentName parent)
    
    
    public final DocumentLinkServiceClient.ListLinkedSourcesPagedResponse listLinkedSources(@Nullable DocumentName parent)

Return all source document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DocumentName parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       for (DocumentLink element :
           documentLinkServiceClient.listLinkedSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document, for which all source links are returned. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient.ListLinkedSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient.ListLinkedSourcesPagedResponse)` |   
  
### listLinkedSources(ListLinkedSourcesRequest request)
    
    
    public final DocumentLinkServiceClient.ListLinkedSourcesPagedResponse listLinkedSources(ListLinkedSourcesRequest request)

Return all source document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       ListLinkedSourcesRequest request =
           ListLinkedSourcesRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       for (DocumentLink element :
           documentLinkServiceClient.listLinkedSources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLinkedSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient.ListLinkedSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient.ListLinkedSourcesPagedResponse)` |   
  
### listLinkedSources(String parent)
    
    
    public final DocumentLinkServiceClient.ListLinkedSourcesPagedResponse listLinkedSources(String parent)

Return all source document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       String parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       for (DocumentLink element :
           documentLinkServiceClient.listLinkedSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document, for which all source links are returned. Format: projects/{project_number}/locations/{location}/documents/{source_document_id}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentLinkServiceClient.ListLinkedSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient.ListLinkedSourcesPagedResponse)` |   
  
### listLinkedSourcesCallable()
    
    
    public final UnaryCallable<ListLinkedSourcesRequest,ListLinkedSourcesResponse> listLinkedSourcesCallable()

Return all source document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       ListLinkedSourcesRequest request =
           ListLinkedSourcesRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       while (true) {
         ListLinkedSourcesResponse response =
             documentLinkServiceClient.listLinkedSourcesCallable().call(request);
         for (DocumentLink element : response.getDocumentLinksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinkedSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedSourcesRequest),[ListLinkedSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedSourcesResponse)>` |   
  
### listLinkedSourcesPagedCallable()
    
    
    public final UnaryCallable<ListLinkedSourcesRequest,DocumentLinkServiceClient.ListLinkedSourcesPagedResponse> listLinkedSourcesPagedCallable()

Return all source document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       ListLinkedSourcesRequest request =
           ListLinkedSourcesRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<DocumentLink> future =
           documentLinkServiceClient.listLinkedSourcesPagedCallable().futureCall(request);
       // Do something.
       for (DocumentLink element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinkedSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedSourcesRequest),[ListLinkedSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentLinkServiceClient.ListLinkedSourcesPagedResponse)>` |   
  
### listLinkedTargets(@Nullable DocumentName parent)
    
    
    public final ListLinkedTargetsResponse listLinkedTargets(@Nullable DocumentName parent)

Return all target document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       DocumentName parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]");
       ListLinkedTargetsResponse response = documentLinkServiceClient.listLinkedTargets(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentName`  
Required. The name of the document, for which all target links are returned. Format: projects/{project_number}/locations/{location}/documents/{target_document_id}.  
**Returns**  
---  
**Type** | **Description**  
`[ListLinkedTargetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsResponse)` |   
  
### listLinkedTargets(ListLinkedTargetsRequest request)
    
    
    public final ListLinkedTargetsResponse listLinkedTargets(ListLinkedTargetsRequest request)

Return all target document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       ListLinkedTargetsRequest request =
           ListLinkedTargetsRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ListLinkedTargetsResponse response = documentLinkServiceClient.listLinkedTargets(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLinkedTargetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListLinkedTargetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsResponse)` |   
  
### listLinkedTargets(String parent)
    
    
    public final ListLinkedTargetsResponse listLinkedTargets(String parent)

Return all target document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       String parent =
           DocumentName.ofProjectLocationDocumentName("[PROJECT]", "[LOCATION]", "[DOCUMENT]")
               .toString();
       ListLinkedTargetsResponse response = documentLinkServiceClient.listLinkedTargets(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document, for which all target links are returned. Format: projects/{project_number}/locations/{location}/documents/{target_document_id}.  
**Returns**  
---  
**Type** | **Description**  
`[ListLinkedTargetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsResponse)` |   
  
### listLinkedTargetsCallable()
    
    
    public final UnaryCallable<ListLinkedTargetsRequest,ListLinkedTargetsResponse> listLinkedTargetsCallable()

Return all target document-links from the document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentLinkServiceClient documentLinkServiceClient = DocumentLinkServiceClient.create()) {
       ListLinkedTargetsRequest request =
           ListLinkedTargetsRequest.newBuilder()
               .setParent(
                   DocumentName.ofProjectLocationDocumentName(
                           "[PROJECT]", "[LOCATION]", "[DOCUMENT]")
                       .toString())
               .setRequestMetadata(RequestMetadata.newBuilder().build())
               .build();
       ApiFuture<ListLinkedTargetsResponse> future =
           documentLinkServiceClient.listLinkedTargetsCallable().futureCall(request);
       // Do something.
       ListLinkedTargetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinkedTargetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsRequest),[ListLinkedTargetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListLinkedTargetsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
