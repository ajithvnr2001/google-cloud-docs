---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient
title: Class SlateServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:04.054598+00:00
---

# Class SlateServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SlateServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/SlateServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Slate` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       SlateName name = SlateName.of("[NETWORK_CODE]", "[SLATE]");
       Slate response = slateServiceClient.getSlate(name);
     }
     

Note: close() needs to be called on the SlateServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetSlate |  Retrieves a `Slate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSlate(GetSlateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSlate(SlateName name) 
  * getSlate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSlateCallable() 

  
ListSlates |  Lists `Slate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSlates(ListSlatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSlates(NetworkName parent) 
  * listSlates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSlatesPagedCallable() 
  * listSlatesCallable() 

  
CreateSlate |  Creates a `Slate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSlate(CreateSlateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSlate(NetworkName parent, Slate slate) 
  * createSlate(String parent, Slate slate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSlateCallable() 

  
BatchCreateSlates |  Batch creates `Slate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateSlates(NetworkName parent, List<CreateSlateRequest> requests) 
  * batchCreateSlates(String parent, List<CreateSlateRequest> requests) 
  * batchCreateSlates(BatchCreateSlatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateSlatesCallable() 

  
UpdateSlate |  Updates a `Slate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSlate(UpdateSlateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSlate(Slate slate, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSlateCallable() 

  
BatchUpdateSlates |  Batch updates `Slate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateSlates(NetworkName parent, List<UpdateSlateRequest> requests) 
  * batchUpdateSlates(String parent, List<UpdateSlateRequest> requests) 
  * batchUpdateSlates(BatchUpdateSlatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateSlatesCallable() 

  
BatchArchiveSlates |  Batch archives `Slate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveSlates(BatchArchiveSlatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveSlates(NetworkName parent, List<String> names) 
  * batchArchiveSlates(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveSlatesCallable() 

  
BatchUnarchiveSlates |  Batch unarchives `Slate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUnarchiveSlates(BatchUnarchiveSlatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchUnarchiveSlates(NetworkName parent, List<String> names) 
  * batchUnarchiveSlates(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUnarchiveSlatesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SlateServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SlateServiceSettings slateServiceSettings =
         SlateServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SlateServiceClient slateServiceClient = SlateServiceClient.create(slateServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SlateServiceSettings slateServiceSettings =
         SlateServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SlateServiceClient slateServiceClient = SlateServiceClient.create(slateServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SlateServiceClient

## Static Methods 

### create()
    
    
    public static final SlateServiceClient create()

Constructs an instance of SlateServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SlateServiceSettings settings)
    
    
    public static final SlateServiceClient create(SlateServiceSettings settings)

Constructs an instance of SlateServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SlateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SlateServiceStub stub)
    
    
    public static final SlateServiceClient create(SlateServiceStub stub)

Constructs an instance of SlateServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SlateServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SlateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SlateServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient)` |   
  
## Constructors 

### SlateServiceClient(SlateServiceSettings settings)
    
    
    protected SlateServiceClient(SlateServiceSettings settings)

Constructs an instance of SlateServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SlateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceSettings)`  
  
  
### SlateServiceClient(SlateServiceStub stub)
    
    
    protected SlateServiceClient(SlateServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SlateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SlateServiceStub)`  
  
  
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
  
### batchArchiveSlates(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveSlatesResponse batchArchiveSlates(@Nullable NetworkName parent, List<String> names)

Batch archives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveSlatesResponse response = slateServiceClient.batchArchiveSlates(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource containing the slates. Format: "networks/{network_code}"  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the slates to archive. Format: "networks/{network_code}/slates/{slate_id}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesResponse)` |   
  
### batchArchiveSlates(BatchArchiveSlatesRequest request)
    
    
    public final BatchArchiveSlatesResponse batchArchiveSlates(BatchArchiveSlatesRequest request)

Batch archives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchArchiveSlatesRequest request =
           BatchArchiveSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveSlatesResponse response = slateServiceClient.batchArchiveSlates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesResponse)` |   
  
### batchArchiveSlates(String parent, List<String> names)
    
    
    public final BatchArchiveSlatesResponse batchArchiveSlates(String parent, List<String> names)

Batch archives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveSlatesResponse response = slateServiceClient.batchArchiveSlates(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource containing the slates. Format: "networks/{network_code}"  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the slates to archive. Format: "networks/{network_code}/slates/{slate_id}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesResponse)` |   
  
### batchArchiveSlatesCallable()
    
    
    public final UnaryCallable<BatchArchiveSlatesRequest,BatchArchiveSlatesResponse> batchArchiveSlatesCallable()

Batch archives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchArchiveSlatesRequest request =
           BatchArchiveSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveSlatesResponse> future =
           slateServiceClient.batchArchiveSlatesCallable().futureCall(request);
       // Do something.
       BatchArchiveSlatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesRequest),[BatchArchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveSlatesResponse)>` |   
  
### batchCreateSlates(@Nullable NetworkName parent, List<CreateSlateRequest> requests)
    
    
    public final BatchCreateSlatesResponse batchCreateSlates(@Nullable NetworkName parent, List<CreateSlateRequest> requests)

Batch creates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateSlateRequest> requests = new ArrayList<>();
       BatchCreateSlatesResponse response = slateServiceClient.batchCreateSlates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Slates` will be created. Format: `networks/{network_code}` The parent field in the CreateSlateRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSlateRequest)>`  
Required. The `Slate` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesResponse)` |   
  
### batchCreateSlates(BatchCreateSlatesRequest request)
    
    
    public final BatchCreateSlatesResponse batchCreateSlates(BatchCreateSlatesRequest request)

Batch creates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchCreateSlatesRequest request =
           BatchCreateSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateSlateRequest>())
               .build();
       BatchCreateSlatesResponse response = slateServiceClient.batchCreateSlates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesResponse)` |   
  
### batchCreateSlates(String parent, List<CreateSlateRequest> requests)
    
    
    public final BatchCreateSlatesResponse batchCreateSlates(String parent, List<CreateSlateRequest> requests)

Batch creates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateSlateRequest> requests = new ArrayList<>();
       BatchCreateSlatesResponse response = slateServiceClient.batchCreateSlates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Slates` will be created. Format: `networks/{network_code}` The parent field in the CreateSlateRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSlateRequest)>`  
Required. The `Slate` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesResponse)` |   
  
### batchCreateSlatesCallable()
    
    
    public final UnaryCallable<BatchCreateSlatesRequest,BatchCreateSlatesResponse> batchCreateSlatesCallable()

Batch creates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchCreateSlatesRequest request =
           BatchCreateSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateSlateRequest>())
               .build();
       ApiFuture<BatchCreateSlatesResponse> future =
           slateServiceClient.batchCreateSlatesCallable().futureCall(request);
       // Do something.
       BatchCreateSlatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesRequest),[BatchCreateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSlatesResponse)>` |   
  
### batchUnarchiveSlates(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchUnarchiveSlatesResponse batchUnarchiveSlates(@Nullable NetworkName parent, List<String> names)

Batch unarchives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchUnarchiveSlatesResponse response =
           slateServiceClient.batchUnarchiveSlates(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource containing the slates. Format: "networks/{network_code}"  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the slates to unarchive. Format: "networks/{network_code}/slates/{slate_id}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesResponse)` |   
  
### batchUnarchiveSlates(BatchUnarchiveSlatesRequest request)
    
    
    public final BatchUnarchiveSlatesResponse batchUnarchiveSlates(BatchUnarchiveSlatesRequest request)

Batch unarchives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchUnarchiveSlatesRequest request =
           BatchUnarchiveSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchUnarchiveSlatesResponse response = slateServiceClient.batchUnarchiveSlates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUnarchiveSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesResponse)` |   
  
### batchUnarchiveSlates(String parent, List<String> names)
    
    
    public final BatchUnarchiveSlatesResponse batchUnarchiveSlates(String parent, List<String> names)

Batch unarchives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchUnarchiveSlatesResponse response =
           slateServiceClient.batchUnarchiveSlates(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource containing the slates. Format: "networks/{network_code}"  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the slates to unarchive. Format: "networks/{network_code}/slates/{slate_id}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesResponse)` |   
  
### batchUnarchiveSlatesCallable()
    
    
    public final UnaryCallable<BatchUnarchiveSlatesRequest,BatchUnarchiveSlatesResponse> batchUnarchiveSlatesCallable()

Batch unarchives `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchUnarchiveSlatesRequest request =
           BatchUnarchiveSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchUnarchiveSlatesResponse> future =
           slateServiceClient.batchUnarchiveSlatesCallable().futureCall(request);
       // Do something.
       BatchUnarchiveSlatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUnarchiveSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesRequest),[BatchUnarchiveSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveSlatesResponse)>` |   
  
### batchUpdateSlates(@Nullable NetworkName parent, List<UpdateSlateRequest> requests)
    
    
    public final BatchUpdateSlatesResponse batchUpdateSlates(@Nullable NetworkName parent, List<UpdateSlateRequest> requests)

Batch updates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateSlateRequest> requests = new ArrayList<>();
       BatchUpdateSlatesResponse response = slateServiceClient.batchUpdateSlates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Slates` will be updated. Format: `networks/{network_code}` The parent field in the UpdateSlateRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSlateRequest)>`  
Required. The `Slate` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesResponse)` |   
  
### batchUpdateSlates(BatchUpdateSlatesRequest request)
    
    
    public final BatchUpdateSlatesResponse batchUpdateSlates(BatchUpdateSlatesRequest request)

Batch updates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchUpdateSlatesRequest request =
           BatchUpdateSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateSlateRequest>())
               .build();
       BatchUpdateSlatesResponse response = slateServiceClient.batchUpdateSlates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesResponse)` |   
  
### batchUpdateSlates(String parent, List<UpdateSlateRequest> requests)
    
    
    public final BatchUpdateSlatesResponse batchUpdateSlates(String parent, List<UpdateSlateRequest> requests)

Batch updates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateSlateRequest> requests = new ArrayList<>();
       BatchUpdateSlatesResponse response = slateServiceClient.batchUpdateSlates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Slates` will be updated. Format: `networks/{network_code}` The parent field in the UpdateSlateRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSlateRequest)>`  
Required. The `Slate` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesResponse)` |   
  
### batchUpdateSlatesCallable()
    
    
    public final UnaryCallable<BatchUpdateSlatesRequest,BatchUpdateSlatesResponse> batchUpdateSlatesCallable()

Batch updates `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       BatchUpdateSlatesRequest request =
           BatchUpdateSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateSlateRequest>())
               .build();
       ApiFuture<BatchUpdateSlatesResponse> future =
           slateServiceClient.batchUpdateSlatesCallable().futureCall(request);
       // Do something.
       BatchUpdateSlatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesRequest),[BatchUpdateSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSlatesResponse)>` |   
  
### close()
    
    
    public final void close()

### createSlate(@Nullable NetworkName parent, Slate slate)
    
    
    public final Slate createSlate(@Nullable NetworkName parent, Slate slate)

Creates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Slate slate = Slate.newBuilder().build();
       Slate response = slateServiceClient.createSlate(parent, slate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Slate` will be created. Format: `networks/{network_code}`  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)`  
Required. The `Slate` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### createSlate(CreateSlateRequest request)
    
    
    public final Slate createSlate(CreateSlateRequest request)

Creates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       CreateSlateRequest request =
           CreateSlateRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setSlate(Slate.newBuilder().build())
               .build();
       Slate response = slateServiceClient.createSlate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### createSlate(String parent, Slate slate)
    
    
    public final Slate createSlate(String parent, Slate slate)

Creates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Slate slate = Slate.newBuilder().build();
       Slate response = slateServiceClient.createSlate(parent, slate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Slate` will be created. Format: `networks/{network_code}`  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)`  
Required. The `Slate` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### createSlateCallable()
    
    
    public final UnaryCallable<CreateSlateRequest,Slate> createSlateCallable()

Creates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       CreateSlateRequest request =
           CreateSlateRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setSlate(Slate.newBuilder().build())
               .build();
       ApiFuture<Slate> future = slateServiceClient.createSlateCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)>` |   
  
### getSettings()
    
    
    public final @Nullable SlateServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.SlateServiceSettings` |   
  
### getSlate(@Nullable SlateName name)
    
    
    public final Slate getSlate(@Nullable SlateName name)

Retrieves a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       SlateName name = SlateName.of("[NETWORK_CODE]", "[SLATE]");
       Slate response = slateServiceClient.getSlate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.SlateName`  
Required. The resource name of the Slate to retrieve. Format: `networks/{network_code}/slates/{slate_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### getSlate(GetSlateRequest request)
    
    
    public final Slate getSlate(GetSlateRequest request)

Retrieves a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       GetSlateRequest request =
           GetSlateRequest.newBuilder()
               .setName(SlateName.of("[NETWORK_CODE]", "[SLATE]").toString())
               .build();
       Slate response = slateServiceClient.getSlate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### getSlate(String name)
    
    
    public final Slate getSlate(String name)

Retrieves a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String name = SlateName.of("[NETWORK_CODE]", "[SLATE]").toString();
       Slate response = slateServiceClient.getSlate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Slate to retrieve. Format: `networks/{network_code}/slates/{slate_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### getSlateCallable()
    
    
    public final UnaryCallable<GetSlateRequest,Slate> getSlateCallable()

Retrieves a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       GetSlateRequest request =
           GetSlateRequest.newBuilder()
               .setName(SlateName.of("[NETWORK_CODE]", "[SLATE]").toString())
               .build();
       ApiFuture<Slate> future = slateServiceClient.getSlateCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)>` |   
  
### getStub()
    
    
    public SlateServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SlateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SlateServiceStub)` |   
  
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
  
### listSlates(@Nullable NetworkName parent)
    
    
    public final SlateServiceClient.ListSlatesPagedResponse listSlates(@Nullable NetworkName parent)

Lists `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Slate element : slateServiceClient.listSlates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource containing the Slates. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient.ListSlatesPagedResponse)` |   
  
### listSlates(ListSlatesRequest request)
    
    
    public final SlateServiceClient.ListSlatesPagedResponse listSlates(ListSlatesRequest request)

Lists `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Slate element : slateServiceClient.listSlates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient.ListSlatesPagedResponse)` |   
  
### listSlates(String parent)
    
    
    public final SlateServiceClient.ListSlatesPagedResponse listSlates(String parent)

Lists `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Slate element : slateServiceClient.listSlates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource containing the Slates. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[SlateServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient.ListSlatesPagedResponse)` |   
  
### listSlatesCallable()
    
    
    public final UnaryCallable<ListSlatesRequest,ListSlatesResponse> listSlatesCallable()

Lists `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListSlatesResponse response = slateServiceClient.listSlatesCallable().call(request);
         for (Slate element : response.getSlatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSlatesRequest),[ListSlatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSlatesResponse)>` |   
  
### listSlatesPagedCallable()
    
    
    public final UnaryCallable<ListSlatesRequest,SlateServiceClient.ListSlatesPagedResponse> listSlatesPagedCallable()

Lists `Slate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Slate> future = slateServiceClient.listSlatesPagedCallable().futureCall(request);
       // Do something.
       for (Slate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSlatesRequest),[ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SlateServiceClient.ListSlatesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSlate(Slate slate, FieldMask updateMask)
    
    
    public final Slate updateSlate(Slate slate, FieldMask updateMask)

Updates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       Slate slate = Slate.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Slate response = slateServiceClient.updateSlate(slate, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)`  
Required. The `Slate` to update. The `Slate`'s `name` is used to identify the `Slate` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### updateSlate(UpdateSlateRequest request)
    
    
    public final Slate updateSlate(UpdateSlateRequest request)

Updates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       UpdateSlateRequest request =
           UpdateSlateRequest.newBuilder()
               .setSlate(Slate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Slate response = slateServiceClient.updateSlate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)` |   
  
### updateSlateCallable()
    
    
    public final UnaryCallable<UpdateSlateRequest,Slate> updateSlateCallable()

Updates a `Slate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SlateServiceClient slateServiceClient = SlateServiceClient.create()) {
       UpdateSlateRequest request =
           UpdateSlateRequest.newBuilder()
               .setSlate(Slate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Slate> future = slateServiceClient.updateSlateCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Slate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
