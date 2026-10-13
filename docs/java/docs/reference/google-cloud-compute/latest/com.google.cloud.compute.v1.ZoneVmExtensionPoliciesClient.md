---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient
title: Class ZoneVmExtensionPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:51.622421+00:00
---

# Class ZoneVmExtensionPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ZoneVmExtensionPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ZoneVmExtensionPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ZoneVmExtensionPolicies API.

This client uses ZoneVmExtensionPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String vmExtensionPolicy = "vmExtensionPolicy1236125338";
       VmExtensionPolicy response =
           zoneVmExtensionPoliciesClient.get(project, zone, vmExtensionPolicy);
     }
     

Note: close() needs to be called on the ZoneVmExtensionPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes a specified zone VM extension policy within a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteZoneVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String vmExtensionPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Retrieves details of a specific zone VM extension policy within a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetZoneVmExtensionPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String vmExtensionPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new zone-level VM extension policy within a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertZoneVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, VmExtensionPolicy vmExtensionPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists all VM extension policies within a specific zone for a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListZoneVmExtensionPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Update |  Modifies an existing zone VM extension policy within a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateZoneVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String vmExtensionPolicy, VmExtensionPolicy vmExtensionPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ZoneVmExtensionPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ZoneVmExtensionPoliciesSettings zoneVmExtensionPoliciesSettings =
         ZoneVmExtensionPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create(zoneVmExtensionPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ZoneVmExtensionPoliciesSettings zoneVmExtensionPoliciesSettings =
         ZoneVmExtensionPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create(zoneVmExtensionPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ZoneVmExtensionPoliciesClient

## Static Methods 

### create()
    
    
    public static final ZoneVmExtensionPoliciesClient create()

Constructs an instance of ZoneVmExtensionPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ZoneVmExtensionPoliciesSettings settings)
    
    
    public static final ZoneVmExtensionPoliciesClient create(ZoneVmExtensionPoliciesSettings settings)

Constructs an instance of ZoneVmExtensionPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ZoneVmExtensionPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ZoneVmExtensionPoliciesStub stub)
    
    
    public static final ZoneVmExtensionPoliciesClient create(ZoneVmExtensionPoliciesStub stub)

Constructs an instance of ZoneVmExtensionPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(ZoneVmExtensionPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ZoneVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneVmExtensionPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient)` |   
  
## Constructors 

### ZoneVmExtensionPoliciesClient(ZoneVmExtensionPoliciesSettings settings)
    
    
    protected ZoneVmExtensionPoliciesClient(ZoneVmExtensionPoliciesSettings settings)

Constructs an instance of ZoneVmExtensionPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ZoneVmExtensionPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesSettings)`  
  
  
### ZoneVmExtensionPoliciesClient(ZoneVmExtensionPoliciesStub stub)
    
    
    protected ZoneVmExtensionPoliciesClient(ZoneVmExtensionPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ZoneVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneVmExtensionPoliciesStub)`  
  
  
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

### deleteAsync(DeleteZoneVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteZoneVmExtensionPolicyRequest request)

Deletes a specified zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       DeleteZoneVmExtensionPolicyRequest request =
           DeleteZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setZone("zone3744684")
               .build();
       Operation response = zoneVmExtensionPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String vmExtensionPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String vmExtensionPolicy)

Deletes a specified zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String vmExtensionPolicy = "vmExtensionPolicy1236125338";
       Operation response =
           zoneVmExtensionPoliciesClient.deleteAsync(project, zone, vmExtensionPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`vmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone VM extension policy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteZoneVmExtensionPolicyRequest,Operation> deleteCallable()

Deletes a specified zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       DeleteZoneVmExtensionPolicyRequest request =
           DeleteZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           zoneVmExtensionPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteZoneVmExtensionPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes a specified zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       DeleteZoneVmExtensionPolicyRequest request =
           DeleteZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           zoneVmExtensionPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetZoneVmExtensionPolicyRequest request)
    
    
    public final VmExtensionPolicy get(GetZoneVmExtensionPolicyRequest request)

Retrieves details of a specific zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       GetZoneVmExtensionPolicyRequest request =
           GetZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setZone("zone3744684")
               .build();
       VmExtensionPolicy response = zoneVmExtensionPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetZoneVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicy)` |   
  
### get(String project, String zone, String vmExtensionPolicy)
    
    
    public final VmExtensionPolicy get(String project, String zone, String vmExtensionPolicy)

Retrieves details of a specific zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String vmExtensionPolicy = "vmExtensionPolicy1236125338";
       VmExtensionPolicy response =
           zoneVmExtensionPoliciesClient.get(project, zone, vmExtensionPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`vmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the VM extension policy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[VmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetZoneVmExtensionPolicyRequest,VmExtensionPolicy> getCallable()

Retrieves details of a specific zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       GetZoneVmExtensionPolicyRequest request =
           GetZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setZone("zone3744684")
               .build();
       ApiFuture<VmExtensionPolicy> future =
           zoneVmExtensionPoliciesClient.getCallable().futureCall(request);
       // Do something.
       VmExtensionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetZoneVmExtensionPolicyRequest),[VmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable ZoneVmExtensionPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ZoneVmExtensionPoliciesSettings` |   
  
### getStub()
    
    
    public ZoneVmExtensionPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneVmExtensionPoliciesStub)` |   
  
### insertAsync(InsertZoneVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertZoneVmExtensionPolicyRequest request)

Creates a new zone-level VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       InsertZoneVmExtensionPolicyRequest request =
           InsertZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = zoneVmExtensionPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertZoneVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, VmExtensionPolicy vmExtensionPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, VmExtensionPolicy vmExtensionPolicyResource)

Creates a new zone-level VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       VmExtensionPolicy vmExtensionPolicyResource = VmExtensionPolicy.newBuilder().build();
       Operation response =
           zoneVmExtensionPoliciesClient.insertAsync(project, zone, vmExtensionPolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`vmExtensionPolicyResource` | `[VmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertZoneVmExtensionPolicyRequest,Operation> insertCallable()

Creates a new zone-level VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       InsertZoneVmExtensionPolicyRequest request =
           InsertZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           zoneVmExtensionPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertZoneVmExtensionPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new zone-level VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       InsertZoneVmExtensionPolicyRequest request =
           InsertZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           zoneVmExtensionPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListZoneVmExtensionPoliciesRequest request)
    
    
    public final ZoneVmExtensionPoliciesClient.ListPagedResponse list(ListZoneVmExtensionPoliciesRequest request)

Lists all VM extension policies within a specific zone for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       ListZoneVmExtensionPoliciesRequest request =
           ListZoneVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (VmExtensionPolicy element : zoneVmExtensionPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZoneVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneVmExtensionPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final ZoneVmExtensionPoliciesClient.ListPagedResponse list(String project, String zone)

Lists all VM extension policies within a specific zone for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (VmExtensionPolicy element :
           zoneVmExtensionPoliciesClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[ZoneVmExtensionPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListZoneVmExtensionPoliciesRequest,VmExtensionPolicyList> listCallable()

Lists all VM extension policies within a specific zone for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       ListZoneVmExtensionPoliciesRequest request =
           ListZoneVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         VmExtensionPolicyList response = zoneVmExtensionPoliciesClient.listCallable().call(request);
         for (VmExtensionPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneVmExtensionPoliciesRequest),[VmExtensionPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListZoneVmExtensionPoliciesRequest,ZoneVmExtensionPoliciesClient.ListPagedResponse> listPagedCallable()

Lists all VM extension policies within a specific zone for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       ListZoneVmExtensionPoliciesRequest request =
           ListZoneVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<VmExtensionPolicy> future =
           zoneVmExtensionPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (VmExtensionPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneVmExtensionPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneVmExtensionPoliciesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdateZoneVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateZoneVmExtensionPolicyRequest request)

Modifies an existing zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       UpdateZoneVmExtensionPolicyRequest request =
           UpdateZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = zoneVmExtensionPoliciesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateZoneVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String vmExtensionPolicy, VmExtensionPolicy vmExtensionPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String vmExtensionPolicy, VmExtensionPolicy vmExtensionPolicyResource)

Modifies an existing zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String vmExtensionPolicy = "vmExtensionPolicy1236125338";
       VmExtensionPolicy vmExtensionPolicyResource = VmExtensionPolicy.newBuilder().build();
       Operation response =
           zoneVmExtensionPoliciesClient
               .updateAsync(project, zone, vmExtensionPolicy, vmExtensionPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`vmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone VM extension policy to update.  
`vmExtensionPolicyResource` | `[VmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateZoneVmExtensionPolicyRequest,Operation> updateCallable()

Modifies an existing zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       UpdateZoneVmExtensionPolicyRequest request =
           UpdateZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           zoneVmExtensionPoliciesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateZoneVmExtensionPolicyRequest,Operation,Operation> updateOperationCallable()

Modifies an existing zone VM extension policy within a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneVmExtensionPoliciesClient zoneVmExtensionPoliciesClient =
         ZoneVmExtensionPoliciesClient.create()) {
       UpdateZoneVmExtensionPolicyRequest request =
           UpdateZoneVmExtensionPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setVmExtensionPolicy("vmExtensionPolicy1236125338")
               .setVmExtensionPolicyResource(VmExtensionPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           zoneVmExtensionPoliciesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateZoneVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateZoneVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
