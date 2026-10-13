---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient
title: Class DocumentSchemaServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:46.299277+00:00
---

# Class DocumentSchemaServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentSchemaServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-contentwarehouse/google-cloud-contentwarehouse/src/main/java/com/google/cloud/contentwarehouse/v1/DocumentSchemaServiceClient.java)| [Product Reference](https://cloud.google.com/document-warehouse/docs/overview)  
---|---  
  
Service Description: This service lets you manage document schema.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DocumentSchema documentSchema = DocumentSchema.newBuilder().build();
       DocumentSchema response =
           documentSchemaServiceClient.createDocumentSchema(parent, documentSchema);
     }
     

Note: close() needs to be called on the DocumentSchemaServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDocumentSchema |  Creates a document schema. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDocumentSchema(CreateDocumentSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDocumentSchema(LocationName parent, DocumentSchema documentSchema) 
  * createDocumentSchema(String parent, DocumentSchema documentSchema) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDocumentSchemaCallable() 

  
UpdateDocumentSchema |  Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDocumentSchema(UpdateDocumentSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDocumentSchema(DocumentSchemaName name, DocumentSchema documentSchema) 
  * updateDocumentSchema(String name, DocumentSchema documentSchema) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDocumentSchemaCallable() 

  
GetDocumentSchema |  Gets a document schema. Returns NOT_FOUND if the document schema does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDocumentSchema(GetDocumentSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDocumentSchema(DocumentSchemaName name) 
  * getDocumentSchema(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDocumentSchemaCallable() 

  
DeleteDocumentSchema |  Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDocumentSchema(DeleteDocumentSchemaRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDocumentSchema(DocumentSchemaName name) 
  * deleteDocumentSchema(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDocumentSchemaCallable() 

  
ListDocumentSchemas |  Lists document schemas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDocumentSchemas(ListDocumentSchemasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDocumentSchemas(LocationName parent) 
  * listDocumentSchemas(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDocumentSchemasPagedCallable() 
  * listDocumentSchemasCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DocumentSchemaServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentSchemaServiceSettings documentSchemaServiceSettings =
         DocumentSchemaServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create(documentSchemaServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentSchemaServiceSettings documentSchemaServiceSettings =
         DocumentSchemaServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create(documentSchemaServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentSchemaServiceSettings documentSchemaServiceSettings =
         DocumentSchemaServiceSettings.newHttpJsonBuilder().build();
     DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create(documentSchemaServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentSchemaServiceClient

## Static Methods 

### create()
    
    
    public static final DocumentSchemaServiceClient create()

Constructs an instance of DocumentSchemaServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentSchemaServiceSettings settings)
    
    
    public static final DocumentSchemaServiceClient create(DocumentSchemaServiceSettings settings)

Constructs an instance of DocumentSchemaServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentSchemaServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentSchemaServiceStub stub)
    
    
    public static final DocumentSchemaServiceClient create(DocumentSchemaServiceStub stub)

Constructs an instance of DocumentSchemaServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DocumentSchemaServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentSchemaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentSchemaServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient)` |   
  
## Constructors 

### DocumentSchemaServiceClient(DocumentSchemaServiceSettings settings)
    
    
    protected DocumentSchemaServiceClient(DocumentSchemaServiceSettings settings)

Constructs an instance of DocumentSchemaServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentSchemaServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings)`  
  
  
### DocumentSchemaServiceClient(DocumentSchemaServiceStub stub)
    
    
    protected DocumentSchemaServiceClient(DocumentSchemaServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentSchemaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentSchemaServiceStub)`  
  
  
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

### createDocumentSchema(@Nullable LocationName parent, DocumentSchema documentSchema)
    
    
    public final DocumentSchema createDocumentSchema(@Nullable LocationName parent, DocumentSchema documentSchema)

Creates a document schema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DocumentSchema documentSchema = DocumentSchema.newBuilder().build();
       DocumentSchema response =
           documentSchemaServiceClient.createDocumentSchema(parent, documentSchema);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent name.  
`documentSchema` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)`  
Required. The document schema to create.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### createDocumentSchema(CreateDocumentSchemaRequest request)
    
    
    public final DocumentSchema createDocumentSchema(CreateDocumentSchemaRequest request)

Creates a document schema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       CreateDocumentSchemaRequest request =
           CreateDocumentSchemaRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       DocumentSchema response = documentSchemaServiceClient.createDocumentSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentSchemaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### createDocumentSchema(String parent, DocumentSchema documentSchema)
    
    
    public final DocumentSchema createDocumentSchema(String parent, DocumentSchema documentSchema)

Creates a document schema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DocumentSchema documentSchema = DocumentSchema.newBuilder().build();
       DocumentSchema response =
           documentSchemaServiceClient.createDocumentSchema(parent, documentSchema);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent name.  
`documentSchema` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)`  
Required. The document schema to create.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### createDocumentSchemaCallable()
    
    
    public final UnaryCallable<CreateDocumentSchemaRequest,DocumentSchema> createDocumentSchemaCallable()

Creates a document schema.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       CreateDocumentSchemaRequest request =
           CreateDocumentSchemaRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       ApiFuture<DocumentSchema> future =
           documentSchemaServiceClient.createDocumentSchemaCallable().futureCall(request);
       // Do something.
       DocumentSchema response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentSchemaRequest),[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)>` |   
  
### deleteDocumentSchema(@Nullable DocumentSchemaName name)
    
    
    public final void deleteDocumentSchema(@Nullable DocumentSchemaName name)

Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       DocumentSchemaName name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]");
       documentSchemaServiceClient.deleteDocumentSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentSchemaName`  
Required. The name of the document schema to delete.  
  
### deleteDocumentSchema(DeleteDocumentSchemaRequest request)
    
    
    public final void deleteDocumentSchema(DeleteDocumentSchemaRequest request)

Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       DeleteDocumentSchemaRequest request =
           DeleteDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .build();
       documentSchemaServiceClient.deleteDocumentSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentSchemaRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDocumentSchema(String name)
    
    
    public final void deleteDocumentSchema(String name)

Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       String name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString();
       documentSchemaServiceClient.deleteDocumentSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document schema to delete.  
  
### deleteDocumentSchemaCallable()
    
    
    public final UnaryCallable<DeleteDocumentSchemaRequest,Empty> deleteDocumentSchemaCallable()

Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       DeleteDocumentSchemaRequest request =
           DeleteDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .build();
       ApiFuture<Empty> future =
           documentSchemaServiceClient.deleteDocumentSchemaCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentSchemaRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDocumentSchema(@Nullable DocumentSchemaName name)
    
    
    public final DocumentSchema getDocumentSchema(@Nullable DocumentSchemaName name)

Gets a document schema. Returns NOT_FOUND if the document schema does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       DocumentSchemaName name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]");
       DocumentSchema response = documentSchemaServiceClient.getDocumentSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentSchemaName`  
Required. The name of the document schema to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### getDocumentSchema(GetDocumentSchemaRequest request)
    
    
    public final DocumentSchema getDocumentSchema(GetDocumentSchemaRequest request)

Gets a document schema. Returns NOT_FOUND if the document schema does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       GetDocumentSchemaRequest request =
           GetDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .build();
       DocumentSchema response = documentSchemaServiceClient.getDocumentSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetDocumentSchemaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### getDocumentSchema(String name)
    
    
    public final DocumentSchema getDocumentSchema(String name)

Gets a document schema. Returns NOT_FOUND if the document schema does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       String name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString();
       DocumentSchema response = documentSchemaServiceClient.getDocumentSchema(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document schema to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### getDocumentSchemaCallable()
    
    
    public final UnaryCallable<GetDocumentSchemaRequest,DocumentSchema> getDocumentSchemaCallable()

Gets a document schema. Returns NOT_FOUND if the document schema does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       GetDocumentSchemaRequest request =
           GetDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .build();
       ApiFuture<DocumentSchema> future =
           documentSchemaServiceClient.getDocumentSchemaCallable().futureCall(request);
       // Do something.
       DocumentSchema response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetDocumentSchemaRequest),[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)>` |   
  
### getSettings()
    
    
    public final @Nullable DocumentSchemaServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings` |   
  
### getStub()
    
    
    public DocumentSchemaServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.DocumentSchemaServiceStub)` |   
  
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
  
### listDocumentSchemas(@Nullable LocationName parent)
    
    
    public final DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse listDocumentSchemas(@Nullable LocationName parent)

Lists document schemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DocumentSchema element :
           documentSchemaServiceClient.listDocumentSchemas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent, which owns this collection of document schemas. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse)` |   
  
### listDocumentSchemas(ListDocumentSchemasRequest request)
    
    
    public final DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse listDocumentSchemas(ListDocumentSchemasRequest request)

Lists document schemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       ListDocumentSchemasRequest request =
           ListDocumentSchemasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DocumentSchema element :
           documentSchemaServiceClient.listDocumentSchemas(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDocumentSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListDocumentSchemasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse)` |   
  
### listDocumentSchemas(String parent)
    
    
    public final DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse listDocumentSchemas(String parent)

Lists document schemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DocumentSchema element :
           documentSchemaServiceClient.listDocumentSchemas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of document schemas. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse)` |   
  
### listDocumentSchemasCallable()
    
    
    public final UnaryCallable<ListDocumentSchemasRequest,ListDocumentSchemasResponse> listDocumentSchemasCallable()

Lists document schemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       ListDocumentSchemasRequest request =
           ListDocumentSchemasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDocumentSchemasResponse response =
             documentSchemaServiceClient.listDocumentSchemasCallable().call(request);
         for (DocumentSchema element : response.getDocumentSchemasList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListDocumentSchemasRequest),[ListDocumentSchemasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListDocumentSchemasResponse)>` |   
  
### listDocumentSchemasPagedCallable()
    
    
    public final UnaryCallable<ListDocumentSchemasRequest,DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse> listDocumentSchemasPagedCallable()

Lists document schemas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       ListDocumentSchemasRequest request =
           ListDocumentSchemasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DocumentSchema> future =
           documentSchemaServiceClient.listDocumentSchemasPagedCallable().futureCall(request);
       // Do something.
       for (DocumentSchema element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDocumentSchemasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListDocumentSchemasRequest),[ListDocumentSchemasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.ListDocumentSchemasPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDocumentSchema(@Nullable DocumentSchemaName name, DocumentSchema documentSchema)
    
    
    public final DocumentSchema updateDocumentSchema(@Nullable DocumentSchemaName name, DocumentSchema documentSchema)

Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       DocumentSchemaName name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]");
       DocumentSchema documentSchema = DocumentSchema.newBuilder().build();
       DocumentSchema response =
           documentSchemaServiceClient.updateDocumentSchema(name, documentSchema);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.DocumentSchemaName`  
Required. The name of the document schema to update. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.  
`documentSchema` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)`  
Required. The document schema to update with.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### updateDocumentSchema(UpdateDocumentSchemaRequest request)
    
    
    public final DocumentSchema updateDocumentSchema(UpdateDocumentSchemaRequest request)

Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       UpdateDocumentSchemaRequest request =
           UpdateDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       DocumentSchema response = documentSchemaServiceClient.updateDocumentSchema(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### updateDocumentSchema(String name, DocumentSchema documentSchema)
    
    
    public final DocumentSchema updateDocumentSchema(String name, DocumentSchema documentSchema)

Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       String name =
           DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString();
       DocumentSchema documentSchema = DocumentSchema.newBuilder().build();
       DocumentSchema response =
           documentSchemaServiceClient.updateDocumentSchema(name, documentSchema);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the document schema to update. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.  
`documentSchema` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)`  
Required. The document schema to update with.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)` |   
  
### updateDocumentSchemaCallable()
    
    
    public final UnaryCallable<UpdateDocumentSchemaRequest,DocumentSchema> updateDocumentSchemaCallable()

Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentSchemaServiceClient documentSchemaServiceClient =
         DocumentSchemaServiceClient.create()) {
       UpdateDocumentSchemaRequest request =
           UpdateDocumentSchemaRequest.newBuilder()
               .setName(
                   DocumentSchemaName.of("[PROJECT]", "[LOCATION]", "[DOCUMENT_SCHEMA]").toString())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       ApiFuture<DocumentSchema> future =
           documentSchemaServiceClient.updateDocumentSchemaCallable().futureCall(request);
       // Do something.
       DocumentSchema response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest),[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
