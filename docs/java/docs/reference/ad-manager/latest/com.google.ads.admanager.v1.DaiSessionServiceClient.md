---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceClient
title: Class DaiSessionServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:46.140144+00:00
---

# Class DaiSessionServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DaiSessionServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/DaiSessionServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `DaiSession` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiSessionServiceClient daiSessionServiceClient = DaiSessionServiceClient.create()) {
       DaiSessionName name = DaiSessionName.of("[NETWORK_CODE]", "[DAI_SESSION]");
       DaiSession response = daiSessionServiceClient.getDaiSession(name);
     }
     

Note: close() needs to be called on the DaiSessionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDaiSession |  Retrieves a `DaiSession` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDaiSession(GetDaiSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDaiSession(DaiSessionName name) 
  * getDaiSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDaiSessionCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DaiSessionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiSessionServiceSettings daiSessionServiceSettings =
         DaiSessionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DaiSessionServiceClient daiSessionServiceClient =
         DaiSessionServiceClient.create(daiSessionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiSessionServiceSettings daiSessionServiceSettings =
         DaiSessionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DaiSessionServiceClient daiSessionServiceClient =
         DaiSessionServiceClient.create(daiSessionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DaiSessionServiceClient

## Static Methods 

### create()
    
    
    public static final DaiSessionServiceClient create()

Constructs an instance of DaiSessionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DaiSessionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiSessionServiceSettings settings)
    
    
    public static final DaiSessionServiceClient create(DaiSessionServiceSettings settings)

Constructs an instance of DaiSessionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiSessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiSessionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiSessionServiceStub stub)
    
    
    public static final DaiSessionServiceClient create(DaiSessionServiceStub stub)

Constructs an instance of DaiSessionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DaiSessionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiSessionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiSessionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiSessionServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceClient)` |   
  
## Constructors 

### DaiSessionServiceClient(DaiSessionServiceSettings settings)
    
    
    protected DaiSessionServiceClient(DaiSessionServiceSettings settings)

Constructs an instance of DaiSessionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiSessionServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSessionServiceSettings)`  
  
  
### DaiSessionServiceClient(DaiSessionServiceStub stub)
    
    
    protected DaiSessionServiceClient(DaiSessionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiSessionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiSessionServiceStub)`  
  
  
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

### getDaiSession(@Nullable DaiSessionName name)
    
    
    public final DaiSession getDaiSession(@Nullable DaiSessionName name)

Retrieves a `DaiSession` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiSessionServiceClient daiSessionServiceClient = DaiSessionServiceClient.create()) {
       DaiSessionName name = DaiSessionName.of("[NETWORK_CODE]", "[DAI_SESSION]");
       DaiSession response = daiSessionServiceClient.getDaiSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiSessionName`  
Required. The resource name of the DaiSession. The dai_session can be either the session ID or debug key, that DAI returns on stream create. For details, see [Locate a DAI session ID or debug key](https://support.google.com/admanager/answer/7257678). Format: `networks/{network_code}/daiSessions/{dai_session}` Format: `networks/{network_code}/daiSessions/{session_id}` Format: `networks/{network_code}/daiSessions/{debug_key}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiSession](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession)` |   
  
### getDaiSession(GetDaiSessionRequest request)
    
    
    public final DaiSession getDaiSession(GetDaiSessionRequest request)

Retrieves a `DaiSession` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiSessionServiceClient daiSessionServiceClient = DaiSessionServiceClient.create()) {
       GetDaiSessionRequest request =
           GetDaiSessionRequest.newBuilder()
               .setName(DaiSessionName.of("[NETWORK_CODE]", "[DAI_SESSION]").toString())
               .build();
       DaiSession response = daiSessionServiceClient.getDaiSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDaiSessionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiSession](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession)` |   
  
### getDaiSession(String name)
    
    
    public final DaiSession getDaiSession(String name)

Retrieves a `DaiSession` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiSessionServiceClient daiSessionServiceClient = DaiSessionServiceClient.create()) {
       String name = DaiSessionName.of("[NETWORK_CODE]", "[DAI_SESSION]").toString();
       DaiSession response = daiSessionServiceClient.getDaiSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DaiSession. The dai_session can be either the session ID or debug key, that DAI returns on stream create. For details, see [Locate a DAI session ID or debug key](https://support.google.com/admanager/answer/7257678). Format: `networks/{network_code}/daiSessions/{dai_session}` Format: `networks/{network_code}/daiSessions/{session_id}` Format: `networks/{network_code}/daiSessions/{debug_key}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiSession](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession)` |   
  
### getDaiSessionCallable()
    
    
    public final UnaryCallable<GetDaiSessionRequest,DaiSession> getDaiSessionCallable()

Retrieves a `DaiSession` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiSessionServiceClient daiSessionServiceClient = DaiSessionServiceClient.create()) {
       GetDaiSessionRequest request =
           GetDaiSessionRequest.newBuilder()
               .setName(DaiSessionName.of("[NETWORK_CODE]", "[DAI_SESSION]").toString())
               .build();
       ApiFuture<DaiSession> future =
           daiSessionServiceClient.getDaiSessionCallable().futureCall(request);
       // Do something.
       DaiSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDaiSessionRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiSessionRequest),[DaiSession](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession)>` |   
  
### getSettings()
    
    
    public final @Nullable DaiSessionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiSessionServiceSettings` |   
  
### getStub()
    
    
    public DaiSessionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DaiSessionServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiSessionServiceStub)` |   
  
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

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
