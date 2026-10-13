---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceClient
title: Class CompletionServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:25.935733+00:00
---

# Class CompletionServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompletionServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/CompletionServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for Auto-Completion.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setQuery("query107944136")
               .setQueryModel("queryModel-184930495")
               .setUserPseudoId("userPseudoId-1155274652")
               .setIncludeTailSuggestions(true)
               .build();
       CompleteQueryResponse response = completionServiceClient.completeQuery(request);
     }
     

Note: close() needs to be called on the CompletionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CompleteQuery |  Completes the specified user input with keyword suggestions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeQuery(CompleteQueryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeQueryCallable() 

  
ImportSuggestionDenyListEntries |  Imports all SuggestionDenyListEntry for a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importSuggestionDenyListEntriesAsync(ImportSuggestionDenyListEntriesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importSuggestionDenyListEntriesOperationCallable() 
  * importSuggestionDenyListEntriesCallable() 

  
PurgeSuggestionDenyListEntries |  Permanently deletes all SuggestionDenyListEntry for a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeSuggestionDenyListEntriesAsync(PurgeSuggestionDenyListEntriesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeSuggestionDenyListEntriesOperationCallable() 
  * purgeSuggestionDenyListEntriesCallable() 

  
ImportCompletionSuggestions |  Imports CompletionSuggestions for a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importCompletionSuggestionsAsync(ImportCompletionSuggestionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importCompletionSuggestionsOperationCallable() 
  * importCompletionSuggestionsCallable() 

  
PurgeCompletionSuggestions |  Permanently deletes all CompletionSuggestions for a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeCompletionSuggestionsAsync(PurgeCompletionSuggestionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeCompletionSuggestionsOperationCallable() 
  * purgeCompletionSuggestionsCallable() 

  
  
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
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceClient)` |   
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
`settings` | `[CompletionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceClient)` |   
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
`stub` | `[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CompletionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceClient)` |   
  
## Constructors 

### CompletionServiceClient(CompletionServiceSettings settings)
    
    
    protected CompletionServiceClient(CompletionServiceSettings settings)

Constructs an instance of CompletionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompletionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompletionServiceSettings)`  
  
  
### CompletionServiceClient(CompletionServiceStub stub)
    
    
    protected CompletionServiceClient(CompletionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CompletionServiceStub)`  
  
  
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

Completes the specified user input with keyword suggestions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setQuery("query107944136")
               .setQueryModel("queryModel-184930495")
               .setUserPseudoId("userPseudoId-1155274652")
               .setIncludeTailSuggestions(true)
               .build();
       CompleteQueryResponse response = completionServiceClient.completeQuery(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompleteQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompleteQueryResponse)` |   
  
### completeQueryCallable()
    
    
    public final UnaryCallable<CompleteQueryRequest,CompleteQueryResponse> completeQueryCallable()

Completes the specified user input with keyword suggestions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setQuery("query107944136")
               .setQueryModel("queryModel-184930495")
               .setUserPseudoId("userPseudoId-1155274652")
               .setIncludeTailSuggestions(true)
               .build();
       ApiFuture<CompleteQueryResponse> future =
           completionServiceClient.completeQueryCallable().futureCall(request);
       // Do something.
       CompleteQueryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompleteQueryRequest),[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CompleteQueryResponse)>` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CompletionServiceSettings` |   
  
### getStub()
    
    
    public CompletionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompletionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CompletionServiceStub)` |   
  
### importCompletionSuggestionsAsync(ImportCompletionSuggestionsRequest request)
    
    
    public final OperationFuture<ImportCompletionSuggestionsResponse,ImportCompletionSuggestionsMetadata> importCompletionSuggestionsAsync(ImportCompletionSuggestionsRequest request)

Imports CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionSuggestionsRequest request =
           ImportCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       ImportCompletionSuggestionsResponse response =
           completionServiceClient.importCompletionSuggestionsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsResponse),[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsMetadata)>` |   
  
### importCompletionSuggestionsCallable()
    
    
    public final UnaryCallable<ImportCompletionSuggestionsRequest,Operation> importCompletionSuggestionsCallable()

Imports CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionSuggestionsRequest request =
           ImportCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           completionServiceClient.importCompletionSuggestionsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importCompletionSuggestionsOperationCallable()
    
    
    public final OperationCallable<ImportCompletionSuggestionsRequest,ImportCompletionSuggestionsResponse,ImportCompletionSuggestionsMetadata> importCompletionSuggestionsOperationCallable()

Imports CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportCompletionSuggestionsRequest request =
           ImportCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .build();
       OperationFuture<ImportCompletionSuggestionsResponse, ImportCompletionSuggestionsMetadata>
           future =
               completionServiceClient
                   .importCompletionSuggestionsOperationCallable()
                   .futureCall(request);
       // Do something.
       ImportCompletionSuggestionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsRequest),[ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsResponse),[ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsMetadata)>` |   
  
### importSuggestionDenyListEntriesAsync(ImportSuggestionDenyListEntriesRequest request)
    
    
    public final OperationFuture<ImportSuggestionDenyListEntriesResponse,ImportSuggestionDenyListEntriesMetadata> importSuggestionDenyListEntriesAsync(ImportSuggestionDenyListEntriesRequest request)

Imports all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportSuggestionDenyListEntriesRequest request =
           ImportSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ImportSuggestionDenyListEntriesResponse response =
           completionServiceClient.importSuggestionDenyListEntriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesResponse),[ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesMetadata)>` |   
  
### importSuggestionDenyListEntriesCallable()
    
    
    public final UnaryCallable<ImportSuggestionDenyListEntriesRequest,Operation> importSuggestionDenyListEntriesCallable()

Imports all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportSuggestionDenyListEntriesRequest request =
           ImportSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           completionServiceClient.importSuggestionDenyListEntriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importSuggestionDenyListEntriesOperationCallable()
    
    
    public final OperationCallable<ImportSuggestionDenyListEntriesRequest,ImportSuggestionDenyListEntriesResponse,ImportSuggestionDenyListEntriesMetadata> importSuggestionDenyListEntriesOperationCallable()

Imports all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       ImportSuggestionDenyListEntriesRequest request =
           ImportSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture< importsuggestiondenylistentriesresponse,="" importsuggestiondenylistentriesmetadata="">
           future =
               completionServiceClient
                   .importSuggestionDenyListEntriesOperationCallable()
                   .futureCall(request);
       // Do something.
       ImportSuggestionDenyListEntriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesRequest),[ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesResponse),[ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesMetadata)>` |   
  
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
  
### purgeCompletionSuggestionsAsync(PurgeCompletionSuggestionsRequest request)
    
    
    public final OperationFuture<PurgeCompletionSuggestionsResponse,PurgeCompletionSuggestionsMetadata> purgeCompletionSuggestionsAsync(PurgeCompletionSuggestionsRequest request)

Permanently deletes all CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeCompletionSuggestionsRequest request =
           PurgeCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       PurgeCompletionSuggestionsResponse response =
           completionServiceClient.purgeCompletionSuggestionsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeCompletionSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsResponse),[PurgeCompletionSuggestionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsMetadata)>` |   
  
### purgeCompletionSuggestionsCallable()
    
    
    public final UnaryCallable<PurgeCompletionSuggestionsRequest,Operation> purgeCompletionSuggestionsCallable()

Permanently deletes all CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeCompletionSuggestionsRequest request =
           PurgeCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           completionServiceClient.purgeCompletionSuggestionsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeCompletionSuggestionsOperationCallable()
    
    
    public final OperationCallable<PurgeCompletionSuggestionsRequest,PurgeCompletionSuggestionsResponse,PurgeCompletionSuggestionsMetadata> purgeCompletionSuggestionsOperationCallable()

Permanently deletes all CompletionSuggestions for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeCompletionSuggestionsRequest request =
           PurgeCompletionSuggestionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture<PurgeCompletionSuggestionsResponse, PurgeCompletionSuggestionsMetadata>
           future =
               completionServiceClient
                   .purgeCompletionSuggestionsOperationCallable()
                   .futureCall(request);
       // Do something.
       PurgeCompletionSuggestionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsRequest),[PurgeCompletionSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsResponse),[PurgeCompletionSuggestionsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsMetadata)>` |   
  
### purgeSuggestionDenyListEntriesAsync(PurgeSuggestionDenyListEntriesRequest request)
    
    
    public final OperationFuture<PurgeSuggestionDenyListEntriesResponse,PurgeSuggestionDenyListEntriesMetadata> purgeSuggestionDenyListEntriesAsync(PurgeSuggestionDenyListEntriesRequest request)

Permanently deletes all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeSuggestionDenyListEntriesRequest request =
           PurgeSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       PurgeSuggestionDenyListEntriesResponse response =
           completionServiceClient.purgeSuggestionDenyListEntriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesResponse),[PurgeSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesMetadata)>` |   
  
### purgeSuggestionDenyListEntriesCallable()
    
    
    public final UnaryCallable<PurgeSuggestionDenyListEntriesRequest,Operation> purgeSuggestionDenyListEntriesCallable()

Permanently deletes all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeSuggestionDenyListEntriesRequest request =
           PurgeSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           completionServiceClient.purgeSuggestionDenyListEntriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeSuggestionDenyListEntriesOperationCallable()
    
    
    public final OperationCallable<PurgeSuggestionDenyListEntriesRequest,PurgeSuggestionDenyListEntriesResponse,PurgeSuggestionDenyListEntriesMetadata> purgeSuggestionDenyListEntriesOperationCallable()

Permanently deletes all SuggestionDenyListEntry for a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
       PurgeSuggestionDenyListEntriesRequest request =
           PurgeSuggestionDenyListEntriesRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture< purgesuggestiondenylistentriesresponse,="" purgesuggestiondenylistentriesmetadata="">
           future =
               completionServiceClient
                   .purgeSuggestionDenyListEntriesOperationCallable()
                   .futureCall(request);
       // Do something.
       PurgeSuggestionDenyListEntriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesRequest),[PurgeSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesResponse),[PurgeSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeSuggestionDenyListEntriesMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
