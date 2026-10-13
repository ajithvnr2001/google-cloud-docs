---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient
title: Class RegionAutoscalersClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:27.881801+00:00
---

# Class RegionAutoscalersClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionAutoscalersClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionAutoscalersClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionAutoscalers API.

This client uses RegionAutoscalers version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String autoscaler = "autoscaler517258967";
       Autoscaler response = regionAutoscalersClient.get(project, region, autoscaler);
     }
     

Note: close() needs to be called on the RegionAutoscalersClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified autoscaler. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String autoscaler) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified autoscaler. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionAutoscalerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String autoscaler) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates an autoscaler in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of autoscalers contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionAutoscalersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionAutoscalerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates an autoscaler in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateRegionAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String region, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionAutoscalersSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionAutoscalersSettings regionAutoscalersSettings =
         RegionAutoscalersSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionAutoscalersClient regionAutoscalersClient =
         RegionAutoscalersClient.create(regionAutoscalersSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionAutoscalersSettings regionAutoscalersSettings =
         RegionAutoscalersSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionAutoscalersClient regionAutoscalersClient =
         RegionAutoscalersClient.create(regionAutoscalersSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionAutoscalersClient

## Static Methods 

### create()
    
    
    public static final RegionAutoscalersClient create()

Constructs an instance of RegionAutoscalersClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionAutoscalersSettings settings)
    
    
    public static final RegionAutoscalersClient create(RegionAutoscalersSettings settings)

Constructs an instance of RegionAutoscalersClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionAutoscalersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionAutoscalersStub stub)
    
    
    public static final RegionAutoscalersClient create(RegionAutoscalersStub stub)

Constructs an instance of RegionAutoscalersClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionAutoscalersSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionAutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionAutoscalersStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient)` |   
  
## Constructors 

### RegionAutoscalersClient(RegionAutoscalersSettings settings)
    
    
    protected RegionAutoscalersClient(RegionAutoscalersSettings settings)

Constructs an instance of RegionAutoscalersClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionAutoscalersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersSettings)`  
  
  
### RegionAutoscalersClient(RegionAutoscalersStub stub)
    
    
    protected RegionAutoscalersClient(RegionAutoscalersStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionAutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionAutoscalersStub)`  
  
  
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

### deleteAsync(DeleteRegionAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionAutoscalerRequest request)

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       DeleteRegionAutoscalerRequest request =
           DeleteRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionAutoscalersClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String autoscaler)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String autoscaler)

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String autoscaler = "autoscaler517258967";
       Operation response = regionAutoscalersClient.deleteAsync(project, region, autoscaler).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`autoscaler` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the autoscaler to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionAutoscalerRequest,Operation> deleteCallable()

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       DeleteRegionAutoscalerRequest request =
           DeleteRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionAutoscalersClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionAutoscalerRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       DeleteRegionAutoscalerRequest request =
           DeleteRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionAutoscalersClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionAutoscalerRequest request)
    
    
    public final Autoscaler get(GetRegionAutoscalerRequest request)

Returns the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       GetRegionAutoscalerRequest request =
           GetRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       Autoscaler response = regionAutoscalersClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)` |   
  
### get(String project, String region, String autoscaler)
    
    
    public final Autoscaler get(String project, String region, String autoscaler)

Returns the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String autoscaler = "autoscaler517258967";
       Autoscaler response = regionAutoscalersClient.get(project, region, autoscaler);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`autoscaler` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the autoscaler to return.  
**Returns**  
---  
**Type** | **Description**  
`[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionAutoscalerRequest,Autoscaler> getCallable()

Returns the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       GetRegionAutoscalerRequest request =
           GetRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Autoscaler> future = regionAutoscalersClient.getCallable().futureCall(request);
       // Do something.
       Autoscaler response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionAutoscalerRequest),[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionAutoscalersSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionAutoscalersSettings` |   
  
### getStub()
    
    
    public RegionAutoscalersStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionAutoscalersStub)` |   
  
### insertAsync(InsertRegionAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionAutoscalerRequest request)

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       InsertRegionAutoscalerRequest request =
           InsertRegionAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionAutoscalersClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, Autoscaler autoscalerResource)

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response =
           regionAutoscalersClient.insertAsync(project, region, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionAutoscalerRequest,Operation> insertCallable()

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       InsertRegionAutoscalerRequest request =
           InsertRegionAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionAutoscalersClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionAutoscalerRequest,Operation,Operation> insertOperationCallable()

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       InsertRegionAutoscalerRequest request =
           InsertRegionAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionAutoscalersClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionAutoscalersRequest request)
    
    
    public final RegionAutoscalersClient.ListPagedResponse list(ListRegionAutoscalersRequest request)

Retrieves a list of autoscalers contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       ListRegionAutoscalersRequest request =
           ListRegionAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (Autoscaler element : regionAutoscalersClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionAutoscalersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionAutoscalersClient.ListPagedResponse list(String project, String region)

Retrieves a list of autoscalers contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (Autoscaler element : regionAutoscalersClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionAutoscalersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionAutoscalersRequest,RegionAutoscalerList> listCallable()

Retrieves a list of autoscalers contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       ListRegionAutoscalersRequest request =
           ListRegionAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionAutoscalerList response = regionAutoscalersClient.listCallable().call(request);
         for (Autoscaler element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionAutoscalersRequest),[RegionAutoscalerList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalerList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionAutoscalersRequest,RegionAutoscalersClient.ListPagedResponse> listPagedCallable()

Retrieves a list of autoscalers contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       ListRegionAutoscalersRequest request =
           ListRegionAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Autoscaler> future =
           regionAutoscalersClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Autoscaler element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionAutoscalersRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionAutoscalersClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionAutoscalerRequest request)

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       PatchRegionAutoscalerRequest request =
           PatchRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionAutoscalersClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, Autoscaler autoscalerResource)

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response =
           regionAutoscalersClient.patchAsync(project, region, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionAutoscalerRequest,Operation> patchCallable()

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       PatchRegionAutoscalerRequest request =
           PatchRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionAutoscalersClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionAutoscalerRequest,Operation,Operation> patchOperationCallable()

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       PatchRegionAutoscalerRequest request =
           PatchRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionAutoscalersClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionAutoscalerRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionAutoscalerRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       TestIamPermissionsRegionAutoscalerRequest request =
           TestIamPermissionsRegionAutoscalerRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = regionAutoscalersClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionAutoscalersClient.testIamPermissions(
               project, region, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRegionAutoscalerRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       TestIamPermissionsRegionAutoscalerRequest request =
           TestIamPermissionsRegionAutoscalerRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionAutoscalersClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionAutoscalerRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateRegionAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateRegionAutoscalerRequest request)

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       UpdateRegionAutoscalerRequest request =
           UpdateRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionAutoscalersClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String region, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String region, Autoscaler autoscalerResource)

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response =
           regionAutoscalersClient.updateAsync(project, region, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateRegionAutoscalerRequest,Operation> updateCallable()

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       UpdateRegionAutoscalerRequest request =
           UpdateRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionAutoscalersClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateRegionAutoscalerRequest,Operation,Operation> updateOperationCallable()

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionAutoscalersClient regionAutoscalersClient = RegionAutoscalersClient.create()) {
       UpdateRegionAutoscalerRequest request =
           UpdateRegionAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionAutoscalersClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRegionAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
