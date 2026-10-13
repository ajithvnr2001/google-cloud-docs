---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient
title: Class DataSubscriptionServiceClient (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:58.394757+00:00
---

# Class DataSubscriptionServiceClient (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataSubscriptionServiceClient (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-health/google-cloud-health/src/main/java/com/google/devicesandservices/health/v4/DataSubscriptionServiceClient.java)| [Product Reference](https://developers.google.com/health/api)| [RPC Documentation](https://developers.google.com/health/api/reference/rpc)  
---|---|---  
  
Service Description: Data Subscription Service that allows clients (e.g., Fitbit 3P applications, internal Fitbit Services) to manage their subscriber endpoints. This service provides CRUD APIs for subscribers, and also offers functionalities for subscriber verification and statistics.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       SubscriberName parent = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]");
       CreateSubscriptionPayload subscription = CreateSubscriptionPayload.newBuilder().build();
       String subscriptionId = "subscriptionId1478790936";
       Subscription response =
           dataSubscriptionServiceClient.createSubscription(parent, subscription, subscriptionId);
     }
     

Note: close() needs to be called on the DataSubscriptionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSubscriber |  Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.  **Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:  1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.  2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.  Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSubscriberAsync(CreateSubscriberRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSubscriberAsync(ProjectName parent, CreateSubscriberPayload subscriber, String subscriberId) 
  * createSubscriberAsync(String parent, CreateSubscriberPayload subscriber, String subscriberId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSubscriberOperationCallable() 
  * createSubscriberCallable() 

  
ListSubscribers |  Lists all subscribers registered within the owned Google Cloud Project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubscribers(ListSubscribersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSubscribers(ProjectName parent) 
  * listSubscribers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubscribersPagedCallable() 
  * listSubscribersCallable() 

  
UpdateSubscriber |  Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in.  **Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:  1\. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`. 2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`.  Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSubscriberAsync(UpdateSubscriberRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSubscriberAsync(Subscriber subscriber, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSubscriberOperationCallable() 
  * updateSubscriberCallable() 

  
DeleteSubscriber |  Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSubscriberAsync(DeleteSubscriberRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSubscriberAsync(SubscriberName name) 
  * deleteSubscriberAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSubscriberOperationCallable() 
  * deleteSubscriberCallable() 

  
CreateSubscription |  Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSubscription(CreateSubscriptionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSubscription(SubscriberName parent, CreateSubscriptionPayload subscription, String subscriptionId) 
  * createSubscription(String parent, CreateSubscriptionPayload subscription, String subscriptionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSubscriptionCallable() 

  
ListSubscriptions |  Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubscriptions(ListSubscriptionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSubscriptions(SubscriberName parent) 
  * listSubscriptions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubscriptionsPagedCallable() 
  * listSubscriptionsCallable() 

  
UpdateSubscription |  Updates the data types for an existing user subscription. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSubscription(UpdateSubscriptionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSubscription(Subscription subscription, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSubscriptionCallable() 

  
DeleteSubscription |  Deletes a specific user subscription, stopping notifications for this user to this subscriber. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSubscription(DeleteSubscriptionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSubscription(SubscriptionName name) 
  * deleteSubscription(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSubscriptionCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataSubscriptionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSubscriptionServiceSettings dataSubscriptionServiceSettings =
         DataSubscriptionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create(dataSubscriptionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSubscriptionServiceSettings dataSubscriptionServiceSettings =
         DataSubscriptionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create(dataSubscriptionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSubscriptionServiceSettings dataSubscriptionServiceSettings =
         DataSubscriptionServiceSettings.newHttpJsonBuilder().build();
     DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create(dataSubscriptionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataSubscriptionServiceClient

## Static Methods 

### create()
    
    
    public static final DataSubscriptionServiceClient create()

Constructs an instance of DataSubscriptionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataSubscriptionServiceSettings settings)
    
    
    public static final DataSubscriptionServiceClient create(DataSubscriptionServiceSettings settings)

Constructs an instance of DataSubscriptionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataSubscriptionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataSubscriptionServiceStub stub)
    
    
    public static final DataSubscriptionServiceClient create(DataSubscriptionServiceStub stub)

Constructs an instance of DataSubscriptionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataSubscriptionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataSubscriptionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataSubscriptionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient)` |   
  
## Constructors 

### DataSubscriptionServiceClient(DataSubscriptionServiceSettings settings)
    
    
    protected DataSubscriptionServiceClient(DataSubscriptionServiceSettings settings)

Constructs an instance of DataSubscriptionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataSubscriptionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceSettings)`  
  
  
### DataSubscriptionServiceClient(DataSubscriptionServiceStub stub)
    
    
    protected DataSubscriptionServiceClient(DataSubscriptionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataSubscriptionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataSubscriptionServiceStub)`  
  
  
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

### createSubscriberAsync(@Nullable ProjectName parent, CreateSubscriberPayload subscriber, String subscriberId)
    
    
    public final OperationFuture<Subscriber,CreateSubscriberMetadata> createSubscriberAsync(@Nullable ProjectName parent, CreateSubscriberPayload subscriber, String subscriberId)

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.

**Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.

2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       CreateSubscriberPayload subscriber = CreateSubscriberPayload.newBuilder().build();
       String subscriberId = "subscriberId327834531";
       Subscriber response =
           dataSubscriptionServiceClient
               .createSubscriberAsync(parent, subscriber, subscriberId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.ProjectName`  
Required. The parent resource where this subscriber will be created. Format: projects/{project_number} Example: projects/1234567890  
`subscriber` | `[CreateSubscriberPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberPayload)`  
Required. The subscriber to create.  
`subscriberId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the subscriber, which will become the final component of the subscriber's resource name. This value should be 4-36 characters, and valid characters are /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[CreateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberMetadata)>` |   
  
### createSubscriberAsync(CreateSubscriberRequest request)
    
    
    public final OperationFuture<Subscriber,CreateSubscriberMetadata> createSubscriberAsync(CreateSubscriberRequest request)

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.

**Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.

2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       CreateSubscriberRequest request =
           CreateSubscriberRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setSubscriber(CreateSubscriberPayload.newBuilder().build())
               .setSubscriberId("subscriberId327834531")
               .build();
       Subscriber response = dataSubscriptionServiceClient.createSubscriberAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[CreateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberMetadata)>` |   
  
### createSubscriberAsync(String parent, CreateSubscriberPayload subscriber, String subscriberId)
    
    
    public final OperationFuture<Subscriber,CreateSubscriberMetadata> createSubscriberAsync(String parent, CreateSubscriberPayload subscriber, String subscriberId)

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.

**Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.

2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       CreateSubscriberPayload subscriber = CreateSubscriberPayload.newBuilder().build();
       String subscriberId = "subscriberId327834531";
       Subscriber response =
           dataSubscriptionServiceClient
               .createSubscriberAsync(parent, subscriber, subscriberId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this subscriber will be created. Format: projects/{project_number} Example: projects/1234567890  
`subscriber` | `[CreateSubscriberPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberPayload)`  
Required. The subscriber to create.  
`subscriberId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the subscriber, which will become the final component of the subscriber's resource name. This value should be 4-36 characters, and valid characters are /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[CreateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberMetadata)>` |   
  
### createSubscriberCallable()
    
    
    public final UnaryCallable<CreateSubscriberRequest,Operation> createSubscriberCallable()

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.

**Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.

2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       CreateSubscriberRequest request =
           CreateSubscriberRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setSubscriber(CreateSubscriberPayload.newBuilder().build())
               .setSubscriberId("subscriberId327834531")
               .build();
       ApiFuture<Operation> future =
           dataSubscriptionServiceClient.createSubscriberCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSubscriberOperationCallable()
    
    
    public final OperationCallable<CreateSubscriberRequest,Subscriber,CreateSubscriberMetadata> createSubscriberOperationCallable()

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent.

**Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

1\. **Verification with Authorization:** * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`). * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `201 Created`.

2\. **Verification without Authorization:** * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED. * **Body:** `{"type": "verification"}` * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       CreateSubscriberRequest request =
           CreateSubscriberRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setSubscriber(CreateSubscriberPayload.newBuilder().build())
               .setSubscriberId("subscriberId327834531")
               .build();
       OperationFuture<Subscriber, CreateSubscriberMetadata> future =
           dataSubscriptionServiceClient.createSubscriberOperationCallable().futureCall(request);
       // Do something.
       Subscriber response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest),[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[CreateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberMetadata)>` |   
  
### createSubscription(@Nullable SubscriberName parent, CreateSubscriptionPayload subscription, String subscriptionId)
    
    
    public final Subscription createSubscription(@Nullable SubscriberName parent, CreateSubscriptionPayload subscription, String subscriptionId)

Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       SubscriberName parent = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]");
       CreateSubscriptionPayload subscription = CreateSubscriptionPayload.newBuilder().build();
       String subscriptionId = "subscriptionId1478790936";
       Subscription response =
           dataSubscriptionServiceClient.createSubscription(parent, subscription, subscriptionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.SubscriberName`  
Required. The parent subscriber. Format: projects/{project}/subscribers/{subscriber} The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise.  
`subscription` | `[CreateSubscriptionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionPayload)`  
Required. The subscription to create.  
`subscriptionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The {subscription_id} is user-settable (4-36 chars, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated otherwise. If provided, the ID must be unique within the parent subscriber.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)` |   
  
### createSubscription(CreateSubscriptionRequest request)
    
    
    public final Subscription createSubscription(CreateSubscriptionRequest request)

Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       CreateSubscriptionRequest request =
           CreateSubscriptionRequest.newBuilder()
               .setParent(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setSubscriptionId("subscriptionId1478790936")
               .setSubscription(CreateSubscriptionPayload.newBuilder().build())
               .build();
       Subscription response = dataSubscriptionServiceClient.createSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)` |   
  
### createSubscription(String parent, CreateSubscriptionPayload subscription, String subscriptionId)
    
    
    public final Subscription createSubscription(String parent, CreateSubscriptionPayload subscription, String subscriptionId)

Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String parent = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString();
       CreateSubscriptionPayload subscription = CreateSubscriptionPayload.newBuilder().build();
       String subscriptionId = "subscriptionId1478790936";
       Subscription response =
           dataSubscriptionServiceClient.createSubscription(parent, subscription, subscriptionId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent subscriber. Format: projects/{project}/subscribers/{subscriber} The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise.  
`subscription` | `[CreateSubscriptionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionPayload)`  
Required. The subscription to create.  
`subscriptionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The {subscription_id} is user-settable (4-36 chars, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated otherwise. If provided, the ID must be unique within the parent subscriber.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)` |   
  
### createSubscriptionCallable()
    
    
    public final UnaryCallable<CreateSubscriptionRequest,Subscription> createSubscriptionCallable()

Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       CreateSubscriptionRequest request =
           CreateSubscriptionRequest.newBuilder()
               .setParent(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setSubscriptionId("subscriptionId1478790936")
               .setSubscription(CreateSubscriptionPayload.newBuilder().build())
               .build();
       ApiFuture<Subscription> future =
           dataSubscriptionServiceClient.createSubscriptionCallable().futureCall(request);
       // Do something.
       Subscription response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>` |   
  
### deleteSubscriberAsync(@Nullable SubscriberName name)
    
    
    public final OperationFuture<Empty,DeleteSubscriberMetadata> deleteSubscriberAsync(@Nullable SubscriberName name)

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       SubscriberName name = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]");
       dataSubscriptionServiceClient.deleteSubscriberAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.SubscriberName`  
Required. The name of the subscriber to delete. Format: projects/{project}/subscribers/{subscriber} Example: projects/my-project/subscribers/my-subscriber-123 The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated if not provided during creation.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberMetadata)>` |   
  
### deleteSubscriberAsync(DeleteSubscriberRequest request)
    
    
    public final OperationFuture<Empty,DeleteSubscriberMetadata> deleteSubscriberAsync(DeleteSubscriberRequest request)

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       DeleteSubscriberRequest request =
           DeleteSubscriberRequest.newBuilder()
               .setName(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setForce(true)
               .build();
       dataSubscriptionServiceClient.deleteSubscriberAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberMetadata)>` |   
  
### deleteSubscriberAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteSubscriberMetadata> deleteSubscriberAsync(String name)

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String name = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString();
       dataSubscriptionServiceClient.deleteSubscriberAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the subscriber to delete. Format: projects/{project}/subscribers/{subscriber} Example: projects/my-project/subscribers/my-subscriber-123 The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated if not provided during creation.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberMetadata)>` |   
  
### deleteSubscriberCallable()
    
    
    public final UnaryCallable<DeleteSubscriberRequest,Operation> deleteSubscriberCallable()

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       DeleteSubscriberRequest request =
           DeleteSubscriberRequest.newBuilder()
               .setName(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataSubscriptionServiceClient.deleteSubscriberCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSubscriberOperationCallable()
    
    
    public final OperationCallable<DeleteSubscriberRequest,Empty,DeleteSubscriberMetadata> deleteSubscriberOperationCallable()

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       DeleteSubscriberRequest request =
           DeleteSubscriberRequest.newBuilder()
               .setName(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteSubscriberMetadata> future =
           dataSubscriptionServiceClient.deleteSubscriberOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberMetadata)>` |   
  
### deleteSubscription(@Nullable SubscriptionName name)
    
    
    public final void deleteSubscription(@Nullable SubscriptionName name)

Deletes a specific user subscription, stopping notifications for this user to this subscriber.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       SubscriptionName name = SubscriptionName.of("[PROJECT]", "[SUBSCRIBER]", "[SUBSCRIPTION]");
       dataSubscriptionServiceClient.deleteSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.SubscriptionName`  
Required. The resource name of the subscription to delete. Format: `projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}` Example: `projects/my-project/subscribers/my-subscriber-123/subscriptions/my-subscription-456` The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise. The {subscription} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated if not provided during creation.  
  
### deleteSubscription(DeleteSubscriptionRequest request)
    
    
    public final void deleteSubscription(DeleteSubscriptionRequest request)

Deletes a specific user subscription, stopping notifications for this user to this subscriber.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       DeleteSubscriptionRequest request =
           DeleteSubscriptionRequest.newBuilder()
               .setName(
                   SubscriptionName.of("[PROJECT]", "[SUBSCRIBER]", "[SUBSCRIPTION]").toString())
               .build();
       dataSubscriptionServiceClient.deleteSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSubscription(String name)
    
    
    public final void deleteSubscription(String name)

Deletes a specific user subscription, stopping notifications for this user to this subscriber.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String name = SubscriptionName.of("[PROJECT]", "[SUBSCRIBER]", "[SUBSCRIPTION]").toString();
       dataSubscriptionServiceClient.deleteSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the subscription to delete. Format: `projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}` Example: `projects/my-project/subscribers/my-subscriber-123/subscriptions/my-subscription-456` The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise. The {subscription} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) or system-generated if not provided during creation.  
  
### deleteSubscriptionCallable()
    
    
    public final UnaryCallable<DeleteSubscriptionRequest,Empty> deleteSubscriptionCallable()

Deletes a specific user subscription, stopping notifications for this user to this subscriber.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       DeleteSubscriptionRequest request =
           DeleteSubscriptionRequest.newBuilder()
               .setName(
                   SubscriptionName.of("[PROJECT]", "[SUBSCRIBER]", "[SUBSCRIPTION]").toString())
               .build();
       ApiFuture<Empty> future =
           dataSubscriptionServiceClient.deleteSubscriptionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriptionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
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
    
    
    public final @Nullable DataSubscriptionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataSubscriptionServiceSettings` |   
  
### getStub()
    
    
    public DataSubscriptionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataSubscriptionServiceStub)` |   
  
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
  
### listSubscribers(@Nullable ProjectName parent)
    
    
    public final DataSubscriptionServiceClient.ListSubscribersPagedResponse listSubscribers(@Nullable ProjectName parent)

Lists all subscribers registered within the owned Google Cloud Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Subscriber element :
           dataSubscriptionServiceClient.listSubscribers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.ProjectName`  
Required. The parent, which owns this collection of subscribers. Format: projects/{project}  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscribersPagedResponse)` |   
  
### listSubscribers(ListSubscribersRequest request)
    
    
    public final DataSubscriptionServiceClient.ListSubscribersPagedResponse listSubscribers(ListSubscribersRequest request)

Lists all subscribers registered within the owned Google Cloud Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Subscriber element :
           dataSubscriptionServiceClient.listSubscribers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscribersPagedResponse)` |   
  
### listSubscribers(String parent)
    
    
    public final DataSubscriptionServiceClient.ListSubscribersPagedResponse listSubscribers(String parent)

Lists all subscribers registered within the owned Google Cloud Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (Subscriber element :
           dataSubscriptionServiceClient.listSubscribers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of subscribers. Format: projects/{project}  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscribersPagedResponse)` |   
  
### listSubscribersCallable()
    
    
    public final UnaryCallable<ListSubscribersRequest,ListSubscribersResponse> listSubscribersCallable()

Lists all subscribers registered within the owned Google Cloud Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSubscribersResponse response =
             dataSubscriptionServiceClient.listSubscribersCallable().call(request);
         for (Subscriber element : response.getSubscribersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest),[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersResponse)>` |   
  
### listSubscribersPagedCallable()
    
    
    public final UnaryCallable<ListSubscribersRequest,DataSubscriptionServiceClient.ListSubscribersPagedResponse> listSubscribersPagedCallable()

Lists all subscribers registered within the owned Google Cloud Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscribersRequest request =
           ListSubscribersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Subscriber> future =
           dataSubscriptionServiceClient.listSubscribersPagedCallable().futureCall(request);
       // Do something.
       for (Subscriber element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest),[ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscribersPagedResponse)>` |   
  
### listSubscriptions(@Nullable SubscriberName parent)
    
    
    public final DataSubscriptionServiceClient.ListSubscriptionsPagedResponse listSubscriptions(@Nullable SubscriberName parent)

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       SubscriberName parent = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]");
       for (Subscription element :
           dataSubscriptionServiceClient.listSubscriptions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.SubscriberName`  
Required. The parent subscriber. Format: projects/{project}/subscribers/{subscriber} The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise.  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptions(ListSubscriptionsRequest request)
    
    
    public final DataSubscriptionServiceClient.ListSubscriptionsPagedResponse listSubscriptions(ListSubscriptionsRequest request)

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Subscription element :
           dataSubscriptionServiceClient.listSubscriptions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptions(String parent)
    
    
    public final DataSubscriptionServiceClient.ListSubscriptionsPagedResponse listSubscriptions(String parent)

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       String parent = SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString();
       for (Subscription element :
           dataSubscriptionServiceClient.listSubscriptions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent subscriber. Format: projects/{project}/subscribers/{subscriber} The {subscriber} ID is user-settable (4-36 characters, matching /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/) if provided during creation, or system-generated otherwise.  
**Returns**  
---  
**Type** | **Description**  
`[DataSubscriptionServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptionsCallable()
    
    
    public final UnaryCallable<ListSubscriptionsRequest,ListSubscriptionsResponse> listSubscriptionsCallable()

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSubscriptionsResponse response =
             dataSubscriptionServiceClient.listSubscriptionsCallable().call(request);
         for (Subscription element : response.getSubscriptionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest),[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsResponse)>` |   
  
### listSubscriptionsPagedCallable()
    
    
    public final UnaryCallable<ListSubscriptionsRequest,DataSubscriptionServiceClient.ListSubscriptionsPagedResponse> listSubscriptionsPagedCallable()

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(SubscriberName.of("[PROJECT]", "[SUBSCRIBER]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Subscription> future =
           dataSubscriptionServiceClient.listSubscriptionsPagedCallable().futureCall(request);
       // Do something.
       for (Subscription element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest),[ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscriptionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSubscriberAsync(Subscriber subscriber, FieldMask updateMask)
    
    
    public final OperationFuture<Subscriber,UpdateSubscriberMetadata> updateSubscriberAsync(Subscriber subscriber, FieldMask updateMask)

Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in.

**Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:

1\. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`. 2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       Subscriber subscriber = Subscriber.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Subscriber response =
           dataSubscriptionServiceClient.updateSubscriberAsync(subscriber, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`subscriber` | `[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber)`  
Required. The subscriber resource to update. Its 'name' field is mapped to the URI, and the value of the 'name' field should be of the form: "projects/{project}/subscribers/{subscriber_id}". The remaining fields of the Subscriber object represent the new values for the corresponding fields in the existing subscriber resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A field mask that specifies which fields of the Subscriber message are to be updated. This allows for partial updates. Supported fields: - endpoint_uri - subscriber_configs - endpoint_authorization  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[UpdateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberMetadata)>` |   
  
### updateSubscriberAsync(UpdateSubscriberRequest request)
    
    
    public final OperationFuture<Subscriber,UpdateSubscriberMetadata> updateSubscriberAsync(UpdateSubscriberRequest request)

Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in.

**Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:

1\. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`. 2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       UpdateSubscriberRequest request =
           UpdateSubscriberRequest.newBuilder()
               .setSubscriber(Subscriber.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Subscriber response = dataSubscriptionServiceClient.updateSubscriberAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[UpdateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberMetadata)>` |   
  
### updateSubscriberCallable()
    
    
    public final UnaryCallable<UpdateSubscriberRequest,Operation> updateSubscriberCallable()

Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in.

**Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:

1\. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`. 2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       UpdateSubscriberRequest request =
           UpdateSubscriberRequest.newBuilder()
               .setSubscriber(Subscriber.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           dataSubscriptionServiceClient.updateSubscriberCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubscriberOperationCallable()
    
    
    public final OperationCallable<UpdateSubscriberRequest,Subscriber,UpdateSubscriberMetadata> updateSubscriberOperationCallable()

Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in.

**Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:

1\. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`. 2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`.

Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       UpdateSubscriberRequest request =
           UpdateSubscriberRequest.newBuilder()
               .setSubscriber(Subscriber.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Subscriber, UpdateSubscriberMetadata> future =
           dataSubscriptionServiceClient.updateSubscriberOperationCallable().futureCall(request);
       // Do something.
       Subscriber response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest),[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[UpdateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberMetadata)>` |   
  
### updateSubscription(Subscription subscription, FieldMask updateMask)
    
    
    public final Subscription updateSubscription(Subscription subscription, FieldMask updateMask)

Updates the data types for an existing user subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       Subscription subscription = Subscription.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Subscription response =
           dataSubscriptionServiceClient.updateSubscription(subscription, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)`  
Required. The subscription to update. The subscription's `name` field is used to identify the subscription to update. Format: projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)` |   
  
### updateSubscription(UpdateSubscriptionRequest request)
    
    
    public final Subscription updateSubscription(UpdateSubscriptionRequest request)

Updates the data types for an existing user subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       UpdateSubscriptionRequest request =
           UpdateSubscriptionRequest.newBuilder()
               .setSubscription(Subscription.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Subscription response = dataSubscriptionServiceClient.updateSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)` |   
  
### updateSubscriptionCallable()
    
    
    public final UnaryCallable<UpdateSubscriptionRequest,Subscription> updateSubscriptionCallable()

Updates the data types for an existing user subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSubscriptionServiceClient dataSubscriptionServiceClient =
         DataSubscriptionServiceClient.create()) {
       UpdateSubscriptionRequest request =
           UpdateSubscriptionRequest.newBuilder()
               .setSubscription(Subscription.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Subscription> future =
           dataSubscriptionServiceClient.updateSubscriptionCallable().futureCall(request);
       // Do something.
       Subscription response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
