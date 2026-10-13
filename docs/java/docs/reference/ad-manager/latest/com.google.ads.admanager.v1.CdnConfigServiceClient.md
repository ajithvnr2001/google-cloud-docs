---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient
title: Class CdnConfigServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:30.226934+00:00
---

# Class CdnConfigServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CdnConfigServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CdnConfigServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CdnConfig` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       CdnConfigName name = CdnConfigName.of("[NETWORK_CODE]", "[CDN_CONFIG]");
       CdnConfig response = cdnConfigServiceClient.getCdnConfig(name);
     }
     

Note: close() needs to be called on the CdnConfigServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCdnConfig |  Retrieves a `CdnConfig` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCdnConfig(GetCdnConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCdnConfig(CdnConfigName name) 
  * getCdnConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCdnConfigCallable() 

  
ListCdnConfigs |  Lists `CdnConfig` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCdnConfigs(ListCdnConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCdnConfigs(NetworkName parent) 
  * listCdnConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCdnConfigsPagedCallable() 
  * listCdnConfigsCallable() 

  
CreateCdnConfig |  Creates a `CdnConfig` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCdnConfig(CreateCdnConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCdnConfig(NetworkName parent, CdnConfig cdnConfig) 
  * createCdnConfig(String parent, CdnConfig cdnConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCdnConfigCallable() 

  
BatchCreateCdnConfigs |  Batch creates `CdnConfig` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCdnConfigs(NetworkName parent, List<CreateCdnConfigRequest> requests) 
  * batchCreateCdnConfigs(String parent, List<CreateCdnConfigRequest> requests) 
  * batchCreateCdnConfigs(BatchCreateCdnConfigsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCdnConfigsCallable() 

  
UpdateCdnConfig |  Updates a `CdnConfig` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCdnConfig(UpdateCdnConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCdnConfig(CdnConfig cdnConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCdnConfigCallable() 

  
BatchUpdateCdnConfigs |  Batch updates `CdnConfig` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCdnConfigs(NetworkName parent, List<UpdateCdnConfigRequest> requests) 
  * batchUpdateCdnConfigs(String parent, List<UpdateCdnConfigRequest> requests) 
  * batchUpdateCdnConfigs(BatchUpdateCdnConfigsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCdnConfigsCallable() 

  
BatchActivateCdnConfigs |  Batch activates `CdnConfig` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCdnConfigs(BatchActivateCdnConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCdnConfigs(NetworkName parent, List<String> names) 
  * batchActivateCdnConfigs(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCdnConfigsCallable() 

  
BatchArchiveCdnConfigs |  Batch archives `CdnConfig` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveCdnConfigs(BatchArchiveCdnConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveCdnConfigs(NetworkName parent, List<String> names) 
  * batchArchiveCdnConfigs(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveCdnConfigsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CdnConfigServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CdnConfigServiceSettings cdnConfigServiceSettings =
         CdnConfigServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CdnConfigServiceClient cdnConfigServiceClient =
         CdnConfigServiceClient.create(cdnConfigServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CdnConfigServiceSettings cdnConfigServiceSettings =
         CdnConfigServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CdnConfigServiceClient cdnConfigServiceClient =
         CdnConfigServiceClient.create(cdnConfigServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CdnConfigServiceClient

## Static Methods 

### create()
    
    
    public static final CdnConfigServiceClient create()

Constructs an instance of CdnConfigServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CdnConfigServiceSettings settings)
    
    
    public static final CdnConfigServiceClient create(CdnConfigServiceSettings settings)

Constructs an instance of CdnConfigServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CdnConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CdnConfigServiceStub stub)
    
    
    public static final CdnConfigServiceClient create(CdnConfigServiceStub stub)

Constructs an instance of CdnConfigServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CdnConfigServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CdnConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CdnConfigServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient)` |   
  
## Constructors 

### CdnConfigServiceClient(CdnConfigServiceSettings settings)
    
    
    protected CdnConfigServiceClient(CdnConfigServiceSettings settings)

Constructs an instance of CdnConfigServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CdnConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceSettings)`  
  
  
### CdnConfigServiceClient(CdnConfigServiceStub stub)
    
    
    protected CdnConfigServiceClient(CdnConfigServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CdnConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CdnConfigServiceStub)`  
  
  
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
  
### batchActivateCdnConfigs(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCdnConfigsResponse batchActivateCdnConfigs(@Nullable NetworkName parent, List<String> names)

Batch activates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCdnConfigsResponse response =
           cdnConfigServiceClient.batchActivateCdnConfigs(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CdnConfig` objects to activate. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsResponse)` |   
  
### batchActivateCdnConfigs(BatchActivateCdnConfigsRequest request)
    
    
    public final BatchActivateCdnConfigsResponse batchActivateCdnConfigs(BatchActivateCdnConfigsRequest request)

Batch activates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchActivateCdnConfigsRequest request =
           BatchActivateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCdnConfigsResponse response =
           cdnConfigServiceClient.batchActivateCdnConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsResponse)` |   
  
### batchActivateCdnConfigs(String parent, List<String> names)
    
    
    public final BatchActivateCdnConfigsResponse batchActivateCdnConfigs(String parent, List<String> names)

Batch activates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCdnConfigsResponse response =
           cdnConfigServiceClient.batchActivateCdnConfigs(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CdnConfig` objects to activate. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsResponse)` |   
  
### batchActivateCdnConfigsCallable()
    
    
    public final UnaryCallable<BatchActivateCdnConfigsRequest,BatchActivateCdnConfigsResponse> batchActivateCdnConfigsCallable()

Batch activates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchActivateCdnConfigsRequest request =
           BatchActivateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCdnConfigsResponse> future =
           cdnConfigServiceClient.batchActivateCdnConfigsCallable().futureCall(request);
       // Do something.
       BatchActivateCdnConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsRequest),[BatchActivateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCdnConfigsResponse)>` |   
  
### batchArchiveCdnConfigs(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveCdnConfigsResponse batchArchiveCdnConfigs(@Nullable NetworkName parent, List<String> names)

Batch archives `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveCdnConfigsResponse response =
           cdnConfigServiceClient.batchArchiveCdnConfigs(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CdnConfig` objects to archive. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsResponse)` |   
  
### batchArchiveCdnConfigs(BatchArchiveCdnConfigsRequest request)
    
    
    public final BatchArchiveCdnConfigsResponse batchArchiveCdnConfigs(BatchArchiveCdnConfigsRequest request)

Batch archives `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchArchiveCdnConfigsRequest request =
           BatchArchiveCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveCdnConfigsResponse response =
           cdnConfigServiceClient.batchArchiveCdnConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsResponse)` |   
  
### batchArchiveCdnConfigs(String parent, List<String> names)
    
    
    public final BatchArchiveCdnConfigsResponse batchArchiveCdnConfigs(String parent, List<String> names)

Batch archives `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveCdnConfigsResponse response =
           cdnConfigServiceClient.batchArchiveCdnConfigs(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CdnConfig` objects to archive. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsResponse)` |   
  
### batchArchiveCdnConfigsCallable()
    
    
    public final UnaryCallable<BatchArchiveCdnConfigsRequest,BatchArchiveCdnConfigsResponse> batchArchiveCdnConfigsCallable()

Batch archives `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchArchiveCdnConfigsRequest request =
           BatchArchiveCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveCdnConfigsResponse> future =
           cdnConfigServiceClient.batchArchiveCdnConfigsCallable().futureCall(request);
       // Do something.
       BatchArchiveCdnConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsRequest),[BatchArchiveCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveCdnConfigsResponse)>` |   
  
### batchCreateCdnConfigs(@Nullable NetworkName parent, List<CreateCdnConfigRequest> requests)
    
    
    public final BatchCreateCdnConfigsResponse batchCreateCdnConfigs(@Nullable NetworkName parent, List<CreateCdnConfigRequest> requests)

Batch creates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCdnConfigRequest> requests = new ArrayList<>();
       BatchCreateCdnConfigsResponse response =
           cdnConfigServiceClient.batchCreateCdnConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CdnConfigs` will be created. Format: `networks/{network_code}` The parent field in the CreateCdnConfigRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCdnConfigRequest)>`  
Required. The `CdnConfig` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsResponse)` |   
  
### batchCreateCdnConfigs(BatchCreateCdnConfigsRequest request)
    
    
    public final BatchCreateCdnConfigsResponse batchCreateCdnConfigs(BatchCreateCdnConfigsRequest request)

Batch creates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchCreateCdnConfigsRequest request =
           BatchCreateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCdnConfigRequest>())
               .build();
       BatchCreateCdnConfigsResponse response =
           cdnConfigServiceClient.batchCreateCdnConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsResponse)` |   
  
### batchCreateCdnConfigs(String parent, List<CreateCdnConfigRequest> requests)
    
    
    public final BatchCreateCdnConfigsResponse batchCreateCdnConfigs(String parent, List<CreateCdnConfigRequest> requests)

Batch creates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCdnConfigRequest> requests = new ArrayList<>();
       BatchCreateCdnConfigsResponse response =
           cdnConfigServiceClient.batchCreateCdnConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CdnConfigs` will be created. Format: `networks/{network_code}` The parent field in the CreateCdnConfigRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCdnConfigRequest)>`  
Required. The `CdnConfig` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsResponse)` |   
  
### batchCreateCdnConfigsCallable()
    
    
    public final UnaryCallable<BatchCreateCdnConfigsRequest,BatchCreateCdnConfigsResponse> batchCreateCdnConfigsCallable()

Batch creates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchCreateCdnConfigsRequest request =
           BatchCreateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCdnConfigRequest>())
               .build();
       ApiFuture<BatchCreateCdnConfigsResponse> future =
           cdnConfigServiceClient.batchCreateCdnConfigsCallable().futureCall(request);
       // Do something.
       BatchCreateCdnConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsRequest),[BatchCreateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCdnConfigsResponse)>` |   
  
### batchUpdateCdnConfigs(@Nullable NetworkName parent, List<UpdateCdnConfigRequest> requests)
    
    
    public final BatchUpdateCdnConfigsResponse batchUpdateCdnConfigs(@Nullable NetworkName parent, List<UpdateCdnConfigRequest> requests)

Batch updates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCdnConfigRequest> requests = new ArrayList<>();
       BatchUpdateCdnConfigsResponse response =
           cdnConfigServiceClient.batchUpdateCdnConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CdnConfigs` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCdnConfigRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCdnConfigRequest)>`  
Required. The `CdnConfig` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsResponse)` |   
  
### batchUpdateCdnConfigs(BatchUpdateCdnConfigsRequest request)
    
    
    public final BatchUpdateCdnConfigsResponse batchUpdateCdnConfigs(BatchUpdateCdnConfigsRequest request)

Batch updates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchUpdateCdnConfigsRequest request =
           BatchUpdateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCdnConfigRequest>())
               .build();
       BatchUpdateCdnConfigsResponse response =
           cdnConfigServiceClient.batchUpdateCdnConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsResponse)` |   
  
### batchUpdateCdnConfigs(String parent, List<UpdateCdnConfigRequest> requests)
    
    
    public final BatchUpdateCdnConfigsResponse batchUpdateCdnConfigs(String parent, List<UpdateCdnConfigRequest> requests)

Batch updates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCdnConfigRequest> requests = new ArrayList<>();
       BatchUpdateCdnConfigsResponse response =
           cdnConfigServiceClient.batchUpdateCdnConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CdnConfigs` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCdnConfigRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCdnConfigRequest)>`  
Required. The `CdnConfig` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsResponse)` |   
  
### batchUpdateCdnConfigsCallable()
    
    
    public final UnaryCallable<BatchUpdateCdnConfigsRequest,BatchUpdateCdnConfigsResponse> batchUpdateCdnConfigsCallable()

Batch updates `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       BatchUpdateCdnConfigsRequest request =
           BatchUpdateCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCdnConfigRequest>())
               .build();
       ApiFuture<BatchUpdateCdnConfigsResponse> future =
           cdnConfigServiceClient.batchUpdateCdnConfigsCallable().futureCall(request);
       // Do something.
       BatchUpdateCdnConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsRequest),[BatchUpdateCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCdnConfigsResponse)>` |   
  
### close()
    
    
    public final void close()

### createCdnConfig(@Nullable NetworkName parent, CdnConfig cdnConfig)
    
    
    public final CdnConfig createCdnConfig(@Nullable NetworkName parent, CdnConfig cdnConfig)

Creates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CdnConfig cdnConfig = CdnConfig.newBuilder().build();
       CdnConfig response = cdnConfigServiceClient.createCdnConfig(parent, cdnConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `CdnConfig` will be created. Format: `networks/{network_code}`  
`cdnConfig` | `[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)`  
Required. The `CdnConfig` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### createCdnConfig(CreateCdnConfigRequest request)
    
    
    public final CdnConfig createCdnConfig(CreateCdnConfigRequest request)

Creates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       CreateCdnConfigRequest request =
           CreateCdnConfigRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCdnConfig(CdnConfig.newBuilder().build())
               .build();
       CdnConfig response = cdnConfigServiceClient.createCdnConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCdnConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### createCdnConfig(String parent, CdnConfig cdnConfig)
    
    
    public final CdnConfig createCdnConfig(String parent, CdnConfig cdnConfig)

Creates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CdnConfig cdnConfig = CdnConfig.newBuilder().build();
       CdnConfig response = cdnConfigServiceClient.createCdnConfig(parent, cdnConfig);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `CdnConfig` will be created. Format: `networks/{network_code}`  
`cdnConfig` | `[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)`  
Required. The `CdnConfig` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### createCdnConfigCallable()
    
    
    public final UnaryCallable<CreateCdnConfigRequest,CdnConfig> createCdnConfigCallable()

Creates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       CreateCdnConfigRequest request =
           CreateCdnConfigRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCdnConfig(CdnConfig.newBuilder().build())
               .build();
       ApiFuture<CdnConfig> future =
           cdnConfigServiceClient.createCdnConfigCallable().futureCall(request);
       // Do something.
       CdnConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCdnConfigRequest),[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)>` |   
  
### getCdnConfig(@Nullable CdnConfigName name)
    
    
    public final CdnConfig getCdnConfig(@Nullable CdnConfigName name)

Retrieves a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       CdnConfigName name = CdnConfigName.of("[NETWORK_CODE]", "[CDN_CONFIG]");
       CdnConfig response = cdnConfigServiceClient.getCdnConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CdnConfigName`  
Required. The resource name of the CdnConfig. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### getCdnConfig(GetCdnConfigRequest request)
    
    
    public final CdnConfig getCdnConfig(GetCdnConfigRequest request)

Retrieves a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       GetCdnConfigRequest request =
           GetCdnConfigRequest.newBuilder()
               .setName(CdnConfigName.of("[NETWORK_CODE]", "[CDN_CONFIG]").toString())
               .build();
       CdnConfig response = cdnConfigServiceClient.getCdnConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCdnConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### getCdnConfig(String name)
    
    
    public final CdnConfig getCdnConfig(String name)

Retrieves a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String name = CdnConfigName.of("[NETWORK_CODE]", "[CDN_CONFIG]").toString();
       CdnConfig response = cdnConfigServiceClient.getCdnConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CdnConfig. Format: `networks/{network_code}/cdnConfigs/{cdn_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### getCdnConfigCallable()
    
    
    public final UnaryCallable<GetCdnConfigRequest,CdnConfig> getCdnConfigCallable()

Retrieves a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       GetCdnConfigRequest request =
           GetCdnConfigRequest.newBuilder()
               .setName(CdnConfigName.of("[NETWORK_CODE]", "[CDN_CONFIG]").toString())
               .build();
       ApiFuture<CdnConfig> future =
           cdnConfigServiceClient.getCdnConfigCallable().futureCall(request);
       // Do something.
       CdnConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCdnConfigRequest),[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable CdnConfigServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CdnConfigServiceSettings` |   
  
### getStub()
    
    
    public CdnConfigServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CdnConfigServiceStub)` |   
  
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
  
### listCdnConfigs(@Nullable NetworkName parent)
    
    
    public final CdnConfigServiceClient.ListCdnConfigsPagedResponse listCdnConfigs(@Nullable NetworkName parent)

Lists `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CdnConfig element : cdnConfigServiceClient.listCdnConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CdnConfigs. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient.ListCdnConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient.ListCdnConfigsPagedResponse)` |   
  
### listCdnConfigs(ListCdnConfigsRequest request)
    
    
    public final CdnConfigServiceClient.ListCdnConfigsPagedResponse listCdnConfigs(ListCdnConfigsRequest request)

Lists `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       ListCdnConfigsRequest request =
           ListCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CdnConfig element : cdnConfigServiceClient.listCdnConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCdnConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient.ListCdnConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient.ListCdnConfigsPagedResponse)` |   
  
### listCdnConfigs(String parent)
    
    
    public final CdnConfigServiceClient.ListCdnConfigsPagedResponse listCdnConfigs(String parent)

Lists `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CdnConfig element : cdnConfigServiceClient.listCdnConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CdnConfigs. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfigServiceClient.ListCdnConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient.ListCdnConfigsPagedResponse)` |   
  
### listCdnConfigsCallable()
    
    
    public final UnaryCallable<ListCdnConfigsRequest,ListCdnConfigsResponse> listCdnConfigsCallable()

Lists `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       ListCdnConfigsRequest request =
           ListCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCdnConfigsResponse response =
             cdnConfigServiceClient.listCdnConfigsCallable().call(request);
         for (CdnConfig element : response.getCdnConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCdnConfigsRequest),[ListCdnConfigsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCdnConfigsResponse)>` |   
  
### listCdnConfigsPagedCallable()
    
    
    public final UnaryCallable<ListCdnConfigsRequest,CdnConfigServiceClient.ListCdnConfigsPagedResponse> listCdnConfigsPagedCallable()

Lists `CdnConfig` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       ListCdnConfigsRequest request =
           ListCdnConfigsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CdnConfig> future =
           cdnConfigServiceClient.listCdnConfigsPagedCallable().futureCall(request);
       // Do something.
       for (CdnConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnConfigsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCdnConfigsRequest),[ListCdnConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfigServiceClient.ListCdnConfigsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCdnConfig(CdnConfig cdnConfig, FieldMask updateMask)
    
    
    public final CdnConfig updateCdnConfig(CdnConfig cdnConfig, FieldMask updateMask)

Updates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       CdnConfig cdnConfig = CdnConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CdnConfig response = cdnConfigServiceClient.updateCdnConfig(cdnConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cdnConfig` | `[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)`  
Required. The `CdnConfig` to update. The `CdnConfig`'s `name` is used to identify the `CdnConfig` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### updateCdnConfig(UpdateCdnConfigRequest request)
    
    
    public final CdnConfig updateCdnConfig(UpdateCdnConfigRequest request)

Updates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       UpdateCdnConfigRequest request =
           UpdateCdnConfigRequest.newBuilder()
               .setCdnConfig(CdnConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CdnConfig response = cdnConfigServiceClient.updateCdnConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCdnConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)` |   
  
### updateCdnConfigCallable()
    
    
    public final UnaryCallable<UpdateCdnConfigRequest,CdnConfig> updateCdnConfigCallable()

Updates a `CdnConfig` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CdnConfigServiceClient cdnConfigServiceClient = CdnConfigServiceClient.create()) {
       UpdateCdnConfigRequest request =
           UpdateCdnConfigRequest.newBuilder()
               .setCdnConfig(CdnConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CdnConfig> future =
           cdnConfigServiceClient.updateCdnConfigCallable().futureCall(request);
       // Do something.
       CdnConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCdnConfigRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCdnConfigRequest),[CdnConfig](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CdnConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
