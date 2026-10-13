---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient
title: Class AutoMlClient (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:42.252836+00:00
---

# Class AutoMlClient (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AutoMlClient (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-automl/google-cloud-automl/src/main/java/com/google/cloud/automl/v1/AutoMlClient.java)| [Product Reference](https://cloud.google.com/automl/docs/)| [REST Documentation](https://cloud.google.com/automl/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/automl/docs/reference/rpc)  
---|---|---|---  
  
Service Description: AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       Dataset response = autoMlClient.getDataset(name);
     }
     

Note: close() needs to be called on the AutoMlClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataset |  Creates a dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDatasetAsync(CreateDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDatasetAsync(LocationName parent, Dataset dataset) 
  * createDatasetAsync(String parent, Dataset dataset) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDatasetOperationCallable() 
  * createDatasetCallable() 

  
GetDataset |  Gets a dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataset(GetDatasetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataset(DatasetName name) 
  * getDataset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDatasetCallable() 

  
ListDatasets |  Lists datasets in a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatasets(ListDatasetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatasets(LocationName parent) 
  * listDatasets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatasetsPagedCallable() 
  * listDatasetsCallable() 

  
UpdateDataset |  Updates a dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataset(UpdateDatasetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataset(Dataset dataset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDatasetCallable() 

  
DeleteDataset |  Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDatasetAsync(DeleteDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDatasetAsync(DatasetName name) 
  * deleteDatasetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDatasetOperationCallable() 
  * deleteDatasetCallable() 

  
ImportData |  Imports data into a dataset. For Tables this method can only be called on an empty Dataset.  For Tables: 

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDataAsync(ImportDataRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importDataAsync(DatasetName name, InputConfig inputConfig) 
  * importDataAsync(String name, InputConfig inputConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDataOperationCallable() 
  * importDataCallable() 

  
ExportData |  Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDataAsync(ExportDataRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportDataAsync(DatasetName name, OutputConfig outputConfig) 
  * exportDataAsync(String name, OutputConfig outputConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDataOperationCallable() 
  * exportDataCallable() 

  
GetAnnotationSpec |  Gets an annotation spec. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAnnotationSpec(GetAnnotationSpecRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAnnotationSpec(AnnotationSpecName name) 
  * getAnnotationSpec(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAnnotationSpecCallable() 

  
CreateModel |  Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createModelAsync(CreateModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createModelAsync(LocationName parent, Model model) 
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

  
ListModels |  Lists models. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModels(ListModelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModels(LocationName parent) 
  * listModels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelsPagedCallable() 
  * listModelsCallable() 

  
DeleteModel |  Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteModelAsync(DeleteModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteModelAsync(ModelName name) 
  * deleteModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteModelOperationCallable() 
  * deleteModelCallable() 

  
UpdateModel |  Updates a model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateModel(UpdateModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateModel(Model model, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateModelCallable() 

  
DeployModel |  Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.  Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.  Returns an empty response in the response field when it completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployModelAsync(DeployModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deployModelAsync(ModelName name) 
  * deployModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployModelOperationCallable() 
  * deployModelCallable() 

  
UndeployModel |  Undeploys a model. If the model is not deployed this method has no effect.  Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.  Returns an empty response in the response field when it completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeployModelAsync(UndeployModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeployModelAsync(ModelName name) 
  * undeployModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeployModelOperationCallable() 
  * undeployModelCallable() 

  
ExportModel |  Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.  Returns an empty response in the response field when it completes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportModelAsync(ExportModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportModelAsync(ModelName name, ModelExportOutputConfig outputConfig) 
  * exportModelAsync(String name, ModelExportOutputConfig outputConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportModelOperationCallable() 
  * exportModelCallable() 

  
GetModelEvaluation |  Gets a model evaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModelEvaluation(GetModelEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModelEvaluation(ModelEvaluationName name) 
  * getModelEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelEvaluationCallable() 

  
ListModelEvaluations |  Lists model evaluations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelEvaluations(ListModelEvaluationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelEvaluations(ModelName parent, String filter) 
  * listModelEvaluations(String parent, String filter) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelEvaluationsPagedCallable() 
  * listModelEvaluationsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AutoMlSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutoMlSettings autoMlSettings =
         AutoMlSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AutoMlClient autoMlClient = AutoMlClient.create(autoMlSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutoMlSettings autoMlSettings = AutoMlSettings.newBuilder().setEndpoint(myEndpoint).build();
     AutoMlClient autoMlClient = AutoMlClient.create(autoMlSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutoMlSettings autoMlSettings = AutoMlSettings.newHttpJsonBuilder().build();
     AutoMlClient autoMlClient = AutoMlClient.create(autoMlSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AutoMlClient

## Static Methods 

### create()
    
    
    public static final AutoMlClient create()

Constructs an instance of AutoMlClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutoMlSettings settings)
    
    
    public static final AutoMlClient create(AutoMlSettings settings)

Constructs an instance of AutoMlClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutoMlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutoMlStub stub)
    
    
    public static final AutoMlClient create(AutoMlStub stub)

Constructs an instance of AutoMlClient, using the given stub for making calls. This is for advanced usage - prefer using create(AutoMlSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutoMlStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.AutoMlStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient)` |   
  
## Constructors 

### AutoMlClient(AutoMlSettings settings)
    
    
    protected AutoMlClient(AutoMlSettings settings)

Constructs an instance of AutoMlClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutoMlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlSettings)`  
  
  
### AutoMlClient(AutoMlStub stub)
    
    
    protected AutoMlClient(AutoMlStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutoMlStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.AutoMlStub)`  
  
  
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

### createDatasetAsync(@Nullable LocationName parent, Dataset dataset)
    
    
    public final OperationFuture<Dataset,OperationMetadata> createDatasetAsync(@Nullable LocationName parent, Dataset dataset)

Creates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Dataset dataset = Dataset.newBuilder().build();
       Dataset response = autoMlClient.createDatasetAsync(parent, dataset).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.LocationName`  
Required. The resource name of the project to create the dataset for.  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)`  
Required. The dataset to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createDatasetAsync(CreateDatasetRequest request)
    
    
    public final OperationFuture<Dataset,OperationMetadata> createDatasetAsync(CreateDatasetRequest request)

Creates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       Dataset response = autoMlClient.createDatasetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createDatasetAsync(String parent, Dataset dataset)
    
    
    public final OperationFuture<Dataset,OperationMetadata> createDatasetAsync(String parent, Dataset dataset)

Creates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Dataset dataset = Dataset.newBuilder().build();
       Dataset response = autoMlClient.createDatasetAsync(parent, dataset).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the project to create the dataset for.  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)`  
Required. The dataset to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createDatasetCallable()
    
    
    public final UnaryCallable<CreateDatasetRequest,Operation> createDatasetCallable()

Creates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       ApiFuture<Operation> future = autoMlClient.createDatasetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDatasetOperationCallable()
    
    
    public final OperationCallable<CreateDatasetRequest,Dataset,OperationMetadata> createDatasetOperationCallable()

Creates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       OperationFuture<Dataset, OperationMetadata> future =
           autoMlClient.createDatasetOperationCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createModelAsync(@Nullable LocationName parent, Model model)
    
    
    public final OperationFuture<Model,OperationMetadata> createModelAsync(@Nullable LocationName parent, Model model)

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Model model = Model.newBuilder().build();
       Model response = autoMlClient.createModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.LocationName`  
Required. Resource name of the parent project where the model is being created.  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)`  
Required. The model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createModelAsync(CreateModelRequest request)
    
    
    public final OperationFuture<Model,OperationMetadata> createModelAsync(CreateModelRequest request)

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setModel(Model.newBuilder().build())
               .build();
       Model response = autoMlClient.createModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createModelAsync(String parent, Model model)
    
    
    public final OperationFuture<Model,OperationMetadata> createModelAsync(String parent, Model model)

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Model model = Model.newBuilder().build();
       Model response = autoMlClient.createModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the parent project where the model is being created.  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)`  
Required. The model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### createModelCallable()
    
    
    public final UnaryCallable<CreateModelRequest,Operation> createModelCallable()

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setModel(Model.newBuilder().build())
               .build();
       ApiFuture<Operation> future = autoMlClient.createModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createModelOperationCallable()
    
    
    public final OperationCallable<CreateModelRequest,Model,OperationMetadata> createModelOperationCallable()

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       CreateModelRequest request =
           CreateModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setModel(Model.newBuilder().build())
               .build();
       OperationFuture<Model, OperationMetadata> future =
           autoMlClient.createModelOperationCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.CreateModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteDatasetAsync(@Nullable DatasetName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDatasetAsync(@Nullable DatasetName name)

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       autoMlClient.deleteDatasetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.DatasetName`  
Required. The resource name of the dataset to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteDatasetAsync(DeleteDatasetRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDatasetAsync(DeleteDatasetRequest request)

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       autoMlClient.deleteDatasetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteDatasetAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDatasetAsync(String name)

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       autoMlClient.deleteDatasetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataset to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteDatasetCallable()
    
    
    public final UnaryCallable<DeleteDatasetRequest,Operation> deleteDatasetCallable()

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       ApiFuture<Operation> future = autoMlClient.deleteDatasetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDatasetOperationCallable()
    
    
    public final OperationCallable<DeleteDatasetRequest,Empty,OperationMetadata> deleteDatasetOperationCallable()

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.deleteDatasetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteDatasetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteModelAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteModelAsync(@Nullable ModelName name)

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       autoMlClient.deleteModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Resource name of the model being deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteModelAsync(DeleteModelRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteModelAsync(DeleteModelRequest request)

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       autoMlClient.deleteModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteModelAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteModelAsync(String name)

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       autoMlClient.deleteModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the model being deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deleteModelCallable()
    
    
    public final UnaryCallable<DeleteModelRequest,Operation> deleteModelCallable()

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future = autoMlClient.deleteModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteModelOperationCallable()
    
    
    public final OperationCallable<DeleteModelRequest,Empty,OperationMetadata> deleteModelOperationCallable()

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.deleteModelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeleteModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deployModelAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deployModelAsync(@Nullable ModelName name)

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       autoMlClient.deployModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Resource name of the model to deploy.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deployModelAsync(DeployModelRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deployModelAsync(DeployModelRequest request)

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       autoMlClient.deployModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeployModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deployModelAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deployModelAsync(String name)

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       autoMlClient.deployModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the model to deploy.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### deployModelCallable()
    
    
    public final UnaryCallable<DeployModelRequest,Operation> deployModelCallable()

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future = autoMlClient.deployModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeployModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployModelOperationCallable()
    
    
    public final OperationCallable<DeployModelRequest,Empty,OperationMetadata> deployModelOperationCallable()

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.deployModelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.DeployModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportDataAsync(@Nullable DatasetName name, OutputConfig outputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportDataAsync(@Nullable DatasetName name, OutputConfig outputConfig)

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       OutputConfig outputConfig = OutputConfig.newBuilder().build();
       autoMlClient.exportDataAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.DatasetName`  
Required. The resource name of the dataset.  
`outputConfig` | `[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OutputConfig)`  
Required. The desired output location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportDataAsync(ExportDataRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportDataAsync(ExportDataRequest request)

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setOutputConfig(OutputConfig.newBuilder().build())
               .build();
       autoMlClient.exportDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportDataAsync(String name, OutputConfig outputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportDataAsync(String name, OutputConfig outputConfig)

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       OutputConfig outputConfig = OutputConfig.newBuilder().build();
       autoMlClient.exportDataAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataset.  
`outputConfig` | `[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OutputConfig)`  
Required. The desired output location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportDataCallable()
    
    
    public final UnaryCallable<ExportDataRequest,Operation> exportDataCallable()

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setOutputConfig(OutputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = autoMlClient.exportDataCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDataOperationCallable()
    
    
    public final OperationCallable<ExportDataRequest,Empty,OperationMetadata> exportDataOperationCallable()

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setOutputConfig(OutputConfig.newBuilder().build())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.exportDataOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportDataRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportModelAsync(@Nullable ModelName name, ModelExportOutputConfig outputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportModelAsync(@Nullable ModelName name, ModelExportOutputConfig outputConfig)

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       ModelExportOutputConfig outputConfig = ModelExportOutputConfig.newBuilder().build();
       autoMlClient.exportModelAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. The resource name of the model to export.  
`outputConfig` | `[ModelExportOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelExportOutputConfig)`  
Required. The desired output location and configuration.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportModelAsync(ExportModelRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportModelAsync(ExportModelRequest request)

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ModelExportOutputConfig.newBuilder().build())
               .build();
       autoMlClient.exportModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportModelAsync(String name, ModelExportOutputConfig outputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> exportModelAsync(String name, ModelExportOutputConfig outputConfig)

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       ModelExportOutputConfig outputConfig = ModelExportOutputConfig.newBuilder().build();
       autoMlClient.exportModelAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the model to export.  
`outputConfig` | `[ModelExportOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelExportOutputConfig)`  
Required. The desired output location and configuration.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### exportModelCallable()
    
    
    public final UnaryCallable<ExportModelRequest,Operation> exportModelCallable()

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ModelExportOutputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = autoMlClient.exportModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportModelOperationCallable()
    
    
    public final OperationCallable<ExportModelRequest,Empty,OperationMetadata> exportModelOperationCallable()

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ModelExportOutputConfig.newBuilder().build())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.exportModelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExportModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### getAnnotationSpec(@Nullable AnnotationSpecName name)
    
    
    public final AnnotationSpec getAnnotationSpec(@Nullable AnnotationSpecName name)

Gets an annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       AnnotationSpecName name =
           AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]");
       AnnotationSpec response = autoMlClient.getAnnotationSpec(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.AnnotationSpecName`  
Required. The resource name of the annotation spec to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AnnotationSpec)` |   
  
### getAnnotationSpec(GetAnnotationSpecRequest request)
    
    
    public final AnnotationSpec getAnnotationSpec(GetAnnotationSpecRequest request)

Gets an annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetAnnotationSpecRequest request =
           GetAnnotationSpecRequest.newBuilder()
               .setName(
                   AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
                       .toString())
               .build();
       AnnotationSpec response = autoMlClient.getAnnotationSpec(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetAnnotationSpecRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AnnotationSpec)` |   
  
### getAnnotationSpec(String name)
    
    
    public final AnnotationSpec getAnnotationSpec(String name)

Gets an annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name =
           AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
               .toString();
       AnnotationSpec response = autoMlClient.getAnnotationSpec(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the annotation spec to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AnnotationSpec)` |   
  
### getAnnotationSpecCallable()
    
    
    public final UnaryCallable<GetAnnotationSpecRequest,AnnotationSpec> getAnnotationSpecCallable()

Gets an annotation spec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetAnnotationSpecRequest request =
           GetAnnotationSpecRequest.newBuilder()
               .setName(
                   AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
                       .toString())
               .build();
       ApiFuture<AnnotationSpec> future =
           autoMlClient.getAnnotationSpecCallable().futureCall(request);
       // Do something.
       AnnotationSpec response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetAnnotationSpecRequest),[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AnnotationSpec)>` |   
  
### getDataset(@Nullable DatasetName name)
    
    
    public final Dataset getDataset(@Nullable DatasetName name)

Gets a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       Dataset response = autoMlClient.getDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.DatasetName`  
Required. The resource name of the dataset to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)` |   
  
### getDataset(GetDatasetRequest request)
    
    
    public final Dataset getDataset(GetDatasetRequest request)

Gets a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetDatasetRequest request =
           GetDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       Dataset response = autoMlClient.getDataset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)` |   
  
### getDataset(String name)
    
    
    public final Dataset getDataset(String name)

Gets a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       Dataset response = autoMlClient.getDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataset to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)` |   
  
### getDatasetCallable()
    
    
    public final UnaryCallable<GetDatasetRequest,Dataset> getDatasetCallable()

Gets a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetDatasetRequest request =
           GetDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       ApiFuture<Dataset> future = autoMlClient.getDatasetCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)>` |   
  
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
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       Model response = autoMlClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Resource name of the model.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)` |   
  
### getModel(GetModelRequest request)
    
    
    public final Model getModel(GetModelRequest request)

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       Model response = autoMlClient.getModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)` |   
  
### getModel(String name)
    
    
    public final Model getModel(String name)

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       Model response = autoMlClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the model.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)` |   
  
### getModelCallable()
    
    
    public final UnaryCallable<GetModelRequest,Model> getModelCallable()

Gets a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Model> future = autoMlClient.getModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)>` |   
  
### getModelEvaluation(@Nullable ModelEvaluationName name)
    
    
    public final ModelEvaluation getModelEvaluation(@Nullable ModelEvaluationName name)

Gets a model evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelEvaluationName name =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[MODEL_EVALUATION]");
       ModelEvaluation response = autoMlClient.getModelEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelEvaluationName`  
Required. Resource name for the model evaluation.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelEvaluation)` |   
  
### getModelEvaluation(GetModelEvaluationRequest request)
    
    
    public final ModelEvaluation getModelEvaluation(GetModelEvaluationRequest request)

Gets a model evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetModelEvaluationRequest request =
           GetModelEvaluationRequest.newBuilder()
               .setName(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[MODEL_EVALUATION]")
                       .toString())
               .build();
       ModelEvaluation response = autoMlClient.getModelEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetModelEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelEvaluation)` |   
  
### getModelEvaluation(String name)
    
    
    public final ModelEvaluation getModelEvaluation(String name)

Gets a model evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[MODEL_EVALUATION]")
               .toString();
       ModelEvaluation response = autoMlClient.getModelEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name for the model evaluation.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelEvaluation)` |   
  
### getModelEvaluationCallable()
    
    
    public final UnaryCallable<GetModelEvaluationRequest,ModelEvaluation> getModelEvaluationCallable()

Gets a model evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       GetModelEvaluationRequest request =
           GetModelEvaluationRequest.newBuilder()
               .setName(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[MODEL_EVALUATION]")
                       .toString())
               .build();
       ApiFuture<ModelEvaluation> future =
           autoMlClient.getModelEvaluationCallable().futureCall(request);
       // Do something.
       ModelEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.GetModelEvaluationRequest),[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ModelEvaluation)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AutoMlSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.AutoMlSettings` |   
  
### getStub()
    
    
    public AutoMlStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AutoMlStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.AutoMlStub)` |   
  
### importDataAsync(@Nullable DatasetName name, InputConfig inputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> importDataAsync(@Nullable DatasetName name, InputConfig inputConfig)

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       InputConfig inputConfig = InputConfig.newBuilder().build();
       autoMlClient.importDataAsync(name, inputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.DatasetName`  
Required. Dataset name. Dataset must already exist. All imported annotations and examples will be added.  
`inputConfig` | `[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)`  
Required. The desired input location and its domain specific semantics, if any.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### importDataAsync(ImportDataRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> importDataAsync(ImportDataRequest request)

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setInputConfig(InputConfig.newBuilder().build())
               .build();
       autoMlClient.importDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### importDataAsync(String name, InputConfig inputConfig)
    
    
    public final OperationFuture<Empty,OperationMetadata> importDataAsync(String name, InputConfig inputConfig)

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       InputConfig inputConfig = InputConfig.newBuilder().build();
       autoMlClient.importDataAsync(name, inputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Dataset name. Dataset must already exist. All imported annotations and examples will be added.  
`inputConfig` | `[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.InputConfig)`  
Required. The desired input location and its domain specific semantics, if any.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### importDataCallable()
    
    
    public final UnaryCallable<ImportDataRequest,Operation> importDataCallable()

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setInputConfig(InputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = autoMlClient.importDataCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ImportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDataOperationCallable()
    
    
    public final OperationCallable<ImportDataRequest,Empty,OperationMetadata> importDataOperationCallable()

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setInputConfig(InputConfig.newBuilder().build())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.importDataOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ImportDataRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
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
  
### listDatasets(@Nullable LocationName parent)
    
    
    public final AutoMlClient.ListDatasetsPagedResponse listDatasets(@Nullable LocationName parent)

Lists datasets in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Dataset element : autoMlClient.listDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.LocationName`  
Required. The resource name of the project from which to list datasets.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListDatasetsPagedResponse)` |   
  
### listDatasets(ListDatasetsRequest request)
    
    
    public final AutoMlClient.ListDatasetsPagedResponse listDatasets(ListDatasetsRequest request)

Lists datasets in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Dataset element : autoMlClient.listDatasets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListDatasetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListDatasetsPagedResponse)` |   
  
### listDatasets(String parent)
    
    
    public final AutoMlClient.ListDatasetsPagedResponse listDatasets(String parent)

Lists datasets in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Dataset element : autoMlClient.listDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the project from which to list datasets.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListDatasetsPagedResponse)` |   
  
### listDatasetsCallable()
    
    
    public final UnaryCallable<ListDatasetsRequest,ListDatasetsResponse> listDatasetsCallable()

Lists datasets in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDatasetsResponse response = autoMlClient.listDatasetsCallable().call(request);
         for (Dataset element : response.getDatasetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListDatasetsRequest),[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListDatasetsResponse)>` |   
  
### listDatasetsPagedCallable()
    
    
    public final UnaryCallable<ListDatasetsRequest,AutoMlClient.ListDatasetsPagedResponse> listDatasetsPagedCallable()

Lists datasets in a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Dataset> future = autoMlClient.listDatasetsPagedCallable().futureCall(request);
       // Do something.
       for (Dataset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListDatasetsRequest),[ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListDatasetsPagedResponse)>` |   
  
### listModelEvaluations(@Nullable ModelName parent, String filter)
    
    
    public final AutoMlClient.ListModelEvaluationsPagedResponse listModelEvaluations(@Nullable ModelName parent, String filter)

Lists model evaluations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       String filter = "filter-1274492040";
       for (ModelEvaluation element :
           autoMlClient.listModelEvaluations(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Resource name of the model to list the model evaluations for. If modelId is set as "-", this will list model evaluations from across all models of the parent location.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. An expression for filtering the results of the request. * `annotation_spec_id` \- for =, != or existence. See example below for the last. Some examples of using the filter are: * `annotation_spec_id!=4` \--> The model evaluation was done for annotation spec with ID different than 4. * `NOT annotation_spec_id:*` \--> The model evaluation was done for aggregate of all annotation specs.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluations(ListModelEvaluationsRequest request)
    
    
    public final AutoMlClient.ListModelEvaluationsPagedResponse listModelEvaluations(ListModelEvaluationsRequest request)

Lists model evaluations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ModelEvaluation element : autoMlClient.listModelEvaluations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelEvaluationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluations(String parent, String filter)
    
    
    public final AutoMlClient.ListModelEvaluationsPagedResponse listModelEvaluations(String parent, String filter)

Lists model evaluations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       String filter = "filter-1274492040";
       for (ModelEvaluation element :
           autoMlClient.listModelEvaluations(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the model to list the model evaluations for. If modelId is set as "-", this will list model evaluations from across all models of the parent location.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. An expression for filtering the results of the request. * `annotation_spec_id` \- for =, != or existence. See example below for the last. Some examples of using the filter are: * `annotation_spec_id!=4` \--> The model evaluation was done for annotation spec with ID different than 4. * `NOT annotation_spec_id:*` \--> The model evaluation was done for aggregate of all annotation specs.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluationsCallable()
    
    
    public final UnaryCallable<ListModelEvaluationsRequest,ListModelEvaluationsResponse> listModelEvaluationsCallable()

Lists model evaluations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListModelEvaluationsResponse response =
             autoMlClient.listModelEvaluationsCallable().call(request);
         for (ModelEvaluation element : response.getModelEvaluationList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelEvaluationsRequest),[ListModelEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelEvaluationsResponse)>` |   
  
### listModelEvaluationsPagedCallable()
    
    
    public final UnaryCallable<ListModelEvaluationsRequest,AutoMlClient.ListModelEvaluationsPagedResponse> listModelEvaluationsPagedCallable()

Lists model evaluations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ModelEvaluation> future =
           autoMlClient.listModelEvaluationsPagedCallable().futureCall(request);
       // Do something.
       for (ModelEvaluation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelEvaluationsRequest),[ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelEvaluationsPagedResponse)>` |   
  
### listModels(@Nullable LocationName parent)
    
    
    public final AutoMlClient.ListModelsPagedResponse listModels(@Nullable LocationName parent)

Lists models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Model element : autoMlClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.LocationName`  
Required. Resource name of the project, from which to list the models.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelsPagedResponse)` |   
  
### listModels(ListModelsRequest request)
    
    
    public final AutoMlClient.ListModelsPagedResponse listModels(ListModelsRequest request)

Lists models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Model element : autoMlClient.listModels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelsPagedResponse)` |   
  
### listModels(String parent)
    
    
    public final AutoMlClient.ListModelsPagedResponse listModels(String parent)

Lists models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Model element : autoMlClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the project, from which to list the models.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelsPagedResponse)` |   
  
### listModelsCallable()
    
    
    public final UnaryCallable<ListModelsRequest,ListModelsResponse> listModelsCallable()

Lists models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListModelsResponse response = autoMlClient.listModelsCallable().call(request);
         for (Model element : response.getModelList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelsRequest),[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelsResponse)>` |   
  
### listModelsPagedCallable()
    
    
    public final UnaryCallable<ListModelsRequest,AutoMlClient.ListModelsPagedResponse> listModelsPagedCallable()

Lists models.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Model> future = autoMlClient.listModelsPagedCallable().futureCall(request);
       // Do something.
       for (Model element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ListModelsRequest),[ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.AutoMlClient.ListModelsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### undeployModelAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> undeployModelAsync(@Nullable ModelName name)

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       autoMlClient.undeployModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Resource name of the model to undeploy.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### undeployModelAsync(UndeployModelRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> undeployModelAsync(UndeployModelRequest request)

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       autoMlClient.undeployModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UndeployModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### undeployModelAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> undeployModelAsync(String name)

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       autoMlClient.undeployModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the model to undeploy.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### undeployModelCallable()
    
    
    public final UnaryCallable<UndeployModelRequest,Operation> undeployModelCallable()

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future = autoMlClient.undeployModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UndeployModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeployModelOperationCallable()
    
    
    public final OperationCallable<UndeployModelRequest,Empty,OperationMetadata> undeployModelOperationCallable()

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the response field when it completes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           autoMlClient.undeployModelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UndeployModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### updateDataset(Dataset dataset, FieldMask updateMask)
    
    
    public final Dataset updateDataset(Dataset dataset, FieldMask updateMask)

Updates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       Dataset dataset = Dataset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Dataset response = autoMlClient.updateDataset(dataset, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)`  
Required. The dataset which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)` |   
  
### updateDataset(UpdateDatasetRequest request)
    
    
    public final Dataset updateDataset(UpdateDatasetRequest request)

Updates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UpdateDatasetRequest request =
           UpdateDatasetRequest.newBuilder()
               .setDataset(Dataset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Dataset response = autoMlClient.updateDataset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UpdateDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)` |   
  
### updateDatasetCallable()
    
    
    public final UnaryCallable<UpdateDatasetRequest,Dataset> updateDatasetCallable()

Updates a dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UpdateDatasetRequest request =
           UpdateDatasetRequest.newBuilder()
               .setDataset(Dataset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Dataset> future = autoMlClient.updateDatasetCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UpdateDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Dataset)>` |   
  
### updateModel(Model model, FieldMask updateMask)
    
    
    public final Model updateModel(Model model, FieldMask updateMask)

Updates a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       Model model = Model.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Model response = autoMlClient.updateModel(model, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)`  
Required. The model which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)` |   
  
### updateModel(UpdateModelRequest request)
    
    
    public final Model updateModel(UpdateModelRequest request)

Updates a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UpdateModelRequest request =
           UpdateModelRequest.newBuilder()
               .setModel(Model.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Model response = autoMlClient.updateModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UpdateModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)` |   
  
### updateModelCallable()
    
    
    public final UnaryCallable<UpdateModelRequest,Model> updateModelCallable()

Updates a model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoMlClient autoMlClient = AutoMlClient.create()) {
       UpdateModelRequest request =
           UpdateModelRequest.newBuilder()
               .setModel(Model.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Model> future = autoMlClient.updateModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.UpdateModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.Model)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
