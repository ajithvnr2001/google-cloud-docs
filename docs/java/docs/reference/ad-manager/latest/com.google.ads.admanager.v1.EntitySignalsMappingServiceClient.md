---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient
title: Class EntitySignalsMappingServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:45.134523+00:00
---

# Class EntitySignalsMappingServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EntitySignalsMappingServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/EntitySignalsMappingServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `EntitySignalsMapping` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       EntitySignalsMappingName name =
           EntitySignalsMappingName.of("[NETWORK_CODE]", "[ENTITY_SIGNALS_MAPPING]");
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.getEntitySignalsMapping(name);
     }
     

Note: close() needs to be called on the EntitySignalsMappingServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetEntitySignalsMapping |  Retrieves a `EntitySignalsMapping` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntitySignalsMapping(GetEntitySignalsMappingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntitySignalsMapping(EntitySignalsMappingName name) 
  * getEntitySignalsMapping(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntitySignalsMappingCallable() 

  
ListEntitySignalsMappings |  Lists `EntitySignalsMapping` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntitySignalsMappings(ListEntitySignalsMappingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntitySignalsMappings(NetworkName parent) 
  * listEntitySignalsMappings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntitySignalsMappingsPagedCallable() 
  * listEntitySignalsMappingsCallable() 

  
CreateEntitySignalsMapping |  Creates an `EntitySignalsMapping` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntitySignalsMapping(CreateEntitySignalsMappingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEntitySignalsMapping(NetworkName parent, EntitySignalsMapping entitySignalsMapping) 
  * createEntitySignalsMapping(String parent, EntitySignalsMapping entitySignalsMapping) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntitySignalsMappingCallable() 

  
UpdateEntitySignalsMapping |  Updates an `EntitySignalsMapping` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntitySignalsMapping(UpdateEntitySignalsMappingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEntitySignalsMapping(EntitySignalsMapping entitySignalsMapping, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntitySignalsMappingCallable() 

  
BatchCreateEntitySignalsMappings |  Creates `EntitySignalsMapping` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateEntitySignalsMappings(NetworkName parent, List<CreateEntitySignalsMappingRequest> requests) 
  * batchCreateEntitySignalsMappings(String parent, List<CreateEntitySignalsMappingRequest> requests) 
  * batchCreateEntitySignalsMappings(BatchCreateEntitySignalsMappingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateEntitySignalsMappingsCallable() 

  
BatchUpdateEntitySignalsMappings |  Batch updates `EntitySignalsMapping` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateEntitySignalsMappings(NetworkName parent, List<UpdateEntitySignalsMappingRequest> requests) 
  * batchUpdateEntitySignalsMappings(String parent, List<UpdateEntitySignalsMappingRequest> requests) 
  * batchUpdateEntitySignalsMappings(BatchUpdateEntitySignalsMappingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateEntitySignalsMappingsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EntitySignalsMappingServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EntitySignalsMappingServiceSettings entitySignalsMappingServiceSettings =
         EntitySignalsMappingServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create(entitySignalsMappingServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EntitySignalsMappingServiceSettings entitySignalsMappingServiceSettings =
         EntitySignalsMappingServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create(entitySignalsMappingServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EntitySignalsMappingServiceClient

## Static Methods 

### create()
    
    
    public static final EntitySignalsMappingServiceClient create()

Constructs an instance of EntitySignalsMappingServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EntitySignalsMappingServiceSettings settings)
    
    
    public static final EntitySignalsMappingServiceClient create(EntitySignalsMappingServiceSettings settings)

Constructs an instance of EntitySignalsMappingServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EntitySignalsMappingServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EntitySignalsMappingServiceStub stub)
    
    
    public static final EntitySignalsMappingServiceClient create(EntitySignalsMappingServiceStub stub)

Constructs an instance of EntitySignalsMappingServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(EntitySignalsMappingServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EntitySignalsMappingServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.EntitySignalsMappingServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient)` |   
  
## Constructors 

### EntitySignalsMappingServiceClient(EntitySignalsMappingServiceSettings settings)
    
    
    protected EntitySignalsMappingServiceClient(EntitySignalsMappingServiceSettings settings)

Constructs an instance of EntitySignalsMappingServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EntitySignalsMappingServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceSettings)`  
  
  
### EntitySignalsMappingServiceClient(EntitySignalsMappingServiceStub stub)
    
    
    protected EntitySignalsMappingServiceClient(EntitySignalsMappingServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EntitySignalsMappingServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.EntitySignalsMappingServiceStub)`  
  
  
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
  
### batchCreateEntitySignalsMappings(@Nullable NetworkName parent, List<CreateEntitySignalsMappingRequest> requests)
    
    
    public final BatchCreateEntitySignalsMappingsResponse batchCreateEntitySignalsMappings(@Nullable NetworkName parent, List<CreateEntitySignalsMappingRequest> requests)

Creates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateEntitySignalsMappingRequest> requests = new ArrayList<>();
       BatchCreateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchCreateEntitySignalsMappings(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `EntitySignalsMappings` will be created. Format: `networks/{network_code}` The parent field in the CreateEntitySignalsMappingRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateEntitySignalsMappingRequest)>`  
Required. The `EntitySignalsMapping` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsResponse)` |   
  
### batchCreateEntitySignalsMappings(BatchCreateEntitySignalsMappingsRequest request)
    
    
    public final BatchCreateEntitySignalsMappingsResponse batchCreateEntitySignalsMappings(BatchCreateEntitySignalsMappingsRequest request)

Creates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       BatchCreateEntitySignalsMappingsRequest request =
           BatchCreateEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateEntitySignalsMappingRequest>())
               .build();
       BatchCreateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchCreateEntitySignalsMappings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsResponse)` |   
  
### batchCreateEntitySignalsMappings(String parent, List<CreateEntitySignalsMappingRequest> requests)
    
    
    public final BatchCreateEntitySignalsMappingsResponse batchCreateEntitySignalsMappings(String parent, List<CreateEntitySignalsMappingRequest> requests)

Creates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateEntitySignalsMappingRequest> requests = new ArrayList<>();
       BatchCreateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchCreateEntitySignalsMappings(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `EntitySignalsMappings` will be created. Format: `networks/{network_code}` The parent field in the CreateEntitySignalsMappingRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateEntitySignalsMappingRequest)>`  
Required. The `EntitySignalsMapping` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsResponse)` |   
  
### batchCreateEntitySignalsMappingsCallable()
    
    
    public final UnaryCallable<BatchCreateEntitySignalsMappingsRequest,BatchCreateEntitySignalsMappingsResponse> batchCreateEntitySignalsMappingsCallable()

Creates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       BatchCreateEntitySignalsMappingsRequest request =
           BatchCreateEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateEntitySignalsMappingRequest>())
               .build();
       ApiFuture<BatchCreateEntitySignalsMappingsResponse> future =
           entitySignalsMappingServiceClient
               .batchCreateEntitySignalsMappingsCallable()
               .futureCall(request);
       // Do something.
       BatchCreateEntitySignalsMappingsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsRequest),[BatchCreateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateEntitySignalsMappingsResponse)>` |   
  
### batchUpdateEntitySignalsMappings(@Nullable NetworkName parent, List<UpdateEntitySignalsMappingRequest> requests)
    
    
    public final BatchUpdateEntitySignalsMappingsResponse batchUpdateEntitySignalsMappings(@Nullable NetworkName parent, List<UpdateEntitySignalsMappingRequest> requests)

Batch updates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateEntitySignalsMappingRequest> requests = new ArrayList<>();
       BatchUpdateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchUpdateEntitySignalsMappings(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `EntitySignalsMappings` will be updated. Format: `networks/{network_code}` The parent field in the UpdateEntitySignalsMappingRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateEntitySignalsMappingRequest)>`  
Required. The `EntitySignalsMapping` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsResponse)` |   
  
### batchUpdateEntitySignalsMappings(BatchUpdateEntitySignalsMappingsRequest request)
    
    
    public final BatchUpdateEntitySignalsMappingsResponse batchUpdateEntitySignalsMappings(BatchUpdateEntitySignalsMappingsRequest request)

Batch updates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       BatchUpdateEntitySignalsMappingsRequest request =
           BatchUpdateEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateEntitySignalsMappingRequest>())
               .build();
       BatchUpdateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchUpdateEntitySignalsMappings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsResponse)` |   
  
### batchUpdateEntitySignalsMappings(String parent, List<UpdateEntitySignalsMappingRequest> requests)
    
    
    public final BatchUpdateEntitySignalsMappingsResponse batchUpdateEntitySignalsMappings(String parent, List<UpdateEntitySignalsMappingRequest> requests)

Batch updates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateEntitySignalsMappingRequest> requests = new ArrayList<>();
       BatchUpdateEntitySignalsMappingsResponse response =
           entitySignalsMappingServiceClient.batchUpdateEntitySignalsMappings(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `EntitySignalsMappings` will be updated. Format: `networks/{network_code}` The parent field in the UpdateEntitySignalsMappingRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateEntitySignalsMappingRequest)>`  
Required. The `EntitySignalsMapping` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsResponse)` |   
  
### batchUpdateEntitySignalsMappingsCallable()
    
    
    public final UnaryCallable<BatchUpdateEntitySignalsMappingsRequest,BatchUpdateEntitySignalsMappingsResponse> batchUpdateEntitySignalsMappingsCallable()

Batch updates `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       BatchUpdateEntitySignalsMappingsRequest request =
           BatchUpdateEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateEntitySignalsMappingRequest>())
               .build();
       ApiFuture<BatchUpdateEntitySignalsMappingsResponse> future =
           entitySignalsMappingServiceClient
               .batchUpdateEntitySignalsMappingsCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateEntitySignalsMappingsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsRequest),[BatchUpdateEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateEntitySignalsMappingsResponse)>` |   
  
### close()
    
    
    public final void close()

### createEntitySignalsMapping(@Nullable NetworkName parent, EntitySignalsMapping entitySignalsMapping)
    
    
    public final EntitySignalsMapping createEntitySignalsMapping(@Nullable NetworkName parent, EntitySignalsMapping entitySignalsMapping)

Creates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       EntitySignalsMapping entitySignalsMapping = EntitySignalsMapping.newBuilder().build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.createEntitySignalsMapping(
               parent, entitySignalsMapping);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this EntitySignalsMapping will be created. Format: `networks/{network_code}`  
`entitySignalsMapping` | `[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)`  
Required. The EntitySignalsMapping object to create.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### createEntitySignalsMapping(CreateEntitySignalsMappingRequest request)
    
    
    public final EntitySignalsMapping createEntitySignalsMapping(CreateEntitySignalsMappingRequest request)

Creates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       CreateEntitySignalsMappingRequest request =
           CreateEntitySignalsMappingRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setEntitySignalsMapping(EntitySignalsMapping.newBuilder().build())
               .build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.createEntitySignalsMapping(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateEntitySignalsMappingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### createEntitySignalsMapping(String parent, EntitySignalsMapping entitySignalsMapping)
    
    
    public final EntitySignalsMapping createEntitySignalsMapping(String parent, EntitySignalsMapping entitySignalsMapping)

Creates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       EntitySignalsMapping entitySignalsMapping = EntitySignalsMapping.newBuilder().build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.createEntitySignalsMapping(
               parent, entitySignalsMapping);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this EntitySignalsMapping will be created. Format: `networks/{network_code}`  
`entitySignalsMapping` | `[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)`  
Required. The EntitySignalsMapping object to create.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### createEntitySignalsMappingCallable()
    
    
    public final UnaryCallable<CreateEntitySignalsMappingRequest,EntitySignalsMapping> createEntitySignalsMappingCallable()

Creates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       CreateEntitySignalsMappingRequest request =
           CreateEntitySignalsMappingRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setEntitySignalsMapping(EntitySignalsMapping.newBuilder().build())
               .build();
       ApiFuture<EntitySignalsMapping> future =
           entitySignalsMappingServiceClient
               .createEntitySignalsMappingCallable()
               .futureCall(request);
       // Do something.
       EntitySignalsMapping response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateEntitySignalsMappingRequest),[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)>` |   
  
### getEntitySignalsMapping(@Nullable EntitySignalsMappingName name)
    
    
    public final EntitySignalsMapping getEntitySignalsMapping(@Nullable EntitySignalsMappingName name)

Retrieves a `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       EntitySignalsMappingName name =
           EntitySignalsMappingName.of("[NETWORK_CODE]", "[ENTITY_SIGNALS_MAPPING]");
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.getEntitySignalsMapping(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.EntitySignalsMappingName`  
Required. The resource name of the EntitySignalsMapping. Format: `networks/{network_code}/entitySignalsMappings/{entity_signals_mapping_id}`  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### getEntitySignalsMapping(GetEntitySignalsMappingRequest request)
    
    
    public final EntitySignalsMapping getEntitySignalsMapping(GetEntitySignalsMappingRequest request)

Retrieves a `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       GetEntitySignalsMappingRequest request =
           GetEntitySignalsMappingRequest.newBuilder()
               .setName(
                   EntitySignalsMappingName.of("[NETWORK_CODE]", "[ENTITY_SIGNALS_MAPPING]")
                       .toString())
               .build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.getEntitySignalsMapping(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetEntitySignalsMappingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### getEntitySignalsMapping(String name)
    
    
    public final EntitySignalsMapping getEntitySignalsMapping(String name)

Retrieves a `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       String name =
           EntitySignalsMappingName.of("[NETWORK_CODE]", "[ENTITY_SIGNALS_MAPPING]").toString();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.getEntitySignalsMapping(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntitySignalsMapping. Format: `networks/{network_code}/entitySignalsMappings/{entity_signals_mapping_id}`  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### getEntitySignalsMappingCallable()
    
    
    public final UnaryCallable<GetEntitySignalsMappingRequest,EntitySignalsMapping> getEntitySignalsMappingCallable()

Retrieves a `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       GetEntitySignalsMappingRequest request =
           GetEntitySignalsMappingRequest.newBuilder()
               .setName(
                   EntitySignalsMappingName.of("[NETWORK_CODE]", "[ENTITY_SIGNALS_MAPPING]")
                       .toString())
               .build();
       ApiFuture<EntitySignalsMapping> future =
           entitySignalsMappingServiceClient.getEntitySignalsMappingCallable().futureCall(request);
       // Do something.
       EntitySignalsMapping response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetEntitySignalsMappingRequest),[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)>` |   
  
### getSettings()
    
    
    public final @Nullable EntitySignalsMappingServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.EntitySignalsMappingServiceSettings` |   
  
### getStub()
    
    
    public EntitySignalsMappingServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.EntitySignalsMappingServiceStub)` |   
  
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
  
### listEntitySignalsMappings(@Nullable NetworkName parent)
    
    
    public final EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse listEntitySignalsMappings(@Nullable NetworkName parent)

Lists `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (EntitySignalsMapping element :
           entitySignalsMappingServiceClient.listEntitySignalsMappings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of EntitySignalsMappings. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse)` |   
  
### listEntitySignalsMappings(ListEntitySignalsMappingsRequest request)
    
    
    public final EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse listEntitySignalsMappings(ListEntitySignalsMappingsRequest request)

Lists `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       ListEntitySignalsMappingsRequest request =
           ListEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (EntitySignalsMapping element :
           entitySignalsMappingServiceClient.listEntitySignalsMappings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListEntitySignalsMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse)` |   
  
### listEntitySignalsMappings(String parent)
    
    
    public final EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse listEntitySignalsMappings(String parent)

Lists `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (EntitySignalsMapping element :
           entitySignalsMappingServiceClient.listEntitySignalsMappings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of EntitySignalsMappings. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse)` |   
  
### listEntitySignalsMappingsCallable()
    
    
    public final UnaryCallable<ListEntitySignalsMappingsRequest,ListEntitySignalsMappingsResponse> listEntitySignalsMappingsCallable()

Lists `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       ListEntitySignalsMappingsRequest request =
           ListEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListEntitySignalsMappingsResponse response =
             entitySignalsMappingServiceClient.listEntitySignalsMappingsCallable().call(request);
         for (EntitySignalsMapping element : response.getEntitySignalsMappingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListEntitySignalsMappingsRequest),[ListEntitySignalsMappingsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListEntitySignalsMappingsResponse)>` |   
  
### listEntitySignalsMappingsPagedCallable()
    
    
    public final UnaryCallable<ListEntitySignalsMappingsRequest,EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse> listEntitySignalsMappingsPagedCallable()

Lists `EntitySignalsMapping` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       ListEntitySignalsMappingsRequest request =
           ListEntitySignalsMappingsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<EntitySignalsMapping> future =
           entitySignalsMappingServiceClient
               .listEntitySignalsMappingsPagedCallable()
               .futureCall(request);
       // Do something.
       for (EntitySignalsMapping element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntitySignalsMappingsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListEntitySignalsMappingsRequest),[ListEntitySignalsMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMappingServiceClient.ListEntitySignalsMappingsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateEntitySignalsMapping(EntitySignalsMapping entitySignalsMapping, FieldMask updateMask)
    
    
    public final EntitySignalsMapping updateEntitySignalsMapping(EntitySignalsMapping entitySignalsMapping, FieldMask updateMask)

Updates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       EntitySignalsMapping entitySignalsMapping = EntitySignalsMapping.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.updateEntitySignalsMapping(
               entitySignalsMapping, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entitySignalsMapping` | `[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)`  
Required. The `EntitySignalsMapping` to update. The EntitySignalsMapping's name is used to identify the EntitySignalsMapping to update. Format: `networks/{network_code}/entitySignalsMappings/{entity_signals_mapping}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### updateEntitySignalsMapping(UpdateEntitySignalsMappingRequest request)
    
    
    public final EntitySignalsMapping updateEntitySignalsMapping(UpdateEntitySignalsMappingRequest request)

Updates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       UpdateEntitySignalsMappingRequest request =
           UpdateEntitySignalsMappingRequest.newBuilder()
               .setEntitySignalsMapping(EntitySignalsMapping.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       EntitySignalsMapping response =
           entitySignalsMappingServiceClient.updateEntitySignalsMapping(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateEntitySignalsMappingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)` |   
  
### updateEntitySignalsMappingCallable()
    
    
    public final UnaryCallable<UpdateEntitySignalsMappingRequest,EntitySignalsMapping> updateEntitySignalsMappingCallable()

Updates an `EntitySignalsMapping` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EntitySignalsMappingServiceClient entitySignalsMappingServiceClient =
         EntitySignalsMappingServiceClient.create()) {
       UpdateEntitySignalsMappingRequest request =
           UpdateEntitySignalsMappingRequest.newBuilder()
               .setEntitySignalsMapping(EntitySignalsMapping.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<EntitySignalsMapping> future =
           entitySignalsMappingServiceClient
               .updateEntitySignalsMappingCallable()
               .futureCall(request);
       // Do something.
       EntitySignalsMapping response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntitySignalsMappingRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateEntitySignalsMappingRequest),[EntitySignalsMapping](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.EntitySignalsMapping)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
