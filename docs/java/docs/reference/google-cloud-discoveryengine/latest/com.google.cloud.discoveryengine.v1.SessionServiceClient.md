---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient
title: Class SessionServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:48.371600+00:00
---

# Class SessionServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/SessionServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing Sessions and Session-related resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Session session = Session.newBuilder().build();
       Session response = sessionServiceClient.createSession(parent, session);
     }
     

Note: close() needs to be called on the SessionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSession |  Creates a Session.  If the Session to create already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSession(CreateSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSession(DataStoreName parent, Session session) 
  * createSession(String parent, Session session) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSessionCallable() 

  
DeleteSession |  Deletes a Session.  If the Session to delete does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSession(DeleteSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSession(SessionName name) 
  * deleteSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSessionCallable() 

  
UpdateSession |  Updates a Session.  Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSession(UpdateSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSession(Session session, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSessionCallable() 

  
GetSession |  Gets a Session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSession(GetSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSession(SessionName name) 
  * getSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSessionCallable() 

  
ListSessions |  Lists all Sessions by their parent DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSessions(ListSessionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSessions(DataStoreName parent) 
  * listSessions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSessionsPagedCallable() 
  * listSessionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SessionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionServiceSettings sessionServiceSettings =
         SessionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SessionServiceClient sessionServiceClient = SessionServiceClient.create(sessionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionServiceSettings sessionServiceSettings =
         SessionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SessionServiceClient sessionServiceClient = SessionServiceClient.create(sessionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionServiceSettings sessionServiceSettings =
         SessionServiceSettings.newHttpJsonBuilder().build();
     SessionServiceClient sessionServiceClient = SessionServiceClient.create(sessionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SessionServiceClient

## Static Methods 

### create()
    
    
    public static final SessionServiceClient create()

Constructs an instance of SessionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionServiceSettings settings)
    
    
    public static final SessionServiceClient create(SessionServiceSettings settings)

Constructs an instance of SessionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionServiceStub stub)
    
    
    public static final SessionServiceClient create(SessionServiceStub stub)

Constructs an instance of SessionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SessionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SessionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient)` |   
  
## Constructors 

### SessionServiceClient(SessionServiceSettings settings)
    
    
    protected SessionServiceClient(SessionServiceSettings settings)

Constructs an instance of SessionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceSettings)`  
  
  
### SessionServiceClient(SessionServiceStub stub)
    
    
    protected SessionServiceClient(SessionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SessionServiceStub)`  
  
  
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

### createSession(@Nullable DataStoreName parent, Session session)
    
    
    public final Session createSession(@Nullable DataStoreName parent, Session session)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Session session = Session.newBuilder().build();
       Session response = sessionServiceClient.createSession(parent, session);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The session to create.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSession(CreateSessionRequest request)
    
    
    public final Session createSession(CreateSessionRequest request)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       CreateSessionRequest request =
           CreateSessionRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSession(Session.newBuilder().build())
               .build();
       Session response = sessionServiceClient.createSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSession(String parent, Session session)
    
    
    public final Session createSession(String parent, Session session)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       Session session = Session.newBuilder().build();
       Session response = sessionServiceClient.createSession(parent, session);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The session to create.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSessionCallable()
    
    
    public final UnaryCallable<CreateSessionRequest,Session> createSessionCallable()

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       CreateSessionRequest request =
           CreateSessionRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSession(Session.newBuilder().build())
               .build();
       ApiFuture<Session> future = sessionServiceClient.createSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
### deleteSession(@Nullable SessionName name)
    
    
    public final void deleteSession(@Nullable SessionName name)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       SessionName name =
           SessionName.ofProjectLocationDataStoreSessionName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]");
       sessionServiceClient.deleteSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SessionName`  
Required. The resource name of the Session to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
  
### deleteSession(DeleteSessionRequest request)
    
    
    public final void deleteSession(DeleteSessionRequest request)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       DeleteSessionRequest request =
           DeleteSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .build();
       sessionServiceClient.deleteSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSessionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSession(String name)
    
    
    public final void deleteSession(String name)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       String name =
           SessionName.ofProjectLocationDataStoreSessionName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
               .toString();
       sessionServiceClient.deleteSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Session to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
  
### deleteSessionCallable()
    
    
    public final UnaryCallable<DeleteSessionRequest,Empty> deleteSessionCallable()

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       DeleteSessionRequest request =
           DeleteSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .build();
       ApiFuture<Empty> future = sessionServiceClient.deleteSessionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSessionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSession(@Nullable SessionName name)
    
    
    public final Session getSession(@Nullable SessionName name)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       SessionName name =
           SessionName.ofProjectLocationDataStoreSessionName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]");
       Session response = sessionServiceClient.getSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SessionName`  
Required. The resource name of the Session to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSession(GetSessionRequest request)
    
    
    public final Session getSession(GetSessionRequest request)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       GetSessionRequest request =
           GetSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setIncludeAnswerDetails(true)
               .build();
       Session response = sessionServiceClient.getSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSession(String name)
    
    
    public final Session getSession(String name)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       String name =
           SessionName.ofProjectLocationDataStoreSessionName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
               .toString();
       Session response = sessionServiceClient.getSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Session to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSessionCallable()
    
    
    public final UnaryCallable<GetSessionRequest,Session> getSessionCallable()

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       GetSessionRequest request =
           GetSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setIncludeAnswerDetails(true)
               .build();
       ApiFuture<Session> future = sessionServiceClient.getSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
### getSettings()
    
    
    public final @Nullable SessionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SessionServiceSettings` |   
  
### getStub()
    
    
    public SessionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SessionServiceStub)` |   
  
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
  
### listSessions(@Nullable DataStoreName parent)
    
    
    public final SessionServiceClient.ListSessionsPagedResponse listSessions(@Nullable DataStoreName parent)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       for (Session element : sessionServiceClient.listSessions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient.ListSessionsPagedResponse)` |   
  
### listSessions(ListSessionsRequest request)
    
    
    public final SessionServiceClient.ListSessionsPagedResponse listSessions(ListSessionsRequest request)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Session element : sessionServiceClient.listSessions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient.ListSessionsPagedResponse)` |   
  
### listSessions(String parent)
    
    
    public final SessionServiceClient.ListSessionsPagedResponse listSessions(String parent)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       for (Session element : sessionServiceClient.listSessions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient.ListSessionsPagedResponse)` |   
  
### listSessionsCallable()
    
    
    public final UnaryCallable<ListSessionsRequest,ListSessionsResponse> listSessionsCallable()

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSessionsResponse response = sessionServiceClient.listSessionsCallable().call(request);
         for (Session element : response.getSessionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest),[ListSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsResponse)>` |   
  
### listSessionsPagedCallable()
    
    
    public final UnaryCallable<ListSessionsRequest,SessionServiceClient.ListSessionsPagedResponse> listSessionsPagedCallable()

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Session> future =
           sessionServiceClient.listSessionsPagedCallable().futureCall(request);
       // Do something.
       for (Session element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest),[ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SessionServiceClient.ListSessionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSession(Session session, FieldMask updateMask)
    
    
    public final Session updateSession(Session session, FieldMask updateMask)

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       Session session = Session.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Session response = sessionServiceClient.updateSession(session, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The Session to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Session to update. The following are NOT supported: 

  * Session.name

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### updateSession(UpdateSessionRequest request)
    
    
    public final Session updateSession(UpdateSessionRequest request)

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       UpdateSessionRequest request =
           UpdateSessionRequest.newBuilder()
               .setSession(Session.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Session response = sessionServiceClient.updateSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### updateSessionCallable()
    
    
    public final UnaryCallable<UpdateSessionRequest,Session> updateSessionCallable()

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       UpdateSessionRequest request =
           UpdateSessionRequest.newBuilder()
               .setSession(Session.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Session> future = sessionServiceClient.updateSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
