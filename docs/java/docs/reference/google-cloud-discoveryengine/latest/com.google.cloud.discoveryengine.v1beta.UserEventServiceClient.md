---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceClient
title: Class UserEventServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:29.964113+00:00
---

# Class UserEventServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserEventServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1beta/UserEventServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for ingesting end user actions on a website to Discovery Engine API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       WriteUserEventRequest request =
           WriteUserEventRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setUserEvent(UserEvent.newBuilder().build())
               .setWriteAsync(true)
               .build();
       UserEvent response = userEventServiceClient.writeUserEvent(request);
     }
     

Note: close() needs to be called on the UserEventServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
WriteUserEvent |  Writes a single user event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeUserEvent(WriteUserEventRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeUserEventCallable() 

  
CollectUserEvent |  Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain.  This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * collectUserEvent(CollectUserEventRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * collectUserEventCallable() 

  
PurgeUserEvents |  Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeUserEventsAsync(PurgeUserEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeUserEventsOperationCallable() 
  * purgeUserEventsCallable() 

  
ImportUserEvents |  Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.  Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importUserEventsAsync(ImportUserEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importUserEventsOperationCallable() 
  * importUserEventsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of UserEventServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserEventServiceSettings userEventServiceSettings =
         UserEventServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     UserEventServiceClient userEventServiceClient =
         UserEventServiceClient.create(userEventServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserEventServiceSettings userEventServiceSettings =
         UserEventServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     UserEventServiceClient userEventServiceClient =
         UserEventServiceClient.create(userEventServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UserEventServiceSettings userEventServiceSettings =
         UserEventServiceSettings.newHttpJsonBuilder().build();
     UserEventServiceClient userEventServiceClient =
         UserEventServiceClient.create(userEventServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UserEventServiceClient

## Static Methods 

### create()
    
    
    public static final UserEventServiceClient create()

Constructs an instance of UserEventServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserEventServiceSettings settings)
    
    
    public static final UserEventServiceClient create(UserEventServiceSettings settings)

Constructs an instance of UserEventServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserEventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UserEventServiceStub stub)
    
    
    public static final UserEventServiceClient create(UserEventServiceStub stub)

Constructs an instance of UserEventServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(UserEventServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.stub.UserEventServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceClient)` |   
  
## Constructors 

### UserEventServiceClient(UserEventServiceSettings settings)
    
    
    protected UserEventServiceClient(UserEventServiceSettings settings)

Constructs an instance of UserEventServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserEventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEventServiceSettings)`  
  
  
### UserEventServiceClient(UserEventServiceStub stub)
    
    
    protected UserEventServiceClient(UserEventServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.stub.UserEventServiceStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### collectUserEvent(CollectUserEventRequest request)
    
    
    public final HttpBody collectUserEvent(CollectUserEventRequest request)

Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain.

This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       CollectUserEventRequest request =
           CollectUserEventRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setUserEvent("userEvent315571599")
               .setUri("uri116076")
               .setEts(100772)
               .build();
       HttpBody response = userEventServiceClient.collectUserEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CollectUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CollectUserEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### collectUserEventCallable()
    
    
    public final UnaryCallable<CollectUserEventRequest,HttpBody> collectUserEventCallable()

Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain.

This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       CollectUserEventRequest request =
           CollectUserEventRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setUserEvent("userEvent315571599")
               .setUri("uri116076")
               .setEts(100772)
               .build();
       ApiFuture<HttpBody> future =
           userEventServiceClient.collectUserEventCallable().futureCall(request);
       // Do something.
       HttpBody response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CollectUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CollectUserEventRequest),com.google.api.HttpBody>` |   
  
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
    
    
    public final @Nullable UserEventServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1beta.UserEventServiceSettings` |   
  
### getStub()
    
    
    public UserEventServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.stub.UserEventServiceStub)` |   
  
### importUserEventsAsync(ImportUserEventsRequest request)
    
    
    public final OperationFuture<ImportUserEventsResponse,ImportUserEventsMetadata> importUserEventsAsync(ImportUserEventsRequest request)

Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       ImportUserEventsResponse response =
           userEventServiceClient.importUserEventsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsResponse),[ImportUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsMetadata)>` |   
  
### importUserEventsCallable()
    
    
    public final UnaryCallable<ImportUserEventsRequest,Operation> importUserEventsCallable()

Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           userEventServiceClient.importUserEventsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importUserEventsOperationCallable()
    
    
    public final OperationCallable<ImportUserEventsRequest,ImportUserEventsResponse,ImportUserEventsMetadata> importUserEventsOperationCallable()

Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       OperationFuture<ImportUserEventsResponse, ImportUserEventsMetadata> future =
           userEventServiceClient.importUserEventsOperationCallable().futureCall(request);
       // Do something.
       ImportUserEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsRequest),[ImportUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsResponse),[ImportUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ImportUserEventsMetadata)>` |   
  
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
  
### purgeUserEventsAsync(PurgeUserEventsRequest request)
    
    
    public final OperationFuture<PurgeUserEventsResponse,PurgeUserEventsMetadata> purgeUserEventsAsync(PurgeUserEventsRequest request)

Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       PurgeUserEventsRequest request =
           PurgeUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeUserEventsResponse response = userEventServiceClient.purgeUserEventsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsResponse),[PurgeUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsMetadata)>` |   
  
### purgeUserEventsCallable()
    
    
    public final UnaryCallable<PurgeUserEventsRequest,Operation> purgeUserEventsCallable()

Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       PurgeUserEventsRequest request =
           PurgeUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           userEventServiceClient.purgeUserEventsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeUserEventsOperationCallable()
    
    
    public final OperationCallable<PurgeUserEventsRequest,PurgeUserEventsResponse,PurgeUserEventsMetadata> purgeUserEventsOperationCallable()

Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       PurgeUserEventsRequest request =
           PurgeUserEventsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeUserEventsResponse, PurgeUserEventsMetadata> future =
           userEventServiceClient.purgeUserEventsOperationCallable().futureCall(request);
       // Do something.
       PurgeUserEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsRequest),[PurgeUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsResponse),[PurgeUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.PurgeUserEventsMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### writeUserEvent(WriteUserEventRequest request)
    
    
    public final UserEvent writeUserEvent(WriteUserEventRequest request)

Writes a single user event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       WriteUserEventRequest request =
           WriteUserEventRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setUserEvent(UserEvent.newBuilder().build())
               .setWriteAsync(true)
               .build();
       UserEvent response = userEventServiceClient.writeUserEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.WriteUserEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEvent)` |   
  
### writeUserEventCallable()
    
    
    public final UnaryCallable<WriteUserEventRequest,UserEvent> writeUserEventCallable()

Writes a single user event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       WriteUserEventRequest request =
           WriteUserEventRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setUserEvent(UserEvent.newBuilder().build())
               .setWriteAsync(true)
               .build();
       ApiFuture<UserEvent> future =
           userEventServiceClient.writeUserEventCallable().futureCall(request);
       // Do something.
       UserEvent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.WriteUserEventRequest),[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.UserEvent)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
