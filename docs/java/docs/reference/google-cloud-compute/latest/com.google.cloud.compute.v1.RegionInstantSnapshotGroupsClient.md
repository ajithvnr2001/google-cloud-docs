---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient
title: Class RegionInstantSnapshotGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:46.617117+00:00
---

# Class RegionInstantSnapshotGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionInstantSnapshotGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionInstantSnapshotGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionInstantSnapshotGroups API.

This client uses RegionInstantSnapshotGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instantSnapshotGroup = "instantSnapshotGroup500796090";
       InstantSnapshotGroup response =
           regionInstantSnapshotGroupsClient.get(project, region, instantSnapshotGroup);
     }
     

Note: close() needs to be called on the RegionInstantSnapshotGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  deletes a Regional InstantSnapshotGroup resource |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionInstantSnapshotGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String instantSnapshotGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  returns the specified InstantSnapshotGroup resource in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionInstantSnapshotGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String instantSnapshotGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRegionInstantSnapshotGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String region, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  creates a Regional InstantSnapshotGroup resource |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionInstantSnapshotGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, InstantSnapshotGroup instantSnapshotGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  retrieves the list of InstantSnapshotGroup resources contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionInstantSnapshotGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRegionInstantSnapshotGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionInstantSnapshotGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionInstantSnapshotGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstantSnapshotGroupsSettings regionInstantSnapshotGroupsSettings =
         RegionInstantSnapshotGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create(regionInstantSnapshotGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstantSnapshotGroupsSettings regionInstantSnapshotGroupsSettings =
         RegionInstantSnapshotGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create(regionInstantSnapshotGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionInstantSnapshotGroupsClient

## Static Methods 

### create()
    
    
    public static final RegionInstantSnapshotGroupsClient create()

Constructs an instance of RegionInstantSnapshotGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstantSnapshotGroupsSettings settings)
    
    
    public static final RegionInstantSnapshotGroupsClient create(RegionInstantSnapshotGroupsSettings settings)

Constructs an instance of RegionInstantSnapshotGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstantSnapshotGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstantSnapshotGroupsStub stub)
    
    
    public static final RegionInstantSnapshotGroupsClient create(RegionInstantSnapshotGroupsStub stub)

Constructs an instance of RegionInstantSnapshotGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionInstantSnapshotGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstantSnapshotGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstantSnapshotGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient)` |   
  
## Constructors 

### RegionInstantSnapshotGroupsClient(RegionInstantSnapshotGroupsSettings settings)
    
    
    protected RegionInstantSnapshotGroupsClient(RegionInstantSnapshotGroupsSettings settings)

Constructs an instance of RegionInstantSnapshotGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstantSnapshotGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsSettings)`  
  
  
### RegionInstantSnapshotGroupsClient(RegionInstantSnapshotGroupsStub stub)
    
    
    protected RegionInstantSnapshotGroupsClient(RegionInstantSnapshotGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstantSnapshotGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstantSnapshotGroupsStub)`  
  
  
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

### deleteAsync(DeleteRegionInstantSnapshotGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionInstantSnapshotGroupRequest request)

deletes a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       DeleteRegionInstantSnapshotGroupRequest request =
           DeleteRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroup("instantSnapshotGroup500796090")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstantSnapshotGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstantSnapshotGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String instantSnapshotGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String instantSnapshotGroup)

deletes a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instantSnapshotGroup = "instantSnapshotGroup500796090";
       Operation response =
           regionInstantSnapshotGroupsClient
               .deleteAsync(project, region, instantSnapshotGroup)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`instantSnapshotGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InstantSnapshotGroup resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionInstantSnapshotGroupRequest,Operation> deleteCallable()

deletes a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       DeleteRegionInstantSnapshotGroupRequest request =
           DeleteRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroup("instantSnapshotGroup500796090")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstantSnapshotGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstantSnapshotGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionInstantSnapshotGroupRequest,Operation,Operation> deleteOperationCallable()

deletes a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       DeleteRegionInstantSnapshotGroupRequest request =
           DeleteRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroup("instantSnapshotGroup500796090")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstantSnapshotGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstantSnapshotGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionInstantSnapshotGroupRequest request)
    
    
    public final InstantSnapshotGroup get(GetRegionInstantSnapshotGroupRequest request)

returns the specified InstantSnapshotGroup resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       GetRegionInstantSnapshotGroupRequest request =
           GetRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroup("instantSnapshotGroup500796090")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       InstantSnapshotGroup response = regionInstantSnapshotGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstantSnapshotGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotGroup)` |   
  
### get(String project, String region, String instantSnapshotGroup)
    
    
    public final InstantSnapshotGroup get(String project, String region, String instantSnapshotGroup)

returns the specified InstantSnapshotGroup resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instantSnapshotGroup = "instantSnapshotGroup500796090";
       InstantSnapshotGroup response =
           regionInstantSnapshotGroupsClient.get(project, region, instantSnapshotGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`instantSnapshotGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InstantSnapshotGroup resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionInstantSnapshotGroupRequest,InstantSnapshotGroup> getCallable()

returns the specified InstantSnapshotGroup resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       GetRegionInstantSnapshotGroupRequest request =
           GetRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroup("instantSnapshotGroup500796090")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstantSnapshotGroup> future =
           regionInstantSnapshotGroupsClient.getCallable().futureCall(request);
       // Do something.
       InstantSnapshotGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstantSnapshotGroupRequest),[InstantSnapshotGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotGroup)>` |   
  
### getIamPolicy(GetIamPolicyRegionInstantSnapshotGroupRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRegionInstantSnapshotGroupRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       GetIamPolicyRegionInstantSnapshotGroupRequest request =
           GetIamPolicyRegionInstantSnapshotGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       Policy response = regionInstantSnapshotGroupsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionInstantSnapshotGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String region, String resource)
    
    
    public final Policy getIamPolicy(String project, String region, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       Policy response = regionInstantSnapshotGroupsClient.getIamPolicy(project, region, resource);
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
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRegionInstantSnapshotGroupRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       GetIamPolicyRegionInstantSnapshotGroupRequest request =
           GetIamPolicyRegionInstantSnapshotGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           regionInstantSnapshotGroupsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionInstantSnapshotGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionInstantSnapshotGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionInstantSnapshotGroupsSettings` |   
  
### getStub()
    
    
    public RegionInstantSnapshotGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstantSnapshotGroupsStub)` |   
  
### insertAsync(InsertRegionInstantSnapshotGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionInstantSnapshotGroupRequest request)

creates a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       InsertRegionInstantSnapshotGroupRequest request =
           InsertRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroupResource(InstantSnapshotGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceConsistencyGroup("sourceConsistencyGroup-2056893054")
               .build();
       Operation response = regionInstantSnapshotGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstantSnapshotGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, InstantSnapshotGroup instantSnapshotGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, InstantSnapshotGroup instantSnapshotGroupResource)

creates a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       InstantSnapshotGroup instantSnapshotGroupResource = InstantSnapshotGroup.newBuilder().build();
       Operation response =
           regionInstantSnapshotGroupsClient
               .insertAsync(project, region, instantSnapshotGroupResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`instantSnapshotGroupResource` | `[InstantSnapshotGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionInstantSnapshotGroupRequest,Operation> insertCallable()

creates a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       InsertRegionInstantSnapshotGroupRequest request =
           InsertRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroupResource(InstantSnapshotGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceConsistencyGroup("sourceConsistencyGroup-2056893054")
               .build();
       ApiFuture<Operation> future =
           regionInstantSnapshotGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstantSnapshotGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionInstantSnapshotGroupRequest,Operation,Operation> insertOperationCallable()

creates a Regional InstantSnapshotGroup resource

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       InsertRegionInstantSnapshotGroupRequest request =
           InsertRegionInstantSnapshotGroupRequest.newBuilder()
               .setInstantSnapshotGroupResource(InstantSnapshotGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceConsistencyGroup("sourceConsistencyGroup-2056893054")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstantSnapshotGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstantSnapshotGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionInstantSnapshotGroupsRequest request)
    
    
    public final RegionInstantSnapshotGroupsClient.ListPagedResponse list(ListRegionInstantSnapshotGroupsRequest request)

retrieves the list of InstantSnapshotGroup resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       ListRegionInstantSnapshotGroupsRequest request =
           ListRegionInstantSnapshotGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstantSnapshotGroup element :
           regionInstantSnapshotGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionInstantSnapshotGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstantSnapshotGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionInstantSnapshotGroupsClient.ListPagedResponse list(String project, String region)

retrieves the list of InstantSnapshotGroup resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (InstantSnapshotGroup element :
           regionInstantSnapshotGroupsClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstantSnapshotGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionInstantSnapshotGroupsRequest,ListInstantSnapshotGroups> listCallable()

retrieves the list of InstantSnapshotGroup resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       ListRegionInstantSnapshotGroupsRequest request =
           ListRegionInstantSnapshotGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         ListInstantSnapshotGroups response =
             regionInstantSnapshotGroupsClient.listCallable().call(request);
         for (InstantSnapshotGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstantSnapshotGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstantSnapshotGroupsRequest),[ListInstantSnapshotGroups](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstantSnapshotGroups)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionInstantSnapshotGroupsRequest,RegionInstantSnapshotGroupsClient.ListPagedResponse> listPagedCallable()

retrieves the list of InstantSnapshotGroup resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       ListRegionInstantSnapshotGroupsRequest request =
           ListRegionInstantSnapshotGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstantSnapshotGroup> future =
           regionInstantSnapshotGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstantSnapshotGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstantSnapshotGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstantSnapshotGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstantSnapshotGroupsClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRegionInstantSnapshotGroupRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRegionInstantSnapshotGroupRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       SetIamPolicyRegionInstantSnapshotGroupRequest request =
           SetIamPolicyRegionInstantSnapshotGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = regionInstantSnapshotGroupsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionInstantSnapshotGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetPolicyRequest regionSetPolicyRequestResource =
           RegionSetPolicyRequest.newBuilder().build();
       Policy response =
           regionInstantSnapshotGroupsClient.setIamPolicy(
               project, region, resource, regionSetPolicyRequestResource);
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
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRegionInstantSnapshotGroupRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       SetIamPolicyRegionInstantSnapshotGroupRequest request =
           SetIamPolicyRegionInstantSnapshotGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           regionInstantSnapshotGroupsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionInstantSnapshotGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionInstantSnapshotGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionInstantSnapshotGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       TestIamPermissionsRegionInstantSnapshotGroupRequest request =
           TestIamPermissionsRegionInstantSnapshotGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response =
           regionInstantSnapshotGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionInstantSnapshotGroupRequest)`  
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
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionInstantSnapshotGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionInstantSnapshotGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstantSnapshotGroupsClient regionInstantSnapshotGroupsClient =
         RegionInstantSnapshotGroupsClient.create()) {
       TestIamPermissionsRegionInstantSnapshotGroupRequest request =
           TestIamPermissionsRegionInstantSnapshotGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionInstantSnapshotGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionInstantSnapshotGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionInstantSnapshotGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
