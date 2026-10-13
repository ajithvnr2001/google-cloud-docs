---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceClient
title: Class AssistantServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:29.142769+00:00
---

# Class AssistantServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AssistantServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/AssistantServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing Assistant configuration and assisting users.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssistantServiceClient assistantServiceClient = AssistantServiceClient.create()) {
       StreamAssistRequest request =
           StreamAssistRequest.newBuilder()
               .setName(
                   AssistantName.of(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]")
                       .toString())
               .setQuery(Query.newBuilder().build())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setUserMetadata(AssistUserMetadata.newBuilder().build())
               .setAgentsSpec(StreamAssistRequest.AgentsSpec.newBuilder().build())
               .setToolsSpec(StreamAssistRequest.ToolsSpec.newBuilder().build())
               .setGenerationSpec(StreamAssistRequest.GenerationSpec.newBuilder().build())
               .build();
       ServerStream<StreamAssistResponse> stream =
           assistantServiceClient.streamAssistCallable().call(request);
       for (StreamAssistResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

Note: close() needs to be called on the AssistantServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
StreamAssist |  Assists the user with a query in a streaming fashion. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamAssistCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AssistantServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssistantServiceSettings assistantServiceSettings =
         AssistantServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AssistantServiceClient assistantServiceClient =
         AssistantServiceClient.create(assistantServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssistantServiceSettings assistantServiceSettings =
         AssistantServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AssistantServiceClient assistantServiceClient =
         AssistantServiceClient.create(assistantServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssistantServiceSettings assistantServiceSettings =
         AssistantServiceSettings.newHttpJsonBuilder().build();
     AssistantServiceClient assistantServiceClient =
         AssistantServiceClient.create(assistantServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AssistantServiceClient

## Static Methods 

### create()
    
    
    public static final AssistantServiceClient create()

Constructs an instance of AssistantServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AssistantServiceSettings settings)
    
    
    public static final AssistantServiceClient create(AssistantServiceSettings settings)

Constructs an instance of AssistantServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AssistantServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AssistantServiceStub stub)
    
    
    public static final AssistantServiceClient create(AssistantServiceStub stub)

Constructs an instance of AssistantServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AssistantServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AssistantServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.AssistantServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceClient)` |   
  
## Constructors 

### AssistantServiceClient(AssistantServiceSettings settings)
    
    
    protected AssistantServiceClient(AssistantServiceSettings settings)

Constructs an instance of AssistantServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AssistantServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AssistantServiceSettings)`  
  
  
### AssistantServiceClient(AssistantServiceStub stub)
    
    
    protected AssistantServiceClient(AssistantServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AssistantServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.AssistantServiceStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable AssistantServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.AssistantServiceSettings` |   
  
### getStub()
    
    
    public AssistantServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AssistantServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.AssistantServiceStub)` |   
  
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
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamAssistCallable()
    
    
    public final ServerStreamingCallable<StreamAssistRequest,StreamAssistResponse> streamAssistCallable()

Assists the user with a query in a streaming fashion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssistantServiceClient assistantServiceClient = AssistantServiceClient.create()) {
       StreamAssistRequest request =
           StreamAssistRequest.newBuilder()
               .setName(
                   AssistantName.of(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[ENGINE]", "[ASSISTANT]")
                       .toString())
               .setQuery(Query.newBuilder().build())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setUserMetadata(AssistUserMetadata.newBuilder().build())
               .setAgentsSpec(StreamAssistRequest.AgentsSpec.newBuilder().build())
               .setToolsSpec(StreamAssistRequest.ToolsSpec.newBuilder().build())
               .setGenerationSpec(StreamAssistRequest.GenerationSpec.newBuilder().build())
               .build();
       ServerStream<StreamAssistResponse> stream =
           assistantServiceClient.streamAssistCallable().call(request);
       for (StreamAssistResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[StreamAssistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.StreamAssistRequest),[StreamAssistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.StreamAssistResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
