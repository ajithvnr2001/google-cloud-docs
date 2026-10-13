---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient
title: Class ViewabilityProviderServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:09.283848+00:00
---

# Class ViewabilityProviderServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ViewabilityProviderServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ViewabilityProviderServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling ViewabilityProvider objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ViewabilityProviderName name =
           ViewabilityProviderName.of("[NETWORK_CODE]", "[VIEWABILITY_PROVIDER]");
       ViewabilityProvider response = viewabilityProviderServiceClient.getViewabilityProvider(name);
     }
     

Note: close() needs to be called on the ViewabilityProviderServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetViewabilityProvider |  Retrieves a ViewabilityProvider object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getViewabilityProvider(GetViewabilityProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getViewabilityProvider(ViewabilityProviderName name) 
  * getViewabilityProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getViewabilityProviderCallable() 

  
ListViewabilityProviders |  Lists ViewabilityProvider objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listViewabilityProviders(ListViewabilityProvidersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listViewabilityProviders(NetworkName parent) 
  * listViewabilityProviders(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listViewabilityProvidersPagedCallable() 
  * listViewabilityProvidersCallable() 

  
CreateViewabilityProvider |  Creates a ViewabilityProvider object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createViewabilityProvider(CreateViewabilityProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createViewabilityProvider(NetworkName parent, ViewabilityProvider viewabilityProvider) 
  * createViewabilityProvider(String parent, ViewabilityProvider viewabilityProvider) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createViewabilityProviderCallable() 

  
BatchCreateViewabilityProviders |  Creates ViewabilityProvider objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateViewabilityProviders(NetworkName parent, List<CreateViewabilityProviderRequest> requests) 
  * batchCreateViewabilityProviders(String parent, List<CreateViewabilityProviderRequest> requests) 
  * batchCreateViewabilityProviders(BatchCreateViewabilityProvidersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateViewabilityProvidersCallable() 

  
UpdateViewabilityProvider |  Updates a ViewabilityProvider object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateViewabilityProvider(UpdateViewabilityProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateViewabilityProvider(ViewabilityProvider viewabilityProvider, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateViewabilityProviderCallable() 

  
BatchUpdateViewabilityProviders |  Batch updates ViewabilityProvider objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateViewabilityProviders(NetworkName parent, List<UpdateViewabilityProviderRequest> requests) 
  * batchUpdateViewabilityProviders(String parent, List<UpdateViewabilityProviderRequest> requests) 
  * batchUpdateViewabilityProviders(BatchUpdateViewabilityProvidersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateViewabilityProvidersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ViewabilityProviderServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ViewabilityProviderServiceSettings viewabilityProviderServiceSettings =
         ViewabilityProviderServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create(viewabilityProviderServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ViewabilityProviderServiceSettings viewabilityProviderServiceSettings =
         ViewabilityProviderServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create(viewabilityProviderServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ViewabilityProviderServiceClient

## Static Methods 

### create()
    
    
    public static final ViewabilityProviderServiceClient create()

Constructs an instance of ViewabilityProviderServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ViewabilityProviderServiceSettings settings)
    
    
    public static final ViewabilityProviderServiceClient create(ViewabilityProviderServiceSettings settings)

Constructs an instance of ViewabilityProviderServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ViewabilityProviderServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ViewabilityProviderServiceStub stub)
    
    
    public static final ViewabilityProviderServiceClient create(ViewabilityProviderServiceStub stub)

Constructs an instance of ViewabilityProviderServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ViewabilityProviderServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ViewabilityProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ViewabilityProviderServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient)` |   
  
## Constructors 

### ViewabilityProviderServiceClient(ViewabilityProviderServiceSettings settings)
    
    
    protected ViewabilityProviderServiceClient(ViewabilityProviderServiceSettings settings)

Constructs an instance of ViewabilityProviderServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ViewabilityProviderServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceSettings)`  
  
  
### ViewabilityProviderServiceClient(ViewabilityProviderServiceStub stub)
    
    
    protected ViewabilityProviderServiceClient(ViewabilityProviderServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ViewabilityProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ViewabilityProviderServiceStub)`  
  
  
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
  
### batchCreateViewabilityProviders(@Nullable NetworkName parent, List<CreateViewabilityProviderRequest> requests)
    
    
    public final BatchCreateViewabilityProvidersResponse batchCreateViewabilityProviders(@Nullable NetworkName parent, List<CreateViewabilityProviderRequest> requests)

Creates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateViewabilityProviderRequest> requests = new ArrayList<>();
       BatchCreateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchCreateViewabilityProviders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where ViewabilityProviders will be created. Format: `networks/{network_code}` The parent field in the CreateViewabilityProviderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateViewabilityProviderRequest)>`  
Required. The ViewabilityProvider objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersResponse)` |   
  
### batchCreateViewabilityProviders(BatchCreateViewabilityProvidersRequest request)
    
    
    public final BatchCreateViewabilityProvidersResponse batchCreateViewabilityProviders(BatchCreateViewabilityProvidersRequest request)

Creates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       BatchCreateViewabilityProvidersRequest request =
           BatchCreateViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateViewabilityProviderRequest>())
               .build();
       BatchCreateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchCreateViewabilityProviders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersResponse)` |   
  
### batchCreateViewabilityProviders(String parent, List<CreateViewabilityProviderRequest> requests)
    
    
    public final BatchCreateViewabilityProvidersResponse batchCreateViewabilityProviders(String parent, List<CreateViewabilityProviderRequest> requests)

Creates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateViewabilityProviderRequest> requests = new ArrayList<>();
       BatchCreateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchCreateViewabilityProviders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where ViewabilityProviders will be created. Format: `networks/{network_code}` The parent field in the CreateViewabilityProviderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateViewabilityProviderRequest)>`  
Required. The ViewabilityProvider objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersResponse)` |   
  
### batchCreateViewabilityProvidersCallable()
    
    
    public final UnaryCallable<BatchCreateViewabilityProvidersRequest,BatchCreateViewabilityProvidersResponse> batchCreateViewabilityProvidersCallable()

Creates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       BatchCreateViewabilityProvidersRequest request =
           BatchCreateViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateViewabilityProviderRequest>())
               .build();
       ApiFuture<BatchCreateViewabilityProvidersResponse> future =
           viewabilityProviderServiceClient
               .batchCreateViewabilityProvidersCallable()
               .futureCall(request);
       // Do something.
       BatchCreateViewabilityProvidersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersRequest),[BatchCreateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateViewabilityProvidersResponse)>` |   
  
### batchUpdateViewabilityProviders(@Nullable NetworkName parent, List<UpdateViewabilityProviderRequest> requests)
    
    
    public final BatchUpdateViewabilityProvidersResponse batchUpdateViewabilityProviders(@Nullable NetworkName parent, List<UpdateViewabilityProviderRequest> requests)

Batch updates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateViewabilityProviderRequest> requests = new ArrayList<>();
       BatchUpdateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchUpdateViewabilityProviders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where ViewabilityProviders will be updated. Format: `networks/{network_code}` The parent field in the UpdateViewabilityProviderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateViewabilityProviderRequest)>`  
Required. The ViewabilityProvider objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersResponse)` |   
  
### batchUpdateViewabilityProviders(BatchUpdateViewabilityProvidersRequest request)
    
    
    public final BatchUpdateViewabilityProvidersResponse batchUpdateViewabilityProviders(BatchUpdateViewabilityProvidersRequest request)

Batch updates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       BatchUpdateViewabilityProvidersRequest request =
           BatchUpdateViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateViewabilityProviderRequest>())
               .build();
       BatchUpdateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchUpdateViewabilityProviders(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersResponse)` |   
  
### batchUpdateViewabilityProviders(String parent, List<UpdateViewabilityProviderRequest> requests)
    
    
    public final BatchUpdateViewabilityProvidersResponse batchUpdateViewabilityProviders(String parent, List<UpdateViewabilityProviderRequest> requests)

Batch updates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateViewabilityProviderRequest> requests = new ArrayList<>();
       BatchUpdateViewabilityProvidersResponse response =
           viewabilityProviderServiceClient.batchUpdateViewabilityProviders(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where ViewabilityProviders will be updated. Format: `networks/{network_code}` The parent field in the UpdateViewabilityProviderRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateViewabilityProviderRequest)>`  
Required. The ViewabilityProvider objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersResponse)` |   
  
### batchUpdateViewabilityProvidersCallable()
    
    
    public final UnaryCallable<BatchUpdateViewabilityProvidersRequest,BatchUpdateViewabilityProvidersResponse> batchUpdateViewabilityProvidersCallable()

Batch updates ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       BatchUpdateViewabilityProvidersRequest request =
           BatchUpdateViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateViewabilityProviderRequest>())
               .build();
       ApiFuture<BatchUpdateViewabilityProvidersResponse> future =
           viewabilityProviderServiceClient
               .batchUpdateViewabilityProvidersCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateViewabilityProvidersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersRequest),[BatchUpdateViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateViewabilityProvidersResponse)>` |   
  
### close()
    
    
    public final void close()

### createViewabilityProvider(@Nullable NetworkName parent, ViewabilityProvider viewabilityProvider)
    
    
    public final ViewabilityProvider createViewabilityProvider(@Nullable NetworkName parent, ViewabilityProvider viewabilityProvider)

Creates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       ViewabilityProvider viewabilityProvider = ViewabilityProvider.newBuilder().build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.createViewabilityProvider(parent, viewabilityProvider);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this ViewabilityProvider will be created. Format: `networks/{network_code}`  
`viewabilityProvider` | `[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)`  
Required. The ViewabilityProvider to create.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### createViewabilityProvider(CreateViewabilityProviderRequest request)
    
    
    public final ViewabilityProvider createViewabilityProvider(CreateViewabilityProviderRequest request)

Creates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       CreateViewabilityProviderRequest request =
           CreateViewabilityProviderRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setViewabilityProvider(ViewabilityProvider.newBuilder().build())
               .build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.createViewabilityProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateViewabilityProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### createViewabilityProvider(String parent, ViewabilityProvider viewabilityProvider)
    
    
    public final ViewabilityProvider createViewabilityProvider(String parent, ViewabilityProvider viewabilityProvider)

Creates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       ViewabilityProvider viewabilityProvider = ViewabilityProvider.newBuilder().build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.createViewabilityProvider(parent, viewabilityProvider);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this ViewabilityProvider will be created. Format: `networks/{network_code}`  
`viewabilityProvider` | `[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)`  
Required. The ViewabilityProvider to create.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### createViewabilityProviderCallable()
    
    
    public final UnaryCallable<CreateViewabilityProviderRequest,ViewabilityProvider> createViewabilityProviderCallable()

Creates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       CreateViewabilityProviderRequest request =
           CreateViewabilityProviderRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setViewabilityProvider(ViewabilityProvider.newBuilder().build())
               .build();
       ApiFuture<ViewabilityProvider> future =
           viewabilityProviderServiceClient.createViewabilityProviderCallable().futureCall(request);
       // Do something.
       ViewabilityProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateViewabilityProviderRequest),[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)>` |   
  
### getSettings()
    
    
    public final @Nullable ViewabilityProviderServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ViewabilityProviderServiceSettings` |   
  
### getStub()
    
    
    public ViewabilityProviderServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ViewabilityProviderServiceStub)` |   
  
### getViewabilityProvider(@Nullable ViewabilityProviderName name)
    
    
    public final ViewabilityProvider getViewabilityProvider(@Nullable ViewabilityProviderName name)

Retrieves a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ViewabilityProviderName name =
           ViewabilityProviderName.of("[NETWORK_CODE]", "[VIEWABILITY_PROVIDER]");
       ViewabilityProvider response = viewabilityProviderServiceClient.getViewabilityProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ViewabilityProviderName`  
Required. The resource name of the ViewabilityProvider. Format: `networks/{network_code}/viewabilityProviders/{viewability_provider}`  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### getViewabilityProvider(GetViewabilityProviderRequest request)
    
    
    public final ViewabilityProvider getViewabilityProvider(GetViewabilityProviderRequest request)

Retrieves a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       GetViewabilityProviderRequest request =
           GetViewabilityProviderRequest.newBuilder()
               .setName(
                   ViewabilityProviderName.of("[NETWORK_CODE]", "[VIEWABILITY_PROVIDER]").toString())
               .build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.getViewabilityProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetViewabilityProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### getViewabilityProvider(String name)
    
    
    public final ViewabilityProvider getViewabilityProvider(String name)

Retrieves a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       String name =
           ViewabilityProviderName.of("[NETWORK_CODE]", "[VIEWABILITY_PROVIDER]").toString();
       ViewabilityProvider response = viewabilityProviderServiceClient.getViewabilityProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ViewabilityProvider. Format: `networks/{network_code}/viewabilityProviders/{viewability_provider}`  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### getViewabilityProviderCallable()
    
    
    public final UnaryCallable<GetViewabilityProviderRequest,ViewabilityProvider> getViewabilityProviderCallable()

Retrieves a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       GetViewabilityProviderRequest request =
           GetViewabilityProviderRequest.newBuilder()
               .setName(
                   ViewabilityProviderName.of("[NETWORK_CODE]", "[VIEWABILITY_PROVIDER]").toString())
               .build();
       ApiFuture<ViewabilityProvider> future =
           viewabilityProviderServiceClient.getViewabilityProviderCallable().futureCall(request);
       // Do something.
       ViewabilityProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetViewabilityProviderRequest),[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)>` |   
  
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
  
### listViewabilityProviders(@Nullable NetworkName parent)
    
    
    public final ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse listViewabilityProviders(@Nullable NetworkName parent)

Lists ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ViewabilityProvider element :
           viewabilityProviderServiceClient.listViewabilityProviders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ViewabilityProviders. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse)` |   
  
### listViewabilityProviders(ListViewabilityProvidersRequest request)
    
    
    public final ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse listViewabilityProviders(ListViewabilityProvidersRequest request)

Lists ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ListViewabilityProvidersRequest request =
           ListViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ViewabilityProvider element :
           viewabilityProviderServiceClient.listViewabilityProviders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListViewabilityProvidersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse)` |   
  
### listViewabilityProviders(String parent)
    
    
    public final ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse listViewabilityProviders(String parent)

Lists ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ViewabilityProvider element :
           viewabilityProviderServiceClient.listViewabilityProviders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ViewabilityProviders. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse)` |   
  
### listViewabilityProvidersCallable()
    
    
    public final UnaryCallable<ListViewabilityProvidersRequest,ListViewabilityProvidersResponse> listViewabilityProvidersCallable()

Lists ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ListViewabilityProvidersRequest request =
           ListViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListViewabilityProvidersResponse response =
             viewabilityProviderServiceClient.listViewabilityProvidersCallable().call(request);
         for (ViewabilityProvider element : response.getViewabilityProvidersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListViewabilityProvidersRequest),[ListViewabilityProvidersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListViewabilityProvidersResponse)>` |   
  
### listViewabilityProvidersPagedCallable()
    
    
    public final UnaryCallable<ListViewabilityProvidersRequest,ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse> listViewabilityProvidersPagedCallable()

Lists ViewabilityProvider objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ListViewabilityProvidersRequest request =
           ListViewabilityProvidersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ViewabilityProvider> future =
           viewabilityProviderServiceClient
               .listViewabilityProvidersPagedCallable()
               .futureCall(request);
       // Do something.
       for (ViewabilityProvider element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViewabilityProvidersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListViewabilityProvidersRequest),[ListViewabilityProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProviderServiceClient.ListViewabilityProvidersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateViewabilityProvider(UpdateViewabilityProviderRequest request)
    
    
    public final ViewabilityProvider updateViewabilityProvider(UpdateViewabilityProviderRequest request)

Updates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       UpdateViewabilityProviderRequest request =
           UpdateViewabilityProviderRequest.newBuilder()
               .setViewabilityProvider(ViewabilityProvider.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.updateViewabilityProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateViewabilityProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### updateViewabilityProvider(ViewabilityProvider viewabilityProvider, FieldMask updateMask)
    
    
    public final ViewabilityProvider updateViewabilityProvider(ViewabilityProvider viewabilityProvider, FieldMask updateMask)

Updates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       ViewabilityProvider viewabilityProvider = ViewabilityProvider.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ViewabilityProvider response =
           viewabilityProviderServiceClient.updateViewabilityProvider(
               viewabilityProvider, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`viewabilityProvider` | `[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)`  
Required. The ViewabilityProvider to update. The ViewabilityProvider's `name` is used to identify the ViewabilityProvider to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)` |   
  
### updateViewabilityProviderCallable()
    
    
    public final UnaryCallable<UpdateViewabilityProviderRequest,ViewabilityProvider> updateViewabilityProviderCallable()

Updates a ViewabilityProvider object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ViewabilityProviderServiceClient viewabilityProviderServiceClient =
         ViewabilityProviderServiceClient.create()) {
       UpdateViewabilityProviderRequest request =
           UpdateViewabilityProviderRequest.newBuilder()
               .setViewabilityProvider(ViewabilityProvider.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ViewabilityProvider> future =
           viewabilityProviderServiceClient.updateViewabilityProviderCallable().futureCall(request);
       // Do something.
       ViewabilityProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateViewabilityProviderRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateViewabilityProviderRequest),[ViewabilityProvider](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ViewabilityProvider)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
