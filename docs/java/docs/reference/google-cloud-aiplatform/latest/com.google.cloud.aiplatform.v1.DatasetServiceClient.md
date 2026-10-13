---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient
title: Class DatasetServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:43.146113+00:00
---

# Class DatasetServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatasetServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/DatasetServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The service that manages Vertex AI Dataset and its child resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       Dataset response = datasetServiceClient.getDataset(name);
     }
     

Note: close() needs to be called on the DatasetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataset |  Creates a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDatasetAsync(CreateDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDatasetAsync(LocationName parent, Dataset dataset) 
  * createDatasetAsync(String parent, Dataset dataset) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDatasetOperationCallable() 
  * createDatasetCallable() 

  
GetDataset |  Gets a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataset(GetDatasetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataset(DatasetName name) 
  * getDataset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDatasetCallable() 

  
UpdateDataset |  Updates a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataset(UpdateDatasetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataset(Dataset dataset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDatasetCallable() 

  
ListDatasets |  Lists Datasets in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatasets(ListDatasetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatasets(LocationName parent) 
  * listDatasets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatasetsPagedCallable() 
  * listDatasetsCallable() 

  
DeleteDataset |  Deletes a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDatasetAsync(DeleteDatasetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDatasetAsync(DatasetName name) 
  * deleteDatasetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDatasetOperationCallable() 
  * deleteDatasetCallable() 

  
ImportData |  Imports data into a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDataAsync(ImportDataRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importDataAsync(DatasetName name, List<ImportDataConfig> importConfigs) 
  * importDataAsync(String name, List<ImportDataConfig> importConfigs) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDataOperationCallable() 
  * importDataCallable() 

  
ExportData |  Exports data from a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDataAsync(ExportDataRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportDataAsync(DatasetName name, ExportDataConfig exportConfig) 
  * exportDataAsync(String name, ExportDataConfig exportConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDataOperationCallable() 
  * exportDataCallable() 

  
CreateDatasetVersion |  Create a version from a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDatasetVersionAsync(CreateDatasetVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDatasetVersionAsync(DatasetName parent, DatasetVersion datasetVersion) 
  * createDatasetVersionAsync(String parent, DatasetVersion datasetVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDatasetVersionOperationCallable() 
  * createDatasetVersionCallable() 

  
UpdateDatasetVersion |  Updates a DatasetVersion. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDatasetVersion(UpdateDatasetVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDatasetVersion(DatasetVersion datasetVersion, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDatasetVersionCallable() 

  
DeleteDatasetVersion |  Deletes a Dataset version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDatasetVersionAsync(DeleteDatasetVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDatasetVersionAsync(DatasetVersionName name) 
  * deleteDatasetVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDatasetVersionOperationCallable() 
  * deleteDatasetVersionCallable() 

  
GetDatasetVersion |  Gets a Dataset version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDatasetVersion(GetDatasetVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDatasetVersion(DatasetVersionName name) 
  * getDatasetVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDatasetVersionCallable() 

  
ListDatasetVersions |  Lists DatasetVersions in a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatasetVersions(ListDatasetVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatasetVersions(DatasetName parent) 
  * listDatasetVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatasetVersionsPagedCallable() 
  * listDatasetVersionsCallable() 

  
RestoreDatasetVersion |  Restores a dataset version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreDatasetVersionAsync(RestoreDatasetVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreDatasetVersionAsync(DatasetVersionName name) 
  * restoreDatasetVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreDatasetVersionOperationCallable() 
  * restoreDatasetVersionCallable() 

  
ListDataItems |  Lists DataItems in a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataItems(ListDataItemsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataItems(DatasetName parent) 
  * listDataItems(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataItemsPagedCallable() 
  * listDataItemsCallable() 

  
SearchDataItems |  Searches DataItems in a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchDataItems(SearchDataItemsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchDataItemsPagedCallable() 
  * searchDataItemsCallable() 

  
ListSavedQueries |  Lists SavedQueries in a Dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSavedQueries(ListSavedQueriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSavedQueries(DatasetName parent) 
  * listSavedQueries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSavedQueriesPagedCallable() 
  * listSavedQueriesCallable() 

  
DeleteSavedQuery |  Deletes a SavedQuery. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSavedQueryAsync(DeleteSavedQueryRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSavedQueryAsync(SavedQueryName name) 
  * deleteSavedQueryAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSavedQueryOperationCallable() 
  * deleteSavedQueryCallable() 

  
GetAnnotationSpec |  Gets an AnnotationSpec. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAnnotationSpec(GetAnnotationSpecRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAnnotationSpec(AnnotationSpecName name) 
  * getAnnotationSpec(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAnnotationSpecCallable() 

  
ListAnnotations |  Lists Annotations belongs to a dataitem. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAnnotations(ListAnnotationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAnnotations(DataItemName parent) 
  * listAnnotations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAnnotationsPagedCallable() 
  * listAnnotationsCallable() 

  
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

This class can be customized by passing in a custom instance of DatasetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatasetServiceSettings datasetServiceSettings =
         DatasetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DatasetServiceClient datasetServiceClient = DatasetServiceClient.create(datasetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatasetServiceSettings datasetServiceSettings =
         DatasetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DatasetServiceClient datasetServiceClient = DatasetServiceClient.create(datasetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatasetServiceClient

## Static Methods 

### create()
    
    
    public static final DatasetServiceClient create()

Constructs an instance of DatasetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DatasetServiceSettings settings)
    
    
    public static final DatasetServiceClient create(DatasetServiceSettings settings)

Constructs an instance of DatasetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DatasetServiceStub stub)
    
    
    public static final DatasetServiceClient create(DatasetServiceStub stub)

Constructs an instance of DatasetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DatasetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DatasetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DatasetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient)` |   
  
## Constructors 

### DatasetServiceClient(DatasetServiceSettings settings)
    
    
    protected DatasetServiceClient(DatasetServiceSettings settings)

Constructs an instance of DatasetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings)`  
  
  
### DatasetServiceClient(DatasetServiceStub stub)
    
    
    protected DatasetServiceClient(DatasetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DatasetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DatasetServiceStub)`  
  
  
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
    
    
    public final OperationFuture<Dataset,CreateDatasetOperationMetadata> createDatasetAsync(@Nullable LocationName parent, Dataset dataset)

Creates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Dataset dataset = Dataset.newBuilder().build();
       Dataset response = datasetServiceClient.createDatasetAsync(parent, dataset).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the Dataset in. Format: `projects/{project}/locations/{location}`  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)`  
Required. The Dataset to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset),[CreateDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata)>` |   
  
### createDatasetAsync(CreateDatasetRequest request)
    
    
    public final OperationFuture<Dataset,CreateDatasetOperationMetadata> createDatasetAsync(CreateDatasetRequest request)

Creates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       Dataset response = datasetServiceClient.createDatasetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset),[CreateDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata)>` |   
  
### createDatasetAsync(String parent, Dataset dataset)
    
    
    public final OperationFuture<Dataset,CreateDatasetOperationMetadata> createDatasetAsync(String parent, Dataset dataset)

Creates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Dataset dataset = Dataset.newBuilder().build();
       Dataset response = datasetServiceClient.createDatasetAsync(parent, dataset).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the Dataset in. Format: `projects/{project}/locations/{location}`  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)`  
Required. The Dataset to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset),[CreateDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata)>` |   
  
### createDatasetCallable()
    
    
    public final UnaryCallable<CreateDatasetRequest,Operation> createDatasetCallable()

Creates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.createDatasetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDatasetOperationCallable()
    
    
    public final OperationCallable<CreateDatasetRequest,Dataset,CreateDatasetOperationMetadata> createDatasetOperationCallable()

Creates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetRequest request =
           CreateDatasetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataset(Dataset.newBuilder().build())
               .build();
       OperationFuture<Dataset, CreateDatasetOperationMetadata> future =
           datasetServiceClient.createDatasetOperationCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset),[CreateDatasetOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata)>` |   
  
### createDatasetVersionAsync(@Nullable DatasetName parent, DatasetVersion datasetVersion)
    
    
    public final OperationFuture<DatasetVersion,CreateDatasetVersionOperationMetadata> createDatasetVersionAsync(@Nullable DatasetName parent, DatasetVersion datasetVersion)

Create a version from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       DatasetVersion datasetVersion = DatasetVersion.newBuilder().build();
       DatasetVersion response =
           datasetServiceClient.createDatasetVersionAsync(parent, datasetVersion).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`datasetVersion` | `[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)`  
Required. The version to be created. The same CMEK policies with the original Dataset will be applied the dataset version. So here we don't need to specify the EncryptionSpecType here.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[CreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionOperationMetadata)>` |   
  
### createDatasetVersionAsync(CreateDatasetVersionRequest request)
    
    
    public final OperationFuture<DatasetVersion,CreateDatasetVersionOperationMetadata> createDatasetVersionAsync(CreateDatasetVersionRequest request)

Create a version from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetVersionRequest request =
           CreateDatasetVersionRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setDatasetVersion(DatasetVersion.newBuilder().build())
               .build();
       DatasetVersion response = datasetServiceClient.createDatasetVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[CreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionOperationMetadata)>` |   
  
### createDatasetVersionAsync(String parent, DatasetVersion datasetVersion)
    
    
    public final OperationFuture<DatasetVersion,CreateDatasetVersionOperationMetadata> createDatasetVersionAsync(String parent, DatasetVersion datasetVersion)

Create a version from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       DatasetVersion datasetVersion = DatasetVersion.newBuilder().build();
       DatasetVersion response =
           datasetServiceClient.createDatasetVersionAsync(parent, datasetVersion).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`datasetVersion` | `[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)`  
Required. The version to be created. The same CMEK policies with the original Dataset will be applied the dataset version. So here we don't need to specify the EncryptionSpecType here.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[CreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionOperationMetadata)>` |   
  
### createDatasetVersionCallable()
    
    
    public final UnaryCallable<CreateDatasetVersionRequest,Operation> createDatasetVersionCallable()

Create a version from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetVersionRequest request =
           CreateDatasetVersionRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setDatasetVersion(DatasetVersion.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.createDatasetVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDatasetVersionOperationCallable()
    
    
    public final OperationCallable<CreateDatasetVersionRequest,DatasetVersion,CreateDatasetVersionOperationMetadata> createDatasetVersionOperationCallable()

Create a version from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       CreateDatasetVersionRequest request =
           CreateDatasetVersionRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setDatasetVersion(DatasetVersion.newBuilder().build())
               .build();
       OperationFuture<DatasetVersion, CreateDatasetVersionOperationMetadata> future =
           datasetServiceClient.createDatasetVersionOperationCallable().futureCall(request);
       // Do something.
       DatasetVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionRequest),[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[CreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionOperationMetadata)>` |   
  
### deleteDatasetAsync(@Nullable DatasetName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetAsync(@Nullable DatasetName name)

Deletes a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       datasetServiceClient.deleteDatasetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The resource name of the Dataset to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetAsync(DeleteDatasetRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetAsync(DeleteDatasetRequest request)

Deletes a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       datasetServiceClient.deleteDatasetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetAsync(String name)

Deletes a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       datasetServiceClient.deleteDatasetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetCallable()
    
    
    public final UnaryCallable<DeleteDatasetRequest,Operation> deleteDatasetCallable()

Deletes a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.deleteDatasetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDatasetOperationCallable()
    
    
    public final OperationCallable<DeleteDatasetRequest,Empty,DeleteOperationMetadata> deleteDatasetOperationCallable()

Deletes a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetRequest request =
           DeleteDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           datasetServiceClient.deleteDatasetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetVersionAsync(@Nullable DatasetVersionName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetVersionAsync(@Nullable DatasetVersionName name)

Deletes a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetVersionName name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]");
       datasetServiceClient.deleteDatasetVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetVersionName`  
Required. The resource name of the Dataset version to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetVersionAsync(DeleteDatasetVersionRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetVersionAsync(DeleteDatasetVersionRequest request)

Deletes a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetVersionRequest request =
           DeleteDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       datasetServiceClient.deleteDatasetVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetVersionAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDatasetVersionAsync(String name)

Deletes a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
               .toString();
       datasetServiceClient.deleteDatasetVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset version to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDatasetVersionCallable()
    
    
    public final UnaryCallable<DeleteDatasetVersionRequest,Operation> deleteDatasetVersionCallable()

Deletes a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetVersionRequest request =
           DeleteDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.deleteDatasetVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDatasetVersionOperationCallable()
    
    
    public final OperationCallable<DeleteDatasetVersionRequest,Empty,DeleteOperationMetadata> deleteDatasetVersionOperationCallable()

Deletes a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteDatasetVersionRequest request =
           DeleteDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           datasetServiceClient.deleteDatasetVersionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSavedQueryAsync(@Nullable SavedQueryName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSavedQueryAsync(@Nullable SavedQueryName name)

Deletes a SavedQuery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SavedQueryName name =
           SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]");
       datasetServiceClient.deleteSavedQueryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.SavedQueryName`  
Required. The resource name of the SavedQuery to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSavedQueryAsync(DeleteSavedQueryRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSavedQueryAsync(DeleteSavedQueryRequest request)

Deletes a SavedQuery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteSavedQueryRequest request =
           DeleteSavedQueryRequest.newBuilder()
               .setName(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .build();
       datasetServiceClient.deleteSavedQueryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSavedQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSavedQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSavedQueryAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSavedQueryAsync(String name)

Deletes a SavedQuery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name =
           SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]").toString();
       datasetServiceClient.deleteSavedQueryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the SavedQuery to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSavedQueryCallable()
    
    
    public final UnaryCallable<DeleteSavedQueryRequest,Operation> deleteSavedQueryCallable()

Deletes a SavedQuery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteSavedQueryRequest request =
           DeleteSavedQueryRequest.newBuilder()
               .setName(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.deleteSavedQueryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSavedQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSavedQueryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSavedQueryOperationCallable()
    
    
    public final OperationCallable<DeleteSavedQueryRequest,Empty,DeleteOperationMetadata> deleteSavedQueryOperationCallable()

Deletes a SavedQuery.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DeleteSavedQueryRequest request =
           DeleteSavedQueryRequest.newBuilder()
               .setName(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           datasetServiceClient.deleteSavedQueryOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSavedQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSavedQueryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### exportDataAsync(@Nullable DatasetName name, ExportDataConfig exportConfig)
    
    
    public final OperationFuture<ExportDataResponse,ExportDataOperationMetadata> exportDataAsync(@Nullable DatasetName name, ExportDataConfig exportConfig)

Exports data from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       ExportDataConfig exportConfig = ExportDataConfig.newBuilder().build();
       ExportDataResponse response = datasetServiceClient.exportDataAsync(name, exportConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`exportConfig` | `[ExportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataConfig)`  
Required. The desired output location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataResponse),[ExportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataOperationMetadata)>` |   
  
### exportDataAsync(ExportDataRequest request)
    
    
    public final OperationFuture<ExportDataResponse,ExportDataOperationMetadata> exportDataAsync(ExportDataRequest request)

Exports data from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setExportConfig(ExportDataConfig.newBuilder().build())
               .build();
       ExportDataResponse response = datasetServiceClient.exportDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataResponse),[ExportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataOperationMetadata)>` |   
  
### exportDataAsync(String name, ExportDataConfig exportConfig)
    
    
    public final OperationFuture<ExportDataResponse,ExportDataOperationMetadata> exportDataAsync(String name, ExportDataConfig exportConfig)

Exports data from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       ExportDataConfig exportConfig = ExportDataConfig.newBuilder().build();
       ExportDataResponse response = datasetServiceClient.exportDataAsync(name, exportConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`exportConfig` | `[ExportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataConfig)`  
Required. The desired output location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataResponse),[ExportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataOperationMetadata)>` |   
  
### exportDataCallable()
    
    
    public final UnaryCallable<ExportDataRequest,Operation> exportDataCallable()

Exports data from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setExportConfig(ExportDataConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = datasetServiceClient.exportDataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDataOperationCallable()
    
    
    public final OperationCallable<ExportDataRequest,ExportDataResponse,ExportDataOperationMetadata> exportDataOperationCallable()

Exports data from a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setExportConfig(ExportDataConfig.newBuilder().build())
               .build();
       OperationFuture<ExportDataResponse, ExportDataOperationMetadata> future =
           datasetServiceClient.exportDataOperationCallable().futureCall(request);
       // Do something.
       ExportDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataRequest),[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataResponse),[ExportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataOperationMetadata)>` |   
  
### getAnnotationSpec(@Nullable AnnotationSpecName name)
    
    
    public final AnnotationSpec getAnnotationSpec(@Nullable AnnotationSpecName name)

Gets an AnnotationSpec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       AnnotationSpecName name =
           AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]");
       AnnotationSpec response = datasetServiceClient.getAnnotationSpec(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.AnnotationSpecName`  
Required. The name of the AnnotationSpec resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AnnotationSpec)` |   
  
### getAnnotationSpec(GetAnnotationSpecRequest request)
    
    
    public final AnnotationSpec getAnnotationSpec(GetAnnotationSpecRequest request)

Gets an AnnotationSpec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetAnnotationSpecRequest request =
           GetAnnotationSpecRequest.newBuilder()
               .setName(
                   AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
                       .toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       AnnotationSpec response = datasetServiceClient.getAnnotationSpec(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetAnnotationSpecRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AnnotationSpec)` |   
  
### getAnnotationSpec(String name)
    
    
    public final AnnotationSpec getAnnotationSpec(String name)

Gets an AnnotationSpec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name =
           AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
               .toString();
       AnnotationSpec response = datasetServiceClient.getAnnotationSpec(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the AnnotationSpec resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AnnotationSpec)` |   
  
### getAnnotationSpecCallable()
    
    
    public final UnaryCallable<GetAnnotationSpecRequest,AnnotationSpec> getAnnotationSpecCallable()

Gets an AnnotationSpec.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetAnnotationSpecRequest request =
           GetAnnotationSpecRequest.newBuilder()
               .setName(
                   AnnotationSpecName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[ANNOTATION_SPEC]")
                       .toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AnnotationSpec> future =
           datasetServiceClient.getAnnotationSpecCallable().futureCall(request);
       // Do something.
       AnnotationSpec response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetAnnotationSpecRequest),[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AnnotationSpec)>` |   
  
### getDataset(@Nullable DatasetName name)
    
    
    public final Dataset getDataset(@Nullable DatasetName name)

Gets a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       Dataset response = datasetServiceClient.getDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The name of the Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)` |   
  
### getDataset(GetDatasetRequest request)
    
    
    public final Dataset getDataset(GetDatasetRequest request)

Gets a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetDatasetRequest request =
           GetDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       Dataset response = datasetServiceClient.getDataset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)` |   
  
### getDataset(String name)
    
    
    public final Dataset getDataset(String name)

Gets a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       Dataset response = datasetServiceClient.getDataset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)` |   
  
### getDatasetCallable()
    
    
    public final UnaryCallable<GetDatasetRequest,Dataset> getDatasetCallable()

Gets a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetDatasetRequest request =
           GetDatasetRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Dataset> future = datasetServiceClient.getDatasetCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)>` |   
  
### getDatasetVersion(@Nullable DatasetVersionName name)
    
    
    public final DatasetVersion getDatasetVersion(@Nullable DatasetVersionName name)

Gets a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetVersionName name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]");
       DatasetVersion response = datasetServiceClient.getDatasetVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetVersionName`  
Required. The resource name of the Dataset version to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)` |   
  
### getDatasetVersion(GetDatasetVersionRequest request)
    
    
    public final DatasetVersion getDatasetVersion(GetDatasetVersionRequest request)

Gets a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetDatasetVersionRequest request =
           GetDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       DatasetVersion response = datasetServiceClient.getDatasetVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)` |   
  
### getDatasetVersion(String name)
    
    
    public final DatasetVersion getDatasetVersion(String name)

Gets a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
               .toString();
       DatasetVersion response = datasetServiceClient.getDatasetVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset version to delete. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)` |   
  
### getDatasetVersionCallable()
    
    
    public final UnaryCallable<GetDatasetVersionRequest,DatasetVersion> getDatasetVersionCallable()

Gets a Dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetDatasetVersionRequest request =
           GetDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DatasetVersion> future =
           datasetServiceClient.getDatasetVersionCallable().futureCall(request);
       // Do something.
       DatasetVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetVersionRequest),[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = datasetServiceClient.getIamPolicy(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = datasetServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = datasetServiceClient.getLocation(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = datasetServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DatasetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetServiceSettings` |   
  
### getStub()
    
    
    public DatasetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DatasetServiceStub)` |   
  
### importDataAsync(@Nullable DatasetName name, List<ImportDataConfig> importConfigs)
    
    
    public final OperationFuture<ImportDataResponse,ImportDataOperationMetadata> importDataAsync(@Nullable DatasetName name, List<ImportDataConfig> importConfigs)

Imports data into a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       List<ImportDataConfig> importConfigs = new ArrayList<>();
       ImportDataResponse response = datasetServiceClient.importDataAsync(name, importConfigs).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`importConfigs` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ImportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataConfig)>`  
Required. The desired input locations. The contents of all input locations will be imported in one batch.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse),[ImportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataOperationMetadata)>` |   
  
### importDataAsync(ImportDataRequest request)
    
    
    public final OperationFuture<ImportDataResponse,ImportDataOperationMetadata> importDataAsync(ImportDataRequest request)

Imports data into a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .addAllImportConfigs(new ArrayList<ImportDataConfig>())
               .build();
       ImportDataResponse response = datasetServiceClient.importDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse),[ImportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataOperationMetadata)>` |   
  
### importDataAsync(String name, List<ImportDataConfig> importConfigs)
    
    
    public final OperationFuture<ImportDataResponse,ImportDataOperationMetadata> importDataAsync(String name, List<ImportDataConfig> importConfigs)

Imports data into a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       List<ImportDataConfig> importConfigs = new ArrayList<>();
       ImportDataResponse response = datasetServiceClient.importDataAsync(name, importConfigs).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`importConfigs` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ImportDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataConfig)>`  
Required. The desired input locations. The contents of all input locations will be imported in one batch.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse),[ImportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataOperationMetadata)>` |   
  
### importDataCallable()
    
    
    public final UnaryCallable<ImportDataRequest,Operation> importDataCallable()

Imports data into a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .addAllImportConfigs(new ArrayList<ImportDataConfig>())
               .build();
       ApiFuture<Operation> future = datasetServiceClient.importDataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDataOperationCallable()
    
    
    public final OperationCallable<ImportDataRequest,ImportDataResponse,ImportDataOperationMetadata> importDataOperationCallable()

Imports data into a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .addAllImportConfigs(new ArrayList<ImportDataConfig>())
               .build();
       OperationFuture<ImportDataResponse, ImportDataOperationMetadata> future =
           datasetServiceClient.importDataOperationCallable().futureCall(request);
       // Do something.
       ImportDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataRequest),[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataResponse),[ImportDataOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataOperationMetadata)>` |   
  
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
  
### listAnnotations(@Nullable DataItemName parent)
    
    
    public final DatasetServiceClient.ListAnnotationsPagedResponse listAnnotations(@Nullable DataItemName parent)

Lists Annotations belongs to a dataitem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DataItemName parent = DataItemName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATA_ITEM]");
       for (Annotation element : datasetServiceClient.listAnnotations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DataItemName`  
Required. The resource name of the DataItem to list Annotations from. Format: `projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListAnnotationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListAnnotationsPagedResponse)` |   
  
### listAnnotations(ListAnnotationsRequest request)
    
    
    public final DatasetServiceClient.ListAnnotationsPagedResponse listAnnotations(ListAnnotationsRequest request)

Lists Annotations belongs to a dataitem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListAnnotationsRequest request =
           ListAnnotationsRequest.newBuilder()
               .setParent(
                   DataItemName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATA_ITEM]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Annotation element : datasetServiceClient.listAnnotations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListAnnotationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListAnnotationsPagedResponse)` |   
  
### listAnnotations(String parent)
    
    
    public final DatasetServiceClient.ListAnnotationsPagedResponse listAnnotations(String parent)

Lists Annotations belongs to a dataitem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent =
           DataItemName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATA_ITEM]").toString();
       for (Annotation element : datasetServiceClient.listAnnotations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataItem to list Annotations from. Format: `projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListAnnotationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListAnnotationsPagedResponse)` |   
  
### listAnnotationsCallable()
    
    
    public final UnaryCallable<ListAnnotationsRequest,ListAnnotationsResponse> listAnnotationsCallable()

Lists Annotations belongs to a dataitem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListAnnotationsRequest request =
           ListAnnotationsRequest.newBuilder()
               .setParent(
                   DataItemName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATA_ITEM]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAnnotationsResponse response =
             datasetServiceClient.listAnnotationsCallable().call(request);
         for (Annotation element : response.getAnnotationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsRequest),[ListAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsResponse)>` |   
  
### listAnnotationsPagedCallable()
    
    
    public final UnaryCallable<ListAnnotationsRequest,DatasetServiceClient.ListAnnotationsPagedResponse> listAnnotationsPagedCallable()

Lists Annotations belongs to a dataitem.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListAnnotationsRequest request =
           ListAnnotationsRequest.newBuilder()
               .setParent(
                   DataItemName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATA_ITEM]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Annotation> future =
           datasetServiceClient.listAnnotationsPagedCallable().futureCall(request);
       // Do something.
       for (Annotation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsRequest),[ListAnnotationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListAnnotationsPagedResponse)>` |   
  
### listDataItems(@Nullable DatasetName parent)
    
    
    public final DatasetServiceClient.ListDataItemsPagedResponse listDataItems(@Nullable DatasetName parent)

Lists DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       for (DataItem element : datasetServiceClient.listDataItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The resource name of the Dataset to list DataItems from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDataItemsPagedResponse)` |   
  
### listDataItems(ListDataItemsRequest request)
    
    
    public final DatasetServiceClient.ListDataItemsPagedResponse listDataItems(ListDataItemsRequest request)

Lists DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDataItemsRequest request =
           ListDataItemsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataItem element : datasetServiceClient.listDataItems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDataItemsPagedResponse)` |   
  
### listDataItems(String parent)
    
    
    public final DatasetServiceClient.ListDataItemsPagedResponse listDataItems(String parent)

Lists DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       for (DataItem element : datasetServiceClient.listDataItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset to list DataItems from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDataItemsPagedResponse)` |   
  
### listDataItemsCallable()
    
    
    public final UnaryCallable<ListDataItemsRequest,ListDataItemsResponse> listDataItemsCallable()

Lists DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDataItemsRequest request =
           ListDataItemsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataItemsResponse response = datasetServiceClient.listDataItemsCallable().call(request);
         for (DataItem element : response.getDataItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsRequest),[ListDataItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsResponse)>` |   
  
### listDataItemsPagedCallable()
    
    
    public final UnaryCallable<ListDataItemsRequest,DatasetServiceClient.ListDataItemsPagedResponse> listDataItemsPagedCallable()

Lists DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDataItemsRequest request =
           ListDataItemsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataItem> future =
           datasetServiceClient.listDataItemsPagedCallable().futureCall(request);
       // Do something.
       for (DataItem element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsRequest),[ListDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDataItemsPagedResponse)>` |   
  
### listDatasetVersions(@Nullable DatasetName parent)
    
    
    public final DatasetServiceClient.ListDatasetVersionsPagedResponse listDatasetVersions(@Nullable DatasetName parent)

Lists DatasetVersions in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       for (DatasetVersion element : datasetServiceClient.listDatasetVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The resource name of the Dataset to list DatasetVersions from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetVersionsPagedResponse)` |   
  
### listDatasetVersions(ListDatasetVersionsRequest request)
    
    
    public final DatasetServiceClient.ListDatasetVersionsPagedResponse listDatasetVersions(ListDatasetVersionsRequest request)

Lists DatasetVersions in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetVersionsRequest request =
           ListDatasetVersionsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DatasetVersion element :
           datasetServiceClient.listDatasetVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetVersionsPagedResponse)` |   
  
### listDatasetVersions(String parent)
    
    
    public final DatasetServiceClient.ListDatasetVersionsPagedResponse listDatasetVersions(String parent)

Lists DatasetVersions in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       for (DatasetVersion element : datasetServiceClient.listDatasetVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset to list DatasetVersions from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetVersionsPagedResponse)` |   
  
### listDatasetVersionsCallable()
    
    
    public final UnaryCallable<ListDatasetVersionsRequest,ListDatasetVersionsResponse> listDatasetVersionsCallable()

Lists DatasetVersions in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetVersionsRequest request =
           ListDatasetVersionsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDatasetVersionsResponse response =
             datasetServiceClient.listDatasetVersionsCallable().call(request);
         for (DatasetVersion element : response.getDatasetVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsRequest),[ListDatasetVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsResponse)>` |   
  
### listDatasetVersionsPagedCallable()
    
    
    public final UnaryCallable<ListDatasetVersionsRequest,DatasetServiceClient.ListDatasetVersionsPagedResponse> listDatasetVersionsPagedCallable()

Lists DatasetVersions in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetVersionsRequest request =
           ListDatasetVersionsRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DatasetVersion> future =
           datasetServiceClient.listDatasetVersionsPagedCallable().futureCall(request);
       // Do something.
       for (DatasetVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsRequest),[ListDatasetVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetVersionsPagedResponse)>` |   
  
### listDatasets(@Nullable LocationName parent)
    
    
    public final DatasetServiceClient.ListDatasetsPagedResponse listDatasets(@Nullable LocationName parent)

Lists Datasets in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Dataset element : datasetServiceClient.listDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The name of the Dataset's parent resource. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetsPagedResponse)` |   
  
### listDatasets(ListDatasetsRequest request)
    
    
    public final DatasetServiceClient.ListDatasetsPagedResponse listDatasets(ListDatasetsRequest request)

Lists Datasets in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Dataset element : datasetServiceClient.listDatasets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetsPagedResponse)` |   
  
### listDatasets(String parent)
    
    
    public final DatasetServiceClient.ListDatasetsPagedResponse listDatasets(String parent)

Lists Datasets in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Dataset element : datasetServiceClient.listDatasets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Dataset's parent resource. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetsPagedResponse)` |   
  
### listDatasetsCallable()
    
    
    public final UnaryCallable<ListDatasetsRequest,ListDatasetsResponse> listDatasetsCallable()

Lists Datasets in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDatasetsResponse response = datasetServiceClient.listDatasetsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsRequest),[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsResponse)>` |   
  
### listDatasetsPagedCallable()
    
    
    public final UnaryCallable<ListDatasetsRequest,DatasetServiceClient.ListDatasetsPagedResponse> listDatasetsPagedCallable()

Lists Datasets in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListDatasetsRequest request =
           ListDatasetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Dataset> future =
           datasetServiceClient.listDatasetsPagedCallable().futureCall(request);
       // Do something.
       for (Dataset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsRequest),[ListDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListDatasetsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DatasetServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : datasetServiceClient.listLocations(request).iterateAll()) {
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
`[DatasetServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = datasetServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DatasetServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           datasetServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListLocationsPagedResponse)>` |   
  
### listSavedQueries(@Nullable DatasetName parent)
    
    
    public final DatasetServiceClient.ListSavedQueriesPagedResponse listSavedQueries(@Nullable DatasetName parent)

Lists SavedQueries in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetName parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]");
       for (SavedQuery element : datasetServiceClient.listSavedQueries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetName`  
Required. The resource name of the Dataset to list SavedQueries from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListSavedQueriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListSavedQueriesPagedResponse)` |   
  
### listSavedQueries(ListSavedQueriesRequest request)
    
    
    public final DatasetServiceClient.ListSavedQueriesPagedResponse listSavedQueries(ListSavedQueriesRequest request)

Lists SavedQueries in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListSavedQueriesRequest request =
           ListSavedQueriesRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (SavedQuery element : datasetServiceClient.listSavedQueries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSavedQueriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListSavedQueriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListSavedQueriesPagedResponse)` |   
  
### listSavedQueries(String parent)
    
    
    public final DatasetServiceClient.ListSavedQueriesPagedResponse listSavedQueries(String parent)

Lists SavedQueries in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String parent = DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString();
       for (SavedQuery element : datasetServiceClient.listSavedQueries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Dataset to list SavedQueries from. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.ListSavedQueriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListSavedQueriesPagedResponse)` |   
  
### listSavedQueriesCallable()
    
    
    public final UnaryCallable<ListSavedQueriesRequest,ListSavedQueriesResponse> listSavedQueriesCallable()

Lists SavedQueries in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListSavedQueriesRequest request =
           ListSavedQueriesRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSavedQueriesResponse response =
             datasetServiceClient.listSavedQueriesCallable().call(request);
         for (SavedQuery element : response.getSavedQueriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSavedQueriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesRequest),[ListSavedQueriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesResponse)>` |   
  
### listSavedQueriesPagedCallable()
    
    
    public final UnaryCallable<ListSavedQueriesRequest,DatasetServiceClient.ListSavedQueriesPagedResponse> listSavedQueriesPagedCallable()

Lists SavedQueries in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       ListSavedQueriesRequest request =
           ListSavedQueriesRequest.newBuilder()
               .setParent(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<SavedQuery> future =
           datasetServiceClient.listSavedQueriesPagedCallable().futureCall(request);
       // Do something.
       for (SavedQuery element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSavedQueriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesRequest),[ListSavedQueriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.ListSavedQueriesPagedResponse)>` |   
  
### restoreDatasetVersionAsync(@Nullable DatasetVersionName name)
    
    
    public final OperationFuture<DatasetVersion,RestoreDatasetVersionOperationMetadata> restoreDatasetVersionAsync(@Nullable DatasetVersionName name)

Restores a dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetVersionName name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]");
       DatasetVersion response = datasetServiceClient.restoreDatasetVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DatasetVersionName`  
Required. The name of the DatasetVersion resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[RestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionOperationMetadata)>` |   
  
### restoreDatasetVersionAsync(RestoreDatasetVersionRequest request)
    
    
    public final OperationFuture<DatasetVersion,RestoreDatasetVersionOperationMetadata> restoreDatasetVersionAsync(RestoreDatasetVersionRequest request)

Restores a dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       RestoreDatasetVersionRequest request =
           RestoreDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       DatasetVersion response = datasetServiceClient.restoreDatasetVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[RestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionOperationMetadata)>` |   
  
### restoreDatasetVersionAsync(String name)
    
    
    public final OperationFuture<DatasetVersion,RestoreDatasetVersionOperationMetadata> restoreDatasetVersionAsync(String name)

Restores a dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       String name =
           DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
               .toString();
       DatasetVersion response = datasetServiceClient.restoreDatasetVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DatasetVersion resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[RestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionOperationMetadata)>` |   
  
### restoreDatasetVersionCallable()
    
    
    public final UnaryCallable<RestoreDatasetVersionRequest,Operation> restoreDatasetVersionCallable()

Restores a dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       RestoreDatasetVersionRequest request =
           RestoreDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           datasetServiceClient.restoreDatasetVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreDatasetVersionOperationCallable()
    
    
    public final OperationCallable<RestoreDatasetVersionRequest,DatasetVersion,RestoreDatasetVersionOperationMetadata> restoreDatasetVersionOperationCallable()

Restores a dataset version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       RestoreDatasetVersionRequest request =
           RestoreDatasetVersionRequest.newBuilder()
               .setName(
                   DatasetVersionName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[DATASET_VERSION]")
                       .toString())
               .build();
       OperationFuture<DatasetVersion, RestoreDatasetVersionOperationMetadata> future =
           datasetServiceClient.restoreDatasetVersionOperationCallable().futureCall(request);
       // Do something.
       DatasetVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionRequest),[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion),[RestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionOperationMetadata)>` |   
  
### searchDataItems(SearchDataItemsRequest request)
    
    
    public final DatasetServiceClient.SearchDataItemsPagedResponse searchDataItems(SearchDataItemsRequest request)

Searches DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SearchDataItemsRequest request =
           SearchDataItemsRequest.newBuilder()
               .setDataset(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setSavedQuery(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .setDataLabelingJob("dataLabelingJob951814757")
               .setDataItemFilter("dataItemFilter1487804341")
               .setAnnotationsFilter("annotationsFilter-583841860")
               .addAllAnnotationFilters(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setAnnotationsLimit(134561504)
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .build();
       for (DataItemView element : datasetServiceClient.searchDataItems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetServiceClient.SearchDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.SearchDataItemsPagedResponse)` |   
  
### searchDataItemsCallable()
    
    
    public final UnaryCallable<SearchDataItemsRequest,SearchDataItemsResponse> searchDataItemsCallable()

Searches DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SearchDataItemsRequest request =
           SearchDataItemsRequest.newBuilder()
               .setDataset(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setSavedQuery(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .setDataLabelingJob("dataLabelingJob951814757")
               .setDataItemFilter("dataItemFilter1487804341")
               .setAnnotationsFilter("annotationsFilter-583841860")
               .addAllAnnotationFilters(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setAnnotationsLimit(134561504)
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         SearchDataItemsResponse response =
             datasetServiceClient.searchDataItemsCallable().call(request);
         for (DataItemView element : response.getDataItemViewsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsRequest),[SearchDataItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsResponse)>` |   
  
### searchDataItemsPagedCallable()
    
    
    public final UnaryCallable<SearchDataItemsRequest,DatasetServiceClient.SearchDataItemsPagedResponse> searchDataItemsPagedCallable()

Searches DataItems in a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SearchDataItemsRequest request =
           SearchDataItemsRequest.newBuilder()
               .setDataset(DatasetName.of("[PROJECT]", "[LOCATION]", "[DATASET]").toString())
               .setSavedQuery(
                   SavedQueryName.of("[PROJECT]", "[LOCATION]", "[DATASET]", "[SAVED_QUERY]")
                       .toString())
               .setDataLabelingJob("dataLabelingJob951814757")
               .setDataItemFilter("dataItemFilter1487804341")
               .setAnnotationsFilter("annotationsFilter-583841860")
               .addAllAnnotationFilters(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setAnnotationsLimit(134561504)
               .setPageSize(883849137)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataItemView> future =
           datasetServiceClient.searchDataItemsPagedCallable().futureCall(request);
       // Do something.
       for (DataItemView element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsRequest),[SearchDataItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.SearchDataItemsPagedResponse)>` |   
  
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = datasetServiceClient.setIamPolicy(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = datasetServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = datasetServiceClient.testIamPermissions(request);
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
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           datasetServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDataset(Dataset dataset, FieldMask updateMask)
    
    
    public final Dataset updateDataset(Dataset dataset, FieldMask updateMask)

Updates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       Dataset dataset = Dataset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Dataset response = datasetServiceClient.updateDataset(dataset, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataset` | `[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)`  
Required. The Dataset which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see google.protobuf.FieldMask. Updatable fields: * `display_name` * `description` * `labels`  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)` |   
  
### updateDataset(UpdateDatasetRequest request)
    
    
    public final Dataset updateDataset(UpdateDatasetRequest request)

Updates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       UpdateDatasetRequest request =
           UpdateDatasetRequest.newBuilder()
               .setDataset(Dataset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Dataset response = datasetServiceClient.updateDataset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)` |   
  
### updateDatasetCallable()
    
    
    public final UnaryCallable<UpdateDatasetRequest,Dataset> updateDatasetCallable()

Updates a Dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       UpdateDatasetRequest request =
           UpdateDatasetRequest.newBuilder()
               .setDataset(Dataset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Dataset> future = datasetServiceClient.updateDatasetCallable().futureCall(request);
       // Do something.
       Dataset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetRequest),[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)>` |   
  
### updateDatasetVersion(DatasetVersion datasetVersion, FieldMask updateMask)
    
    
    public final DatasetVersion updateDatasetVersion(DatasetVersion datasetVersion, FieldMask updateMask)

Updates a DatasetVersion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       DatasetVersion datasetVersion = DatasetVersion.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DatasetVersion response =
           datasetServiceClient.updateDatasetVersion(datasetVersion, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`datasetVersion` | `[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)`  
Required. The DatasetVersion which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see google.protobuf.FieldMask. Updatable fields: * `display_name`  
**Returns**  
---  
**Type** | **Description**  
`[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)` |   
  
### updateDatasetVersion(UpdateDatasetVersionRequest request)
    
    
    public final DatasetVersion updateDatasetVersion(UpdateDatasetVersionRequest request)

Updates a DatasetVersion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       UpdateDatasetVersionRequest request =
           UpdateDatasetVersionRequest.newBuilder()
               .setDatasetVersion(DatasetVersion.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DatasetVersion response = datasetServiceClient.updateDatasetVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)` |   
  
### updateDatasetVersionCallable()
    
    
    public final UnaryCallable<UpdateDatasetVersionRequest,DatasetVersion> updateDatasetVersionCallable()

Updates a DatasetVersion.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatasetServiceClient datasetServiceClient = DatasetServiceClient.create()) {
       UpdateDatasetVersionRequest request =
           UpdateDatasetVersionRequest.newBuilder()
               .setDatasetVersion(DatasetVersion.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DatasetVersion> future =
           datasetServiceClient.updateDatasetVersionCallable().futureCall(request);
       // Do something.
       DatasetVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetVersionRequest),[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
