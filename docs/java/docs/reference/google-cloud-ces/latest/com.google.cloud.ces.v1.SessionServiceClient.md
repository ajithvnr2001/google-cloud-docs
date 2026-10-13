---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient
title: Class SessionServiceClient (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:42.893253+00:00
---

# Class SessionServiceClient (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SessionServiceClient (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-ces/google-cloud-ces/src/main/java/com/google/cloud/ces/v1/SessionServiceClient.java)| [Product Reference](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps)| [RPC Documentation](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/rpc)  
---|---|---  
  
Service Description: Session service provides APIs for interacting with CES agents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       RunSessionRequest request =
           RunSessionRequest.newBuilder()
               .setConfig(SessionConfig.newBuilder().build())
               .addAllInputs(new ArrayList<SessionInput>())
               .build();
       RunSessionResponse response = sessionServiceClient.runSession(request);
     }
     

Note: close() needs to be called on the SessionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RunSession |  Initiates a single-turn interaction with the CES agent within a session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runSession(RunSessionRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runSessionCallable() 

  
StreamRunSession |  Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.  By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set enable_text_streaming to true. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamRunSessionCallable() 

  
BidiRunSession |  Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.  \--- Client Request Stream --- The client streams requests in the following order:  1\. Initialization: The first message must contain SessionConfig. For audio sessions, this should also include InputAudioConfig and OutputAudioConfig to define audio processing and synthesis parameters.  2\. Interaction: Subsequent messages stream SessionInput containing real-time user input data.  3\. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving EndSession or GoAway from the agent.  \--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:  1\. Speech Recognition (First N messages): Contains RecognitionResult representing the concatenated user speech segments captured so far. This is only populated for audio sessions.  2\. Response (Next M messages): Contains SessionOutput delivering the agent's response in various modalities (e.g., text, audio).  3\. Turn Completion (Final message of the turn): Contains SessionOutput with turn_completed set to true. This signals the end of the current turn and includes DiagnosticInfo with execution details.  \--- Audio Best Practices --- 1. Streaming: Stream audio data **CONTINUOUSLY**, even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).  2\. Playback & Interruption: Play audio responses upon receipt. Stop playback immediately if an InterruptionSignal is received (e.g., user barge-in or new agent response). |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bidiRunSessionCallable() 

  
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
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient)` |   
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
`settings` | `[SessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient)` |   
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
`stub` | `[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.stub.SessionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient)` |   
  
## Constructors 

### SessionServiceClient(SessionServiceSettings settings)
    
    
    protected SessionServiceClient(SessionServiceSettings settings)

Constructs an instance of SessionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceSettings)`  
  
  
### SessionServiceClient(SessionServiceStub stub)
    
    
    protected SessionServiceClient(SessionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.stub.SessionServiceStub)`  
  
  
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
  
### bidiRunSessionCallable()
    
    
    public final BidiStreamingCallable<BidiSessionClientMessage,BidiSessionServerMessage> bidiRunSessionCallable()

Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.

\--- Client Request Stream --- The client streams requests in the following order:

1\. Initialization: The first message must contain SessionConfig. For audio sessions, this should also include InputAudioConfig and OutputAudioConfig to define audio processing and synthesis parameters.

2\. Interaction: Subsequent messages stream SessionInput containing real-time user input data.

3\. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving EndSession or GoAway from the agent.

\--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:

1\. Speech Recognition (First N messages): Contains RecognitionResult representing the concatenated user speech segments captured so far. This is only populated for audio sessions.

2\. Response (Next M messages): Contains SessionOutput delivering the agent's response in various modalities (e.g., text, audio).

3\. Turn Completion (Final message of the turn): Contains SessionOutput with turn_completed set to true. This signals the end of the current turn and includes DiagnosticInfo with execution details.

\--- Audio Best Practices --- 1. Streaming: Stream audio data **CONTINUOUSLY**, even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).

2\. Playback & Interruption: Play audio responses upon receipt. Stop playback immediately if an InterruptionSignal is received (e.g., user barge-in or new agent response).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       BidiStream<BidiSessionClientMessage, BidiSessionServerMessage> bidiStream =
           sessionServiceClient.bidiRunSessionCallable().call();
       BidiSessionClientMessage request = BidiSessionClientMessage.newBuilder().build();
       bidiStream.send(request);
       for (BidiSessionServerMessage response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[BidiSessionClientMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.BidiSessionClientMessage),[BidiSessionServerMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.BidiSessionServerMessage)>` |   
  
### close()
    
    
    public final void close()

### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = sessionServiceClient.getLocation(request);
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
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = sessionServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable SessionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.ces.v1.SessionServiceSettings` |   
  
### getStub()
    
    
    public SessionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SessionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.stub.SessionServiceStub)` |   
  
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
    
    
    public final SessionServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : sessionServiceClient.listLocations(request).iterateAll()) {
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
`[SessionServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = sessionServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SessionServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           sessionServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SessionServiceClient.ListLocationsPagedResponse)>` |   
  
### runSession(RunSessionRequest request)
    
    
    public final RunSessionResponse runSession(RunSessionRequest request)

Initiates a single-turn interaction with the CES agent within a session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       RunSessionRequest request =
           RunSessionRequest.newBuilder()
               .setConfig(SessionConfig.newBuilder().build())
               .addAllInputs(new ArrayList<SessionInput>())
               .build();
       RunSessionResponse response = sessionServiceClient.runSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunSessionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionResponse)` |   
  
### runSessionCallable()
    
    
    public final UnaryCallable<RunSessionRequest,RunSessionResponse> runSessionCallable()

Initiates a single-turn interaction with the CES agent within a session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       RunSessionRequest request =
           RunSessionRequest.newBuilder()
               .setConfig(SessionConfig.newBuilder().build())
               .addAllInputs(new ArrayList<SessionInput>())
               .build();
       ApiFuture<RunSessionResponse> future =
           sessionServiceClient.runSessionCallable().futureCall(request);
       // Do something.
       RunSessionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionRequest),[RunSessionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamRunSessionCallable()
    
    
    public final ServerStreamingCallable<RunSessionRequest,RunSessionResponse> streamRunSessionCallable()

Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.

By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set enable_text_streaming to true.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SessionServiceClient sessionServiceClient = SessionServiceClient.create()) {
       RunSessionRequest request =
           RunSessionRequest.newBuilder()
               .setConfig(SessionConfig.newBuilder().build())
               .addAllInputs(new ArrayList<SessionInput>())
               .build();
       ServerStream<RunSessionResponse> stream =
           sessionServiceClient.streamRunSessionCallable().call(request);
       for (RunSessionResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[RunSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionRequest),[RunSessionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.RunSessionResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
