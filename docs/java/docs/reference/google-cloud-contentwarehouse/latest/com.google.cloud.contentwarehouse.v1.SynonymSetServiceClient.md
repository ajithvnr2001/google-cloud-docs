---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient
title: Class SynonymSetServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:02.875637+00:00
---

# Class SynonymSetServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SynonymSetServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-contentwarehouse/google-cloud-contentwarehouse/src/main/java/com/google/cloud/contentwarehouse/v1/SynonymSetServiceClient.java)| [Product Reference](https://cloud.google.com/document-warehouse/docs/overview)  
---|---  
  
Service Description: A Service that manage/custom customer specified SynonymSets.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SynonymSet synonymSet = SynonymSet.newBuilder().build();
       SynonymSet response = synonymSetServiceClient.createSynonymSet(parent, synonymSet);
     }
     

Note: close() needs to be called on the SynonymSetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSynonymSet |  Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSynonymSet(CreateSynonymSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSynonymSet(LocationName parent, SynonymSet synonymSet) 
  * createSynonymSet(String parent, SynonymSet synonymSet) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSynonymSetCallable() 

  
GetSynonymSet |  Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSynonymSet(GetSynonymSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSynonymSet(SynonymSetName name) 
  * getSynonymSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSynonymSetCallable() 

  
UpdateSynonymSet |  Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSynonymSet(UpdateSynonymSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSynonymSet(SynonymSetName name, SynonymSet synonymSet) 
  * updateSynonymSet(String name, SynonymSet synonymSet) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSynonymSetCallable() 

  
DeleteSynonymSet |  Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSynonymSet(DeleteSynonymSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSynonymSet(SynonymSetName name) 
  * deleteSynonymSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSynonymSetCallable() 

  
ListSynonymSets |  Returns all SynonymSets (for all contexts) for the specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSynonymSets(ListSynonymSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSynonymSets(LocationName parent) 
  * listSynonymSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSynonymSetsPagedCallable() 
  * listSynonymSetsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SynonymSetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SynonymSetServiceSettings synonymSetServiceSettings =
         SynonymSetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SynonymSetServiceClient synonymSetServiceClient =
         SynonymSetServiceClient.create(synonymSetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SynonymSetServiceSettings synonymSetServiceSettings =
         SynonymSetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SynonymSetServiceClient synonymSetServiceClient =
         SynonymSetServiceClient.create(synonymSetServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SynonymSetServiceSettings synonymSetServiceSettings =
         SynonymSetServiceSettings.newHttpJsonBuilder().build();
     SynonymSetServiceClient synonymSetServiceClient =
         SynonymSetServiceClient.create(synonymSetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SynonymSetServiceClient

## Static Methods 

### create()
    
    
    public static final SynonymSetServiceClient create()

Constructs an instance of SynonymSetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SynonymSetServiceSettings settings)
    
    
    public static final SynonymSetServiceClient create(SynonymSetServiceSettings settings)

Constructs an instance of SynonymSetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SynonymSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SynonymSetServiceStub stub)
    
    
    public static final SynonymSetServiceClient create(SynonymSetServiceStub stub)

Constructs an instance of SynonymSetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SynonymSetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SynonymSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.SynonymSetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient)` |   
  
## Constructors 

### SynonymSetServiceClient(SynonymSetServiceSettings settings)
    
    
    protected SynonymSetServiceClient(SynonymSetServiceSettings settings)

Constructs an instance of SynonymSetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SynonymSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceSettings)`  
  
  
### SynonymSetServiceClient(SynonymSetServiceStub stub)
    
    
    protected SynonymSetServiceClient(SynonymSetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SynonymSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.SynonymSetServiceStub)`  
  
  
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

### createSynonymSet(@Nullable LocationName parent, SynonymSet synonymSet)
    
    
    public final SynonymSet createSynonymSet(@Nullable LocationName parent, SynonymSet synonymSet)

Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SynonymSet synonymSet = SynonymSet.newBuilder().build();
       SynonymSet response = synonymSetServiceClient.createSynonymSet(parent, synonymSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`synonymSet` | `[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)`  
Required. The synonymSet to be created for a context  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### createSynonymSet(CreateSynonymSetRequest request)
    
    
    public final SynonymSet createSynonymSet(CreateSynonymSetRequest request)

Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       CreateSynonymSetRequest request =
           CreateSynonymSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSynonymSet(SynonymSet.newBuilder().build())
               .build();
       SynonymSet response = synonymSetServiceClient.createSynonymSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateSynonymSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### createSynonymSet(String parent, SynonymSet synonymSet)
    
    
    public final SynonymSet createSynonymSet(String parent, SynonymSet synonymSet)

Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       SynonymSet synonymSet = SynonymSet.newBuilder().build();
       SynonymSet response = synonymSetServiceClient.createSynonymSet(parent, synonymSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`synonymSet` | `[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)`  
Required. The synonymSet to be created for a context  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### createSynonymSetCallable()
    
    
    public final UnaryCallable<CreateSynonymSetRequest,SynonymSet> createSynonymSetCallable()

Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       CreateSynonymSetRequest request =
           CreateSynonymSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSynonymSet(SynonymSet.newBuilder().build())
               .build();
       ApiFuture<SynonymSet> future =
           synonymSetServiceClient.createSynonymSetCallable().futureCall(request);
       // Do something.
       SynonymSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateSynonymSetRequest),[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)>` |   
  
### deleteSynonymSet(@Nullable SynonymSetName name)
    
    
    public final void deleteSynonymSet(@Nullable SynonymSetName name)

Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       SynonymSetName name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]");
       synonymSetServiceClient.deleteSynonymSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.SynonymSetName`  
Required. The name of the synonymSet to delete Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
  
### deleteSynonymSet(DeleteSynonymSetRequest request)
    
    
    public final void deleteSynonymSet(DeleteSynonymSetRequest request)

Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       DeleteSynonymSetRequest request =
           DeleteSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .build();
       synonymSetServiceClient.deleteSynonymSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteSynonymSetRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSynonymSet(String name)
    
    
    public final void deleteSynonymSet(String name)

Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       String name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString();
       synonymSetServiceClient.deleteSynonymSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the synonymSet to delete Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
  
### deleteSynonymSetCallable()
    
    
    public final UnaryCallable<DeleteSynonymSetRequest,Empty> deleteSynonymSetCallable()

Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       DeleteSynonymSetRequest request =
           DeleteSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .build();
       ApiFuture<Empty> future =
           synonymSetServiceClient.deleteSynonymSetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteSynonymSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSettings()
    
    
    public final @Nullable SynonymSetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.SynonymSetServiceSettings` |   
  
### getStub()
    
    
    public SynonymSetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.SynonymSetServiceStub)` |   
  
### getSynonymSet(@Nullable SynonymSetName name)
    
    
    public final SynonymSet getSynonymSet(@Nullable SynonymSetName name)

Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       SynonymSetName name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]");
       SynonymSet response = synonymSetServiceClient.getSynonymSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.SynonymSetName`  
Required. The name of the synonymSet to retrieve Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### getSynonymSet(GetSynonymSetRequest request)
    
    
    public final SynonymSet getSynonymSet(GetSynonymSetRequest request)

Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       GetSynonymSetRequest request =
           GetSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .build();
       SynonymSet response = synonymSetServiceClient.getSynonymSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetSynonymSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### getSynonymSet(String name)
    
    
    public final SynonymSet getSynonymSet(String name)

Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       String name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString();
       SynonymSet response = synonymSetServiceClient.getSynonymSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the synonymSet to retrieve Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### getSynonymSetCallable()
    
    
    public final UnaryCallable<GetSynonymSetRequest,SynonymSet> getSynonymSetCallable()

Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       GetSynonymSetRequest request =
           GetSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .build();
       ApiFuture<SynonymSet> future =
           synonymSetServiceClient.getSynonymSetCallable().futureCall(request);
       // Do something.
       SynonymSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetSynonymSetRequest),[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)>` |   
  
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
  
### listSynonymSets(@Nullable LocationName parent)
    
    
    public final SynonymSetServiceClient.ListSynonymSetsPagedResponse listSynonymSets(@Nullable LocationName parent)

Returns all SynonymSets (for all contexts) for the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SynonymSet element : synonymSetServiceClient.listSynonymSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient.ListSynonymSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient.ListSynonymSetsPagedResponse)` |   
  
### listSynonymSets(ListSynonymSetsRequest request)
    
    
    public final SynonymSetServiceClient.ListSynonymSetsPagedResponse listSynonymSets(ListSynonymSetsRequest request)

Returns all SynonymSets (for all contexts) for the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       ListSynonymSetsRequest request =
           ListSynonymSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SynonymSet element : synonymSetServiceClient.listSynonymSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSynonymSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListSynonymSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient.ListSynonymSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient.ListSynonymSetsPagedResponse)` |   
  
### listSynonymSets(String parent)
    
    
    public final SynonymSetServiceClient.ListSynonymSetsPagedResponse listSynonymSets(String parent)

Returns all SynonymSets (for all contexts) for the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SynonymSet element : synonymSetServiceClient.listSynonymSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSetServiceClient.ListSynonymSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient.ListSynonymSetsPagedResponse)` |   
  
### listSynonymSetsCallable()
    
    
    public final UnaryCallable<ListSynonymSetsRequest,ListSynonymSetsResponse> listSynonymSetsCallable()

Returns all SynonymSets (for all contexts) for the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       ListSynonymSetsRequest request =
           ListSynonymSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSynonymSetsResponse response =
             synonymSetServiceClient.listSynonymSetsCallable().call(request);
         for (SynonymSet element : response.getSynonymSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSynonymSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListSynonymSetsRequest),[ListSynonymSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListSynonymSetsResponse)>` |   
  
### listSynonymSetsPagedCallable()
    
    
    public final UnaryCallable<ListSynonymSetsRequest,SynonymSetServiceClient.ListSynonymSetsPagedResponse> listSynonymSetsPagedCallable()

Returns all SynonymSets (for all contexts) for the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       ListSynonymSetsRequest request =
           ListSynonymSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SynonymSet> future =
           synonymSetServiceClient.listSynonymSetsPagedCallable().futureCall(request);
       // Do something.
       for (SynonymSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSynonymSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListSynonymSetsRequest),[ListSynonymSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetServiceClient.ListSynonymSetsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSynonymSet(@Nullable SynonymSetName name, SynonymSet synonymSet)
    
    
    public final SynonymSet updateSynonymSet(@Nullable SynonymSetName name, SynonymSet synonymSet)

Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       SynonymSetName name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]");
       SynonymSet synonymSet = SynonymSet.newBuilder().build();
       SynonymSet response = synonymSetServiceClient.updateSynonymSet(name, synonymSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.SynonymSetName`  
Required. The name of the synonymSet to update Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
`synonymSet` | `[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)`  
Required. The synonymSet to be updated for the customer  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### updateSynonymSet(UpdateSynonymSetRequest request)
    
    
    public final SynonymSet updateSynonymSet(UpdateSynonymSetRequest request)

Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       UpdateSynonymSetRequest request =
           UpdateSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .setSynonymSet(SynonymSet.newBuilder().build())
               .build();
       SynonymSet response = synonymSetServiceClient.updateSynonymSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateSynonymSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### updateSynonymSet(String name, SynonymSet synonymSet)
    
    
    public final SynonymSet updateSynonymSet(String name, SynonymSet synonymSet)

Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       String name = SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString();
       SynonymSet synonymSet = SynonymSet.newBuilder().build();
       SynonymSet response = synonymSetServiceClient.updateSynonymSet(name, synonymSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the synonymSet to update Format: projects/{project_number}/locations/{location}/synonymSets/{context}.  
`synonymSet` | `[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)`  
Required. The synonymSet to be updated for the customer  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### updateSynonymSetCallable()
    
    
    public final UnaryCallable<UpdateSynonymSetRequest,SynonymSet> updateSynonymSetCallable()

Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SynonymSetServiceClient synonymSetServiceClient = SynonymSetServiceClient.create()) {
       UpdateSynonymSetRequest request =
           UpdateSynonymSetRequest.newBuilder()
               .setName(SynonymSetName.of("[PROJECT]", "[LOCATION]", "[CONTEXT]").toString())
               .setSynonymSet(SynonymSet.newBuilder().build())
               .build();
       ApiFuture<SynonymSet> future =
           synonymSetServiceClient.updateSynonymSetCallable().futureCall(request);
       // Do something.
       SynonymSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSynonymSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateSynonymSetRequest),[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
