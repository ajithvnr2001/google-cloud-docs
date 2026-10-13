---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient
title: Class CreativeWrapperServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:39.129181+00:00
---

# Class CreativeWrapperServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CreativeWrapperServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CreativeWrapperServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CreativeWrapper` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       CreativeWrapperName name = CreativeWrapperName.of("[NETWORK_CODE]", "[CREATIVE_WRAPPER]");
       CreativeWrapper response = creativeWrapperServiceClient.getCreativeWrapper(name);
     }
     

Note: close() needs to be called on the CreativeWrapperServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCreativeWrapper |  Retrieves a `CreativeWrapper` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCreativeWrapper(GetCreativeWrapperRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCreativeWrapper(CreativeWrapperName name) 
  * getCreativeWrapper(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCreativeWrapperCallable() 

  
ListCreativeWrappers |  Lists `CreativeWrapper` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCreativeWrappers(ListCreativeWrappersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCreativeWrappers(NetworkName parent) 
  * listCreativeWrappers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCreativeWrappersPagedCallable() 
  * listCreativeWrappersCallable() 

  
CreateCreativeWrapper |  Creates a `CreativeWrapper` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCreativeWrapper(CreateCreativeWrapperRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCreativeWrapper(NetworkName parent, CreativeWrapper creativeWrapper) 
  * createCreativeWrapper(String parent, CreativeWrapper creativeWrapper) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCreativeWrapperCallable() 

  
BatchCreateCreativeWrappers |  Creates `CreativeWrapper` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCreativeWrappers(NetworkName parent, List<CreateCreativeWrapperRequest> requests) 
  * batchCreateCreativeWrappers(String parent, List<CreateCreativeWrapperRequest> requests) 
  * batchCreateCreativeWrappers(BatchCreateCreativeWrappersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCreativeWrappersCallable() 

  
UpdateCreativeWrapper |  Updates a `CreativeWrapper` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCreativeWrapper(UpdateCreativeWrapperRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCreativeWrapper(CreativeWrapper creativeWrapper, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCreativeWrapperCallable() 

  
BatchUpdateCreativeWrappers |  Batch updates `CreativeWrapper` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCreativeWrappers(NetworkName parent, List<UpdateCreativeWrapperRequest> requests) 
  * batchUpdateCreativeWrappers(String parent, List<UpdateCreativeWrapperRequest> requests) 
  * batchUpdateCreativeWrappers(BatchUpdateCreativeWrappersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCreativeWrappersCallable() 

  
BatchActivateCreativeWrappers |  Batch activates `CreativeWrapper` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCreativeWrappers(BatchActivateCreativeWrappersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCreativeWrappers(NetworkName parent, List<String> names) 
  * batchActivateCreativeWrappers(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCreativeWrappersCallable() 

  
BatchDeactivateCreativeWrappers |  Deactivates a list of `CreativeWrapper` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCreativeWrappers(BatchDeactivateCreativeWrappersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateCreativeWrappers(NetworkName parent, List<String> names) 
  * batchDeactivateCreativeWrappers(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCreativeWrappersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CreativeWrapperServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeWrapperServiceSettings creativeWrapperServiceSettings =
         CreativeWrapperServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create(creativeWrapperServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeWrapperServiceSettings creativeWrapperServiceSettings =
         CreativeWrapperServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create(creativeWrapperServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CreativeWrapperServiceClient

## Static Methods 

### create()
    
    
    public static final CreativeWrapperServiceClient create()

Constructs an instance of CreativeWrapperServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeWrapperServiceSettings settings)
    
    
    public static final CreativeWrapperServiceClient create(CreativeWrapperServiceSettings settings)

Constructs an instance of CreativeWrapperServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeWrapperServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeWrapperServiceStub stub)
    
    
    public static final CreativeWrapperServiceClient create(CreativeWrapperServiceStub stub)

Constructs an instance of CreativeWrapperServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CreativeWrapperServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeWrapperServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeWrapperServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient)` |   
  
## Constructors 

### CreativeWrapperServiceClient(CreativeWrapperServiceSettings settings)
    
    
    protected CreativeWrapperServiceClient(CreativeWrapperServiceSettings settings)

Constructs an instance of CreativeWrapperServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeWrapperServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceSettings)`  
  
  
### CreativeWrapperServiceClient(CreativeWrapperServiceStub stub)
    
    
    protected CreativeWrapperServiceClient(CreativeWrapperServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeWrapperServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeWrapperServiceStub)`  
  
  
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
  
### batchActivateCreativeWrappers(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCreativeWrappersResponse batchActivateCreativeWrappers(@Nullable NetworkName parent, List<String> names)

Batch activates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchActivateCreativeWrappers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CreativeWrapper` objects to activate. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersResponse)` |   
  
### batchActivateCreativeWrappers(BatchActivateCreativeWrappersRequest request)
    
    
    public final BatchActivateCreativeWrappersResponse batchActivateCreativeWrappers(BatchActivateCreativeWrappersRequest request)

Batch activates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchActivateCreativeWrappersRequest request =
           BatchActivateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchActivateCreativeWrappers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersResponse)` |   
  
### batchActivateCreativeWrappers(String parent, List<String> names)
    
    
    public final BatchActivateCreativeWrappersResponse batchActivateCreativeWrappers(String parent, List<String> names)

Batch activates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchActivateCreativeWrappers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CreativeWrapper` objects to activate. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersResponse)` |   
  
### batchActivateCreativeWrappersCallable()
    
    
    public final UnaryCallable<BatchActivateCreativeWrappersRequest,BatchActivateCreativeWrappersResponse> batchActivateCreativeWrappersCallable()

Batch activates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchActivateCreativeWrappersRequest request =
           BatchActivateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCreativeWrappersResponse> future =
           creativeWrapperServiceClient.batchActivateCreativeWrappersCallable().futureCall(request);
       // Do something.
       BatchActivateCreativeWrappersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersRequest),[BatchActivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCreativeWrappersResponse)>` |   
  
### batchCreateCreativeWrappers(@Nullable NetworkName parent, List<CreateCreativeWrapperRequest> requests)
    
    
    public final BatchCreateCreativeWrappersResponse batchCreateCreativeWrappers(@Nullable NetworkName parent, List<CreateCreativeWrapperRequest> requests)

Creates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCreativeWrapperRequest> requests = new ArrayList<>();
       BatchCreateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchCreateCreativeWrappers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CreativeWrappers` will be created. Format: `networks/{network_code}` The parent field in the CreateCreativeWrapperRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeWrapperRequest)>`  
Required. The `CreativeWrapper` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersResponse)` |   
  
### batchCreateCreativeWrappers(BatchCreateCreativeWrappersRequest request)
    
    
    public final BatchCreateCreativeWrappersResponse batchCreateCreativeWrappers(BatchCreateCreativeWrappersRequest request)

Creates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchCreateCreativeWrappersRequest request =
           BatchCreateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCreativeWrapperRequest>())
               .build();
       BatchCreateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchCreateCreativeWrappers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersResponse)` |   
  
### batchCreateCreativeWrappers(String parent, List<CreateCreativeWrapperRequest> requests)
    
    
    public final BatchCreateCreativeWrappersResponse batchCreateCreativeWrappers(String parent, List<CreateCreativeWrapperRequest> requests)

Creates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCreativeWrapperRequest> requests = new ArrayList<>();
       BatchCreateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchCreateCreativeWrappers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CreativeWrappers` will be created. Format: `networks/{network_code}` The parent field in the CreateCreativeWrapperRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeWrapperRequest)>`  
Required. The `CreativeWrapper` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersResponse)` |   
  
### batchCreateCreativeWrappersCallable()
    
    
    public final UnaryCallable<BatchCreateCreativeWrappersRequest,BatchCreateCreativeWrappersResponse> batchCreateCreativeWrappersCallable()

Creates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchCreateCreativeWrappersRequest request =
           BatchCreateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCreativeWrapperRequest>())
               .build();
       ApiFuture<BatchCreateCreativeWrappersResponse> future =
           creativeWrapperServiceClient.batchCreateCreativeWrappersCallable().futureCall(request);
       // Do something.
       BatchCreateCreativeWrappersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersRequest),[BatchCreateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCreativeWrappersResponse)>` |   
  
### batchDeactivateCreativeWrappers(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateCreativeWrappersResponse batchDeactivateCreativeWrappers(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchDeactivateCreativeWrappers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CreativeWrapper` objects to deactivate. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse)` |   
  
### batchDeactivateCreativeWrappers(BatchDeactivateCreativeWrappersRequest request)
    
    
    public final BatchDeactivateCreativeWrappersResponse batchDeactivateCreativeWrappers(BatchDeactivateCreativeWrappersRequest request)

Deactivates a list of `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchDeactivateCreativeWrappersRequest request =
           BatchDeactivateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchDeactivateCreativeWrappers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse)` |   
  
### batchDeactivateCreativeWrappers(String parent, List<String> names)
    
    
    public final BatchDeactivateCreativeWrappersResponse batchDeactivateCreativeWrappers(String parent, List<String> names)

Deactivates a list of `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchDeactivateCreativeWrappers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CreativeWrapper` objects to deactivate. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse)` |   
  
### batchDeactivateCreativeWrappersCallable()
    
    
    public final UnaryCallable<BatchDeactivateCreativeWrappersRequest,BatchDeactivateCreativeWrappersResponse> batchDeactivateCreativeWrappersCallable()

Deactivates a list of `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchDeactivateCreativeWrappersRequest request =
           BatchDeactivateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateCreativeWrappersResponse> future =
           creativeWrapperServiceClient
               .batchDeactivateCreativeWrappersCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateCreativeWrappersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersRequest),[BatchDeactivateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse)>` |   
  
### batchUpdateCreativeWrappers(@Nullable NetworkName parent, List<UpdateCreativeWrapperRequest> requests)
    
    
    public final BatchUpdateCreativeWrappersResponse batchUpdateCreativeWrappers(@Nullable NetworkName parent, List<UpdateCreativeWrapperRequest> requests)

Batch updates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCreativeWrapperRequest> requests = new ArrayList<>();
       BatchUpdateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchUpdateCreativeWrappers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CreativeWrappers` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCreativeWrapperRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeWrapperRequest)>`  
Required. The `CreativeWrapper` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse)` |   
  
### batchUpdateCreativeWrappers(BatchUpdateCreativeWrappersRequest request)
    
    
    public final BatchUpdateCreativeWrappersResponse batchUpdateCreativeWrappers(BatchUpdateCreativeWrappersRequest request)

Batch updates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchUpdateCreativeWrappersRequest request =
           BatchUpdateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCreativeWrapperRequest>())
               .build();
       BatchUpdateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchUpdateCreativeWrappers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse)` |   
  
### batchUpdateCreativeWrappers(String parent, List<UpdateCreativeWrapperRequest> requests)
    
    
    public final BatchUpdateCreativeWrappersResponse batchUpdateCreativeWrappers(String parent, List<UpdateCreativeWrapperRequest> requests)

Batch updates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCreativeWrapperRequest> requests = new ArrayList<>();
       BatchUpdateCreativeWrappersResponse response =
           creativeWrapperServiceClient.batchUpdateCreativeWrappers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CreativeWrappers` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCreativeWrapperRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeWrapperRequest)>`  
Required. The `CreativeWrapper` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse)` |   
  
### batchUpdateCreativeWrappersCallable()
    
    
    public final UnaryCallable<BatchUpdateCreativeWrappersRequest,BatchUpdateCreativeWrappersResponse> batchUpdateCreativeWrappersCallable()

Batch updates `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       BatchUpdateCreativeWrappersRequest request =
           BatchUpdateCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCreativeWrapperRequest>())
               .build();
       ApiFuture<BatchUpdateCreativeWrappersResponse> future =
           creativeWrapperServiceClient.batchUpdateCreativeWrappersCallable().futureCall(request);
       // Do something.
       BatchUpdateCreativeWrappersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersRequest),[BatchUpdateCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse)>` |   
  
### close()
    
    
    public final void close()

### createCreativeWrapper(@Nullable NetworkName parent, CreativeWrapper creativeWrapper)
    
    
    public final CreativeWrapper createCreativeWrapper(@Nullable NetworkName parent, CreativeWrapper creativeWrapper)

Creates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CreativeWrapper creativeWrapper = CreativeWrapper.newBuilder().build();
       CreativeWrapper response =
           creativeWrapperServiceClient.createCreativeWrapper(parent, creativeWrapper);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `CreativeWrapper` will be created. Format: `networks/{network_code}`  
`creativeWrapper` | `[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)`  
Required. The `CreativeWrapper` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### createCreativeWrapper(CreateCreativeWrapperRequest request)
    
    
    public final CreativeWrapper createCreativeWrapper(CreateCreativeWrapperRequest request)

Creates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       CreateCreativeWrapperRequest request =
           CreateCreativeWrapperRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCreativeWrapper(CreativeWrapper.newBuilder().build())
               .build();
       CreativeWrapper response = creativeWrapperServiceClient.createCreativeWrapper(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeWrapperRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### createCreativeWrapper(String parent, CreativeWrapper creativeWrapper)
    
    
    public final CreativeWrapper createCreativeWrapper(String parent, CreativeWrapper creativeWrapper)

Creates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CreativeWrapper creativeWrapper = CreativeWrapper.newBuilder().build();
       CreativeWrapper response =
           creativeWrapperServiceClient.createCreativeWrapper(parent, creativeWrapper);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `CreativeWrapper` will be created. Format: `networks/{network_code}`  
`creativeWrapper` | `[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)`  
Required. The `CreativeWrapper` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### createCreativeWrapperCallable()
    
    
    public final UnaryCallable<CreateCreativeWrapperRequest,CreativeWrapper> createCreativeWrapperCallable()

Creates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       CreateCreativeWrapperRequest request =
           CreateCreativeWrapperRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCreativeWrapper(CreativeWrapper.newBuilder().build())
               .build();
       ApiFuture<CreativeWrapper> future =
           creativeWrapperServiceClient.createCreativeWrapperCallable().futureCall(request);
       // Do something.
       CreativeWrapper response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCreativeWrapperRequest),[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)>` |   
  
### getCreativeWrapper(@Nullable CreativeWrapperName name)
    
    
    public final CreativeWrapper getCreativeWrapper(@Nullable CreativeWrapperName name)

Retrieves a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       CreativeWrapperName name = CreativeWrapperName.of("[NETWORK_CODE]", "[CREATIVE_WRAPPER]");
       CreativeWrapper response = creativeWrapperServiceClient.getCreativeWrapper(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeWrapperName`  
Required. The resource name of the CreativeWrapper. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### getCreativeWrapper(GetCreativeWrapperRequest request)
    
    
    public final CreativeWrapper getCreativeWrapper(GetCreativeWrapperRequest request)

Retrieves a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       GetCreativeWrapperRequest request =
           GetCreativeWrapperRequest.newBuilder()
               .setName(CreativeWrapperName.of("[NETWORK_CODE]", "[CREATIVE_WRAPPER]").toString())
               .build();
       CreativeWrapper response = creativeWrapperServiceClient.getCreativeWrapper(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeWrapperRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### getCreativeWrapper(String name)
    
    
    public final CreativeWrapper getCreativeWrapper(String name)

Retrieves a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String name = CreativeWrapperName.of("[NETWORK_CODE]", "[CREATIVE_WRAPPER]").toString();
       CreativeWrapper response = creativeWrapperServiceClient.getCreativeWrapper(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CreativeWrapper. Format: `networks/{network_code}/creativeWrappers/{creative_wrapper_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### getCreativeWrapperCallable()
    
    
    public final UnaryCallable<GetCreativeWrapperRequest,CreativeWrapper> getCreativeWrapperCallable()

Retrieves a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       GetCreativeWrapperRequest request =
           GetCreativeWrapperRequest.newBuilder()
               .setName(CreativeWrapperName.of("[NETWORK_CODE]", "[CREATIVE_WRAPPER]").toString())
               .build();
       ApiFuture<CreativeWrapper> future =
           creativeWrapperServiceClient.getCreativeWrapperCallable().futureCall(request);
       // Do something.
       CreativeWrapper response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeWrapperRequest),[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)>` |   
  
### getSettings()
    
    
    public final @Nullable CreativeWrapperServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeWrapperServiceSettings` |   
  
### getStub()
    
    
    public CreativeWrapperServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeWrapperServiceStub)` |   
  
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
  
### listCreativeWrappers(@Nullable NetworkName parent)
    
    
    public final CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse listCreativeWrappers(@Nullable NetworkName parent)

Lists `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CreativeWrapper element :
           creativeWrapperServiceClient.listCreativeWrappers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CreativeWrappers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse)` |   
  
### listCreativeWrappers(ListCreativeWrappersRequest request)
    
    
    public final CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse listCreativeWrappers(ListCreativeWrappersRequest request)

Lists `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       ListCreativeWrappersRequest request =
           ListCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CreativeWrapper element :
           creativeWrapperServiceClient.listCreativeWrappers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeWrappersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse)` |   
  
### listCreativeWrappers(String parent)
    
    
    public final CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse listCreativeWrappers(String parent)

Lists `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CreativeWrapper element :
           creativeWrapperServiceClient.listCreativeWrappers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CreativeWrappers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse)` |   
  
### listCreativeWrappersCallable()
    
    
    public final UnaryCallable<ListCreativeWrappersRequest,ListCreativeWrappersResponse> listCreativeWrappersCallable()

Lists `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       ListCreativeWrappersRequest request =
           ListCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCreativeWrappersResponse response =
             creativeWrapperServiceClient.listCreativeWrappersCallable().call(request);
         for (CreativeWrapper element : response.getCreativeWrappersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeWrappersRequest),[ListCreativeWrappersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeWrappersResponse)>` |   
  
### listCreativeWrappersPagedCallable()
    
    
    public final UnaryCallable<ListCreativeWrappersRequest,CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse> listCreativeWrappersPagedCallable()

Lists `CreativeWrapper` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       ListCreativeWrappersRequest request =
           ListCreativeWrappersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CreativeWrapper> future =
           creativeWrapperServiceClient.listCreativeWrappersPagedCallable().futureCall(request);
       // Do something.
       for (CreativeWrapper element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeWrappersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeWrappersRequest),[ListCreativeWrappersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapperServiceClient.ListCreativeWrappersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCreativeWrapper(CreativeWrapper creativeWrapper, FieldMask updateMask)
    
    
    public final CreativeWrapper updateCreativeWrapper(CreativeWrapper creativeWrapper, FieldMask updateMask)

Updates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       CreativeWrapper creativeWrapper = CreativeWrapper.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CreativeWrapper response =
           creativeWrapperServiceClient.updateCreativeWrapper(creativeWrapper, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`creativeWrapper` | `[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)`  
Required. The `CreativeWrapper` to update. The `CreativeWrapper`'s `name` is used to identify the `CreativeWrapper` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### updateCreativeWrapper(UpdateCreativeWrapperRequest request)
    
    
    public final CreativeWrapper updateCreativeWrapper(UpdateCreativeWrapperRequest request)

Updates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       UpdateCreativeWrapperRequest request =
           UpdateCreativeWrapperRequest.newBuilder()
               .setCreativeWrapper(CreativeWrapper.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CreativeWrapper response = creativeWrapperServiceClient.updateCreativeWrapper(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeWrapperRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)` |   
  
### updateCreativeWrapperCallable()
    
    
    public final UnaryCallable<UpdateCreativeWrapperRequest,CreativeWrapper> updateCreativeWrapperCallable()

Updates a `CreativeWrapper` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeWrapperServiceClient creativeWrapperServiceClient =
         CreativeWrapperServiceClient.create()) {
       UpdateCreativeWrapperRequest request =
           UpdateCreativeWrapperRequest.newBuilder()
               .setCreativeWrapper(CreativeWrapper.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CreativeWrapper> future =
           creativeWrapperServiceClient.updateCreativeWrapperCallable().futureCall(request);
       // Do something.
       CreativeWrapper response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCreativeWrapperRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCreativeWrapperRequest),[CreativeWrapper](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeWrapper)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
