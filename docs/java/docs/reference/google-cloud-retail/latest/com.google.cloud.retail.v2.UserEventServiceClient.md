---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceClient
title: Class UserEventServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:27.289195+00:00
---

# Class UserEventServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserEventServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/UserEventServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for ingesting end user actions on the customer website.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       WriteUserEventRequest request =
           WriteUserEventRequest.newBuilder()
               .setParent("parent-995424086")
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

  
CollectUserEvent |  Writes a single user event from the browser.  For larger user event payload over 16 KB, the POST method should be used instead, otherwise a 400 Bad Request error is returned.  This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * collectUserEvent(CollectUserEventRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * collectUserEventCallable() 

  
PurgeUserEvents |  Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeUserEventsAsync(PurgeUserEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeUserEventsOperationCallable() 
  * purgeUserEventsCallable() 

  
ImportUserEvents |  Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.  `Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importUserEventsAsync(ImportUserEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importUserEventsOperationCallable() 
  * importUserEventsCallable() 

  
RejoinUserEvents |  Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rejoinUserEventsAsync(RejoinUserEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rejoinUserEventsOperationCallable() 
  * rejoinUserEventsCallable() 

  
  
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
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceClient)` |   
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
`settings` | `[UserEventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceClient)` |   
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
`stub` | `[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.UserEventServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceClient)` |   
  
## Constructors 

### UserEventServiceClient(UserEventServiceSettings settings)
    
    
    protected UserEventServiceClient(UserEventServiceSettings settings)

Constructs an instance of UserEventServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UserEventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEventServiceSettings)`  
  
  
### UserEventServiceClient(UserEventServiceStub stub)
    
    
    protected UserEventServiceClient(UserEventServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.UserEventServiceStub)`  
  
  
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

Writes a single user event from the browser.

For larger user event payload over 16 KB, the POST method should be used instead, otherwise a 400 Bad Request error is returned.

This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       CollectUserEventRequest request =
           CollectUserEventRequest.newBuilder()
               .setParent("parent-995424086")
               .setUserEvent("userEvent315571599")
               .setUri("uri116076")
               .setEts(100772)
               .setRawJson("rawJson985449776")
               .build();
       HttpBody response = userEventServiceClient.collectUserEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CollectUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CollectUserEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### collectUserEventCallable()
    
    
    public final UnaryCallable<CollectUserEventRequest,HttpBody> collectUserEventCallable()

Writes a single user event from the browser.

For larger user event payload over 16 KB, the POST method should be used instead, otherwise a 400 Bad Request error is returned.

This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       CollectUserEventRequest request =
           CollectUserEventRequest.newBuilder()
               .setParent("parent-995424086")
               .setUserEvent("userEvent315571599")
               .setUri("uri116076")
               .setEts(100772)
               .setRawJson("rawJson985449776")
               .build();
       ApiFuture<HttpBody> future =
           userEventServiceClient.collectUserEventCallable().futureCall(request);
       // Do something.
       HttpBody response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CollectUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CollectUserEventRequest),com.google.api.HttpBody>` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.UserEventServiceSettings` |   
  
### getStub()
    
    
    public UserEventServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.UserEventServiceStub)` |   
  
### importUserEventsAsync(ImportUserEventsRequest request)
    
    
    public final OperationFuture<ImportUserEventsResponse,ImportMetadata> importUserEventsAsync(ImportUserEventsRequest request)

Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

`Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(UserEventInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .build();
       ImportUserEventsResponse response =
           userEventServiceClient.importUserEventsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportUserEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportUserEventsResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportMetadata)>` |   
  
### importUserEventsCallable()
    
    
    public final UnaryCallable<ImportUserEventsRequest,Operation> importUserEventsCallable()

Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

`Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(UserEventInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           userEventServiceClient.importUserEventsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportUserEventsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importUserEventsOperationCallable()
    
    
    public final OperationCallable<ImportUserEventsRequest,ImportUserEventsResponse,ImportMetadata> importUserEventsOperationCallable()

Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

`Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       ImportUserEventsRequest request =
           ImportUserEventsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(UserEventInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .build();
       OperationFuture<ImportUserEventsResponse, ImportMetadata> future =
           userEventServiceClient.importUserEventsOperationCallable().futureCall(request);
       // Do something.
       ImportUserEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportUserEventsRequest),[ImportUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportUserEventsResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportMetadata)>` |   
  
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
    
    
    public final OperationFuture<PurgeUserEventsResponse,PurgeMetadata> purgeUserEventsAsync(PurgeUserEventsRequest request)

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
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeUserEventsResponse response = userEventServiceClient.purgeUserEventsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeUserEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeUserEventsResponse),[PurgeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeMetadata)>` |   
  
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
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeUserEventsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeUserEventsOperationCallable()
    
    
    public final OperationCallable<PurgeUserEventsRequest,PurgeUserEventsResponse,PurgeMetadata> purgeUserEventsOperationCallable()

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
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeUserEventsResponse, PurgeMetadata> future =
           userEventServiceClient.purgeUserEventsOperationCallable().futureCall(request);
       // Do something.
       PurgeUserEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeUserEventsRequest),[PurgeUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeUserEventsResponse),[PurgeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeMetadata)>` |   
  
### rejoinUserEventsAsync(RejoinUserEventsRequest request)
    
    
    public final OperationFuture<RejoinUserEventsResponse,RejoinUserEventsMetadata> rejoinUserEventsAsync(RejoinUserEventsRequest request)

Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       RejoinUserEventsRequest request =
           RejoinUserEventsRequest.newBuilder().setParent("parent-995424086").build();
       RejoinUserEventsResponse response =
           userEventServiceClient.rejoinUserEventsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RejoinUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RejoinUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsResponse),[RejoinUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsMetadata)>` |   
  
### rejoinUserEventsCallable()
    
    
    public final UnaryCallable<RejoinUserEventsRequest,Operation> rejoinUserEventsCallable()

Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       RejoinUserEventsRequest request =
           RejoinUserEventsRequest.newBuilder().setParent("parent-995424086").build();
       ApiFuture<Operation> future =
           userEventServiceClient.rejoinUserEventsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RejoinUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejoinUserEventsOperationCallable()
    
    
    public final OperationCallable<RejoinUserEventsRequest,RejoinUserEventsResponse,RejoinUserEventsMetadata> rejoinUserEventsOperationCallable()

Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
       RejoinUserEventsRequest request =
           RejoinUserEventsRequest.newBuilder().setParent("parent-995424086").build();
       OperationFuture<RejoinUserEventsResponse, RejoinUserEventsMetadata> future =
           userEventServiceClient.rejoinUserEventsOperationCallable().futureCall(request);
       // Do something.
       RejoinUserEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RejoinUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsRequest),[RejoinUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsResponse),[RejoinUserEventsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RejoinUserEventsMetadata)>` |   
  
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
               .setParent("parent-995424086")
               .setUserEvent(UserEvent.newBuilder().build())
               .setWriteAsync(true)
               .build();
       UserEvent response = userEventServiceClient.writeUserEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.WriteUserEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEvent)` |   
  
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
               .setParent("parent-995424086")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.WriteUserEventRequest),[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UserEvent)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
