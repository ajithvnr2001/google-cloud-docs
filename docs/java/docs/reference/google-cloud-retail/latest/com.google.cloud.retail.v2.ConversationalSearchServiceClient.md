---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceClient
title: Class ConversationalSearchServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:20.292616+00:00
---

# Class ConversationalSearchServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationalSearchServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/ConversationalSearchServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for retail conversational search.

This feature is only available for users who have Retail Conversational Search enabled. Enable Retail Conversational Search on Cloud Console before using this feature.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationalSearchRequest request =
           ConversationalSearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setConversationId("conversationId-1676095234")
               .setSearchParams(ConversationalSearchRequest.SearchParams.newBuilder().build())
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setConversationalFilteringSpec(
                   ConversationalSearchRequest.ConversationalFilteringSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .addAllSafetySettings(new ArrayList<SafetySetting>())
               .build();
       ServerStream<ConversationalSearchResponse> stream =
           conversationalSearchServiceClient.conversationalSearchCallable().call(request);
       for (ConversationalSearchResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

Note: close() needs to be called on the ConversationalSearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ConversationalSearch |  Performs a conversational search.  This feature is only available for users who have Conversational Search enabled. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * conversationalSearchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ConversationalSearchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newHttpJsonBuilder().build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationalSearchServiceClient

## Static Methods 

### create()
    
    
    public static final ConversationalSearchServiceClient create()

Constructs an instance of ConversationalSearchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationalSearchServiceSettings settings)
    
    
    public static final ConversationalSearchServiceClient create(ConversationalSearchServiceSettings settings)

Constructs an instance of ConversationalSearchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationalSearchServiceStub stub)
    
    
    public static final ConversationalSearchServiceClient create(ConversationalSearchServiceStub stub)

Constructs an instance of ConversationalSearchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationalSearchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ConversationalSearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceClient)` |   
  
## Constructors 

### ConversationalSearchServiceClient(ConversationalSearchServiceSettings settings)
    
    
    protected ConversationalSearchServiceClient(ConversationalSearchServiceSettings settings)

Constructs an instance of ConversationalSearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchServiceSettings)`  
  
  
### ConversationalSearchServiceClient(ConversationalSearchServiceStub stub)
    
    
    protected ConversationalSearchServiceClient(ConversationalSearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ConversationalSearchServiceStub)`  
  
  
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

### conversationalSearchCallable()
    
    
    public final ServerStreamingCallable<ConversationalSearchRequest,ConversationalSearchResponse> conversationalSearchCallable()

Performs a conversational search.

This feature is only available for users who have Conversational Search enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationalSearchRequest request =
           ConversationalSearchRequest.newBuilder()
               .setPlacement("placement1792938725")
               .setBranch(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setQuery("query107944136")
               .addAllPageCategories(new ArrayList<String>())
               .setConversationId("conversationId-1676095234")
               .setSearchParams(ConversationalSearchRequest.SearchParams.newBuilder().build())
               .setVisitorId("visitorId1880545833")
               .setUserInfo(UserInfo.newBuilder().build())
               .setConversationalFilteringSpec(
                   ConversationalSearchRequest.ConversationalFilteringSpec.newBuilder().build())
               .putAllUserLabels(new HashMap<String, String>())
               .addAllSafetySettings(new ArrayList<SafetySetting>())
               .build();
       ServerStream<ConversationalSearchResponse> stream =
           conversationalSearchServiceClient.conversationalSearchCallable().call(request);
       for (ConversationalSearchResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[ConversationalSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchRequest),[ConversationalSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ConversationalSearchResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable ConversationalSearchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ConversationalSearchServiceSettings` |   
  
### getStub()
    
    
    public ConversationalSearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ConversationalSearchServiceStub)` |   
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
