---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceClient
title: Class GroundedGenerationServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:04.163308+00:00
---

# Class GroundedGenerationServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GroundedGenerationServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/GroundedGenerationServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for grounded generation.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       GenerateGroundedContentRequest request =
           GenerateGroundedContentRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSystemInstruction(GroundedGenerationContent.newBuilder().build())
               .addAllContents(new ArrayList<GroundedGenerationContent>())
               .setGenerationSpec(GenerateGroundedContentRequest.GenerationSpec.newBuilder().build())
               .setGroundingSpec(GenerateGroundedContentRequest.GroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       GenerateGroundedContentResponse response =
           groundedGenerationServiceClient.generateGroundedContent(request);
     }
     

Note: close() needs to be called on the GroundedGenerationServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
StreamGenerateGroundedContent |  Generates grounded content in a streaming fashion. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamGenerateGroundedContentCallable() 

  
GenerateGroundedContent |  Generates grounded content. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateGroundedContent(GenerateGroundedContentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateGroundedContentCallable() 

  
CheckGrounding |  Performs a grounding check. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkGrounding(CheckGroundingRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkGroundingCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GroundedGenerationServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GroundedGenerationServiceSettings groundedGenerationServiceSettings =
         GroundedGenerationServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create(groundedGenerationServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GroundedGenerationServiceSettings groundedGenerationServiceSettings =
         GroundedGenerationServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create(groundedGenerationServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GroundedGenerationServiceSettings groundedGenerationServiceSettings =
         GroundedGenerationServiceSettings.newHttpJsonBuilder().build();
     GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create(groundedGenerationServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GroundedGenerationServiceClient

## Static Methods 

### create()
    
    
    public static final GroundedGenerationServiceClient create()

Constructs an instance of GroundedGenerationServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GroundedGenerationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GroundedGenerationServiceSettings settings)
    
    
    public static final GroundedGenerationServiceClient create(GroundedGenerationServiceSettings settings)

Constructs an instance of GroundedGenerationServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GroundedGenerationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundedGenerationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GroundedGenerationServiceStub stub)
    
    
    public static final GroundedGenerationServiceClient create(GroundedGenerationServiceStub stub)

Constructs an instance of GroundedGenerationServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(GroundedGenerationServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GroundedGenerationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.GroundedGenerationServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GroundedGenerationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceClient)` |   
  
## Constructors 

### GroundedGenerationServiceClient(GroundedGenerationServiceSettings settings)
    
    
    protected GroundedGenerationServiceClient(GroundedGenerationServiceSettings settings)

Constructs an instance of GroundedGenerationServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GroundedGenerationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GroundedGenerationServiceSettings)`  
  
  
### GroundedGenerationServiceClient(GroundedGenerationServiceStub stub)
    
    
    protected GroundedGenerationServiceClient(GroundedGenerationServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GroundedGenerationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.GroundedGenerationServiceStub)`  
  
  
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
  
### checkGrounding(CheckGroundingRequest request)
    
    
    public final CheckGroundingResponse checkGrounding(CheckGroundingRequest request)

Performs a grounding check.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       CheckGroundingRequest request =
           CheckGroundingRequest.newBuilder()
               .setGroundingConfig(
                   GroundingConfigName.of("[PROJECT]", "[LOCATION]", "[GROUNDING_CONFIG]")
                       .toString())
               .setAnswerCandidate("answerCandidate-292402331")
               .addAllFacts(new ArrayList<GroundingFact>())
               .setGroundingSpec(CheckGroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       CheckGroundingResponse response = groundedGenerationServiceClient.checkGrounding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckGroundingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CheckGroundingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckGroundingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CheckGroundingResponse)` |   
  
### checkGroundingCallable()
    
    
    public final UnaryCallable<CheckGroundingRequest,CheckGroundingResponse> checkGroundingCallable()

Performs a grounding check.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       CheckGroundingRequest request =
           CheckGroundingRequest.newBuilder()
               .setGroundingConfig(
                   GroundingConfigName.of("[PROJECT]", "[LOCATION]", "[GROUNDING_CONFIG]")
                       .toString())
               .setAnswerCandidate("answerCandidate-292402331")
               .addAllFacts(new ArrayList<GroundingFact>())
               .setGroundingSpec(CheckGroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       ApiFuture<CheckGroundingResponse> future =
           groundedGenerationServiceClient.checkGroundingCallable().futureCall(request);
       // Do something.
       CheckGroundingResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckGroundingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CheckGroundingRequest),[CheckGroundingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CheckGroundingResponse)>` |   
  
### close()
    
    
    public final void close()

### generateGroundedContent(GenerateGroundedContentRequest request)
    
    
    public final GenerateGroundedContentResponse generateGroundedContent(GenerateGroundedContentRequest request)

Generates grounded content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       GenerateGroundedContentRequest request =
           GenerateGroundedContentRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSystemInstruction(GroundedGenerationContent.newBuilder().build())
               .addAllContents(new ArrayList<GroundedGenerationContent>())
               .setGenerationSpec(GenerateGroundedContentRequest.GenerationSpec.newBuilder().build())
               .setGroundingSpec(GenerateGroundedContentRequest.GroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       GenerateGroundedContentResponse response =
           groundedGenerationServiceClient.generateGroundedContent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateGroundedContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateGroundedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentResponse)` |   
  
### generateGroundedContentCallable()
    
    
    public final UnaryCallable<GenerateGroundedContentRequest,GenerateGroundedContentResponse> generateGroundedContentCallable()

Generates grounded content.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       GenerateGroundedContentRequest request =
           GenerateGroundedContentRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSystemInstruction(GroundedGenerationContent.newBuilder().build())
               .addAllContents(new ArrayList<GroundedGenerationContent>())
               .setGenerationSpec(GenerateGroundedContentRequest.GenerationSpec.newBuilder().build())
               .setGroundingSpec(GenerateGroundedContentRequest.GroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       ApiFuture<GenerateGroundedContentResponse> future =
           groundedGenerationServiceClient.generateGroundedContentCallable().futureCall(request);
       // Do something.
       GenerateGroundedContentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateGroundedContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentRequest),[GenerateGroundedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable GroundedGenerationServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.GroundedGenerationServiceSettings` |   
  
### getStub()
    
    
    public GroundedGenerationServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GroundedGenerationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.GroundedGenerationServiceStub)` |   
  
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

### streamGenerateGroundedContentCallable()
    
    
    public final BidiStreamingCallable<GenerateGroundedContentRequest,GenerateGroundedContentResponse> streamGenerateGroundedContentCallable()

Generates grounded content in a streaming fashion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GroundedGenerationServiceClient groundedGenerationServiceClient =
         GroundedGenerationServiceClient.create()) {
       BidiStream<GenerateGroundedContentRequest, GenerateGroundedContentResponse> bidiStream =
           groundedGenerationServiceClient.streamGenerateGroundedContentCallable().call();
       GenerateGroundedContentRequest request =
           GenerateGroundedContentRequest.newBuilder()
               .setLocation(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSystemInstruction(GroundedGenerationContent.newBuilder().build())
               .addAllContents(new ArrayList<GroundedGenerationContent>())
               .setGenerationSpec(GenerateGroundedContentRequest.GenerationSpec.newBuilder().build())
               .setGroundingSpec(GenerateGroundedContentRequest.GroundingSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .build();
       bidiStream.send(request);
       for (GenerateGroundedContentResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[GenerateGroundedContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentRequest),[GenerateGroundedContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GenerateGroundedContentResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
