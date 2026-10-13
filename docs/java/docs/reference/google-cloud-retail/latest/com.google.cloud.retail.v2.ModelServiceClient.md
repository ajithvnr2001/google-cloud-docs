---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient
title: Class ModelServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:23.483999+00:00
---

# Class ModelServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ModelServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/ModelServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for performing CRUD operations on models. Recommendation models contain all the metadata necessary to generate a set of models for the `Predict()` API. A model is queried indirectly via a ServingConfig, which associates a model with a given Placement (e.g. Frequently Bought Together on Home Page).

This service allows you to do the following:

  * Initiate training of a model. 
  * Pause training of an existing model. 
  * List all the available models along with their metadata. 
  * Control their tuning schedule. 



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]");
       Model response = modelServiceClient.getModel(name);
     }
     

Note: close() needs to be called on the ModelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateModel |  Creates a new model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createModelAsync(CreateModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createModelAsync(CatalogName parent, Model model) 
  * createModelAsync(String parent, Model model) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createModelOperationCallable() 
  * createModelCallable() 

  
GetModel |  Gets a model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModel(GetModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModel(ModelName name) 
  * getModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelCallable() 

  
PauseModel |  Pauses the training of an existing model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pauseModel(PauseModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * pauseModel(ModelName name) 
  * pauseModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pauseModelCallable() 

  
ResumeModel |  Resumes the training of an existing model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeModel(ResumeModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resumeModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeModelCallable() 

  
DeleteModel |  Deletes an existing model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteModel(DeleteModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteModel(ModelName name) 
  * deleteModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteModelCallable() 

  
ListModels |  Lists all the models linked to this event store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModels(ListModelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModels(CatalogName parent) 
  * listModels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelsPagedCallable() 
  * listModelsCallable() 

  
UpdateModel |  Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateModel(UpdateModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateModel(Model model, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateModelCallable() 

  
TuneModel |  Tunes an existing model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * tuneModelAsync(TuneModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * tuneModelAsync(ModelName name) 
  * tuneModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * tuneModelOperationCallable() 
  * tuneModelCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ModelServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ModelServiceSettings modelServiceSettings =
         ModelServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ModelServiceClient modelServiceClient = ModelServiceClient.create(modelServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ModelServiceSettings modelServiceSettings =
         ModelServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ModelServiceClient modelServiceClient = ModelServiceClient.create(modelServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ModelServiceSettings modelServiceSettings = ModelServiceSettings.newHttpJsonBuilder().build();
     ModelServiceClient modelServiceClient = ModelServiceClient.create(modelServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ModelServiceClient

## Static Methods 

### create()
    
    
    public static final ModelServiceClient create()

Constructs an instance of ModelServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ModelServiceSettings settings)
    
    
    public static final ModelServiceClient create(ModelServiceSettings settings)

Constructs an instance of ModelServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ModelServiceStub stub)
    
    
    public static final ModelServiceClient create(ModelServiceStub stub)

Constructs an instance of ModelServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ModelServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ModelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient)` |   
  
## Constructors 

### ModelServiceClient(ModelServiceSettings settings)
    
    
    protected ModelServiceClient(ModelServiceSettings settings)

Constructs an instance of ModelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceSettings)`  
  
  
### ModelServiceClient(ModelServiceStub stub)
    
    
    protected ModelServiceClient(ModelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ModelServiceStub)`  
  
  
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

### createModelAsync(@Nullable CatalogName parent, Model model)
    
    
    public final OperationFuture<Model,CreateModelMetadata> createModelAsync(@Nullable CatalogName parent, Model model)

Creates a new model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       Model model = Model.newBuilder().build();
       Model response = modelServiceClient.createModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. The parent resource under which to create the model. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)`  
Required. The payload of the Model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model),[CreateModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelMetadata)>` |   
  
### createModelAsync(CreateModelRequest request)
    
    
    public final OperationFuture<Model,CreateModelMetadata> createModelAsync(CreateModelRequest request)

Creates a new model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setModel(Model.newBuilder().build())
               .setDryRun(true)
               .build();
       Model response = modelServiceClient.createModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model),[CreateModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelMetadata)>` |   
  
### createModelAsync(String parent, Model model)
    
    
    public final OperationFuture<Model,CreateModelMetadata> createModelAsync(String parent, Model model)

Creates a new model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       Model model = Model.newBuilder().build();
       Model response = modelServiceClient.createModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource under which to create the model. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)`  
Required. The payload of the Model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model),[CreateModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelMetadata)>` |   
  
### createModelCallable()
    
    
    public final UnaryCallable<CreateModelRequest,Operation> createModelCallable()

Creates a new model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setModel(Model.newBuilder().build())
               .setDryRun(true)
               .build();
       ApiFuture<Operation> future = modelServiceClient.createModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createModelOperationCallable()
    
    
    public final OperationCallable<CreateModelRequest,Model,CreateModelMetadata> createModelOperationCallable()

Creates a new model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setModel(Model.newBuilder().build())
               .setDryRun(true)
               .build();
       OperationFuture<Model, CreateModelMetadata> future =
           modelServiceClient.createModelOperationCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model),[CreateModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateModelMetadata)>` |   
  
### deleteModel(@Nullable ModelName name)
    
    
    public final void deleteModel(@Nullable ModelName name)

Deletes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]");
       modelServiceClient.deleteModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ModelName`  
Required. The resource name of the Model to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
  
### deleteModel(DeleteModelRequest request)
    
    
    public final void deleteModel(DeleteModelRequest request)

Deletes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       modelServiceClient.deleteModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteModelRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteModel(String name)
    
    
    public final void deleteModel(String name)

Deletes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString();
       modelServiceClient.deleteModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
  
### deleteModelCallable()
    
    
    public final UnaryCallable<DeleteModelRequest,Empty> deleteModelCallable()

Deletes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       ApiFuture<Empty> future = modelServiceClient.deleteModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getModel(@Nullable ModelName name)
    
    
    public final Model getModel(@Nullable ModelName name)

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]");
       Model response = modelServiceClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ModelName`  
Required. The resource name of the Model to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### getModel(GetModelRequest request)
    
    
    public final Model getModel(GetModelRequest request)

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       Model response = modelServiceClient.getModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### getModel(String name)
    
    
    public final Model getModel(String name)

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString();
       Model response = modelServiceClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### getModelCallable()
    
    
    public final UnaryCallable<GetModelRequest,Model> getModelCallable()

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       ApiFuture<Model> future = modelServiceClient.getModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable ModelServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ModelServiceSettings` |   
  
### getStub()
    
    
    public ModelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ModelServiceStub)` |   
  
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
  
### listModels(@Nullable CatalogName parent)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(@Nullable CatalogName parent)

Lists all the models linked to this event store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       for (Model element : modelServiceClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. The parent for which to list models. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModels(ListModelsRequest request)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(ListModelsRequest request)

Lists all the models linked to this event store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Model element : modelServiceClient.listModels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModels(String parent)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(String parent)

Lists all the models linked to this event store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       for (Model element : modelServiceClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent for which to list models. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModelsCallable()
    
    
    public final UnaryCallable<ListModelsRequest,ListModelsResponse> listModelsCallable()

Lists all the models linked to this event store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListModelsResponse response = modelServiceClient.listModelsCallable().call(request);
         for (Model element : response.getModelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListModelsRequest),[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListModelsResponse)>` |   
  
### listModelsPagedCallable()
    
    
    public final UnaryCallable<ListModelsRequest,ModelServiceClient.ListModelsPagedResponse> listModelsPagedCallable()

Lists all the models linked to this event store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Model> future = modelServiceClient.listModelsPagedCallable().futureCall(request);
       // Do something.
       for (Model element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListModelsRequest),[ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ModelServiceClient.ListModelsPagedResponse)>` |   
  
### pauseModel(@Nullable ModelName name)
    
    
    public final Model pauseModel(@Nullable ModelName name)

Pauses the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]");
       Model response = modelServiceClient.pauseModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ModelName`  
Required. The name of the model to pause. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### pauseModel(PauseModelRequest request)
    
    
    public final Model pauseModel(PauseModelRequest request)

Pauses the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       PauseModelRequest request =
           PauseModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       Model response = modelServiceClient.pauseModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PauseModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PauseModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### pauseModel(String name)
    
    
    public final Model pauseModel(String name)

Pauses the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString();
       Model response = modelServiceClient.pauseModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model to pause. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### pauseModelCallable()
    
    
    public final UnaryCallable<PauseModelRequest,Model> pauseModelCallable()

Pauses the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       PauseModelRequest request =
           PauseModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       ApiFuture<Model> future = modelServiceClient.pauseModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PauseModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PauseModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)>` |   
  
### resumeModel(ResumeModelRequest request)
    
    
    public final Model resumeModel(ResumeModelRequest request)

Resumes the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ResumeModelRequest request = ResumeModelRequest.newBuilder().setName("name3373707").build();
       Model response = modelServiceClient.resumeModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ResumeModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### resumeModel(String name)
    
    
    public final Model resumeModel(String name)

Resumes the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = "name3373707";
       Model response = modelServiceClient.resumeModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model to resume. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### resumeModelCallable()
    
    
    public final UnaryCallable<ResumeModelRequest,Model> resumeModelCallable()

Resumes the training of an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ResumeModelRequest request = ResumeModelRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Model> future = modelServiceClient.resumeModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ResumeModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### tuneModelAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<TuneModelResponse,TuneModelMetadata> tuneModelAsync(@Nullable ModelName name)

Tunes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]");
       TuneModelResponse response = modelServiceClient.tuneModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ModelName`  
Required. The resource name of the model to tune. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TuneModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelResponse),[TuneModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelMetadata)>` |   
  
### tuneModelAsync(TuneModelRequest request)
    
    
    public final OperationFuture<TuneModelResponse,TuneModelMetadata> tuneModelAsync(TuneModelRequest request)

Tunes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       TuneModelRequest request =
           TuneModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       TuneModelResponse response = modelServiceClient.tuneModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TuneModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TuneModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelResponse),[TuneModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelMetadata)>` |   
  
### tuneModelAsync(String name)
    
    
    public final OperationFuture<TuneModelResponse,TuneModelMetadata> tuneModelAsync(String name)

Tunes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString();
       TuneModelResponse response = modelServiceClient.tuneModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the model to tune. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TuneModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelResponse),[TuneModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelMetadata)>` |   
  
### tuneModelCallable()
    
    
    public final UnaryCallable<TuneModelRequest,Operation> tuneModelCallable()

Tunes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       TuneModelRequest request =
           TuneModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future = modelServiceClient.tuneModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TuneModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### tuneModelOperationCallable()
    
    
    public final OperationCallable<TuneModelRequest,TuneModelResponse,TuneModelMetadata> tuneModelOperationCallable()

Tunes an existing model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       TuneModelRequest request =
           TuneModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[MODEL]").toString())
               .build();
       OperationFuture<TuneModelResponse, TuneModelMetadata> future =
           modelServiceClient.tuneModelOperationCallable().futureCall(request);
       // Do something.
       TuneModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TuneModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelRequest),[TuneModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelResponse),[TuneModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.TuneModelMetadata)>` |   
  
### updateModel(Model model, FieldMask updateMask)
    
    
    public final Model updateModel(Model model, FieldMask updateMask)

Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       Model model = Model.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Model response = modelServiceClient.updateModel(model, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)`  
Required. The body of the updated Model.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Indicates which fields in the provided 'model' to update. If not set, by default updates all fields.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### updateModel(UpdateModelRequest request)
    
    
    public final Model updateModel(UpdateModelRequest request)

Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UpdateModelRequest request =
           UpdateModelRequest.newBuilder()
               .setModel(Model.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Model response = modelServiceClient.updateModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)` |   
  
### updateModelCallable()
    
    
    public final UnaryCallable<UpdateModelRequest,Model> updateModelCallable()

Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UpdateModelRequest request =
           UpdateModelRequest.newBuilder()
               .setModel(Model.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Model> future = modelServiceClient.updateModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Model)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
