---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient
title: Class ApplicationServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:26.491993+00:00
---

# Class ApplicationServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ApplicationServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ApplicationServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Application` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       ApplicationName name = ApplicationName.of("[NETWORK_CODE]", "[APPLICATION]");
       Application response = applicationServiceClient.getApplication(name);
     }
     

Note: close() needs to be called on the ApplicationServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetApplication |  Retrieves a `Application` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getApplication(GetApplicationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getApplication(ApplicationName name) 
  * getApplication(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getApplicationCallable() 

  
ListApplications |  Lists `Application` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listApplications(ListApplicationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listApplications(NetworkName parent) 
  * listApplications(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listApplicationsPagedCallable() 
  * listApplicationsCallable() 

  
CreateApplication |  Creates a `Application` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createApplication(CreateApplicationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createApplication(NetworkName parent, Application application) 
  * createApplication(String parent, Application application) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createApplicationCallable() 

  
BatchCreateApplications |  Creates `Application` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateApplications(NetworkName parent, List<CreateApplicationRequest> requests) 
  * batchCreateApplications(String parent, List<CreateApplicationRequest> requests) 
  * batchCreateApplications(BatchCreateApplicationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateApplicationsCallable() 

  
UpdateApplication |  Updates a `Application` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateApplication(UpdateApplicationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateApplication(Application application, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateApplicationCallable() 

  
BatchUpdateApplications |  Batch updates `Application` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateApplications(NetworkName parent, List<UpdateApplicationRequest> requests) 
  * batchUpdateApplications(String parent, List<UpdateApplicationRequest> requests) 
  * batchUpdateApplications(BatchUpdateApplicationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateApplicationsCallable() 

  
BatchArchiveApplications |  Batch archives `Application` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveApplications(BatchArchiveApplicationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveApplications(NetworkName parent, List<String> names) 
  * batchArchiveApplications(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveApplicationsCallable() 

  
BatchUnarchiveApplications |  Batch unarchives `Application` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUnarchiveApplications(BatchUnarchiveApplicationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchUnarchiveApplications(NetworkName parent, List<String> names) 
  * batchUnarchiveApplications(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUnarchiveApplicationsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ApplicationServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ApplicationServiceSettings applicationServiceSettings =
         ApplicationServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ApplicationServiceClient applicationServiceClient =
         ApplicationServiceClient.create(applicationServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ApplicationServiceSettings applicationServiceSettings =
         ApplicationServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ApplicationServiceClient applicationServiceClient =
         ApplicationServiceClient.create(applicationServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ApplicationServiceClient

## Static Methods 

### create()
    
    
    public static final ApplicationServiceClient create()

Constructs an instance of ApplicationServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ApplicationServiceSettings settings)
    
    
    public static final ApplicationServiceClient create(ApplicationServiceSettings settings)

Constructs an instance of ApplicationServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ApplicationServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ApplicationServiceStub stub)
    
    
    public static final ApplicationServiceClient create(ApplicationServiceStub stub)

Constructs an instance of ApplicationServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ApplicationServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ApplicationServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ApplicationServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient)` |   
  
## Constructors 

### ApplicationServiceClient(ApplicationServiceSettings settings)
    
    
    protected ApplicationServiceClient(ApplicationServiceSettings settings)

Constructs an instance of ApplicationServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ApplicationServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceSettings)`  
  
  
### ApplicationServiceClient(ApplicationServiceStub stub)
    
    
    protected ApplicationServiceClient(ApplicationServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ApplicationServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ApplicationServiceStub)`  
  
  
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
  
### batchArchiveApplications(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveApplicationsResponse batchArchiveApplications(@Nullable NetworkName parent, List<String> names)

Batch archives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveApplicationsResponse response =
           applicationServiceClient.batchArchiveApplications(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource shared by all `Applications` to archive. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The `Application` objects to archive.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsResponse)` |   
  
### batchArchiveApplications(BatchArchiveApplicationsRequest request)
    
    
    public final BatchArchiveApplicationsResponse batchArchiveApplications(BatchArchiveApplicationsRequest request)

Batch archives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchArchiveApplicationsRequest request =
           BatchArchiveApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveApplicationsResponse response =
           applicationServiceClient.batchArchiveApplications(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsResponse)` |   
  
### batchArchiveApplications(String parent, List<String> names)
    
    
    public final BatchArchiveApplicationsResponse batchArchiveApplications(String parent, List<String> names)

Batch archives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveApplicationsResponse response =
           applicationServiceClient.batchArchiveApplications(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource shared by all `Applications` to archive. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The `Application` objects to archive.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsResponse)` |   
  
### batchArchiveApplicationsCallable()
    
    
    public final UnaryCallable<BatchArchiveApplicationsRequest,BatchArchiveApplicationsResponse> batchArchiveApplicationsCallable()

Batch archives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchArchiveApplicationsRequest request =
           BatchArchiveApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveApplicationsResponse> future =
           applicationServiceClient.batchArchiveApplicationsCallable().futureCall(request);
       // Do something.
       BatchArchiveApplicationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsRequest),[BatchArchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveApplicationsResponse)>` |   
  
### batchCreateApplications(@Nullable NetworkName parent, List<CreateApplicationRequest> requests)
    
    
    public final BatchCreateApplicationsResponse batchCreateApplications(@Nullable NetworkName parent, List<CreateApplicationRequest> requests)

Creates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateApplicationRequest> requests = new ArrayList<>();
       BatchCreateApplicationsResponse response =
           applicationServiceClient.batchCreateApplications(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Applications` will be created. Format: `networks/{network_code}` The parent field in the CreateApplicationRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateApplicationRequest)>`  
Required. The `Application` objects to create.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsResponse)` |   
  
### batchCreateApplications(BatchCreateApplicationsRequest request)
    
    
    public final BatchCreateApplicationsResponse batchCreateApplications(BatchCreateApplicationsRequest request)

Creates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchCreateApplicationsRequest request =
           BatchCreateApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateApplicationRequest>())
               .build();
       BatchCreateApplicationsResponse response =
           applicationServiceClient.batchCreateApplications(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsResponse)` |   
  
### batchCreateApplications(String parent, List<CreateApplicationRequest> requests)
    
    
    public final BatchCreateApplicationsResponse batchCreateApplications(String parent, List<CreateApplicationRequest> requests)

Creates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateApplicationRequest> requests = new ArrayList<>();
       BatchCreateApplicationsResponse response =
           applicationServiceClient.batchCreateApplications(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Applications` will be created. Format: `networks/{network_code}` The parent field in the CreateApplicationRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateApplicationRequest)>`  
Required. The `Application` objects to create.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsResponse)` |   
  
### batchCreateApplicationsCallable()
    
    
    public final UnaryCallable<BatchCreateApplicationsRequest,BatchCreateApplicationsResponse> batchCreateApplicationsCallable()

Creates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchCreateApplicationsRequest request =
           BatchCreateApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateApplicationRequest>())
               .build();
       ApiFuture<BatchCreateApplicationsResponse> future =
           applicationServiceClient.batchCreateApplicationsCallable().futureCall(request);
       // Do something.
       BatchCreateApplicationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsRequest),[BatchCreateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateApplicationsResponse)>` |   
  
### batchUnarchiveApplications(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchUnarchiveApplicationsResponse batchUnarchiveApplications(@Nullable NetworkName parent, List<String> names)

Batch unarchives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchUnarchiveApplicationsResponse response =
           applicationServiceClient.batchUnarchiveApplications(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource shared by all `Applications` to Unarchive. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The `Application` objects to unarchive.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsResponse)` |   
  
### batchUnarchiveApplications(BatchUnarchiveApplicationsRequest request)
    
    
    public final BatchUnarchiveApplicationsResponse batchUnarchiveApplications(BatchUnarchiveApplicationsRequest request)

Batch unarchives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchUnarchiveApplicationsRequest request =
           BatchUnarchiveApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchUnarchiveApplicationsResponse response =
           applicationServiceClient.batchUnarchiveApplications(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUnarchiveApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsResponse)` |   
  
### batchUnarchiveApplications(String parent, List<String> names)
    
    
    public final BatchUnarchiveApplicationsResponse batchUnarchiveApplications(String parent, List<String> names)

Batch unarchives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchUnarchiveApplicationsResponse response =
           applicationServiceClient.batchUnarchiveApplications(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource shared by all `Applications` to Unarchive. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The `Application` objects to unarchive.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUnarchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsResponse)` |   
  
### batchUnarchiveApplicationsCallable()
    
    
    public final UnaryCallable<BatchUnarchiveApplicationsRequest,BatchUnarchiveApplicationsResponse> batchUnarchiveApplicationsCallable()

Batch unarchives `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchUnarchiveApplicationsRequest request =
           BatchUnarchiveApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchUnarchiveApplicationsResponse> future =
           applicationServiceClient.batchUnarchiveApplicationsCallable().futureCall(request);
       // Do something.
       BatchUnarchiveApplicationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUnarchiveApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsRequest),[BatchUnarchiveApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUnarchiveApplicationsResponse)>` |   
  
### batchUpdateApplications(@Nullable NetworkName parent, List<UpdateApplicationRequest> requests)
    
    
    public final BatchUpdateApplicationsResponse batchUpdateApplications(@Nullable NetworkName parent, List<UpdateApplicationRequest> requests)

Batch updates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateApplicationRequest> requests = new ArrayList<>();
       BatchUpdateApplicationsResponse response =
           applicationServiceClient.batchUpdateApplications(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Applications` will be updated. Format: `networks/{network_code}` The parent field in the UpdateApplicationRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateApplicationRequest)>`  
Required. The `Application` objects to update.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsResponse)` |   
  
### batchUpdateApplications(BatchUpdateApplicationsRequest request)
    
    
    public final BatchUpdateApplicationsResponse batchUpdateApplications(BatchUpdateApplicationsRequest request)

Batch updates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchUpdateApplicationsRequest request =
           BatchUpdateApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateApplicationRequest>())
               .build();
       BatchUpdateApplicationsResponse response =
           applicationServiceClient.batchUpdateApplications(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsResponse)` |   
  
### batchUpdateApplications(String parent, List<UpdateApplicationRequest> requests)
    
    
    public final BatchUpdateApplicationsResponse batchUpdateApplications(String parent, List<UpdateApplicationRequest> requests)

Batch updates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateApplicationRequest> requests = new ArrayList<>();
       BatchUpdateApplicationsResponse response =
           applicationServiceClient.batchUpdateApplications(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Applications` will be updated. Format: `networks/{network_code}` The parent field in the UpdateApplicationRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateApplicationRequest)>`  
Required. The `Application` objects to update.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsResponse)` |   
  
### batchUpdateApplicationsCallable()
    
    
    public final UnaryCallable<BatchUpdateApplicationsRequest,BatchUpdateApplicationsResponse> batchUpdateApplicationsCallable()

Batch updates `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       BatchUpdateApplicationsRequest request =
           BatchUpdateApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateApplicationRequest>())
               .build();
       ApiFuture<BatchUpdateApplicationsResponse> future =
           applicationServiceClient.batchUpdateApplicationsCallable().futureCall(request);
       // Do something.
       BatchUpdateApplicationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsRequest),[BatchUpdateApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateApplicationsResponse)>` |   
  
### close()
    
    
    public final void close()

### createApplication(@Nullable NetworkName parent, Application application)
    
    
    public final Application createApplication(@Nullable NetworkName parent, Application application)

Creates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Application application = Application.newBuilder().build();
       Application response = applicationServiceClient.createApplication(parent, application);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Application` will be created. Format: `networks/{network_code}`  
`application` | `[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)`  
Required. The `Application` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### createApplication(CreateApplicationRequest request)
    
    
    public final Application createApplication(CreateApplicationRequest request)

Creates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       CreateApplicationRequest request =
           CreateApplicationRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setApplication(Application.newBuilder().build())
               .build();
       Application response = applicationServiceClient.createApplication(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### createApplication(String parent, Application application)
    
    
    public final Application createApplication(String parent, Application application)

Creates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Application application = Application.newBuilder().build();
       Application response = applicationServiceClient.createApplication(parent, application);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Application` will be created. Format: `networks/{network_code}`  
`application` | `[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)`  
Required. The `Application` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### createApplicationCallable()
    
    
    public final UnaryCallable<CreateApplicationRequest,Application> createApplicationCallable()

Creates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       CreateApplicationRequest request =
           CreateApplicationRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setApplication(Application.newBuilder().build())
               .build();
       ApiFuture<Application> future =
           applicationServiceClient.createApplicationCallable().futureCall(request);
       // Do something.
       Application response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateApplicationRequest),[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)>` |   
  
### getApplication(@Nullable ApplicationName name)
    
    
    public final Application getApplication(@Nullable ApplicationName name)

Retrieves a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       ApplicationName name = ApplicationName.of("[NETWORK_CODE]", "[APPLICATION]");
       Application response = applicationServiceClient.getApplication(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ApplicationName`  
Required. The resource name of the Application. Format: `networks/{network_code}/applications/{application_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### getApplication(GetApplicationRequest request)
    
    
    public final Application getApplication(GetApplicationRequest request)

Retrieves a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       GetApplicationRequest request =
           GetApplicationRequest.newBuilder()
               .setName(ApplicationName.of("[NETWORK_CODE]", "[APPLICATION]").toString())
               .build();
       Application response = applicationServiceClient.getApplication(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetApplicationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### getApplication(String name)
    
    
    public final Application getApplication(String name)

Retrieves a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String name = ApplicationName.of("[NETWORK_CODE]", "[APPLICATION]").toString();
       Application response = applicationServiceClient.getApplication(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Application. Format: `networks/{network_code}/applications/{application_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### getApplicationCallable()
    
    
    public final UnaryCallable<GetApplicationRequest,Application> getApplicationCallable()

Retrieves a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       GetApplicationRequest request =
           GetApplicationRequest.newBuilder()
               .setName(ApplicationName.of("[NETWORK_CODE]", "[APPLICATION]").toString())
               .build();
       ApiFuture<Application> future =
           applicationServiceClient.getApplicationCallable().futureCall(request);
       // Do something.
       Application response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetApplicationRequest),[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)>` |   
  
### getSettings()
    
    
    public final @Nullable ApplicationServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ApplicationServiceSettings` |   
  
### getStub()
    
    
    public ApplicationServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ApplicationServiceStub)` |   
  
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
  
### listApplications(@Nullable NetworkName parent)
    
    
    public final ApplicationServiceClient.ListApplicationsPagedResponse listApplications(@Nullable NetworkName parent)

Lists `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Application element : applicationServiceClient.listApplications(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Applications. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient.ListApplicationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient.ListApplicationsPagedResponse)` |   
  
### listApplications(ListApplicationsRequest request)
    
    
    public final ApplicationServiceClient.ListApplicationsPagedResponse listApplications(ListApplicationsRequest request)

Lists `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       ListApplicationsRequest request =
           ListApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Application element : applicationServiceClient.listApplications(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListApplicationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient.ListApplicationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient.ListApplicationsPagedResponse)` |   
  
### listApplications(String parent)
    
    
    public final ApplicationServiceClient.ListApplicationsPagedResponse listApplications(String parent)

Lists `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Application element : applicationServiceClient.listApplications(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Applications. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ApplicationServiceClient.ListApplicationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient.ListApplicationsPagedResponse)` |   
  
### listApplicationsCallable()
    
    
    public final UnaryCallable<ListApplicationsRequest,ListApplicationsResponse> listApplicationsCallable()

Lists `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       ListApplicationsRequest request =
           ListApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListApplicationsResponse response =
             applicationServiceClient.listApplicationsCallable().call(request);
         for (Application element : response.getApplicationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListApplicationsRequest),[ListApplicationsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListApplicationsResponse)>` |   
  
### listApplicationsPagedCallable()
    
    
    public final UnaryCallable<ListApplicationsRequest,ApplicationServiceClient.ListApplicationsPagedResponse> listApplicationsPagedCallable()

Lists `Application` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       ListApplicationsRequest request =
           ListApplicationsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Application> future =
           applicationServiceClient.listApplicationsPagedCallable().futureCall(request);
       // Do something.
       for (Application element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListApplicationsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListApplicationsRequest),[ListApplicationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ApplicationServiceClient.ListApplicationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateApplication(Application application, FieldMask updateMask)
    
    
    public final Application updateApplication(Application application, FieldMask updateMask)

Updates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       Application application = Application.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Application response = applicationServiceClient.updateApplication(application, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`application` | `[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)`  
Required. The `Application` to update. The `Application`'s `name` is used to identify the `Application` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### updateApplication(UpdateApplicationRequest request)
    
    
    public final Application updateApplication(UpdateApplicationRequest request)

Updates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       UpdateApplicationRequest request =
           UpdateApplicationRequest.newBuilder()
               .setApplication(Application.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Application response = applicationServiceClient.updateApplication(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateApplicationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)` |   
  
### updateApplicationCallable()
    
    
    public final UnaryCallable<UpdateApplicationRequest,Application> updateApplicationCallable()

Updates a `Application` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApplicationServiceClient applicationServiceClient = ApplicationServiceClient.create()) {
       UpdateApplicationRequest request =
           UpdateApplicationRequest.newBuilder()
               .setApplication(Application.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Application> future =
           applicationServiceClient.updateApplicationCallable().futureCall(request);
       // Do something.
       Application response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateApplicationRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateApplicationRequest),[Application](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Application)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
