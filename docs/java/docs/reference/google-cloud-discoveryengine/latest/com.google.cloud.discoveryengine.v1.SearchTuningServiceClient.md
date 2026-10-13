---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceClient
title: Class SearchTuningServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:46.174565+00:00
---

# Class SearchTuningServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SearchTuningServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/SearchTuningServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for search tuning.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       ListCustomModelsRequest request =
           ListCustomModelsRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ListCustomModelsResponse response = searchTuningServiceClient.listCustomModels(request);
     }
     

Note: close() needs to be called on the SearchTuningServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
TrainCustomModel |  Trains a custom model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * trainCustomModelAsync(TrainCustomModelRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * trainCustomModelOperationCallable() 
  * trainCustomModelCallable() 

  
ListCustomModels |  Gets a list of all the custom models. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomModels(ListCustomModelsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomModelsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SearchTuningServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchTuningServiceSettings searchTuningServiceSettings =
         SearchTuningServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SearchTuningServiceClient searchTuningServiceClient =
         SearchTuningServiceClient.create(searchTuningServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchTuningServiceSettings searchTuningServiceSettings =
         SearchTuningServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SearchTuningServiceClient searchTuningServiceClient =
         SearchTuningServiceClient.create(searchTuningServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SearchTuningServiceSettings searchTuningServiceSettings =
         SearchTuningServiceSettings.newHttpJsonBuilder().build();
     SearchTuningServiceClient searchTuningServiceClient =
         SearchTuningServiceClient.create(searchTuningServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SearchTuningServiceClient

## Static Methods 

### create()
    
    
    public static final SearchTuningServiceClient create()

Constructs an instance of SearchTuningServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SearchTuningServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SearchTuningServiceSettings settings)
    
    
    public static final SearchTuningServiceClient create(SearchTuningServiceSettings settings)

Constructs an instance of SearchTuningServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SearchTuningServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchTuningServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SearchTuningServiceStub stub)
    
    
    public static final SearchTuningServiceClient create(SearchTuningServiceStub stub)

Constructs an instance of SearchTuningServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SearchTuningServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SearchTuningServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchTuningServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchTuningServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceClient)` |   
  
## Constructors 

### SearchTuningServiceClient(SearchTuningServiceSettings settings)
    
    
    protected SearchTuningServiceClient(SearchTuningServiceSettings settings)

Constructs an instance of SearchTuningServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SearchTuningServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchTuningServiceSettings)`  
  
  
### SearchTuningServiceClient(SearchTuningServiceStub stub)
    
    
    protected SearchTuningServiceClient(SearchTuningServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SearchTuningServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchTuningServiceStub)`  
  
  
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
    
    
    public final @Nullable SearchTuningServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SearchTuningServiceSettings` |   
  
### getStub()
    
    
    public SearchTuningServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SearchTuningServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SearchTuningServiceStub)` |   
  
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
  
### listCustomModels(ListCustomModelsRequest request)
    
    
    public final ListCustomModelsResponse listCustomModels(ListCustomModelsRequest request)

Gets a list of all the custom models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       ListCustomModelsRequest request =
           ListCustomModelsRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ListCustomModelsResponse response = searchTuningServiceClient.listCustomModels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCustomModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCustomModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCustomModelsResponse)` |   
  
### listCustomModelsCallable()
    
    
    public final UnaryCallable<ListCustomModelsRequest,ListCustomModelsResponse> listCustomModelsCallable()

Gets a list of all the custom models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       ListCustomModelsRequest request =
           ListCustomModelsRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<ListCustomModelsResponse> future =
           searchTuningServiceClient.listCustomModelsCallable().futureCall(request);
       // Do something.
       ListCustomModelsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCustomModelsRequest),[ListCustomModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCustomModelsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### trainCustomModelAsync(TrainCustomModelRequest request)
    
    
    public final OperationFuture<TrainCustomModelResponse,TrainCustomModelMetadata> trainCustomModelAsync(TrainCustomModelRequest request)

Trains a custom model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       TrainCustomModelRequest request =
           TrainCustomModelRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setModelType("modelType-2010627581")
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setModelId("modelId1226956324")
               .build();
       TrainCustomModelResponse response =
           searchTuningServiceClient.trainCustomModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TrainCustomModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TrainCustomModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelResponse),[TrainCustomModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelMetadata)>` |   
  
### trainCustomModelCallable()
    
    
    public final UnaryCallable<TrainCustomModelRequest,Operation> trainCustomModelCallable()

Trains a custom model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       TrainCustomModelRequest request =
           TrainCustomModelRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setModelType("modelType-2010627581")
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setModelId("modelId1226956324")
               .build();
       ApiFuture<Operation> future =
           searchTuningServiceClient.trainCustomModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TrainCustomModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### trainCustomModelOperationCallable()
    
    
    public final OperationCallable<TrainCustomModelRequest,TrainCustomModelResponse,TrainCustomModelMetadata> trainCustomModelOperationCallable()

Trains a custom model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.create()) {
       TrainCustomModelRequest request =
           TrainCustomModelRequest.newBuilder()
               .setDataStore(
                   DataStoreName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setModelType("modelType-2010627581")
               .setErrorConfig(ImportErrorConfig.newBuilder().build())
               .setModelId("modelId1226956324")
               .build();
       OperationFuture<TrainCustomModelResponse, TrainCustomModelMetadata> future =
           searchTuningServiceClient.trainCustomModelOperationCallable().futureCall(request);
       // Do something.
       TrainCustomModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TrainCustomModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelRequest),[TrainCustomModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelResponse),[TrainCustomModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TrainCustomModelMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
