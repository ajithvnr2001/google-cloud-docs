---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient
title: Class DataTransferServiceClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:02.302821+00:00
---

# Class DataTransferServiceClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataTransferServiceClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkconnectivity/google-cloud-networkconnectivity/src/main/java/com/google/cloud/networkconnectivity/v1/DataTransferServiceClient.java)| [Product Reference](https://cloud.google.com/network-connectivity/docs)  
---|---  
  
Service Description: DataTransferService is the service for the Data Transfer API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfigName name =
           MulticloudDataTransferConfigName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.getMulticloudDataTransferConfig(name);
     }
     

Note: close() needs to be called on the DataTransferServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListMulticloudDataTransferConfigs |  Lists the `MulticloudDataTransferConfig` resources in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMulticloudDataTransferConfigs(LocationName parent) 
  * listMulticloudDataTransferConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMulticloudDataTransferConfigsPagedCallable() 
  * listMulticloudDataTransferConfigsCallable() 

  
GetMulticloudDataTransferConfig |  Gets the details of a `MulticloudDataTransferConfig` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMulticloudDataTransferConfig(MulticloudDataTransferConfigName name) 
  * getMulticloudDataTransferConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMulticloudDataTransferConfigCallable() 

  
CreateMulticloudDataTransferConfig |  Creates a `MulticloudDataTransferConfig` resource in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMulticloudDataTransferConfigAsync(LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId) 
  * createMulticloudDataTransferConfigAsync(String parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMulticloudDataTransferConfigOperationCallable() 
  * createMulticloudDataTransferConfigCallable() 

  
UpdateMulticloudDataTransferConfig |  Updates a `MulticloudDataTransferConfig` resource in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMulticloudDataTransferConfigOperationCallable() 
  * updateMulticloudDataTransferConfigCallable() 

  
DeleteMulticloudDataTransferConfig |  Deletes a `MulticloudDataTransferConfig` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteMulticloudDataTransferConfigAsync(MulticloudDataTransferConfigName name) 
  * deleteMulticloudDataTransferConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMulticloudDataTransferConfigOperationCallable() 
  * deleteMulticloudDataTransferConfigCallable() 

  
ListDestinations |  Lists the `Destination` resources in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDestinations(ListDestinationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDestinations(MulticloudDataTransferConfigName parent) 
  * listDestinations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDestinationsPagedCallable() 
  * listDestinationsCallable() 

  
GetDestination |  Gets the details of a `Destination` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDestination(GetDestinationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDestination(DestinationName name) 
  * getDestination(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDestinationCallable() 

  
CreateDestination |  Creates a `Destination` resource in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDestinationAsync(CreateDestinationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDestinationAsync(MulticloudDataTransferConfigName parent, Destination destination, String destinationId) 
  * createDestinationAsync(String parent, Destination destination, String destinationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDestinationOperationCallable() 
  * createDestinationCallable() 

  
UpdateDestination |  Updates a `Destination` resource in a specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDestinationAsync(UpdateDestinationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDestinationAsync(Destination destination, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDestinationOperationCallable() 
  * updateDestinationCallable() 

  
DeleteDestination |  Deletes a `Destination` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDestinationAsync(DeleteDestinationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDestinationAsync(DestinationName name) 
  * deleteDestinationAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDestinationOperationCallable() 
  * deleteDestinationCallable() 

  
GetMulticloudDataTransferSupportedService |  Gets the details of a service that is supported for Data Transfer Essentials. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMulticloudDataTransferSupportedService(MulticloudDataTransferSupportedServiceName name) 
  * getMulticloudDataTransferSupportedService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMulticloudDataTransferSupportedServiceCallable() 

  
ListMulticloudDataTransferSupportedServices |  Lists the services in the project for a region that are supported for Data Transfer Essentials. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMulticloudDataTransferSupportedServices(LocationName parent) 
  * listMulticloudDataTransferSupportedServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMulticloudDataTransferSupportedServicesPagedCallable() 
  * listMulticloudDataTransferSupportedServicesCallable() 

  
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

This class can be customized by passing in a custom instance of DataTransferServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataTransferServiceSettings dataTransferServiceSettings =
         DataTransferServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataTransferServiceClient dataTransferServiceClient =
         DataTransferServiceClient.create(dataTransferServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataTransferServiceSettings dataTransferServiceSettings =
         DataTransferServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataTransferServiceClient dataTransferServiceClient =
         DataTransferServiceClient.create(dataTransferServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataTransferServiceClient

## Static Methods 

### create()
    
    
    public static final DataTransferServiceClient create()

Constructs an instance of DataTransferServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataTransferServiceSettings settings)
    
    
    public static final DataTransferServiceClient create(DataTransferServiceSettings settings)

Constructs an instance of DataTransferServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataTransferServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataTransferServiceStub stub)
    
    
    public static final DataTransferServiceClient create(DataTransferServiceStub stub)

Constructs an instance of DataTransferServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataTransferServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataTransferServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.DataTransferServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient)` |   
  
## Constructors 

### DataTransferServiceClient(DataTransferServiceSettings settings)
    
    
    protected DataTransferServiceClient(DataTransferServiceSettings settings)

Constructs an instance of DataTransferServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataTransferServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceSettings)`  
  
  
### DataTransferServiceClient(DataTransferServiceStub stub)
    
    
    protected DataTransferServiceClient(DataTransferServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataTransferServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.DataTransferServiceStub)`  
  
  
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

### createDestinationAsync(@Nullable MulticloudDataTransferConfigName parent, Destination destination, String destinationId)
    
    
    public final OperationFuture<Destination,OperationMetadata> createDestinationAsync(@Nullable MulticloudDataTransferConfigName parent, Destination destination, String destinationId)

Creates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfigName parent =
           MulticloudDataTransferConfigName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
       Destination destination = Destination.newBuilder().build();
       String destinationId = "destinationId306545097";
       Destination response =
           dataTransferServiceClient
               .createDestinationAsync(parent, destination, destinationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfigName`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createDestinationAsync(CreateDestinationRequest request)
    
    
    public final OperationFuture<Destination,OperationMetadata> createDestinationAsync(CreateDestinationRequest request)

Creates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateDestinationRequest request =
           CreateDestinationRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setDestinationId("destinationId306545097")
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Destination response = dataTransferServiceClient.createDestinationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createDestinationAsync(String parent, Destination destination, String destinationId)
    
    
    public final OperationFuture<Destination,OperationMetadata> createDestinationAsync(String parent, Destination destination, String destinationId)

Creates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String parent =
           MulticloudDataTransferConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
               .toString();
       Destination destination = Destination.newBuilder().build();
       String destinationId = "destinationId306545097";
       Destination response =
           dataTransferServiceClient
               .createDestinationAsync(parent, destination, destinationId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource.  
`destination` | `[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)`  
Required. The `Destination` resource to create.  
`destinationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the `Destination` resource, which becomes the final component of the `Destination` resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createDestinationCallable()
    
    
    public final UnaryCallable<CreateDestinationRequest,Operation> createDestinationCallable()

Creates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateDestinationRequest request =
           CreateDestinationRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setDestinationId("destinationId306545097")
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient.createDestinationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateDestinationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDestinationOperationCallable()
    
    
    public final OperationCallable<CreateDestinationRequest,Destination,OperationMetadata> createDestinationOperationCallable()

Creates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateDestinationRequest request =
           CreateDestinationRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setDestinationId("destinationId306545097")
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Destination, OperationMetadata> future =
           dataTransferServiceClient.createDestinationOperationCallable().futureCall(request);
       // Do something.
       Destination response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateDestinationRequest),[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createMulticloudDataTransferConfigAsync(@Nullable LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId)
    
    
    public final OperationFuture<MulticloudDataTransferConfig,OperationMetadata> createMulticloudDataTransferConfigAsync(@Nullable LocationName parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MulticloudDataTransferConfig multicloudDataTransferConfig =
           MulticloudDataTransferConfig.newBuilder().build();
       String multicloudDataTransferConfigId = "multicloudDataTransferConfigId-1067608178";
       MulticloudDataTransferConfig response =
           dataTransferServiceClient
               .createMulticloudDataTransferConfigAsync(
                   parent, multicloudDataTransferConfig, multicloudDataTransferConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest request)
    
    
    public final OperationFuture<MulticloudDataTransferConfig,OperationMetadata> createMulticloudDataTransferConfigAsync(CreateMulticloudDataTransferConfigRequest request)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateMulticloudDataTransferConfigRequest request =
           CreateMulticloudDataTransferConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMulticloudDataTransferConfigId("multicloudDataTransferConfigId-1067608178")
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.createMulticloudDataTransferConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createMulticloudDataTransferConfigAsync(String parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId)
    
    
    public final OperationFuture<MulticloudDataTransferConfig,OperationMetadata> createMulticloudDataTransferConfigAsync(String parent, MulticloudDataTransferConfig multicloudDataTransferConfig, String multicloudDataTransferConfigId)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       MulticloudDataTransferConfig multicloudDataTransferConfig =
           MulticloudDataTransferConfig.newBuilder().build();
       String multicloudDataTransferConfigId = "multicloudDataTransferConfigId-1067608178";
       MulticloudDataTransferConfig response =
           dataTransferServiceClient
               .createMulticloudDataTransferConfigAsync(
                   parent, multicloudDataTransferConfig, multicloudDataTransferConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource.  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to create.  
`multicloudDataTransferConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the `MulticloudDataTransferConfig` resource, which becomes the final component of the `MulticloudDataTransferConfig` resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createMulticloudDataTransferConfigCallable()
    
    
    public final UnaryCallable<CreateMulticloudDataTransferConfigRequest,Operation> createMulticloudDataTransferConfigCallable()

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateMulticloudDataTransferConfigRequest request =
           CreateMulticloudDataTransferConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMulticloudDataTransferConfigId("multicloudDataTransferConfigId-1067608178")
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient
               .createMulticloudDataTransferConfigCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateMulticloudDataTransferConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMulticloudDataTransferConfigOperationCallable()
    
    
    public final OperationCallable<CreateMulticloudDataTransferConfigRequest,MulticloudDataTransferConfig,OperationMetadata> createMulticloudDataTransferConfigOperationCallable()

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       CreateMulticloudDataTransferConfigRequest request =
           CreateMulticloudDataTransferConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMulticloudDataTransferConfigId("multicloudDataTransferConfigId-1067608178")
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MulticloudDataTransferConfig, OperationMetadata> future =
           dataTransferServiceClient
               .createMulticloudDataTransferConfigOperationCallable()
               .futureCall(request);
       // Do something.
       MulticloudDataTransferConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateMulticloudDataTransferConfigRequest),[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteDestinationAsync(@Nullable DestinationName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDestinationAsync(@Nullable DestinationName name)

Deletes a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DestinationName name =
           DestinationName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
       dataTransferServiceClient.deleteDestinationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.DestinationName`  
Required. The name of the `Destination` resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteDestinationAsync(DeleteDestinationRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDestinationAsync(DeleteDestinationRequest request)

Deletes a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteDestinationRequest request =
           DeleteDestinationRequest.newBuilder()
               .setName(
                   DestinationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[MULTICLOUD_DATA_TRANSFER_CONFIG]",
                           "[DESTINATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       dataTransferServiceClient.deleteDestinationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteDestinationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteDestinationAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDestinationAsync(String name)

Deletes a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String name =
           DestinationName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]")
               .toString();
       dataTransferServiceClient.deleteDestinationAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Destination` resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteDestinationCallable()
    
    
    public final UnaryCallable<DeleteDestinationRequest,Operation> deleteDestinationCallable()

Deletes a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteDestinationRequest request =
           DeleteDestinationRequest.newBuilder()
               .setName(
                   DestinationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[MULTICLOUD_DATA_TRANSFER_CONFIG]",
                           "[DESTINATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient.deleteDestinationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteDestinationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDestinationOperationCallable()
    
    
    public final OperationCallable<DeleteDestinationRequest,Empty,OperationMetadata> deleteDestinationOperationCallable()

Deletes a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteDestinationRequest request =
           DeleteDestinationRequest.newBuilder()
               .setName(
                   DestinationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[MULTICLOUD_DATA_TRANSFER_CONFIG]",
                           "[DESTINATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataTransferServiceClient.deleteDestinationOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteDestinationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteMulticloudDataTransferConfigAsync(@Nullable MulticloudDataTransferConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMulticloudDataTransferConfigAsync(@Nullable MulticloudDataTransferConfigName name)

Deletes a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfigName name =
           MulticloudDataTransferConfigName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
       dataTransferServiceClient.deleteMulticloudDataTransferConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfigName`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMulticloudDataTransferConfigAsync(DeleteMulticloudDataTransferConfigRequest request)

Deletes a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteMulticloudDataTransferConfigRequest request =
           DeleteMulticloudDataTransferConfigRequest.newBuilder()
               .setName(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       dataTransferServiceClient.deleteMulticloudDataTransferConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteMulticloudDataTransferConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMulticloudDataTransferConfigAsync(String name)

Deletes a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String name =
           MulticloudDataTransferConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
               .toString();
       dataTransferServiceClient.deleteMulticloudDataTransferConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `MulticloudDataTransferConfig` resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteMulticloudDataTransferConfigCallable()
    
    
    public final UnaryCallable<DeleteMulticloudDataTransferConfigRequest,Operation> deleteMulticloudDataTransferConfigCallable()

Deletes a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteMulticloudDataTransferConfigRequest request =
           DeleteMulticloudDataTransferConfigRequest.newBuilder()
               .setName(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient
               .deleteMulticloudDataTransferConfigCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteMulticloudDataTransferConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMulticloudDataTransferConfigOperationCallable()
    
    
    public final OperationCallable<DeleteMulticloudDataTransferConfigRequest,Empty,OperationMetadata> deleteMulticloudDataTransferConfigOperationCallable()

Deletes a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DeleteMulticloudDataTransferConfigRequest request =
           DeleteMulticloudDataTransferConfigRequest.newBuilder()
               .setName(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataTransferServiceClient
               .deleteMulticloudDataTransferConfigOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteMulticloudDataTransferConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### getDestination(@Nullable DestinationName name)
    
    
    public final Destination getDestination(@Nullable DestinationName name)

Gets the details of a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       DestinationName name =
           DestinationName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]");
       Destination response = dataTransferServiceClient.getDestination(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.DestinationName`  
Required. The name of the `Destination` resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)` |   
  
### getDestination(GetDestinationRequest request)
    
    
    public final Destination getDestination(GetDestinationRequest request)

Gets the details of a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetDestinationRequest request =
           GetDestinationRequest.newBuilder()
               .setName(
                   DestinationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[MULTICLOUD_DATA_TRANSFER_CONFIG]",
                           "[DESTINATION]")
                       .toString())
               .build();
       Destination response = dataTransferServiceClient.getDestination(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetDestinationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)` |   
  
### getDestination(String name)
    
    
    public final Destination getDestination(String name)

Gets the details of a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String name =
           DestinationName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]", "[DESTINATION]")
               .toString();
       Destination response = dataTransferServiceClient.getDestination(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `Destination` resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)` |   
  
### getDestinationCallable()
    
    
    public final UnaryCallable<GetDestinationRequest,Destination> getDestinationCallable()

Gets the details of a `Destination` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetDestinationRequest request =
           GetDestinationRequest.newBuilder()
               .setName(
                   DestinationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[MULTICLOUD_DATA_TRANSFER_CONFIG]",
                           "[DESTINATION]")
                       .toString())
               .build();
       ApiFuture<Destination> future =
           dataTransferServiceClient.getDestinationCallable().futureCall(request);
       // Do something.
       Destination response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetDestinationRequest),[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataTransferServiceClient.getIamPolicy(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataTransferServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataTransferServiceClient.getLocation(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataTransferServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMulticloudDataTransferConfig(@Nullable MulticloudDataTransferConfigName name)
    
    
    public final MulticloudDataTransferConfig getMulticloudDataTransferConfig(@Nullable MulticloudDataTransferConfigName name)

Gets the details of a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfigName name =
           MulticloudDataTransferConfigName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.getMulticloudDataTransferConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfigName`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)` |   
  
### getMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request)
    
    
    public final MulticloudDataTransferConfig getMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request)

Gets the details of a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetMulticloudDataTransferConfigRequest request =
           GetMulticloudDataTransferConfigRequest.newBuilder()
               .setName(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .build();
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.getMulticloudDataTransferConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)` |   
  
### getMulticloudDataTransferConfig(String name)
    
    
    public final MulticloudDataTransferConfig getMulticloudDataTransferConfig(String name)

Gets the details of a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String name =
           MulticloudDataTransferConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
               .toString();
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.getMulticloudDataTransferConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `MulticloudDataTransferConfig` resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)` |   
  
### getMulticloudDataTransferConfigCallable()
    
    
    public final UnaryCallable<GetMulticloudDataTransferConfigRequest,MulticloudDataTransferConfig> getMulticloudDataTransferConfigCallable()

Gets the details of a `MulticloudDataTransferConfig` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetMulticloudDataTransferConfigRequest request =
           GetMulticloudDataTransferConfigRequest.newBuilder()
               .setName(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .build();
       ApiFuture<MulticloudDataTransferConfig> future =
           dataTransferServiceClient.getMulticloudDataTransferConfigCallable().futureCall(request);
       // Do something.
       MulticloudDataTransferConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetMulticloudDataTransferConfigRequest),[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)>` |   
  
### getMulticloudDataTransferSupportedService(@Nullable MulticloudDataTransferSupportedServiceName name)
    
    
    public final MulticloudDataTransferSupportedService getMulticloudDataTransferSupportedService(@Nullable MulticloudDataTransferSupportedServiceName name)

Gets the details of a service that is supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferSupportedServiceName name =
           MulticloudDataTransferSupportedServiceName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]");
       MulticloudDataTransferSupportedService response =
           dataTransferServiceClient.getMulticloudDataTransferSupportedService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedServiceName`  
Required. The name of the service.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService)` |   
  
### getMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request)
    
    
    public final MulticloudDataTransferSupportedService getMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request)

Gets the details of a service that is supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetMulticloudDataTransferSupportedServiceRequest request =
           GetMulticloudDataTransferSupportedServiceRequest.newBuilder()
               .setName(
                   MulticloudDataTransferSupportedServiceName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]")
                       .toString())
               .build();
       MulticloudDataTransferSupportedService response =
           dataTransferServiceClient.getMulticloudDataTransferSupportedService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetMulticloudDataTransferSupportedServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService)` |   
  
### getMulticloudDataTransferSupportedService(String name)
    
    
    public final MulticloudDataTransferSupportedService getMulticloudDataTransferSupportedService(String name)

Gets the details of a service that is supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String name =
           MulticloudDataTransferSupportedServiceName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]")
               .toString();
       MulticloudDataTransferSupportedService response =
           dataTransferServiceClient.getMulticloudDataTransferSupportedService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the service.  
**Returns**  
---  
**Type** | **Description**  
`[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService)` |   
  
### getMulticloudDataTransferSupportedServiceCallable()
    
    
    public final UnaryCallable<GetMulticloudDataTransferSupportedServiceRequest,MulticloudDataTransferSupportedService> getMulticloudDataTransferSupportedServiceCallable()

Gets the details of a service that is supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       GetMulticloudDataTransferSupportedServiceRequest request =
           GetMulticloudDataTransferSupportedServiceRequest.newBuilder()
               .setName(
                   MulticloudDataTransferSupportedServiceName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICE]")
                       .toString())
               .build();
       ApiFuture<MulticloudDataTransferSupportedService> future =
           dataTransferServiceClient
               .getMulticloudDataTransferSupportedServiceCallable()
               .futureCall(request);
       // Do something.
       MulticloudDataTransferSupportedService response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetMulticloudDataTransferSupportedServiceRequest),[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferSupportedService)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DataTransferServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.DataTransferServiceSettings` |   
  
### getStub()
    
    
    public DataTransferServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.DataTransferServiceStub)` |   
  
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
  
### listDestinations(@Nullable MulticloudDataTransferConfigName parent)
    
    
    public final DataTransferServiceClient.ListDestinationsPagedResponse listDestinations(@Nullable MulticloudDataTransferConfigName parent)

Lists the `Destination` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfigName parent =
           MulticloudDataTransferConfigName.of(
               "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]");
       for (Destination element : dataTransferServiceClient.listDestinations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfigName`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListDestinationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListDestinationsPagedResponse)` |   
  
### listDestinations(ListDestinationsRequest request)
    
    
    public final DataTransferServiceClient.ListDestinationsPagedResponse listDestinations(ListDestinationsRequest request)

Lists the `Destination` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListDestinationsRequest request =
           ListDestinationsRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       for (Destination element : dataTransferServiceClient.listDestinations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDestinationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListDestinationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListDestinationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListDestinationsPagedResponse)` |   
  
### listDestinations(String parent)
    
    
    public final DataTransferServiceClient.ListDestinationsPagedResponse listDestinations(String parent)

Lists the `Destination` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String parent =
           MulticloudDataTransferConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
               .toString();
       for (Destination element : dataTransferServiceClient.listDestinations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListDestinationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListDestinationsPagedResponse)` |   
  
### listDestinationsCallable()
    
    
    public final UnaryCallable<ListDestinationsRequest,ListDestinationsResponse> listDestinationsCallable()

Lists the `Destination` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListDestinationsRequest request =
           ListDestinationsRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListDestinationsResponse response =
             dataTransferServiceClient.listDestinationsCallable().call(request);
         for (Destination element : response.getDestinationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDestinationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListDestinationsRequest),[ListDestinationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListDestinationsResponse)>` |   
  
### listDestinationsPagedCallable()
    
    
    public final UnaryCallable<ListDestinationsRequest,DataTransferServiceClient.ListDestinationsPagedResponse> listDestinationsPagedCallable()

Lists the `Destination` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListDestinationsRequest request =
           ListDestinationsRequest.newBuilder()
               .setParent(
                   MulticloudDataTransferConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[MULTICLOUD_DATA_TRANSFER_CONFIG]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<Destination> future =
           dataTransferServiceClient.listDestinationsPagedCallable().futureCall(request);
       // Do something.
       for (Destination element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDestinationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListDestinationsRequest),[ListDestinationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListDestinationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataTransferServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataTransferServiceClient.listLocations(request).iterateAll()) {
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
`[DataTransferServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataTransferServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataTransferServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataTransferServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListLocationsPagedResponse)>` |   
  
### listMulticloudDataTransferConfigs(@Nullable LocationName parent)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse listMulticloudDataTransferConfigs(@Nullable LocationName parent)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MulticloudDataTransferConfig element :
           dataTransferServiceClient.listMulticloudDataTransferConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse)` |   
  
### listMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse listMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferConfigsRequest request =
           ListMulticloudDataTransferConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       for (MulticloudDataTransferConfig element :
           dataTransferServiceClient.listMulticloudDataTransferConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse)` |   
  
### listMulticloudDataTransferConfigs(String parent)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse listMulticloudDataTransferConfigs(String parent)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MulticloudDataTransferConfig element :
           dataTransferServiceClient.listMulticloudDataTransferConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse)` |   
  
### listMulticloudDataTransferConfigsCallable()
    
    
    public final UnaryCallable<ListMulticloudDataTransferConfigsRequest,ListMulticloudDataTransferConfigsResponse> listMulticloudDataTransferConfigsCallable()

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferConfigsRequest request =
           ListMulticloudDataTransferConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListMulticloudDataTransferConfigsResponse response =
             dataTransferServiceClient.listMulticloudDataTransferConfigsCallable().call(request);
         for (MulticloudDataTransferConfig element :
             response.getMulticloudDataTransferConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsRequest),[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsResponse)>` |   
  
### listMulticloudDataTransferConfigsPagedCallable()
    
    
    public final UnaryCallable<ListMulticloudDataTransferConfigsRequest,DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse> listMulticloudDataTransferConfigsPagedCallable()

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferConfigsRequest request =
           ListMulticloudDataTransferConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<MulticloudDataTransferConfig> future =
           dataTransferServiceClient
               .listMulticloudDataTransferConfigsPagedCallable()
               .futureCall(request);
       // Do something.
       for (MulticloudDataTransferConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferConfigsRequest),[ListMulticloudDataTransferConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferConfigsPagedResponse)>` |   
  
### listMulticloudDataTransferSupportedServices(@Nullable LocationName parent)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse listMulticloudDataTransferSupportedServices(@Nullable LocationName parent)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MulticloudDataTransferSupportedService element :
           dataTransferServiceClient
               .listMulticloudDataTransferSupportedServices(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse)` |   
  
### listMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse listMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferSupportedServicesRequest request =
           ListMulticloudDataTransferSupportedServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MulticloudDataTransferSupportedService element :
           dataTransferServiceClient
               .listMulticloudDataTransferSupportedServices(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse)` |   
  
### listMulticloudDataTransferSupportedServices(String parent)
    
    
    public final DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse listMulticloudDataTransferSupportedServices(String parent)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MulticloudDataTransferSupportedService element :
           dataTransferServiceClient
               .listMulticloudDataTransferSupportedServices(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse)` |   
  
### listMulticloudDataTransferSupportedServicesCallable()
    
    
    public final UnaryCallable<ListMulticloudDataTransferSupportedServicesRequest,ListMulticloudDataTransferSupportedServicesResponse> listMulticloudDataTransferSupportedServicesCallable()

Lists the services in the project for a region that are supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferSupportedServicesRequest request =
           ListMulticloudDataTransferSupportedServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMulticloudDataTransferSupportedServicesResponse response =
             dataTransferServiceClient
                 .listMulticloudDataTransferSupportedServicesCallable()
                 .call(request);
         for (MulticloudDataTransferSupportedService element :
             response.getMulticloudDataTransferSupportedServicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesRequest),[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesResponse)>` |   
  
### listMulticloudDataTransferSupportedServicesPagedCallable()
    
    
    public final UnaryCallable<ListMulticloudDataTransferSupportedServicesRequest,DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse> listMulticloudDataTransferSupportedServicesPagedCallable()

Lists the services in the project for a region that are supported for Data Transfer Essentials.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       ListMulticloudDataTransferSupportedServicesRequest request =
           ListMulticloudDataTransferSupportedServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MulticloudDataTransferSupportedService> future =
           dataTransferServiceClient
               .listMulticloudDataTransferSupportedServicesPagedCallable()
               .futureCall(request);
       // Do something.
       for (MulticloudDataTransferSupportedService element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListMulticloudDataTransferSupportedServicesRequest),[ListMulticloudDataTransferSupportedServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DataTransferServiceClient.ListMulticloudDataTransferSupportedServicesPagedResponse)>` |   
  
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataTransferServiceClient.setIamPolicy(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataTransferServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataTransferServiceClient.testIamPermissions(request);
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
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataTransferServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDestinationAsync(Destination destination, FieldMask updateMask)
    
    
    public final OperationFuture<Destination,OperationMetadata> updateDestinationAsync(Destination destination, FieldMask updateMask)

Updates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       Destination destination = Destination.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Destination response =
           dataTransferServiceClient.updateDestinationAsync(destination, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`destination` | `[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination)`  
Required. The `Destination` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. `FieldMask is used to specify the fields to be overwritten in the `Destination` resource by the update. The fields specified in `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateDestinationAsync(UpdateDestinationRequest request)
    
    
    public final OperationFuture<Destination,OperationMetadata> updateDestinationAsync(UpdateDestinationRequest request)

Updates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateDestinationRequest request =
           UpdateDestinationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Destination response = dataTransferServiceClient.updateDestinationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateDestinationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateDestinationCallable()
    
    
    public final UnaryCallable<UpdateDestinationRequest,Operation> updateDestinationCallable()

Updates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateDestinationRequest request =
           UpdateDestinationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient.updateDestinationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateDestinationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDestinationOperationCallable()
    
    
    public final OperationCallable<UpdateDestinationRequest,Destination,OperationMetadata> updateDestinationOperationCallable()

Updates a `Destination` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateDestinationRequest request =
           UpdateDestinationRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDestination(Destination.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Destination, OperationMetadata> future =
           dataTransferServiceClient.updateDestinationOperationCallable().futureCall(request);
       // Do something.
       Destination response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateDestinationRequest),[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Destination),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask)
    
    
    public final OperationFuture<MulticloudDataTransferConfig,OperationMetadata> updateMulticloudDataTransferConfigAsync(MulticloudDataTransferConfig multicloudDataTransferConfig, FieldMask updateMask)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       MulticloudDataTransferConfig multicloudDataTransferConfig =
           MulticloudDataTransferConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MulticloudDataTransferConfig response =
           dataTransferServiceClient
               .updateMulticloudDataTransferConfigAsync(multicloudDataTransferConfig, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`multicloudDataTransferConfig` | `[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig)`  
Required. The `MulticloudDataTransferConfig` resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. `FieldMask` is used to specify the fields in the `MulticloudDataTransferConfig` resource to be overwritten by the update. The fields specified in `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't specify a mask, all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest request)
    
    
    public final OperationFuture<MulticloudDataTransferConfig,OperationMetadata> updateMulticloudDataTransferConfigAsync(UpdateMulticloudDataTransferConfigRequest request)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateMulticloudDataTransferConfigRequest request =
           UpdateMulticloudDataTransferConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MulticloudDataTransferConfig response =
           dataTransferServiceClient.updateMulticloudDataTransferConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateMulticloudDataTransferConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateMulticloudDataTransferConfigCallable()
    
    
    public final UnaryCallable<UpdateMulticloudDataTransferConfigRequest,Operation> updateMulticloudDataTransferConfigCallable()

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateMulticloudDataTransferConfigRequest request =
           UpdateMulticloudDataTransferConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataTransferServiceClient
               .updateMulticloudDataTransferConfigCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateMulticloudDataTransferConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMulticloudDataTransferConfigOperationCallable()
    
    
    public final OperationCallable<UpdateMulticloudDataTransferConfigRequest,MulticloudDataTransferConfig,OperationMetadata> updateMulticloudDataTransferConfigOperationCallable()

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTransferServiceClient dataTransferServiceClient = DataTransferServiceClient.create()) {
       UpdateMulticloudDataTransferConfigRequest request =
           UpdateMulticloudDataTransferConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMulticloudDataTransferConfig(MulticloudDataTransferConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MulticloudDataTransferConfig, OperationMetadata> future =
           dataTransferServiceClient
               .updateMulticloudDataTransferConfigOperationCallable()
               .futureCall(request);
       // Do something.
       MulticloudDataTransferConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateMulticloudDataTransferConfigRequest),[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.MulticloudDataTransferConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
