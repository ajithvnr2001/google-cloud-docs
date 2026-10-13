---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient
title: Class TargetPoolsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:39.050312+00:00
---

# Class TargetPoolsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetPoolsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/TargetPoolsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The TargetPools API.

This client uses TargetPools version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPool response = targetPoolsClient.get(project, region, targetPool);
     }
     

Note: close() needs to be called on the TargetPoolsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddHealthCheck |  Adds health check URLs to a target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addHealthCheckAsync(AddHealthCheckTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addHealthCheckAsync(String project, String region, String targetPool, TargetPoolsAddHealthCheckRequest targetPoolsAddHealthCheckRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addHealthCheckOperationCallable() 
  * addHealthCheckCallable() 

  
AddInstance |  Adds an instance to a target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addInstanceAsync(AddInstanceTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addInstanceAsync(String project, String region, String targetPool, TargetPoolsAddInstanceRequest targetPoolsAddInstanceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addInstanceOperationCallable() 
  * addInstanceCallable() 

  
AggregatedList |  Retrieves an aggregated list of target pools.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListTargetPoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String targetPool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetTargetPoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String targetPool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetHealth |  Gets the most recent health check results for each IP for the instance that is referenced by the given target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHealth(GetHealthTargetPoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHealth(String project, String region, String targetPool, InstanceReference instanceReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHealthCallable() 

  
Insert |  Creates a target pool in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, TargetPool targetPoolResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of target pools available to the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListTargetPoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
RemoveHealthCheck |  Removes health check URL from a target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeHealthCheckAsync(RemoveHealthCheckTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeHealthCheckAsync(String project, String region, String targetPool, TargetPoolsRemoveHealthCheckRequest targetPoolsRemoveHealthCheckRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeHealthCheckOperationCallable() 
  * removeHealthCheckCallable() 

  
RemoveInstance |  Removes instance URL from a target pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeInstanceAsync(RemoveInstanceTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeInstanceAsync(String project, String region, String targetPool, TargetPoolsRemoveInstanceRequest targetPoolsRemoveInstanceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeInstanceOperationCallable() 
  * removeInstanceCallable() 

  
SetBackup |  Changes a backup target pool's configurations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setBackupAsync(SetBackupTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setBackupAsync(String project, String region, String targetPool, TargetReference targetReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setBackupOperationCallable() 
  * setBackupCallable() 

  
SetSecurityPolicy |  Sets the Google Cloud Armor security policy for the specified target pool. For more information, seeGoogle Cloud Armor Overview |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSecurityPolicyAsync(SetSecurityPolicyTargetPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSecurityPolicyAsync(String project, String region, String targetPool, SecurityPolicyReference securityPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSecurityPolicyOperationCallable() 
  * setSecurityPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsTargetPoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetPoolsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetPoolsSettings targetPoolsSettings =
         TargetPoolsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetPoolsClient targetPoolsClient = TargetPoolsClient.create(targetPoolsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetPoolsSettings targetPoolsSettings =
         TargetPoolsSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetPoolsClient targetPoolsClient = TargetPoolsClient.create(targetPoolsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetPoolsClient

## Static Methods 

### create()
    
    
    public static final TargetPoolsClient create()

Constructs an instance of TargetPoolsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetPoolsSettings settings)
    
    
    public static final TargetPoolsClient create(TargetPoolsSettings settings)

Constructs an instance of TargetPoolsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetPoolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetPoolsStub stub)
    
    
    public static final TargetPoolsClient create(TargetPoolsStub stub)

Constructs an instance of TargetPoolsClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetPoolsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetPoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetPoolsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient)` |   
  
## Constructors 

### TargetPoolsClient(TargetPoolsSettings settings)
    
    
    protected TargetPoolsClient(TargetPoolsSettings settings)

Constructs an instance of TargetPoolsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetPoolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsSettings)`  
  
  
### TargetPoolsClient(TargetPoolsStub stub)
    
    
    protected TargetPoolsClient(TargetPoolsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetPoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetPoolsStub)`  
  
  
## Methods 

### addHealthCheckAsync(AddHealthCheckTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> addHealthCheckAsync(AddHealthCheckTargetPoolRequest request)

Adds health check URLs to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddHealthCheckTargetPoolRequest request =
           AddHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddHealthCheckRequestResource(
                   TargetPoolsAddHealthCheckRequest.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.addHealthCheckAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddHealthCheckTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addHealthCheckAsync(String project, String region, String targetPool, TargetPoolsAddHealthCheckRequest targetPoolsAddHealthCheckRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addHealthCheckAsync(String project, String region, String targetPool, TargetPoolsAddHealthCheckRequest targetPoolsAddHealthCheckRequestResource)

Adds health check URLs to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPoolsAddHealthCheckRequest targetPoolsAddHealthCheckRequestResource =
           TargetPoolsAddHealthCheckRequest.newBuilder().build();
       Operation response =
           targetPoolsClient
               .addHealthCheckAsync(
                   project, region, targetPool, targetPoolsAddHealthCheckRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the target pool to add a health check to.  
`targetPoolsAddHealthCheckRequestResource` | `[TargetPoolsAddHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsAddHealthCheckRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addHealthCheckCallable()
    
    
    public final UnaryCallable<AddHealthCheckTargetPoolRequest,Operation> addHealthCheckCallable()

Adds health check URLs to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddHealthCheckTargetPoolRequest request =
           AddHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddHealthCheckRequestResource(
                   TargetPoolsAddHealthCheckRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetPoolsClient.addHealthCheckCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddHealthCheckTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addHealthCheckOperationCallable()
    
    
    public final OperationCallable<AddHealthCheckTargetPoolRequest,Operation,Operation> addHealthCheckOperationCallable()

Adds health check URLs to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddHealthCheckTargetPoolRequest request =
           AddHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddHealthCheckRequestResource(
                   TargetPoolsAddHealthCheckRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.addHealthCheckOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddHealthCheckTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstanceAsync(AddInstanceTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> addInstanceAsync(AddInstanceTargetPoolRequest request)

Adds an instance to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddInstanceTargetPoolRequest request =
           AddInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddInstanceRequestResource(
                   TargetPoolsAddInstanceRequest.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.addInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstanceTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstanceAsync(String project, String region, String targetPool, TargetPoolsAddInstanceRequest targetPoolsAddInstanceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addInstanceAsync(String project, String region, String targetPool, TargetPoolsAddInstanceRequest targetPoolsAddInstanceRequestResource)

Adds an instance to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPoolsAddInstanceRequest targetPoolsAddInstanceRequestResource =
           TargetPoolsAddInstanceRequest.newBuilder().build();
       Operation response =
           targetPoolsClient
               .addInstanceAsync(project, region, targetPool, targetPoolsAddInstanceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to add instances to.  
`targetPoolsAddInstanceRequestResource` | `[TargetPoolsAddInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsAddInstanceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstanceCallable()
    
    
    public final UnaryCallable<AddInstanceTargetPoolRequest,Operation> addInstanceCallable()

Adds an instance to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddInstanceTargetPoolRequest request =
           AddInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddInstanceRequestResource(
                   TargetPoolsAddInstanceRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetPoolsClient.addInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstanceTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstanceOperationCallable()
    
    
    public final OperationCallable<AddInstanceTargetPoolRequest,Operation,Operation> addInstanceOperationCallable()

Adds an instance to a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AddInstanceTargetPoolRequest request =
           AddInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsAddInstanceRequestResource(
                   TargetPoolsAddInstanceRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.addInstanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstanceTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListTargetPoolsRequest request)
    
    
    public final TargetPoolsClient.AggregatedListPagedResponse aggregatedList(AggregatedListTargetPoolsRequest request)

Retrieves an aggregated list of target pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AggregatedListTargetPoolsRequest request =
           AggregatedListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, TargetPoolsScopedList> element :
           targetPoolsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetPoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final TargetPoolsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of target pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, TargetPoolsScopedList> element :
           targetPoolsClient.aggregatedList(project).iterateAll()) {
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
`[TargetPoolsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListTargetPoolsRequest,TargetPoolAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of target pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AggregatedListTargetPoolsRequest request =
           AggregatedListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         TargetPoolAggregatedList response =
             targetPoolsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, TargetPoolsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetPoolsRequest),[TargetPoolAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListTargetPoolsRequest,TargetPoolsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of target pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       AggregatedListTargetPoolsRequest request =
           AggregatedListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, TargetPoolsScopedList>> future =
           targetPoolsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, TargetPoolsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetPoolsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteTargetPoolRequest request)

Deletes the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       DeleteTargetPoolRequest request =
           DeleteTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .build();
       Operation response = targetPoolsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String targetPool)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String targetPool)

Deletes the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       Operation response = targetPoolsClient.deleteAsync(project, region, targetPool).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteTargetPoolRequest,Operation> deleteCallable()

Deletes the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       DeleteTargetPoolRequest request =
           DeleteTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .build();
       ApiFuture<Operation> future = targetPoolsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetPoolRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       DeleteTargetPoolRequest request =
           DeleteTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetTargetPoolRequest request)
    
    
    public final TargetPool get(GetTargetPoolRequest request)

Returns the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       GetTargetPoolRequest request =
           GetTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetPool("targetPool486493517")
               .build();
       TargetPool response = targetPoolsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPool)` |   
  
### get(String project, String region, String targetPool)
    
    
    public final TargetPool get(String project, String region, String targetPool)

Returns the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPool response = targetPoolsClient.get(project, region, targetPool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPool)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetTargetPoolRequest,TargetPool> getCallable()

Returns the specified target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       GetTargetPoolRequest request =
           GetTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetPool("targetPool486493517")
               .build();
       ApiFuture<TargetPool> future = targetPoolsClient.getCallable().futureCall(request);
       // Do something.
       TargetPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetPoolRequest),[TargetPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPool)>` |   
  
### getHealth(GetHealthTargetPoolRequest request)
    
    
    public final TargetPoolInstanceHealth getHealth(GetHealthTargetPoolRequest request)

Gets the most recent health check results for each IP for the instance that is referenced by the given target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       GetHealthTargetPoolRequest request =
           GetHealthTargetPoolRequest.newBuilder()
               .setInstanceReferenceResource(InstanceReference.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetPool("targetPool486493517")
               .build();
       TargetPoolInstanceHealth response = targetPoolsClient.getHealth(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHealthTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolInstanceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolInstanceHealth)` |   
  
### getHealth(String project, String region, String targetPool, InstanceReference instanceReferenceResource)
    
    
    public final TargetPoolInstanceHealth getHealth(String project, String region, String targetPool, InstanceReference instanceReferenceResource)

Gets the most recent health check results for each IP for the instance that is referenced by the given target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       InstanceReference instanceReferenceResource = InstanceReference.newBuilder().build();
       TargetPoolInstanceHealth response =
           targetPoolsClient.getHealth(project, region, targetPool, instanceReferenceResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to which the queried instance belongs.  
`instanceReferenceResource` | `[InstanceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolInstanceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolInstanceHealth)` |   
  
### getHealthCallable()
    
    
    public final UnaryCallable<GetHealthTargetPoolRequest,TargetPoolInstanceHealth> getHealthCallable()

Gets the most recent health check results for each IP for the instance that is referenced by the given target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       GetHealthTargetPoolRequest request =
           GetHealthTargetPoolRequest.newBuilder()
               .setInstanceReferenceResource(InstanceReference.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetPool("targetPool486493517")
               .build();
       ApiFuture<TargetPoolInstanceHealth> future =
           targetPoolsClient.getHealthCallable().futureCall(request);
       // Do something.
       TargetPoolInstanceHealth response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHealthTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthTargetPoolRequest),[TargetPoolInstanceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolInstanceHealth)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetPoolsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.TargetPoolsSettings` |   
  
### getStub()
    
    
    public TargetPoolsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetPoolsStub)` |   
  
### insertAsync(InsertTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertTargetPoolRequest request)

Creates a target pool in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       InsertTargetPoolRequest request =
           InsertTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPoolResource(TargetPool.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, TargetPool targetPoolResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, TargetPool targetPoolResource)

Creates a target pool in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       TargetPool targetPoolResource = TargetPool.newBuilder().build();
       Operation response = targetPoolsClient.insertAsync(project, region, targetPoolResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPoolResource` | `[TargetPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPool)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertTargetPoolRequest,Operation> insertCallable()

Creates a target pool in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       InsertTargetPoolRequest request =
           InsertTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPoolResource(TargetPool.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetPoolsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertTargetPoolRequest,Operation,Operation> insertOperationCallable()

Creates a target pool in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       InsertTargetPoolRequest request =
           InsertTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPoolResource(TargetPool.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListTargetPoolsRequest request)
    
    
    public final TargetPoolsClient.ListPagedResponse list(ListTargetPoolsRequest request)

Retrieves a list of target pools available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       ListTargetPoolsRequest request =
           ListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (TargetPool element : targetPoolsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetPoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetPoolsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final TargetPoolsClient.ListPagedResponse list(String project, String region)

Retrieves a list of target pools available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (TargetPool element : targetPoolsClient.list(project, region).iterateAll()) {
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
`[TargetPoolsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListTargetPoolsRequest,TargetPoolList> listCallable()

Retrieves a list of target pools available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       ListTargetPoolsRequest request =
           ListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         TargetPoolList response = targetPoolsClient.listCallable().call(request);
         for (TargetPool element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetPoolsRequest),[TargetPoolList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListTargetPoolsRequest,TargetPoolsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of target pools available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       ListTargetPoolsRequest request =
           ListTargetPoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<TargetPool> future = targetPoolsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetPool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetPoolsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsClient.ListPagedResponse)>` |   
  
### removeHealthCheckAsync(RemoveHealthCheckTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeHealthCheckAsync(RemoveHealthCheckTargetPoolRequest request)

Removes health check URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveHealthCheckTargetPoolRequest request =
           RemoveHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveHealthCheckRequestResource(
                   TargetPoolsRemoveHealthCheckRequest.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.removeHealthCheckAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveHealthCheckTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeHealthCheckAsync(String project, String region, String targetPool, TargetPoolsRemoveHealthCheckRequest targetPoolsRemoveHealthCheckRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removeHealthCheckAsync(String project, String region, String targetPool, TargetPoolsRemoveHealthCheckRequest targetPoolsRemoveHealthCheckRequestResource)

Removes health check URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPoolsRemoveHealthCheckRequest targetPoolsRemoveHealthCheckRequestResource =
           TargetPoolsRemoveHealthCheckRequest.newBuilder().build();
       Operation response =
           targetPoolsClient
               .removeHealthCheckAsync(
                   project, region, targetPool, targetPoolsRemoveHealthCheckRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the target pool to remove health checks from.  
`targetPoolsRemoveHealthCheckRequestResource` | `[TargetPoolsRemoveHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsRemoveHealthCheckRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeHealthCheckCallable()
    
    
    public final UnaryCallable<RemoveHealthCheckTargetPoolRequest,Operation> removeHealthCheckCallable()

Removes health check URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveHealthCheckTargetPoolRequest request =
           RemoveHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveHealthCheckRequestResource(
                   TargetPoolsRemoveHealthCheckRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           targetPoolsClient.removeHealthCheckCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveHealthCheckTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeHealthCheckOperationCallable()
    
    
    public final OperationCallable<RemoveHealthCheckTargetPoolRequest,Operation,Operation> removeHealthCheckOperationCallable()

Removes health check URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveHealthCheckTargetPoolRequest request =
           RemoveHealthCheckTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveHealthCheckRequestResource(
                   TargetPoolsRemoveHealthCheckRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.removeHealthCheckOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveHealthCheckTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveHealthCheckTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstanceAsync(RemoveInstanceTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeInstanceAsync(RemoveInstanceTargetPoolRequest request)

Removes instance URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveInstanceTargetPoolRequest request =
           RemoveInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveInstanceRequestResource(
                   TargetPoolsRemoveInstanceRequest.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.removeInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstanceTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstanceAsync(String project, String region, String targetPool, TargetPoolsRemoveInstanceRequest targetPoolsRemoveInstanceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removeInstanceAsync(String project, String region, String targetPool, TargetPoolsRemoveInstanceRequest targetPoolsRemoveInstanceRequestResource)

Removes instance URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetPoolsRemoveInstanceRequest targetPoolsRemoveInstanceRequestResource =
           TargetPoolsRemoveInstanceRequest.newBuilder().build();
       Operation response =
           targetPoolsClient
               .removeInstanceAsync(
                   project, region, targetPool, targetPoolsRemoveInstanceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to remove instances from.  
`targetPoolsRemoveInstanceRequestResource` | `[TargetPoolsRemoveInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetPoolsRemoveInstanceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstanceCallable()
    
    
    public final UnaryCallable<RemoveInstanceTargetPoolRequest,Operation> removeInstanceCallable()

Removes instance URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveInstanceTargetPoolRequest request =
           RemoveInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveInstanceRequestResource(
                   TargetPoolsRemoveInstanceRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetPoolsClient.removeInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstanceTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstanceOperationCallable()
    
    
    public final OperationCallable<RemoveInstanceTargetPoolRequest,Operation,Operation> removeInstanceOperationCallable()

Removes instance URL from a target pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       RemoveInstanceTargetPoolRequest request =
           RemoveInstanceTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetPoolsRemoveInstanceRequestResource(
                   TargetPoolsRemoveInstanceRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.removeInstanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveInstanceTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstanceTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackupAsync(SetBackupTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> setBackupAsync(SetBackupTargetPoolRequest request)

Changes a backup target pool's configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetBackupTargetPoolRequest request =
           SetBackupTargetPoolRequest.newBuilder()
               .setFailoverRatio(-861074818)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       Operation response = targetPoolsClient.setBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetBackupTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackupTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackupAsync(String project, String region, String targetPool, TargetReference targetReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setBackupAsync(String project, String region, String targetPool, TargetReference targetReferenceResource)

Changes a backup target pool's configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       TargetReference targetReferenceResource = TargetReference.newBuilder().build();
       Operation response =
           targetPoolsClient
               .setBackupAsync(project, region, targetPool, targetReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to set a backup pool for.  
`targetReferenceResource` | `[TargetReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackupCallable()
    
    
    public final UnaryCallable<SetBackupTargetPoolRequest,Operation> setBackupCallable()

Changes a backup target pool's configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetBackupTargetPoolRequest request =
           SetBackupTargetPoolRequest.newBuilder()
               .setFailoverRatio(-861074818)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetPoolsClient.setBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetBackupTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackupTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackupOperationCallable()
    
    
    public final OperationCallable<SetBackupTargetPoolRequest,Operation,Operation> setBackupOperationCallable()

Changes a backup target pool's configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetBackupTargetPoolRequest request =
           SetBackupTargetPoolRequest.newBuilder()
               .setFailoverRatio(-861074818)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetPool("targetPool486493517")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.setBackupOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetBackupTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackupTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyAsync(SetSecurityPolicyTargetPoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(SetSecurityPolicyTargetPoolRequest request)

Sets the Google Cloud Armor security policy for the specified target pool. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetSecurityPolicyTargetPoolRequest request =
           SetSecurityPolicyTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .setTargetPool("targetPool486493517")
               .build();
       Operation response = targetPoolsClient.setSecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSecurityPolicyTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyTargetPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyAsync(String project, String region, String targetPool, SecurityPolicyReference securityPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(String project, String region, String targetPool, SecurityPolicyReference securityPolicyReferenceResource)

Sets the Google Cloud Armor security policy for the specified target pool. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetPool = "targetPool486493517";
       SecurityPolicyReference securityPolicyReferenceResource =
           SecurityPolicyReference.newBuilder().build();
       Operation response =
           targetPoolsClient
               .setSecurityPolicyAsync(project, region, targetPool, securityPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetPool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetPool resource to which the security policy should be set. The name should conform to RFC1035.  
`securityPolicyReferenceResource` | `[SecurityPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyCallable()
    
    
    public final UnaryCallable<SetSecurityPolicyTargetPoolRequest,Operation> setSecurityPolicyCallable()

Sets the Google Cloud Armor security policy for the specified target pool. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetSecurityPolicyTargetPoolRequest request =
           SetSecurityPolicyTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .setTargetPool("targetPool486493517")
               .build();
       ApiFuture<Operation> future =
           targetPoolsClient.setSecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSecurityPolicyTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyOperationCallable()
    
    
    public final OperationCallable<SetSecurityPolicyTargetPoolRequest,Operation,Operation> setSecurityPolicyOperationCallable()

Sets the Google Cloud Armor security policy for the specified target pool. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       SetSecurityPolicyTargetPoolRequest request =
           SetSecurityPolicyTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .setTargetPool("targetPool486493517")
               .build();
       OperationFuture<Operation, Operation> future =
           targetPoolsClient.setSecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSecurityPolicyTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyTargetPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsTargetPoolRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsTargetPoolRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       TestIamPermissionsTargetPoolRequest request =
           TestIamPermissionsTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = targetPoolsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetPoolRequest)`  
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
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           targetPoolsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsTargetPoolRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetPoolsClient targetPoolsClient = TargetPoolsClient.create()) {
       TestIamPermissionsTargetPoolRequest request =
           TestIamPermissionsTargetPoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           targetPoolsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsTargetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetPoolRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
