---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient
title: Class ExternalVpnGatewaysClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:10.483369+00:00
---

# Class ExternalVpnGatewaysClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ExternalVpnGatewaysClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ExternalVpnGatewaysClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ExternalVpnGateways API.

This client uses ExternalVpnGateways version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       String externalVpnGateway = "externalVpnGateway-1140582181";
       ExternalVpnGateway response = externalVpnGatewaysClient.get(project, externalVpnGateway);
     }
     

Note: close() needs to be called on the ExternalVpnGatewaysClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified externalVpnGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteExternalVpnGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String externalVpnGateway) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetExternalVpnGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String externalVpnGateway) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a ExternalVpnGateway in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertExternalVpnGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, ExternalVpnGateway externalVpnGatewayResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of ExternalVpnGateway available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListExternalVpnGatewaysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetLabels |  Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsExternalVpnGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsExternalVpnGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ExternalVpnGatewaysSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ExternalVpnGatewaysSettings externalVpnGatewaysSettings =
         ExternalVpnGatewaysSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ExternalVpnGatewaysClient externalVpnGatewaysClient =
         ExternalVpnGatewaysClient.create(externalVpnGatewaysSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ExternalVpnGatewaysSettings externalVpnGatewaysSettings =
         ExternalVpnGatewaysSettings.newBuilder().setEndpoint(myEndpoint).build();
     ExternalVpnGatewaysClient externalVpnGatewaysClient =
         ExternalVpnGatewaysClient.create(externalVpnGatewaysSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ExternalVpnGatewaysClient

## Static Methods 

### create()
    
    
    public static final ExternalVpnGatewaysClient create()

Constructs an instance of ExternalVpnGatewaysClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ExternalVpnGatewaysSettings settings)
    
    
    public static final ExternalVpnGatewaysClient create(ExternalVpnGatewaysSettings settings)

Constructs an instance of ExternalVpnGatewaysClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ExternalVpnGatewaysSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ExternalVpnGatewaysStub stub)
    
    
    public static final ExternalVpnGatewaysClient create(ExternalVpnGatewaysStub stub)

Constructs an instance of ExternalVpnGatewaysClient, using the given stub for making calls. This is for advanced usage - prefer using create(ExternalVpnGatewaysSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ExternalVpnGatewaysStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ExternalVpnGatewaysStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient)` |   
  
## Constructors 

### ExternalVpnGatewaysClient(ExternalVpnGatewaysSettings settings)
    
    
    protected ExternalVpnGatewaysClient(ExternalVpnGatewaysSettings settings)

Constructs an instance of ExternalVpnGatewaysClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ExternalVpnGatewaysSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysSettings)`  
  
  
### ExternalVpnGatewaysClient(ExternalVpnGatewaysStub stub)
    
    
    protected ExternalVpnGatewaysClient(ExternalVpnGatewaysStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ExternalVpnGatewaysStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ExternalVpnGatewaysStub)`  
  
  
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

### deleteAsync(DeleteExternalVpnGatewayRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteExternalVpnGatewayRequest request)

Deletes the specified externalVpnGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       DeleteExternalVpnGatewayRequest request =
           DeleteExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGateway("externalVpnGateway-1140582181")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = externalVpnGatewaysClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String externalVpnGateway)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String externalVpnGateway)

Deletes the specified externalVpnGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       String externalVpnGateway = "externalVpnGateway-1140582181";
       Operation response = externalVpnGatewaysClient.deleteAsync(project, externalVpnGateway).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`externalVpnGateway` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the externalVpnGateways to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteExternalVpnGatewayRequest,Operation> deleteCallable()

Deletes the specified externalVpnGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       DeleteExternalVpnGatewayRequest request =
           DeleteExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGateway("externalVpnGateway-1140582181")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = externalVpnGatewaysClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteExternalVpnGatewayRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified externalVpnGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       DeleteExternalVpnGatewayRequest request =
           DeleteExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGateway("externalVpnGateway-1140582181")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           externalVpnGatewaysClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetExternalVpnGatewayRequest request)
    
    
    public final ExternalVpnGateway get(GetExternalVpnGatewayRequest request)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       GetExternalVpnGatewayRequest request =
           GetExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGateway("externalVpnGateway-1140582181")
               .setProject("project-309310695")
               .build();
       ExternalVpnGateway response = externalVpnGatewaysClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGateway)` |   
  
### get(String project, String externalVpnGateway)
    
    
    public final ExternalVpnGateway get(String project, String externalVpnGateway)

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       String externalVpnGateway = "externalVpnGateway-1140582181";
       ExternalVpnGateway response = externalVpnGatewaysClient.get(project, externalVpnGateway);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`externalVpnGateway` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the externalVpnGateway to return.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGateway)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetExternalVpnGatewayRequest,ExternalVpnGateway> getCallable()

Returns the specified externalVpnGateway. Get a list of available externalVpnGateways by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       GetExternalVpnGatewayRequest request =
           GetExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGateway("externalVpnGateway-1140582181")
               .setProject("project-309310695")
               .build();
       ApiFuture<ExternalVpnGateway> future =
           externalVpnGatewaysClient.getCallable().futureCall(request);
       // Do something.
       ExternalVpnGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetExternalVpnGatewayRequest),[ExternalVpnGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGateway)>` |   
  
### getSettings()
    
    
    public final @Nullable ExternalVpnGatewaysSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ExternalVpnGatewaysSettings` |   
  
### getStub()
    
    
    public ExternalVpnGatewaysStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ExternalVpnGatewaysStub)` |   
  
### insertAsync(InsertExternalVpnGatewayRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertExternalVpnGatewayRequest request)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       InsertExternalVpnGatewayRequest request =
           InsertExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGatewayResource(ExternalVpnGateway.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = externalVpnGatewaysClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, ExternalVpnGateway externalVpnGatewayResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, ExternalVpnGateway externalVpnGatewayResource)

Creates a ExternalVpnGateway in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       ExternalVpnGateway externalVpnGatewayResource = ExternalVpnGateway.newBuilder().build();
       Operation response =
           externalVpnGatewaysClient.insertAsync(project, externalVpnGatewayResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`externalVpnGatewayResource` | `[ExternalVpnGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGateway)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertExternalVpnGatewayRequest,Operation> insertCallable()

Creates a ExternalVpnGateway in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       InsertExternalVpnGatewayRequest request =
           InsertExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGatewayResource(ExternalVpnGateway.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = externalVpnGatewaysClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertExternalVpnGatewayRequest,Operation,Operation> insertOperationCallable()

Creates a ExternalVpnGateway in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       InsertExternalVpnGatewayRequest request =
           InsertExternalVpnGatewayRequest.newBuilder()
               .setExternalVpnGatewayResource(ExternalVpnGateway.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           externalVpnGatewaysClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListExternalVpnGatewaysRequest request)
    
    
    public final ExternalVpnGatewaysClient.ListPagedResponse list(ListExternalVpnGatewaysRequest request)

Retrieves the list of ExternalVpnGateway available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       ListExternalVpnGatewaysRequest request =
           ListExternalVpnGatewaysRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (ExternalVpnGateway element : externalVpnGatewaysClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExternalVpnGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListExternalVpnGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final ExternalVpnGatewaysClient.ListPagedResponse list(String project)

Retrieves the list of ExternalVpnGateway available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       for (ExternalVpnGateway element : externalVpnGatewaysClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalVpnGatewaysClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListExternalVpnGatewaysRequest,ExternalVpnGatewayList> listCallable()

Retrieves the list of ExternalVpnGateway available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       ListExternalVpnGatewaysRequest request =
           ListExternalVpnGatewaysRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         ExternalVpnGatewayList response = externalVpnGatewaysClient.listCallable().call(request);
         for (ExternalVpnGateway element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalVpnGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListExternalVpnGatewaysRequest),[ExternalVpnGatewayList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewayList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListExternalVpnGatewaysRequest,ExternalVpnGatewaysClient.ListPagedResponse> listPagedCallable()

Retrieves the list of ExternalVpnGateway available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       ListExternalVpnGatewaysRequest request =
           ListExternalVpnGatewaysRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<ExternalVpnGateway> future =
           externalVpnGatewaysClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ExternalVpnGateway element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExternalVpnGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListExternalVpnGatewaysRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExternalVpnGatewaysClient.ListPagedResponse)>` |   
  
### setLabelsAsync(SetLabelsExternalVpnGatewayRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsExternalVpnGatewayRequest request)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       SetLabelsExternalVpnGatewayRequest request =
           SetLabelsExternalVpnGatewayRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Operation response = externalVpnGatewaysClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetLabelsRequest globalSetLabelsRequestResource =
           GlobalSetLabelsRequest.newBuilder().build();
       Operation response =
           externalVpnGatewaysClient
               .setLabelsAsync(project, resource, globalSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsExternalVpnGatewayRequest,Operation> setLabelsCallable()

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       SetLabelsExternalVpnGatewayRequest request =
           SetLabelsExternalVpnGatewayRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future =
           externalVpnGatewaysClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsExternalVpnGatewayRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on an ExternalVpnGateway. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       SetLabelsExternalVpnGatewayRequest request =
           SetLabelsExternalVpnGatewayRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           externalVpnGatewaysClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsExternalVpnGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsExternalVpnGatewayRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsExternalVpnGatewayRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       TestIamPermissionsExternalVpnGatewayRequest request =
           TestIamPermissionsExternalVpnGatewayRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = externalVpnGatewaysClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsExternalVpnGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           externalVpnGatewaysClient.testIamPermissions(
               project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsExternalVpnGatewayRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExternalVpnGatewaysClient externalVpnGatewaysClient = ExternalVpnGatewaysClient.create()) {
       TestIamPermissionsExternalVpnGatewayRequest request =
           TestIamPermissionsExternalVpnGatewayRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           externalVpnGatewaysClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsExternalVpnGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsExternalVpnGatewayRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
