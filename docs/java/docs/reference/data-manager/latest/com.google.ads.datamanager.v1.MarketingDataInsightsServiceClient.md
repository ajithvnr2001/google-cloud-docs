---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceClient
title: Class MarketingDataInsightsServiceClient (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:00.327852+00:00
---

# Class MarketingDataInsightsServiceClient (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MarketingDataInsightsServiceClient (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-datamanager/data-manager/src/main/java/com/google/ads/datamanager/v1/MarketingDataInsightsServiceClient.java)| [Product Reference](https://developers.google.com/data-manager)| [RPC Documentation](https://developers.google.com/data-manager/api/reference/rpc)  
---|---|---  
  
Service Description: Service to return insights on marketing data.

This feature is only available to data partners.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create()) {
       RetrieveInsightsRequest request =
           RetrieveInsightsRequest.newBuilder()
               .setParent("parent-995424086")
               .setBaseline(Baseline.newBuilder().build())
               .setUserListId("userListId1381604868")
               .build();
       RetrieveInsightsResponse response =
           marketingDataInsightsServiceClient.retrieveInsights(request);
     }
     

Note: close() needs to be called on the MarketingDataInsightsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RetrieveInsights |  Retrieves marketing data insights for a given user list.  This feature is only available to data partners.  Authorization Headers:  This method supports the following optional headers to define how the API authorizes access for the request: 

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveInsights(RetrieveInsightsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveInsightsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MarketingDataInsightsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingDataInsightsServiceSettings marketingDataInsightsServiceSettings =
         MarketingDataInsightsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create(marketingDataInsightsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingDataInsightsServiceSettings marketingDataInsightsServiceSettings =
         MarketingDataInsightsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create(marketingDataInsightsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingDataInsightsServiceSettings marketingDataInsightsServiceSettings =
         MarketingDataInsightsServiceSettings.newHttpJsonBuilder().build();
     MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create(marketingDataInsightsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MarketingDataInsightsServiceClient

## Static Methods 

### create()
    
    
    public static final MarketingDataInsightsServiceClient create()

Constructs an instance of MarketingDataInsightsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MarketingDataInsightsServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MarketingDataInsightsServiceSettings settings)
    
    
    public static final MarketingDataInsightsServiceClient create(MarketingDataInsightsServiceSettings settings)

Constructs an instance of MarketingDataInsightsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MarketingDataInsightsServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingDataInsightsServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MarketingDataInsightsServiceStub stub)
    
    
    public static final MarketingDataInsightsServiceClient create(MarketingDataInsightsServiceStub stub)

Constructs an instance of MarketingDataInsightsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MarketingDataInsightsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MarketingDataInsightsServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.MarketingDataInsightsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingDataInsightsServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceClient)` |   
  
## Constructors 

### MarketingDataInsightsServiceClient(MarketingDataInsightsServiceSettings settings)
    
    
    protected MarketingDataInsightsServiceClient(MarketingDataInsightsServiceSettings settings)

Constructs an instance of MarketingDataInsightsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MarketingDataInsightsServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.MarketingDataInsightsServiceSettings)`  
  
  
### MarketingDataInsightsServiceClient(MarketingDataInsightsServiceStub stub)
    
    
    protected MarketingDataInsightsServiceClient(MarketingDataInsightsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MarketingDataInsightsServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.MarketingDataInsightsServiceStub)`  
  
  
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
    
    
    public final @Nullable MarketingDataInsightsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.MarketingDataInsightsServiceSettings` |   
  
### getStub()
    
    
    public MarketingDataInsightsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MarketingDataInsightsServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.MarketingDataInsightsServiceStub)` |   
  
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
  
### retrieveInsights(RetrieveInsightsRequest request)
    
    
    public final RetrieveInsightsResponse retrieveInsights(RetrieveInsightsRequest request)

Retrieves marketing data insights for a given user list.

This feature is only available to data partners.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create()) {
       RetrieveInsightsRequest request =
           RetrieveInsightsRequest.newBuilder()
               .setParent("parent-995424086")
               .setBaseline(Baseline.newBuilder().build())
               .setUserListId("userListId1381604868")
               .build();
       RetrieveInsightsResponse response =
           marketingDataInsightsServiceClient.retrieveInsights(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveInsightsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveInsightsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveInsightsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveInsightsResponse)` |   
  
### retrieveInsightsCallable()
    
    
    public final UnaryCallable<RetrieveInsightsRequest,RetrieveInsightsResponse> retrieveInsightsCallable()

Retrieves marketing data insights for a given user list.

This feature is only available to data partners.

Authorization Headers:

This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`
  * `linked-account`: (Optional) The resource name of the account with an established product link to the `login-account`. Format: `accountTypes/{linkedAccountType}/accounts/{linkedAccountId}`



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingDataInsightsServiceClient marketingDataInsightsServiceClient =
         MarketingDataInsightsServiceClient.create()) {
       RetrieveInsightsRequest request =
           RetrieveInsightsRequest.newBuilder()
               .setParent("parent-995424086")
               .setBaseline(Baseline.newBuilder().build())
               .setUserListId("userListId1381604868")
               .build();
       ApiFuture<RetrieveInsightsResponse> future =
           marketingDataInsightsServiceClient.retrieveInsightsCallable().futureCall(request);
       // Do something.
       RetrieveInsightsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveInsightsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveInsightsRequest),[RetrieveInsightsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveInsightsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
