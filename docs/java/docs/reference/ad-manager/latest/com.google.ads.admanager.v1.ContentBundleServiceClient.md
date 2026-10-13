---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient
title: Class ContentBundleServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:33.954881+00:00
---

# Class ContentBundleServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ContentBundleServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ContentBundleServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `ContentBundle` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       ContentBundleName name = ContentBundleName.of("[NETWORK_CODE]", "[CONTENT_BUNDLE]");
       ContentBundle response = contentBundleServiceClient.getContentBundle(name);
     }
     

Note: close() needs to be called on the ContentBundleServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetContentBundle |  Retrieves a `ContentBundle` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getContentBundle(GetContentBundleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getContentBundle(ContentBundleName name) 
  * getContentBundle(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getContentBundleCallable() 

  
ListContentBundles |  Lists `ContentBundle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContentBundles(ListContentBundlesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContentBundles(NetworkName parent) 
  * listContentBundles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContentBundlesPagedCallable() 
  * listContentBundlesCallable() 

  
BatchActivateContentBundles |  Activate a list of `ContentBundle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateContentBundles(BatchActivateContentBundlesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateContentBundles(NetworkName parent, List<String> names) 
  * batchActivateContentBundles(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateContentBundlesCallable() 

  
BatchDeactivateContentBundles |  Deactivates a list of `ContentBundle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateContentBundles(BatchDeactivateContentBundlesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateContentBundles(NetworkName parent, List<String> names) 
  * batchDeactivateContentBundles(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateContentBundlesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ContentBundleServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContentBundleServiceSettings contentBundleServiceSettings =
         ContentBundleServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create(contentBundleServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContentBundleServiceSettings contentBundleServiceSettings =
         ContentBundleServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create(contentBundleServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ContentBundleServiceClient

## Static Methods 

### create()
    
    
    public static final ContentBundleServiceClient create()

Constructs an instance of ContentBundleServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContentBundleServiceSettings settings)
    
    
    public static final ContentBundleServiceClient create(ContentBundleServiceSettings settings)

Constructs an instance of ContentBundleServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContentBundleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContentBundleServiceStub stub)
    
    
    public static final ContentBundleServiceClient create(ContentBundleServiceStub stub)

Constructs an instance of ContentBundleServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ContentBundleServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContentBundleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentBundleServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient)` |   
  
## Constructors 

### ContentBundleServiceClient(ContentBundleServiceSettings settings)
    
    
    protected ContentBundleServiceClient(ContentBundleServiceSettings settings)

Constructs an instance of ContentBundleServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContentBundleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceSettings)`  
  
  
### ContentBundleServiceClient(ContentBundleServiceStub stub)
    
    
    protected ContentBundleServiceClient(ContentBundleServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContentBundleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentBundleServiceStub)`  
  
  
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
  
### batchActivateContentBundles(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateContentBundlesResponse batchActivateContentBundles(@Nullable NetworkName parent, List<String> names)

Activate a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateContentBundlesResponse response =
           contentBundleServiceClient.batchActivateContentBundles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `ContentBundles` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `ContentBundle`s to activate. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesResponse)` |   
  
### batchActivateContentBundles(BatchActivateContentBundlesRequest request)
    
    
    public final BatchActivateContentBundlesResponse batchActivateContentBundles(BatchActivateContentBundlesRequest request)

Activate a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       BatchActivateContentBundlesRequest request =
           BatchActivateContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateContentBundlesResponse response =
           contentBundleServiceClient.batchActivateContentBundles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesResponse)` |   
  
### batchActivateContentBundles(String parent, List<String> names)
    
    
    public final BatchActivateContentBundlesResponse batchActivateContentBundles(String parent, List<String> names)

Activate a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateContentBundlesResponse response =
           contentBundleServiceClient.batchActivateContentBundles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `ContentBundles` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `ContentBundle`s to activate. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesResponse)` |   
  
### batchActivateContentBundlesCallable()
    
    
    public final UnaryCallable<BatchActivateContentBundlesRequest,BatchActivateContentBundlesResponse> batchActivateContentBundlesCallable()

Activate a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       BatchActivateContentBundlesRequest request =
           BatchActivateContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateContentBundlesResponse> future =
           contentBundleServiceClient.batchActivateContentBundlesCallable().futureCall(request);
       // Do something.
       BatchActivateContentBundlesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesRequest),[BatchActivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateContentBundlesResponse)>` |   
  
### batchDeactivateContentBundles(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateContentBundlesResponse batchDeactivateContentBundles(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateContentBundlesResponse response =
           contentBundleServiceClient.batchDeactivateContentBundles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `ContentBundles` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `ContentBundle`s to deactivate. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesResponse)` |   
  
### batchDeactivateContentBundles(BatchDeactivateContentBundlesRequest request)
    
    
    public final BatchDeactivateContentBundlesResponse batchDeactivateContentBundles(BatchDeactivateContentBundlesRequest request)

Deactivates a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       BatchDeactivateContentBundlesRequest request =
           BatchDeactivateContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateContentBundlesResponse response =
           contentBundleServiceClient.batchDeactivateContentBundles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesResponse)` |   
  
### batchDeactivateContentBundles(String parent, List<String> names)
    
    
    public final BatchDeactivateContentBundlesResponse batchDeactivateContentBundles(String parent, List<String> names)

Deactivates a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateContentBundlesResponse response =
           contentBundleServiceClient.batchDeactivateContentBundles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `ContentBundles` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `ContentBundle`s to deactivate. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesResponse)` |   
  
### batchDeactivateContentBundlesCallable()
    
    
    public final UnaryCallable<BatchDeactivateContentBundlesRequest,BatchDeactivateContentBundlesResponse> batchDeactivateContentBundlesCallable()

Deactivates a list of `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       BatchDeactivateContentBundlesRequest request =
           BatchDeactivateContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateContentBundlesResponse> future =
           contentBundleServiceClient.batchDeactivateContentBundlesCallable().futureCall(request);
       // Do something.
       BatchDeactivateContentBundlesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesRequest),[BatchDeactivateContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateContentBundlesResponse)>` |   
  
### close()
    
    
    public final void close()

### getContentBundle(@Nullable ContentBundleName name)
    
    
    public final ContentBundle getContentBundle(@Nullable ContentBundleName name)

Retrieves a `ContentBundle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       ContentBundleName name = ContentBundleName.of("[NETWORK_CODE]", "[CONTENT_BUNDLE]");
       ContentBundle response = contentBundleServiceClient.getContentBundle(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContentBundleName`  
Required. The resource name of the ContentBundle. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundle)` |   
  
### getContentBundle(GetContentBundleRequest request)
    
    
    public final ContentBundle getContentBundle(GetContentBundleRequest request)

Retrieves a `ContentBundle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       GetContentBundleRequest request =
           GetContentBundleRequest.newBuilder()
               .setName(ContentBundleName.of("[NETWORK_CODE]", "[CONTENT_BUNDLE]").toString())
               .build();
       ContentBundle response = contentBundleServiceClient.getContentBundle(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContentBundleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContentBundleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundle)` |   
  
### getContentBundle(String name)
    
    
    public final ContentBundle getContentBundle(String name)

Retrieves a `ContentBundle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       String name = ContentBundleName.of("[NETWORK_CODE]", "[CONTENT_BUNDLE]").toString();
       ContentBundle response = contentBundleServiceClient.getContentBundle(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ContentBundle. Format: `networks/{network_code}/contentBundles/{content_bundle_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundle)` |   
  
### getContentBundleCallable()
    
    
    public final UnaryCallable<GetContentBundleRequest,ContentBundle> getContentBundleCallable()

Retrieves a `ContentBundle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       GetContentBundleRequest request =
           GetContentBundleRequest.newBuilder()
               .setName(ContentBundleName.of("[NETWORK_CODE]", "[CONTENT_BUNDLE]").toString())
               .build();
       ApiFuture<ContentBundle> future =
           contentBundleServiceClient.getContentBundleCallable().futureCall(request);
       // Do something.
       ContentBundle response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContentBundleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContentBundleRequest),[ContentBundle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundle)>` |   
  
### getSettings()
    
    
    public final @Nullable ContentBundleServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContentBundleServiceSettings` |   
  
### getStub()
    
    
    public ContentBundleServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContentBundleServiceStub)` |   
  
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
  
### listContentBundles(@Nullable NetworkName parent)
    
    
    public final ContentBundleServiceClient.ListContentBundlesPagedResponse listContentBundles(@Nullable NetworkName parent)

Lists `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ContentBundle element :
           contentBundleServiceClient.listContentBundles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ContentBundles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient.ListContentBundlesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient.ListContentBundlesPagedResponse)` |   
  
### listContentBundles(ListContentBundlesRequest request)
    
    
    public final ContentBundleServiceClient.ListContentBundlesPagedResponse listContentBundles(ListContentBundlesRequest request)

Lists `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       ListContentBundlesRequest request =
           ListContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ContentBundle element :
           contentBundleServiceClient.listContentBundles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentBundlesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient.ListContentBundlesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient.ListContentBundlesPagedResponse)` |   
  
### listContentBundles(String parent)
    
    
    public final ContentBundleServiceClient.ListContentBundlesPagedResponse listContentBundles(String parent)

Lists `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ContentBundle element :
           contentBundleServiceClient.listContentBundles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ContentBundles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContentBundleServiceClient.ListContentBundlesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient.ListContentBundlesPagedResponse)` |   
  
### listContentBundlesCallable()
    
    
    public final UnaryCallable<ListContentBundlesRequest,ListContentBundlesResponse> listContentBundlesCallable()

Lists `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       ListContentBundlesRequest request =
           ListContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListContentBundlesResponse response =
             contentBundleServiceClient.listContentBundlesCallable().call(request);
         for (ContentBundle element : response.getContentBundlesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentBundlesRequest),[ListContentBundlesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentBundlesResponse)>` |   
  
### listContentBundlesPagedCallable()
    
    
    public final UnaryCallable<ListContentBundlesRequest,ContentBundleServiceClient.ListContentBundlesPagedResponse> listContentBundlesPagedCallable()

Lists `ContentBundle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContentBundleServiceClient contentBundleServiceClient =
         ContentBundleServiceClient.create()) {
       ListContentBundlesRequest request =
           ListContentBundlesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ContentBundle> future =
           contentBundleServiceClient.listContentBundlesPagedCallable().futureCall(request);
       // Do something.
       for (ContentBundle element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContentBundlesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContentBundlesRequest),[ListContentBundlesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContentBundleServiceClient.ListContentBundlesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
