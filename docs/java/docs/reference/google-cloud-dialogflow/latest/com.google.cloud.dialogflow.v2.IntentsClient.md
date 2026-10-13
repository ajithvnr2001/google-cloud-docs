---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient
title: Class IntentsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:47.058471+00:00
---

# Class IntentsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IntentsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/IntentsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing Intents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       IntentName name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]");
       Intent response = intentsClient.getIntent(name);
     }
     

Note: close() needs to be called on the IntentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListIntents |  Returns the list of all intents in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIntents(ListIntentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listIntents(AgentName parent) 
  * listIntents(String parent) 
  * listIntents(AgentName parent, String languageCode) 
  * listIntents(String parent, String languageCode) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIntentsPagedCallable() 
  * listIntentsCallable() 

  
GetIntent |  Retrieves the specified intent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIntent(GetIntentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIntent(IntentName name) 
  * getIntent(String name) 
  * getIntent(IntentName name, String languageCode) 
  * getIntent(String name, String languageCode) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIntentCallable() 

  
CreateIntent |  Creates an intent in the specified agent.  Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIntent(CreateIntentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createIntent(AgentName parent, Intent intent) 
  * createIntent(String parent, Intent intent) 
  * createIntent(AgentName parent, Intent intent, String languageCode) 
  * createIntent(String parent, Intent intent, String languageCode) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIntentCallable() 

  
UpdateIntent |  Updates the specified intent.  Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateIntent(UpdateIntentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateIntent(Intent intent, String languageCode) 
  * updateIntent(Intent intent, String languageCode, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateIntentCallable() 

  
DeleteIntent |  Deletes the specified intent and its direct or indirect followup intents.  Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIntent(DeleteIntentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteIntent(IntentName name) 
  * deleteIntent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIntentCallable() 

  
BatchUpdateIntents |  Updates/Creates multiple intents in the specified agent.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: BatchUpdateIntentsResponse Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateIntentsAsync(BatchUpdateIntentsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchUpdateIntentsAsync(AgentName parent, IntentBatch intentBatchInline) 
  * batchUpdateIntentsAsync(AgentName parent, String intentBatchUri) 
  * batchUpdateIntentsAsync(String parent, IntentBatch intentBatchInline) 
  * batchUpdateIntentsAsync(String parent, String intentBatchUri) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateIntentsOperationCallable() 
  * batchUpdateIntentsCallable() 

  
BatchDeleteIntents |  Deletes intents in the specified agent.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteIntentsAsync(BatchDeleteIntentsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchDeleteIntentsAsync(AgentName parent, List<Intent> intents) 
  * batchDeleteIntentsAsync(String parent, List<Intent> intents) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteIntentsOperationCallable() 
  * batchDeleteIntentsCallable() 

  
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

This class can be customized by passing in a custom instance of IntentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IntentsSettings intentsSettings =
         IntentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     IntentsClient intentsClient = IntentsClient.create(intentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IntentsSettings intentsSettings = IntentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     IntentsClient intentsClient = IntentsClient.create(intentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IntentsSettings intentsSettings = IntentsSettings.newHttpJsonBuilder().build();
     IntentsClient intentsClient = IntentsClient.create(intentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IntentsClient

## Static Methods 

### create()
    
    
    public static final IntentsClient create()

Constructs an instance of IntentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IntentsSettings settings)
    
    
    public static final IntentsClient create(IntentsSettings settings)

Constructs an instance of IntentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IntentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IntentsStub stub)
    
    
    public static final IntentsClient create(IntentsStub stub)

Constructs an instance of IntentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(IntentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IntentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.IntentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient)` |   
  
## Constructors 

### IntentsClient(IntentsSettings settings)
    
    
    protected IntentsClient(IntentsSettings settings)

Constructs an instance of IntentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IntentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsSettings)`  
  
  
### IntentsClient(IntentsStub stub)
    
    
    protected IntentsClient(IntentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IntentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.IntentsStub)`  
  
  
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
  
### batchDeleteIntentsAsync(@Nullable AgentName parent, List<Intent> intents)
    
    
    public final OperationFuture<Empty,Struct> batchDeleteIntentsAsync(@Nullable AgentName parent, List<Intent> intents)

Deletes intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        AgentName parent = AgentName.ofProjectName("[PROJECT]");
        List<Intent> intents = new ArrayList<>();
        intentsClient.batchDeleteIntentsAsync(parent, intents).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The name of the agent to delete all entities types for. Format: `projects/<Project ID>/agent`.  
`intents` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)>`  
Required. The collection of intents to delete. Only intent `name` must be filled in.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchDeleteIntentsAsync(BatchDeleteIntentsRequest request)
    
    
    public final OperationFuture<Empty,Struct> batchDeleteIntentsAsync(BatchDeleteIntentsRequest request)

Deletes intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchDeleteIntentsRequest request =
            BatchDeleteIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .addAllIntents(new ArrayList<Intent>())
                .build();
        intentsClient.batchDeleteIntentsAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchDeleteIntentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchDeleteIntentsAsync(String parent, List<Intent> intents)
    
    
    public final OperationFuture<Empty,Struct> batchDeleteIntentsAsync(String parent, List<Intent> intents)

Deletes intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        String parent = AgentName.ofProjectName("[PROJECT]").toString();
        List<Intent> intents = new ArrayList<>();
        intentsClient.batchDeleteIntentsAsync(parent, intents).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the agent to delete all entities types for. Format: `projects/<Project ID>/agent`.  
`intents` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)>`  
Required. The collection of intents to delete. Only intent `name` must be filled in.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchDeleteIntentsCallable()
    
    
    public final UnaryCallable<BatchDeleteIntentsRequest,Operation> batchDeleteIntentsCallable()

Deletes intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchDeleteIntentsRequest request =
            BatchDeleteIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .addAllIntents(new ArrayList<Intent>())
                .build();
        ApiFuture<Operation> future = intentsClient.batchDeleteIntentsCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchDeleteIntentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchDeleteIntentsOperationCallable()
    
    
    public final OperationCallable<BatchDeleteIntentsRequest,Empty,Struct> batchDeleteIntentsOperationCallable()

Deletes intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchDeleteIntentsRequest request =
            BatchDeleteIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .addAllIntents(new ArrayList<Intent>())
                .build();
        OperationFuture<Empty, Struct> future =
            intentsClient.batchDeleteIntentsOperationCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchDeleteIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchDeleteIntentsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsAsync(@Nullable AgentName parent, IntentBatch intentBatchInline)
    
    
    public final OperationFuture<BatchUpdateIntentsResponse,Struct> batchUpdateIntentsAsync(@Nullable AgentName parent, IntentBatch intentBatchInline)

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        AgentName parent = AgentName.ofProjectName("[PROJECT]");
        IntentBatch intentBatchInline = IntentBatch.newBuilder().build();
        BatchUpdateIntentsResponse response =
            intentsClient.batchUpdateIntentsAsync(parent, intentBatchInline).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The name of the agent to update or create intents in. Format: `projects/<Project ID>/agent`.  
`intentBatchInline` | `[IntentBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentBatch)`  
The collection of intents to update or create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsAsync(@Nullable AgentName parent, String intentBatchUri)
    
    
    public final OperationFuture<BatchUpdateIntentsResponse,Struct> batchUpdateIntentsAsync(@Nullable AgentName parent, String intentBatchUri)

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        AgentName parent = AgentName.ofProjectName("[PROJECT]");
        String intentBatchUri = "intentBatchUri544125582";
        BatchUpdateIntentsResponse response =
            intentsClient.batchUpdateIntentsAsync(parent, intentBatchUri).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The name of the agent to update or create intents in. Format: `projects/<Project ID>/agent`.  
`intentBatchUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The URI to a Google Cloud Storage file containing intents to update or create. The file format can either be a serialized proto (of IntentBatch type) or JSON object. Note: The URI must start with "gs://".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsAsync(BatchUpdateIntentsRequest request)
    
    
    public final OperationFuture<BatchUpdateIntentsResponse,Struct> batchUpdateIntentsAsync(BatchUpdateIntentsRequest request)

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchUpdateIntentsRequest request =
            BatchUpdateIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .setLanguageCode("languageCode-2092349083")
                .setUpdateMask(FieldMask.newBuilder().build())
                .setIntentView(IntentView.forNumber(0))
                .build();
        BatchUpdateIntentsResponse response = intentsClient.batchUpdateIntentsAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsAsync(String parent, IntentBatch intentBatchInline)
    
    
    public final OperationFuture<BatchUpdateIntentsResponse,Struct> batchUpdateIntentsAsync(String parent, IntentBatch intentBatchInline)

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        String parent = AgentName.ofProjectName("[PROJECT]").toString();
        IntentBatch intentBatchInline = IntentBatch.newBuilder().build();
        BatchUpdateIntentsResponse response =
            intentsClient.batchUpdateIntentsAsync(parent, intentBatchInline).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the agent to update or create intents in. Format: `projects/<Project ID>/agent`.  
`intentBatchInline` | `[IntentBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentBatch)`  
The collection of intents to update or create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsAsync(String parent, String intentBatchUri)
    
    
    public final OperationFuture<BatchUpdateIntentsResponse,Struct> batchUpdateIntentsAsync(String parent, String intentBatchUri)

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        String parent = AgentName.ofProjectName("[PROJECT]").toString();
        String intentBatchUri = "intentBatchUri544125582";
        BatchUpdateIntentsResponse response =
            intentsClient.batchUpdateIntentsAsync(parent, intentBatchUri).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the agent to update or create intents in. Format: `projects/<Project ID>/agent`.  
`intentBatchUri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The URI to a Google Cloud Storage file containing intents to update or create. The file format can either be a serialized proto (of IntentBatch type) or JSON object. Note: The URI must start with "gs://".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### batchUpdateIntentsCallable()
    
    
    public final UnaryCallable<BatchUpdateIntentsRequest,Operation> batchUpdateIntentsCallable()

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchUpdateIntentsRequest request =
            BatchUpdateIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .setLanguageCode("languageCode-2092349083")
                .setUpdateMask(FieldMask.newBuilder().build())
                .setIntentView(IntentView.forNumber(0))
                .build();
        ApiFuture<Operation> future = intentsClient.batchUpdateIntentsCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchUpdateIntentsOperationCallable()
    
    
    public final OperationCallable<BatchUpdateIntentsRequest,BatchUpdateIntentsResponse,Struct> batchUpdateIntentsOperationCallable()

Updates/Creates multiple intents in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: BatchUpdateIntentsResponse

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IntentsClient intentsClient = IntentsClient.create()) {
        BatchUpdateIntentsRequest request =
            BatchUpdateIntentsRequest.newBuilder()
                .setParent(AgentName.ofProjectName("[PROJECT]").toString())
                .setLanguageCode("languageCode-2092349083")
                .setUpdateMask(FieldMask.newBuilder().build())
                .setIntentView(IntentView.forNumber(0))
                .build();
        OperationFuture<BatchUpdateIntentsResponse, Struct> future =
            intentsClient.batchUpdateIntentsOperationCallable().futureCall(request);
        // Do something.
        BatchUpdateIntentsResponse response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchUpdateIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsRequest),[BatchUpdateIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BatchUpdateIntentsResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### close()
    
    
    public final void close()

### createIntent(@Nullable AgentName parent, Intent intent)
    
    
    public final Intent createIntent(@Nullable AgentName parent, Intent intent)

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       AgentName parent = AgentName.ofProjectName("[PROJECT]");
       Intent intent = Intent.newBuilder().build();
       Intent response = intentsClient.createIntent(parent, intent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The agent to create a intent for. Format: `projects/<Project ID>/agent`.  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### createIntent(@Nullable AgentName parent, Intent intent, String languageCode)
    
    
    public final Intent createIntent(@Nullable AgentName parent, Intent intent, String languageCode)

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       AgentName parent = AgentName.ofProjectName("[PROJECT]");
       Intent intent = Intent.newBuilder().build();
       String languageCode = "languageCode-2092349083";
       Intent response = intentsClient.createIntent(parent, intent, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The agent to create a intent for. Format: `projects/<Project ID>/agent`.  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to create.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### createIntent(CreateIntentRequest request)
    
    
    public final Intent createIntent(CreateIntentRequest request)

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       CreateIntentRequest request =
           CreateIntentRequest.newBuilder()
               .setParent(AgentName.ofProjectName("[PROJECT]").toString())
               .setIntent(Intent.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .build();
       Intent response = intentsClient.createIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### createIntent(String parent, Intent intent)
    
    
    public final Intent createIntent(String parent, Intent intent)

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String parent = AgentName.ofProjectName("[PROJECT]").toString();
       Intent intent = Intent.newBuilder().build();
       Intent response = intentsClient.createIntent(parent, intent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create a intent for. Format: `projects/<Project ID>/agent`.  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### createIntent(String parent, Intent intent, String languageCode)
    
    
    public final Intent createIntent(String parent, Intent intent, String languageCode)

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String parent = AgentName.ofProjectName("[PROJECT]").toString();
       Intent intent = Intent.newBuilder().build();
       String languageCode = "languageCode-2092349083";
       Intent response = intentsClient.createIntent(parent, intent, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create a intent for. Format: `projects/<Project ID>/agent`.  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to create.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### createIntentCallable()
    
    
    public final UnaryCallable<CreateIntentRequest,Intent> createIntentCallable()

Creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       CreateIntentRequest request =
           CreateIntentRequest.newBuilder()
               .setParent(AgentName.ofProjectName("[PROJECT]").toString())
               .setIntent(Intent.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .build();
       ApiFuture<Intent> future = intentsClient.createIntentCallable().futureCall(request);
       // Do something.
       Intent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateIntentRequest),[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)>` |   
  
### deleteIntent(@Nullable IntentName name)
    
    
    public final void deleteIntent(@Nullable IntentName name)

Deletes the specified intent and its direct or indirect followup intents.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       IntentName name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]");
       intentsClient.deleteIntent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.IntentName`  
Required. The name of the intent to delete. If this intent has direct or indirect followup intents, we also delete them. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
  
### deleteIntent(DeleteIntentRequest request)
    
    
    public final void deleteIntent(DeleteIntentRequest request)

Deletes the specified intent and its direct or indirect followup intents.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       DeleteIntentRequest request =
           DeleteIntentRequest.newBuilder()
               .setName(IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString())
               .build();
       intentsClient.deleteIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteIntentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteIntent(String name)
    
    
    public final void deleteIntent(String name)

Deletes the specified intent and its direct or indirect followup intents.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString();
       intentsClient.deleteIntent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the intent to delete. If this intent has direct or indirect followup intents, we also delete them. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
  
### deleteIntentCallable()
    
    
    public final UnaryCallable<DeleteIntentRequest,Empty> deleteIntentCallable()

Deletes the specified intent and its direct or indirect followup intents.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       DeleteIntentRequest request =
           DeleteIntentRequest.newBuilder()
               .setName(IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString())
               .build();
       ApiFuture<Empty> future = intentsClient.deleteIntentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteIntentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIntent(@Nullable IntentName name)
    
    
    public final Intent getIntent(@Nullable IntentName name)

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       IntentName name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]");
       Intent response = intentsClient.getIntent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.IntentName`  
Required. The name of the intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### getIntent(@Nullable IntentName name, String languageCode)
    
    
    public final Intent getIntent(@Nullable IntentName name, String languageCode)

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       IntentName name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]");
       String languageCode = "languageCode-2092349083";
       Intent response = intentsClient.getIntent(name, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.IntentName`  
Required. The name of the intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### getIntent(GetIntentRequest request)
    
    
    public final Intent getIntent(GetIntentRequest request)

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       GetIntentRequest request =
           GetIntentRequest.newBuilder()
               .setName(IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .build();
       Intent response = intentsClient.getIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### getIntent(String name)
    
    
    public final Intent getIntent(String name)

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString();
       Intent response = intentsClient.getIntent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### getIntent(String name, String languageCode)
    
    
    public final Intent getIntent(String name, String languageCode)

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String name = IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString();
       String languageCode = "languageCode-2092349083";
       Intent response = intentsClient.getIntent(name, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### getIntentCallable()
    
    
    public final UnaryCallable<GetIntentRequest,Intent> getIntentCallable()

Retrieves the specified intent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       GetIntentRequest request =
           GetIntentRequest.newBuilder()
               .setName(IntentName.ofProjectIntentName("[PROJECT]", "[INTENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .build();
       ApiFuture<Intent> future = intentsClient.getIntentCallable().futureCall(request);
       // Do something.
       Intent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetIntentRequest),[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = intentsClient.getLocation(request);
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
     try (IntentsClient intentsClient = IntentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = intentsClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable IntentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.IntentsSettings` |   
  
### getStub()
    
    
    public IntentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[IntentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.IntentsStub)` |   
  
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
  
### listIntents(@Nullable AgentName parent)
    
    
    public final IntentsClient.ListIntentsPagedResponse listIntents(@Nullable AgentName parent)

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       AgentName parent = AgentName.ofProjectName("[PROJECT]");
       for (Intent element : intentsClient.listIntents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The agent to list all intents from. Format: `projects/<Project ID>/agent` or `projects/<Project ID>/locations/<Location ID>/agent`. Alternatively, you can specify the environment to list intents for. Format: `projects/<Project ID>/agent/environments/<Environment ID>` or `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`. Note: training phrases of the intents will not be returned for non-draft environment.  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient.ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)` |   
  
### listIntents(@Nullable AgentName parent, String languageCode)
    
    
    public final IntentsClient.ListIntentsPagedResponse listIntents(@Nullable AgentName parent, String languageCode)

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       AgentName parent = AgentName.ofProjectName("[PROJECT]");
       String languageCode = "languageCode-2092349083";
       for (Intent element : intentsClient.listIntents(parent, languageCode).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.AgentName`  
Required. The agent to list all intents from. Format: `projects/<Project ID>/agent` or `projects/<Project ID>/locations/<Location ID>/agent`. Alternatively, you can specify the environment to list intents for. Format: `projects/<Project ID>/agent/environments/<Environment ID>` or `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`. Note: training phrases of the intents will not be returned for non-draft environment.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient.ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)` |   
  
### listIntents(ListIntentsRequest request)
    
    
    public final IntentsClient.ListIntentsPagedResponse listIntents(ListIntentsRequest request)

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListIntentsRequest request =
           ListIntentsRequest.newBuilder()
               .setParent(AgentName.ofProjectName("[PROJECT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Intent element : intentsClient.listIntents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListIntentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient.ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)` |   
  
### listIntents(String parent)
    
    
    public final IntentsClient.ListIntentsPagedResponse listIntents(String parent)

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String parent = AgentName.ofProjectName("[PROJECT]").toString();
       for (Intent element : intentsClient.listIntents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list all intents from. Format: `projects/<Project ID>/agent` or `projects/<Project ID>/locations/<Location ID>/agent`. Alternatively, you can specify the environment to list intents for. Format: `projects/<Project ID>/agent/environments/<Environment ID>` or `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`. Note: training phrases of the intents will not be returned for non-draft environment.  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient.ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)` |   
  
### listIntents(String parent, String languageCode)
    
    
    public final IntentsClient.ListIntentsPagedResponse listIntents(String parent, String languageCode)

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       String parent = AgentName.ofProjectName("[PROJECT]").toString();
       String languageCode = "languageCode-2092349083";
       for (Intent element : intentsClient.listIntents(parent, languageCode).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list all intents from. Format: `projects/<Project ID>/agent` or `projects/<Project ID>/locations/<Location ID>/agent`. Alternatively, you can specify the environment to list intents for. Format: `projects/<Project ID>/agent/environments/<Environment ID>` or `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`. Note: training phrases of the intents will not be returned for non-draft environment.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[IntentsClient.ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)` |   
  
### listIntentsCallable()
    
    
    public final UnaryCallable<ListIntentsRequest,ListIntentsResponse> listIntentsCallable()

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListIntentsRequest request =
           ListIntentsRequest.newBuilder()
               .setParent(AgentName.ofProjectName("[PROJECT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListIntentsResponse response = intentsClient.listIntentsCallable().call(request);
         for (Intent element : response.getIntentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListIntentsRequest),[ListIntentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListIntentsResponse)>` |   
  
### listIntentsPagedCallable()
    
    
    public final UnaryCallable<ListIntentsRequest,IntentsClient.ListIntentsPagedResponse> listIntentsPagedCallable()

Returns the list of all intents in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListIntentsRequest request =
           ListIntentsRequest.newBuilder()
               .setParent(AgentName.ofProjectName("[PROJECT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .setIntentView(IntentView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Intent> future = intentsClient.listIntentsPagedCallable().futureCall(request);
       // Do something.
       for (Intent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIntentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListIntentsRequest),[ListIntentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListIntentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final IntentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : intentsClient.listLocations(request).iterateAll()) {
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
`[IntentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListLocationsPagedResponse)` |   
  
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
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = intentsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,IntentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = intentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateIntent(Intent intent, String languageCode)
    
    
    public final Intent updateIntent(Intent intent, String languageCode)

Updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       Intent intent = Intent.newBuilder().build();
       String languageCode = "languageCode-2092349083";
       Intent response = intentsClient.updateIntent(intent, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to update.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### updateIntent(Intent intent, String languageCode, FieldMask updateMask)
    
    
    public final Intent updateIntent(Intent intent, String languageCode, FieldMask updateMask)

Updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       Intent intent = Intent.newBuilder().build();
       String languageCode = "languageCode-2092349083";
       FieldMask updateMask = FieldMask.newBuilder().build();
       Intent response = intentsClient.updateIntent(intent, languageCode, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`intent` | `[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)`  
Required. The intent to update.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The mask to control which fields get updated.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### updateIntent(UpdateIntentRequest request)
    
    
    public final Intent updateIntent(UpdateIntentRequest request)

Updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       UpdateIntentRequest request =
           UpdateIntentRequest.newBuilder()
               .setIntent(Intent.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setUpdateMask(FieldMask.newBuilder().build())
               .setIntentView(IntentView.forNumber(0))
               .build();
       Intent response = intentsClient.updateIntent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateIntentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` |   
  
### updateIntentCallable()
    
    
    public final UnaryCallable<UpdateIntentRequest,Intent> updateIntentCallable()

Updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IntentsClient intentsClient = IntentsClient.create()) {
       UpdateIntentRequest request =
           UpdateIntentRequest.newBuilder()
               .setIntent(Intent.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .setUpdateMask(FieldMask.newBuilder().build())
               .setIntentView(IntentView.forNumber(0))
               .build();
       ApiFuture<Intent> future = intentsClient.updateIntentCallable().futureCall(request);
       // Do something.
       Intent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateIntentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateIntentRequest),[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
