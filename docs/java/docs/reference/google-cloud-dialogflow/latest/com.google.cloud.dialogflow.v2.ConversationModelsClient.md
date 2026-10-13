---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient
title: Class ConversationModelsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:33.728332+00:00
---

# Class ConversationModelsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationModelsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/ConversationModelsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Manages a collection of models for human agent assistant.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String name = "name3373707";
       ConversationModel response = conversationModelsClient.getConversationModel(name);
     }
     

Note: close() needs to be called on the ConversationModelsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateConversationModel |  Creates a model.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: CreateConversationModelOperationMetadata \- `response`: ConversationModel |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversationModelAsync(CreateConversationModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConversationModelAsync(String parent, ConversationModel conversationModel) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationModelOperationCallable() 
  * createConversationModelCallable() 

  
GetConversationModel |  Gets conversation model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversationModel(GetConversationModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversationModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationModelCallable() 

  
ListConversationModels |  Lists conversation models. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversationModels(ListConversationModelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversationModels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationModelsPagedCallable() 
  * listConversationModelsCallable() 

  
DeleteConversationModel |  Deletes a model.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: DeleteConversationModelOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversationModelAsync(DeleteConversationModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteConversationModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversationModelOperationCallable() 
  * deleteConversationModelCallable() 

  
DeployConversationModel |  Deploys a model. If a model is already deployed, deploying it has no effect. A model can only serve prediction requests after it gets deployed. For article suggestion, custom model will not be used unless it is deployed.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: DeployConversationModelOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployConversationModelAsync(DeployConversationModelRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployConversationModelOperationCallable() 
  * deployConversationModelCallable() 

  
UndeployConversationModel |  Undeploys a model. If the model is not deployed this method has no effect. If the model is currently being used: - For article suggestion, article suggestion will fallback to the default model if model is undeployed.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: UndeployConversationModelOperationMetadata \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeployConversationModelAsync(UndeployConversationModelRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeployConversationModelOperationCallable() 
  * undeployConversationModelCallable() 

  
GetConversationModelEvaluation |  Gets an evaluation of conversation model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversationModelEvaluation(GetConversationModelEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversationModelEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationModelEvaluationCallable() 

  
ListConversationModelEvaluations |  Lists evaluations of a conversation model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversationModelEvaluations(ListConversationModelEvaluationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversationModelEvaluations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationModelEvaluationsPagedCallable() 
  * listConversationModelEvaluationsCallable() 

  
CreateConversationModelEvaluation |  Creates evaluation of a conversation model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversationModelEvaluationAsync(CreateConversationModelEvaluationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConversationModelEvaluationAsync(ConversationModelName parent, ConversationModelEvaluation conversationModelEvaluation) 
  * createConversationModelEvaluationAsync(String parent, ConversationModelEvaluation conversationModelEvaluation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationModelEvaluationOperationCallable() 
  * createConversationModelEvaluationCallable() 

  
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

This class can be customized by passing in a custom instance of ConversationModelsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationModelsSettings conversationModelsSettings =
         ConversationModelsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationModelsClient conversationModelsClient =
         ConversationModelsClient.create(conversationModelsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationModelsSettings conversationModelsSettings =
         ConversationModelsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationModelsClient conversationModelsClient =
         ConversationModelsClient.create(conversationModelsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationModelsSettings conversationModelsSettings =
         ConversationModelsSettings.newHttpJsonBuilder().build();
     ConversationModelsClient conversationModelsClient =
         ConversationModelsClient.create(conversationModelsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationModelsClient

## Static Methods 

### create()
    
    
    public static final ConversationModelsClient create()

Constructs an instance of ConversationModelsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationModelsSettings settings)
    
    
    public static final ConversationModelsClient create(ConversationModelsSettings settings)

Constructs an instance of ConversationModelsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationModelsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationModelsStub stub)
    
    
    public static final ConversationModelsClient create(ConversationModelsStub stub)

Constructs an instance of ConversationModelsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationModelsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationModelsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationModelsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient)` |   
  
## Constructors 

### ConversationModelsClient(ConversationModelsSettings settings)
    
    
    protected ConversationModelsClient(ConversationModelsSettings settings)

Constructs an instance of ConversationModelsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationModelsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsSettings)`  
  
  
### ConversationModelsClient(ConversationModelsStub stub)
    
    
    protected ConversationModelsClient(ConversationModelsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationModelsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationModelsStub)`  
  
  
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

### createConversationModelAsync(CreateConversationModelRequest request)
    
    
    public final OperationFuture<ConversationModel,CreateConversationModelOperationMetadata> createConversationModelAsync(CreateConversationModelRequest request)

Creates a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationModelOperationMetadata

  * `response`: ConversationModel

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        CreateConversationModelRequest request =
            CreateConversationModelRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationModel(ConversationModel.newBuilder().build())
                .build();
        ConversationModel response =
            conversationModelsClient.createConversationModelAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel),[CreateConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelOperationMetadata)>` |   
  
### createConversationModelAsync(String parent, ConversationModel conversationModel)
    
    
    public final OperationFuture<ConversationModel,CreateConversationModelOperationMetadata> createConversationModelAsync(String parent, ConversationModel conversationModel)

Creates a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationModelOperationMetadata

  * `response`: ConversationModel

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        String parent = "parent-995424086";
        ConversationModel conversationModel = ConversationModel.newBuilder().build();
        ConversationModel response =
            conversationModelsClient.createConversationModelAsync(parent, conversationModel).get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project to create conversation model for. Format: `projects/<Project ID>`  
`conversationModel` | `[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel)`  
Required. The conversation model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel),[CreateConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelOperationMetadata)>` |   
  
### createConversationModelCallable()
    
    
    public final UnaryCallable<CreateConversationModelRequest,Operation> createConversationModelCallable()

Creates a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationModelOperationMetadata

  * `response`: ConversationModel

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        CreateConversationModelRequest request =
            CreateConversationModelRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationModel(ConversationModel.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            conversationModelsClient.createConversationModelCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConversationModelEvaluationAsync(@Nullable ConversationModelName parent, ConversationModelEvaluation conversationModelEvaluation)
    
    
    public final OperationFuture<ConversationModelEvaluation,CreateConversationModelEvaluationOperationMetadata> createConversationModelEvaluationAsync(@Nullable ConversationModelName parent, ConversationModelEvaluation conversationModelEvaluation)

Creates evaluation of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ConversationModelName parent =
           ConversationModelName.ofProjectLocationConversationModelName(
               "[PROJECT]", "[LOCATION]", "[CONVERSATION_MODEL]");
       ConversationModelEvaluation conversationModelEvaluation =
           ConversationModelEvaluation.newBuilder().build();
       ConversationModelEvaluation response =
           conversationModelsClient
               .createConversationModelEvaluationAsync(parent, conversationModelEvaluation)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationModelName`  
Required. The conversation model resource name. Format: `projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model ID>`  
`conversationModelEvaluation` | `[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation)`  
Required. The conversation model evaluation to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation),[CreateConversationModelEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationOperationMetadata)>` |   
  
### createConversationModelEvaluationAsync(CreateConversationModelEvaluationRequest request)
    
    
    public final OperationFuture<ConversationModelEvaluation,CreateConversationModelEvaluationOperationMetadata> createConversationModelEvaluationAsync(CreateConversationModelEvaluationRequest request)

Creates evaluation of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       CreateConversationModelEvaluationRequest request =
           CreateConversationModelEvaluationRequest.newBuilder()
               .setParent(
                   ConversationModelName.ofProjectLocationConversationModelName(
                           "[PROJECT]", "[LOCATION]", "[CONVERSATION_MODEL]")
                       .toString())
               .setConversationModelEvaluation(ConversationModelEvaluation.newBuilder().build())
               .build();
       ConversationModelEvaluation response =
           conversationModelsClient.createConversationModelEvaluationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation),[CreateConversationModelEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationOperationMetadata)>` |   
  
### createConversationModelEvaluationAsync(String parent, ConversationModelEvaluation conversationModelEvaluation)
    
    
    public final OperationFuture<ConversationModelEvaluation,CreateConversationModelEvaluationOperationMetadata> createConversationModelEvaluationAsync(String parent, ConversationModelEvaluation conversationModelEvaluation)

Creates evaluation of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String parent =
           ConversationModelName.ofProjectLocationConversationModelName(
                   "[PROJECT]", "[LOCATION]", "[CONVERSATION_MODEL]")
               .toString();
       ConversationModelEvaluation conversationModelEvaluation =
           ConversationModelEvaluation.newBuilder().build();
       ConversationModelEvaluation response =
           conversationModelsClient
               .createConversationModelEvaluationAsync(parent, conversationModelEvaluation)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation model resource name. Format: `projects/<Project ID>/locations/<Location ID>/conversationModels/<Conversation Model ID>`  
`conversationModelEvaluation` | `[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation)`  
Required. The conversation model evaluation to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation),[CreateConversationModelEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationOperationMetadata)>` |   
  
### createConversationModelEvaluationCallable()
    
    
    public final UnaryCallable<CreateConversationModelEvaluationRequest,Operation> createConversationModelEvaluationCallable()

Creates evaluation of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       CreateConversationModelEvaluationRequest request =
           CreateConversationModelEvaluationRequest.newBuilder()
               .setParent(
                   ConversationModelName.ofProjectLocationConversationModelName(
                           "[PROJECT]", "[LOCATION]", "[CONVERSATION_MODEL]")
                       .toString())
               .setConversationModelEvaluation(ConversationModelEvaluation.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           conversationModelsClient.createConversationModelEvaluationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConversationModelEvaluationOperationCallable()
    
    
    public final OperationCallable<CreateConversationModelEvaluationRequest,ConversationModelEvaluation,CreateConversationModelEvaluationOperationMetadata> createConversationModelEvaluationOperationCallable()

Creates evaluation of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       CreateConversationModelEvaluationRequest request =
           CreateConversationModelEvaluationRequest.newBuilder()
               .setParent(
                   ConversationModelName.ofProjectLocationConversationModelName(
                           "[PROJECT]", "[LOCATION]", "[CONVERSATION_MODEL]")
                       .toString())
               .setConversationModelEvaluation(ConversationModelEvaluation.newBuilder().build())
               .build();
       OperationFuture< conversationmodelevaluation,="" createconversationmodelevaluationoperationmetadata="">
           future =
               conversationModelsClient
                   .createConversationModelEvaluationOperationCallable()
                   .futureCall(request);
       // Do something.
       ConversationModelEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConversationModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationRequest),[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation),[CreateConversationModelEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelEvaluationOperationMetadata)>` |   
  
### createConversationModelOperationCallable()
    
    
    public final OperationCallable<CreateConversationModelRequest,ConversationModel,CreateConversationModelOperationMetadata> createConversationModelOperationCallable()

Creates a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: CreateConversationModelOperationMetadata

  * `response`: ConversationModel

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        CreateConversationModelRequest request =
            CreateConversationModelRequest.newBuilder()
                .setParent("parent-995424086")
                .setConversationModel(ConversationModel.newBuilder().build())
                .build();
        OperationFuture<ConversationModel, CreateConversationModelOperationMetadata> future =
            conversationModelsClient.createConversationModelOperationCallable().futureCall(request);
        // Do something.
        ConversationModel response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelRequest),[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel),[CreateConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationModelOperationMetadata)>` |   
  
### deleteConversationModelAsync(DeleteConversationModelRequest request)
    
    
    public final OperationFuture<Empty,DeleteConversationModelOperationMetadata> deleteConversationModelAsync(DeleteConversationModelRequest request)

Deletes a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeleteConversationModelRequest request =
            DeleteConversationModelRequest.newBuilder().setName("name3373707").build();
        conversationModelsClient.deleteConversationModelAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelOperationMetadata)>` |   
  
### deleteConversationModelAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteConversationModelOperationMetadata> deleteConversationModelAsync(String name)

Deletes a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        String name = "name3373707";
        conversationModelsClient.deleteConversationModelAsync(name).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation model to delete. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelOperationMetadata)>` |   
  
### deleteConversationModelCallable()
    
    
    public final UnaryCallable<DeleteConversationModelRequest,Operation> deleteConversationModelCallable()

Deletes a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeleteConversationModelRequest request =
            DeleteConversationModelRequest.newBuilder().setName("name3373707").build();
        ApiFuture<Operation> future =
            conversationModelsClient.deleteConversationModelCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConversationModelOperationCallable()
    
    
    public final OperationCallable<DeleteConversationModelRequest,Empty,DeleteConversationModelOperationMetadata> deleteConversationModelOperationCallable()

Deletes a model.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeleteConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeleteConversationModelRequest request =
            DeleteConversationModelRequest.newBuilder().setName("name3373707").build();
        OperationFuture<Empty, DeleteConversationModelOperationMetadata> future =
            conversationModelsClient.deleteConversationModelOperationCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationModelOperationMetadata)>` |   
  
### deployConversationModelAsync(DeployConversationModelRequest request)
    
    
    public final OperationFuture<Empty,DeployConversationModelOperationMetadata> deployConversationModelAsync(DeployConversationModelRequest request)

Deploys a model. If a model is already deployed, deploying it has no effect. A model can only serve prediction requests after it gets deployed. For article suggestion, custom model will not be used unless it is deployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeployConversationModelRequest request =
            DeployConversationModelRequest.newBuilder().setName("name3373707").build();
        conversationModelsClient.deployConversationModelAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeployConversationModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeployConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeployConversationModelOperationMetadata)>` |   
  
### deployConversationModelCallable()
    
    
    public final UnaryCallable<DeployConversationModelRequest,Operation> deployConversationModelCallable()

Deploys a model. If a model is already deployed, deploying it has no effect. A model can only serve prediction requests after it gets deployed. For article suggestion, custom model will not be used unless it is deployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeployConversationModelRequest request =
            DeployConversationModelRequest.newBuilder().setName("name3373707").build();
        ApiFuture<Operation> future =
            conversationModelsClient.deployConversationModelCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeployConversationModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployConversationModelOperationCallable()
    
    
    public final OperationCallable<DeployConversationModelRequest,Empty,DeployConversationModelOperationMetadata> deployConversationModelOperationCallable()

Deploys a model. If a model is already deployed, deploying it has no effect. A model can only serve prediction requests after it gets deployed. For article suggestion, custom model will not be used unless it is deployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: DeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        DeployConversationModelRequest request =
            DeployConversationModelRequest.newBuilder().setName("name3373707").build();
        OperationFuture<Empty, DeployConversationModelOperationMetadata> future =
            conversationModelsClient.deployConversationModelOperationCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeployConversationModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeployConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeployConversationModelOperationMetadata)>` |   
  
### getConversationModel(GetConversationModelRequest request)
    
    
    public final ConversationModel getConversationModel(GetConversationModelRequest request)

Gets conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetConversationModelRequest request =
           GetConversationModelRequest.newBuilder().setName("name3373707").build();
       ConversationModel response = conversationModelsClient.getConversationModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel)` |   
  
### getConversationModel(String name)
    
    
    public final ConversationModel getConversationModel(String name)

Gets conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String name = "name3373707";
       ConversationModel response = conversationModelsClient.getConversationModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation model to retrieve. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel)` |   
  
### getConversationModelCallable()
    
    
    public final UnaryCallable<GetConversationModelRequest,ConversationModel> getConversationModelCallable()

Gets conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetConversationModelRequest request =
           GetConversationModelRequest.newBuilder().setName("name3373707").build();
       ApiFuture<ConversationModel> future =
           conversationModelsClient.getConversationModelCallable().futureCall(request);
       // Do something.
       ConversationModel response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationModelRequest),[ConversationModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModel)>` |   
  
### getConversationModelEvaluation(GetConversationModelEvaluationRequest request)
    
    
    public final ConversationModelEvaluation getConversationModelEvaluation(GetConversationModelEvaluationRequest request)

Gets an evaluation of conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetConversationModelEvaluationRequest request =
           GetConversationModelEvaluationRequest.newBuilder().setName("name3373707").build();
       ConversationModelEvaluation response =
           conversationModelsClient.getConversationModelEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationModelEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation)` |   
  
### getConversationModelEvaluation(String name)
    
    
    public final ConversationModelEvaluation getConversationModelEvaluation(String name)

Gets an evaluation of conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String name = "name3373707";
       ConversationModelEvaluation response =
           conversationModelsClient.getConversationModelEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation model evaluation resource name. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>/evaluations/<Evaluation ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation)` |   
  
### getConversationModelEvaluationCallable()
    
    
    public final UnaryCallable<GetConversationModelEvaluationRequest,ConversationModelEvaluation> getConversationModelEvaluationCallable()

Gets an evaluation of conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetConversationModelEvaluationRequest request =
           GetConversationModelEvaluationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<ConversationModelEvaluation> future =
           conversationModelsClient.getConversationModelEvaluationCallable().futureCall(request);
       // Do something.
       ConversationModelEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationModelEvaluationRequest),[ConversationModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelEvaluation)>` |   
  
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
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = conversationModelsClient.getLocation(request);
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
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           conversationModelsClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable ConversationModelsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationModelsSettings` |   
  
### getStub()
    
    
    public ConversationModelsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationModelsStub)` |   
  
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
  
### listConversationModelEvaluations(ListConversationModelEvaluationsRequest request)
    
    
    public final ConversationModelsClient.ListConversationModelEvaluationsPagedResponse listConversationModelEvaluations(ListConversationModelEvaluationsRequest request)

Lists evaluations of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelEvaluationsRequest request =
           ListConversationModelEvaluationsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ConversationModelEvaluation element :
           conversationModelsClient.listConversationModelEvaluations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelEvaluationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient.ListConversationModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelEvaluationsPagedResponse)` |   
  
### listConversationModelEvaluations(String parent)
    
    
    public final ConversationModelsClient.ListConversationModelEvaluationsPagedResponse listConversationModelEvaluations(String parent)

Lists evaluations of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String parent = "parent-995424086";
       for (ConversationModelEvaluation element :
           conversationModelsClient.listConversationModelEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation model resource name. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient.ListConversationModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelEvaluationsPagedResponse)` |   
  
### listConversationModelEvaluationsCallable()
    
    
    public final UnaryCallable<ListConversationModelEvaluationsRequest,ListConversationModelEvaluationsResponse> listConversationModelEvaluationsCallable()

Lists evaluations of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelEvaluationsRequest request =
           ListConversationModelEvaluationsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListConversationModelEvaluationsResponse response =
             conversationModelsClient.listConversationModelEvaluationsCallable().call(request);
         for (ConversationModelEvaluation element : response.getConversationModelEvaluationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelEvaluationsRequest),[ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelEvaluationsResponse)>` |   
  
### listConversationModelEvaluationsPagedCallable()
    
    
    public final UnaryCallable<ListConversationModelEvaluationsRequest,ConversationModelsClient.ListConversationModelEvaluationsPagedResponse> listConversationModelEvaluationsPagedCallable()

Lists evaluations of a conversation model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelEvaluationsRequest request =
           ListConversationModelEvaluationsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ConversationModelEvaluation> future =
           conversationModelsClient
               .listConversationModelEvaluationsPagedCallable()
               .futureCall(request);
       // Do something.
       for (ConversationModelEvaluation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelEvaluationsRequest),[ListConversationModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelEvaluationsPagedResponse)>` |   
  
### listConversationModels(ListConversationModelsRequest request)
    
    
    public final ConversationModelsClient.ListConversationModelsPagedResponse listConversationModels(ListConversationModelsRequest request)

Lists conversation models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelsRequest request =
           ListConversationModelsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ConversationModel element :
           conversationModelsClient.listConversationModels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient.ListConversationModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelsPagedResponse)` |   
  
### listConversationModels(String parent)
    
    
    public final ConversationModelsClient.ListConversationModelsPagedResponse listConversationModels(String parent)

Lists conversation models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       String parent = "parent-995424086";
       for (ConversationModel element :
           conversationModelsClient.listConversationModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to list all conversation models for. Format: `projects/<Project ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationModelsClient.ListConversationModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelsPagedResponse)` |   
  
### listConversationModelsCallable()
    
    
    public final UnaryCallable<ListConversationModelsRequest,ListConversationModelsResponse> listConversationModelsCallable()

Lists conversation models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelsRequest request =
           ListConversationModelsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListConversationModelsResponse response =
             conversationModelsClient.listConversationModelsCallable().call(request);
         for (ConversationModel element : response.getConversationModelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelsRequest),[ListConversationModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelsResponse)>` |   
  
### listConversationModelsPagedCallable()
    
    
    public final UnaryCallable<ListConversationModelsRequest,ConversationModelsClient.ListConversationModelsPagedResponse> listConversationModelsPagedCallable()

Lists conversation models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListConversationModelsRequest request =
           ListConversationModelsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ConversationModel> future =
           conversationModelsClient.listConversationModelsPagedCallable().futureCall(request);
       // Do something.
       for (ConversationModel element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationModelsRequest),[ListConversationModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListConversationModelsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ConversationModelsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : conversationModelsClient.listLocations(request).iterateAll()) {
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
`[ConversationModelsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListLocationsPagedResponse)` |   
  
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
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             conversationModelsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ConversationModelsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           conversationModelsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationModelsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### undeployConversationModelAsync(UndeployConversationModelRequest request)
    
    
    public final OperationFuture<Empty,UndeployConversationModelOperationMetadata> undeployConversationModelAsync(UndeployConversationModelRequest request)

Undeploys a model. If the model is not deployed this method has no effect. If the model is currently being used: - For article suggestion, article suggestion will fallback to the default model if model is undeployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: UndeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        UndeployConversationModelRequest request =
            UndeployConversationModelRequest.newBuilder().setName("name3373707").build();
        conversationModelsClient.undeployConversationModelAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UndeployConversationModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[UndeployConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UndeployConversationModelOperationMetadata)>` |   
  
### undeployConversationModelCallable()
    
    
    public final UnaryCallable<UndeployConversationModelRequest,Operation> undeployConversationModelCallable()

Undeploys a model. If the model is not deployed this method has no effect. If the model is currently being used: - For article suggestion, article suggestion will fallback to the default model if model is undeployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: UndeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        UndeployConversationModelRequest request =
            UndeployConversationModelRequest.newBuilder().setName("name3373707").build();
        ApiFuture<Operation> future =
            conversationModelsClient.undeployConversationModelCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UndeployConversationModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeployConversationModelOperationCallable()
    
    
    public final OperationCallable<UndeployConversationModelRequest,Empty,UndeployConversationModelOperationMetadata> undeployConversationModelOperationCallable()

Undeploys a model. If the model is not deployed this method has no effect. If the model is currently being used: - For article suggestion, article suggestion will fallback to the default model if model is undeployed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: UndeployConversationModelOperationMetadata

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationModelsClient conversationModelsClient = ConversationModelsClient.create()) {
        UndeployConversationModelRequest request =
            UndeployConversationModelRequest.newBuilder().setName("name3373707").build();
        OperationFuture<Empty, UndeployConversationModelOperationMetadata> future =
            conversationModelsClient.undeployConversationModelOperationCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeployConversationModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UndeployConversationModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[UndeployConversationModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UndeployConversationModelOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
