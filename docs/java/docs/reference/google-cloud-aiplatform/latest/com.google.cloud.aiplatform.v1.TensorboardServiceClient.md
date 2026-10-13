---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient
title: Class TensorboardServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:36.500288+00:00
---

# Class TensorboardServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TensorboardServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/TensorboardServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: TensorboardService

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName name = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       Tensorboard response = tensorboardServiceClient.getTensorboard(name);
     }
     

Note: close() needs to be called on the TensorboardServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateTensorboard |  Creates a Tensorboard. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTensorboardAsync(CreateTensorboardRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTensorboardAsync(TensorboardName parent, Tensorboard tensorboard) 
  * createTensorboardAsync(String parent, Tensorboard tensorboard) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTensorboardOperationCallable() 
  * createTensorboardCallable() 

  
GetTensorboard |  Gets a Tensorboard. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTensorboard(GetTensorboardRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTensorboard(TensorboardName name) 
  * getTensorboard(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTensorboardCallable() 

  
UpdateTensorboard |  Updates a Tensorboard. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTensorboardAsync(UpdateTensorboardRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTensorboardAsync(Tensorboard tensorboard, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTensorboardOperationCallable() 
  * updateTensorboardCallable() 

  
ListTensorboards |  Lists Tensorboards in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTensorboards(ListTensorboardsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTensorboards(LocationName parent) 
  * listTensorboards(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTensorboardsPagedCallable() 
  * listTensorboardsCallable() 

  
DeleteTensorboard |  Deletes a Tensorboard. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTensorboardAsync(DeleteTensorboardRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTensorboardAsync(TensorboardName name) 
  * deleteTensorboardAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTensorboardOperationCallable() 
  * deleteTensorboardCallable() 

  
ReadTensorboardUsage |  Returns a list of monthly active users for a given TensorBoard instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readTensorboardUsage(ReadTensorboardUsageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * readTensorboardUsage(TensorboardName tensorboard) 
  * readTensorboardUsage(String tensorboard) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readTensorboardUsageCallable() 

  
ReadTensorboardSize |  Returns the storage size for a given TensorBoard instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readTensorboardSize(ReadTensorboardSizeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * readTensorboardSize(TensorboardName tensorboard) 
  * readTensorboardSize(String tensorboard) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readTensorboardSizeCallable() 

  
CreateTensorboardExperiment |  Creates a TensorboardExperiment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTensorboardExperiment(CreateTensorboardExperimentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTensorboardExperiment(TensorboardExperimentName parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId) 
  * createTensorboardExperiment(String parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTensorboardExperimentCallable() 

  
GetTensorboardExperiment |  Gets a TensorboardExperiment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTensorboardExperiment(GetTensorboardExperimentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTensorboardExperiment(TensorboardExperimentName name) 
  * getTensorboardExperiment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTensorboardExperimentCallable() 

  
UpdateTensorboardExperiment |  Updates a TensorboardExperiment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTensorboardExperiment(UpdateTensorboardExperimentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTensorboardExperiment(TensorboardExperiment tensorboardExperiment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTensorboardExperimentCallable() 

  
ListTensorboardExperiments |  Lists TensorboardExperiments in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTensorboardExperiments(ListTensorboardExperimentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTensorboardExperiments(TensorboardName parent) 
  * listTensorboardExperiments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTensorboardExperimentsPagedCallable() 
  * listTensorboardExperimentsCallable() 

  
DeleteTensorboardExperiment |  Deletes a TensorboardExperiment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTensorboardExperimentAsync(DeleteTensorboardExperimentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTensorboardExperimentAsync(TensorboardExperimentName name) 
  * deleteTensorboardExperimentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTensorboardExperimentOperationCallable() 
  * deleteTensorboardExperimentCallable() 

  
CreateTensorboardRun |  Creates a TensorboardRun. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTensorboardRun(CreateTensorboardRunRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTensorboardRun(TensorboardRunName parent, TensorboardRun tensorboardRun, String tensorboardRunId) 
  * createTensorboardRun(String parent, TensorboardRun tensorboardRun, String tensorboardRunId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTensorboardRunCallable() 

  
BatchCreateTensorboardRuns |  Batch create TensorboardRuns. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateTensorboardRuns(TensorboardExperimentName parent, List<CreateTensorboardRunRequest> requests) 
  * batchCreateTensorboardRuns(String parent, List<CreateTensorboardRunRequest> requests) 
  * batchCreateTensorboardRuns(BatchCreateTensorboardRunsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateTensorboardRunsCallable() 

  
GetTensorboardRun |  Gets a TensorboardRun. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTensorboardRun(GetTensorboardRunRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTensorboardRun(TensorboardRunName name) 
  * getTensorboardRun(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTensorboardRunCallable() 

  
UpdateTensorboardRun |  Updates a TensorboardRun. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTensorboardRun(UpdateTensorboardRunRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTensorboardRun(TensorboardRun tensorboardRun, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTensorboardRunCallable() 

  
ListTensorboardRuns |  Lists TensorboardRuns in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTensorboardRuns(ListTensorboardRunsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTensorboardRuns(TensorboardExperimentName parent) 
  * listTensorboardRuns(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTensorboardRunsPagedCallable() 
  * listTensorboardRunsCallable() 

  
DeleteTensorboardRun |  Deletes a TensorboardRun. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTensorboardRunAsync(DeleteTensorboardRunRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTensorboardRunAsync(TensorboardRunName name) 
  * deleteTensorboardRunAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTensorboardRunOperationCallable() 
  * deleteTensorboardRunCallable() 

  
BatchCreateTensorboardTimeSeries |  Batch create TensorboardTimeSeries that belong to a TensorboardExperiment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateTensorboardTimeSeries(TensorboardExperimentName parent, List<CreateTensorboardTimeSeriesRequest> requests) 
  * batchCreateTensorboardTimeSeries(String parent, List<CreateTensorboardTimeSeriesRequest> requests) 
  * batchCreateTensorboardTimeSeries(BatchCreateTensorboardTimeSeriesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateTensorboardTimeSeriesCallable() 

  
CreateTensorboardTimeSeries |  Creates a TensorboardTimeSeries. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTensorboardTimeSeries(CreateTensorboardTimeSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTensorboardTimeSeries(TensorboardTimeSeriesName parent, TensorboardTimeSeries tensorboardTimeSeries) 
  * createTensorboardTimeSeries(String parent, TensorboardTimeSeries tensorboardTimeSeries) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTensorboardTimeSeriesCallable() 

  
GetTensorboardTimeSeries |  Gets a TensorboardTimeSeries. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTensorboardTimeSeries(GetTensorboardTimeSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTensorboardTimeSeries(TensorboardTimeSeriesName name) 
  * getTensorboardTimeSeries(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTensorboardTimeSeriesCallable() 

  
UpdateTensorboardTimeSeries |  Updates a TensorboardTimeSeries. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTensorboardTimeSeries(UpdateTensorboardTimeSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTensorboardTimeSeries(TensorboardTimeSeries tensorboardTimeSeries, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTensorboardTimeSeriesCallable() 

  
ListTensorboardTimeSeries |  Lists TensorboardTimeSeries in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTensorboardTimeSeries(ListTensorboardTimeSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTensorboardTimeSeries(TensorboardRunName parent) 
  * listTensorboardTimeSeries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTensorboardTimeSeriesPagedCallable() 
  * listTensorboardTimeSeriesCallable() 

  
DeleteTensorboardTimeSeries |  Deletes a TensorboardTimeSeries. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTensorboardTimeSeriesAsync(DeleteTensorboardTimeSeriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTensorboardTimeSeriesAsync(TensorboardTimeSeriesName name) 
  * deleteTensorboardTimeSeriesAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTensorboardTimeSeriesOperationCallable() 
  * deleteTensorboardTimeSeriesCallable() 

  
BatchReadTensorboardTimeSeriesData |  Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchReadTensorboardTimeSeriesData(BatchReadTensorboardTimeSeriesDataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchReadTensorboardTimeSeriesData(TensorboardName tensorboard) 
  * batchReadTensorboardTimeSeriesData(String tensorboard) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchReadTensorboardTimeSeriesDataCallable() 

  
ReadTensorboardTimeSeriesData |  Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * readTensorboardTimeSeriesData(ReadTensorboardTimeSeriesDataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * readTensorboardTimeSeriesData(TensorboardTimeSeriesName tensorboardTimeSeries) 
  * readTensorboardTimeSeriesData(String tensorboardTimeSeries) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readTensorboardTimeSeriesDataCallable() 

  
ReadTensorboardBlobData |  Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project's Cloud Storage bucket without users having to obtain Cloud Storage access permission. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * readTensorboardBlobDataCallable() 

  
WriteTensorboardExperimentData |  Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeTensorboardExperimentData(WriteTensorboardExperimentDataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * writeTensorboardExperimentData(TensorboardExperimentName tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests) 
  * writeTensorboardExperimentData(String tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeTensorboardExperimentDataCallable() 

  
WriteTensorboardRunData |  Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeTensorboardRunData(WriteTensorboardRunDataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * writeTensorboardRunData(TensorboardRunName tensorboardRun, List<TimeSeriesData> timeSeriesData) 
  * writeTensorboardRunData(String tensorboardRun, List<TimeSeriesData> timeSeriesData) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeTensorboardRunDataCallable() 

  
ExportTensorboardTimeSeriesData |  Exports a TensorboardTimeSeries' data. Data is returned in paginated responses. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportTensorboardTimeSeriesData(ExportTensorboardTimeSeriesDataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * exportTensorboardTimeSeriesData(TensorboardTimeSeriesName tensorboardTimeSeries) 
  * exportTensorboardTimeSeriesData(String tensorboardTimeSeries) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportTensorboardTimeSeriesDataPagedCallable() 
  * exportTensorboardTimeSeriesDataCallable() 

  
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

This class can be customized by passing in a custom instance of TensorboardServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TensorboardServiceSettings tensorboardServiceSettings =
         TensorboardServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TensorboardServiceClient tensorboardServiceClient =
         TensorboardServiceClient.create(tensorboardServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TensorboardServiceSettings tensorboardServiceSettings =
         TensorboardServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     TensorboardServiceClient tensorboardServiceClient =
         TensorboardServiceClient.create(tensorboardServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TensorboardServiceClient

## Static Methods 

### create()
    
    
    public static final TensorboardServiceClient create()

Constructs an instance of TensorboardServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TensorboardServiceSettings settings)
    
    
    public static final TensorboardServiceClient create(TensorboardServiceSettings settings)

Constructs an instance of TensorboardServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TensorboardServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TensorboardServiceStub stub)
    
    
    public static final TensorboardServiceClient create(TensorboardServiceStub stub)

Constructs an instance of TensorboardServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(TensorboardServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TensorboardServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.TensorboardServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient)` |   
  
## Constructors 

### TensorboardServiceClient(TensorboardServiceSettings settings)
    
    
    protected TensorboardServiceClient(TensorboardServiceSettings settings)

Constructs an instance of TensorboardServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TensorboardServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceSettings)`  
  
  
### TensorboardServiceClient(TensorboardServiceStub stub)
    
    
    protected TensorboardServiceClient(TensorboardServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TensorboardServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.TensorboardServiceStub)`  
  
  
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
  
### batchCreateTensorboardRuns(@Nullable TensorboardExperimentName parent, List<CreateTensorboardRunRequest> requests)
    
    
    public final BatchCreateTensorboardRunsResponse batchCreateTensorboardRuns(@Nullable TensorboardExperimentName parent, List<CreateTensorboardRunRequest> requests)

Batch create TensorboardRuns.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       List<CreateTensorboardRunRequest> requests = new ArrayList<>();
       BatchCreateTensorboardRunsResponse response =
           tensorboardServiceClient.batchCreateTensorboardRuns(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The parent field in the CreateTensorboardRunRequest messages must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRunRequest)>`  
Required. The request message specifying the TensorboardRuns to create. A maximum of 1000 TensorboardRuns can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsResponse)` |   
  
### batchCreateTensorboardRuns(BatchCreateTensorboardRunsRequest request)
    
    
    public final BatchCreateTensorboardRunsResponse batchCreateTensorboardRuns(BatchCreateTensorboardRunsRequest request)

Batch create TensorboardRuns.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchCreateTensorboardRunsRequest request =
           BatchCreateTensorboardRunsRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTensorboardRunRequest>())
               .build();
       BatchCreateTensorboardRunsResponse response =
           tensorboardServiceClient.batchCreateTensorboardRuns(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsResponse)` |   
  
### batchCreateTensorboardRuns(String parent, List<CreateTensorboardRunRequest> requests)
    
    
    public final BatchCreateTensorboardRunsResponse batchCreateTensorboardRuns(String parent, List<CreateTensorboardRunRequest> requests)

Batch create TensorboardRuns.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       List<CreateTensorboardRunRequest> requests = new ArrayList<>();
       BatchCreateTensorboardRunsResponse response =
           tensorboardServiceClient.batchCreateTensorboardRuns(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The parent field in the CreateTensorboardRunRequest messages must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRunRequest)>`  
Required. The request message specifying the TensorboardRuns to create. A maximum of 1000 TensorboardRuns can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsResponse)` |   
  
### batchCreateTensorboardRunsCallable()
    
    
    public final UnaryCallable<BatchCreateTensorboardRunsRequest,BatchCreateTensorboardRunsResponse> batchCreateTensorboardRunsCallable()

Batch create TensorboardRuns.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchCreateTensorboardRunsRequest request =
           BatchCreateTensorboardRunsRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTensorboardRunRequest>())
               .build();
       ApiFuture<BatchCreateTensorboardRunsResponse> future =
           tensorboardServiceClient.batchCreateTensorboardRunsCallable().futureCall(request);
       // Do something.
       BatchCreateTensorboardRunsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsRequest),[BatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardRunsResponse)>` |   
  
### batchCreateTensorboardTimeSeries(@Nullable TensorboardExperimentName parent, List<CreateTensorboardTimeSeriesRequest> requests)
    
    
    public final BatchCreateTensorboardTimeSeriesResponse batchCreateTensorboardTimeSeries(@Nullable TensorboardExperimentName parent, List<CreateTensorboardTimeSeriesRequest> requests)

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       List<CreateTensorboardTimeSeriesRequest> requests = new ArrayList<>();
       BatchCreateTensorboardTimeSeriesResponse response =
           tensorboardServiceClient.batchCreateTensorboardTimeSeries(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardTimeSeriesRequest)>`  
Required. The request message specifying the TensorboardTimeSeries to create. A maximum of 1000 TensorboardTimeSeries can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesResponse)` |   
  
### batchCreateTensorboardTimeSeries(BatchCreateTensorboardTimeSeriesRequest request)
    
    
    public final BatchCreateTensorboardTimeSeriesResponse batchCreateTensorboardTimeSeries(BatchCreateTensorboardTimeSeriesRequest request)

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchCreateTensorboardTimeSeriesRequest request =
           BatchCreateTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTensorboardTimeSeriesRequest>())
               .build();
       BatchCreateTensorboardTimeSeriesResponse response =
           tensorboardServiceClient.batchCreateTensorboardTimeSeries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesResponse)` |   
  
### batchCreateTensorboardTimeSeries(String parent, List<CreateTensorboardTimeSeriesRequest> requests)
    
    
    public final BatchCreateTensorboardTimeSeriesResponse batchCreateTensorboardTimeSeries(String parent, List<CreateTensorboardTimeSeriesRequest> requests)

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       List<CreateTensorboardTimeSeriesRequest> requests = new ArrayList<>();
       BatchCreateTensorboardTimeSeriesResponse response =
           tensorboardServiceClient.batchCreateTensorboardTimeSeries(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardTimeSeriesRequest)>`  
Required. The request message specifying the TensorboardTimeSeries to create. A maximum of 1000 TensorboardTimeSeries can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesResponse)` |   
  
### batchCreateTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<BatchCreateTensorboardTimeSeriesRequest,BatchCreateTensorboardTimeSeriesResponse> batchCreateTensorboardTimeSeriesCallable()

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchCreateTensorboardTimeSeriesRequest request =
           BatchCreateTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTensorboardTimeSeriesRequest>())
               .build();
       ApiFuture<BatchCreateTensorboardTimeSeriesResponse> future =
           tensorboardServiceClient.batchCreateTensorboardTimeSeriesCallable().futureCall(request);
       // Do something.
       BatchCreateTensorboardTimeSeriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesRequest),[BatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateTensorboardTimeSeriesResponse)>` |   
  
### batchReadTensorboardTimeSeriesData(@Nullable TensorboardName tensorboard)
    
    
    public final BatchReadTensorboardTimeSeriesDataResponse batchReadTensorboardTimeSeriesData(@Nullable TensorboardName tensorboard)

Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName tensorboard = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       BatchReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.batchReadTensorboardTimeSeriesData(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The resource name of the Tensorboard containing TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`. The TensorboardTimeSeries referenced by time_series must be sub resources of this Tensorboard.  
**Returns**  
---  
**Type** | **Description**  
`[BatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataResponse)` |   
  
### batchReadTensorboardTimeSeriesData(BatchReadTensorboardTimeSeriesDataRequest request)
    
    
    public final BatchReadTensorboardTimeSeriesDataResponse batchReadTensorboardTimeSeriesData(BatchReadTensorboardTimeSeriesDataRequest request)

Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchReadTensorboardTimeSeriesDataRequest request =
           BatchReadTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .addAllTimeSeries(new ArrayList<String>())
               .build();
       BatchReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.batchReadTensorboardTimeSeriesData(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataResponse)` |   
  
### batchReadTensorboardTimeSeriesData(String tensorboard)
    
    
    public final BatchReadTensorboardTimeSeriesDataResponse batchReadTensorboardTimeSeriesData(String tensorboard)

Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboard =
           TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       BatchReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.batchReadTensorboardTimeSeriesData(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Tensorboard containing TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`. The TensorboardTimeSeries referenced by time_series must be sub resources of this Tensorboard.  
**Returns**  
---  
**Type** | **Description**  
`[BatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataResponse)` |   
  
### batchReadTensorboardTimeSeriesDataCallable()
    
    
    public final UnaryCallable<BatchReadTensorboardTimeSeriesDataRequest,BatchReadTensorboardTimeSeriesDataResponse> batchReadTensorboardTimeSeriesDataCallable()

Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       BatchReadTensorboardTimeSeriesDataRequest request =
           BatchReadTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .addAllTimeSeries(new ArrayList<String>())
               .build();
       ApiFuture<BatchReadTensorboardTimeSeriesDataResponse> future =
           tensorboardServiceClient.batchReadTensorboardTimeSeriesDataCallable().futureCall(request);
       // Do something.
       BatchReadTensorboardTimeSeriesDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataRequest),[BatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchReadTensorboardTimeSeriesDataResponse)>` |   
  
### close()
    
    
    public final void close()

### createTensorboardAsync(@Nullable TensorboardName parent, Tensorboard tensorboard)
    
    
    public final OperationFuture<Tensorboard,CreateTensorboardOperationMetadata> createTensorboardAsync(@Nullable TensorboardName parent, Tensorboard tensorboard)

Creates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName parent = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       Tensorboard tensorboard = Tensorboard.newBuilder().build();
       Tensorboard response =
           tensorboardServiceClient.createTensorboardAsync(parent, tensorboard).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The resource name of the Location to create the Tensorboard in. Format: `projects/{project}/locations/{location}`  
`tensorboard` | `[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)`  
Required. The Tensorboard to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[CreateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardOperationMetadata)>` |   
  
### createTensorboardAsync(CreateTensorboardRequest request)
    
    
    public final OperationFuture<Tensorboard,CreateTensorboardOperationMetadata> createTensorboardAsync(CreateTensorboardRequest request)

Creates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardRequest request =
           CreateTensorboardRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       Tensorboard response = tensorboardServiceClient.createTensorboardAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[CreateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardOperationMetadata)>` |   
  
### createTensorboardAsync(String parent, Tensorboard tensorboard)
    
    
    public final OperationFuture<Tensorboard,CreateTensorboardOperationMetadata> createTensorboardAsync(String parent, Tensorboard tensorboard)

Creates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       Tensorboard tensorboard = Tensorboard.newBuilder().build();
       Tensorboard response =
           tensorboardServiceClient.createTensorboardAsync(parent, tensorboard).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the Tensorboard in. Format: `projects/{project}/locations/{location}`  
`tensorboard` | `[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)`  
Required. The Tensorboard to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[CreateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardOperationMetadata)>` |   
  
### createTensorboardCallable()
    
    
    public final UnaryCallable<CreateTensorboardRequest,Operation> createTensorboardCallable()

Creates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardRequest request =
           CreateTensorboardRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.createTensorboardCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTensorboardExperiment(@Nullable TensorboardExperimentName parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId)
    
    
    public final TensorboardExperiment createTensorboardExperiment(@Nullable TensorboardExperimentName parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId)

Creates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       TensorboardExperiment tensorboardExperiment = TensorboardExperiment.newBuilder().build();
       String tensorboardExperimentId = "tensorboardExperimentId1267328197";
       TensorboardExperiment response =
           tensorboardServiceClient.createTensorboardExperiment(
               parent, tensorboardExperiment, tensorboardExperimentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The resource name of the Tensorboard to create the TensorboardExperiment in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
`tensorboardExperiment` | `[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)`  
The TensorboardExperiment to create.  
`tensorboardExperimentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Tensorboard experiment, which becomes the final component of the Tensorboard experiment's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### createTensorboardExperiment(CreateTensorboardExperimentRequest request)
    
    
    public final TensorboardExperiment createTensorboardExperiment(CreateTensorboardExperimentRequest request)

Creates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardExperimentRequest request =
           CreateTensorboardExperimentRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .setTensorboardExperiment(TensorboardExperiment.newBuilder().build())
               .setTensorboardExperimentId("tensorboardExperimentId1267328197")
               .build();
       TensorboardExperiment response =
           tensorboardServiceClient.createTensorboardExperiment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardExperimentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### createTensorboardExperiment(String parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId)
    
    
    public final TensorboardExperiment createTensorboardExperiment(String parent, TensorboardExperiment tensorboardExperiment, String tensorboardExperimentId)

Creates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       TensorboardExperiment tensorboardExperiment = TensorboardExperiment.newBuilder().build();
       String tensorboardExperimentId = "tensorboardExperimentId1267328197";
       TensorboardExperiment response =
           tensorboardServiceClient.createTensorboardExperiment(
               parent, tensorboardExperiment, tensorboardExperimentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Tensorboard to create the TensorboardExperiment in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
`tensorboardExperiment` | `[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)`  
The TensorboardExperiment to create.  
`tensorboardExperimentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Tensorboard experiment, which becomes the final component of the Tensorboard experiment's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### createTensorboardExperimentCallable()
    
    
    public final UnaryCallable<CreateTensorboardExperimentRequest,TensorboardExperiment> createTensorboardExperimentCallable()

Creates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardExperimentRequest request =
           CreateTensorboardExperimentRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .setTensorboardExperiment(TensorboardExperiment.newBuilder().build())
               .setTensorboardExperimentId("tensorboardExperimentId1267328197")
               .build();
       ApiFuture<TensorboardExperiment> future =
           tensorboardServiceClient.createTensorboardExperimentCallable().futureCall(request);
       // Do something.
       TensorboardExperiment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardExperimentRequest),[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)>` |   
  
### createTensorboardOperationCallable()
    
    
    public final OperationCallable<CreateTensorboardRequest,Tensorboard,CreateTensorboardOperationMetadata> createTensorboardOperationCallable()

Creates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardRequest request =
           CreateTensorboardRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       OperationFuture<Tensorboard, CreateTensorboardOperationMetadata> future =
           tensorboardServiceClient.createTensorboardOperationCallable().futureCall(request);
       // Do something.
       Tensorboard response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRequest),[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[CreateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardOperationMetadata)>` |   
  
### createTensorboardRun(@Nullable TensorboardRunName parent, TensorboardRun tensorboardRun, String tensorboardRunId)
    
    
    public final TensorboardRun createTensorboardRun(@Nullable TensorboardRunName parent, TensorboardRun tensorboardRun, String tensorboardRunId)

Creates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRunName parent =
           TensorboardRunName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]");
       TensorboardRun tensorboardRun = TensorboardRun.newBuilder().build();
       String tensorboardRunId = "tensorboardRunId-407822631";
       TensorboardRun response =
           tensorboardServiceClient.createTensorboardRun(parent, tensorboardRun, tensorboardRunId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardRunName`  
Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
`tensorboardRun` | `[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)`  
Required. The TensorboardRun to create.  
`tensorboardRunId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### createTensorboardRun(CreateTensorboardRunRequest request)
    
    
    public final TensorboardRun createTensorboardRun(CreateTensorboardRunRequest request)

Creates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardRunRequest request =
           CreateTensorboardRunRequest.newBuilder()
               .setParent(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .setTensorboardRun(TensorboardRun.newBuilder().build())
               .setTensorboardRunId("tensorboardRunId-407822631")
               .build();
       TensorboardRun response = tensorboardServiceClient.createTensorboardRun(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRunRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### createTensorboardRun(String parent, TensorboardRun tensorboardRun, String tensorboardRunId)
    
    
    public final TensorboardRun createTensorboardRun(String parent, TensorboardRun tensorboardRun, String tensorboardRunId)

Creates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardRunName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
               .toString();
       TensorboardRun tensorboardRun = TensorboardRun.newBuilder().build();
       String tensorboardRunId = "tensorboardRunId-407822631";
       TensorboardRun response =
           tensorboardServiceClient.createTensorboardRun(parent, tensorboardRun, tensorboardRunId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
`tensorboardRun` | `[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)`  
Required. The TensorboardRun to create.  
`tensorboardRunId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run's resource name. This value should be 1-128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### createTensorboardRunCallable()
    
    
    public final UnaryCallable<CreateTensorboardRunRequest,TensorboardRun> createTensorboardRunCallable()

Creates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardRunRequest request =
           CreateTensorboardRunRequest.newBuilder()
               .setParent(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .setTensorboardRun(TensorboardRun.newBuilder().build())
               .setTensorboardRunId("tensorboardRunId-407822631")
               .build();
       ApiFuture<TensorboardRun> future =
           tensorboardServiceClient.createTensorboardRunCallable().futureCall(request);
       // Do something.
       TensorboardRun response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardRunRequest),[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)>` |   
  
### createTensorboardTimeSeries(@Nullable TensorboardTimeSeriesName parent, TensorboardTimeSeries tensorboardTimeSeries)
    
    
    public final TensorboardTimeSeries createTensorboardTimeSeries(@Nullable TensorboardTimeSeriesName parent, TensorboardTimeSeries tensorboardTimeSeries)

Creates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeriesName parent =
           TensorboardTimeSeriesName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]", "[TIME_SERIES]");
       TensorboardTimeSeries tensorboardTimeSeries = TensorboardTimeSeries.newBuilder().build();
       TensorboardTimeSeries response =
           tensorboardServiceClient.createTensorboardTimeSeries(parent, tensorboardTimeSeries);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardTimeSeriesName`  
Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
`tensorboardTimeSeries` | `[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)`  
Required. The TensorboardTimeSeries to create.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### createTensorboardTimeSeries(CreateTensorboardTimeSeriesRequest request)
    
    
    public final TensorboardTimeSeries createTensorboardTimeSeries(CreateTensorboardTimeSeriesRequest request)

Creates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardTimeSeriesRequest request =
           CreateTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setTensorboardTimeSeriesId("tensorboardTimeSeriesId-913380692")
               .setTensorboardTimeSeries(TensorboardTimeSeries.newBuilder().build())
               .build();
       TensorboardTimeSeries response =
           tensorboardServiceClient.createTensorboardTimeSeries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### createTensorboardTimeSeries(String parent, TensorboardTimeSeries tensorboardTimeSeries)
    
    
    public final TensorboardTimeSeries createTensorboardTimeSeries(String parent, TensorboardTimeSeries tensorboardTimeSeries)

Creates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardTimeSeriesName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[TENSORBOARD]",
                   "[EXPERIMENT]",
                   "[RUN]",
                   "[TIME_SERIES]")
               .toString();
       TensorboardTimeSeries tensorboardTimeSeries = TensorboardTimeSeries.newBuilder().build();
       TensorboardTimeSeries response =
           tensorboardServiceClient.createTensorboardTimeSeries(parent, tensorboardTimeSeries);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
`tensorboardTimeSeries` | `[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)`  
Required. The TensorboardTimeSeries to create.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### createTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<CreateTensorboardTimeSeriesRequest,TensorboardTimeSeries> createTensorboardTimeSeriesCallable()

Creates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       CreateTensorboardTimeSeriesRequest request =
           CreateTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setTensorboardTimeSeriesId("tensorboardTimeSeriesId-913380692")
               .setTensorboardTimeSeries(TensorboardTimeSeries.newBuilder().build())
               .build();
       ApiFuture<TensorboardTimeSeries> future =
           tensorboardServiceClient.createTensorboardTimeSeriesCallable().futureCall(request);
       // Do something.
       TensorboardTimeSeries response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTensorboardTimeSeriesRequest),[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)>` |   
  
### deleteTensorboardAsync(@Nullable TensorboardName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardAsync(@Nullable TensorboardName name)

Deletes a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName name = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       tensorboardServiceClient.deleteTensorboardAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The name of the Tensorboard to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardAsync(DeleteTensorboardRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardAsync(DeleteTensorboardRequest request)

Deletes a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRequest request =
           DeleteTensorboardRequest.newBuilder()
               .setName(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       tensorboardServiceClient.deleteTensorboardAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardAsync(String name)

Deletes a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       tensorboardServiceClient.deleteTensorboardAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tensorboard to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardCallable()
    
    
    public final UnaryCallable<DeleteTensorboardRequest,Operation> deleteTensorboardCallable()

Deletes a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRequest request =
           DeleteTensorboardRequest.newBuilder()
               .setName(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.deleteTensorboardCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTensorboardExperimentAsync(@Nullable TensorboardExperimentName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardExperimentAsync(@Nullable TensorboardExperimentName name)

Deletes a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName name =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       tensorboardServiceClient.deleteTensorboardExperimentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The name of the TensorboardExperiment to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardExperimentAsync(DeleteTensorboardExperimentRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardExperimentAsync(DeleteTensorboardExperimentRequest request)

Deletes a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardExperimentRequest request =
           DeleteTensorboardExperimentRequest.newBuilder()
               .setName(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .build();
       tensorboardServiceClient.deleteTensorboardExperimentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardExperimentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardExperimentAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardExperimentAsync(String name)

Deletes a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       tensorboardServiceClient.deleteTensorboardExperimentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardExperiment to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardExperimentCallable()
    
    
    public final UnaryCallable<DeleteTensorboardExperimentRequest,Operation> deleteTensorboardExperimentCallable()

Deletes a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardExperimentRequest request =
           DeleteTensorboardExperimentRequest.newBuilder()
               .setName(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.deleteTensorboardExperimentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardExperimentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTensorboardExperimentOperationCallable()
    
    
    public final OperationCallable<DeleteTensorboardExperimentRequest,Empty,DeleteOperationMetadata> deleteTensorboardExperimentOperationCallable()

Deletes a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardExperimentRequest request =
           DeleteTensorboardExperimentRequest.newBuilder()
               .setName(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           tensorboardServiceClient
               .deleteTensorboardExperimentOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardExperimentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardOperationCallable()
    
    
    public final OperationCallable<DeleteTensorboardRequest,Empty,DeleteOperationMetadata> deleteTensorboardOperationCallable()

Deletes a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRequest request =
           DeleteTensorboardRequest.newBuilder()
               .setName(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           tensorboardServiceClient.deleteTensorboardOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardRunAsync(@Nullable TensorboardRunName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardRunAsync(@Nullable TensorboardRunName name)

Deletes a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRunName name =
           TensorboardRunName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]");
       tensorboardServiceClient.deleteTensorboardRunAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardRunName`  
Required. The name of the TensorboardRun to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardRunAsync(DeleteTensorboardRunRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardRunAsync(DeleteTensorboardRunRequest request)

Deletes a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRunRequest request =
           DeleteTensorboardRunRequest.newBuilder()
               .setName(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .build();
       tensorboardServiceClient.deleteTensorboardRunAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRunRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardRunAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardRunAsync(String name)

Deletes a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardRunName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
               .toString();
       tensorboardServiceClient.deleteTensorboardRunAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardRun to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardRunCallable()
    
    
    public final UnaryCallable<DeleteTensorboardRunRequest,Operation> deleteTensorboardRunCallable()

Deletes a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRunRequest request =
           DeleteTensorboardRunRequest.newBuilder()
               .setName(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.deleteTensorboardRunCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRunRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTensorboardRunOperationCallable()
    
    
    public final OperationCallable<DeleteTensorboardRunRequest,Empty,DeleteOperationMetadata> deleteTensorboardRunOperationCallable()

Deletes a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardRunRequest request =
           DeleteTensorboardRunRequest.newBuilder()
               .setName(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           tensorboardServiceClient.deleteTensorboardRunOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardRunRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardTimeSeriesAsync(@Nullable TensorboardTimeSeriesName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardTimeSeriesAsync(@Nullable TensorboardTimeSeriesName name)

Deletes a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeriesName name =
           TensorboardTimeSeriesName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]", "[TIME_SERIES]");
       tensorboardServiceClient.deleteTensorboardTimeSeriesAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardTimeSeriesName`  
Required. The name of the TensorboardTimeSeries to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardTimeSeriesAsync(DeleteTensorboardTimeSeriesRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardTimeSeriesAsync(DeleteTensorboardTimeSeriesRequest request)

Deletes a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardTimeSeriesRequest request =
           DeleteTensorboardTimeSeriesRequest.newBuilder()
               .setName(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .build();
       tensorboardServiceClient.deleteTensorboardTimeSeriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardTimeSeriesAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTensorboardTimeSeriesAsync(String name)

Deletes a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardTimeSeriesName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[TENSORBOARD]",
                   "[EXPERIMENT]",
                   "[RUN]",
                   "[TIME_SERIES]")
               .toString();
       tensorboardServiceClient.deleteTensorboardTimeSeriesAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardTimeSeries to be deleted. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<DeleteTensorboardTimeSeriesRequest,Operation> deleteTensorboardTimeSeriesCallable()

Deletes a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardTimeSeriesRequest request =
           DeleteTensorboardTimeSeriesRequest.newBuilder()
               .setName(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.deleteTensorboardTimeSeriesCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardTimeSeriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTensorboardTimeSeriesOperationCallable()
    
    
    public final OperationCallable<DeleteTensorboardTimeSeriesRequest,Empty,DeleteOperationMetadata> deleteTensorboardTimeSeriesOperationCallable()

Deletes a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       DeleteTensorboardTimeSeriesRequest request =
           DeleteTensorboardTimeSeriesRequest.newBuilder()
               .setName(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           tensorboardServiceClient
               .deleteTensorboardTimeSeriesOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTensorboardTimeSeriesRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### exportTensorboardTimeSeriesData(@Nullable TensorboardTimeSeriesName tensorboardTimeSeries)
    
    
    public final TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse exportTensorboardTimeSeriesData(@Nullable TensorboardTimeSeriesName tensorboardTimeSeries)

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeriesName tensorboardTimeSeries =
           TensorboardTimeSeriesName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]", "[TIME_SERIES]");
       for (TimeSeriesDataPoint element :
           tensorboardServiceClient
               .exportTensorboardTimeSeriesData(tensorboardTimeSeries)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeries` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardTimeSeriesName`  
Required. The resource name of the TensorboardTimeSeries to export data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse)` |   
  
### exportTensorboardTimeSeriesData(ExportTensorboardTimeSeriesDataRequest request)
    
    
    public final TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse exportTensorboardTimeSeriesData(ExportTensorboardTimeSeriesDataRequest request)

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ExportTensorboardTimeSeriesDataRequest request =
           ExportTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboardTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (TimeSeriesDataPoint element :
           tensorboardServiceClient.exportTensorboardTimeSeriesData(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportTensorboardTimeSeriesDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse)` |   
  
### exportTensorboardTimeSeriesData(String tensorboardTimeSeries)
    
    
    public final TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse exportTensorboardTimeSeriesData(String tensorboardTimeSeries)

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboardTimeSeries =
           TensorboardTimeSeriesName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[TENSORBOARD]",
                   "[EXPERIMENT]",
                   "[RUN]",
                   "[TIME_SERIES]")
               .toString();
       for (TimeSeriesDataPoint element :
           tensorboardServiceClient
               .exportTensorboardTimeSeriesData(tensorboardTimeSeries)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeries` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardTimeSeries to export data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse)` |   
  
### exportTensorboardTimeSeriesDataCallable()
    
    
    public final UnaryCallable<ExportTensorboardTimeSeriesDataRequest,ExportTensorboardTimeSeriesDataResponse> exportTensorboardTimeSeriesDataCallable()

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ExportTensorboardTimeSeriesDataRequest request =
           ExportTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboardTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ExportTensorboardTimeSeriesDataResponse response =
             tensorboardServiceClient.exportTensorboardTimeSeriesDataCallable().call(request);
         for (TimeSeriesDataPoint element : response.getTimeSeriesDataPointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportTensorboardTimeSeriesDataRequest),[ExportTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportTensorboardTimeSeriesDataResponse)>` |   
  
### exportTensorboardTimeSeriesDataPagedCallable()
    
    
    public final UnaryCallable<ExportTensorboardTimeSeriesDataRequest,TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse> exportTensorboardTimeSeriesDataPagedCallable()

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ExportTensorboardTimeSeriesDataRequest request =
           ExportTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboardTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<TimeSeriesDataPoint> future =
           tensorboardServiceClient
               .exportTensorboardTimeSeriesDataPagedCallable()
               .futureCall(request);
       // Do something.
       for (TimeSeriesDataPoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportTensorboardTimeSeriesDataRequest),[ExportTensorboardTimeSeriesDataPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ExportTensorboardTimeSeriesDataPagedResponse)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = tensorboardServiceClient.getIamPolicy(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           tensorboardServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = tensorboardServiceClient.getLocation(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           tensorboardServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable TensorboardServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardServiceSettings` |   
  
### getStub()
    
    
    public TensorboardServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.TensorboardServiceStub)` |   
  
### getTensorboard(@Nullable TensorboardName name)
    
    
    public final Tensorboard getTensorboard(@Nullable TensorboardName name)

Gets a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName name = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       Tensorboard response = tensorboardServiceClient.getTensorboard(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### getTensorboard(GetTensorboardRequest request)
    
    
    public final Tensorboard getTensorboard(GetTensorboardRequest request)

Gets a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardRequest request =
           GetTensorboardRequest.newBuilder()
               .setName(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       Tensorboard response = tensorboardServiceClient.getTensorboard(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### getTensorboard(String name)
    
    
    public final Tensorboard getTensorboard(String name)

Gets a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       Tensorboard response = tensorboardServiceClient.getTensorboard(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### getTensorboardCallable()
    
    
    public final UnaryCallable<GetTensorboardRequest,Tensorboard> getTensorboardCallable()

Gets a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardRequest request =
           GetTensorboardRequest.newBuilder()
               .setName(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ApiFuture<Tensorboard> future =
           tensorboardServiceClient.getTensorboardCallable().futureCall(request);
       // Do something.
       Tensorboard response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardRequest),[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)>` |   
  
### getTensorboardExperiment(@Nullable TensorboardExperimentName name)
    
    
    public final TensorboardExperiment getTensorboardExperiment(@Nullable TensorboardExperimentName name)

Gets a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName name =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       TensorboardExperiment response = tensorboardServiceClient.getTensorboardExperiment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The name of the TensorboardExperiment resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### getTensorboardExperiment(GetTensorboardExperimentRequest request)
    
    
    public final TensorboardExperiment getTensorboardExperiment(GetTensorboardExperimentRequest request)

Gets a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardExperimentRequest request =
           GetTensorboardExperimentRequest.newBuilder()
               .setName(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .build();
       TensorboardExperiment response = tensorboardServiceClient.getTensorboardExperiment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardExperimentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### getTensorboardExperiment(String name)
    
    
    public final TensorboardExperiment getTensorboardExperiment(String name)

Gets a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       TensorboardExperiment response = tensorboardServiceClient.getTensorboardExperiment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardExperiment resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### getTensorboardExperimentCallable()
    
    
    public final UnaryCallable<GetTensorboardExperimentRequest,TensorboardExperiment> getTensorboardExperimentCallable()

Gets a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardExperimentRequest request =
           GetTensorboardExperimentRequest.newBuilder()
               .setName(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .build();
       ApiFuture<TensorboardExperiment> future =
           tensorboardServiceClient.getTensorboardExperimentCallable().futureCall(request);
       // Do something.
       TensorboardExperiment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardExperimentRequest),[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)>` |   
  
### getTensorboardRun(@Nullable TensorboardRunName name)
    
    
    public final TensorboardRun getTensorboardRun(@Nullable TensorboardRunName name)

Gets a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRunName name =
           TensorboardRunName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]");
       TensorboardRun response = tensorboardServiceClient.getTensorboardRun(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardRunName`  
Required. The name of the TensorboardRun resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### getTensorboardRun(GetTensorboardRunRequest request)
    
    
    public final TensorboardRun getTensorboardRun(GetTensorboardRunRequest request)

Gets a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardRunRequest request =
           GetTensorboardRunRequest.newBuilder()
               .setName(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .build();
       TensorboardRun response = tensorboardServiceClient.getTensorboardRun(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardRunRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### getTensorboardRun(String name)
    
    
    public final TensorboardRun getTensorboardRun(String name)

Gets a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardRunName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
               .toString();
       TensorboardRun response = tensorboardServiceClient.getTensorboardRun(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardRun resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### getTensorboardRunCallable()
    
    
    public final UnaryCallable<GetTensorboardRunRequest,TensorboardRun> getTensorboardRunCallable()

Gets a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardRunRequest request =
           GetTensorboardRunRequest.newBuilder()
               .setName(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .build();
       ApiFuture<TensorboardRun> future =
           tensorboardServiceClient.getTensorboardRunCallable().futureCall(request);
       // Do something.
       TensorboardRun response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardRunRequest),[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)>` |   
  
### getTensorboardTimeSeries(@Nullable TensorboardTimeSeriesName name)
    
    
    public final TensorboardTimeSeries getTensorboardTimeSeries(@Nullable TensorboardTimeSeriesName name)

Gets a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeriesName name =
           TensorboardTimeSeriesName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]", "[TIME_SERIES]");
       TensorboardTimeSeries response = tensorboardServiceClient.getTensorboardTimeSeries(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardTimeSeriesName`  
Required. The name of the TensorboardTimeSeries resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### getTensorboardTimeSeries(GetTensorboardTimeSeriesRequest request)
    
    
    public final TensorboardTimeSeries getTensorboardTimeSeries(GetTensorboardTimeSeriesRequest request)

Gets a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardTimeSeriesRequest request =
           GetTensorboardTimeSeriesRequest.newBuilder()
               .setName(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .build();
       TensorboardTimeSeries response = tensorboardServiceClient.getTensorboardTimeSeries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### getTensorboardTimeSeries(String name)
    
    
    public final TensorboardTimeSeries getTensorboardTimeSeries(String name)

Gets a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String name =
           TensorboardTimeSeriesName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[TENSORBOARD]",
                   "[EXPERIMENT]",
                   "[RUN]",
                   "[TIME_SERIES]")
               .toString();
       TensorboardTimeSeries response = tensorboardServiceClient.getTensorboardTimeSeries(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TensorboardTimeSeries resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### getTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<GetTensorboardTimeSeriesRequest,TensorboardTimeSeries> getTensorboardTimeSeriesCallable()

Gets a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       GetTensorboardTimeSeriesRequest request =
           GetTensorboardTimeSeriesRequest.newBuilder()
               .setName(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .build();
       ApiFuture<TensorboardTimeSeries> future =
           tensorboardServiceClient.getTensorboardTimeSeriesCallable().futureCall(request);
       // Do something.
       TensorboardTimeSeries response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTensorboardTimeSeriesRequest),[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)>` |   
  
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
    
    
    public final TensorboardServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : tensorboardServiceClient.listLocations(request).iterateAll()) {
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
`[TensorboardServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             tensorboardServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,TensorboardServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           tensorboardServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListLocationsPagedResponse)>` |   
  
### listTensorboardExperiments(@Nullable TensorboardName parent)
    
    
    public final TensorboardServiceClient.ListTensorboardExperimentsPagedResponse listTensorboardExperiments(@Nullable TensorboardName parent)

Lists TensorboardExperiments in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName parent = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       for (TensorboardExperiment element :
           tensorboardServiceClient.listTensorboardExperiments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The resource name of the Tensorboard to list TensorboardExperiments. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardExperimentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardExperimentsPagedResponse)` |   
  
### listTensorboardExperiments(ListTensorboardExperimentsRequest request)
    
    
    public final TensorboardServiceClient.ListTensorboardExperimentsPagedResponse listTensorboardExperiments(ListTensorboardExperimentsRequest request)

Lists TensorboardExperiments in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardExperimentsRequest request =
           ListTensorboardExperimentsRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (TensorboardExperiment element :
           tensorboardServiceClient.listTensorboardExperiments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTensorboardExperimentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardExperimentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardExperimentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardExperimentsPagedResponse)` |   
  
### listTensorboardExperiments(String parent)
    
    
    public final TensorboardServiceClient.ListTensorboardExperimentsPagedResponse listTensorboardExperiments(String parent)

Lists TensorboardExperiments in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       for (TensorboardExperiment element :
           tensorboardServiceClient.listTensorboardExperiments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Tensorboard to list TensorboardExperiments. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardExperimentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardExperimentsPagedResponse)` |   
  
### listTensorboardExperimentsCallable()
    
    
    public final UnaryCallable<ListTensorboardExperimentsRequest,ListTensorboardExperimentsResponse> listTensorboardExperimentsCallable()

Lists TensorboardExperiments in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardExperimentsRequest request =
           ListTensorboardExperimentsRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListTensorboardExperimentsResponse response =
             tensorboardServiceClient.listTensorboardExperimentsCallable().call(request);
         for (TensorboardExperiment element : response.getTensorboardExperimentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardExperimentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardExperimentsRequest),[ListTensorboardExperimentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardExperimentsResponse)>` |   
  
### listTensorboardExperimentsPagedCallable()
    
    
    public final UnaryCallable<ListTensorboardExperimentsRequest,TensorboardServiceClient.ListTensorboardExperimentsPagedResponse> listTensorboardExperimentsPagedCallable()

Lists TensorboardExperiments in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardExperimentsRequest request =
           ListTensorboardExperimentsRequest.newBuilder()
               .setParent(TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TensorboardExperiment> future =
           tensorboardServiceClient.listTensorboardExperimentsPagedCallable().futureCall(request);
       // Do something.
       for (TensorboardExperiment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardExperimentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardExperimentsRequest),[ListTensorboardExperimentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardExperimentsPagedResponse)>` |   
  
### listTensorboardRuns(@Nullable TensorboardExperimentName parent)
    
    
    public final TensorboardServiceClient.ListTensorboardRunsPagedResponse listTensorboardRuns(@Nullable TensorboardExperimentName parent)

Lists TensorboardRuns in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       for (TensorboardRun element :
           tensorboardServiceClient.listTensorboardRuns(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The resource name of the TensorboardExperiment to list TensorboardRuns. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardRunsPagedResponse)` |   
  
### listTensorboardRuns(ListTensorboardRunsRequest request)
    
    
    public final TensorboardServiceClient.ListTensorboardRunsPagedResponse listTensorboardRuns(ListTensorboardRunsRequest request)

Lists TensorboardRuns in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardRunsRequest request =
           ListTensorboardRunsRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (TensorboardRun element :
           tensorboardServiceClient.listTensorboardRuns(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTensorboardRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardRunsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardRunsPagedResponse)` |   
  
### listTensorboardRuns(String parent)
    
    
    public final TensorboardServiceClient.ListTensorboardRunsPagedResponse listTensorboardRuns(String parent)

Lists TensorboardRuns in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       for (TensorboardRun element :
           tensorboardServiceClient.listTensorboardRuns(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardExperiment to list TensorboardRuns. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardRunsPagedResponse)` |   
  
### listTensorboardRunsCallable()
    
    
    public final UnaryCallable<ListTensorboardRunsRequest,ListTensorboardRunsResponse> listTensorboardRunsCallable()

Lists TensorboardRuns in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardRunsRequest request =
           ListTensorboardRunsRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListTensorboardRunsResponse response =
             tensorboardServiceClient.listTensorboardRunsCallable().call(request);
         for (TensorboardRun element : response.getTensorboardRunsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardRunsRequest),[ListTensorboardRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardRunsResponse)>` |   
  
### listTensorboardRunsPagedCallable()
    
    
    public final UnaryCallable<ListTensorboardRunsRequest,TensorboardServiceClient.ListTensorboardRunsPagedResponse> listTensorboardRunsPagedCallable()

Lists TensorboardRuns in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardRunsRequest request =
           ListTensorboardRunsRequest.newBuilder()
               .setParent(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TensorboardRun> future =
           tensorboardServiceClient.listTensorboardRunsPagedCallable().futureCall(request);
       // Do something.
       for (TensorboardRun element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardRunsRequest),[ListTensorboardRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardRunsPagedResponse)>` |   
  
### listTensorboardTimeSeries(@Nullable TensorboardRunName parent)
    
    
    public final TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse listTensorboardTimeSeries(@Nullable TensorboardRunName parent)

Lists TensorboardTimeSeries in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRunName parent =
           TensorboardRunName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]");
       for (TensorboardTimeSeries element :
           tensorboardServiceClient.listTensorboardTimeSeries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardRunName`  
Required. The resource name of the TensorboardRun to list TensorboardTimeSeries. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse)` |   
  
### listTensorboardTimeSeries(ListTensorboardTimeSeriesRequest request)
    
    
    public final TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse listTensorboardTimeSeries(ListTensorboardTimeSeriesRequest request)

Lists TensorboardTimeSeries in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardTimeSeriesRequest request =
           ListTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (TensorboardTimeSeries element :
           tensorboardServiceClient.listTensorboardTimeSeries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse)` |   
  
### listTensorboardTimeSeries(String parent)
    
    
    public final TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse listTensorboardTimeSeries(String parent)

Lists TensorboardTimeSeries in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent =
           TensorboardRunName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
               .toString();
       for (TensorboardTimeSeries element :
           tensorboardServiceClient.listTensorboardTimeSeries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardRun to list TensorboardTimeSeries. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse)` |   
  
### listTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<ListTensorboardTimeSeriesRequest,ListTensorboardTimeSeriesResponse> listTensorboardTimeSeriesCallable()

Lists TensorboardTimeSeries in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardTimeSeriesRequest request =
           ListTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListTensorboardTimeSeriesResponse response =
             tensorboardServiceClient.listTensorboardTimeSeriesCallable().call(request);
         for (TensorboardTimeSeries element : response.getTensorboardTimeSeriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardTimeSeriesRequest),[ListTensorboardTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardTimeSeriesResponse)>` |   
  
### listTensorboardTimeSeriesPagedCallable()
    
    
    public final UnaryCallable<ListTensorboardTimeSeriesRequest,TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse> listTensorboardTimeSeriesPagedCallable()

Lists TensorboardTimeSeries in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardTimeSeriesRequest request =
           ListTensorboardTimeSeriesRequest.newBuilder()
               .setParent(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TensorboardTimeSeries> future =
           tensorboardServiceClient.listTensorboardTimeSeriesPagedCallable().futureCall(request);
       // Do something.
       for (TensorboardTimeSeries element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardTimeSeriesRequest),[ListTensorboardTimeSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardTimeSeriesPagedResponse)>` |   
  
### listTensorboards(@Nullable LocationName parent)
    
    
    public final TensorboardServiceClient.ListTensorboardsPagedResponse listTensorboards(@Nullable LocationName parent)

Lists Tensorboards in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Tensorboard element : tensorboardServiceClient.listTensorboards(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list Tensorboards. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardsPagedResponse)` |   
  
### listTensorboards(ListTensorboardsRequest request)
    
    
    public final TensorboardServiceClient.ListTensorboardsPagedResponse listTensorboards(ListTensorboardsRequest request)

Lists Tensorboards in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardsRequest request =
           ListTensorboardsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (Tensorboard element : tensorboardServiceClient.listTensorboards(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTensorboardsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardsPagedResponse)` |   
  
### listTensorboards(String parent)
    
    
    public final TensorboardServiceClient.ListTensorboardsPagedResponse listTensorboards(String parent)

Lists Tensorboards in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Tensorboard element : tensorboardServiceClient.listTensorboards(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list Tensorboards. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardServiceClient.ListTensorboardsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardsPagedResponse)` |   
  
### listTensorboardsCallable()
    
    
    public final UnaryCallable<ListTensorboardsRequest,ListTensorboardsResponse> listTensorboardsCallable()

Lists Tensorboards in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardsRequest request =
           ListTensorboardsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListTensorboardsResponse response =
             tensorboardServiceClient.listTensorboardsCallable().call(request);
         for (Tensorboard element : response.getTensorboardsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardsRequest),[ListTensorboardsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardsResponse)>` |   
  
### listTensorboardsPagedCallable()
    
    
    public final UnaryCallable<ListTensorboardsRequest,TensorboardServiceClient.ListTensorboardsPagedResponse> listTensorboardsPagedCallable()

Lists Tensorboards in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ListTensorboardsRequest request =
           ListTensorboardsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Tensorboard> future =
           tensorboardServiceClient.listTensorboardsPagedCallable().futureCall(request);
       // Do something.
       for (Tensorboard element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTensorboardsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTensorboardsRequest),[ListTensorboardsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardServiceClient.ListTensorboardsPagedResponse)>` |   
  
### readTensorboardBlobDataCallable()
    
    
    public final ServerStreamingCallable<ReadTensorboardBlobDataRequest,ReadTensorboardBlobDataResponse> readTensorboardBlobDataCallable()

Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project's Cloud Storage bucket without users having to obtain Cloud Storage access permission.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardBlobDataRequest request =
           ReadTensorboardBlobDataRequest.newBuilder()
               .setTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .addAllBlobIds(new ArrayList<String>())
               .build();
       ServerStream<ReadTensorboardBlobDataResponse> stream =
           tensorboardServiceClient.readTensorboardBlobDataCallable().call(request);
       for (ReadTensorboardBlobDataResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[ReadTensorboardBlobDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardBlobDataRequest),[ReadTensorboardBlobDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardBlobDataResponse)>` |   
  
### readTensorboardSize(@Nullable TensorboardName tensorboard)
    
    
    public final ReadTensorboardSizeResponse readTensorboardSize(@Nullable TensorboardName tensorboard)

Returns the storage size for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName tensorboard = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       ReadTensorboardSizeResponse response =
           tensorboardServiceClient.readTensorboardSize(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardSizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeResponse)` |   
  
### readTensorboardSize(ReadTensorboardSizeRequest request)
    
    
    public final ReadTensorboardSizeResponse readTensorboardSize(ReadTensorboardSizeRequest request)

Returns the storage size for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardSizeRequest request =
           ReadTensorboardSizeRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ReadTensorboardSizeResponse response = tensorboardServiceClient.readTensorboardSize(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadTensorboardSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardSizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeResponse)` |   
  
### readTensorboardSize(String tensorboard)
    
    
    public final ReadTensorboardSizeResponse readTensorboardSize(String tensorboard)

Returns the storage size for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboard =
           TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       ReadTensorboardSizeResponse response =
           tensorboardServiceClient.readTensorboardSize(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardSizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeResponse)` |   
  
### readTensorboardSizeCallable()
    
    
    public final UnaryCallable<ReadTensorboardSizeRequest,ReadTensorboardSizeResponse> readTensorboardSizeCallable()

Returns the storage size for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardSizeRequest request =
           ReadTensorboardSizeRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ApiFuture<ReadTensorboardSizeResponse> future =
           tensorboardServiceClient.readTensorboardSizeCallable().futureCall(request);
       // Do something.
       ReadTensorboardSizeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadTensorboardSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeRequest),[ReadTensorboardSizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardSizeResponse)>` |   
  
### readTensorboardTimeSeriesData(@Nullable TensorboardTimeSeriesName tensorboardTimeSeries)
    
    
    public final ReadTensorboardTimeSeriesDataResponse readTensorboardTimeSeriesData(@Nullable TensorboardTimeSeriesName tensorboardTimeSeries)

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeriesName tensorboardTimeSeries =
           TensorboardTimeSeriesName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]", "[TIME_SERIES]");
       ReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.readTensorboardTimeSeriesData(tensorboardTimeSeries);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeries` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardTimeSeriesName`  
Required. The resource name of the TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataResponse)` |   
  
### readTensorboardTimeSeriesData(ReadTensorboardTimeSeriesDataRequest request)
    
    
    public final ReadTensorboardTimeSeriesDataResponse readTensorboardTimeSeriesData(ReadTensorboardTimeSeriesDataRequest request)

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardTimeSeriesDataRequest request =
           ReadTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboardTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setMaxDataPoints(724001981)
               .setFilter("filter-1274492040")
               .build();
       ReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.readTensorboardTimeSeriesData(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataResponse)` |   
  
### readTensorboardTimeSeriesData(String tensorboardTimeSeries)
    
    
    public final ReadTensorboardTimeSeriesDataResponse readTensorboardTimeSeriesData(String tensorboardTimeSeries)

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboardTimeSeries =
           TensorboardTimeSeriesName.of(
                   "[PROJECT]",
                   "[LOCATION]",
                   "[TENSORBOARD]",
                   "[EXPERIMENT]",
                   "[RUN]",
                   "[TIME_SERIES]")
               .toString();
       ReadTensorboardTimeSeriesDataResponse response =
           tensorboardServiceClient.readTensorboardTimeSeriesData(tensorboardTimeSeries);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeries` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardTimeSeries to read data from. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataResponse)` |   
  
### readTensorboardTimeSeriesDataCallable()
    
    
    public final UnaryCallable<ReadTensorboardTimeSeriesDataRequest,ReadTensorboardTimeSeriesDataResponse> readTensorboardTimeSeriesDataCallable()

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardTimeSeriesDataRequest request =
           ReadTensorboardTimeSeriesDataRequest.newBuilder()
               .setTensorboardTimeSeries(
                   TensorboardTimeSeriesName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[TENSORBOARD]",
                           "[EXPERIMENT]",
                           "[RUN]",
                           "[TIME_SERIES]")
                       .toString())
               .setMaxDataPoints(724001981)
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ReadTensorboardTimeSeriesDataResponse> future =
           tensorboardServiceClient.readTensorboardTimeSeriesDataCallable().futureCall(request);
       // Do something.
       ReadTensorboardTimeSeriesDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataRequest),[ReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardTimeSeriesDataResponse)>` |   
  
### readTensorboardUsage(@Nullable TensorboardName tensorboard)
    
    
    public final ReadTensorboardUsageResponse readTensorboardUsage(@Nullable TensorboardName tensorboard)

Returns a list of monthly active users for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardName tensorboard = TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]");
       ReadTensorboardUsageResponse response =
           tensorboardServiceClient.readTensorboardUsage(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardName`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageResponse)` |   
  
### readTensorboardUsage(ReadTensorboardUsageRequest request)
    
    
    public final ReadTensorboardUsageResponse readTensorboardUsage(ReadTensorboardUsageRequest request)

Returns a list of monthly active users for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardUsageRequest request =
           ReadTensorboardUsageRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ReadTensorboardUsageResponse response =
           tensorboardServiceClient.readTensorboardUsage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReadTensorboardUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageResponse)` |   
  
### readTensorboardUsage(String tensorboard)
    
    
    public final ReadTensorboardUsageResponse readTensorboardUsage(String tensorboard)

Returns a list of monthly active users for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboard =
           TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString();
       ReadTensorboardUsageResponse response =
           tensorboardServiceClient.readTensorboardUsage(tensorboard);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
**Returns**  
---  
**Type** | **Description**  
`[ReadTensorboardUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageResponse)` |   
  
### readTensorboardUsageCallable()
    
    
    public final UnaryCallable<ReadTensorboardUsageRequest,ReadTensorboardUsageResponse> readTensorboardUsageCallable()

Returns a list of monthly active users for a given TensorBoard instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       ReadTensorboardUsageRequest request =
           ReadTensorboardUsageRequest.newBuilder()
               .setTensorboard(
                   TensorboardName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]").toString())
               .build();
       ApiFuture<ReadTensorboardUsageResponse> future =
           tensorboardServiceClient.readTensorboardUsageCallable().futureCall(request);
       // Do something.
       ReadTensorboardUsageResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReadTensorboardUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageRequest),[ReadTensorboardUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadTensorboardUsageResponse)>` |   
  
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = tensorboardServiceClient.setIamPolicy(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           tensorboardServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = tensorboardServiceClient.testIamPermissions(request);
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
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           tensorboardServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateTensorboardAsync(Tensorboard tensorboard, FieldMask updateMask)
    
    
    public final OperationFuture<Tensorboard,UpdateTensorboardOperationMetadata> updateTensorboardAsync(Tensorboard tensorboard, FieldMask updateMask)

Updates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       Tensorboard tensorboard = Tensorboard.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Tensorboard response =
           tensorboardServiceClient.updateTensorboardAsync(tensorboard, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboard` | `[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)`  
Required. The Tensorboard's `name` field is used to identify the Tensorboard to be updated. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Tensorboard resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[UpdateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardOperationMetadata)>` |   
  
### updateTensorboardAsync(UpdateTensorboardRequest request)
    
    
    public final OperationFuture<Tensorboard,UpdateTensorboardOperationMetadata> updateTensorboardAsync(UpdateTensorboardRequest request)

Updates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardRequest request =
           UpdateTensorboardRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       Tensorboard response = tensorboardServiceClient.updateTensorboardAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[UpdateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardOperationMetadata)>` |   
  
### updateTensorboardCallable()
    
    
    public final UnaryCallable<UpdateTensorboardRequest,Operation> updateTensorboardCallable()

Updates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardRequest request =
           UpdateTensorboardRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           tensorboardServiceClient.updateTensorboardCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTensorboardExperiment(TensorboardExperiment tensorboardExperiment, FieldMask updateMask)
    
    
    public final TensorboardExperiment updateTensorboardExperiment(TensorboardExperiment tensorboardExperiment, FieldMask updateMask)

Updates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperiment tensorboardExperiment = TensorboardExperiment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TensorboardExperiment response =
           tensorboardServiceClient.updateTensorboardExperiment(tensorboardExperiment, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardExperiment` | `[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)`  
Required. The TensorboardExperiment's `name` field is used to identify the TensorboardExperiment to be updated. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the TensorboardExperiment resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### updateTensorboardExperiment(UpdateTensorboardExperimentRequest request)
    
    
    public final TensorboardExperiment updateTensorboardExperiment(UpdateTensorboardExperimentRequest request)

Updates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardExperimentRequest request =
           UpdateTensorboardExperimentRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardExperiment(TensorboardExperiment.newBuilder().build())
               .build();
       TensorboardExperiment response =
           tensorboardServiceClient.updateTensorboardExperiment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardExperimentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)` |   
  
### updateTensorboardExperimentCallable()
    
    
    public final UnaryCallable<UpdateTensorboardExperimentRequest,TensorboardExperiment> updateTensorboardExperimentCallable()

Updates a TensorboardExperiment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardExperimentRequest request =
           UpdateTensorboardExperimentRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardExperiment(TensorboardExperiment.newBuilder().build())
               .build();
       ApiFuture<TensorboardExperiment> future =
           tensorboardServiceClient.updateTensorboardExperimentCallable().futureCall(request);
       // Do something.
       TensorboardExperiment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTensorboardExperimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardExperimentRequest),[TensorboardExperiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardExperiment)>` |   
  
### updateTensorboardOperationCallable()
    
    
    public final OperationCallable<UpdateTensorboardRequest,Tensorboard,UpdateTensorboardOperationMetadata> updateTensorboardOperationCallable()

Updates a Tensorboard.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardRequest request =
           UpdateTensorboardRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboard(Tensorboard.newBuilder().build())
               .build();
       OperationFuture<Tensorboard, UpdateTensorboardOperationMetadata> future =
           tensorboardServiceClient.updateTensorboardOperationCallable().futureCall(request);
       // Do something.
       Tensorboard response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTensorboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardRequest),[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard),[UpdateTensorboardOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardOperationMetadata)>` |   
  
### updateTensorboardRun(TensorboardRun tensorboardRun, FieldMask updateMask)
    
    
    public final TensorboardRun updateTensorboardRun(TensorboardRun tensorboardRun, FieldMask updateMask)

Updates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRun tensorboardRun = TensorboardRun.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TensorboardRun response =
           tensorboardServiceClient.updateTensorboardRun(tensorboardRun, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardRun` | `[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)`  
Required. The TensorboardRun's `name` field is used to identify the TensorboardRun to be updated. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the TensorboardRun resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### updateTensorboardRun(UpdateTensorboardRunRequest request)
    
    
    public final TensorboardRun updateTensorboardRun(UpdateTensorboardRunRequest request)

Updates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardRunRequest request =
           UpdateTensorboardRunRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardRun(TensorboardRun.newBuilder().build())
               .build();
       TensorboardRun response = tensorboardServiceClient.updateTensorboardRun(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardRunRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)` |   
  
### updateTensorboardRunCallable()
    
    
    public final UnaryCallable<UpdateTensorboardRunRequest,TensorboardRun> updateTensorboardRunCallable()

Updates a TensorboardRun.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardRunRequest request =
           UpdateTensorboardRunRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardRun(TensorboardRun.newBuilder().build())
               .build();
       ApiFuture<TensorboardRun> future =
           tensorboardServiceClient.updateTensorboardRunCallable().futureCall(request);
       // Do something.
       TensorboardRun response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTensorboardRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardRunRequest),[TensorboardRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardRun)>` |   
  
### updateTensorboardTimeSeries(TensorboardTimeSeries tensorboardTimeSeries, FieldMask updateMask)
    
    
    public final TensorboardTimeSeries updateTensorboardTimeSeries(TensorboardTimeSeries tensorboardTimeSeries, FieldMask updateMask)

Updates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardTimeSeries tensorboardTimeSeries = TensorboardTimeSeries.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TensorboardTimeSeries response =
           tensorboardServiceClient.updateTensorboardTimeSeries(tensorboardTimeSeries, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardTimeSeries` | `[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)`  
Required. The TensorboardTimeSeries' `name` field is used to identify the TensorboardTimeSeries to be updated. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the TensorboardTimeSeries resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it's in the mask. If the user does not provide a mask then all fields are overwritten if new values are specified.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### updateTensorboardTimeSeries(UpdateTensorboardTimeSeriesRequest request)
    
    
    public final TensorboardTimeSeries updateTensorboardTimeSeries(UpdateTensorboardTimeSeriesRequest request)

Updates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardTimeSeriesRequest request =
           UpdateTensorboardTimeSeriesRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardTimeSeries(TensorboardTimeSeries.newBuilder().build())
               .build();
       TensorboardTimeSeries response =
           tensorboardServiceClient.updateTensorboardTimeSeries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardTimeSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)` |   
  
### updateTensorboardTimeSeriesCallable()
    
    
    public final UnaryCallable<UpdateTensorboardTimeSeriesRequest,TensorboardTimeSeries> updateTensorboardTimeSeriesCallable()

Updates a TensorboardTimeSeries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       UpdateTensorboardTimeSeriesRequest request =
           UpdateTensorboardTimeSeriesRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTensorboardTimeSeries(TensorboardTimeSeries.newBuilder().build())
               .build();
       ApiFuture<TensorboardTimeSeries> future =
           tensorboardServiceClient.updateTensorboardTimeSeriesCallable().futureCall(request);
       // Do something.
       TensorboardTimeSeries response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateTensorboardTimeSeriesRequest),[TensorboardTimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardTimeSeries)>` |   
  
### writeTensorboardExperimentData(@Nullable TensorboardExperimentName tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests)
    
    
    public final WriteTensorboardExperimentDataResponse writeTensorboardExperimentData(@Nullable TensorboardExperimentName tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests)

Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardExperimentName tensorboardExperiment =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]");
       List<WriteTensorboardRunDataRequest> writeRunDataRequests = new ArrayList<>();
       WriteTensorboardExperimentDataResponse response =
           tensorboardServiceClient.writeTensorboardExperimentData(
               tensorboardExperiment, writeRunDataRequests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardExperiment` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardExperimentName`  
Required. The resource name of the TensorboardExperiment to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
`writeRunDataRequests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WriteTensorboardRunDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataRequest)>`  
Required. Requests containing per-run TensorboardTimeSeries data to write.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataResponse)` |   
  
### writeTensorboardExperimentData(WriteTensorboardExperimentDataRequest request)
    
    
    public final WriteTensorboardExperimentDataResponse writeTensorboardExperimentData(WriteTensorboardExperimentDataRequest request)

Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       WriteTensorboardExperimentDataRequest request =
           WriteTensorboardExperimentDataRequest.newBuilder()
               .setTensorboardExperiment(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllWriteRunDataRequests(new ArrayList<WriteTensorboardRunDataRequest>())
               .build();
       WriteTensorboardExperimentDataResponse response =
           tensorboardServiceClient.writeTensorboardExperimentData(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataResponse)` |   
  
### writeTensorboardExperimentData(String tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests)
    
    
    public final WriteTensorboardExperimentDataResponse writeTensorboardExperimentData(String tensorboardExperiment, List<WriteTensorboardRunDataRequest> writeRunDataRequests)

Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboardExperiment =
           TensorboardExperimentName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
               .toString();
       List<WriteTensorboardRunDataRequest> writeRunDataRequests = new ArrayList<>();
       WriteTensorboardExperimentDataResponse response =
           tensorboardServiceClient.writeTensorboardExperimentData(
               tensorboardExperiment, writeRunDataRequests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardExperiment` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardExperiment to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`  
`writeRunDataRequests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WriteTensorboardRunDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataRequest)>`  
Required. Requests containing per-run TensorboardTimeSeries data to write.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataResponse)` |   
  
### writeTensorboardExperimentDataCallable()
    
    
    public final UnaryCallable<WriteTensorboardExperimentDataRequest,WriteTensorboardExperimentDataResponse> writeTensorboardExperimentDataCallable()

Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       WriteTensorboardExperimentDataRequest request =
           WriteTensorboardExperimentDataRequest.newBuilder()
               .setTensorboardExperiment(
                   TensorboardExperimentName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]")
                       .toString())
               .addAllWriteRunDataRequests(new ArrayList<WriteTensorboardRunDataRequest>())
               .build();
       ApiFuture<WriteTensorboardExperimentDataResponse> future =
           tensorboardServiceClient.writeTensorboardExperimentDataCallable().futureCall(request);
       // Do something.
       WriteTensorboardExperimentDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataRequest),[WriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardExperimentDataResponse)>` |   
  
### writeTensorboardRunData(@Nullable TensorboardRunName tensorboardRun, List<TimeSeriesData> timeSeriesData)
    
    
    public final WriteTensorboardRunDataResponse writeTensorboardRunData(@Nullable TensorboardRunName tensorboardRun, List<TimeSeriesData> timeSeriesData)

Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       TensorboardRunName tensorboardRun =
           TensorboardRunName.of(
               "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]");
       List<TimeSeriesData> timeSeriesData = new ArrayList<>();
       WriteTensorboardRunDataResponse response =
           tensorboardServiceClient.writeTensorboardRunData(tensorboardRun, timeSeriesData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardRun` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TensorboardRunName`  
Required. The resource name of the TensorboardRun to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
`timeSeriesData` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TimeSeriesData](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimeSeriesData)>`  
Required. The TensorboardTimeSeries data to write. Values with in a time series are indexed by their step value. Repeated writes to the same step will overwrite the existing value for that step. The upper limit of data points per write request is 5000.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardRunDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataResponse)` |   
  
### writeTensorboardRunData(WriteTensorboardRunDataRequest request)
    
    
    public final WriteTensorboardRunDataResponse writeTensorboardRunData(WriteTensorboardRunDataRequest request)

Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       WriteTensorboardRunDataRequest request =
           WriteTensorboardRunDataRequest.newBuilder()
               .setTensorboardRun(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .addAllTimeSeriesData(new ArrayList<TimeSeriesData>())
               .build();
       WriteTensorboardRunDataResponse response =
           tensorboardServiceClient.writeTensorboardRunData(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteTensorboardRunDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardRunDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataResponse)` |   
  
### writeTensorboardRunData(String tensorboardRun, List<TimeSeriesData> timeSeriesData)
    
    
    public final WriteTensorboardRunDataResponse writeTensorboardRunData(String tensorboardRun, List<TimeSeriesData> timeSeriesData)

Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       String tensorboardRun =
           TensorboardRunName.of("[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
               .toString();
       List<TimeSeriesData> timeSeriesData = new ArrayList<>();
       WriteTensorboardRunDataResponse response =
           tensorboardServiceClient.writeTensorboardRunData(tensorboardRun, timeSeriesData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tensorboardRun` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TensorboardRun to write data to. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`  
`timeSeriesData` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TimeSeriesData](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimeSeriesData)>`  
Required. The TensorboardTimeSeries data to write. Values with in a time series are indexed by their step value. Repeated writes to the same step will overwrite the existing value for that step. The upper limit of data points per write request is 5000.  
**Returns**  
---  
**Type** | **Description**  
`[WriteTensorboardRunDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataResponse)` |   
  
### writeTensorboardRunDataCallable()
    
    
    public final UnaryCallable<WriteTensorboardRunDataRequest,WriteTensorboardRunDataResponse> writeTensorboardRunDataCallable()

Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TensorboardServiceClient tensorboardServiceClient = TensorboardServiceClient.create()) {
       WriteTensorboardRunDataRequest request =
           WriteTensorboardRunDataRequest.newBuilder()
               .setTensorboardRun(
                   TensorboardRunName.of(
                           "[PROJECT]", "[LOCATION]", "[TENSORBOARD]", "[EXPERIMENT]", "[RUN]")
                       .toString())
               .addAllTimeSeriesData(new ArrayList<TimeSeriesData>())
               .build();
       ApiFuture<WriteTensorboardRunDataResponse> future =
           tensorboardServiceClient.writeTensorboardRunDataCallable().futureCall(request);
       // Do something.
       WriteTensorboardRunDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteTensorboardRunDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataRequest),[WriteTensorboardRunDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WriteTensorboardRunDataResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
