---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient
title: Class CmsMetadataValueServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:34.688667+00:00
---

# Class CmsMetadataValueServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CmsMetadataValueServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CmsMetadataValueServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CmsMetadataValue` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       CmsMetadataValueName name = CmsMetadataValueName.of("[NETWORK_CODE]", "[CMS_METADATA_VALUE]");
       CmsMetadataValue response = cmsMetadataValueServiceClient.getCmsMetadataValue(name);
     }
     

Note: close() needs to be called on the CmsMetadataValueServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCmsMetadataValue |  Retrieves a `CmsMetadataValue` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCmsMetadataValue(GetCmsMetadataValueRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCmsMetadataValue(CmsMetadataValueName name) 
  * getCmsMetadataValue(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCmsMetadataValueCallable() 

  
ListCmsMetadataValues |  Lists `CmsMetadataValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCmsMetadataValues(ListCmsMetadataValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCmsMetadataValues(NetworkName parent) 
  * listCmsMetadataValues(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCmsMetadataValuesPagedCallable() 
  * listCmsMetadataValuesCallable() 

  
BatchActivateCmsMetadataValues |  Activates a list of `CmsMetadataValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCmsMetadataValues(BatchActivateCmsMetadataValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCmsMetadataValues(NetworkName parent, List<String> names) 
  * batchActivateCmsMetadataValues(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCmsMetadataValuesCallable() 

  
BatchDeactivateCmsMetadataValues |  Deactivates a list of `CmsMetadataValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCmsMetadataValues(BatchDeactivateCmsMetadataValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateCmsMetadataValues(NetworkName parent, List<String> names) 
  * batchDeactivateCmsMetadataValues(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCmsMetadataValuesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CmsMetadataValueServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmsMetadataValueServiceSettings cmsMetadataValueServiceSettings =
         CmsMetadataValueServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create(cmsMetadataValueServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmsMetadataValueServiceSettings cmsMetadataValueServiceSettings =
         CmsMetadataValueServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create(cmsMetadataValueServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CmsMetadataValueServiceClient

## Static Methods 

### create()
    
    
    public static final CmsMetadataValueServiceClient create()

Constructs an instance of CmsMetadataValueServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmsMetadataValueServiceSettings settings)
    
    
    public static final CmsMetadataValueServiceClient create(CmsMetadataValueServiceSettings settings)

Constructs an instance of CmsMetadataValueServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmsMetadataValueServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmsMetadataValueServiceStub stub)
    
    
    public static final CmsMetadataValueServiceClient create(CmsMetadataValueServiceStub stub)

Constructs an instance of CmsMetadataValueServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CmsMetadataValueServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmsMetadataValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataValueServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient)` |   
  
## Constructors 

### CmsMetadataValueServiceClient(CmsMetadataValueServiceSettings settings)
    
    
    protected CmsMetadataValueServiceClient(CmsMetadataValueServiceSettings settings)

Constructs an instance of CmsMetadataValueServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmsMetadataValueServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceSettings)`  
  
  
### CmsMetadataValueServiceClient(CmsMetadataValueServiceStub stub)
    
    
    protected CmsMetadataValueServiceClient(CmsMetadataValueServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmsMetadataValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataValueServiceStub)`  
  
  
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
  
### batchActivateCmsMetadataValues(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCmsMetadataValuesResponse batchActivateCmsMetadataValues(@Nullable NetworkName parent, List<String> names)

Activates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchActivateCmsMetadataValues(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CmsMetadataValues` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataValue`s to activate. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesResponse)` |   
  
### batchActivateCmsMetadataValues(BatchActivateCmsMetadataValuesRequest request)
    
    
    public final BatchActivateCmsMetadataValuesResponse batchActivateCmsMetadataValues(BatchActivateCmsMetadataValuesRequest request)

Activates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       BatchActivateCmsMetadataValuesRequest request =
           BatchActivateCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchActivateCmsMetadataValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesResponse)` |   
  
### batchActivateCmsMetadataValues(String parent, List<String> names)
    
    
    public final BatchActivateCmsMetadataValuesResponse batchActivateCmsMetadataValues(String parent, List<String> names)

Activates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchActivateCmsMetadataValues(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CmsMetadataValues` will be activated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataValue`s to activate. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesResponse)` |   
  
### batchActivateCmsMetadataValuesCallable()
    
    
    public final UnaryCallable<BatchActivateCmsMetadataValuesRequest,BatchActivateCmsMetadataValuesResponse> batchActivateCmsMetadataValuesCallable()

Activates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       BatchActivateCmsMetadataValuesRequest request =
           BatchActivateCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCmsMetadataValuesResponse> future =
           cmsMetadataValueServiceClient
               .batchActivateCmsMetadataValuesCallable()
               .futureCall(request);
       // Do something.
       BatchActivateCmsMetadataValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest),[BatchActivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCmsMetadataValuesResponse)>` |   
  
### batchDeactivateCmsMetadataValues(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateCmsMetadataValuesResponse batchDeactivateCmsMetadataValues(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchDeactivateCmsMetadataValues(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CmsMetadataValues` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataValue`s to deactivate. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesResponse)` |   
  
### batchDeactivateCmsMetadataValues(BatchDeactivateCmsMetadataValuesRequest request)
    
    
    public final BatchDeactivateCmsMetadataValuesResponse batchDeactivateCmsMetadataValues(BatchDeactivateCmsMetadataValuesRequest request)

Deactivates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       BatchDeactivateCmsMetadataValuesRequest request =
           BatchDeactivateCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchDeactivateCmsMetadataValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesResponse)` |   
  
### batchDeactivateCmsMetadataValues(String parent, List<String> names)
    
    
    public final BatchDeactivateCmsMetadataValuesResponse batchDeactivateCmsMetadataValues(String parent, List<String> names)

Deactivates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateCmsMetadataValuesResponse response =
           cmsMetadataValueServiceClient.batchDeactivateCmsMetadataValues(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CmsMetadataValues` will be deactivated. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CmsMetadataValue`s to deactivate. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesResponse)` |   
  
### batchDeactivateCmsMetadataValuesCallable()
    
    
    public final UnaryCallable<BatchDeactivateCmsMetadataValuesRequest,BatchDeactivateCmsMetadataValuesResponse> batchDeactivateCmsMetadataValuesCallable()

Deactivates a list of `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       BatchDeactivateCmsMetadataValuesRequest request =
           BatchDeactivateCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateCmsMetadataValuesResponse> future =
           cmsMetadataValueServiceClient
               .batchDeactivateCmsMetadataValuesCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateCmsMetadataValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesRequest),[BatchDeactivateCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCmsMetadataValuesResponse)>` |   
  
### close()
    
    
    public final void close()

### getCmsMetadataValue(@Nullable CmsMetadataValueName name)
    
    
    public final CmsMetadataValue getCmsMetadataValue(@Nullable CmsMetadataValueName name)

Retrieves a `CmsMetadataValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       CmsMetadataValueName name = CmsMetadataValueName.of("[NETWORK_CODE]", "[CMS_METADATA_VALUE]");
       CmsMetadataValue response = cmsMetadataValueServiceClient.getCmsMetadataValue(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CmsMetadataValueName`  
Required. The resource name of the CmsMetadataValue. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValue)` |   
  
### getCmsMetadataValue(GetCmsMetadataValueRequest request)
    
    
    public final CmsMetadataValue getCmsMetadataValue(GetCmsMetadataValueRequest request)

Retrieves a `CmsMetadataValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       GetCmsMetadataValueRequest request =
           GetCmsMetadataValueRequest.newBuilder()
               .setName(CmsMetadataValueName.of("[NETWORK_CODE]", "[CMS_METADATA_VALUE]").toString())
               .build();
       CmsMetadataValue response = cmsMetadataValueServiceClient.getCmsMetadataValue(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCmsMetadataValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCmsMetadataValueRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValue)` |   
  
### getCmsMetadataValue(String name)
    
    
    public final CmsMetadataValue getCmsMetadataValue(String name)

Retrieves a `CmsMetadataValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       String name = CmsMetadataValueName.of("[NETWORK_CODE]", "[CMS_METADATA_VALUE]").toString();
       CmsMetadataValue response = cmsMetadataValueServiceClient.getCmsMetadataValue(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CmsMetadataValue. Format: `networks/{network_code}/cmsMetadataValues/{cms_metadata_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValue)` |   
  
### getCmsMetadataValueCallable()
    
    
    public final UnaryCallable<GetCmsMetadataValueRequest,CmsMetadataValue> getCmsMetadataValueCallable()

Retrieves a `CmsMetadataValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       GetCmsMetadataValueRequest request =
           GetCmsMetadataValueRequest.newBuilder()
               .setName(CmsMetadataValueName.of("[NETWORK_CODE]", "[CMS_METADATA_VALUE]").toString())
               .build();
       ApiFuture<CmsMetadataValue> future =
           cmsMetadataValueServiceClient.getCmsMetadataValueCallable().futureCall(request);
       // Do something.
       CmsMetadataValue response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCmsMetadataValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCmsMetadataValueRequest),[CmsMetadataValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValue)>` |   
  
### getSettings()
    
    
    public final @Nullable CmsMetadataValueServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CmsMetadataValueServiceSettings` |   
  
### getStub()
    
    
    public CmsMetadataValueServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CmsMetadataValueServiceStub)` |   
  
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
  
### listCmsMetadataValues(@Nullable NetworkName parent)
    
    
    public final CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse listCmsMetadataValues(@Nullable NetworkName parent)

Lists `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CmsMetadataValue element :
           cmsMetadataValueServiceClient.listCmsMetadataValues(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CmsMetadataValues. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse)` |   
  
### listCmsMetadataValues(ListCmsMetadataValuesRequest request)
    
    
    public final CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse listCmsMetadataValues(ListCmsMetadataValuesRequest request)

Lists `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       ListCmsMetadataValuesRequest request =
           ListCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CmsMetadataValue element :
           cmsMetadataValueServiceClient.listCmsMetadataValues(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse)` |   
  
### listCmsMetadataValues(String parent)
    
    
    public final CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse listCmsMetadataValues(String parent)

Lists `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CmsMetadataValue element :
           cmsMetadataValueServiceClient.listCmsMetadataValues(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CmsMetadataValues. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse)` |   
  
### listCmsMetadataValuesCallable()
    
    
    public final UnaryCallable<ListCmsMetadataValuesRequest,ListCmsMetadataValuesResponse> listCmsMetadataValuesCallable()

Lists `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       ListCmsMetadataValuesRequest request =
           ListCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCmsMetadataValuesResponse response =
             cmsMetadataValueServiceClient.listCmsMetadataValuesCallable().call(request);
         for (CmsMetadataValue element : response.getCmsMetadataValuesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataValuesRequest),[ListCmsMetadataValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataValuesResponse)>` |   
  
### listCmsMetadataValuesPagedCallable()
    
    
    public final UnaryCallable<ListCmsMetadataValuesRequest,CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse> listCmsMetadataValuesPagedCallable()

Lists `CmsMetadataValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmsMetadataValueServiceClient cmsMetadataValueServiceClient =
         CmsMetadataValueServiceClient.create()) {
       ListCmsMetadataValuesRequest request =
           ListCmsMetadataValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CmsMetadataValue> future =
           cmsMetadataValueServiceClient.listCmsMetadataValuesPagedCallable().futureCall(request);
       // Do something.
       for (CmsMetadataValue element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCmsMetadataValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCmsMetadataValuesRequest),[ListCmsMetadataValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CmsMetadataValueServiceClient.ListCmsMetadataValuesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
