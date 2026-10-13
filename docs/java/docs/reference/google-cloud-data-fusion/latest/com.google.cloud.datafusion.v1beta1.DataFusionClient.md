---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient
title: Class DataFusionClient (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:47.000060+00:00
---

# Class DataFusionClient (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataFusionClient (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-data-fusion/google-cloud-data-fusion/src/main/java/com/google/cloud/datafusion/v1beta1/DataFusionClient.java)| [Product Reference](https://cloud.google.com/data-fusion/docs)| [REST Documentation](https://cloud.google.com/data-fusion/docs/reference/rest)  
---|---|---  
  
Service Description: Service for creating and managing Data Fusion instances. Data Fusion enables ETL developers to build code-free, data integration pipelines via a point-and-click UI.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = dataFusionClient.getInstance(request);
     }
     

Note: close() needs to be called on the DataFusionClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAvailableVersions |  Lists possible versions for Data Fusion instances in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAvailableVersions(ListAvailableVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAvailableVersions(LocationName parent) 
  * listAvailableVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAvailableVersionsPagedCallable() 
  * listAvailableVersionsCallable() 

  
ListInstances |  Lists Data Fusion instances in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
GetInstance |  Gets details of a single Data Fusion instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInstance(GetInstanceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInstanceCallable() 

  
CreateInstance |  Creates a new Data Fusion instance in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstanceAsync(CreateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstanceAsync(LocationName parent, Instance instance, String instanceId) 
  * createInstanceAsync(String parent, Instance instance, String instanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstanceOperationCallable() 
  * createInstanceCallable() 

  
DeleteInstance |  Deletes a single Data Fusion instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstanceAsync(DeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstanceAsync(InstanceName name) 
  * deleteInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstanceOperationCallable() 
  * deleteInstanceCallable() 

  
UpdateInstance |  Updates a single Data Fusion instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInstanceAsync(UpdateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateInstanceAsync(Instance instance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInstanceOperationCallable() 
  * updateInstanceCallable() 

  
RestartInstance |  Restart a single Data Fusion instance. At the end of an operation instance is fully restarted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restartInstanceAsync(RestartInstanceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restartInstanceOperationCallable() 
  * restartInstanceCallable() 

  
UpgradeInstance |  Upgrade a single Data Fusion instance. At the end of an operation instance is fully upgraded. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * upgradeInstanceAsync(UpgradeInstanceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * upgradeInstanceOperationCallable() 
  * upgradeInstanceCallable() 

  
RemoveIamPolicy |  Remove IAM policy that is currently set on the given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeIamPolicy(RemoveIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeIamPolicyCallable() 

  
ListNamespaces |  List namespaces in a given instance |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNamespaces(ListNamespacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNamespaces(InstanceName parent) 
  * listNamespaces(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNamespacesPagedCallable() 
  * listNamespacesCallable() 

  
AddDnsPeering |  Add DNS peering on the given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addDnsPeering(AddDnsPeeringRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addDnsPeering(InstanceName parent) 
  * addDnsPeering(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addDnsPeeringCallable() 

  
RemoveDnsPeering |  Remove DNS peering on the given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeDnsPeering(RemoveDnsPeeringRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * removeDnsPeering(InstanceName parent) 
  * removeDnsPeering(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeDnsPeeringCallable() 

  
ListDnsPeerings |  List DNS peering for a given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDnsPeerings(ListDnsPeeringsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDnsPeerings(InstanceName parent) 
  * listDnsPeerings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDnsPeeringsPagedCallable() 
  * listDnsPeeringsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataFusionSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataFusionSettings dataFusionSettings =
         DataFusionSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataFusionClient dataFusionClient = DataFusionClient.create(dataFusionSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataFusionSettings dataFusionSettings =
         DataFusionSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataFusionClient dataFusionClient = DataFusionClient.create(dataFusionSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataFusionSettings dataFusionSettings = DataFusionSettings.newHttpJsonBuilder().build();
     DataFusionClient dataFusionClient = DataFusionClient.create(dataFusionSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataFusionClient

## Static Methods 

### create()
    
    
    public static final DataFusionClient create()

Constructs an instance of DataFusionClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataFusionSettings settings)
    
    
    public static final DataFusionClient create(DataFusionSettings settings)

Constructs an instance of DataFusionClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataFusionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataFusionStub stub)
    
    
    public static final DataFusionClient create(DataFusionStub stub)

Constructs an instance of DataFusionClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataFusionSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataFusionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.stub.DataFusionStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient)` |   
  
## Constructors 

### DataFusionClient(DataFusionSettings settings)
    
    
    protected DataFusionClient(DataFusionSettings settings)

Constructs an instance of DataFusionClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataFusionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionSettings)`  
  
  
### DataFusionClient(DataFusionStub stub)
    
    
    protected DataFusionClient(DataFusionStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataFusionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.stub.DataFusionStub)`  
  
  
## Methods 

### addDnsPeering(@Nullable InstanceName parent)
    
    
    public final AddDnsPeeringResponse addDnsPeering(@Nullable InstanceName parent)

Add DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       AddDnsPeeringResponse response = dataFusionClient.addDnsPeering(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.InstanceName`  
Required. The resource on which DNS peering will be created.  
**Returns**  
---  
**Type** | **Description**  
`[AddDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringResponse)` |   
  
### addDnsPeering(AddDnsPeeringRequest request)
    
    
    public final AddDnsPeeringResponse addDnsPeering(AddDnsPeeringRequest request)

Add DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       AddDnsPeeringRequest request =
           AddDnsPeeringRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setDnsPeering(DnsPeering.newBuilder().build())
               .build();
       AddDnsPeeringResponse response = dataFusionClient.addDnsPeering(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AddDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringResponse)` |   
  
### addDnsPeering(String parent)
    
    
    public final AddDnsPeeringResponse addDnsPeering(String parent)

Add DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       AddDnsPeeringResponse response = dataFusionClient.addDnsPeering(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource on which DNS peering will be created.  
**Returns**  
---  
**Type** | **Description**  
`[AddDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringResponse)` |   
  
### addDnsPeeringCallable()
    
    
    public final UnaryCallable<AddDnsPeeringRequest,AddDnsPeeringResponse> addDnsPeeringCallable()

Add DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       AddDnsPeeringRequest request =
           AddDnsPeeringRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setDnsPeering(DnsPeering.newBuilder().build())
               .build();
       ApiFuture<AddDnsPeeringResponse> future =
           dataFusionClient.addDnsPeeringCallable().futureCall(request);
       // Do something.
       AddDnsPeeringResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringRequest),[AddDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringResponse)>` |   
  
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

Creates a new Data Fusion instance in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response = dataFusionClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.LocationName`  
Required. The instance's project and location in the format projects/{project}/locations/{location}.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)`  
An instance resource.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the instance to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### createInstanceAsync(CreateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(CreateInstanceRequest request)

Creates a new Data Fusion instance in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .build();
       Instance response = dataFusionClient.createInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### createInstanceAsync(String parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(String parent, Instance instance, String instanceId)

Creates a new Data Fusion instance in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response = dataFusionClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance's project and location in the format projects/{project}/locations/{location}.  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)`  
An instance resource.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the instance to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### createInstanceCallable()
    
    
    public final UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

Creates a new Data Fusion instance in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .build();
       ApiFuture<Operation> future = dataFusionClient.createInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public final OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

Creates a new Data Fusion instance in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           dataFusionClient.createInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### deleteInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(@Nullable InstanceName name)

Deletes a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       dataFusionClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.InstanceName`  
Required. The instance resource name in the format projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### deleteInstanceAsync(DeleteInstanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(DeleteInstanceRequest request)

Deletes a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       dataFusionClient.deleteInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### deleteInstanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(String name)

Deletes a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       dataFusionClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance resource name in the format projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public final UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

Deletes a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Operation> future = dataFusionClient.deleteInstanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

Deletes a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataFusionClient.deleteInstanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public final Instance getInstance(GetInstanceRequest request)

Gets details of a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = dataFusionClient.getInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)` |   
  
### getInstanceCallable()
    
    
    public final UnaryCallable<GetInstanceRequest,Instance> getInstanceCallable()

Gets details of a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Instance> future = dataFusionClient.getInstanceCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DataFusionSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.DataFusionSettings` |   
  
### getStub()
    
    
    public DataFusionStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataFusionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.stub.DataFusionStub)` |   
  
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
  
### listAvailableVersions(@Nullable LocationName parent)
    
    
    public final DataFusionClient.ListAvailableVersionsPagedResponse listAvailableVersions(@Nullable LocationName parent)

Lists possible versions for Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Version element : dataFusionClient.listAvailableVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.LocationName`  
Required. The project and location for which to retrieve instance information in the format projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListAvailableVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListAvailableVersionsPagedResponse)` |   
  
### listAvailableVersions(ListAvailableVersionsRequest request)
    
    
    public final DataFusionClient.ListAvailableVersionsPagedResponse listAvailableVersions(ListAvailableVersionsRequest request)

Lists possible versions for Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListAvailableVersionsRequest request =
           ListAvailableVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLatestPatchOnly(true)
               .build();
       for (Version element : dataFusionClient.listAvailableVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAvailableVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListAvailableVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListAvailableVersionsPagedResponse)` |   
  
### listAvailableVersions(String parent)
    
    
    public final DataFusionClient.ListAvailableVersionsPagedResponse listAvailableVersions(String parent)

Lists possible versions for Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Version element : dataFusionClient.listAvailableVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location for which to retrieve instance information in the format projects/{project}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListAvailableVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListAvailableVersionsPagedResponse)` |   
  
### listAvailableVersionsCallable()
    
    
    public final UnaryCallable<ListAvailableVersionsRequest,ListAvailableVersionsResponse> listAvailableVersionsCallable()

Lists possible versions for Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListAvailableVersionsRequest request =
           ListAvailableVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLatestPatchOnly(true)
               .build();
       while (true) {
         ListAvailableVersionsResponse response =
             dataFusionClient.listAvailableVersionsCallable().call(request);
         for (Version element : response.getAvailableVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAvailableVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsRequest),[ListAvailableVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsResponse)>` |   
  
### listAvailableVersionsPagedCallable()
    
    
    public final UnaryCallable<ListAvailableVersionsRequest,DataFusionClient.ListAvailableVersionsPagedResponse> listAvailableVersionsPagedCallable()

Lists possible versions for Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListAvailableVersionsRequest request =
           ListAvailableVersionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLatestPatchOnly(true)
               .build();
       ApiFuture<Version> future =
           dataFusionClient.listAvailableVersionsPagedCallable().futureCall(request);
       // Do something.
       for (Version element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAvailableVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsRequest),[ListAvailableVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListAvailableVersionsPagedResponse)>` |   
  
### listDnsPeerings(@Nullable InstanceName parent)
    
    
    public final DataFusionClient.ListDnsPeeringsPagedResponse listDnsPeerings(@Nullable InstanceName parent)

List DNS peering for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (DnsPeering element : dataFusionClient.listDnsPeerings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.InstanceName`  
Required. The resource on which dns peering will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListDnsPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListDnsPeeringsPagedResponse)` |   
  
### listDnsPeerings(ListDnsPeeringsRequest request)
    
    
    public final DataFusionClient.ListDnsPeeringsPagedResponse listDnsPeerings(ListDnsPeeringsRequest request)

List DNS peering for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListDnsPeeringsRequest request =
           ListDnsPeeringsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DnsPeering element : dataFusionClient.listDnsPeerings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDnsPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListDnsPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListDnsPeeringsPagedResponse)` |   
  
### listDnsPeerings(String parent)
    
    
    public final DataFusionClient.ListDnsPeeringsPagedResponse listDnsPeerings(String parent)

List DNS peering for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       for (DnsPeering element : dataFusionClient.listDnsPeerings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource on which dns peering will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListDnsPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListDnsPeeringsPagedResponse)` |   
  
### listDnsPeeringsCallable()
    
    
    public final UnaryCallable<ListDnsPeeringsRequest,ListDnsPeeringsResponse> listDnsPeeringsCallable()

List DNS peering for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListDnsPeeringsRequest request =
           ListDnsPeeringsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDnsPeeringsResponse response = dataFusionClient.listDnsPeeringsCallable().call(request);
         for (DnsPeering element : response.getDnsPeeringsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDnsPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsRequest),[ListDnsPeeringsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsResponse)>` |   
  
### listDnsPeeringsPagedCallable()
    
    
    public final UnaryCallable<ListDnsPeeringsRequest,DataFusionClient.ListDnsPeeringsPagedResponse> listDnsPeeringsPagedCallable()

List DNS peering for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListDnsPeeringsRequest request =
           ListDnsPeeringsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DnsPeering> future =
           dataFusionClient.listDnsPeeringsPagedCallable().futureCall(request);
       // Do something.
       for (DnsPeering element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDnsPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsRequest),[ListDnsPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListDnsPeeringsPagedResponse)>` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public final DataFusionClient.ListInstancesPagedResponse listInstances(ListInstancesRequest request)

Lists Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Instance element : dataFusionClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

Lists Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInstancesResponse response = dataFusionClient.listInstancesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,DataFusionClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists Data Fusion instances in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Instance> future =
           dataFusionClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (Instance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListInstancesPagedResponse)>` |   
  
### listNamespaces(@Nullable InstanceName parent)
    
    
    public final DataFusionClient.ListNamespacesPagedResponse listNamespaces(@Nullable InstanceName parent)

List namespaces in a given instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (Namespace element : dataFusionClient.listNamespaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.InstanceName`  
Required. The instance to list its namespaces.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListNamespacesPagedResponse)` |   
  
### listNamespaces(ListNamespacesRequest request)
    
    
    public final DataFusionClient.ListNamespacesPagedResponse listNamespaces(ListNamespacesRequest request)

List namespaces in a given instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(NamespaceView.forNumber(0))
               .build();
       for (Namespace element : dataFusionClient.listNamespaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListNamespacesPagedResponse)` |   
  
### listNamespaces(String parent)
    
    
    public final DataFusionClient.ListNamespacesPagedResponse listNamespaces(String parent)

List namespaces in a given instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       for (Namespace element : dataFusionClient.listNamespaces(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance to list its namespaces.  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionClient.ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListNamespacesPagedResponse)` |   
  
### listNamespacesCallable()
    
    
    public final UnaryCallable<ListNamespacesRequest,ListNamespacesResponse> listNamespacesCallable()

List namespaces in a given instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(NamespaceView.forNumber(0))
               .build();
       while (true) {
         ListNamespacesResponse response = dataFusionClient.listNamespacesCallable().call(request);
         for (Namespace element : response.getNamespacesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesRequest),[ListNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesResponse)>` |   
  
### listNamespacesPagedCallable()
    
    
    public final UnaryCallable<ListNamespacesRequest,DataFusionClient.ListNamespacesPagedResponse> listNamespacesPagedCallable()

List namespaces in a given instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       ListNamespacesRequest request =
           ListNamespacesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(NamespaceView.forNumber(0))
               .build();
       ApiFuture<Namespace> future =
           dataFusionClient.listNamespacesPagedCallable().futureCall(request);
       // Do something.
       for (Namespace element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesRequest),[ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionClient.ListNamespacesPagedResponse)>` |   
  
### removeDnsPeering(@Nullable InstanceName parent)
    
    
    public final RemoveDnsPeeringResponse removeDnsPeering(@Nullable InstanceName parent)

Remove DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       RemoveDnsPeeringResponse response = dataFusionClient.removeDnsPeering(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datafusion.v1beta1.InstanceName`  
Required. The resource on which DNS peering will be removed.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringResponse)` |   
  
### removeDnsPeering(RemoveDnsPeeringRequest request)
    
    
    public final RemoveDnsPeeringResponse removeDnsPeering(RemoveDnsPeeringRequest request)

Remove DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RemoveDnsPeeringRequest request =
           RemoveDnsPeeringRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setZone("zone3744684")
               .build();
       RemoveDnsPeeringResponse response = dataFusionClient.removeDnsPeering(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringResponse)` |   
  
### removeDnsPeering(String parent)
    
    
    public final RemoveDnsPeeringResponse removeDnsPeering(String parent)

Remove DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       RemoveDnsPeeringResponse response = dataFusionClient.removeDnsPeering(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource on which DNS peering will be removed.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringResponse)` |   
  
### removeDnsPeeringCallable()
    
    
    public final UnaryCallable<RemoveDnsPeeringRequest,RemoveDnsPeeringResponse> removeDnsPeeringCallable()

Remove DNS peering on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RemoveDnsPeeringRequest request =
           RemoveDnsPeeringRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setZone("zone3744684")
               .build();
       ApiFuture<RemoveDnsPeeringResponse> future =
           dataFusionClient.removeDnsPeeringCallable().futureCall(request);
       // Do something.
       RemoveDnsPeeringResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringRequest),[RemoveDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringResponse)>` |   
  
### removeIamPolicy(RemoveIamPolicyRequest request)
    
    
    public final RemoveIamPolicyResponse removeIamPolicy(RemoveIamPolicyRequest request)

Remove IAM policy that is currently set on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RemoveIamPolicyRequest request =
           RemoveIamPolicyRequest.newBuilder().setResource("resource-341064690").build();
       RemoveIamPolicyResponse response = dataFusionClient.removeIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveIamPolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyResponse)` |   
  
### removeIamPolicyCallable()
    
    
    public final UnaryCallable<RemoveIamPolicyRequest,RemoveIamPolicyResponse> removeIamPolicyCallable()

Remove IAM policy that is currently set on the given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RemoveIamPolicyRequest request =
           RemoveIamPolicyRequest.newBuilder().setResource("resource-341064690").build();
       ApiFuture<RemoveIamPolicyResponse> future =
           dataFusionClient.removeIamPolicyCallable().futureCall(request);
       // Do something.
       RemoveIamPolicyResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyRequest),[RemoveIamPolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyResponse)>` |   
  
### restartInstanceAsync(RestartInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> restartInstanceAsync(RestartInstanceRequest request)

Restart a single Data Fusion instance. At the end of an operation instance is fully restarted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = dataFusionClient.restartInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RestartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### restartInstanceCallable()
    
    
    public final UnaryCallable<RestartInstanceRequest,Operation> restartInstanceCallable()

Restart a single Data Fusion instance. At the end of an operation instance is fully restarted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Operation> future = dataFusionClient.restartInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RestartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartInstanceOperationCallable()
    
    
    public final OperationCallable<RestartInstanceRequest,Instance,OperationMetadata> restartInstanceOperationCallable()

Restart a single Data Fusion instance. At the end of an operation instance is fully restarted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       RestartInstanceRequest request =
           RestartInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           dataFusionClient.restartInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RestartInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateInstanceAsync(Instance instance, FieldMask updateMask)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(Instance instance, FieldMask updateMask)

Updates a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       Instance instance = Instance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Instance response = dataFusionClient.updateInstanceAsync(instance, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)`  
Required. The instance resource that replaces the resource on the server. Currently, Data Fusion only allows replacing labels, options, and stack driver settings. All other fields will be ignored.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields that the update will overwrite in an instance resource. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask, all the supported fields (labels and options currently) will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### updateInstanceAsync(UpdateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(UpdateInstanceRequest request)

Updates a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setInstance(Instance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Instance response = dataFusionClient.updateInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### updateInstanceCallable()
    
    
    public final UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

Updates a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setInstance(Instance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = dataFusionClient.updateInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public final OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

Updates a single Data Fusion instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setInstance(Instance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           dataFusionClient.updateInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### upgradeInstanceAsync(UpgradeInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> upgradeInstanceAsync(UpgradeInstanceRequest request)

Upgrade a single Data Fusion instance. At the end of an operation instance is fully upgraded.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpgradeInstanceRequest request =
           UpgradeInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = dataFusionClient.upgradeInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpgradeInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
### upgradeInstanceCallable()
    
    
    public final UnaryCallable<UpgradeInstanceRequest,Operation> upgradeInstanceCallable()

Upgrade a single Data Fusion instance. At the end of an operation instance is fully upgraded.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpgradeInstanceRequest request =
           UpgradeInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Operation> future = dataFusionClient.upgradeInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpgradeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### upgradeInstanceOperationCallable()
    
    
    public final OperationCallable<UpgradeInstanceRequest,Instance,OperationMetadata> upgradeInstanceOperationCallable()

Upgrade a single Data Fusion instance. At the end of an operation instance is fully upgraded.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataFusionClient dataFusionClient = DataFusionClient.create()) {
       UpgradeInstanceRequest request =
           UpgradeInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           dataFusionClient.upgradeInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpgradeInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
