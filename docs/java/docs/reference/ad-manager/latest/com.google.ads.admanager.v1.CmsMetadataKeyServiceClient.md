---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient
title: Class CmsMetadataKeyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:32.585353+00:00
---

# Class CmsMetadataKeyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CmsMetadataKeyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CmsMetadataKeyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CmsMetadataKey` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       CmsMetadataKeyName name = CmsMetadataKeyName.of("[NETWORK_CODE]", "[CMS_METADATA_KEY]");
       CmsMetadataKey response = cmsMetadataKeyServiceClient.getCmsMetadataKey(name);
     }
     

Note: close() needs to be called on the CmsMetadataKeyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCmsMetadataKey |  Retrieves a `CmsMetadataKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCmsMetadataKey(GetCmsMetadataKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCmsMetadataKey(CmsMetadataKeyName name) 
  * getCmsMetadataKey(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCmsMetadataKeyCallable() 

  
ListCmsMetadataKeys |  Lists `CmsMetadataKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCmsMetadataKeys(ListCmsMetadataKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCmsMetadataKeys(NetworkName parent) 
  * listCmsMetadataKeys(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCmsMetadataKeysPagedCallable() 
  * listCmsMetadataKeysCallable() 

  
BatchActivateCmsMetadataKeys |  Activates a list of `CmsMetadataKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCmsMetadataKeys(BatchActivateCmsMetadataKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCmsMetadataKeys(NetworkName parent, List<String> names) 
  * batchActivateCmsMetadataKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCmsMetadataKeysCallable() 

  
BatchDeactivateCmsMetadataKeys |  Deactivates a list of `CmsMetadataKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCmsMetadataKeys(BatchDeactivateCmsMetadataKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateCmsMetadataKeys(NetworkName parent, List<String> names) 
  * batchDeactivateCmsMetadataKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCmsMetadataKeysCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CmsMetadataKeyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmsMetadataKeyServiceSettings cmsMetadataKeyServiceSettings =
         CmsMetadataKeyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create(cmsMetadataKeyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmsMetadataKeyServiceSettings cmsMetadataKeyServiceSettings =
         CmsMetadataKeyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create(cmsMetadataKeyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CmsMetadataKeyServiceClient

## Static Methods 

### create()
    
    
    public static final CmsMetadataKeyServiceClient create()

Constructs an instance of CmsMetadataKeyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmsMetadataKeyServiceSettings settings)
    
    
    public static final CmsMetadataKeyServiceClient create(CmsMetadataKeyServiceSettings settings)

Constructs an instance of CmsMetadataKeyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmsMetadataKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmsMetadataKeyServiceStub stub)
    
    
    public static final CmsMetadataKeyServiceClient create(CmsMetadataKeyServiceStub stub)

Constructs an instance of CmsMetadataKeyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CmsMetadataKeyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmsMetadataKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataKeyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient)` |   
  
## Constructors 

### CmsMetadataKeyServiceClient(CmsMetadataKeyServiceSettings settings)
    
    
    protected CmsMetadataKeyServiceClient(CmsMetadataKeyServiceSettings settings)

Constructs an instance of CmsMetadataKeyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmsMetadataKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceSettings)`  
  
  
### CmsMetadataKeyServiceClient(CmsMetadataKeyServiceStub stub)
    
    
    protected CmsMetadataKeyServiceClient(CmsMetadataKeyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmsMetadataKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataKeyServiceStub)`  
  
  
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
  
### batchActivateCmsMetadataKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCmsMetadataKeysResponse batchActivateCmsMetadataKeys(@Nullable NetworkName parent, List<String> names)

Activates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchActivateCmsMetadataKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CmsMetadataKeys` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataKey`s to activate. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysResponse)` |   
  
### batchActivateCmsMetadataKeys(BatchActivateCmsMetadataKeysRequest request)
    
    
    public final BatchActivateCmsMetadataKeysResponse batchActivateCmsMetadataKeys(BatchActivateCmsMetadataKeysRequest request)

Activates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       BatchActivateCmsMetadataKeysRequest request =
           BatchActivateCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchActivateCmsMetadataKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysResponse)` |   
  
### batchActivateCmsMetadataKeys(String parent, List<String> names)
    
    
    public final BatchActivateCmsMetadataKeysResponse batchActivateCmsMetadataKeys(String parent, List<String> names)

Activates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchActivateCmsMetadataKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CmsMetadataKeys` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataKey`s to activate. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysResponse)` |   
  
### batchActivateCmsMetadataKeysCallable()
    
    
    public final UnaryCallable<BatchActivateCmsMetadataKeysRequest,BatchActivateCmsMetadataKeysResponse> batchActivateCmsMetadataKeysCallable()

Activates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       BatchActivateCmsMetadataKeysRequest request =
           BatchActivateCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCmsMetadataKeysResponse> future =
           cmsMetadataKeyServiceClient.batchActivateCmsMetadataKeysCallable().futureCall(request);
       // Do something.
       BatchActivateCmsMetadataKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysRequest),[BatchActivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataKeysResponse)>` |   
  
### batchDeactivateCmsMetadataKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateCmsMetadataKeysResponse batchDeactivateCmsMetadataKeys(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchDeactivateCmsMetadataKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CmsMetadataKeys` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataKey`s to deactivate. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysResponse)` |   
  
### batchDeactivateCmsMetadataKeys(BatchDeactivateCmsMetadataKeysRequest request)
    
    
    public final BatchDeactivateCmsMetadataKeysResponse batchDeactivateCmsMetadataKeys(BatchDeactivateCmsMetadataKeysRequest request)

Deactivates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       BatchDeactivateCmsMetadataKeysRequest request =
           BatchDeactivateCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchDeactivateCmsMetadataKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysResponse)` |   
  
### batchDeactivateCmsMetadataKeys(String parent, List<String> names)
    
    
    public final BatchDeactivateCmsMetadataKeysResponse batchDeactivateCmsMetadataKeys(String parent, List<String> names)

Deactivates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateCmsMetadataKeysResponse response =
           cmsMetadataKeyServiceClient.batchDeactivateCmsMetadataKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CmsMetadataKeys` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataKey`s to deactivate. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysResponse)` |   
  
### batchDeactivateCmsMetadataKeysCallable()
    
    
    public final UnaryCallable<BatchDeactivateCmsMetadataKeysRequest,BatchDeactivateCmsMetadataKeysResponse> batchDeactivateCmsMetadataKeysCallable()

Deactivates a list of `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       BatchDeactivateCmsMetadataKeysRequest request =
           BatchDeactivateCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateCmsMetadataKeysResponse> future =
           cmsMetadataKeyServiceClient.batchDeactivateCmsMetadataKeysCallable().futureCall(request);
       // Do something.
       BatchDeactivateCmsMetadataKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysRequest),[BatchDeactivateCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataKeysResponse)>` |   
  
### close()
    
    
    public final void close()

### getCmsMetadataKey(@Nullable CmsMetadataKeyName name)
    
    
    public final CmsMetadataKey getCmsMetadataKey(@Nullable CmsMetadataKeyName name)

Retrieves a `CmsMetadataKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       CmsMetadataKeyName name = CmsMetadataKeyName.of("[NETWORK_CODE]", "[CMS_METADATA_KEY]");
       CmsMetadataKey response = cmsMetadataKeyServiceClient.getCmsMetadataKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CmsMetadataKeyName`  
Required. The resource name of the CmsMetadataKey. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKey)` |   
  
### getCmsMetadataKey(GetCmsMetadataKeyRequest request)
    
    
    public final CmsMetadataKey getCmsMetadataKey(GetCmsMetadataKeyRequest request)

Retrieves a `CmsMetadataKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       GetCmsMetadataKeyRequest request =
           GetCmsMetadataKeyRequest.newBuilder()
               .setName(CmsMetadataKeyName.of("[NETWORK_CODE]", "[CMS_METADATA_KEY]").toString())
               .build();
       CmsMetadataKey response = cmsMetadataKeyServiceClient.getCmsMetadataKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCmsMetadataKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCmsMetadataKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKey)` |   
  
### getCmsMetadataKey(String name)
    
    
    public final CmsMetadataKey getCmsMetadataKey(String name)

Retrieves a `CmsMetadataKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       String name = CmsMetadataKeyName.of("[NETWORK_CODE]", "[CMS_METADATA_KEY]").toString();
       CmsMetadataKey response = cmsMetadataKeyServiceClient.getCmsMetadataKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CmsMetadataKey. Format: `networks/{network_code}/cmsMetadataKeys/{cms_metadata_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKey)` |   
  
### getCmsMetadataKeyCallable()
    
    
    public final UnaryCallable<GetCmsMetadataKeyRequest,CmsMetadataKey> getCmsMetadataKeyCallable()

Retrieves a `CmsMetadataKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       GetCmsMetadataKeyRequest request =
           GetCmsMetadataKeyRequest.newBuilder()
               .setName(CmsMetadataKeyName.of("[NETWORK_CODE]", "[CMS_METADATA_KEY]").toString())
               .build();
       ApiFuture<CmsMetadataKey> future =
           cmsMetadataKeyServiceClient.getCmsMetadataKeyCallable().futureCall(request);
       // Do something.
       CmsMetadataKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCmsMetadataKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCmsMetadataKeyRequest),[CmsMetadataKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKey)>` |   
  
### getSettings()
    
    
    public final @Nullable CmsMetadataKeyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CmsMetadataKeyServiceSettings` |   
  
### getStub()
    
    
    public CmsMetadataKeyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataKeyServiceStub)` |   
  
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
  
### listCmsMetadataKeys(@Nullable NetworkName parent)
    
    
    public final CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse listCmsMetadataKeys(@Nullable NetworkName parent)

Lists `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CmsMetadataKey element :
           cmsMetadataKeyServiceClient.listCmsMetadataKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CmsMetadataKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse)` |   
  
### listCmsMetadataKeys(ListCmsMetadataKeysRequest request)
    
    
    public final CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse listCmsMetadataKeys(ListCmsMetadataKeysRequest request)

Lists `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       ListCmsMetadataKeysRequest request =
           ListCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CmsMetadataKey element :
           cmsMetadataKeyServiceClient.listCmsMetadataKeys(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse)` |   
  
### listCmsMetadataKeys(String parent)
    
    
    public final CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse listCmsMetadataKeys(String parent)

Lists `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CmsMetadataKey element :
           cmsMetadataKeyServiceClient.listCmsMetadataKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CmsMetadataKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse)` |   
  
### listCmsMetadataKeysCallable()
    
    
    public final UnaryCallable<ListCmsMetadataKeysRequest,ListCmsMetadataKeysResponse> listCmsMetadataKeysCallable()

Lists `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       ListCmsMetadataKeysRequest request =
           ListCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCmsMetadataKeysResponse response =
             cmsMetadataKeyServiceClient.listCmsMetadataKeysCallable().call(request);
         for (CmsMetadataKey element : response.getCmsMetadataKeysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataKeysRequest),[ListCmsMetadataKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataKeysResponse)>` |   
  
### listCmsMetadataKeysPagedCallable()
    
    
    public final UnaryCallable<ListCmsMetadataKeysRequest,CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse> listCmsMetadataKeysPagedCallable()

Lists `CmsMetadataKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataKeyServiceClient cmsMetadataKeyServiceClient =
         CmsMetadataKeyServiceClient.create()) {
       ListCmsMetadataKeysRequest request =
           ListCmsMetadataKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CmsMetadataKey> future =
           cmsMetadataKeyServiceClient.listCmsMetadataKeysPagedCallable().futureCall(request);
       // Do something.
       for (CmsMetadataKey element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCmsMetadataKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataKeysRequest),[ListCmsMetadataKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataKeyServiceClient.ListCmsMetadataKeysPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
