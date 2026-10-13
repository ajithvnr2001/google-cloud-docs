---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient
title: Class ParallelstoreClient (0.62.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:47.773361+00:00
---

# Class ParallelstoreClient (0.62.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParallelstoreClient (0.62.0) Stay organized with collections  Save and categorize content based on your preferences. 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-parallelstore/google-cloud-parallelstore/src/main/java/com/google/cloud/parallelstore/v1/ParallelstoreClient.java)| [Product Reference](https://cloud/parallelstore?hl=en)  
---|---  
  
Service Description: Service describing handlers for resources Configures and manages parallelstore resources.

Parallelstore service.

The `parallelstore.googleapis.com` service implements the parallelstore API and defines the following resource model for managing instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of instances named `/instances/*`. 
  * Parallelstore instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be a Google Cloud `zone`; for example:

  * `projects/12345/locations/us-central1-c/instances/my-parallelstore-share`



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Instance response = parallelstoreClient.getInstance(name);
     }
     

Note: close() needs to be called on the ParallelstoreClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListInstances |  Lists all instances in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInstances(LocationName parent) 
  * listInstances(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
GetInstance |  Gets details of a single instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInstance(GetInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInstance(InstanceName name) 
  * getInstance(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInstanceCallable() 

  
CreateInstance |  Creates a Parallelstore instance in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstanceAsync(CreateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstanceAsync(LocationName parent, Instance instance, String instanceId) 
  * createInstanceAsync(String parent, Instance instance, String instanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstanceOperationCallable() 
  * createInstanceCallable() 

  
UpdateInstance |  Updates the parameters of a single instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInstanceAsync(UpdateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateInstanceAsync(Instance instance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInstanceOperationCallable() 
  * updateInstanceCallable() 

  
DeleteInstance |  Deletes a single instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstanceAsync(DeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstanceAsync(InstanceName name) 
  * deleteInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstanceOperationCallable() 
  * deleteInstanceCallable() 

  
ImportData |  Copies data from Cloud Storage to Parallelstore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDataAsync(ImportDataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDataOperationCallable() 
  * importDataCallable() 

  
ExportData |  Copies data from Parallelstore to Cloud Storage. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDataAsync(ExportDataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDataOperationCallable() 
  * exportDataCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of ParallelstoreSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParallelstoreSettings parallelstoreSettings =
         ParallelstoreSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ParallelstoreClient parallelstoreClient = ParallelstoreClient.create(parallelstoreSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParallelstoreSettings parallelstoreSettings =
         ParallelstoreSettings.newBuilder().setEndpoint(myEndpoint).build();
     ParallelstoreClient parallelstoreClient = ParallelstoreClient.create(parallelstoreSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParallelstoreSettings parallelstoreSettings =
         ParallelstoreSettings.newHttpJsonBuilder().build();
     ParallelstoreClient parallelstoreClient = ParallelstoreClient.create(parallelstoreSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ParallelstoreClient

## Static Methods 

### create()
    
    
    public static final ParallelstoreClient create()

Constructs an instance of ParallelstoreClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ParallelstoreSettings settings)
    
    
    public static final ParallelstoreClient create(ParallelstoreSettings settings)

Constructs an instance of ParallelstoreClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ParallelstoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ParallelstoreStub stub)
    
    
    public static final ParallelstoreClient create(ParallelstoreStub stub)

Constructs an instance of ParallelstoreClient, using the given stub for making calls. This is for advanced usage - prefer using create(ParallelstoreSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ParallelstoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.stub.ParallelstoreStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient)` |   
  
## Constructors 

### ParallelstoreClient(ParallelstoreSettings settings)
    
    
    protected ParallelstoreClient(ParallelstoreSettings settings)

Constructs an instance of ParallelstoreClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ParallelstoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreSettings)`  
  
  
### ParallelstoreClient(ParallelstoreStub stub)
    
    
    protected ParallelstoreClient(ParallelstoreStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ParallelstoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.stub.ParallelstoreStub)`  
  
  
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

### createInstanceAsync(@Nullable LocationName parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(@Nullable LocationName parent, Instance instance, String instanceId)

Creates a Parallelstore instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           parallelstoreClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.parallelstore.v1.LocationName`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)`  
Required. The instance to create.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Parallelstore instance. 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the customer project / location 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### createInstanceAsync(CreateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(CreateInstanceRequest request)

Creates a Parallelstore instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Instance response = parallelstoreClient.createInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### createInstanceAsync(String parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(String parent, Instance instance, String instanceId)

Creates a Parallelstore instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response =
           parallelstoreClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)`  
Required. The instance to create.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Parallelstore instance. 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the customer project / location 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### createInstanceCallable()
    
    
    public final UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

Creates a Parallelstore instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           parallelstoreClient.createInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public final OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

Creates a Parallelstore instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           parallelstoreClient.createInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(@Nullable InstanceName name)

Deletes a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       parallelstoreClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.parallelstore.v1.InstanceName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(DeleteInstanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(DeleteInstanceRequest request)

Deletes a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       parallelstoreClient.deleteInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(String name)

Deletes a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       parallelstoreClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public final UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

Deletes a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           parallelstoreClient.deleteInstanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

Deletes a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           parallelstoreClient.deleteInstanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### exportDataAsync(ExportDataRequest request)
    
    
    public final OperationFuture<ExportDataResponse,ExportDataMetadata> exportDataAsync(ExportDataRequest request)

Copies data from Parallelstore to Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       ExportDataResponse response = parallelstoreClient.exportDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataResponse),[ExportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataMetadata)>` |   
  
### exportDataCallable()
    
    
    public final UnaryCallable<ExportDataRequest,Operation> exportDataCallable()

Copies data from Parallelstore to Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       ApiFuture<Operation> future = parallelstoreClient.exportDataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDataOperationCallable()
    
    
    public final OperationCallable<ExportDataRequest,ExportDataResponse,ExportDataMetadata> exportDataOperationCallable()

Copies data from Parallelstore to Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ExportDataRequest request =
           ExportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       OperationFuture<ExportDataResponse, ExportDataMetadata> future =
           parallelstoreClient.exportDataOperationCallable().futureCall(request);
       // Do something.
       ExportDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataRequest),[ExportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataResponse),[ExportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ExportDataMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInstance(@Nullable InstanceName name)
    
    
    public final Instance getInstance(@Nullable InstanceName name)

Gets details of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Instance response = parallelstoreClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.parallelstore.v1.InstanceName`  
Required. The instance resource name, in the format `projects/{project_id}/locations/{location}/instances/{instance_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public final Instance getInstance(GetInstanceRequest request)

Gets details of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = parallelstoreClient.getInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)` |   
  
### getInstance(String name)
    
    
    public final Instance getInstance(String name)

Gets details of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       Instance response = parallelstoreClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance resource name, in the format `projects/{project_id}/locations/{location}/instances/{instance_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)` |   
  
### getInstanceCallable()
    
    
    public final UnaryCallable<GetInstanceRequest,Instance> getInstanceCallable()

Gets details of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Instance> future = parallelstoreClient.getInstanceCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = parallelstoreClient.getLocation(request);
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
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = parallelstoreClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable ParallelstoreSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.parallelstore.v1.ParallelstoreSettings` |   
  
### getStub()
    
    
    public ParallelstoreStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.stub.ParallelstoreStub)` |   
  
### importDataAsync(ImportDataRequest request)
    
    
    public final OperationFuture<ImportDataResponse,ImportDataMetadata> importDataAsync(ImportDataRequest request)

Copies data from Cloud Storage to Parallelstore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       ImportDataResponse response = parallelstoreClient.importDataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataResponse),[ImportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataMetadata)>` |   
  
### importDataCallable()
    
    
    public final UnaryCallable<ImportDataRequest,Operation> importDataCallable()

Copies data from Cloud Storage to Parallelstore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       ApiFuture<Operation> future = parallelstoreClient.importDataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDataOperationCallable()
    
    
    public final OperationCallable<ImportDataRequest,ImportDataResponse,ImportDataMetadata> importDataOperationCallable()

Copies data from Cloud Storage to Parallelstore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ImportDataRequest request =
           ImportDataRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .setServiceAccount(ServiceAccountName.of("[PROJECT]", "[SERVICE_ACCOUNT]").toString())
               .setMetadataOptions(TransferMetadataOptions.newBuilder().build())
               .build();
       OperationFuture<ImportDataResponse, ImportDataMetadata> future =
           parallelstoreClient.importDataOperationCallable().futureCall(request);
       // Do something.
       ImportDataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataRequest),[ImportDataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataResponse),[ImportDataMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ImportDataMetadata)>` |   
  
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
  
### listInstances(@Nullable LocationName parent)
    
    
    public final ParallelstoreClient.ListInstancesPagedResponse listInstances(@Nullable LocationName parent)

Lists all instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Instance element : parallelstoreClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.parallelstore.v1.LocationName`  
Required. The project and location for which to retrieve instance information, in the format `projects/{project_id}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListInstancesPagedResponse)` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public final ParallelstoreClient.ListInstancesPagedResponse listInstances(ListInstancesRequest request)

Lists all instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Instance element : parallelstoreClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListInstancesPagedResponse)` |   
  
### listInstances(String parent)
    
    
    public final ParallelstoreClient.ListInstancesPagedResponse listInstances(String parent)

Lists all instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Instance element : parallelstoreClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve instance information, in the format `projects/{project_id}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

Lists all instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInstancesResponse response = parallelstoreClient.listInstancesCallable().call(request);
         for (Instance element : response.getInstancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,ParallelstoreClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists all instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Instance> future =
           parallelstoreClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (Instance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListInstancesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ParallelstoreClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : parallelstoreClient.listLocations(request).iterateAll()) {
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
`[ParallelstoreClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = parallelstoreClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ParallelstoreClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           parallelstoreClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.ParallelstoreClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateInstanceAsync(Instance instance, FieldMask updateMask)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(Instance instance, FieldMask updateMask)

Updates the parameters of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       Instance instance = Instance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Instance response = parallelstoreClient.updateInstanceAsync(instance, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance)`  
Required. The instance to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. At least one path must be supplied in this field. The fields specified in the update_mask are relative to the resource, not the full request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### updateInstanceAsync(UpdateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(UpdateInstanceRequest request)

Updates the parameters of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Instance response = parallelstoreClient.updateInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
### updateInstanceCallable()
    
    
    public final UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

Updates the parameters of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           parallelstoreClient.updateInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public final OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

Updates the parameters of a single instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParallelstoreClient parallelstoreClient = ParallelstoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           parallelstoreClient.updateInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
