---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient
title: Class GeneratorsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:43.280676+00:00
---

# Class GeneratorsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GeneratorsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/GeneratorsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Generator generator = Generator.newBuilder().build();
       String generatorId = "generatorId887044942";
       Generator response = generatorsClient.createGenerator(parent, generator, generatorId);
     }
     

Note: close() needs to be called on the GeneratorsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateGenerator |  Creates a generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGenerator(CreateGeneratorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createGenerator(ProjectName parent, Generator generator, String generatorId) 
  * createGenerator(String parent, Generator generator, String generatorId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGeneratorCallable() 

  
GetGenerator |  Retrieves a generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGenerator(GetGeneratorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGenerator(GeneratorName name) 
  * getGenerator(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGeneratorCallable() 

  
ListGenerators |  Lists generators. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGenerators(ListGeneratorsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGenerators(ProjectName parent) 
  * listGenerators(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGeneratorsPagedCallable() 
  * listGeneratorsCallable() 

  
DeleteGenerator |  Deletes a generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGenerator(DeleteGeneratorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteGenerator(GeneratorName name) 
  * deleteGenerator(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGeneratorCallable() 

  
UpdateGenerator |  Updates a generator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGenerator(UpdateGeneratorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateGenerator(Generator generator, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGeneratorCallable() 

  
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

This class can be customized by passing in a custom instance of GeneratorsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorsSettings generatorsSettings =
         GeneratorsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GeneratorsClient generatorsClient = GeneratorsClient.create(generatorsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorsSettings generatorsSettings =
         GeneratorsSettings.newBuilder().setEndpoint(myEndpoint).build();
     GeneratorsClient generatorsClient = GeneratorsClient.create(generatorsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeneratorsSettings generatorsSettings = GeneratorsSettings.newHttpJsonBuilder().build();
     GeneratorsClient generatorsClient = GeneratorsClient.create(generatorsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GeneratorsClient

## Static Methods 

### create()
    
    
    public static final GeneratorsClient create()

Constructs an instance of GeneratorsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeneratorsSettings settings)
    
    
    public static final GeneratorsClient create(GeneratorsSettings settings)

Constructs an instance of GeneratorsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeneratorsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeneratorsStub stub)
    
    
    public static final GeneratorsClient create(GeneratorsStub stub)

Constructs an instance of GeneratorsClient, using the given stub for making calls. This is for advanced usage - prefer using create(GeneratorsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeneratorsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient)` |   
  
## Constructors 

### GeneratorsClient(GeneratorsSettings settings)
    
    
    protected GeneratorsClient(GeneratorsSettings settings)

Constructs an instance of GeneratorsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeneratorsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsSettings)`  
  
  
### GeneratorsClient(GeneratorsStub stub)
    
    
    protected GeneratorsClient(GeneratorsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeneratorsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorsStub)`  
  
  
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

### createGenerator(@Nullable ProjectName parent, Generator generator, String generatorId)
    
    
    public final Generator createGenerator(@Nullable ProjectName parent, Generator generator, String generatorId)

Creates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Generator generator = Generator.newBuilder().build();
       String generatorId = "generatorId887044942";
       Generator response = generatorsClient.createGenerator(parent, generator, generatorId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)`  
Required. The generator to create.  
`generatorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `a-zA-Z*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for 1. the uniqueness of the ID, otherwise the request will be rejected. 2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### createGenerator(CreateGeneratorRequest request)
    
    
    public final Generator createGenerator(CreateGeneratorRequest request)

Creates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       CreateGeneratorRequest request =
           CreateGeneratorRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setGenerator(Generator.newBuilder().build())
               .setGeneratorId("generatorId887044942")
               .build();
       Generator response = generatorsClient.createGenerator(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### createGenerator(String parent, Generator generator, String generatorId)
    
    
    public final Generator createGenerator(String parent, Generator generator, String generatorId)

Creates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Generator generator = Generator.newBuilder().build();
       String generatorId = "generatorId887044942";
       Generator response = generatorsClient.createGenerator(parent, generator, generatorId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project/location to create generator for. Format: `projects/<Project ID>/locations/<Location ID>`  
`generator` | `[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)`  
Required. The generator to create.  
`generatorId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the generator, which will become the final component of the generator's resource name. The generator ID must be compliant with the regression formula `a-zA-Z*` with the characters length in range of [3,64]. If the field is not provided, an Id will be auto-generated. If the field is provided, the caller is responsible for 1. the uniqueness of the ID, otherwise the request will be rejected. 2. the consistency for whether to use custom ID or not under a project to better ensure uniqueness.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### createGeneratorCallable()
    
    
    public final UnaryCallable<CreateGeneratorRequest,Generator> createGeneratorCallable()

Creates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       CreateGeneratorRequest request =
           CreateGeneratorRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setGenerator(Generator.newBuilder().build())
               .setGeneratorId("generatorId887044942")
               .build();
       ApiFuture<Generator> future = generatorsClient.createGeneratorCallable().futureCall(request);
       // Do something.
       Generator response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateGeneratorRequest),[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)>` |   
  
### deleteGenerator(@Nullable GeneratorName name)
    
    
    public final void deleteGenerator(@Nullable GeneratorName name)

Deletes a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GeneratorName name = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]");
       generatorsClient.deleteGenerator(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorName`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
  
### deleteGenerator(DeleteGeneratorRequest request)
    
    
    public final void deleteGenerator(DeleteGeneratorRequest request)

Deletes a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       DeleteGeneratorRequest request =
           DeleteGeneratorRequest.newBuilder()
               .setName(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .build();
       generatorsClient.deleteGenerator(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteGenerator(String name)
    
    
    public final void deleteGenerator(String name)

Deletes a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       String name = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString();
       generatorsClient.deleteGenerator(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator resource name to delete. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
  
### deleteGeneratorCallable()
    
    
    public final UnaryCallable<DeleteGeneratorRequest,Empty> deleteGeneratorCallable()

Deletes a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       DeleteGeneratorRequest request =
           DeleteGeneratorRequest.newBuilder()
               .setName(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .build();
       ApiFuture<Empty> future = generatorsClient.deleteGeneratorCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteGeneratorRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGenerator(@Nullable GeneratorName name)
    
    
    public final Generator getGenerator(@Nullable GeneratorName name)

Retrieves a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GeneratorName name = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]");
       Generator response = generatorsClient.getGenerator(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorName`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### getGenerator(GetGeneratorRequest request)
    
    
    public final Generator getGenerator(GetGeneratorRequest request)

Retrieves a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GetGeneratorRequest request =
           GetGeneratorRequest.newBuilder()
               .setName(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .build();
       Generator response = generatorsClient.getGenerator(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### getGenerator(String name)
    
    
    public final Generator getGenerator(String name)

Retrieves a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       String name = GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString();
       Generator response = generatorsClient.getGenerator(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The generator resource name to retrieve. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### getGeneratorCallable()
    
    
    public final UnaryCallable<GetGeneratorRequest,Generator> getGeneratorCallable()

Retrieves a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GetGeneratorRequest request =
           GetGeneratorRequest.newBuilder()
               .setName(GeneratorName.of("[PROJECT]", "[LOCATION]", "[GENERATOR]").toString())
               .build();
       ApiFuture<Generator> future = generatorsClient.getGeneratorCallable().futureCall(request);
       // Do something.
       Generator response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetGeneratorRequest),[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = generatorsClient.getLocation(request);
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
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = generatorsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable GeneratorsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.GeneratorsSettings` |   
  
### getStub()
    
    
    public GeneratorsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GeneratorsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.GeneratorsStub)` |   
  
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
  
### listGenerators(@Nullable ProjectName parent)
    
    
    public final GeneratorsClient.ListGeneratorsPagedResponse listGenerators(@Nullable ProjectName parent)

Lists generators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Generator element : generatorsClient.listGenerators(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient.ListGeneratorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListGeneratorsPagedResponse)` |   
  
### listGenerators(ListGeneratorsRequest request)
    
    
    public final GeneratorsClient.ListGeneratorsPagedResponse listGenerators(ListGeneratorsRequest request)

Lists generators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListGeneratorsRequest request =
           ListGeneratorsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Generator element : generatorsClient.listGenerators(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGeneratorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient.ListGeneratorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListGeneratorsPagedResponse)` |   
  
### listGenerators(String parent)
    
    
    public final GeneratorsClient.ListGeneratorsPagedResponse listGenerators(String parent)

Lists generators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (Generator element : generatorsClient.listGenerators(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project/location to list generators for. Format: `projects/<Project ID>/locations/<Location ID>`  
**Returns**  
---  
**Type** | **Description**  
`[GeneratorsClient.ListGeneratorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListGeneratorsPagedResponse)` |   
  
### listGeneratorsCallable()
    
    
    public final UnaryCallable<ListGeneratorsRequest,ListGeneratorsResponse> listGeneratorsCallable()

Lists generators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListGeneratorsRequest request =
           ListGeneratorsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGeneratorsResponse response = generatorsClient.listGeneratorsCallable().call(request);
         for (Generator element : response.getGeneratorsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeneratorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorsRequest),[ListGeneratorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorsResponse)>` |   
  
### listGeneratorsPagedCallable()
    
    
    public final UnaryCallable<ListGeneratorsRequest,GeneratorsClient.ListGeneratorsPagedResponse> listGeneratorsPagedCallable()

Lists generators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListGeneratorsRequest request =
           ListGeneratorsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Generator> future =
           generatorsClient.listGeneratorsPagedCallable().futureCall(request);
       // Do something.
       for (Generator element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeneratorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListGeneratorsRequest),[ListGeneratorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListGeneratorsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final GeneratorsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : generatorsClient.listLocations(request).iterateAll()) {
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
`[GeneratorsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListLocationsPagedResponse)` |   
  
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
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = generatorsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,GeneratorsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           generatorsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GeneratorsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateGenerator(Generator generator, FieldMask updateMask)
    
    
    public final Generator updateGenerator(Generator generator, FieldMask updateMask)

Updates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       Generator generator = Generator.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Generator response = generatorsClient.updateGenerator(generator, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`generator` | `[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)`  
Required. The generator to update. The name field of generator is to identify the generator to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### updateGenerator(UpdateGeneratorRequest request)
    
    
    public final Generator updateGenerator(UpdateGeneratorRequest request)

Updates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       UpdateGeneratorRequest request =
           UpdateGeneratorRequest.newBuilder()
               .setGenerator(Generator.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Generator response = generatorsClient.updateGenerator(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateGeneratorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)` |   
  
### updateGeneratorCallable()
    
    
    public final UnaryCallable<UpdateGeneratorRequest,Generator> updateGeneratorCallable()

Updates a generator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeneratorsClient generatorsClient = GeneratorsClient.create()) {
       UpdateGeneratorRequest request =
           UpdateGeneratorRequest.newBuilder()
               .setGenerator(Generator.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Generator> future = generatorsClient.updateGeneratorCallable().futureCall(request);
       // Do something.
       Generator response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGeneratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateGeneratorRequest),[Generator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Generator)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
