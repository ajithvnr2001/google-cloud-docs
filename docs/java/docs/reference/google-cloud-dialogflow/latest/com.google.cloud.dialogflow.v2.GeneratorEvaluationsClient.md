---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient
title: Class GeneratorEvaluationsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:42.483243+00:00
---

# Class GeneratorEvaluationsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GeneratorEvaluationsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/GeneratorEvaluationsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing generator evaluations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GeneratorEvaluationName name =
           GeneratorEvaluationName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]");
       GeneratorEvaluation response = generatorEvaluationsClient.getGeneratorEvaluation(name);
     }
     

Note: close() needs to be called on the GeneratorEvaluationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateGeneratorEvaluation |  Creates evaluation of a generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGeneratorEvaluationAsync(CreateGeneratorEvaluationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGeneratorEvaluationAsync(GeneratorName parent, GeneratorEvaluation generatorEvaluation) 
  * createGeneratorEvaluationAsync(String parent, GeneratorEvaluation generatorEvaluation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGeneratorEvaluationOperationCallable() 
  * createGeneratorEvaluationCallable() 

  
GetGeneratorEvaluation |  Gets an evaluation of generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGeneratorEvaluation(GetGeneratorEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGeneratorEvaluation(GeneratorEvaluationName name) 
  * getGeneratorEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGeneratorEvaluationCallable() 

  
ListGeneratorEvaluations |  Lists evaluations of generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGeneratorEvaluations(ListGeneratorEvaluationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGeneratorEvaluations(GeneratorName parent) 
  * listGeneratorEvaluations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGeneratorEvaluationsPagedCallable() 
  * listGeneratorEvaluationsCallable() 

  
DeleteGeneratorEvaluation |  Deletes an evaluation of generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGeneratorEvaluation(DeleteGeneratorEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteGeneratorEvaluation(GeneratorEvaluationName name) 
  * deleteGeneratorEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGeneratorEvaluationCallable() 

  
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

This class can be customized by passing in a custom instance of GeneratorEvaluationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorEvaluationsSettings generatorEvaluationsSettings =
         GeneratorEvaluationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create(generatorEvaluationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorEvaluationsSettings generatorEvaluationsSettings =
         GeneratorEvaluationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create(generatorEvaluationsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorEvaluationsSettings generatorEvaluationsSettings =
         GeneratorEvaluationsSettings.newHttpJsonBuilder().build();
     GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create(generatorEvaluationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GeneratorEvaluationsClient

## Static Methods 

### create()
    
    
    public static final GeneratorEvaluationsClient create()

Constructs an instance of GeneratorEvaluationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeneratorEvaluationsSettings settings)
    
    
    public static final GeneratorEvaluationsClient create(GeneratorEvaluationsSettings settings)

Constructs an instance of GeneratorEvaluationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeneratorEvaluationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeneratorEvaluationsStub stub)
    
    
    public static final GeneratorEvaluationsClient create(GeneratorEvaluationsStub stub)

Constructs an instance of GeneratorEvaluationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(GeneratorEvaluationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeneratorEvaluationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorEvaluationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient)` |   
  
## Constructors 

### GeneratorEvaluationsClient(GeneratorEvaluationsSettings settings)
    
    
    protected GeneratorEvaluationsClient(GeneratorEvaluationsSettings settings)

Constructs an instance of GeneratorEvaluationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeneratorEvaluationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsSettings)`  
  
  
### GeneratorEvaluationsClient(GeneratorEvaluationsStub stub)
    
    
    protected GeneratorEvaluationsClient(GeneratorEvaluationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeneratorEvaluationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorEvaluationsStub)`  
  
  
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

### createGeneratorEvaluationAsync(@Nullable GeneratorName parent, GeneratorEvaluation generatorEvaluation)
    
    
    public final OperationFuture<GeneratorEvaluation,GeneratorEvaluationOperationMetadata> createGeneratorEvaluationAsync(@Nullable GeneratorName parent, GeneratorEvaluation generatorEvaluation)

Creates evaluation of a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GeneratorName parent = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]");
       GeneratorEvaluation generatorEvaluation = GeneratorEvaluation.newBuilder().build();
       GeneratorEvaluation response =
           generatorEvaluationsClient
               .createGeneratorEvaluationAsync(parent, generatorEvaluation)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorName`  
Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`generatorEvaluation` | `[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)`  
Required. The generator evaluation to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation),[GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationOperationMetadata)>` |   
  
### createGeneratorEvaluationAsync(CreateGeneratorEvaluationRequest request)
    
    
    public final OperationFuture<GeneratorEvaluation,GeneratorEvaluationOperationMetadata> createGeneratorEvaluationAsync(CreateGeneratorEvaluationRequest request)

Creates evaluation of a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       CreateGeneratorEvaluationRequest request =
           CreateGeneratorEvaluationRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setGeneratorEvaluation(GeneratorEvaluation.newBuilder().build())
               .build();
       GeneratorEvaluation response =
           generatorEvaluationsClient.createGeneratorEvaluationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateGeneratorEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation),[GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationOperationMetadata)>` |   
  
### createGeneratorEvaluationAsync(String parent, GeneratorEvaluation generatorEvaluation)
    
    
    public final OperationFuture<GeneratorEvaluation,GeneratorEvaluationOperationMetadata> createGeneratorEvaluationAsync(String parent, GeneratorEvaluation generatorEvaluation)

Creates evaluation of a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       String parent = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString();
       GeneratorEvaluation generatorEvaluation = GeneratorEvaluation.newBuilder().build();
       GeneratorEvaluation response =
           generatorEvaluationsClient
               .createGeneratorEvaluationAsync(parent, generatorEvaluation)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`generatorEvaluation` | `[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)`  
Required. The generator evaluation to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation),[GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationOperationMetadata)>` |   
  
### createGeneratorEvaluationCallable()
    
    
    public final UnaryCallable<CreateGeneratorEvaluationRequest,Operation> createGeneratorEvaluationCallable()

Creates evaluation of a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       CreateGeneratorEvaluationRequest request =
           CreateGeneratorEvaluationRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setGeneratorEvaluation(GeneratorEvaluation.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           generatorEvaluationsClient.createGeneratorEvaluationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateGeneratorEvaluationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGeneratorEvaluationOperationCallable()
    
    
    public final OperationCallable<CreateGeneratorEvaluationRequest,GeneratorEvaluation,GeneratorEvaluationOperationMetadata> createGeneratorEvaluationOperationCallable()

Creates evaluation of a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       CreateGeneratorEvaluationRequest request =
           CreateGeneratorEvaluationRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setGeneratorEvaluation(GeneratorEvaluation.newBuilder().build())
               .build();
       OperationFuture<GeneratorEvaluation, GeneratorEvaluationOperationMetadata> future =
           generatorEvaluationsClient
               .createGeneratorEvaluationOperationCallable()
               .futureCall(request);
       // Do something.
       GeneratorEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateGeneratorEvaluationRequest),[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation),[GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationOperationMetadata)>` |   
  
### deleteGeneratorEvaluation(@Nullable GeneratorEvaluationName name)
    
    
    public final void deleteGeneratorEvaluation(@Nullable GeneratorEvaluationName name)

Deletes an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GeneratorEvaluationName name =
           GeneratorEvaluationName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]");
       generatorEvaluationsClient.deleteGeneratorEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorEvaluationName`  
Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/ evaluations/<Evaluation ID>`  
  
### deleteGeneratorEvaluation(DeleteGeneratorEvaluationRequest request)
    
    
    public final void deleteGeneratorEvaluation(DeleteGeneratorEvaluationRequest request)

Deletes an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       DeleteGeneratorEvaluationRequest request =
           DeleteGeneratorEvaluationRequest.newBuilder()
               .setName(
                   GeneratorEvaluationName.of(
                           "[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
                       .toString())
               .build();
       generatorEvaluationsClient.deleteGeneratorEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteGeneratorEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteGeneratorEvaluation(String name)
    
    
    public final void deleteGeneratorEvaluation(String name)

Deletes an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       String name =
           GeneratorEvaluationName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
               .toString();
       generatorEvaluationsClient.deleteGeneratorEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/ evaluations/<Evaluation ID>`  
  
### deleteGeneratorEvaluationCallable()
    
    
    public final UnaryCallable<DeleteGeneratorEvaluationRequest,Empty> deleteGeneratorEvaluationCallable()

Deletes an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       DeleteGeneratorEvaluationRequest request =
           DeleteGeneratorEvaluationRequest.newBuilder()
               .setName(
                   GeneratorEvaluationName.of(
                           "[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           generatorEvaluationsClient.deleteGeneratorEvaluationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteGeneratorEvaluationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGeneratorEvaluation(@Nullable GeneratorEvaluationName name)
    
    
    public final GeneratorEvaluation getGeneratorEvaluation(@Nullable GeneratorEvaluationName name)

Gets an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GeneratorEvaluationName name =
           GeneratorEvaluationName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]");
       GeneratorEvaluation response = generatorEvaluationsClient.getGeneratorEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorEvaluationName`  
Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/evaluations/<Evaluation ID>`  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)` |   
  
### getGeneratorEvaluation(GetGeneratorEvaluationRequest request)
    
    
    public final GeneratorEvaluation getGeneratorEvaluation(GetGeneratorEvaluationRequest request)

Gets an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GetGeneratorEvaluationRequest request =
           GetGeneratorEvaluationRequest.newBuilder()
               .setName(
                   GeneratorEvaluationName.of(
                           "[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
                       .toString())
               .build();
       GeneratorEvaluation response = generatorEvaluationsClient.getGeneratorEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetGeneratorEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)` |   
  
### getGeneratorEvaluation(String name)
    
    
    public final GeneratorEvaluation getGeneratorEvaluation(String name)

Gets an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       String name =
           GeneratorEvaluationName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
               .toString();
       GeneratorEvaluation response = generatorEvaluationsClient.getGeneratorEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator evaluation resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/evaluations/<Evaluation ID>`  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)` |   
  
### getGeneratorEvaluationCallable()
    
    
    public final UnaryCallable<GetGeneratorEvaluationRequest,GeneratorEvaluation> getGeneratorEvaluationCallable()

Gets an evaluation of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GetGeneratorEvaluationRequest request =
           GetGeneratorEvaluationRequest.newBuilder()
               .setName(
                   GeneratorEvaluationName.of(
                           "[PROJECT]", "[LOCATION]", "[GENERATOR]", "[EVALUATION]")
                       .toString())
               .build();
       ApiFuture<GeneratorEvaluation> future =
           generatorEvaluationsClient.getGeneratorEvaluationCallable().futureCall(request);
       // Do something.
       GeneratorEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGeneratorEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetGeneratorEvaluationRequest),[GeneratorEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluation)>` |   
  
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
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = generatorEvaluationsClient.getLocation(request);
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
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           generatorEvaluationsClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable GeneratorEvaluationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorEvaluationsSettings` |   
  
### getStub()
    
    
    public GeneratorEvaluationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorEvaluationsStub)` |   
  
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
  
### listGeneratorEvaluations(@Nullable GeneratorName parent)
    
    
    public final GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse listGeneratorEvaluations(@Nullable GeneratorName parent)

Lists evaluations of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       GeneratorName parent = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]");
       for (GeneratorEvaluation element :
           generatorEvaluationsClient.listGeneratorEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorName`  
Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>` Wildcard value `-` is supported on generator_id to list evaluations across all generators under same project.  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse)` |   
  
### listGeneratorEvaluations(ListGeneratorEvaluationsRequest request)
    
    
    public final GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse listGeneratorEvaluations(ListGeneratorEvaluationsRequest request)

Lists evaluations of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListGeneratorEvaluationsRequest request =
           ListGeneratorEvaluationsRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (GeneratorEvaluation element :
           generatorEvaluationsClient.listGeneratorEvaluations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorEvaluationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse)` |   
  
### listGeneratorEvaluations(String parent)
    
    
    public final GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse listGeneratorEvaluations(String parent)

Lists evaluations of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       String parent = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString();
       for (GeneratorEvaluation element :
           generatorEvaluationsClient.listGeneratorEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator resource name. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>` Wildcard value `-` is supported on generator_id to list evaluations across all generators under same project.  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse)` |   
  
### listGeneratorEvaluationsCallable()
    
    
    public final UnaryCallable<ListGeneratorEvaluationsRequest,ListGeneratorEvaluationsResponse> listGeneratorEvaluationsCallable()

Lists evaluations of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListGeneratorEvaluationsRequest request =
           ListGeneratorEvaluationsRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGeneratorEvaluationsResponse response =
             generatorEvaluationsClient.listGeneratorEvaluationsCallable().call(request);
         for (GeneratorEvaluation element : response.getGeneratorEvaluationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorEvaluationsRequest),[ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorEvaluationsResponse)>` |   
  
### listGeneratorEvaluationsPagedCallable()
    
    
    public final UnaryCallable<ListGeneratorEvaluationsRequest,GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse> listGeneratorEvaluationsPagedCallable()

Lists evaluations of generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListGeneratorEvaluationsRequest request =
           ListGeneratorEvaluationsRequest.newBuilder()
               .setParent(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<GeneratorEvaluation> future =
           generatorEvaluationsClient.listGeneratorEvaluationsPagedCallable().futureCall(request);
       // Do something.
       for (GeneratorEvaluation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorEvaluationsRequest),[ListGeneratorEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListGeneratorEvaluationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final GeneratorEvaluationsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : generatorEvaluationsClient.listLocations(request).iterateAll()) {
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
`[GeneratorEvaluationsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListLocationsPagedResponse)` |   
  
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
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             generatorEvaluationsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,GeneratorEvaluationsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorEvaluationsClient generatorEvaluationsClient =
         GeneratorEvaluationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           generatorEvaluationsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorEvaluationsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
