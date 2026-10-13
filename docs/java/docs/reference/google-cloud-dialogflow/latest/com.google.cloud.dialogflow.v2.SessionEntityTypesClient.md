---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient
title: Class SessionEntityTypesClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:45.409470+00:00
---

# Class SessionEntityTypesClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionEntityTypesClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/SessionEntityTypesClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing SessionEntityTypes.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionEntityTypeName name =
           SessionEntityTypeName.ofProjectSessionEntityTypeName(
               "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]");
       SessionEntityType response = sessionEntityTypesClient.getSessionEntityType(name);
     }
     

Note: close() needs to be called on the SessionEntityTypesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListSessionEntityTypes |  Returns the list of all session entity types in the specified session.  This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSessionEntityTypes(ListSessionEntityTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSessionEntityTypes(SessionName parent) 
  * listSessionEntityTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSessionEntityTypesPagedCallable() 
  * listSessionEntityTypesCallable() 

  
GetSessionEntityType |  Retrieves the specified session entity type.  This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSessionEntityType(GetSessionEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSessionEntityType(SessionEntityTypeName name) 
  * getSessionEntityType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSessionEntityTypeCallable() 

  
CreateSessionEntityType |  Creates a session entity type.  If the specified session entity type already exists, overrides the session entity type.  This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSessionEntityType(CreateSessionEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSessionEntityType(SessionName parent, SessionEntityType sessionEntityType) 
  * createSessionEntityType(String parent, SessionEntityType sessionEntityType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSessionEntityTypeCallable() 

  
UpdateSessionEntityType |  Updates the specified session entity type.  This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSessionEntityType(UpdateSessionEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSessionEntityType(SessionEntityType sessionEntityType) 
  * updateSessionEntityType(SessionEntityType sessionEntityType, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSessionEntityTypeCallable() 

  
DeleteSessionEntityType |  Deletes the specified session entity type.  This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSessionEntityType(DeleteSessionEntityTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSessionEntityType(SessionEntityTypeName name) 
  * deleteSessionEntityType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSessionEntityTypeCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SessionEntityTypesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionEntityTypesSettings sessionEntityTypesSettings =
         SessionEntityTypesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SessionEntityTypesClient sessionEntityTypesClient =
         SessionEntityTypesClient.create(sessionEntityTypesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionEntityTypesSettings sessionEntityTypesSettings =
         SessionEntityTypesSettings.newBuilder().setEndpoint(myEndpoint).build();
     SessionEntityTypesClient sessionEntityTypesClient =
         SessionEntityTypesClient.create(sessionEntityTypesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionEntityTypesSettings sessionEntityTypesSettings =
         SessionEntityTypesSettings.newHttpJsonBuilder().build();
     SessionEntityTypesClient sessionEntityTypesClient =
         SessionEntityTypesClient.create(sessionEntityTypesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SessionEntityTypesClient

## Static Methods 

### create()
    
    
    public static final SessionEntityTypesClient create()

Constructs an instance of SessionEntityTypesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionEntityTypesSettings settings)
    
    
    public static final SessionEntityTypesClient create(SessionEntityTypesSettings settings)

Constructs an instance of SessionEntityTypesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionEntityTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionEntityTypesStub stub)
    
    
    public static final SessionEntityTypesClient create(SessionEntityTypesStub stub)

Constructs an instance of SessionEntityTypesClient, using the given stub for making calls. This is for advanced usage - prefer using create(SessionEntityTypesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionEntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SessionEntityTypesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient)` |   
  
## Constructors 

### SessionEntityTypesClient(SessionEntityTypesSettings settings)
    
    
    protected SessionEntityTypesClient(SessionEntityTypesSettings settings)

Constructs an instance of SessionEntityTypesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionEntityTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesSettings)`  
  
  
### SessionEntityTypesClient(SessionEntityTypesStub stub)
    
    
    protected SessionEntityTypesClient(SessionEntityTypesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionEntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SessionEntityTypesStub)`  
  
  
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

### createSessionEntityType(@Nullable SessionName parent, SessionEntityType sessionEntityType)
    
    
    public final SessionEntityType createSessionEntityType(@Nullable SessionName parent, SessionEntityType sessionEntityType)

Creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionName parent = SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]");
       SessionEntityType sessionEntityType = SessionEntityType.newBuilder().build();
       SessionEntityType response =
           sessionEntityTypesClient.createSessionEntityType(parent, sessionEntityType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SessionName`  
Required. The session to create a session entity type for. Format: `projects/<Project ID>/agent/sessions/<Session ID>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/ sessions/<Session ID>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
`sessionEntityType` | `[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)`  
Required. The session entity type to create.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### createSessionEntityType(CreateSessionEntityTypeRequest request)
    
    
    public final SessionEntityType createSessionEntityType(CreateSessionEntityTypeRequest request)

Creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       CreateSessionEntityTypeRequest request =
           CreateSessionEntityTypeRequest.newBuilder()
               .setParent(SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString())
               .setSessionEntityType(SessionEntityType.newBuilder().build())
               .build();
       SessionEntityType response = sessionEntityTypesClient.createSessionEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### createSessionEntityType(String parent, SessionEntityType sessionEntityType)
    
    
    public final SessionEntityType createSessionEntityType(String parent, SessionEntityType sessionEntityType)

Creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       String parent = SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString();
       SessionEntityType sessionEntityType = SessionEntityType.newBuilder().build();
       SessionEntityType response =
           sessionEntityTypesClient.createSessionEntityType(parent, sessionEntityType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The session to create a session entity type for. Format: `projects/<Project ID>/agent/sessions/<Session ID>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/ sessions/<Session ID>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
`sessionEntityType` | `[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)`  
Required. The session entity type to create.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### createSessionEntityTypeCallable()
    
    
    public final UnaryCallable<CreateSessionEntityTypeRequest,SessionEntityType> createSessionEntityTypeCallable()

Creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       CreateSessionEntityTypeRequest request =
           CreateSessionEntityTypeRequest.newBuilder()
               .setParent(SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString())
               .setSessionEntityType(SessionEntityType.newBuilder().build())
               .build();
       ApiFuture<SessionEntityType> future =
           sessionEntityTypesClient.createSessionEntityTypeCallable().futureCall(request);
       // Do something.
       SessionEntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)>` |   
  
### deleteSessionEntityType(@Nullable SessionEntityTypeName name)
    
    
    public final void deleteSessionEntityType(@Nullable SessionEntityTypeName name)

Deletes the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionEntityTypeName name =
           SessionEntityTypeName.ofProjectSessionEntityTypeName(
               "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]");
       sessionEntityTypesClient.deleteSessionEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SessionEntityTypeName`  
Required. The name of the entity type to delete. Format: `projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Entity Type Display Name>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
  
### deleteSessionEntityType(DeleteSessionEntityTypeRequest request)
    
    
    public final void deleteSessionEntityType(DeleteSessionEntityTypeRequest request)

Deletes the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       DeleteSessionEntityTypeRequest request =
           DeleteSessionEntityTypeRequest.newBuilder()
               .setName(
                   SessionEntityTypeName.ofProjectSessionEntityTypeName(
                           "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       sessionEntityTypesClient.deleteSessionEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSessionEntityType(String name)
    
    
    public final void deleteSessionEntityType(String name)

Deletes the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       String name =
           SessionEntityTypeName.ofProjectSessionEntityTypeName(
                   "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
               .toString();
       sessionEntityTypesClient.deleteSessionEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the entity type to delete. Format: `projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Entity Type Display Name>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
  
### deleteSessionEntityTypeCallable()
    
    
    public final UnaryCallable<DeleteSessionEntityTypeRequest,Empty> deleteSessionEntityTypeCallable()

Deletes the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       DeleteSessionEntityTypeRequest request =
           DeleteSessionEntityTypeRequest.newBuilder()
               .setName(
                   SessionEntityTypeName.ofProjectSessionEntityTypeName(
                           "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           sessionEntityTypesClient.deleteSessionEntityTypeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteSessionEntityTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = sessionEntityTypesClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           sessionEntityTypesClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSessionEntityType(@Nullable SessionEntityTypeName name)
    
    
    public final SessionEntityType getSessionEntityType(@Nullable SessionEntityTypeName name)

Retrieves the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionEntityTypeName name =
           SessionEntityTypeName.ofProjectSessionEntityTypeName(
               "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]");
       SessionEntityType response = sessionEntityTypesClient.getSessionEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SessionEntityTypeName`  
Required. The name of the session entity type. Format: `projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Entity Type Display Name>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### getSessionEntityType(GetSessionEntityTypeRequest request)
    
    
    public final SessionEntityType getSessionEntityType(GetSessionEntityTypeRequest request)

Retrieves the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       GetSessionEntityTypeRequest request =
           GetSessionEntityTypeRequest.newBuilder()
               .setName(
                   SessionEntityTypeName.ofProjectSessionEntityTypeName(
                           "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       SessionEntityType response = sessionEntityTypesClient.getSessionEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetSessionEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### getSessionEntityType(String name)
    
    
    public final SessionEntityType getSessionEntityType(String name)

Retrieves the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       String name =
           SessionEntityTypeName.ofProjectSessionEntityTypeName(
                   "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
               .toString();
       SessionEntityType response = sessionEntityTypesClient.getSessionEntityType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the session entity type. Format: `projects/<Project ID>/agent/sessions/<Session ID>/entityTypes/<Entity Type Display Name>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>/entityTypes/<Entity Type Display Name>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### getSessionEntityTypeCallable()
    
    
    public final UnaryCallable<GetSessionEntityTypeRequest,SessionEntityType> getSessionEntityTypeCallable()

Retrieves the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       GetSessionEntityTypeRequest request =
           GetSessionEntityTypeRequest.newBuilder()
               .setName(
                   SessionEntityTypeName.ofProjectSessionEntityTypeName(
                           "[PROJECT]", "[SESSION]", "[ENTITY_TYPE]")
                       .toString())
               .build();
       ApiFuture<SessionEntityType> future =
           sessionEntityTypesClient.getSessionEntityTypeCallable().futureCall(request);
       // Do something.
       SessionEntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)>` |   
  
### getSettings()
    
    
    public final @Nullable SessionEntityTypesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SessionEntityTypesSettings` |   
  
### getStub()
    
    
    public SessionEntityTypesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.SessionEntityTypesStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final SessionEntityTypesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : sessionEntityTypesClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             sessionEntityTypesClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,SessionEntityTypesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           sessionEntityTypesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListLocationsPagedResponse)>` |   
  
### listSessionEntityTypes(@Nullable SessionName parent)
    
    
    public final SessionEntityTypesClient.ListSessionEntityTypesPagedResponse listSessionEntityTypes(@Nullable SessionName parent)

Returns the list of all session entity types in the specified session.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionName parent = SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]");
       for (SessionEntityType element :
           sessionEntityTypesClient.listSessionEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.SessionName`  
Required. The session to list all session entity types from. Format: `projects/<Project ID>/agent/sessions/<Session ID>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/ sessions/<Session ID>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient.ListSessionEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListSessionEntityTypesPagedResponse)` |   
  
### listSessionEntityTypes(ListSessionEntityTypesRequest request)
    
    
    public final SessionEntityTypesClient.ListSessionEntityTypesPagedResponse listSessionEntityTypes(ListSessionEntityTypesRequest request)

Returns the list of all session entity types in the specified session.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListSessionEntityTypesRequest request =
           ListSessionEntityTypesRequest.newBuilder()
               .setParent(SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SessionEntityType element :
           sessionEntityTypesClient.listSessionEntityTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSessionEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSessionEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient.ListSessionEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListSessionEntityTypesPagedResponse)` |   
  
### listSessionEntityTypes(String parent)
    
    
    public final SessionEntityTypesClient.ListSessionEntityTypesPagedResponse listSessionEntityTypes(String parent)

Returns the list of all session entity types in the specified session.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       String parent = SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString();
       for (SessionEntityType element :
           sessionEntityTypesClient.listSessionEntityTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The session to list all session entity types from. Format: `projects/<Project ID>/agent/sessions/<Session ID>` or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/ sessions/<Session ID>`. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityTypesClient.ListSessionEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListSessionEntityTypesPagedResponse)` |   
  
### listSessionEntityTypesCallable()
    
    
    public final UnaryCallable<ListSessionEntityTypesRequest,ListSessionEntityTypesResponse> listSessionEntityTypesCallable()

Returns the list of all session entity types in the specified session.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListSessionEntityTypesRequest request =
           ListSessionEntityTypesRequest.newBuilder()
               .setParent(SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSessionEntityTypesResponse response =
             sessionEntityTypesClient.listSessionEntityTypesCallable().call(request);
         for (SessionEntityType element : response.getSessionEntityTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSessionEntityTypesRequest),[ListSessionEntityTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSessionEntityTypesResponse)>` |   
  
### listSessionEntityTypesPagedCallable()
    
    
    public final UnaryCallable<ListSessionEntityTypesRequest,SessionEntityTypesClient.ListSessionEntityTypesPagedResponse> listSessionEntityTypesPagedCallable()

Returns the list of all session entity types in the specified session.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       ListSessionEntityTypesRequest request =
           ListSessionEntityTypesRequest.newBuilder()
               .setParent(SessionName.ofProjectSessionName("[PROJECT]", "[SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SessionEntityType> future =
           sessionEntityTypesClient.listSessionEntityTypesPagedCallable().futureCall(request);
       // Do something.
       for (SessionEntityType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListSessionEntityTypesRequest),[ListSessionEntityTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityTypesClient.ListSessionEntityTypesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSessionEntityType(SessionEntityType sessionEntityType)
    
    
    public final SessionEntityType updateSessionEntityType(SessionEntityType sessionEntityType)

Updates the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionEntityType sessionEntityType = SessionEntityType.newBuilder().build();
       SessionEntityType response =
           sessionEntityTypesClient.updateSessionEntityType(sessionEntityType);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sessionEntityType` | `[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)`  
Required. The session entity type to update.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### updateSessionEntityType(SessionEntityType sessionEntityType, FieldMask updateMask)
    
    
    public final SessionEntityType updateSessionEntityType(SessionEntityType sessionEntityType, FieldMask updateMask)

Updates the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       SessionEntityType sessionEntityType = SessionEntityType.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SessionEntityType response =
           sessionEntityTypesClient.updateSessionEntityType(sessionEntityType, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sessionEntityType` | `[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)`  
Required. The session entity type to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The mask to control which fields get updated.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### updateSessionEntityType(UpdateSessionEntityTypeRequest request)
    
    
    public final SessionEntityType updateSessionEntityType(UpdateSessionEntityTypeRequest request)

Updates the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       UpdateSessionEntityTypeRequest request =
           UpdateSessionEntityTypeRequest.newBuilder()
               .setSessionEntityType(SessionEntityType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SessionEntityType response = sessionEntityTypesClient.updateSessionEntityType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)` |   
  
### updateSessionEntityTypeCallable()
    
    
    public final UnaryCallable<UpdateSessionEntityTypeRequest,SessionEntityType> updateSessionEntityTypeCallable()

Updates the specified session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionEntityTypesClient sessionEntityTypesClient = SessionEntityTypesClient.create()) {
       UpdateSessionEntityTypeRequest request =
           UpdateSessionEntityTypeRequest.newBuilder()
               .setSessionEntityType(SessionEntityType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SessionEntityType> future =
           sessionEntityTypesClient.updateSessionEntityTypeCallable().futureCall(request);
       // Do something.
       SessionEntityType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateSessionEntityTypeRequest),[SessionEntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SessionEntityType)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
