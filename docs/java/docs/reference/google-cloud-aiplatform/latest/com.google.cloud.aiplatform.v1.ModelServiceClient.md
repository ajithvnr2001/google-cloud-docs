---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient
title: Class ModelServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:22.561129+00:00
---

# Class ModelServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ModelServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/ModelServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing Vertex AI's machine learning Models.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       Model response = modelServiceClient.getModel(name);
     }
     

Note: close() needs to be called on the ModelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UploadModel |  Uploads a Model artifact into Vertex AI. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * uploadModelAsync(UploadModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * uploadModelAsync(LocationName parent, Model model) 
  * uploadModelAsync(String parent, Model model) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * uploadModelOperationCallable() 
  * uploadModelCallable() 

  
GetModel |  Gets a Model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModel(GetModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModel(ModelName name) 
  * getModel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelCallable() 

  
ListModels |  Lists Models in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModels(ListModelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModels(LocationName parent) 
  * listModels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelsPagedCallable() 
  * listModelsCallable() 

  
ListModelVersions |  Lists versions of the specified model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelVersions(ListModelVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelVersions(ModelName name) 
  * listModelVersions(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelVersionsPagedCallable() 
  * listModelVersionsCallable() 

  
ListModelVersionCheckpoints |  Lists checkpoints of the specified model version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelVersionCheckpoints(ListModelVersionCheckpointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelVersionCheckpoints(ModelName name) 
  * listModelVersionCheckpoints(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelVersionCheckpointsPagedCallable() 
  * listModelVersionCheckpointsCallable() 

  
UpdateModel |  Updates a Model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateModel(UpdateModelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateModel(Model model, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateModelCallable() 

  
UpdateExplanationDataset |  Incrementally update the dataset used for an examples model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExplanationDatasetAsync(UpdateExplanationDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateExplanationDatasetAsync(ModelName model) 
  * updateExplanationDatasetAsync(String model) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExplanationDatasetOperationCallable() 
  * updateExplanationDatasetCallable() 

  
DeleteModel |  Deletes a Model.  A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteModelAsync(DeleteModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteModelAsync(ModelName name) 
  * deleteModelAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteModelOperationCallable() 
  * deleteModelCallable() 

  
DeleteModelVersion |  Deletes a Model version.  Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteModelVersionAsync(DeleteModelVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteModelVersionAsync(ModelName name) 
  * deleteModelVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteModelVersionOperationCallable() 
  * deleteModelVersionCallable() 

  
MergeVersionAliases |  Merges a set of aliases for a Model version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * mergeVersionAliases(MergeVersionAliasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * mergeVersionAliases(ModelName name, List<String> versionAliases) 
  * mergeVersionAliases(String name, List<String> versionAliases) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * mergeVersionAliasesCallable() 

  
ExportModel |  Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportModelAsync(ExportModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportModelAsync(ModelName name, ExportModelRequest.OutputConfig outputConfig) 
  * exportModelAsync(String name, ExportModelRequest.OutputConfig outputConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportModelOperationCallable() 
  * exportModelCallable() 

  
CopyModel |  Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * copyModelAsync(CopyModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * copyModelAsync(LocationName parent, ModelName sourceModel) 
  * copyModelAsync(LocationName parent, String sourceModel) 
  * copyModelAsync(String parent, ModelName sourceModel) 
  * copyModelAsync(String parent, String sourceModel) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * copyModelOperationCallable() 
  * copyModelCallable() 

  
ImportModelEvaluation |  Imports an externally generated ModelEvaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importModelEvaluation(ImportModelEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * importModelEvaluation(ModelName parent, ModelEvaluation modelEvaluation) 
  * importModelEvaluation(String parent, ModelEvaluation modelEvaluation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importModelEvaluationCallable() 

  
BatchImportModelEvaluationSlices |  Imports a list of externally generated ModelEvaluationSlice. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchImportModelEvaluationSlices(BatchImportModelEvaluationSlicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchImportModelEvaluationSlices(ModelEvaluationName parent, List<ModelEvaluationSlice> modelEvaluationSlices) 
  * batchImportModelEvaluationSlices(String parent, List<ModelEvaluationSlice> modelEvaluationSlices) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchImportModelEvaluationSlicesCallable() 

  
BatchImportEvaluatedAnnotations |  Imports a list of externally generated EvaluatedAnnotations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchImportEvaluatedAnnotations(BatchImportEvaluatedAnnotationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchImportEvaluatedAnnotations(ModelEvaluationSliceName parent, List<EvaluatedAnnotation> evaluatedAnnotations) 
  * batchImportEvaluatedAnnotations(String parent, List<EvaluatedAnnotation> evaluatedAnnotations) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchImportEvaluatedAnnotationsCallable() 

  
GetModelEvaluation |  Gets a ModelEvaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModelEvaluation(GetModelEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModelEvaluation(ModelEvaluationName name) 
  * getModelEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelEvaluationCallable() 

  
ListModelEvaluations |  Lists ModelEvaluations in a Model. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelEvaluations(ListModelEvaluationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelEvaluations(ModelName parent) 
  * listModelEvaluations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelEvaluationsPagedCallable() 
  * listModelEvaluationsCallable() 

  
GetModelEvaluationSlice |  Gets a ModelEvaluationSlice. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModelEvaluationSlice(GetModelEvaluationSliceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModelEvaluationSlice(ModelEvaluationSliceName name) 
  * getModelEvaluationSlice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelEvaluationSliceCallable() 

  
ListModelEvaluationSlices |  Lists ModelEvaluationSlices in a ModelEvaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelEvaluationSlices(ListModelEvaluationSlicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelEvaluationSlices(ModelEvaluationName parent) 
  * listModelEvaluationSlices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelEvaluationSlicesPagedCallable() 
  * listModelEvaluationSlicesCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
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
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient)` |   
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
`settings` | `[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient)` |   
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
`stub` | `[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ModelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient)` |   
  
## Constructors 

### ModelServiceClient(ModelServiceSettings settings)
    
    
    protected ModelServiceClient(ModelServiceSettings settings)

Constructs an instance of ModelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings)`  
  
  
### ModelServiceClient(ModelServiceStub stub)
    
    
    protected ModelServiceClient(ModelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ModelServiceStub)`  
  
  
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
  
### batchImportEvaluatedAnnotations(@Nullable ModelEvaluationSliceName parent, List<EvaluatedAnnotation> evaluatedAnnotations)
    
    
    public final BatchImportEvaluatedAnnotationsResponse batchImportEvaluatedAnnotations(@Nullable ModelEvaluationSliceName parent, List<EvaluatedAnnotation> evaluatedAnnotations)

Imports a list of externally generated EvaluatedAnnotations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelEvaluationSliceName parent =
           ModelEvaluationSliceName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]");
       List<EvaluatedAnnotation> evaluatedAnnotations = new ArrayList<>();
       BatchImportEvaluatedAnnotationsResponse response =
           modelServiceClient.batchImportEvaluatedAnnotations(parent, evaluatedAnnotations);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelEvaluationSliceName`  
Required. The name of the parent ModelEvaluationSlice resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}`  
`evaluatedAnnotations` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EvaluatedAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EvaluatedAnnotation)>`  
Required. Evaluated annotations resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportEvaluatedAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse)` |   
  
### batchImportEvaluatedAnnotations(BatchImportEvaluatedAnnotationsRequest request)
    
    
    public final BatchImportEvaluatedAnnotationsResponse batchImportEvaluatedAnnotations(BatchImportEvaluatedAnnotationsRequest request)

Imports a list of externally generated EvaluatedAnnotations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       BatchImportEvaluatedAnnotationsRequest request =
           BatchImportEvaluatedAnnotationsRequest.newBuilder()
               .setParent(
                   ModelEvaluationSliceName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
                       .toString())
               .addAllEvaluatedAnnotations(new ArrayList<EvaluatedAnnotation>())
               .build();
       BatchImportEvaluatedAnnotationsResponse response =
           modelServiceClient.batchImportEvaluatedAnnotations(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchImportEvaluatedAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportEvaluatedAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse)` |   
  
### batchImportEvaluatedAnnotations(String parent, List<EvaluatedAnnotation> evaluatedAnnotations)
    
    
    public final BatchImportEvaluatedAnnotationsResponse batchImportEvaluatedAnnotations(String parent, List<EvaluatedAnnotation> evaluatedAnnotations)

Imports a list of externally generated EvaluatedAnnotations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent =
           ModelEvaluationSliceName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
               .toString();
       List<EvaluatedAnnotation> evaluatedAnnotations = new ArrayList<>();
       BatchImportEvaluatedAnnotationsResponse response =
           modelServiceClient.batchImportEvaluatedAnnotations(parent, evaluatedAnnotations);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent ModelEvaluationSlice resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}`  
`evaluatedAnnotations` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EvaluatedAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EvaluatedAnnotation)>`  
Required. Evaluated annotations resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportEvaluatedAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse)` |   
  
### batchImportEvaluatedAnnotationsCallable()
    
    
    public final UnaryCallable<BatchImportEvaluatedAnnotationsRequest,BatchImportEvaluatedAnnotationsResponse> batchImportEvaluatedAnnotationsCallable()

Imports a list of externally generated EvaluatedAnnotations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       BatchImportEvaluatedAnnotationsRequest request =
           BatchImportEvaluatedAnnotationsRequest.newBuilder()
               .setParent(
                   ModelEvaluationSliceName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
                       .toString())
               .addAllEvaluatedAnnotations(new ArrayList<EvaluatedAnnotation>())
               .build();
       ApiFuture<BatchImportEvaluatedAnnotationsResponse> future =
           modelServiceClient.batchImportEvaluatedAnnotationsCallable().futureCall(request);
       // Do something.
       BatchImportEvaluatedAnnotationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchImportEvaluatedAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsRequest),[BatchImportEvaluatedAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse)>` |   
  
### batchImportModelEvaluationSlices(@Nullable ModelEvaluationName parent, List<ModelEvaluationSlice> modelEvaluationSlices)
    
    
    public final BatchImportModelEvaluationSlicesResponse batchImportModelEvaluationSlices(@Nullable ModelEvaluationName parent, List<ModelEvaluationSlice> modelEvaluationSlices)

Imports a list of externally generated ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelEvaluationName parent =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]");
       List<ModelEvaluationSlice> modelEvaluationSlices = new ArrayList<>();
       BatchImportModelEvaluationSlicesResponse response =
           modelServiceClient.batchImportModelEvaluationSlices(parent, modelEvaluationSlices);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelEvaluationName`  
Required. The name of the parent ModelEvaluation resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
`modelEvaluationSlices` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)>`  
Required. Model evaluation slice resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse)` |   
  
### batchImportModelEvaluationSlices(BatchImportModelEvaluationSlicesRequest request)
    
    
    public final BatchImportModelEvaluationSlicesResponse batchImportModelEvaluationSlices(BatchImportModelEvaluationSlicesRequest request)

Imports a list of externally generated ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       BatchImportModelEvaluationSlicesRequest request =
           BatchImportModelEvaluationSlicesRequest.newBuilder()
               .setParent(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .addAllModelEvaluationSlices(new ArrayList<ModelEvaluationSlice>())
               .build();
       BatchImportModelEvaluationSlicesResponse response =
           modelServiceClient.batchImportModelEvaluationSlices(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchImportModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse)` |   
  
### batchImportModelEvaluationSlices(String parent, List<ModelEvaluationSlice> modelEvaluationSlices)
    
    
    public final BatchImportModelEvaluationSlicesResponse batchImportModelEvaluationSlices(String parent, List<ModelEvaluationSlice> modelEvaluationSlices)

Imports a list of externally generated ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]").toString();
       List<ModelEvaluationSlice> modelEvaluationSlices = new ArrayList<>();
       BatchImportModelEvaluationSlicesResponse response =
           modelServiceClient.batchImportModelEvaluationSlices(parent, modelEvaluationSlices);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent ModelEvaluation resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
`modelEvaluationSlices` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)>`  
Required. Model evaluation slice resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[BatchImportModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse)` |   
  
### batchImportModelEvaluationSlicesCallable()
    
    
    public final UnaryCallable<BatchImportModelEvaluationSlicesRequest,BatchImportModelEvaluationSlicesResponse> batchImportModelEvaluationSlicesCallable()

Imports a list of externally generated ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       BatchImportModelEvaluationSlicesRequest request =
           BatchImportModelEvaluationSlicesRequest.newBuilder()
               .setParent(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .addAllModelEvaluationSlices(new ArrayList<ModelEvaluationSlice>())
               .build();
       ApiFuture<BatchImportModelEvaluationSlicesResponse> future =
           modelServiceClient.batchImportModelEvaluationSlicesCallable().futureCall(request);
       // Do something.
       BatchImportModelEvaluationSlicesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchImportModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesRequest),[BatchImportModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse)>` |   
  
### close()
    
    
    public final void close()

### copyModelAsync(@Nullable LocationName parent, @Nullable ModelName sourceModel)
    
    
    public final OperationFuture<CopyModelResponse,CopyModelOperationMetadata> copyModelAsync(@Nullable LocationName parent, @Nullable ModelName sourceModel)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ModelName sourceModel = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       CopyModelResponse response = modelServiceClient.copyModelAsync(parent, sourceModel).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`  
`sourceModel` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### copyModelAsync(@Nullable LocationName parent, String sourceModel)
    
    
    public final OperationFuture<CopyModelResponse,CopyModelOperationMetadata> copyModelAsync(@Nullable LocationName parent, String sourceModel)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String sourceModel = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       CopyModelResponse response = modelServiceClient.copyModelAsync(parent, sourceModel).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`  
`sourceModel` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### copyModelAsync(CopyModelRequest request)
    
    
    public final OperationFuture<CopyModelResponse,CopyModelOperationMetadata> copyModelAsync(CopyModelRequest request)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CopyModelRequest request =
           CopyModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSourceModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setEncryptionSpec(EncryptionSpec.newBuilder().build())
               .setCustomServiceAccount("customServiceAccount-2110106743")
               .build();
       CopyModelResponse response = modelServiceClient.copyModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CopyModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### copyModelAsync(String parent, @Nullable ModelName sourceModel)
    
    
    public final OperationFuture<CopyModelResponse,CopyModelOperationMetadata> copyModelAsync(String parent, @Nullable ModelName sourceModel)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ModelName sourceModel = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       CopyModelResponse response = modelServiceClient.copyModelAsync(parent, sourceModel).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`  
`sourceModel` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### copyModelAsync(String parent, String sourceModel)
    
    
    public final OperationFuture<CopyModelResponse,CopyModelOperationMetadata> copyModelAsync(String parent, String sourceModel)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String sourceModel = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       CopyModelResponse response = modelServiceClient.copyModelAsync(parent, sourceModel).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location into which to copy the Model. Format: `projects/{project}/locations/{location}`  
`sourceModel` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to copy. That Model must be in the same Project. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### copyModelCallable()
    
    
    public final UnaryCallable<CopyModelRequest,Operation> copyModelCallable()

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CopyModelRequest request =
           CopyModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSourceModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setEncryptionSpec(EncryptionSpec.newBuilder().build())
               .setCustomServiceAccount("customServiceAccount-2110106743")
               .build();
       ApiFuture<Operation> future = modelServiceClient.copyModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CopyModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### copyModelOperationCallable()
    
    
    public final OperationCallable<CopyModelRequest,CopyModelResponse,CopyModelOperationMetadata> copyModelOperationCallable()

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       CopyModelRequest request =
           CopyModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSourceModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setEncryptionSpec(EncryptionSpec.newBuilder().build())
               .setCustomServiceAccount("customServiceAccount-2110106743")
               .build();
       OperationFuture<CopyModelResponse, CopyModelOperationMetadata> future =
           modelServiceClient.copyModelOperationCallable().futureCall(request);
       // Do something.
       CopyModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CopyModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelRequest),[CopyModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelResponse),[CopyModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelOperationMetadata)>` |   
  
### deleteModelAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelAsync(@Nullable ModelName name)

Deletes a Model.

A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       modelServiceClient.deleteModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the Model resource to be deleted. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelAsync(DeleteModelRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelAsync(DeleteModelRequest request)

Deletes a Model.

A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       modelServiceClient.deleteModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelAsync(String name)

Deletes a Model.

A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       modelServiceClient.deleteModelAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Model resource to be deleted. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelCallable()
    
    
    public final UnaryCallable<DeleteModelRequest,Operation> deleteModelCallable()

Deletes a Model.

A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future = modelServiceClient.deleteModelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteModelOperationCallable()
    
    
    public final OperationCallable<DeleteModelRequest,Empty,DeleteOperationMetadata> deleteModelOperationCallable()

Deletes a Model.

A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelRequest request =
           DeleteModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           modelServiceClient.deleteModelOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelVersionAsync(@Nullable ModelName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelVersionAsync(@Nullable ModelName name)

Deletes a Model version.

Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       modelServiceClient.deleteModelVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the model version to be deleted, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelVersionAsync(DeleteModelVersionRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelVersionAsync(DeleteModelVersionRequest request)

Deletes a Model version.

Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelVersionRequest request =
           DeleteModelVersionRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       modelServiceClient.deleteModelVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelVersionAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelVersionAsync(String name)

Deletes a Model version.

Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       modelServiceClient.deleteModelVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model version to be deleted, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelVersionCallable()
    
    
    public final UnaryCallable<DeleteModelVersionRequest,Operation> deleteModelVersionCallable()

Deletes a Model version.

Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelVersionRequest request =
           DeleteModelVersionRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Operation> future =
           modelServiceClient.deleteModelVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteModelVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteModelVersionOperationCallable()
    
    
    public final OperationCallable<DeleteModelVersionRequest,Empty,DeleteOperationMetadata> deleteModelVersionOperationCallable()

Deletes a Model version.

Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       DeleteModelVersionRequest request =
           DeleteModelVersionRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           modelServiceClient.deleteModelVersionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteModelVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### exportModelAsync(@Nullable ModelName name, ExportModelRequest.OutputConfig outputConfig)
    
    
    public final OperationFuture<ExportModelResponse,ExportModelOperationMetadata> exportModelAsync(@Nullable ModelName name, ExportModelRequest.OutputConfig outputConfig)

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       ExportModelRequest.OutputConfig outputConfig =
           ExportModelRequest.OutputConfig.newBuilder().build();
       ExportModelResponse response = modelServiceClient.exportModelAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported.  
`outputConfig` | `[ExportModelRequest.OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.OutputConfig)`  
Required. The desired output location and configuration.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse),[ExportModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelOperationMetadata)>` |   
  
### exportModelAsync(ExportModelRequest request)
    
    
    public final OperationFuture<ExportModelResponse,ExportModelOperationMetadata> exportModelAsync(ExportModelRequest request)

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ExportModelRequest.OutputConfig.newBuilder().build())
               .build();
       ExportModelResponse response = modelServiceClient.exportModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse),[ExportModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelOperationMetadata)>` |   
  
### exportModelAsync(String name, ExportModelRequest.OutputConfig outputConfig)
    
    
    public final OperationFuture<ExportModelResponse,ExportModelOperationMetadata> exportModelAsync(String name, ExportModelRequest.OutputConfig outputConfig)

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       ExportModelRequest.OutputConfig outputConfig =
           ExportModelRequest.OutputConfig.newBuilder().build();
       ExportModelResponse response = modelServiceClient.exportModelAsync(name, outputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to export. The resource name may contain version id or version alias to specify the version, if no version is specified, the default version will be exported.  
`outputConfig` | `[ExportModelRequest.OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.OutputConfig)`  
Required. The desired output location and configuration.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse),[ExportModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelOperationMetadata)>` |   
  
### exportModelCallable()
    
    
    public final UnaryCallable<ExportModelRequest,Operation> exportModelCallable()

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ExportModelRequest.OutputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = modelServiceClient.exportModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportModelOperationCallable()
    
    
    public final OperationCallable<ExportModelRequest,ExportModelResponse,ExportModelOperationMetadata> exportModelOperationCallable()

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ExportModelRequest request =
           ExportModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setOutputConfig(ExportModelRequest.OutputConfig.newBuilder().build())
               .build();
       OperationFuture<ExportModelResponse, ExportModelOperationMetadata> future =
           modelServiceClient.exportModelOperationCallable().futureCall(request);
       // Do something.
       ExportModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest),[ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse),[ExportModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = modelServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = modelServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = modelServiceClient.getLocation(request);
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
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = modelServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getModel(@Nullable ModelName name)
    
    
    public final Model getModel(@Nullable ModelName name)

Gets a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       Model response = modelServiceClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the Model resource. Format: `projects/{project}/locations/{location}/models/{model}` In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### getModel(GetModelRequest request)
    
    
    public final Model getModel(GetModelRequest request)

Gets a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       Model response = modelServiceClient.getModel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### getModel(String name)
    
    
    public final Model getModel(String name)

Gets a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       Model response = modelServiceClient.getModel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Model resource. Format: `projects/{project}/locations/{location}/models/{model}` In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### getModelCallable()
    
    
    public final UnaryCallable<GetModelRequest,Model> getModelCallable()

Gets a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelRequest request =
           GetModelRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .build();
       ApiFuture<Model> future = modelServiceClient.getModelCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>` |   
  
### getModelEvaluation(@Nullable ModelEvaluationName name)
    
    
    public final ModelEvaluation getModelEvaluation(@Nullable ModelEvaluationName name)

Gets a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelEvaluationName name =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]");
       ModelEvaluation response = modelServiceClient.getModelEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelEvaluationName`  
Required. The name of the ModelEvaluation resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### getModelEvaluation(GetModelEvaluationRequest request)
    
    
    public final ModelEvaluation getModelEvaluation(GetModelEvaluationRequest request)

Gets a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelEvaluationRequest request =
           GetModelEvaluationRequest.newBuilder()
               .setName(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .build();
       ModelEvaluation response = modelServiceClient.getModelEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### getModelEvaluation(String name)
    
    
    public final ModelEvaluation getModelEvaluation(String name)

Gets a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]").toString();
       ModelEvaluation response = modelServiceClient.getModelEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ModelEvaluation resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### getModelEvaluationCallable()
    
    
    public final UnaryCallable<GetModelEvaluationRequest,ModelEvaluation> getModelEvaluationCallable()

Gets a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelEvaluationRequest request =
           GetModelEvaluationRequest.newBuilder()
               .setName(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .build();
       ApiFuture<ModelEvaluation> future =
           modelServiceClient.getModelEvaluationCallable().futureCall(request);
       // Do something.
       ModelEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationRequest),[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)>` |   
  
### getModelEvaluationSlice(@Nullable ModelEvaluationSliceName name)
    
    
    public final ModelEvaluationSlice getModelEvaluationSlice(@Nullable ModelEvaluationSliceName name)

Gets a ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelEvaluationSliceName name =
           ModelEvaluationSliceName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]");
       ModelEvaluationSlice response = modelServiceClient.getModelEvaluationSlice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelEvaluationSliceName`  
Required. The name of the ModelEvaluationSlice resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)` |   
  
### getModelEvaluationSlice(GetModelEvaluationSliceRequest request)
    
    
    public final ModelEvaluationSlice getModelEvaluationSlice(GetModelEvaluationSliceRequest request)

Gets a ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelEvaluationSliceRequest request =
           GetModelEvaluationSliceRequest.newBuilder()
               .setName(
                   ModelEvaluationSliceName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
                       .toString())
               .build();
       ModelEvaluationSlice response = modelServiceClient.getModelEvaluationSlice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationSliceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationSliceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)` |   
  
### getModelEvaluationSlice(String name)
    
    
    public final ModelEvaluationSlice getModelEvaluationSlice(String name)

Gets a ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name =
           ModelEvaluationSliceName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
               .toString();
       ModelEvaluationSlice response = modelServiceClient.getModelEvaluationSlice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ModelEvaluationSlice resource. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)` |   
  
### getModelEvaluationSliceCallable()
    
    
    public final UnaryCallable<GetModelEvaluationSliceRequest,ModelEvaluationSlice> getModelEvaluationSliceCallable()

Gets a ModelEvaluationSlice.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       GetModelEvaluationSliceRequest request =
           GetModelEvaluationSliceRequest.newBuilder()
               .setName(
                   ModelEvaluationSliceName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]", "[SLICE]")
                       .toString())
               .build();
       ApiFuture<ModelEvaluationSlice> future =
           modelServiceClient.getModelEvaluationSliceCallable().futureCall(request);
       // Do something.
       ModelEvaluationSlice response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelEvaluationSliceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationSliceRequest),[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)>` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelServiceSettings` |   
  
### getStub()
    
    
    public ModelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ModelServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ModelServiceStub)` |   
  
### importModelEvaluation(@Nullable ModelName parent, ModelEvaluation modelEvaluation)
    
    
    public final ModelEvaluation importModelEvaluation(@Nullable ModelName parent, ModelEvaluation modelEvaluation)

Imports an externally generated ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       ModelEvaluation modelEvaluation = ModelEvaluation.newBuilder().build();
       ModelEvaluation response = modelServiceClient.importModelEvaluation(parent, modelEvaluation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the parent model resource. Format: `projects/{project}/locations/{location}/models/{model}`  
`modelEvaluation` | `[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)`  
Required. Model evaluation resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### importModelEvaluation(ImportModelEvaluationRequest request)
    
    
    public final ModelEvaluation importModelEvaluation(ImportModelEvaluationRequest request)

Imports an externally generated ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ImportModelEvaluationRequest request =
           ImportModelEvaluationRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setModelEvaluation(ModelEvaluation.newBuilder().build())
               .build();
       ModelEvaluation response = modelServiceClient.importModelEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportModelEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### importModelEvaluation(String parent, ModelEvaluation modelEvaluation)
    
    
    public final ModelEvaluation importModelEvaluation(String parent, ModelEvaluation modelEvaluation)

Imports an externally generated ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       ModelEvaluation modelEvaluation = ModelEvaluation.newBuilder().build();
       ModelEvaluation response = modelServiceClient.importModelEvaluation(parent, modelEvaluation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent model resource. Format: `projects/{project}/locations/{location}/models/{model}`  
`modelEvaluation` | `[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)`  
Required. Model evaluation resource to be imported.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)` |   
  
### importModelEvaluationCallable()
    
    
    public final UnaryCallable<ImportModelEvaluationRequest,ModelEvaluation> importModelEvaluationCallable()

Imports an externally generated ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ImportModelEvaluationRequest request =
           ImportModelEvaluationRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setModelEvaluation(ModelEvaluation.newBuilder().build())
               .build();
       ApiFuture<ModelEvaluation> future =
           modelServiceClient.importModelEvaluationCallable().futureCall(request);
       // Do something.
       ModelEvaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportModelEvaluationRequest),[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)>` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final ModelServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : modelServiceClient.listLocations(request).iterateAll()) {
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
`[ModelServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = modelServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ModelServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           modelServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListLocationsPagedResponse)>` |   
  
### listModelEvaluationSlices(@Nullable ModelEvaluationName parent)
    
    
    public final ModelServiceClient.ListModelEvaluationSlicesPagedResponse listModelEvaluationSlices(@Nullable ModelEvaluationName parent)

Lists ModelEvaluationSlices in a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelEvaluationName parent =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]");
       for (ModelEvaluationSlice element :
           modelServiceClient.listModelEvaluationSlices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelEvaluationName`  
Required. The resource name of the ModelEvaluation to list the ModelEvaluationSlices from. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationSlicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationSlicesPagedResponse)` |   
  
### listModelEvaluationSlices(ListModelEvaluationSlicesRequest request)
    
    
    public final ModelServiceClient.ListModelEvaluationSlicesPagedResponse listModelEvaluationSlices(ListModelEvaluationSlicesRequest request)

Lists ModelEvaluationSlices in a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationSlicesRequest request =
           ListModelEvaluationSlicesRequest.newBuilder()
               .setParent(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (ModelEvaluationSlice element :
           modelServiceClient.listModelEvaluationSlices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationSlicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationSlicesPagedResponse)` |   
  
### listModelEvaluationSlices(String parent)
    
    
    public final ModelServiceClient.ListModelEvaluationSlicesPagedResponse listModelEvaluationSlices(String parent)

Lists ModelEvaluationSlices in a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent =
           ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]").toString();
       for (ModelEvaluationSlice element :
           modelServiceClient.listModelEvaluationSlices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ModelEvaluation to list the ModelEvaluationSlices from. Format: `projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationSlicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationSlicesPagedResponse)` |   
  
### listModelEvaluationSlicesCallable()
    
    
    public final UnaryCallable<ListModelEvaluationSlicesRequest,ListModelEvaluationSlicesResponse> listModelEvaluationSlicesCallable()

Lists ModelEvaluationSlices in a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationSlicesRequest request =
           ListModelEvaluationSlicesRequest.newBuilder()
               .setParent(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListModelEvaluationSlicesResponse response =
             modelServiceClient.listModelEvaluationSlicesCallable().call(request);
         for (ModelEvaluationSlice element : response.getModelEvaluationSlicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesRequest),[ListModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesResponse)>` |   
  
### listModelEvaluationSlicesPagedCallable()
    
    
    public final UnaryCallable<ListModelEvaluationSlicesRequest,ModelServiceClient.ListModelEvaluationSlicesPagedResponse> listModelEvaluationSlicesPagedCallable()

Lists ModelEvaluationSlices in a ModelEvaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationSlicesRequest request =
           ListModelEvaluationSlicesRequest.newBuilder()
               .setParent(
                   ModelEvaluationName.of("[PROJECT]", "[LOCATION]", "[MODEL]", "[EVALUATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ModelEvaluationSlice> future =
           modelServiceClient.listModelEvaluationSlicesPagedCallable().futureCall(request);
       // Do something.
       for (ModelEvaluationSlice element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesRequest),[ListModelEvaluationSlicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationSlicesPagedResponse)>` |   
  
### listModelEvaluations(@Nullable ModelName parent)
    
    
    public final ModelServiceClient.ListModelEvaluationsPagedResponse listModelEvaluations(@Nullable ModelName parent)

Lists ModelEvaluations in a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       for (ModelEvaluation element : modelServiceClient.listModelEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The resource name of the Model to list the ModelEvaluations from. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluations(ListModelEvaluationsRequest request)
    
    
    public final ModelServiceClient.ListModelEvaluationsPagedResponse listModelEvaluations(ListModelEvaluationsRequest request)

Lists ModelEvaluations in a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (ModelEvaluation element :
           modelServiceClient.listModelEvaluations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluations(String parent)
    
    
    public final ModelServiceClient.ListModelEvaluationsPagedResponse listModelEvaluations(String parent)

Lists ModelEvaluations in a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       for (ModelEvaluation element : modelServiceClient.listModelEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to list the ModelEvaluations from. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationsPagedResponse)` |   
  
### listModelEvaluationsCallable()
    
    
    public final UnaryCallable<ListModelEvaluationsRequest,ListModelEvaluationsResponse> listModelEvaluationsCallable()

Lists ModelEvaluations in a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListModelEvaluationsResponse response =
             modelServiceClient.listModelEvaluationsCallable().call(request);
         for (ModelEvaluation element : response.getModelEvaluationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsRequest),[ListModelEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsResponse)>` |   
  
### listModelEvaluationsPagedCallable()
    
    
    public final UnaryCallable<ListModelEvaluationsRequest,ModelServiceClient.ListModelEvaluationsPagedResponse> listModelEvaluationsPagedCallable()

Lists ModelEvaluations in a Model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelEvaluationsRequest request =
           ListModelEvaluationsRequest.newBuilder()
               .setParent(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ModelEvaluation> future =
           modelServiceClient.listModelEvaluationsPagedCallable().futureCall(request);
       // Do something.
       for (ModelEvaluation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsRequest),[ListModelEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelEvaluationsPagedResponse)>` |   
  
### listModelVersionCheckpoints(@Nullable ModelName name)
    
    
    public final ModelServiceClient.ListModelVersionCheckpointsPagedResponse listModelVersionCheckpoints(@Nullable ModelName name)

Lists checkpoints of the specified model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       for (ModelVersionCheckpoint element :
           modelServiceClient.listModelVersionCheckpoints(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the model version to list checkpoints for. `projects/{project}/locations/{location}/models/{model}@{version}` Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the latest version will be used.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionCheckpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionCheckpointsPagedResponse)` |   
  
### listModelVersionCheckpoints(ListModelVersionCheckpointsRequest request)
    
    
    public final ModelServiceClient.ListModelVersionCheckpointsPagedResponse listModelVersionCheckpoints(ListModelVersionCheckpointsRequest request)

Lists checkpoints of the specified model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionCheckpointsRequest request =
           ListModelVersionCheckpointsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ModelVersionCheckpoint element :
           modelServiceClient.listModelVersionCheckpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelVersionCheckpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionCheckpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionCheckpointsPagedResponse)` |   
  
### listModelVersionCheckpoints(String name)
    
    
    public final ModelServiceClient.ListModelVersionCheckpointsPagedResponse listModelVersionCheckpoints(String name)

Lists checkpoints of the specified model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       for (ModelVersionCheckpoint element :
           modelServiceClient.listModelVersionCheckpoints(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model version to list checkpoints for. `projects/{project}/locations/{location}/models/{model}@{version}` Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the latest version will be used.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionCheckpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionCheckpointsPagedResponse)` |   
  
### listModelVersionCheckpointsCallable()
    
    
    public final UnaryCallable<ListModelVersionCheckpointsRequest,ListModelVersionCheckpointsResponse> listModelVersionCheckpointsCallable()

Lists checkpoints of the specified model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionCheckpointsRequest request =
           ListModelVersionCheckpointsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListModelVersionCheckpointsResponse response =
             modelServiceClient.listModelVersionCheckpointsCallable().call(request);
         for (ModelVersionCheckpoint element : response.getCheckpointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelVersionCheckpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsRequest),[ListModelVersionCheckpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsResponse)>` |   
  
### listModelVersionCheckpointsPagedCallable()
    
    
    public final UnaryCallable<ListModelVersionCheckpointsRequest,ModelServiceClient.ListModelVersionCheckpointsPagedResponse> listModelVersionCheckpointsPagedCallable()

Lists checkpoints of the specified model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionCheckpointsRequest request =
           ListModelVersionCheckpointsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ModelVersionCheckpoint> future =
           modelServiceClient.listModelVersionCheckpointsPagedCallable().futureCall(request);
       // Do something.
       for (ModelVersionCheckpoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelVersionCheckpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsRequest),[ListModelVersionCheckpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionCheckpointsPagedResponse)>` |   
  
### listModelVersions(@Nullable ModelName name)
    
    
    public final ModelServiceClient.ListModelVersionsPagedResponse listModelVersions(@Nullable ModelName name)

Lists versions of the specified model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       for (Model element : modelServiceClient.listModelVersions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the model to list versions for.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionsPagedResponse)` |   
  
### listModelVersions(ListModelVersionsRequest request)
    
    
    public final ModelServiceClient.ListModelVersionsPagedResponse listModelVersions(ListModelVersionsRequest request)

Lists versions of the specified model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionsRequest request =
           ListModelVersionsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Model element : modelServiceClient.listModelVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionsPagedResponse)` |   
  
### listModelVersions(String name)
    
    
    public final ModelServiceClient.ListModelVersionsPagedResponse listModelVersions(String name)

Lists versions of the specified model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       for (Model element : modelServiceClient.listModelVersions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model to list versions for.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionsPagedResponse)` |   
  
### listModelVersionsCallable()
    
    
    public final UnaryCallable<ListModelVersionsRequest,ListModelVersionsResponse> listModelVersionsCallable()

Lists versions of the specified model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionsRequest request =
           ListModelVersionsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListModelVersionsResponse response =
             modelServiceClient.listModelVersionsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsRequest),[ListModelVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsResponse)>` |   
  
### listModelVersionsPagedCallable()
    
    
    public final UnaryCallable<ListModelVersionsRequest,ModelServiceClient.ListModelVersionsPagedResponse> listModelVersionsPagedCallable()

Lists versions of the specified model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelVersionsRequest request =
           ListModelVersionsRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Model> future =
           modelServiceClient.listModelVersionsPagedCallable().futureCall(request);
       // Do something.
       for (Model element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsRequest),[ListModelVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelVersionsPagedResponse)>` |   
  
### listModels(@Nullable LocationName parent)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(@Nullable LocationName parent)

Lists Models in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Model element : modelServiceClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the Models from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModels(ListModelsRequest request)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(ListModelsRequest request)

Lists Models in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Model element : modelServiceClient.listModels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModels(String parent)
    
    
    public final ModelServiceClient.ListModelsPagedResponse listModels(String parent)

Lists Models in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Model element : modelServiceClient.listModels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the Models from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelServiceClient.ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelsPagedResponse)` |   
  
### listModelsCallable()
    
    
    public final UnaryCallable<ListModelsRequest,ListModelsResponse> listModelsCallable()

Lists Models in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsRequest),[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsResponse)>` |   
  
### listModelsPagedCallable()
    
    
    public final UnaryCallable<ListModelsRequest,ModelServiceClient.ListModelsPagedResponse> listModelsPagedCallable()

Lists Models in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ListModelsRequest request =
           ListModelsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsRequest),[ListModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.ListModelsPagedResponse)>` |   
  
### mergeVersionAliases(@Nullable ModelName name, List<String> versionAliases)
    
    
    public final Model mergeVersionAliases(@Nullable ModelName name, List<String> versionAliases)

Merges a set of aliases for a Model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       List<String> versionAliases = new ArrayList<>();
       Model response = modelServiceClient.mergeVersionAliases(name, versionAliases);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The name of the model version to merge aliases, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`  
`versionAliases` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The set of version aliases to merge. The alias should be at most 128 characters, and match `a-z{0,126}[a-z-0-9]`. Add the `-` prefix to an alias means removing that alias from the version. `-` is NOT counted in the 128 characters. Example: `-golden` means removing the `golden` alias from the version. There is NO ordering in aliases, which means 1) The aliases returned from GetModel API might not have the exactly same order from this MergeVersionAliases API. 2) Adding and deleting the same alias in the request is not recommended, and the 2 operations will be cancelled out.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### mergeVersionAliases(MergeVersionAliasesRequest request)
    
    
    public final Model mergeVersionAliases(MergeVersionAliasesRequest request)

Merges a set of aliases for a Model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       MergeVersionAliasesRequest request =
           MergeVersionAliasesRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .addAllVersionAliases(new ArrayList<String>())
               .build();
       Model response = modelServiceClient.mergeVersionAliases(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MergeVersionAliasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MergeVersionAliasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### mergeVersionAliases(String name, List<String> versionAliases)
    
    
    public final Model mergeVersionAliases(String name, List<String> versionAliases)

Merges a set of aliases for a Model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       List<String> versionAliases = new ArrayList<>();
       Model response = modelServiceClient.mergeVersionAliases(name, versionAliases);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the model version to merge aliases, with a version ID explicitly included. Example: `projects/{project}/locations/{location}/models/{model}@1234`  
`versionAliases` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The set of version aliases to merge. The alias should be at most 128 characters, and match `a-z{0,126}[a-z-0-9]`. Add the `-` prefix to an alias means removing that alias from the version. `-` is NOT counted in the 128 characters. Example: `-golden` means removing the `golden` alias from the version. There is NO ordering in aliases, which means 1) The aliases returned from GetModel API might not have the exactly same order from this MergeVersionAliases API. 2) Adding and deleting the same alias in the request is not recommended, and the 2 operations will be cancelled out.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### mergeVersionAliasesCallable()
    
    
    public final UnaryCallable<MergeVersionAliasesRequest,Model> mergeVersionAliasesCallable()

Merges a set of aliases for a Model version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       MergeVersionAliasesRequest request =
           MergeVersionAliasesRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .addAllVersionAliases(new ArrayList<String>())
               .build();
       ApiFuture<Model> future =
           modelServiceClient.mergeVersionAliasesCallable().futureCall(request);
       // Do something.
       Model response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MergeVersionAliasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MergeVersionAliasesRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = modelServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = modelServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = modelServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           modelServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateExplanationDatasetAsync(@Nullable ModelName model)
    
    
    public final OperationFuture<UpdateExplanationDatasetResponse,UpdateExplanationDatasetOperationMetadata> updateExplanationDatasetAsync(@Nullable ModelName model)

Incrementally update the dataset used for an examples model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       ModelName model = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       UpdateExplanationDatasetResponse response =
           modelServiceClient.updateExplanationDatasetAsync(model).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`model` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelName`  
Required. The resource name of the Model to update. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpdateExplanationDatasetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetResponse),[UpdateExplanationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetOperationMetadata)>` |   
  
### updateExplanationDatasetAsync(UpdateExplanationDatasetRequest request)
    
    
    public final OperationFuture<UpdateExplanationDatasetResponse,UpdateExplanationDatasetOperationMetadata> updateExplanationDatasetAsync(UpdateExplanationDatasetRequest request)

Incrementally update the dataset used for an examples model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UpdateExplanationDatasetRequest request =
           UpdateExplanationDatasetRequest.newBuilder()
               .setModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setExamples(Examples.newBuilder().build())
               .build();
       UpdateExplanationDatasetResponse response =
           modelServiceClient.updateExplanationDatasetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExplanationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpdateExplanationDatasetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetResponse),[UpdateExplanationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetOperationMetadata)>` |   
  
### updateExplanationDatasetAsync(String model)
    
    
    public final OperationFuture<UpdateExplanationDatasetResponse,UpdateExplanationDatasetOperationMetadata> updateExplanationDatasetAsync(String model)

Incrementally update the dataset used for an examples model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String model = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       UpdateExplanationDatasetResponse response =
           modelServiceClient.updateExplanationDatasetAsync(model).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`model` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Model to update. Format: `projects/{project}/locations/{location}/models/{model}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpdateExplanationDatasetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetResponse),[UpdateExplanationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetOperationMetadata)>` |   
  
### updateExplanationDatasetCallable()
    
    
    public final UnaryCallable<UpdateExplanationDatasetRequest,Operation> updateExplanationDatasetCallable()

Incrementally update the dataset used for an examples model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UpdateExplanationDatasetRequest request =
           UpdateExplanationDatasetRequest.newBuilder()
               .setModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setExamples(Examples.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           modelServiceClient.updateExplanationDatasetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExplanationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExplanationDatasetOperationCallable()
    
    
    public final OperationCallable<UpdateExplanationDatasetRequest,UpdateExplanationDatasetResponse,UpdateExplanationDatasetOperationMetadata> updateExplanationDatasetOperationCallable()

Incrementally update the dataset used for an examples model.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UpdateExplanationDatasetRequest request =
           UpdateExplanationDatasetRequest.newBuilder()
               .setModel(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setExamples(Examples.newBuilder().build())
               .build();
       OperationFuture<UpdateExplanationDatasetResponse, UpdateExplanationDatasetOperationMetadata>
           future =
               modelServiceClient.updateExplanationDatasetOperationCallable().futureCall(request);
       // Do something.
       UpdateExplanationDatasetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateExplanationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetRequest),[UpdateExplanationDatasetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetResponse),[UpdateExplanationDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetOperationMetadata)>` |   
  
### updateModel(Model model, FieldMask updateMask)
    
    
    public final Model updateModel(Model model, FieldMask updateMask)

Updates a Model.

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
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)`  
Required. The Model which replaces the resource on the server. When Model Versioning is enabled, the model.name will be used to determine whether to update the model or model version. 1. model.name with the @ value, e.g. models/123@1, refers to a version specific update. 2. model.name without the @ value, e.g. models/123, refers to a model update. 3. model.name with @-, e.g. models/123@-, refers to a model update. 4. Supported model fields: display_name, description; supported version-specific fields: version_description. Labels are supported in both scenarios. Both the model labels and the version labels are merged when a model is returned. When updating labels, if the request is for model-specific update, model label gets updated. Otherwise, version labels get updated. 5. A model name or model version name fields update mismatch will cause a precondition error. 6. One request cannot update both the model and the version fields. You must update them separately.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### updateModel(UpdateModelRequest request)
    
    
    public final Model updateModel(UpdateModelRequest request)

Updates a Model.

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
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)` |   
  
### updateModelCallable()
    
    
    public final UnaryCallable<UpdateModelRequest,Model> updateModelCallable()

Updates a Model.

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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelRequest),[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>` |   
  
### uploadModelAsync(@Nullable LocationName parent, Model model)
    
    
    public final OperationFuture<UploadModelResponse,UploadModelOperationMetadata> uploadModelAsync(@Nullable LocationName parent, Model model)

Uploads a Model artifact into Vertex AI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Model model = Model.newBuilder().build();
       UploadModelResponse response = modelServiceClient.uploadModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location into which to upload the Model. Format: `projects/{project}/locations/{location}`  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)`  
Required. The Model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UploadModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelResponse),[UploadModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelOperationMetadata)>` |   
  
### uploadModelAsync(UploadModelRequest request)
    
    
    public final OperationFuture<UploadModelResponse,UploadModelOperationMetadata> uploadModelAsync(UploadModelRequest request)

Uploads a Model artifact into Vertex AI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UploadModelRequest request =
           UploadModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setParentModel("parentModel998431903")
               .setModelId("modelId1226956324")
               .setModel(Model.newBuilder().build())
               .setServiceAccount("serviceAccount1079137720")
               .build();
       UploadModelResponse response = modelServiceClient.uploadModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UploadModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UploadModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelResponse),[UploadModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelOperationMetadata)>` |   
  
### uploadModelAsync(String parent, Model model)
    
    
    public final OperationFuture<UploadModelResponse,UploadModelOperationMetadata> uploadModelAsync(String parent, Model model)

Uploads a Model artifact into Vertex AI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Model model = Model.newBuilder().build();
       UploadModelResponse response = modelServiceClient.uploadModelAsync(parent, model).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location into which to upload the Model. Format: `projects/{project}/locations/{location}`  
`model` | `[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)`  
Required. The Model to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UploadModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelResponse),[UploadModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelOperationMetadata)>` |   
  
### uploadModelCallable()
    
    
    public final UnaryCallable<UploadModelRequest,Operation> uploadModelCallable()

Uploads a Model artifact into Vertex AI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UploadModelRequest request =
           UploadModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setParentModel("parentModel998431903")
               .setModelId("modelId1226956324")
               .setModel(Model.newBuilder().build())
               .setServiceAccount("serviceAccount1079137720")
               .build();
       ApiFuture<Operation> future = modelServiceClient.uploadModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UploadModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### uploadModelOperationCallable()
    
    
    public final OperationCallable<UploadModelRequest,UploadModelResponse,UploadModelOperationMetadata> uploadModelOperationCallable()

Uploads a Model artifact into Vertex AI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ModelServiceClient modelServiceClient = ModelServiceClient.create()) {
       UploadModelRequest request =
           UploadModelRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setParentModel("parentModel998431903")
               .setModelId("modelId1226956324")
               .setModel(Model.newBuilder().build())
               .setServiceAccount("serviceAccount1079137720")
               .build();
       OperationFuture<UploadModelResponse, UploadModelOperationMetadata> future =
           modelServiceClient.uploadModelOperationCallable().futureCall(request);
       // Do something.
       UploadModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UploadModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelRequest),[UploadModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelResponse),[UploadModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
