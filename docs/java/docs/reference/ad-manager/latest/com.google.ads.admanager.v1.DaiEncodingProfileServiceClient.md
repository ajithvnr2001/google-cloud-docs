---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient
title: Class DaiEncodingProfileServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:43.359328+00:00
---

# Class DaiEncodingProfileServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DaiEncodingProfileServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/DaiEncodingProfileServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `DaiEncodingProfile` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       DaiEncodingProfileName name =
           DaiEncodingProfileName.of("[NETWORK_CODE]", "[DAI_ENCODING_PROFILE]");
       DaiEncodingProfile response = daiEncodingProfileServiceClient.getDaiEncodingProfile(name);
     }
     

Note: close() needs to be called on the DaiEncodingProfileServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDaiEncodingProfile |  Retrieves a `DaiEncodingProfile` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDaiEncodingProfile(GetDaiEncodingProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDaiEncodingProfile(DaiEncodingProfileName name) 
  * getDaiEncodingProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDaiEncodingProfileCallable() 

  
ListDaiEncodingProfiles |  Lists `DaiEncodingProfile` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDaiEncodingProfiles(ListDaiEncodingProfilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDaiEncodingProfiles(NetworkName parent) 
  * listDaiEncodingProfiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDaiEncodingProfilesPagedCallable() 
  * listDaiEncodingProfilesCallable() 

  
CreateDaiEncodingProfile |  Creates a `DaiEncodingProfile` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDaiEncodingProfile(CreateDaiEncodingProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDaiEncodingProfile(NetworkName parent, DaiEncodingProfile daiEncodingProfile) 
  * createDaiEncodingProfile(String parent, DaiEncodingProfile daiEncodingProfile) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDaiEncodingProfileCallable() 

  
BatchCreateDaiEncodingProfiles |  Batch creates `DaiEncodingProfile` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateDaiEncodingProfiles(NetworkName parent, List<CreateDaiEncodingProfileRequest> requests) 
  * batchCreateDaiEncodingProfiles(String parent, List<CreateDaiEncodingProfileRequest> requests) 
  * batchCreateDaiEncodingProfiles(BatchCreateDaiEncodingProfilesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateDaiEncodingProfilesCallable() 

  
UpdateDaiEncodingProfile |  Updates a `DaiEncodingProfile` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDaiEncodingProfile(UpdateDaiEncodingProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDaiEncodingProfile(DaiEncodingProfile daiEncodingProfile, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDaiEncodingProfileCallable() 

  
BatchUpdateDaiEncodingProfiles |  Batch updates `DaiEncodingProfile` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateDaiEncodingProfiles(NetworkName parent, List<UpdateDaiEncodingProfileRequest> requests) 
  * batchUpdateDaiEncodingProfiles(String parent, List<UpdateDaiEncodingProfileRequest> requests) 
  * batchUpdateDaiEncodingProfiles(BatchUpdateDaiEncodingProfilesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateDaiEncodingProfilesCallable() 

  
BatchActivateDaiEncodingProfiles |  Activates a list of `DaiEncodingProfile` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateDaiEncodingProfiles(NetworkName parent, List<ActivateDaiEncodingProfileRequest> requests) 
  * batchActivateDaiEncodingProfiles(String parent, List<ActivateDaiEncodingProfileRequest> requests) 
  * batchActivateDaiEncodingProfiles(BatchActivateDaiEncodingProfilesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateDaiEncodingProfilesCallable() 

  
BatchArchiveDaiEncodingProfiles |  Archives a list of `DaiEncodingProfile` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveDaiEncodingProfiles(NetworkName parent, List<ArchiveDaiEncodingProfileRequest> requests) 
  * batchArchiveDaiEncodingProfiles(String parent, List<ArchiveDaiEncodingProfileRequest> requests) 
  * batchArchiveDaiEncodingProfiles(BatchArchiveDaiEncodingProfilesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveDaiEncodingProfilesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DaiEncodingProfileServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiEncodingProfileServiceSettings daiEncodingProfileServiceSettings =
         DaiEncodingProfileServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create(daiEncodingProfileServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiEncodingProfileServiceSettings daiEncodingProfileServiceSettings =
         DaiEncodingProfileServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create(daiEncodingProfileServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DaiEncodingProfileServiceClient

## Static Methods 

### create()
    
    
    public static final DaiEncodingProfileServiceClient create()

Constructs an instance of DaiEncodingProfileServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiEncodingProfileServiceSettings settings)
    
    
    public static final DaiEncodingProfileServiceClient create(DaiEncodingProfileServiceSettings settings)

Constructs an instance of DaiEncodingProfileServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiEncodingProfileServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiEncodingProfileServiceStub stub)
    
    
    public static final DaiEncodingProfileServiceClient create(DaiEncodingProfileServiceStub stub)

Constructs an instance of DaiEncodingProfileServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DaiEncodingProfileServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiEncodingProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiEncodingProfileServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient)` |   
  
## Constructors 

### DaiEncodingProfileServiceClient(DaiEncodingProfileServiceSettings settings)
    
    
    protected DaiEncodingProfileServiceClient(DaiEncodingProfileServiceSettings settings)

Constructs an instance of DaiEncodingProfileServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiEncodingProfileServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceSettings)`  
  
  
### DaiEncodingProfileServiceClient(DaiEncodingProfileServiceStub stub)
    
    
    protected DaiEncodingProfileServiceClient(DaiEncodingProfileServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiEncodingProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiEncodingProfileServiceStub)`  
  
  
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
  
### batchActivateDaiEncodingProfiles(@Nullable NetworkName parent, List<ActivateDaiEncodingProfileRequest> requests)
    
    
    public final BatchActivateDaiEncodingProfilesResponse batchActivateDaiEncodingProfiles(@Nullable NetworkName parent, List<ActivateDaiEncodingProfileRequest> requests)

Activates a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<ActivateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchActivateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchActivateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ActivateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ActivateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to activate. A maximum of 100 objects can be activated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesResponse)` |   
  
### batchActivateDaiEncodingProfiles(BatchActivateDaiEncodingProfilesRequest request)
    
    
    public final BatchActivateDaiEncodingProfilesResponse batchActivateDaiEncodingProfiles(BatchActivateDaiEncodingProfilesRequest request)

Activates a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchActivateDaiEncodingProfilesRequest request =
           BatchActivateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ActivateDaiEncodingProfileRequest>())
               .build();
       BatchActivateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchActivateDaiEncodingProfiles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesResponse)` |   
  
### batchActivateDaiEncodingProfiles(String parent, List<ActivateDaiEncodingProfileRequest> requests)
    
    
    public final BatchActivateDaiEncodingProfilesResponse batchActivateDaiEncodingProfiles(String parent, List<ActivateDaiEncodingProfileRequest> requests)

Activates a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<ActivateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchActivateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchActivateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ActivateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ActivateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to activate. A maximum of 100 objects can be activated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesResponse)` |   
  
### batchActivateDaiEncodingProfilesCallable()
    
    
    public final UnaryCallable<BatchActivateDaiEncodingProfilesRequest,BatchActivateDaiEncodingProfilesResponse> batchActivateDaiEncodingProfilesCallable()

Activates a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchActivateDaiEncodingProfilesRequest request =
           BatchActivateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ActivateDaiEncodingProfileRequest>())
               .build();
       ApiFuture<BatchActivateDaiEncodingProfilesResponse> future =
           daiEncodingProfileServiceClient
               .batchActivateDaiEncodingProfilesCallable()
               .futureCall(request);
       // Do something.
       BatchActivateDaiEncodingProfilesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesRequest),[BatchActivateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiEncodingProfilesResponse)>` |   
  
### batchArchiveDaiEncodingProfiles(@Nullable NetworkName parent, List<ArchiveDaiEncodingProfileRequest> requests)
    
    
    public final BatchArchiveDaiEncodingProfilesResponse batchArchiveDaiEncodingProfiles(@Nullable NetworkName parent, List<ArchiveDaiEncodingProfileRequest> requests)

Archives a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<ArchiveDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchArchiveDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchArchiveDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ArchiveDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ArchiveDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to archive. A maximum of 100 objects can be archived in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesResponse)` |   
  
### batchArchiveDaiEncodingProfiles(BatchArchiveDaiEncodingProfilesRequest request)
    
    
    public final BatchArchiveDaiEncodingProfilesResponse batchArchiveDaiEncodingProfiles(BatchArchiveDaiEncodingProfilesRequest request)

Archives a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchArchiveDaiEncodingProfilesRequest request =
           BatchArchiveDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ArchiveDaiEncodingProfileRequest>())
               .build();
       BatchArchiveDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchArchiveDaiEncodingProfiles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesResponse)` |   
  
### batchArchiveDaiEncodingProfiles(String parent, List<ArchiveDaiEncodingProfileRequest> requests)
    
    
    public final BatchArchiveDaiEncodingProfilesResponse batchArchiveDaiEncodingProfiles(String parent, List<ArchiveDaiEncodingProfileRequest> requests)

Archives a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<ArchiveDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchArchiveDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchArchiveDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ArchiveDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ArchiveDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to archive. A maximum of 100 objects can be archived in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesResponse)` |   
  
### batchArchiveDaiEncodingProfilesCallable()
    
    
    public final UnaryCallable<BatchArchiveDaiEncodingProfilesRequest,BatchArchiveDaiEncodingProfilesResponse> batchArchiveDaiEncodingProfilesCallable()

Archives a list of `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchArchiveDaiEncodingProfilesRequest request =
           BatchArchiveDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ArchiveDaiEncodingProfileRequest>())
               .build();
       ApiFuture<BatchArchiveDaiEncodingProfilesResponse> future =
           daiEncodingProfileServiceClient
               .batchArchiveDaiEncodingProfilesCallable()
               .futureCall(request);
       // Do something.
       BatchArchiveDaiEncodingProfilesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesRequest),[BatchArchiveDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveDaiEncodingProfilesResponse)>` |   
  
### batchCreateDaiEncodingProfiles(@Nullable NetworkName parent, List<CreateDaiEncodingProfileRequest> requests)
    
    
    public final BatchCreateDaiEncodingProfilesResponse batchCreateDaiEncodingProfiles(@Nullable NetworkName parent, List<CreateDaiEncodingProfileRequest> requests)

Batch creates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchCreateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchCreateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `DaiEncodingProfiles` will be created. Format: `networks/{network_code}` The parent field in the CreateDaiEncodingProfileRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesResponse)` |   
  
### batchCreateDaiEncodingProfiles(BatchCreateDaiEncodingProfilesRequest request)
    
    
    public final BatchCreateDaiEncodingProfilesResponse batchCreateDaiEncodingProfiles(BatchCreateDaiEncodingProfilesRequest request)

Batch creates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchCreateDaiEncodingProfilesRequest request =
           BatchCreateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateDaiEncodingProfileRequest>())
               .build();
       BatchCreateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchCreateDaiEncodingProfiles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesResponse)` |   
  
### batchCreateDaiEncodingProfiles(String parent, List<CreateDaiEncodingProfileRequest> requests)
    
    
    public final BatchCreateDaiEncodingProfilesResponse batchCreateDaiEncodingProfiles(String parent, List<CreateDaiEncodingProfileRequest> requests)

Batch creates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchCreateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchCreateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `DaiEncodingProfiles` will be created. Format: `networks/{network_code}` The parent field in the CreateDaiEncodingProfileRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesResponse)` |   
  
### batchCreateDaiEncodingProfilesCallable()
    
    
    public final UnaryCallable<BatchCreateDaiEncodingProfilesRequest,BatchCreateDaiEncodingProfilesResponse> batchCreateDaiEncodingProfilesCallable()

Batch creates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchCreateDaiEncodingProfilesRequest request =
           BatchCreateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateDaiEncodingProfileRequest>())
               .build();
       ApiFuture<BatchCreateDaiEncodingProfilesResponse> future =
           daiEncodingProfileServiceClient
               .batchCreateDaiEncodingProfilesCallable()
               .futureCall(request);
       // Do something.
       BatchCreateDaiEncodingProfilesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesRequest),[BatchCreateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiEncodingProfilesResponse)>` |   
  
### batchUpdateDaiEncodingProfiles(@Nullable NetworkName parent, List<UpdateDaiEncodingProfileRequest> requests)
    
    
    public final BatchUpdateDaiEncodingProfilesResponse batchUpdateDaiEncodingProfiles(@Nullable NetworkName parent, List<UpdateDaiEncodingProfileRequest> requests)

Batch updates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchUpdateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchUpdateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `DaiEncodingProfiles` will be updated. Format: `networks/{network_code}` The parent field in the UpdateDaiEncodingProfileRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesResponse)` |   
  
### batchUpdateDaiEncodingProfiles(BatchUpdateDaiEncodingProfilesRequest request)
    
    
    public final BatchUpdateDaiEncodingProfilesResponse batchUpdateDaiEncodingProfiles(BatchUpdateDaiEncodingProfilesRequest request)

Batch updates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchUpdateDaiEncodingProfilesRequest request =
           BatchUpdateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateDaiEncodingProfileRequest>())
               .build();
       BatchUpdateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchUpdateDaiEncodingProfiles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesResponse)` |   
  
### batchUpdateDaiEncodingProfiles(String parent, List<UpdateDaiEncodingProfileRequest> requests)
    
    
    public final BatchUpdateDaiEncodingProfilesResponse batchUpdateDaiEncodingProfiles(String parent, List<UpdateDaiEncodingProfileRequest> requests)

Batch updates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateDaiEncodingProfileRequest> requests = new ArrayList<>();
       BatchUpdateDaiEncodingProfilesResponse response =
           daiEncodingProfileServiceClient.batchUpdateDaiEncodingProfiles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `DaiEncodingProfiles` will be updated. Format: `networks/{network_code}` The parent field in the UpdateDaiEncodingProfileRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiEncodingProfileRequest)>`  
Required. The `DaiEncodingProfile` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesResponse)` |   
  
### batchUpdateDaiEncodingProfilesCallable()
    
    
    public final UnaryCallable<BatchUpdateDaiEncodingProfilesRequest,BatchUpdateDaiEncodingProfilesResponse> batchUpdateDaiEncodingProfilesCallable()

Batch updates `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       BatchUpdateDaiEncodingProfilesRequest request =
           BatchUpdateDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateDaiEncodingProfileRequest>())
               .build();
       ApiFuture<BatchUpdateDaiEncodingProfilesResponse> future =
           daiEncodingProfileServiceClient
               .batchUpdateDaiEncodingProfilesCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateDaiEncodingProfilesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesRequest),[BatchUpdateDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiEncodingProfilesResponse)>` |   
  
### close()
    
    
    public final void close()

### createDaiEncodingProfile(@Nullable NetworkName parent, DaiEncodingProfile daiEncodingProfile)
    
    
    public final DaiEncodingProfile createDaiEncodingProfile(@Nullable NetworkName parent, DaiEncodingProfile daiEncodingProfile)

Creates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       DaiEncodingProfile daiEncodingProfile = DaiEncodingProfile.newBuilder().build();
       DaiEncodingProfile response =
           daiEncodingProfileServiceClient.createDaiEncodingProfile(parent, daiEncodingProfile);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `DaiEncodingProfile` will be created. Format: `networks/{network_code}`  
`daiEncodingProfile` | `[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)`  
Required. The `DaiEncodingProfile` to create.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### createDaiEncodingProfile(CreateDaiEncodingProfileRequest request)
    
    
    public final DaiEncodingProfile createDaiEncodingProfile(CreateDaiEncodingProfileRequest request)

Creates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       CreateDaiEncodingProfileRequest request =
           CreateDaiEncodingProfileRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setDaiEncodingProfile(DaiEncodingProfile.newBuilder().build())
               .build();
       DaiEncodingProfile response =
           daiEncodingProfileServiceClient.createDaiEncodingProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiEncodingProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### createDaiEncodingProfile(String parent, DaiEncodingProfile daiEncodingProfile)
    
    
    public final DaiEncodingProfile createDaiEncodingProfile(String parent, DaiEncodingProfile daiEncodingProfile)

Creates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       DaiEncodingProfile daiEncodingProfile = DaiEncodingProfile.newBuilder().build();
       DaiEncodingProfile response =
           daiEncodingProfileServiceClient.createDaiEncodingProfile(parent, daiEncodingProfile);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `DaiEncodingProfile` will be created. Format: `networks/{network_code}`  
`daiEncodingProfile` | `[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)`  
Required. The `DaiEncodingProfile` to create.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### createDaiEncodingProfileCallable()
    
    
    public final UnaryCallable<CreateDaiEncodingProfileRequest,DaiEncodingProfile> createDaiEncodingProfileCallable()

Creates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       CreateDaiEncodingProfileRequest request =
           CreateDaiEncodingProfileRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setDaiEncodingProfile(DaiEncodingProfile.newBuilder().build())
               .build();
       ApiFuture<DaiEncodingProfile> future =
           daiEncodingProfileServiceClient.createDaiEncodingProfileCallable().futureCall(request);
       // Do something.
       DaiEncodingProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiEncodingProfileRequest),[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)>` |   
  
### getDaiEncodingProfile(@Nullable DaiEncodingProfileName name)
    
    
    public final DaiEncodingProfile getDaiEncodingProfile(@Nullable DaiEncodingProfileName name)

Retrieves a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       DaiEncodingProfileName name =
           DaiEncodingProfileName.of("[NETWORK_CODE]", "[DAI_ENCODING_PROFILE]");
       DaiEncodingProfile response = daiEncodingProfileServiceClient.getDaiEncodingProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiEncodingProfileName`  
Required. The resource name of the DaiEncodingProfile. Format: `networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### getDaiEncodingProfile(GetDaiEncodingProfileRequest request)
    
    
    public final DaiEncodingProfile getDaiEncodingProfile(GetDaiEncodingProfileRequest request)

Retrieves a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       GetDaiEncodingProfileRequest request =
           GetDaiEncodingProfileRequest.newBuilder()
               .setName(
                   DaiEncodingProfileName.of("[NETWORK_CODE]", "[DAI_ENCODING_PROFILE]").toString())
               .build();
       DaiEncodingProfile response = daiEncodingProfileServiceClient.getDaiEncodingProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiEncodingProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### getDaiEncodingProfile(String name)
    
    
    public final DaiEncodingProfile getDaiEncodingProfile(String name)

Retrieves a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String name =
           DaiEncodingProfileName.of("[NETWORK_CODE]", "[DAI_ENCODING_PROFILE]").toString();
       DaiEncodingProfile response = daiEncodingProfileServiceClient.getDaiEncodingProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DaiEncodingProfile. Format: `networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### getDaiEncodingProfileCallable()
    
    
    public final UnaryCallable<GetDaiEncodingProfileRequest,DaiEncodingProfile> getDaiEncodingProfileCallable()

Retrieves a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       GetDaiEncodingProfileRequest request =
           GetDaiEncodingProfileRequest.newBuilder()
               .setName(
                   DaiEncodingProfileName.of("[NETWORK_CODE]", "[DAI_ENCODING_PROFILE]").toString())
               .build();
       ApiFuture<DaiEncodingProfile> future =
           daiEncodingProfileServiceClient.getDaiEncodingProfileCallable().futureCall(request);
       // Do something.
       DaiEncodingProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiEncodingProfileRequest),[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)>` |   
  
### getSettings()
    
    
    public final @Nullable DaiEncodingProfileServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiEncodingProfileServiceSettings` |   
  
### getStub()
    
    
    public DaiEncodingProfileServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiEncodingProfileServiceStub)` |   
  
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
  
### listDaiEncodingProfiles(@Nullable NetworkName parent)
    
    
    public final DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse listDaiEncodingProfiles(@Nullable NetworkName parent)

Lists `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (DaiEncodingProfile element :
           daiEncodingProfileServiceClient.listDaiEncodingProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of DaiEncodingProfiles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse)` |   
  
### listDaiEncodingProfiles(ListDaiEncodingProfilesRequest request)
    
    
    public final DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse listDaiEncodingProfiles(ListDaiEncodingProfilesRequest request)

Lists `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       ListDaiEncodingProfilesRequest request =
           ListDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (DaiEncodingProfile element :
           daiEncodingProfileServiceClient.listDaiEncodingProfiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiEncodingProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse)` |   
  
### listDaiEncodingProfiles(String parent)
    
    
    public final DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse listDaiEncodingProfiles(String parent)

Lists `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (DaiEncodingProfile element :
           daiEncodingProfileServiceClient.listDaiEncodingProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of DaiEncodingProfiles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse)` |   
  
### listDaiEncodingProfilesCallable()
    
    
    public final UnaryCallable<ListDaiEncodingProfilesRequest,ListDaiEncodingProfilesResponse> listDaiEncodingProfilesCallable()

Lists `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       ListDaiEncodingProfilesRequest request =
           ListDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListDaiEncodingProfilesResponse response =
             daiEncodingProfileServiceClient.listDaiEncodingProfilesCallable().call(request);
         for (DaiEncodingProfile element : response.getDaiEncodingProfilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiEncodingProfilesRequest),[ListDaiEncodingProfilesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiEncodingProfilesResponse)>` |   
  
### listDaiEncodingProfilesPagedCallable()
    
    
    public final UnaryCallable<ListDaiEncodingProfilesRequest,DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse> listDaiEncodingProfilesPagedCallable()

Lists `DaiEncodingProfile` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       ListDaiEncodingProfilesRequest request =
           ListDaiEncodingProfilesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<DaiEncodingProfile> future =
           daiEncodingProfileServiceClient
               .listDaiEncodingProfilesPagedCallable()
               .futureCall(request);
       // Do something.
       for (DaiEncodingProfile element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDaiEncodingProfilesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiEncodingProfilesRequest),[ListDaiEncodingProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileServiceClient.ListDaiEncodingProfilesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDaiEncodingProfile(DaiEncodingProfile daiEncodingProfile, FieldMask updateMask)
    
    
    public final DaiEncodingProfile updateDaiEncodingProfile(DaiEncodingProfile daiEncodingProfile, FieldMask updateMask)

Updates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       DaiEncodingProfile daiEncodingProfile = DaiEncodingProfile.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DaiEncodingProfile response =
           daiEncodingProfileServiceClient.updateDaiEncodingProfile(daiEncodingProfile, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`daiEncodingProfile` | `[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)`  
Required. The `DaiEncodingProfile` to update. The `DaiEncodingProfile`'s `name` is used to identify the `DaiEncodingProfile` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### updateDaiEncodingProfile(UpdateDaiEncodingProfileRequest request)
    
    
    public final DaiEncodingProfile updateDaiEncodingProfile(UpdateDaiEncodingProfileRequest request)

Updates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       UpdateDaiEncodingProfileRequest request =
           UpdateDaiEncodingProfileRequest.newBuilder()
               .setDaiEncodingProfile(DaiEncodingProfile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DaiEncodingProfile response =
           daiEncodingProfileServiceClient.updateDaiEncodingProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiEncodingProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)` |   
  
### updateDaiEncodingProfileCallable()
    
    
    public final UnaryCallable<UpdateDaiEncodingProfileRequest,DaiEncodingProfile> updateDaiEncodingProfileCallable()

Updates a `DaiEncodingProfile` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiEncodingProfileServiceClient daiEncodingProfileServiceClient =
         DaiEncodingProfileServiceClient.create()) {
       UpdateDaiEncodingProfileRequest request =
           UpdateDaiEncodingProfileRequest.newBuilder()
               .setDaiEncodingProfile(DaiEncodingProfile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DaiEncodingProfile> future =
           daiEncodingProfileServiceClient.updateDaiEncodingProfileCallable().futureCall(request);
       // Do something.
       DaiEncodingProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDaiEncodingProfileRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiEncodingProfileRequest),[DaiEncodingProfile](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfile)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
