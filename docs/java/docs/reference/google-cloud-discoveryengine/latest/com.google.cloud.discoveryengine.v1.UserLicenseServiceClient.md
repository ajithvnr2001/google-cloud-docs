---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient
title: Class UserLicenseServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:50.204295+00:00
---

# Class UserLicenseServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserLicenseServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/UserLicenseServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing User Licenses.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       UserStoreName parent = UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]");
       for (UserLicense element : userLicenseServiceClient.listUserLicenses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the UserLicenseServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListUserLicenses |  Lists the User Licenses. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserLicenses(ListUserLicensesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserLicenses(UserStoreName parent) 
  * listUserLicenses(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserLicensesPagedCallable() 
  * listUserLicensesCallable() 

  
BatchUpdateUserLicenses |  Updates the User License. This method is used for batch assign/unassign licenses to users. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateUserLicensesAsync(BatchUpdateUserLicensesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateUserLicensesOperationCallable() 
  * batchUpdateUserLicensesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of UserLicenseServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserLicenseServiceSettings userLicenseServiceSettings =
         UserLicenseServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     UserLicenseServiceClient userLicenseServiceClient =
         UserLicenseServiceClient.create(userLicenseServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserLicenseServiceSettings userLicenseServiceSettings =
         UserLicenseServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     UserLicenseServiceClient userLicenseServiceClient =
         UserLicenseServiceClient.create(userLicenseServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserLicenseServiceSettings userLicenseServiceSettings =
         UserLicenseServiceSettings.newHttpJsonBuilder().build();
     UserLicenseServiceClient userLicenseServiceClient =
         UserLicenseServiceClient.create(userLicenseServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UserLicenseServiceClient

## Static Methods 

### create()
    
    
    public static final UserLicenseServiceClient create()

Constructs an instance of UserLicenseServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserLicenseServiceSettings settings)
    
    
    public static final UserLicenseServiceClient create(UserLicenseServiceSettings settings)

Constructs an instance of UserLicenseServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserLicenseServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserLicenseServiceStub stub)
    
    
    public static final UserLicenseServiceClient create(UserLicenseServiceStub stub)

Constructs an instance of UserLicenseServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(UserLicenseServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserLicenseServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.UserLicenseServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient)` |   
  
## Constructors 

### UserLicenseServiceClient(UserLicenseServiceSettings settings)
    
    
    protected UserLicenseServiceClient(UserLicenseServiceSettings settings)

Constructs an instance of UserLicenseServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserLicenseServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceSettings)`  
  
  
### UserLicenseServiceClient(UserLicenseServiceStub stub)
    
    
    protected UserLicenseServiceClient(UserLicenseServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserLicenseServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.UserLicenseServiceStub)`  
  
  
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
  
### batchUpdateUserLicensesAsync(BatchUpdateUserLicensesRequest request)
    
    
    public final OperationFuture<BatchUpdateUserLicensesResponse,BatchUpdateUserLicensesMetadata> batchUpdateUserLicensesAsync(BatchUpdateUserLicensesRequest request)

Updates the User License. This method is used for batch assign/unassign licenses to users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       BatchUpdateUserLicensesRequest request =
           BatchUpdateUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setDeleteUnassignedUserLicenses(true)
               .build();
       BatchUpdateUserLicensesResponse response =
           userLicenseServiceClient.batchUpdateUserLicensesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateUserLicensesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesResponse),[BatchUpdateUserLicensesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesMetadata)>` |   
  
### batchUpdateUserLicensesCallable()
    
    
    public final UnaryCallable<BatchUpdateUserLicensesRequest,Operation> batchUpdateUserLicensesCallable()

Updates the User License. This method is used for batch assign/unassign licenses to users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       BatchUpdateUserLicensesRequest request =
           BatchUpdateUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setDeleteUnassignedUserLicenses(true)
               .build();
       ApiFuture<Operation> future =
           userLicenseServiceClient.batchUpdateUserLicensesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchUpdateUserLicensesOperationCallable()
    
    
    public final OperationCallable<BatchUpdateUserLicensesRequest,BatchUpdateUserLicensesResponse,BatchUpdateUserLicensesMetadata> batchUpdateUserLicensesOperationCallable()

Updates the User License. This method is used for batch assign/unassign licenses to users.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       BatchUpdateUserLicensesRequest request =
           BatchUpdateUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setDeleteUnassignedUserLicenses(true)
               .build();
       OperationFuture<BatchUpdateUserLicensesResponse, BatchUpdateUserLicensesMetadata> future =
           userLicenseServiceClient.batchUpdateUserLicensesOperationCallable().futureCall(request);
       // Do something.
       BatchUpdateUserLicensesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesRequest),[BatchUpdateUserLicensesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesResponse),[BatchUpdateUserLicensesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesMetadata)>` |   
  
### close()
    
    
    public final void close()

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable UserLicenseServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.UserLicenseServiceSettings` |   
  
### getStub()
    
    
    public UserLicenseServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.UserLicenseServiceStub)` |   
  
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
  
### listUserLicenses(@Nullable UserStoreName parent)
    
    
    public final UserLicenseServiceClient.ListUserLicensesPagedResponse listUserLicenses(@Nullable UserStoreName parent)

Lists the User Licenses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       UserStoreName parent = UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]");
       for (UserLicense element : userLicenseServiceClient.listUserLicenses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.UserStoreName`  
Required. The parent [UserStore][] resource name, format: `projects/{project}/locations/{location}/userStores/{user_store_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient.ListUserLicensesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient.ListUserLicensesPagedResponse)` |   
  
### listUserLicenses(ListUserLicensesRequest request)
    
    
    public final UserLicenseServiceClient.ListUserLicensesPagedResponse listUserLicenses(ListUserLicensesRequest request)

Lists the User Licenses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       ListUserLicensesRequest request =
           ListUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (UserLicense element : userLicenseServiceClient.listUserLicenses(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListUserLicensesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient.ListUserLicensesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient.ListUserLicensesPagedResponse)` |   
  
### listUserLicenses(String parent)
    
    
    public final UserLicenseServiceClient.ListUserLicensesPagedResponse listUserLicenses(String parent)

Lists the User Licenses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       String parent = UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString();
       for (UserLicense element : userLicenseServiceClient.listUserLicenses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent [UserStore][] resource name, format: `projects/{project}/locations/{location}/userStores/{user_store_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[UserLicenseServiceClient.ListUserLicensesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient.ListUserLicensesPagedResponse)` |   
  
### listUserLicensesCallable()
    
    
    public final UnaryCallable<ListUserLicensesRequest,ListUserLicensesResponse> listUserLicensesCallable()

Lists the User Licenses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       ListUserLicensesRequest request =
           ListUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListUserLicensesResponse response =
             userLicenseServiceClient.listUserLicensesCallable().call(request);
         for (UserLicense element : response.getUserLicensesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListUserLicensesRequest),[ListUserLicensesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListUserLicensesResponse)>` |   
  
### listUserLicensesPagedCallable()
    
    
    public final UnaryCallable<ListUserLicensesRequest,UserLicenseServiceClient.ListUserLicensesPagedResponse> listUserLicensesPagedCallable()

Lists the User Licenses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserLicenseServiceClient userLicenseServiceClient = UserLicenseServiceClient.create()) {
       ListUserLicensesRequest request =
           ListUserLicensesRequest.newBuilder()
               .setParent(UserStoreName.of("[PROJECT]", "[LOCATION]", "[USER_STORE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<UserLicense> future =
           userLicenseServiceClient.listUserLicensesPagedCallable().futureCall(request);
       // Do something.
       for (UserLicense element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListUserLicensesRequest),[ListUserLicensesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UserLicenseServiceClient.ListUserLicensesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
