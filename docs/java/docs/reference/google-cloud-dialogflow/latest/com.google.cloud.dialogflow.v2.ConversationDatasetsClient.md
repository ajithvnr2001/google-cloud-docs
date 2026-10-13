---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient
title: Class ConversationDatasetsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:35.759465+00:00
---

# Class ConversationDatasetsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationDatasetsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/ConversationDatasetsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Conversation datasets.

Conversation datasets contain raw conversation files and their customizable metadata that can be used for model training.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ConversationDatasetName name =
           ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]");
       ConversationDataset response = conversationDatasetsClient.getConversationDataset(name);
     }
     

Note: close() needs to be called on the ConversationDatasetsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateConversationDataset |  Creates a new conversation dataset.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: CreateConversationDatasetOperationMetadata \- `response`: ConversationDataset |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversationDatasetAsync(CreateConversationDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConversationDatasetAsync(String parent, ConversationDataset conversationDataset) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationDatasetOperationCallable() 
  * createConversationDatasetCallable() 

  
GetConversationDataset |  Retrieves the specified conversation dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversationDataset(GetConversationDatasetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversationDataset(ConversationDatasetName name) 
  * getConversationDataset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationDatasetCallable() 

  
ListConversationDatasets |  Returns the list of all conversation datasets in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversationDatasets(ListConversationDatasetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversationDatasets(LocationName parent) 
  * listConversationDatasets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationDatasetsPagedCallable() 
  * listConversationDatasetsCallable() 

  
DeleteConversationDataset |  Deletes the specified conversation dataset.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: DeleteConversationDatasetOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversationDatasetAsync(DeleteConversationDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteConversationDatasetAsync(ConversationDatasetName name) 
  * deleteConversationDatasetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversationDatasetOperationCallable() 
  * deleteConversationDatasetCallable() 

  
ImportConversationData |  Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: ImportConversationDataOperationMetadata \- `response`: ImportConversationDataOperationResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importConversationDataAsync(ImportConversationDataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importConversationDataOperationCallable() 
  * importConversationDataCallable() 

  
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

This class can be customized by passing in a custom instance of ConversationDatasetsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationDatasetsSettings conversationDatasetsSettings =
         ConversationDatasetsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create(conversationDatasetsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationDatasetsSettings conversationDatasetsSettings =
         ConversationDatasetsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create(conversationDatasetsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationDatasetsSettings conversationDatasetsSettings =
         ConversationDatasetsSettings.newHttpJsonBuilder().build();
     ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create(conversationDatasetsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationDatasetsClient

## Static Methods 

### create()
    
    
    public static final ConversationDatasetsClient create()

Constructs an instance of ConversationDatasetsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationDatasetsSettings settings)
    
    
    public static final ConversationDatasetsClient create(ConversationDatasetsSettings settings)

Constructs an instance of ConversationDatasetsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationDatasetsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationDatasetsStub stub)
    
    
    public static final ConversationDatasetsClient create(ConversationDatasetsStub stub)

Constructs an instance of ConversationDatasetsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationDatasetsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationDatasetsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationDatasetsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient)` |   
  
## Constructors 

### ConversationDatasetsClient(ConversationDatasetsSettings settings)
    
    
    protected ConversationDatasetsClient(ConversationDatasetsSettings settings)

Constructs an instance of ConversationDatasetsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationDatasetsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsSettings)`  
  
  
### ConversationDatasetsClient(ConversationDatasetsStub stub)
    
    
    protected ConversationDatasetsClient(ConversationDatasetsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationDatasetsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationDatasetsStub)`  
  
  
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

### createConversationDatasetAsync(CreateConversationDatasetRequest request)
    
    
    public final OperationFuture<ConversationDataset,CreateConversationDatasetOperationMetadata> createConversationDatasetAsync(CreateConversationDatasetRequest request)

Creates a new conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationDatasetOperationMetadata

  * `response`: ConversationDataset

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        CreateConversationDatasetRequest request =
            CreateConversationDatasetRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationDataset(ConversationDataset.newBuilder().build())
                .build();
        ConversationDataset response =
            conversationDatasetsClient.createConversationDatasetAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset),[CreateConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetOperationMetadata)>` |   
  
### createConversationDatasetAsync(String parent, ConversationDataset conversationDataset)
    
    
    public final OperationFuture<ConversationDataset,CreateConversationDatasetOperationMetadata> createConversationDatasetAsync(String parent, ConversationDataset conversationDataset)

Creates a new conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationDatasetOperationMetadata

  * `response`: ConversationDataset

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        String parent = "parent-995424086";
        ConversationDataset conversationDataset = ConversationDataset.newBuilder().build();
        ConversationDataset response =
            conversationDatasetsClient
                .createConversationDatasetAsync(parent, conversationDataset)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to create conversation dataset for. Format: `projects/<Project ID>/locations/<Location ID>`  
`conversationDataset` | `[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset)`  
Required. The conversation dataset to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset),[CreateConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetOperationMetadata)>` |   
  
### createConversationDatasetCallable()
    
    
    public final UnaryCallable<CreateConversationDatasetRequest,Operation> createConversationDatasetCallable()

Creates a new conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationDatasetOperationMetadata

  * `response`: ConversationDataset

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        CreateConversationDatasetRequest request =
            CreateConversationDatasetRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationDataset(ConversationDataset.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            conversationDatasetsClient.createConversationDatasetCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConversationDatasetOperationCallable()
    
    
    public final OperationCallable<CreateConversationDatasetRequest,ConversationDataset,CreateConversationDatasetOperationMetadata> createConversationDatasetOperationCallable()

Creates a new conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationDatasetOperationMetadata

  * `response`: ConversationDataset

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        CreateConversationDatasetRequest request =
            CreateConversationDatasetRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationDataset(ConversationDataset.newBuilder().build())
                .build();
        OperationFuture<ConversationDataset, CreateConversationDatasetOperationMetadata> future =
            conversationDatasetsClient
                .createConversationDatasetOperationCallable()
                .futureCall(request);
        // Do something.
        ConversationDataset response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetRequest),[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset),[CreateConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationDatasetOperationMetadata)>` |   
  
### deleteConversationDatasetAsync(@Nullable ConversationDatasetName name)
    
    
    public final OperationFuture<Empty,DeleteConversationDatasetOperationMetadata> deleteConversationDatasetAsync(@Nullable ConversationDatasetName name)

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationDatasetOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        ConversationDatasetName name =
            ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]");
        conversationDatasetsClient.deleteConversationDatasetAsync(name).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationDatasetName`  
Required. The conversation dataset to delete. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetOperationMetadata)>` |   
  
### deleteConversationDatasetAsync(DeleteConversationDatasetRequest request)
    
    
    public final OperationFuture<Empty,DeleteConversationDatasetOperationMetadata> deleteConversationDatasetAsync(DeleteConversationDatasetRequest request)

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationDatasetOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        DeleteConversationDatasetRequest request =
            DeleteConversationDatasetRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .build();
        conversationDatasetsClient.deleteConversationDatasetAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetOperationMetadata)>` |   
  
### deleteConversationDatasetAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteConversationDatasetOperationMetadata> deleteConversationDatasetAsync(String name)

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationDatasetOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        String name =
            ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                .toString();
        conversationDatasetsClient.deleteConversationDatasetAsync(name).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation dataset to delete. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetOperationMetadata)>` |   
  
### deleteConversationDatasetCallable()
    
    
    public final UnaryCallable<DeleteConversationDatasetRequest,Operation> deleteConversationDatasetCallable()

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationDatasetOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        DeleteConversationDatasetRequest request =
            DeleteConversationDatasetRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .build();
        ApiFuture<Operation> future =
            conversationDatasetsClient.deleteConversationDatasetCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConversationDatasetOperationCallable()
    
    
    public final OperationCallable<DeleteConversationDatasetRequest,Empty,DeleteConversationDatasetOperationMetadata> deleteConversationDatasetOperationCallable()

Deletes the specified conversation dataset.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationDatasetOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        DeleteConversationDatasetRequest request =
            DeleteConversationDatasetRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .build();
        OperationFuture<Empty, DeleteConversationDatasetOperationMetadata> future =
            conversationDatasetsClient
                .deleteConversationDatasetOperationCallable()
                .futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationDatasetOperationMetadata)>` |   
  
### getConversationDataset(@Nullable ConversationDatasetName name)
    
    
    public final ConversationDataset getConversationDataset(@Nullable ConversationDatasetName name)

Retrieves the specified conversation dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ConversationDatasetName name =
           ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]");
       ConversationDataset response = conversationDatasetsClient.getConversationDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationDatasetName`  
Required. The conversation dataset to retrieve. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset)` |   
  
### getConversationDataset(GetConversationDatasetRequest request)
    
    
    public final ConversationDataset getConversationDataset(GetConversationDatasetRequest request)

Retrieves the specified conversation dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       GetConversationDatasetRequest request =
           GetConversationDatasetRequest.newBuilder()
               .setName(
                   ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                       .toString())
               .build();
       ConversationDataset response = conversationDatasetsClient.getConversationDataset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset)` |   
  
### getConversationDataset(String name)
    
    
    public final ConversationDataset getConversationDataset(String name)

Retrieves the specified conversation dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       String name =
           ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
               .toString();
       ConversationDataset response = conversationDatasetsClient.getConversationDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation dataset to retrieve. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset)` |   
  
### getConversationDatasetCallable()
    
    
    public final UnaryCallable<GetConversationDatasetRequest,ConversationDataset> getConversationDatasetCallable()

Retrieves the specified conversation dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       GetConversationDatasetRequest request =
           GetConversationDatasetRequest.newBuilder()
               .setName(
                   ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                       .toString())
               .build();
       ApiFuture<ConversationDataset> future =
           conversationDatasetsClient.getConversationDatasetCallable().futureCall(request);
       // Do something.
       ConversationDataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationDatasetRequest),[ConversationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDataset)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = conversationDatasetsClient.getLocation(request);
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
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           conversationDatasetsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable ConversationDatasetsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationDatasetsSettings` |   
  
### getStub()
    
    
    public ConversationDatasetsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationDatasetsStub)` |   
  
### importConversationDataAsync(ImportConversationDataRequest request)
    
    
    public final OperationFuture<ImportConversationDataOperationResponse,ImportConversationDataOperationMetadata> importConversationDataAsync(ImportConversationDataRequest request)

Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportConversationDataOperationMetadata

  * `response`: ImportConversationDataOperationResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        ImportConversationDataRequest request =
            ImportConversationDataRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .setInputConfig(InputConfig.newBuilder().build())
                .build();
        ImportConversationDataOperationResponse response =
            conversationDatasetsClient.importConversationDataAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportConversationDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportConversationDataOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataOperationResponse),[ImportConversationDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataOperationMetadata)>` |   
  
### importConversationDataCallable()
    
    
    public final UnaryCallable<ImportConversationDataRequest,Operation> importConversationDataCallable()

Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportConversationDataOperationMetadata

  * `response`: ImportConversationDataOperationResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        ImportConversationDataRequest request =
            ImportConversationDataRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .setInputConfig(InputConfig.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            conversationDatasetsClient.importConversationDataCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportConversationDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importConversationDataOperationCallable()
    
    
    public final OperationCallable<ImportConversationDataRequest,ImportConversationDataOperationResponse,ImportConversationDataOperationMetadata> importConversationDataOperationCallable()

Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportConversationDataOperationMetadata

  * `response`: ImportConversationDataOperationResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationDatasetsClient conversationDatasetsClient =
          ConversationDatasetsClient.create()) {
        ImportConversationDataRequest request =
            ImportConversationDataRequest.newBuilder()
                .setName(
                    ConversationDatasetName.of("[PROJECT]", "[LOCATION]", "[CONVERSATION_DATASET]")
                        .toString())
                .setInputConfig(InputConfig.newBuilder().build())
                .build();
        OperationFuture< importconversationdataoperationresponse,="" importconversationdataoperationmetadata="">
            future =
                conversationDatasetsClient
                    .importConversationDataOperationCallable()
                    .futureCall(request);
        // Do something.
        ImportConversationDataOperationResponse response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportConversationDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataRequest),[ImportConversationDataOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataOperationResponse),[ImportConversationDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ImportConversationDataOperationMetadata)>` |   
  
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
  
### listConversationDatasets(@Nullable LocationName parent)
    
    
    public final ConversationDatasetsClient.ListConversationDatasetsPagedResponse listConversationDatasets(@Nullable LocationName parent)

Returns the list of all conversation datasets in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ConversationDataset element :
           conversationDatasetsClient.listConversationDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project and location name to list all conversation datasets for. Format: `projects/<Project ID>/locations/<Location ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient.ListConversationDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListConversationDatasetsPagedResponse)` |   
  
### listConversationDatasets(ListConversationDatasetsRequest request)
    
    
    public final ConversationDatasetsClient.ListConversationDatasetsPagedResponse listConversationDatasets(ListConversationDatasetsRequest request)

Returns the list of all conversation datasets in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListConversationDatasetsRequest request =
           ListConversationDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ConversationDataset element :
           conversationDatasetsClient.listConversationDatasets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationDatasetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient.ListConversationDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListConversationDatasetsPagedResponse)` |   
  
### listConversationDatasets(String parent)
    
    
    public final ConversationDatasetsClient.ListConversationDatasetsPagedResponse listConversationDatasets(String parent)

Returns the list of all conversation datasets in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ConversationDataset element :
           conversationDatasetsClient.listConversationDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location name to list all conversation datasets for. Format: `projects/<Project ID>/locations/<Location ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationDatasetsClient.ListConversationDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListConversationDatasetsPagedResponse)` |   
  
### listConversationDatasetsCallable()
    
    
    public final UnaryCallable<ListConversationDatasetsRequest,ListConversationDatasetsResponse> listConversationDatasetsCallable()

Returns the list of all conversation datasets in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListConversationDatasetsRequest request =
           ListConversationDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListConversationDatasetsResponse response =
             conversationDatasetsClient.listConversationDatasetsCallable().call(request);
         for (ConversationDataset element : response.getConversationDatasetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationDatasetsRequest),[ListConversationDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationDatasetsResponse)>` |   
  
### listConversationDatasetsPagedCallable()
    
    
    public final UnaryCallable<ListConversationDatasetsRequest,ConversationDatasetsClient.ListConversationDatasetsPagedResponse> listConversationDatasetsPagedCallable()

Returns the list of all conversation datasets in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListConversationDatasetsRequest request =
           ListConversationDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ConversationDataset> future =
           conversationDatasetsClient.listConversationDatasetsPagedCallable().futureCall(request);
       // Do something.
       for (ConversationDataset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationDatasetsRequest),[ListConversationDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListConversationDatasetsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ConversationDatasetsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : conversationDatasetsClient.listLocations(request).iterateAll()) {
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
`[ConversationDatasetsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListLocationsPagedResponse)` |   
  
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
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             conversationDatasetsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ConversationDatasetsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationDatasetsClient conversationDatasetsClient =
         ConversationDatasetsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           conversationDatasetsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationDatasetsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
