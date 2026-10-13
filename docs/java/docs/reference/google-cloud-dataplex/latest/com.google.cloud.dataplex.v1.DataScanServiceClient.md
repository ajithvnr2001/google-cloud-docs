---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient
title: Class DataScanServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:32:09.917722+00:00
---

# Class DataScanServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataScanServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/DataScanServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: DataScanService manages DataScan resources which can be configured to run various types of data scanning workload and generate enriched metadata (e.g. Data Profile, Data Quality) for the data source.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanName name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]");
       DataScan response = dataScanServiceClient.getDataScan(name);
     }
     

Note: close() needs to be called on the DataScanServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataScan |  Creates a DataScan resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataScanAsync(CreateDataScanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataScanAsync(LocationName parent, DataScan dataScan, String dataScanId) 
  * createDataScanAsync(String parent, DataScan dataScan, String dataScanId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataScanOperationCallable() 
  * createDataScanCallable() 

  
UpdateDataScan |  Updates a DataScan resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataScanAsync(UpdateDataScanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataScanAsync(DataScan dataScan, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataScanOperationCallable() 
  * updateDataScanCallable() 

  
DeleteDataScan |  Deletes a DataScan resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataScanAsync(DeleteDataScanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataScanAsync(DataScanName name) 
  * deleteDataScanAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataScanOperationCallable() 
  * deleteDataScanCallable() 

  
GetDataScan |  Gets a DataScan resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataScan(GetDataScanRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataScan(DataScanName name) 
  * getDataScan(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataScanCallable() 

  
ListDataScans |  Lists DataScans. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataScans(ListDataScansRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataScans(LocationName parent) 
  * listDataScans(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataScansPagedCallable() 
  * listDataScansCallable() 

  
RunDataScan |  Runs an on-demand execution of a DataScan |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runDataScan(RunDataScanRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * runDataScan(DataScanName name) 
  * runDataScan(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runDataScanCallable() 

  
GetDataScanJob |  Gets a DataScanJob resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataScanJob(GetDataScanJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataScanJob(DataScanJobName name) 
  * getDataScanJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataScanJobCallable() 

  
ListDataScanJobs |  Lists DataScanJobs under the given DataScan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataScanJobs(ListDataScanJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataScanJobs(DataScanName parent) 
  * listDataScanJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataScanJobsPagedCallable() 
  * listDataScanJobsCallable() 

  
CancelDataScanJob |  Cancels a running/pending DataScan job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelDataScanJob(CancelDataScanJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelDataScanJob(DataScanJobName name) 
  * cancelDataScanJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelDataScanJobCallable() 

  
GenerateDataQualityRules |  Generates recommended data quality rules based on the results of a data profiling scan.  Use the recommendations to build rules for a data quality scan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateDataQualityRules(GenerateDataQualityRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateDataQualityRules(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateDataQualityRulesCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of DataScanServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataScanServiceSettings dataScanServiceSettings =
         DataScanServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataScanServiceClient dataScanServiceClient =
         DataScanServiceClient.create(dataScanServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataScanServiceSettings dataScanServiceSettings =
         DataScanServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataScanServiceClient dataScanServiceClient =
         DataScanServiceClient.create(dataScanServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataScanServiceSettings dataScanServiceSettings =
         DataScanServiceSettings.newHttpJsonBuilder().build();
     DataScanServiceClient dataScanServiceClient =
         DataScanServiceClient.create(dataScanServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataScanServiceClient

## Static Methods 

### create()
    
    
    public static final DataScanServiceClient create()

Constructs an instance of DataScanServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataScanServiceSettings settings)
    
    
    public static final DataScanServiceClient create(DataScanServiceSettings settings)

Constructs an instance of DataScanServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataScanServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataScanServiceStub stub)
    
    
    public static final DataScanServiceClient create(DataScanServiceStub stub)

Constructs an instance of DataScanServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataScanServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataScanServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataScanServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient)` |   
  
## Constructors 

### DataScanServiceClient(DataScanServiceSettings settings)
    
    
    protected DataScanServiceClient(DataScanServiceSettings settings)

Constructs an instance of DataScanServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataScanServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceSettings)`  
  
  
### DataScanServiceClient(DataScanServiceStub stub)
    
    
    protected DataScanServiceClient(DataScanServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataScanServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataScanServiceStub)`  
  
  
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
  
### cancelDataScanJob(@Nullable DataScanJobName name)
    
    
    public final CancelDataScanJobResponse cancelDataScanJob(@Nullable DataScanJobName name)

Cancels a running/pending DataScan job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanJobName name = DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
       CancelDataScanJobResponse response = dataScanServiceClient.cancelDataScanJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanJobName`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobResponse)` |   
  
### cancelDataScanJob(CancelDataScanJobRequest request)
    
    
    public final CancelDataScanJobResponse cancelDataScanJob(CancelDataScanJobRequest request)

Cancels a running/pending DataScan job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       CancelDataScanJobRequest request =
           CancelDataScanJobRequest.newBuilder()
               .setName(
                   DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString())
               .build();
       CancelDataScanJobResponse response = dataScanServiceClient.cancelDataScanJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelDataScanJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobResponse)` |   
  
### cancelDataScanJob(String name)
    
    
    public final CancelDataScanJobResponse cancelDataScanJob(String name)

Cancels a running/pending DataScan job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString();
       CancelDataScanJobResponse response = dataScanServiceClient.cancelDataScanJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataScanJob: `projects/{project_id_or_number}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project_id_or_number` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CancelDataScanJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobResponse)` |   
  
### cancelDataScanJobCallable()
    
    
    public final UnaryCallable<CancelDataScanJobRequest,CancelDataScanJobResponse> cancelDataScanJobCallable()

Cancels a running/pending DataScan job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       CancelDataScanJobRequest request =
           CancelDataScanJobRequest.newBuilder()
               .setName(
                   DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString())
               .build();
       ApiFuture<CancelDataScanJobResponse> future =
           dataScanServiceClient.cancelDataScanJobCallable().futureCall(request);
       // Do something.
       CancelDataScanJobResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelDataScanJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobRequest),[CancelDataScanJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelDataScanJobResponse)>` |   
  
### close()
    
    
    public final void close()

### createDataScanAsync(@Nullable LocationName parent, DataScan dataScan, String dataScanId)
    
    
    public final OperationFuture<DataScan,OperationMetadata> createDataScanAsync(@Nullable LocationName parent, DataScan dataScan, String dataScanId)

Creates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataScan dataScan = DataScan.newBuilder().build();
       String dataScanId = "dataScanId1260787906";
       DataScan response =
           dataScanServiceClient.createDataScanAsync(parent, dataScan, dataScanId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-". 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the customer project / location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataScanAsync(CreateDataScanRequest request)
    
    
    public final OperationFuture<DataScan,OperationMetadata> createDataScanAsync(CreateDataScanRequest request)

Creates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       CreateDataScanRequest request =
           CreateDataScanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataScan(DataScan.newBuilder().build())
               .setDataScanId("dataScanId1260787906")
               .setValidateOnly(true)
               .build();
       DataScan response = dataScanServiceClient.createDataScanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataScanAsync(String parent, DataScan dataScan, String dataScanId)
    
    
    public final OperationFuture<DataScan,OperationMetadata> createDataScanAsync(String parent, DataScan dataScan, String dataScanId)

Creates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataScan dataScan = DataScan.newBuilder().build();
       String dataScanId = "dataScanId1260787906";
       DataScan response =
           dataScanServiceClient.createDataScanAsync(parent, dataScan, dataScanId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
`dataScan` | `[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)`  
Required. DataScan resource.  
`dataScanId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. DataScan identifier. If not provided, a unique ID will be generated with the prefix "data-scan-". 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the customer project / location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataScanCallable()
    
    
    public final UnaryCallable<CreateDataScanRequest,Operation> createDataScanCallable()

Creates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       CreateDataScanRequest request =
           CreateDataScanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataScan(DataScan.newBuilder().build())
               .setDataScanId("dataScanId1260787906")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataScanServiceClient.createDataScanCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataScanOperationCallable()
    
    
    public final OperationCallable<CreateDataScanRequest,DataScan,OperationMetadata> createDataScanOperationCallable()

Creates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       CreateDataScanRequest request =
           CreateDataScanRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataScan(DataScan.newBuilder().build())
               .setDataScanId("dataScanId1260787906")
               .setValidateOnly(true)
               .build();
       OperationFuture<DataScan, OperationMetadata> future =
           dataScanServiceClient.createDataScanOperationCallable().futureCall(request);
       // Do something.
       DataScan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataScanRequest),[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataScanAsync(@Nullable DataScanName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataScanAsync(@Nullable DataScanName name)

Deletes a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanName name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]");
       dataScanServiceClient.deleteDataScanAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanName`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataScanAsync(DeleteDataScanRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataScanAsync(DeleteDataScanRequest request)

Deletes a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DeleteDataScanRequest request =
           DeleteDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setForce(true)
               .build();
       dataScanServiceClient.deleteDataScanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataScanAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataScanAsync(String name)

Deletes a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString();
       dataScanServiceClient.deleteDataScanAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataScanCallable()
    
    
    public final UnaryCallable<DeleteDataScanRequest,Operation> deleteDataScanCallable()

Deletes a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DeleteDataScanRequest request =
           DeleteDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           dataScanServiceClient.deleteDataScanCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataScanOperationCallable()
    
    
    public final OperationCallable<DeleteDataScanRequest,Empty,OperationMetadata> deleteDataScanOperationCallable()

Deletes a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DeleteDataScanRequest request =
           DeleteDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataScanServiceClient.deleteDataScanOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataScanRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### generateDataQualityRules(GenerateDataQualityRulesRequest request)
    
    
    public final GenerateDataQualityRulesResponse generateDataQualityRules(GenerateDataQualityRulesRequest request)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GenerateDataQualityRulesRequest request =
           GenerateDataQualityRulesRequest.newBuilder().setName("name3373707").build();
       GenerateDataQualityRulesResponse response =
           dataScanServiceClient.generateDataQualityRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateDataQualityRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GenerateDataQualityRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GenerateDataQualityRulesResponse)` |   
  
### generateDataQualityRules(String name)
    
    
    public final GenerateDataQualityRulesResponse generateDataQualityRules(String name)

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = "name3373707";
       GenerateDataQualityRulesResponse response =
           dataScanServiceClient.generateDataQualityRules(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name must be one of the following: 

  * The name of a data scan with at least one successful, completed data profiling job 
  * The name of a successful, completed data profiling job (a data scan job where the job type is data profiling) 

  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GenerateDataQualityRulesResponse)` |   
  
### generateDataQualityRulesCallable()
    
    
    public final UnaryCallable<GenerateDataQualityRulesRequest,GenerateDataQualityRulesResponse> generateDataQualityRulesCallable()

Generates recommended data quality rules based on the results of a data profiling scan.

Use the recommendations to build rules for a data quality scan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GenerateDataQualityRulesRequest request =
           GenerateDataQualityRulesRequest.newBuilder().setName("name3373707").build();
       ApiFuture<GenerateDataQualityRulesResponse> future =
           dataScanServiceClient.generateDataQualityRulesCallable().futureCall(request);
       // Do something.
       GenerateDataQualityRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateDataQualityRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GenerateDataQualityRulesRequest),[GenerateDataQualityRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GenerateDataQualityRulesResponse)>` |   
  
### getDataScan(@Nullable DataScanName name)
    
    
    public final DataScan getDataScan(@Nullable DataScanName name)

Gets a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanName name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]");
       DataScan response = dataScanServiceClient.getDataScan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanName`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)` |   
  
### getDataScan(GetDataScanRequest request)
    
    
    public final DataScan getDataScan(GetDataScanRequest request)

Gets a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetDataScanRequest request =
           GetDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .build();
       DataScan response = dataScanServiceClient.getDataScan(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)` |   
  
### getDataScan(String name)
    
    
    public final DataScan getDataScan(String name)

Gets a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString();
       DataScan response = dataScanServiceClient.getDataScan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)` |   
  
### getDataScanCallable()
    
    
    public final UnaryCallable<GetDataScanRequest,DataScan> getDataScanCallable()

Gets a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetDataScanRequest request =
           GetDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .build();
       ApiFuture<DataScan> future = dataScanServiceClient.getDataScanCallable().futureCall(request);
       // Do something.
       DataScan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanRequest),[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)>` |   
  
### getDataScanJob(@Nullable DataScanJobName name)
    
    
    public final DataScanJob getDataScanJob(@Nullable DataScanJobName name)

Gets a DataScanJob resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanJobName name = DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]");
       DataScanJob response = dataScanServiceClient.getDataScanJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanJobName`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob)` |   
  
### getDataScanJob(GetDataScanJobRequest request)
    
    
    public final DataScanJob getDataScanJob(GetDataScanJobRequest request)

Gets a DataScanJob resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetDataScanJobRequest request =
           GetDataScanJobRequest.newBuilder()
               .setName(
                   DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString())
               .build();
       DataScanJob response = dataScanServiceClient.getDataScanJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataScanJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob)` |   
  
### getDataScanJob(String name)
    
    
    public final DataScanJob getDataScanJob(String name)

Gets a DataScanJob resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString();
       DataScanJob response = dataScanServiceClient.getDataScanJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataScanJob: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}/jobs/{data_scan_job_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob)` |   
  
### getDataScanJobCallable()
    
    
    public final UnaryCallable<GetDataScanJobRequest,DataScanJob> getDataScanJobCallable()

Gets a DataScanJob resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetDataScanJobRequest request =
           GetDataScanJobRequest.newBuilder()
               .setName(
                   DataScanJobName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]", "[JOB]").toString())
               .build();
       ApiFuture<DataScanJob> future =
           dataScanServiceClient.getDataScanJobCallable().futureCall(request);
       // Do something.
       DataScanJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataScanJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataScanJobRequest),[DataScanJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanJob)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataScanServiceClient.getIamPolicy(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataScanServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataScanServiceClient.getLocation(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = dataScanServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DataScanServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanServiceSettings` |   
  
### getStub()
    
    
    public DataScanServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataScanServiceStub)` |   
  
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
  
### listDataScanJobs(@Nullable DataScanName parent)
    
    
    public final DataScanServiceClient.ListDataScanJobsPagedResponse listDataScanJobs(@Nullable DataScanName parent)

Lists DataScanJobs under the given DataScan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanName parent = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]");
       for (DataScanJob element : dataScanServiceClient.listDataScanJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanName`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScanJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScanJobsPagedResponse)` |   
  
### listDataScanJobs(ListDataScanJobsRequest request)
    
    
    public final DataScanServiceClient.ListDataScanJobsPagedResponse listDataScanJobs(ListDataScanJobsRequest request)

Lists DataScanJobs under the given DataScan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScanJobsRequest request =
           ListDataScanJobsRequest.newBuilder()
               .setParent(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DataScanJob element : dataScanServiceClient.listDataScanJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScanJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScanJobsPagedResponse)` |   
  
### listDataScanJobs(String parent)
    
    
    public final DataScanServiceClient.ListDataScanJobsPagedResponse listDataScanJobs(String parent)

Lists DataScanJobs under the given DataScan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String parent = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString();
       for (DataScanJob element : dataScanServiceClient.listDataScanJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent environment: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScanJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScanJobsPagedResponse)` |   
  
### listDataScanJobsCallable()
    
    
    public final UnaryCallable<ListDataScanJobsRequest,ListDataScanJobsResponse> listDataScanJobsCallable()

Lists DataScanJobs under the given DataScan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScanJobsRequest request =
           ListDataScanJobsRequest.newBuilder()
               .setParent(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDataScanJobsResponse response =
             dataScanServiceClient.listDataScanJobsCallable().call(request);
         for (DataScanJob element : response.getDataScanJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest),[ListDataScanJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsResponse)>` |   
  
### listDataScanJobsPagedCallable()
    
    
    public final UnaryCallable<ListDataScanJobsRequest,DataScanServiceClient.ListDataScanJobsPagedResponse> listDataScanJobsPagedCallable()

Lists DataScanJobs under the given DataScan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScanJobsRequest request =
           ListDataScanJobsRequest.newBuilder()
               .setParent(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DataScanJob> future =
           dataScanServiceClient.listDataScanJobsPagedCallable().futureCall(request);
       // Do something.
       for (DataScanJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataScanJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScanJobsRequest),[ListDataScanJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScanJobsPagedResponse)>` |   
  
### listDataScans(@Nullable LocationName parent)
    
    
    public final DataScanServiceClient.ListDataScansPagedResponse listDataScans(@Nullable LocationName parent)

Lists DataScans.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataScan element : dataScanServiceClient.listDataScans(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScansPagedResponse)` |   
  
### listDataScans(ListDataScansRequest request)
    
    
    public final DataScanServiceClient.ListDataScansPagedResponse listDataScans(ListDataScansRequest request)

Lists DataScans.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScansRequest request =
           ListDataScansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataScan element : dataScanServiceClient.listDataScans(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataScansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScansRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScansPagedResponse)` |   
  
### listDataScans(String parent)
    
    
    public final DataScanServiceClient.ListDataScansPagedResponse listDataScans(String parent)

Lists DataScans.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataScan element : dataScanServiceClient.listDataScans(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location: `projects/{project}/locations/{location_id}` where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataScanServiceClient.ListDataScansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScansPagedResponse)` |   
  
### listDataScansCallable()
    
    
    public final UnaryCallable<ListDataScansRequest,ListDataScansResponse> listDataScansCallable()

Lists DataScans.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScansRequest request =
           ListDataScansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataScansResponse response =
             dataScanServiceClient.listDataScansCallable().call(request);
         for (DataScan element : response.getDataScansList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataScansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScansRequest),[ListDataScansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScansResponse)>` |   
  
### listDataScansPagedCallable()
    
    
    public final UnaryCallable<ListDataScansRequest,DataScanServiceClient.ListDataScansPagedResponse> listDataScansPagedCallable()

Lists DataScans.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListDataScansRequest request =
           ListDataScansRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataScan> future =
           dataScanServiceClient.listDataScansPagedCallable().futureCall(request);
       // Do something.
       for (DataScan element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataScansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataScansRequest),[ListDataScansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListDataScansPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataScanServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataScanServiceClient.listLocations(request).iterateAll()) {
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
`[DataScanServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataScanServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataScanServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataScanServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScanServiceClient.ListLocationsPagedResponse)>` |   
  
### runDataScan(@Nullable DataScanName name)
    
    
    public final RunDataScanResponse runDataScan(@Nullable DataScanName name)

Runs an on-demand execution of a DataScan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScanName name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]");
       RunDataScanResponse response = dataScanServiceClient.runDataScan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataScanName`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse)` |   
  
### runDataScan(RunDataScanRequest request)
    
    
    public final RunDataScanResponse runDataScan(RunDataScanRequest request)

Runs an on-demand execution of a DataScan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       RunDataScanRequest request =
           RunDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .build();
       RunDataScanResponse response = dataScanServiceClient.runDataScan(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse)` |   
  
### runDataScan(String name)
    
    
    public final RunDataScanResponse runDataScan(String name)

Runs an on-demand execution of a DataScan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       String name = DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString();
       RunDataScanResponse response = dataScanServiceClient.runDataScan(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataScan: `projects/{project}/locations/{location_id}/dataScans/{data_scan_id}`. where `project` refers to a *project_id* or *project_number* and `location_id` refers to a Google Cloud region. Only **OnDemand** data scans are allowed.  
**Returns**  
---  
**Type** | **Description**  
`[RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse)` |   
  
### runDataScanCallable()
    
    
    public final UnaryCallable<RunDataScanRequest,RunDataScanResponse> runDataScanCallable()

Runs an on-demand execution of a DataScan

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       RunDataScanRequest request =
           RunDataScanRequest.newBuilder()
               .setName(DataScanName.of("[PROJECT]", "[LOCATION]", "[DATASCAN]").toString())
               .build();
       ApiFuture<RunDataScanResponse> future =
           dataScanServiceClient.runDataScanCallable().futureCall(request);
       // Do something.
       RunDataScanResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanRequest),[RunDataScanResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunDataScanResponse)>` |   
  
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataScanServiceClient.setIamPolicy(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataScanServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataScanServiceClient.testIamPermissions(request);
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
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataScanServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDataScanAsync(DataScan dataScan, FieldMask updateMask)
    
    
    public final OperationFuture<DataScan,OperationMetadata> updateDataScanAsync(DataScan dataScan, FieldMask updateMask)

Updates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       DataScan dataScan = DataScan.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataScan response = dataScanServiceClient.updateDataScanAsync(dataScan, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataScan` | `[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan)`  
Required. DataScan resource to be updated. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataScanAsync(UpdateDataScanRequest request)
    
    
    public final OperationFuture<DataScan,OperationMetadata> updateDataScanAsync(UpdateDataScanRequest request)

Updates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       UpdateDataScanRequest request =
           UpdateDataScanRequest.newBuilder()
               .setDataScan(DataScan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataScan response = dataScanServiceClient.updateDataScanAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataScanCallable()
    
    
    public final UnaryCallable<UpdateDataScanRequest,Operation> updateDataScanCallable()

Updates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       UpdateDataScanRequest request =
           UpdateDataScanRequest.newBuilder()
               .setDataScan(DataScan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataScanServiceClient.updateDataScanCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataScanOperationCallable()
    
    
    public final OperationCallable<UpdateDataScanRequest,DataScan,OperationMetadata> updateDataScanOperationCallable()

Updates a DataScan resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataScanServiceClient dataScanServiceClient = DataScanServiceClient.create()) {
       UpdateDataScanRequest request =
           UpdateDataScanRequest.newBuilder()
               .setDataScan(DataScan.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataScan, OperationMetadata> future =
           dataScanServiceClient.updateDataScanOperationCallable().futureCall(request);
       // Do something.
       DataScan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataScanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataScanRequest),[DataScan](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataScan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
