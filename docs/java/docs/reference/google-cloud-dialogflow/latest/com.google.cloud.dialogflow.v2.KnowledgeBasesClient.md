---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient
title: Class KnowledgeBasesClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:47.815682+00:00
---

# Class KnowledgeBasesClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class KnowledgeBasesClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/KnowledgeBasesClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing KnowledgeBases.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       KnowledgeBaseName name =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]");
       KnowledgeBase response = knowledgeBasesClient.getKnowledgeBase(name);
     }
     

Note: close() needs to be called on the KnowledgeBasesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListKnowledgeBases |  Returns the list of all knowledge bases of the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listKnowledgeBases(ListKnowledgeBasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listKnowledgeBases(LocationName parent) 
  * listKnowledgeBases(ProjectName parent) 
  * listKnowledgeBases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listKnowledgeBasesPagedCallable() 
  * listKnowledgeBasesCallable() 

  
GetKnowledgeBase |  Retrieves the specified knowledge base. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getKnowledgeBase(GetKnowledgeBaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getKnowledgeBase(KnowledgeBaseName name) 
  * getKnowledgeBase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getKnowledgeBaseCallable() 

  
CreateKnowledgeBase |  Creates a knowledge base. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createKnowledgeBase(CreateKnowledgeBaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createKnowledgeBase(LocationName parent, KnowledgeBase knowledgeBase) 
  * createKnowledgeBase(ProjectName parent, KnowledgeBase knowledgeBase) 
  * createKnowledgeBase(String parent, KnowledgeBase knowledgeBase) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createKnowledgeBaseCallable() 

  
DeleteKnowledgeBase |  Deletes the specified knowledge base. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteKnowledgeBase(DeleteKnowledgeBaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteKnowledgeBase(KnowledgeBaseName name) 
  * deleteKnowledgeBase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteKnowledgeBaseCallable() 

  
UpdateKnowledgeBase |  Updates the specified knowledge base. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateKnowledgeBase(UpdateKnowledgeBaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateKnowledgeBase(KnowledgeBase knowledgeBase, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateKnowledgeBaseCallable() 

  
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

This class can be customized by passing in a custom instance of KnowledgeBasesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     KnowledgeBasesSettings knowledgeBasesSettings =
         KnowledgeBasesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create(knowledgeBasesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     KnowledgeBasesSettings knowledgeBasesSettings =
         KnowledgeBasesSettings.newBuilder().setEndpoint(myEndpoint).build();
     KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create(knowledgeBasesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     KnowledgeBasesSettings knowledgeBasesSettings =
         KnowledgeBasesSettings.newHttpJsonBuilder().build();
     KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create(knowledgeBasesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > KnowledgeBasesClient

## Static Methods 

### create()
    
    
    public static final KnowledgeBasesClient create()

Constructs an instance of KnowledgeBasesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(KnowledgeBasesSettings settings)
    
    
    public static final KnowledgeBasesClient create(KnowledgeBasesSettings settings)

Constructs an instance of KnowledgeBasesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[KnowledgeBasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(KnowledgeBasesStub stub)
    
    
    public static final KnowledgeBasesClient create(KnowledgeBasesStub stub)

Constructs an instance of KnowledgeBasesClient, using the given stub for making calls. This is for advanced usage - prefer using create(KnowledgeBasesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[KnowledgeBasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.KnowledgeBasesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient)` |   
  
## Constructors 

### KnowledgeBasesClient(KnowledgeBasesSettings settings)
    
    
    protected KnowledgeBasesClient(KnowledgeBasesSettings settings)

Constructs an instance of KnowledgeBasesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[KnowledgeBasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesSettings)`  
  
  
### KnowledgeBasesClient(KnowledgeBasesStub stub)
    
    
    protected KnowledgeBasesClient(KnowledgeBasesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[KnowledgeBasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.KnowledgeBasesStub)`  
  
  
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

### createKnowledgeBase(@Nullable LocationName parent, KnowledgeBase knowledgeBase)
    
    
    public final KnowledgeBase createKnowledgeBase(@Nullable LocationName parent, KnowledgeBase knowledgeBase)

Creates a knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       KnowledgeBase knowledgeBase = KnowledgeBase.newBuilder().build();
       KnowledgeBase response = knowledgeBasesClient.createKnowledgeBase(parent, knowledgeBase);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project to create a knowledge base for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`knowledgeBase` | `[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)`  
Required. The knowledge base to create.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### createKnowledgeBase(@Nullable ProjectName parent, KnowledgeBase knowledgeBase)
    
    
    public final KnowledgeBase createKnowledgeBase(@Nullable ProjectName parent, KnowledgeBase knowledgeBase)

Creates a knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       KnowledgeBase knowledgeBase = KnowledgeBase.newBuilder().build();
       KnowledgeBase response = knowledgeBasesClient.createKnowledgeBase(parent, knowledgeBase);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project to create a knowledge base for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`knowledgeBase` | `[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)`  
Required. The knowledge base to create.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### createKnowledgeBase(CreateKnowledgeBaseRequest request)
    
    
    public final KnowledgeBase createKnowledgeBase(CreateKnowledgeBaseRequest request)

Creates a knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       CreateKnowledgeBaseRequest request =
           CreateKnowledgeBaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setKnowledgeBase(KnowledgeBase.newBuilder().build())
               .build();
       KnowledgeBase response = knowledgeBasesClient.createKnowledgeBase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateKnowledgeBaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### createKnowledgeBase(String parent, KnowledgeBase knowledgeBase)
    
    
    public final KnowledgeBase createKnowledgeBase(String parent, KnowledgeBase knowledgeBase)

Creates a knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       KnowledgeBase knowledgeBase = KnowledgeBase.newBuilder().build();
       KnowledgeBase response = knowledgeBasesClient.createKnowledgeBase(parent, knowledgeBase);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to create a knowledge base for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`knowledgeBase` | `[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)`  
Required. The knowledge base to create.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### createKnowledgeBaseCallable()
    
    
    public final UnaryCallable<CreateKnowledgeBaseRequest,KnowledgeBase> createKnowledgeBaseCallable()

Creates a knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       CreateKnowledgeBaseRequest request =
           CreateKnowledgeBaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setKnowledgeBase(KnowledgeBase.newBuilder().build())
               .build();
       ApiFuture<KnowledgeBase> future =
           knowledgeBasesClient.createKnowledgeBaseCallable().futureCall(request);
       // Do something.
       KnowledgeBase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateKnowledgeBaseRequest),[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>` |   
  
### deleteKnowledgeBase(@Nullable KnowledgeBaseName name)
    
    
    public final void deleteKnowledgeBase(@Nullable KnowledgeBaseName name)

Deletes the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       KnowledgeBaseName name =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]");
       knowledgeBasesClient.deleteKnowledgeBase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.KnowledgeBaseName`  
Required. The name of the knowledge base to delete. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
  
### deleteKnowledgeBase(DeleteKnowledgeBaseRequest request)
    
    
    public final void deleteKnowledgeBase(DeleteKnowledgeBaseRequest request)

Deletes the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       DeleteKnowledgeBaseRequest request =
           DeleteKnowledgeBaseRequest.newBuilder()
               .setName(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setForce(true)
               .build();
       knowledgeBasesClient.deleteKnowledgeBase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteKnowledgeBaseRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteKnowledgeBase(String name)
    
    
    public final void deleteKnowledgeBase(String name)

Deletes the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       String name =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]").toString();
       knowledgeBasesClient.deleteKnowledgeBase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the knowledge base to delete. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
  
### deleteKnowledgeBaseCallable()
    
    
    public final UnaryCallable<DeleteKnowledgeBaseRequest,Empty> deleteKnowledgeBaseCallable()

Deletes the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       DeleteKnowledgeBaseRequest request =
           DeleteKnowledgeBaseRequest.newBuilder()
               .setName(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future =
           knowledgeBasesClient.deleteKnowledgeBaseCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteKnowledgeBaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getKnowledgeBase(@Nullable KnowledgeBaseName name)
    
    
    public final KnowledgeBase getKnowledgeBase(@Nullable KnowledgeBaseName name)

Retrieves the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       KnowledgeBaseName name =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]");
       KnowledgeBase response = knowledgeBasesClient.getKnowledgeBase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.KnowledgeBaseName`  
Required. The name of the knowledge base to retrieve. Format `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### getKnowledgeBase(GetKnowledgeBaseRequest request)
    
    
    public final KnowledgeBase getKnowledgeBase(GetKnowledgeBaseRequest request)

Retrieves the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       GetKnowledgeBaseRequest request =
           GetKnowledgeBaseRequest.newBuilder()
               .setName(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .build();
       KnowledgeBase response = knowledgeBasesClient.getKnowledgeBase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetKnowledgeBaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### getKnowledgeBase(String name)
    
    
    public final KnowledgeBase getKnowledgeBase(String name)

Retrieves the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       String name =
           KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]").toString();
       KnowledgeBase response = knowledgeBasesClient.getKnowledgeBase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the knowledge base to retrieve. Format `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### getKnowledgeBaseCallable()
    
    
    public final UnaryCallable<GetKnowledgeBaseRequest,KnowledgeBase> getKnowledgeBaseCallable()

Retrieves the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       GetKnowledgeBaseRequest request =
           GetKnowledgeBaseRequest.newBuilder()
               .setName(
                   KnowledgeBaseName.ofProjectKnowledgeBaseName("[PROJECT]", "[KNOWLEDGE_BASE]")
                       .toString())
               .build();
       ApiFuture<KnowledgeBase> future =
           knowledgeBasesClient.getKnowledgeBaseCallable().futureCall(request);
       // Do something.
       KnowledgeBase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetKnowledgeBaseRequest),[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = knowledgeBasesClient.getLocation(request);
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
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = knowledgeBasesClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable KnowledgeBasesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.KnowledgeBasesSettings` |   
  
### getStub()
    
    
    public KnowledgeBasesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.KnowledgeBasesStub)` |   
  
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
  
### listKnowledgeBases(@Nullable LocationName parent)
    
    
    public final KnowledgeBasesClient.ListKnowledgeBasesPagedResponse listKnowledgeBases(@Nullable LocationName parent)

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (KnowledgeBase element : knowledgeBasesClient.listKnowledgeBases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project to list of knowledge bases for. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient.ListKnowledgeBasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListKnowledgeBasesPagedResponse)` |   
  
### listKnowledgeBases(@Nullable ProjectName parent)
    
    
    public final KnowledgeBasesClient.ListKnowledgeBasesPagedResponse listKnowledgeBases(@Nullable ProjectName parent)

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (KnowledgeBase element : knowledgeBasesClient.listKnowledgeBases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project to list of knowledge bases for. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient.ListKnowledgeBasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListKnowledgeBasesPagedResponse)` |   
  
### listKnowledgeBases(ListKnowledgeBasesRequest request)
    
    
    public final KnowledgeBasesClient.ListKnowledgeBasesPagedResponse listKnowledgeBases(ListKnowledgeBasesRequest request)

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListKnowledgeBasesRequest request =
           ListKnowledgeBasesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (KnowledgeBase element : knowledgeBasesClient.listKnowledgeBases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListKnowledgeBasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient.ListKnowledgeBasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListKnowledgeBasesPagedResponse)` |   
  
### listKnowledgeBases(String parent)
    
    
    public final KnowledgeBasesClient.ListKnowledgeBasesPagedResponse listKnowledgeBases(String parent)

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (KnowledgeBase element : knowledgeBasesClient.listKnowledgeBases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to list of knowledge bases for. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBasesClient.ListKnowledgeBasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListKnowledgeBasesPagedResponse)` |   
  
### listKnowledgeBasesCallable()
    
    
    public final UnaryCallable<ListKnowledgeBasesRequest,ListKnowledgeBasesResponse> listKnowledgeBasesCallable()

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListKnowledgeBasesRequest request =
           ListKnowledgeBasesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListKnowledgeBasesResponse response =
             knowledgeBasesClient.listKnowledgeBasesCallable().call(request);
         for (KnowledgeBase element : response.getKnowledgeBasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListKnowledgeBasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesRequest),[ListKnowledgeBasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesResponse)>` |   
  
### listKnowledgeBasesPagedCallable()
    
    
    public final UnaryCallable<ListKnowledgeBasesRequest,KnowledgeBasesClient.ListKnowledgeBasesPagedResponse> listKnowledgeBasesPagedCallable()

Returns the list of all knowledge bases of the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListKnowledgeBasesRequest request =
           ListKnowledgeBasesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<KnowledgeBase> future =
           knowledgeBasesClient.listKnowledgeBasesPagedCallable().futureCall(request);
       // Do something.
       for (KnowledgeBase element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListKnowledgeBasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesRequest),[ListKnowledgeBasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListKnowledgeBasesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final KnowledgeBasesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : knowledgeBasesClient.listLocations(request).iterateAll()) {
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
`[KnowledgeBasesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListLocationsPagedResponse)` |   
  
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
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = knowledgeBasesClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,KnowledgeBasesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           knowledgeBasesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateKnowledgeBase(KnowledgeBase knowledgeBase, FieldMask updateMask)
    
    
    public final KnowledgeBase updateKnowledgeBase(KnowledgeBase knowledgeBase, FieldMask updateMask)

Updates the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       KnowledgeBase knowledgeBase = KnowledgeBase.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       KnowledgeBase response = knowledgeBasesClient.updateKnowledgeBase(knowledgeBase, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`knowledgeBase` | `[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)`  
Required. The knowledge base to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Not specified means `update all`. Currently, only `display_name` can be updated, an InvalidArgument will be returned for attempting to update other fields.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### updateKnowledgeBase(UpdateKnowledgeBaseRequest request)
    
    
    public final KnowledgeBase updateKnowledgeBase(UpdateKnowledgeBaseRequest request)

Updates the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       UpdateKnowledgeBaseRequest request =
           UpdateKnowledgeBaseRequest.newBuilder()
               .setKnowledgeBase(KnowledgeBase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       KnowledgeBase response = knowledgeBasesClient.updateKnowledgeBase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateKnowledgeBaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)` |   
  
### updateKnowledgeBaseCallable()
    
    
    public final UnaryCallable<UpdateKnowledgeBaseRequest,KnowledgeBase> updateKnowledgeBaseCallable()

Updates the specified knowledge base.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (KnowledgeBasesClient knowledgeBasesClient = KnowledgeBasesClient.create()) {
       UpdateKnowledgeBaseRequest request =
           UpdateKnowledgeBaseRequest.newBuilder()
               .setKnowledgeBase(KnowledgeBase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<KnowledgeBase> future =
           knowledgeBasesClient.updateKnowledgeBaseCallable().futureCall(request);
       // Do something.
       KnowledgeBase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateKnowledgeBaseRequest),[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
