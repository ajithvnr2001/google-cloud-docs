---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceClient
title: Class CompletionServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:00.504515+00:00
---

# Class CompletionServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompletionServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2alpha/CompletionServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Autocomplete service for retail.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .addAllLanguageCodes(new ArrayList<String>())
               .setDeviceType("deviceType781190832")
               .setDataset("dataset1443214456")
               .setMaxSuggestions(618824852)
               .setEnableAttributeSuggestions(true)
               .setEntity("entity-1298275357")
               .build();
       CompleteQueryResponse response = completionServiceClient.completeQuery(request);
     }
     

Note: close() needs to be called on the CompletionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CompleteQuery |  Completes the specified prefix with keyword suggestions.  This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeQuery(CompleteQueryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeQueryCallable() 

  
ImportCompletionData |  Bulk import of processed completion dataset.  Request processing is asynchronous. Partial updating is not supported.  The operation is successfully finished only after the imported suggestions are indexed successfully and ready for serving. The process takes hours.  This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importCompletionDataAsync(ImportCompletionDataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importCompletionDataOperationCallable() 
  * importCompletionDataCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CompletionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionServiceSettings completionServiceSettings =
         CompletionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CompletionServiceClient completionServiceClient =
         CompletionServiceClient.create(completionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionServiceSettings completionServiceSettings =
         CompletionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CompletionServiceClient completionServiceClient =
         CompletionServiceClient.create(completionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionServiceSettings completionServiceSettings =
         CompletionServiceSettings.newHttpJsonBuilder().build();
     CompletionServiceClient completionServiceClient =
         CompletionServiceClient.create(completionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CompletionServiceClient

## Static Methods 

### create()
    
    
    public static final CompletionServiceClient create()

Constructs an instance of CompletionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompletionServiceSettings settings)
    
    
    public static final CompletionServiceClient create(CompletionServiceSettings settings)

Constructs an instance of CompletionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompletionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompletionServiceStub stub)
    
    
    public static final CompletionServiceClient create(CompletionServiceStub stub)

Constructs an instance of CompletionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CompletionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.CompletionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceClient)` |   
  
## Constructors 

### CompletionServiceClient(CompletionServiceSettings settings)
    
    
    protected CompletionServiceClient(CompletionServiceSettings settings)

Constructs an instance of CompletionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompletionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompletionServiceSettings)`  
  
  
### CompletionServiceClient(CompletionServiceStub stub)
    
    
    protected CompletionServiceClient(CompletionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.CompletionServiceStub)`  
  
  
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

### completeQuery(CompleteQueryRequest request)
    
    
    public final CompleteQueryResponse completeQuery(CompleteQueryRequest request)

Completes the specified prefix with keyword suggestions.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .addAllLanguageCodes(new ArrayList<String>())
               .setDeviceType("deviceType781190832")
               .setDataset("dataset1443214456")
               .setMaxSuggestions(618824852)
               .setEnableAttributeSuggestions(true)
               .setEntity("entity-1298275357")
               .build();
       CompleteQueryResponse response = completionServiceClient.completeQuery(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompleteQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompleteQueryResponse)` |   
  
### completeQueryCallable()
    
    
    public final UnaryCallable<CompleteQueryRequest,CompleteQueryResponse> completeQueryCallable()

Completes the specified prefix with keyword suggestions.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setQuery("query107944136")
               .setVisitorId("visitorId1880545833")
               .addAllLanguageCodes(new ArrayList<String>())
               .setDeviceType("deviceType781190832")
               .setDataset("dataset1443214456")
               .setMaxSuggestions(618824852)
               .setEnableAttributeSuggestions(true)
               .setEntity("entity-1298275357")
               .build();
       ApiFuture<CompleteQueryResponse> future =
           completionServiceClient.completeQueryCallable().futureCall(request);
       // Do something.
       CompleteQueryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompleteQueryRequest),[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.CompleteQueryResponse)>` |   
  
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
    
    
    public final @Nullable CompletionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2alpha.CompletionServiceSettings` |   
  
### getStub()
    
    
    public CompletionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.CompletionServiceStub)` |   
  
### importCompletionDataAsync(ImportCompletionDataRequest request)
    
    
    public final OperationFuture<ImportCompletionDataResponse,ImportMetadata> importCompletionDataAsync(ImportCompletionDataRequest request)

Bulk import of processed completion dataset.

Request processing is asynchronous. Partial updating is not supported.

The operation is successfully finished only after the imported suggestions are indexed successfully and ready for serving. The process takes hours.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionDataRequest request =
           ImportCompletionDataRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(CompletionDataInputConfig.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       ImportCompletionDataResponse response =
           completionServiceClient.importCompletionDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportCompletionDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportCompletionDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportCompletionDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportCompletionDataResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportMetadata)>` |   
  
### importCompletionDataCallable()
    
    
    public final UnaryCallable<ImportCompletionDataRequest,Operation> importCompletionDataCallable()

Bulk import of processed completion dataset.

Request processing is asynchronous. Partial updating is not supported.

The operation is successfully finished only after the imported suggestions are indexed successfully and ready for serving. The process takes hours.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionDataRequest request =
           ImportCompletionDataRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(CompletionDataInputConfig.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       ApiFuture<Operation> future =
           completionServiceClient.importCompletionDataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportCompletionDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportCompletionDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importCompletionDataOperationCallable()
    
    
    public final OperationCallable<ImportCompletionDataRequest,ImportCompletionDataResponse,ImportMetadata> importCompletionDataOperationCallable()

Bulk import of processed completion dataset.

Request processing is asynchronous. Partial updating is not supported.

The operation is successfully finished only after the imported suggestions are indexed successfully and ready for serving. The process takes hours.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionDataRequest request =
           ImportCompletionDataRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setInputConfig(CompletionDataInputConfig.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       OperationFuture<ImportCompletionDataResponse, ImportMetadata> future =
           completionServiceClient.importCompletionDataOperationCallable().futureCall(request);
       // Do something.
       ImportCompletionDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportCompletionDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportCompletionDataRequest),[ImportCompletionDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportCompletionDataResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ImportMetadata)>` |   
  
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
