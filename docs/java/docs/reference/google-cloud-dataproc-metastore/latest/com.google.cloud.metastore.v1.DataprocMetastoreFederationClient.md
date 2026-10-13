---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient
title: Class DataprocMetastoreFederationClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:34.641662+00:00
---

# Class DataprocMetastoreFederationClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataprocMetastoreFederationClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.4  2.3.0  2.2.0  2.1.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataproc-metastore/google-cloud-dataproc-metastore/src/main/java/com/google/cloud/metastore/v1/DataprocMetastoreFederationClient.java)| [Product Reference](https://cloud.google.com/dataproc-metastore/docs)| [REST Documentation](https://cloud.google.com/dataproc-metastore/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataproc-metastore/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:

  * The service works with a collection of Google Cloud projects. 
  * Each project has a collection of available locations. 
  * Each location has a collection of federations. 
  * Dataproc Metastore Federations are resources with names of the form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`. 



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       FederationName name = FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]");
       Federation response = dataprocMetastoreFederationClient.getFederation(name);
     }
     

Note: close() needs to be called on the DataprocMetastoreFederationClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListFederations |  Lists federations in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFederations(ListFederationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFederations(LocationName parent) 
  * listFederations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFederationsPagedCallable() 
  * listFederationsCallable() 

  
GetFederation |  Gets the details of a single federation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFederation(GetFederationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFederation(FederationName name) 
  * getFederation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFederationCallable() 

  
CreateFederation |  Creates a metastore federation in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFederationAsync(CreateFederationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFederationAsync(LocationName parent, Federation federation, String federationId) 
  * createFederationAsync(String parent, Federation federation, String federationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFederationOperationCallable() 
  * createFederationCallable() 

  
UpdateFederation |  Updates the fields of a federation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFederationAsync(UpdateFederationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFederationAsync(Federation federation, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFederationOperationCallable() 
  * updateFederationCallable() 

  
DeleteFederation |  Deletes a single federation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFederationAsync(DeleteFederationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFederationAsync(FederationName name) 
  * deleteFederationAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFederationOperationCallable() 
  * deleteFederationCallable() 

  
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

This class can be customized by passing in a custom instance of DataprocMetastoreFederationSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreFederationSettings dataprocMetastoreFederationSettings =
         DataprocMetastoreFederationSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create(dataprocMetastoreFederationSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreFederationSettings dataprocMetastoreFederationSettings =
         DataprocMetastoreFederationSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create(dataprocMetastoreFederationSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreFederationSettings dataprocMetastoreFederationSettings =
         DataprocMetastoreFederationSettings.newHttpJsonBuilder().build();
     DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create(dataprocMetastoreFederationSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataprocMetastoreFederationClient

## Static Methods 

### create()
    
    
    public static final DataprocMetastoreFederationClient create()

Constructs an instance of DataprocMetastoreFederationClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataprocMetastoreFederationSettings settings)
    
    
    public static final DataprocMetastoreFederationClient create(DataprocMetastoreFederationSettings settings)

Constructs an instance of DataprocMetastoreFederationClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataprocMetastoreFederationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataprocMetastoreFederationStub stub)
    
    
    public static final DataprocMetastoreFederationClient create(DataprocMetastoreFederationStub stub)

Constructs an instance of DataprocMetastoreFederationClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataprocMetastoreFederationSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataprocMetastoreFederationStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreFederationStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient)` |   
  
## Constructors 

### DataprocMetastoreFederationClient(DataprocMetastoreFederationSettings settings)
    
    
    protected DataprocMetastoreFederationClient(DataprocMetastoreFederationSettings settings)

Constructs an instance of DataprocMetastoreFederationClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataprocMetastoreFederationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationSettings)`  
  
  
### DataprocMetastoreFederationClient(DataprocMetastoreFederationStub stub)
    
    
    protected DataprocMetastoreFederationClient(DataprocMetastoreFederationStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataprocMetastoreFederationStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreFederationStub)`  
  
  
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

### createFederationAsync(@Nullable LocationName parent, Federation federation, String federationId)
    
    
    public final OperationFuture<Federation,OperationMetadata> createFederationAsync(@Nullable LocationName parent, Federation federation, String federationId)

Creates a metastore federation in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Federation federation = Federation.newBuilder().build();
       String federationId = "federationId-735921218";
       Federation response =
           dataprocMetastoreFederationClient
               .createFederationAsync(parent, federation, federationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.LocationName`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createFederationAsync(CreateFederationRequest request)
    
    
    public final OperationFuture<Federation,OperationMetadata> createFederationAsync(CreateFederationRequest request)

Creates a metastore federation in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       CreateFederationRequest request =
           CreateFederationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFederationId("federationId-735921218")
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Federation response = dataprocMetastoreFederationClient.createFederationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateFederationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createFederationAsync(String parent, Federation federation, String federationId)
    
    
    public final OperationFuture<Federation,OperationMetadata> createFederationAsync(String parent, Federation federation, String federationId)

Creates a metastore federation in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Federation federation = Federation.newBuilder().build();
       String federationId = "federationId-735921218";
       Federation response =
           dataprocMetastoreFederationClient
               .createFederationAsync(parent, federation, federationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the location in which to create a federation service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`federation` | `[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)`  
Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field.  
`federationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createFederationCallable()
    
    
    public final UnaryCallable<CreateFederationRequest,Operation> createFederationCallable()

Creates a metastore federation in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       CreateFederationRequest request =
           CreateFederationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFederationId("federationId-735921218")
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreFederationClient.createFederationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateFederationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFederationOperationCallable()
    
    
    public final OperationCallable<CreateFederationRequest,Federation,OperationMetadata> createFederationOperationCallable()

Creates a metastore federation in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       CreateFederationRequest request =
           CreateFederationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFederationId("federationId-735921218")
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Federation, OperationMetadata> future =
           dataprocMetastoreFederationClient.createFederationOperationCallable().futureCall(request);
       // Do something.
       Federation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateFederationRequest),[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteFederationAsync(@Nullable FederationName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFederationAsync(@Nullable FederationName name)

Deletes a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       FederationName name = FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]");
       dataprocMetastoreFederationClient.deleteFederationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.FederationName`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteFederationAsync(DeleteFederationRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFederationAsync(DeleteFederationRequest request)

Deletes a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       DeleteFederationRequest request =
           DeleteFederationRequest.newBuilder()
               .setName(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .setRequestId("requestId693933066")
               .build();
       dataprocMetastoreFederationClient.deleteFederationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteFederationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteFederationAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFederationAsync(String name)

Deletes a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       String name = FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString();
       dataprocMetastoreFederationClient.deleteFederationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteFederationCallable()
    
    
    public final UnaryCallable<DeleteFederationRequest,Operation> deleteFederationCallable()

Deletes a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       DeleteFederationRequest request =
           DeleteFederationRequest.newBuilder()
               .setName(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreFederationClient.deleteFederationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteFederationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFederationOperationCallable()
    
    
    public final OperationCallable<DeleteFederationRequest,Empty,OperationMetadata> deleteFederationOperationCallable()

Deletes a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       DeleteFederationRequest request =
           DeleteFederationRequest.newBuilder()
               .setName(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataprocMetastoreFederationClient.deleteFederationOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteFederationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### getFederation(@Nullable FederationName name)
    
    
    public final Federation getFederation(@Nullable FederationName name)

Gets the details of a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       FederationName name = FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]");
       Federation response = dataprocMetastoreFederationClient.getFederation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.FederationName`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)` |   
  
### getFederation(GetFederationRequest request)
    
    
    public final Federation getFederation(GetFederationRequest request)

Gets the details of a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetFederationRequest request =
           GetFederationRequest.newBuilder()
               .setName(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .build();
       Federation response = dataprocMetastoreFederationClient.getFederation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetFederationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)` |   
  
### getFederation(String name)
    
    
    public final Federation getFederation(String name)

Gets the details of a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       String name = FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString();
       Federation response = dataprocMetastoreFederationClient.getFederation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore federation to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)` |   
  
### getFederationCallable()
    
    
    public final UnaryCallable<GetFederationRequest,Federation> getFederationCallable()

Gets the details of a single federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetFederationRequest request =
           GetFederationRequest.newBuilder()
               .setName(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .build();
       ApiFuture<Federation> future =
           dataprocMetastoreFederationClient.getFederationCallable().futureCall(request);
       // Do something.
       Federation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetFederationRequest),[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)>` |   
  
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataprocMetastoreFederationClient.getIamPolicy(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataprocMetastoreFederationClient.getIamPolicyCallable().futureCall(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataprocMetastoreFederationClient.getLocation(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataprocMetastoreFederationClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DataprocMetastoreFederationSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.DataprocMetastoreFederationSettings` |   
  
### getStub()
    
    
    public DataprocMetastoreFederationStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreFederationStub)` |   
  
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
  
### listFederations(@Nullable LocationName parent)
    
    
    public final DataprocMetastoreFederationClient.ListFederationsPagedResponse listFederations(@Nullable LocationName parent)

Lists federations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Federation element :
           dataprocMetastoreFederationClient.listFederations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.LocationName`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient.ListFederationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListFederationsPagedResponse)` |   
  
### listFederations(ListFederationsRequest request)
    
    
    public final DataprocMetastoreFederationClient.ListFederationsPagedResponse listFederations(ListFederationsRequest request)

Lists federations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListFederationsRequest request =
           ListFederationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Federation element :
           dataprocMetastoreFederationClient.listFederations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFederationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListFederationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient.ListFederationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListFederationsPagedResponse)` |   
  
### listFederations(String parent)
    
    
    public final DataprocMetastoreFederationClient.ListFederationsPagedResponse listFederations(String parent)

Lists federations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Federation element :
           dataprocMetastoreFederationClient.listFederations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreFederationClient.ListFederationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListFederationsPagedResponse)` |   
  
### listFederationsCallable()
    
    
    public final UnaryCallable<ListFederationsRequest,ListFederationsResponse> listFederationsCallable()

Lists federations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListFederationsRequest request =
           ListFederationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFederationsResponse response =
             dataprocMetastoreFederationClient.listFederationsCallable().call(request);
         for (Federation element : response.getFederationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFederationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListFederationsRequest),[ListFederationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListFederationsResponse)>` |   
  
### listFederationsPagedCallable()
    
    
    public final UnaryCallable<ListFederationsRequest,DataprocMetastoreFederationClient.ListFederationsPagedResponse> listFederationsPagedCallable()

Lists federations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListFederationsRequest request =
           ListFederationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Federation> future =
           dataprocMetastoreFederationClient.listFederationsPagedCallable().futureCall(request);
       // Do something.
       for (Federation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFederationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListFederationsRequest),[ListFederationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListFederationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataprocMetastoreFederationClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           dataprocMetastoreFederationClient.listLocations(request).iterateAll()) {
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
`[DataprocMetastoreFederationClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataprocMetastoreFederationClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataprocMetastoreFederationClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataprocMetastoreFederationClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreFederationClient.ListLocationsPagedResponse)>` |   
  
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataprocMetastoreFederationClient.setIamPolicy(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataprocMetastoreFederationClient.setIamPolicyCallable().futureCall(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           dataprocMetastoreFederationClient.testIamPermissions(request);
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
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataprocMetastoreFederationClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateFederationAsync(Federation federation, FieldMask updateMask)
    
    
    public final OperationFuture<Federation,OperationMetadata> updateFederationAsync(Federation federation, FieldMask updateMask)

Updates the fields of a federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       Federation federation = Federation.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Federation response =
           dataprocMetastoreFederationClient.updateFederationAsync(federation, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`federation` | `[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation)`  
Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore federation's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateFederationAsync(UpdateFederationRequest request)
    
    
    public final OperationFuture<Federation,OperationMetadata> updateFederationAsync(UpdateFederationRequest request)

Updates the fields of a federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       UpdateFederationRequest request =
           UpdateFederationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Federation response = dataprocMetastoreFederationClient.updateFederationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateFederationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateFederationCallable()
    
    
    public final UnaryCallable<UpdateFederationRequest,Operation> updateFederationCallable()

Updates the fields of a federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       UpdateFederationRequest request =
           UpdateFederationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreFederationClient.updateFederationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateFederationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFederationOperationCallable()
    
    
    public final OperationCallable<UpdateFederationRequest,Federation,OperationMetadata> updateFederationOperationCallable()

Updates the fields of a federation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreFederationClient dataprocMetastoreFederationClient =
         DataprocMetastoreFederationClient.create()) {
       UpdateFederationRequest request =
           UpdateFederationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFederation(Federation.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Federation, OperationMetadata> future =
           dataprocMetastoreFederationClient.updateFederationOperationCallable().futureCall(request);
       // Do something.
       Federation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFederationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateFederationRequest),[Federation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Federation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
