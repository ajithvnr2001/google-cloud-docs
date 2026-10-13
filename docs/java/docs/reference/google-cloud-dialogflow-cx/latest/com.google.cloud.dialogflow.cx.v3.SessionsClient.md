---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient
title: Class SessionsClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:10.599596+00:00
---

# Class SessionsClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionsClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/SessionsClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A session represents an interaction with a user. You retrieve user input and pass it to the DetectIntent method to determine user intent and respond.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       DetectIntentRequest request =
           DetectIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .setResponseView(DetectIntentResponseView.forNumber(0))
               .build();
       DetectIntentResponse response = sessionsClient.detectIntent(request);
     }
     

Note: close() needs to be called on the SessionsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
DetectIntent |  Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.  Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detectIntent(DetectIntentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detectIntentCallable() 

  
ServerStreamingDetectIntent |  Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * serverStreamingDetectIntentCallable() 

  
StreamingDetectIntent |  Processes a natural language query in audio format in a streaming fashion and returns structured, actionable data as a result. This method is only available via the gRPC API (not REST).  Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingDetectIntentCallable() 

  
MatchIntent |  Returns preliminary intent match results, doesn't change the session status. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * matchIntent(MatchIntentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * matchIntentCallable() 

  
FulfillIntent |  Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fulfillIntent(FulfillIntentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fulfillIntentCallable() 

  
SubmitAnswerFeedback |  Updates the feedback received from the user for a single turn of the bot response. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * submitAnswerFeedback(SubmitAnswerFeedbackRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * submitAnswerFeedbackCallable() 

  
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

This class can be customized by passing in a custom instance of SessionsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionsSettings sessionsSettings =
         SessionsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SessionsClient sessionsClient = SessionsClient.create(sessionsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionsSettings sessionsSettings =
         SessionsSettings.newBuilder().setEndpoint(myEndpoint).build();
     SessionsClient sessionsClient = SessionsClient.create(sessionsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SessionsSettings sessionsSettings = SessionsSettings.newHttpJsonBuilder().build();
     SessionsClient sessionsClient = SessionsClient.create(sessionsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SessionsClient

## Static Methods 

### create()
    
    
    public static final SessionsClient create()

Constructs an instance of SessionsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionsSettings settings)
    
    
    public static final SessionsClient create(SessionsSettings settings)

Constructs an instance of SessionsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SessionsStub stub)
    
    
    public static final SessionsClient create(SessionsStub stub)

Constructs an instance of SessionsClient, using the given stub for making calls. This is for advanced usage - prefer using create(SessionsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SessionsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient)` |   
  
## Constructors 

### SessionsClient(SessionsSettings settings)
    
    
    protected SessionsClient(SessionsSettings settings)

Constructs an instance of SessionsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsSettings)`  
  
  
### SessionsClient(SessionsStub stub)
    
    
    protected SessionsClient(SessionsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SessionsStub)`  
  
  
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

### detectIntent(DetectIntentRequest request)
    
    
    public final DetectIntentResponse detectIntent(DetectIntentRequest request)

Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       DetectIntentRequest request =
           DetectIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .setResponseView(DetectIntentResponseView.forNumber(0))
               .build();
       DetectIntentResponse response = sessionsClient.detectIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse)` |   
  
### detectIntentCallable()
    
    
    public final UnaryCallable<DetectIntentRequest,DetectIntentResponse> detectIntentCallable()

Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       DetectIntentRequest request =
           DetectIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .setResponseView(DetectIntentResponseView.forNumber(0))
               .build();
       ApiFuture<DetectIntentResponse> future =
           sessionsClient.detectIntentCallable().futureCall(request);
       // Do something.
       DetectIntentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest),[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse)>` |   
  
### fulfillIntent(FulfillIntentRequest request)
    
    
    public final FulfillIntentResponse fulfillIntent(FulfillIntentRequest request)

Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       FulfillIntentRequest request =
           FulfillIntentRequest.newBuilder()
               .setMatchIntentRequest(MatchIntentRequest.newBuilder().build())
               .setMatch(Match.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .build();
       FulfillIntentResponse response = sessionsClient.fulfillIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FulfillIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FulfillIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillIntentResponse)` |   
  
### fulfillIntentCallable()
    
    
    public final UnaryCallable<FulfillIntentRequest,FulfillIntentResponse> fulfillIntentCallable()

Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       FulfillIntentRequest request =
           FulfillIntentRequest.newBuilder()
               .setMatchIntentRequest(MatchIntentRequest.newBuilder().build())
               .setMatch(Match.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .build();
       ApiFuture<FulfillIntentResponse> future =
           sessionsClient.fulfillIntentCallable().futureCall(request);
       // Do something.
       FulfillIntentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FulfillIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillIntentRequest),[FulfillIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FulfillIntentResponse)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = sessionsClient.getLocation(request);
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
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = sessionsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable SessionsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.SessionsSettings` |   
  
### getStub()
    
    
    public SessionsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SessionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.SessionsStub)` |   
  
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
    
    
    public final SessionsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : sessionsClient.listLocations(request).iterateAll()) {
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
`[SessionsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.ListLocationsPagedResponse)` |   
  
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
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = sessionsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SessionsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = sessionsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient.ListLocationsPagedResponse)>` |   
  
### matchIntent(MatchIntentRequest request)
    
    
    public final MatchIntentResponse matchIntent(MatchIntentRequest request)

Returns preliminary intent match results, doesn't change the session status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       MatchIntentRequest request =
           MatchIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setPersistParameterChanges(true)
               .build();
       MatchIntentResponse response = sessionsClient.matchIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MatchIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.MatchIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MatchIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.MatchIntentResponse)` |   
  
### matchIntentCallable()
    
    
    public final UnaryCallable<MatchIntentRequest,MatchIntentResponse> matchIntentCallable()

Returns preliminary intent match results, doesn't change the session status.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       MatchIntentRequest request =
           MatchIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setPersistParameterChanges(true)
               .build();
       ApiFuture<MatchIntentResponse> future =
           sessionsClient.matchIntentCallable().futureCall(request);
       // Do something.
       MatchIntentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MatchIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.MatchIntentRequest),[MatchIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.MatchIntentResponse)>` |   
  
### serverStreamingDetectIntentCallable()
    
    
    public final ServerStreamingCallable<DetectIntentRequest,DetectIntentResponse> serverStreamingDetectIntentCallable()

Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       DetectIntentRequest request =
           DetectIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .setResponseView(DetectIntentResponseView.forNumber(0))
               .build();
       ServerStream<DetectIntentResponse> stream =
           sessionsClient.serverStreamingDetectIntentCallable().call(request);
       for (DetectIntentResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[DetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentRequest),[DetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamingDetectIntentCallable()
    
    
    public final BidiStreamingCallable<StreamingDetectIntentRequest,StreamingDetectIntentResponse> streamingDetectIntentCallable()

Processes a natural language query in audio format in a streaming fashion and returns structured, actionable data as a result. This method is only available via the gRPC API (not REST).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       BidiStream<StreamingDetectIntentRequest, StreamingDetectIntentResponse> bidiStream =
           sessionsClient.streamingDetectIntentCallable().call();
       StreamingDetectIntentRequest request =
           StreamingDetectIntentRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setQueryInput(QueryInput.newBuilder().build())
               .setOutputAudioConfig(OutputAudioConfig.newBuilder().build())
               .setEnablePartialResponse(true)
               .setEnableDebuggingInfo(true)
               .setResponseView(DetectIntentResponseView.forNumber(0))
               .build();
       bidiStream.send(request);
       for (StreamingDetectIntentResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingDetectIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest),[StreamingDetectIntentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentResponse)>` |   
  
### submitAnswerFeedback(SubmitAnswerFeedbackRequest request)
    
    
    public final AnswerFeedback submitAnswerFeedback(SubmitAnswerFeedbackRequest request)

Updates the feedback received from the user for a single turn of the bot response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       SubmitAnswerFeedbackRequest request =
           SubmitAnswerFeedbackRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setResponseId("responseId-633138884")
               .setAnswerFeedback(AnswerFeedback.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AnswerFeedback response = sessionsClient.submitAnswerFeedback(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubmitAnswerFeedbackRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SubmitAnswerFeedbackRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerFeedback](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AnswerFeedback)` |   
  
### submitAnswerFeedbackCallable()
    
    
    public final UnaryCallable<SubmitAnswerFeedbackRequest,AnswerFeedback> submitAnswerFeedbackCallable()

Updates the feedback received from the user for a single turn of the bot response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionsClient sessionsClient = SessionsClient.create()) {
       SubmitAnswerFeedbackRequest request =
           SubmitAnswerFeedbackRequest.newBuilder()
               .setSession(
                   SessionName.ofProjectLocationAgentSessionName(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[SESSION]")
                       .toString())
               .setResponseId("responseId-633138884")
               .setAnswerFeedback(AnswerFeedback.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AnswerFeedback> future =
           sessionsClient.submitAnswerFeedbackCallable().futureCall(request);
       // Do something.
       AnswerFeedback response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SubmitAnswerFeedbackRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SubmitAnswerFeedbackRequest),[AnswerFeedback](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AnswerFeedback)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
