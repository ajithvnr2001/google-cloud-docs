---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient
title: Class CreativeSetServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:38.313093+00:00
---

# Class CreativeSetServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CreativeSetServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CreativeSetServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CreativeSet` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       CreativeSetName name = CreativeSetName.of("[NETWORK_CODE]", "[CREATIVE_SET]");
       CreativeSet response = creativeSetServiceClient.getCreativeSet(name);
     }
     

Note: close() needs to be called on the CreativeSetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCreativeSet |  Retrieves a `CreativeSet` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCreativeSet(GetCreativeSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCreativeSet(CreativeSetName name) 
  * getCreativeSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCreativeSetCallable() 

  
ListCreativeSets |  Lists `CreativeSet` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCreativeSets(ListCreativeSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCreativeSets(NetworkName parent) 
  * listCreativeSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCreativeSetsPagedCallable() 
  * listCreativeSetsCallable() 

  
CreateCreativeSet |  Creates a `CreativeSet` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCreativeSet(CreateCreativeSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCreativeSet(NetworkName parent, CreativeSet creativeSet) 
  * createCreativeSet(String parent, CreativeSet creativeSet) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCreativeSetCallable() 

  
UpdateCreativeSet |  Updates a `CreativeSet` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCreativeSet(UpdateCreativeSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCreativeSet(CreativeSet creativeSet, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCreativeSetCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CreativeSetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeSetServiceSettings creativeSetServiceSettings =
         CreativeSetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CreativeSetServiceClient creativeSetServiceClient =
         CreativeSetServiceClient.create(creativeSetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeSetServiceSettings creativeSetServiceSettings =
         CreativeSetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CreativeSetServiceClient creativeSetServiceClient =
         CreativeSetServiceClient.create(creativeSetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CreativeSetServiceClient

## Static Methods 

### create()
    
    
    public static final CreativeSetServiceClient create()

Constructs an instance of CreativeSetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeSetServiceSettings settings)
    
    
    public static final CreativeSetServiceClient create(CreativeSetServiceSettings settings)

Constructs an instance of CreativeSetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeSetServiceStub stub)
    
    
    public static final CreativeSetServiceClient create(CreativeSetServiceStub stub)

Constructs an instance of CreativeSetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CreativeSetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeSetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeSetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient)` |   
  
## Constructors 

### CreativeSetServiceClient(CreativeSetServiceSettings settings)
    
    
    protected CreativeSetServiceClient(CreativeSetServiceSettings settings)

Constructs an instance of CreativeSetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceSettings)`  
  
  
### CreativeSetServiceClient(CreativeSetServiceStub stub)
    
    
    protected CreativeSetServiceClient(CreativeSetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeSetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeSetServiceStub)`  
  
  
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

### createCreativeSet(@Nullable NetworkName parent, CreativeSet creativeSet)
    
    
    public final CreativeSet createCreativeSet(@Nullable NetworkName parent, CreativeSet creativeSet)

Creates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CreativeSet creativeSet = CreativeSet.newBuilder().build();
       CreativeSet response = creativeSetServiceClient.createCreativeSet(parent, creativeSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `CreativeSet` will be created. Format: `networks/{network_code}`  
`creativeSet` | `[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)`  
Required. The `CreativeSet` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### createCreativeSet(CreateCreativeSetRequest request)
    
    
    public final CreativeSet createCreativeSet(CreateCreativeSetRequest request)

Creates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       CreateCreativeSetRequest request =
           CreateCreativeSetRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCreativeSet(CreativeSet.newBuilder().build())
               .build();
       CreativeSet response = creativeSetServiceClient.createCreativeSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### createCreativeSet(String parent, CreativeSet creativeSet)
    
    
    public final CreativeSet createCreativeSet(String parent, CreativeSet creativeSet)

Creates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CreativeSet creativeSet = CreativeSet.newBuilder().build();
       CreativeSet response = creativeSetServiceClient.createCreativeSet(parent, creativeSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `CreativeSet` will be created. Format: `networks/{network_code}`  
`creativeSet` | `[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)`  
Required. The `CreativeSet` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### createCreativeSetCallable()
    
    
    public final UnaryCallable<CreateCreativeSetRequest,CreativeSet> createCreativeSetCallable()

Creates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       CreateCreativeSetRequest request =
           CreateCreativeSetRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCreativeSet(CreativeSet.newBuilder().build())
               .build();
       ApiFuture<CreativeSet> future =
           creativeSetServiceClient.createCreativeSetCallable().futureCall(request);
       // Do something.
       CreativeSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeSetRequest),[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)>` |   
  
### getCreativeSet(@Nullable CreativeSetName name)
    
    
    public final CreativeSet getCreativeSet(@Nullable CreativeSetName name)

Retrieves a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       CreativeSetName name = CreativeSetName.of("[NETWORK_CODE]", "[CREATIVE_SET]");
       CreativeSet response = creativeSetServiceClient.getCreativeSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeSetName`  
Required. The resource name of the CreativeSet. Format: `networks/{network_code}/creativeSets/{creative_set_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### getCreativeSet(GetCreativeSetRequest request)
    
    
    public final CreativeSet getCreativeSet(GetCreativeSetRequest request)

Retrieves a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       GetCreativeSetRequest request =
           GetCreativeSetRequest.newBuilder()
               .setName(CreativeSetName.of("[NETWORK_CODE]", "[CREATIVE_SET]").toString())
               .build();
       CreativeSet response = creativeSetServiceClient.getCreativeSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### getCreativeSet(String name)
    
    
    public final CreativeSet getCreativeSet(String name)

Retrieves a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       String name = CreativeSetName.of("[NETWORK_CODE]", "[CREATIVE_SET]").toString();
       CreativeSet response = creativeSetServiceClient.getCreativeSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CreativeSet. Format: `networks/{network_code}/creativeSets/{creative_set_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### getCreativeSetCallable()
    
    
    public final UnaryCallable<GetCreativeSetRequest,CreativeSet> getCreativeSetCallable()

Retrieves a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       GetCreativeSetRequest request =
           GetCreativeSetRequest.newBuilder()
               .setName(CreativeSetName.of("[NETWORK_CODE]", "[CREATIVE_SET]").toString())
               .build();
       ApiFuture<CreativeSet> future =
           creativeSetServiceClient.getCreativeSetCallable().futureCall(request);
       // Do something.
       CreativeSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeSetRequest),[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)>` |   
  
### getSettings()
    
    
    public final @Nullable CreativeSetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeSetServiceSettings` |   
  
### getStub()
    
    
    public CreativeSetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeSetServiceStub)` |   
  
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
  
### listCreativeSets(@Nullable NetworkName parent)
    
    
    public final CreativeSetServiceClient.ListCreativeSetsPagedResponse listCreativeSets(@Nullable NetworkName parent)

Lists `CreativeSet` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CreativeSet element : creativeSetServiceClient.listCreativeSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CreativeSets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient.ListCreativeSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient.ListCreativeSetsPagedResponse)` |   
  
### listCreativeSets(ListCreativeSetsRequest request)
    
    
    public final CreativeSetServiceClient.ListCreativeSetsPagedResponse listCreativeSets(ListCreativeSetsRequest request)

Lists `CreativeSet` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       ListCreativeSetsRequest request =
           ListCreativeSetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CreativeSet element : creativeSetServiceClient.listCreativeSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCreativeSetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient.ListCreativeSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient.ListCreativeSetsPagedResponse)` |   
  
### listCreativeSets(String parent)
    
    
    public final CreativeSetServiceClient.ListCreativeSetsPagedResponse listCreativeSets(String parent)

Lists `CreativeSet` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CreativeSet element : creativeSetServiceClient.listCreativeSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CreativeSets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSetServiceClient.ListCreativeSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient.ListCreativeSetsPagedResponse)` |   
  
### listCreativeSetsCallable()
    
    
    public final UnaryCallable<ListCreativeSetsRequest,ListCreativeSetsResponse> listCreativeSetsCallable()

Lists `CreativeSet` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       ListCreativeSetsRequest request =
           ListCreativeSetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCreativeSetsResponse response =
             creativeSetServiceClient.listCreativeSetsCallable().call(request);
         for (CreativeSet element : response.getCreativeSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeSetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeSetsRequest),[ListCreativeSetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeSetsResponse)>` |   
  
### listCreativeSetsPagedCallable()
    
    
    public final UnaryCallable<ListCreativeSetsRequest,CreativeSetServiceClient.ListCreativeSetsPagedResponse> listCreativeSetsPagedCallable()

Lists `CreativeSet` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       ListCreativeSetsRequest request =
           ListCreativeSetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CreativeSet> future =
           creativeSetServiceClient.listCreativeSetsPagedCallable().futureCall(request);
       // Do something.
       for (CreativeSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeSetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeSetsRequest),[ListCreativeSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSetServiceClient.ListCreativeSetsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCreativeSet(CreativeSet creativeSet, FieldMask updateMask)
    
    
    public final CreativeSet updateCreativeSet(CreativeSet creativeSet, FieldMask updateMask)

Updates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       CreativeSet creativeSet = CreativeSet.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CreativeSet response = creativeSetServiceClient.updateCreativeSet(creativeSet, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`creativeSet` | `[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)`  
Required. The `CreativeSet` to update. The `CreativeSet`'s `name` is used to identify the `CreativeSet` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### updateCreativeSet(UpdateCreativeSetRequest request)
    
    
    public final CreativeSet updateCreativeSet(UpdateCreativeSetRequest request)

Updates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       UpdateCreativeSetRequest request =
           UpdateCreativeSetRequest.newBuilder()
               .setCreativeSet(CreativeSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CreativeSet response = creativeSetServiceClient.updateCreativeSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)` |   
  
### updateCreativeSetCallable()
    
    
    public final UnaryCallable<UpdateCreativeSetRequest,CreativeSet> updateCreativeSetCallable()

Updates a `CreativeSet` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeSetServiceClient creativeSetServiceClient = CreativeSetServiceClient.create()) {
       UpdateCreativeSetRequest request =
           UpdateCreativeSetRequest.newBuilder()
               .setCreativeSet(CreativeSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CreativeSet> future =
           creativeSetServiceClient.updateCreativeSetCallable().futureCall(request);
       // Do something.
       CreativeSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCreativeSetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeSetRequest),[CreativeSet](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeSet)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
