---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient
title: Class RegionSslPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:00.212973+00:00
---

# Class RegionSslPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionSslPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionSslPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionSslPolicies API.

This client uses RegionSslPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String sslPolicy = "sslPolicy618174046";
       SslPolicy response = regionSslPoliciesClient.get(project, region, sslPolicy);
     }
     

Note: close() needs to be called on the RegionSslPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionSslPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String sslPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Lists all of the ordered rules present in a single specified policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionSslPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String sslPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new policy in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionSslPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, SslPolicy sslPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists all the SSL policies that have been configured for the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionSslPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListAvailableFeatures |  Lists all features that can be specified in the SSL policy when using custom profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAvailableFeatures(ListAvailableFeaturesRegionSslPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAvailableFeatures(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAvailableFeaturesCallable() 

  
Patch |  Patches the specified SSL policy with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionSslPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String sslPolicy, SslPolicy sslPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionSslPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionSslPoliciesSettings regionSslPoliciesSettings =
         RegionSslPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionSslPoliciesClient regionSslPoliciesClient =
         RegionSslPoliciesClient.create(regionSslPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionSslPoliciesSettings regionSslPoliciesSettings =
         RegionSslPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionSslPoliciesClient regionSslPoliciesClient =
         RegionSslPoliciesClient.create(regionSslPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionSslPoliciesClient

## Static Methods 

### create()
    
    
    public static final RegionSslPoliciesClient create()

Constructs an instance of RegionSslPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionSslPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionSslPoliciesSettings settings)
    
    
    public static final RegionSslPoliciesClient create(RegionSslPoliciesSettings settings)

Constructs an instance of RegionSslPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionSslPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionSslPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionSslPoliciesStub stub)
    
    
    public static final RegionSslPoliciesClient create(RegionSslPoliciesStub stub)

Constructs an instance of RegionSslPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionSslPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionSslPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSslPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionSslPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient)` |   
  
## Constructors 

### RegionSslPoliciesClient(RegionSslPoliciesSettings settings)
    
    
    protected RegionSslPoliciesClient(RegionSslPoliciesSettings settings)

Constructs an instance of RegionSslPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionSslPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesSettings)`  
  
  
### RegionSslPoliciesClient(RegionSslPoliciesStub stub)
    
    
    protected RegionSslPoliciesClient(RegionSslPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionSslPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSslPoliciesStub)`  
  
  
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

### deleteAsync(DeleteRegionSslPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionSslPolicyRequest request)

Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       DeleteRegionSslPolicyRequest request =
           DeleteRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .build();
       Operation response = regionSslPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSslPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String sslPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String sslPolicy)

Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String sslPolicy = "sslPolicy618174046";
       Operation response = regionSslPoliciesClient.deleteAsync(project, region, sslPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`sslPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the SSL policy to delete. The name must be 1-63 characters long, and comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionSslPolicyRequest,Operation> deleteCallable()

Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       DeleteRegionSslPolicyRequest request =
           DeleteRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .build();
       ApiFuture<Operation> future = regionSslPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionSslPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified SSL policy. The SSL policy resource can be deleted only if it is not in use by any TargetHttpsProxy or TargetSslProxy resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       DeleteRegionSslPolicyRequest request =
           DeleteRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .build();
       OperationFuture<Operation, Operation> future =
           regionSslPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionSslPolicyRequest request)
    
    
    public final SslPolicy get(GetRegionSslPolicyRequest request)

Lists all of the ordered rules present in a single specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       GetRegionSslPolicyRequest request =
           GetRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSslPolicy("sslPolicy618174046")
               .build();
       SslPolicy response = regionSslPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionSslPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SslPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicy)` |   
  
### get(String project, String region, String sslPolicy)
    
    
    public final SslPolicy get(String project, String region, String sslPolicy)

Lists all of the ordered rules present in a single specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String sslPolicy = "sslPolicy618174046";
       SslPolicy response = regionSslPoliciesClient.get(project, region, sslPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`sslPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the SSL policy to update. The name must be 1-63 characters long, and comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[SslPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionSslPolicyRequest,SslPolicy> getCallable()

Lists all of the ordered rules present in a single specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       GetRegionSslPolicyRequest request =
           GetRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSslPolicy("sslPolicy618174046")
               .build();
       ApiFuture<SslPolicy> future = regionSslPoliciesClient.getCallable().futureCall(request);
       // Do something.
       SslPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionSslPolicyRequest),[SslPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionSslPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionSslPoliciesSettings` |   
  
### getStub()
    
    
    public RegionSslPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionSslPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSslPoliciesStub)` |   
  
### insertAsync(InsertRegionSslPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionSslPolicyRequest request)

Creates a new policy in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       InsertRegionSslPolicyRequest request =
           InsertRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       Operation response = regionSslPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, SslPolicy sslPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, SslPolicy sslPolicyResource)

Creates a new policy in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       SslPolicy sslPolicyResource = SslPolicy.newBuilder().build();
       Operation response =
           regionSslPoliciesClient.insertAsync(project, region, sslPolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`sslPolicyResource` | `[SslPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionSslPolicyRequest,Operation> insertCallable()

Creates a new policy in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       InsertRegionSslPolicyRequest request =
           InsertRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = regionSslPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionSslPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new policy in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       InsertRegionSslPolicyRequest request =
           InsertRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionSslPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionSslPoliciesRequest request)
    
    
    public final RegionSslPoliciesClient.ListPagedResponse list(ListRegionSslPoliciesRequest request)

Lists all the SSL policies that have been configured for the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       ListRegionSslPoliciesRequest request =
           ListRegionSslPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (SslPolicy element : regionSslPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionSslPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSslPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionSslPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionSslPoliciesClient.ListPagedResponse list(String project, String region)

Lists all the SSL policies that have been configured for the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (SslPolicy element : regionSslPoliciesClient.list(project, region).iterateAll()) {
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
`[RegionSslPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient.ListPagedResponse)` |   
  
### listAvailableFeatures(ListAvailableFeaturesRegionSslPoliciesRequest request)
    
    
    public final SslPoliciesListAvailableFeaturesResponse listAvailableFeatures(ListAvailableFeaturesRegionSslPoliciesRequest request)

Lists all features that can be specified in the SSL policy when using custom profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       ListAvailableFeaturesRegionSslPoliciesRequest request =
           ListAvailableFeaturesRegionSslPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       SslPoliciesListAvailableFeaturesResponse response =
           regionSslPoliciesClient.listAvailableFeatures(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAvailableFeaturesRegionSslPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAvailableFeaturesRegionSslPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SslPoliciesListAvailableFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPoliciesListAvailableFeaturesResponse)` |   
  
### listAvailableFeatures(String project, String region)
    
    
    public final SslPoliciesListAvailableFeaturesResponse listAvailableFeatures(String project, String region)

Lists all features that can be specified in the SSL policy when using custom profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       SslPoliciesListAvailableFeaturesResponse response =
           regionSslPoliciesClient.listAvailableFeatures(project, region);
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
`[SslPoliciesListAvailableFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPoliciesListAvailableFeaturesResponse)` |   
  
### listAvailableFeaturesCallable()
    
    
    public final UnaryCallable<ListAvailableFeaturesRegionSslPoliciesRequest,SslPoliciesListAvailableFeaturesResponse> listAvailableFeaturesCallable()

Lists all features that can be specified in the SSL policy when using custom profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       ListAvailableFeaturesRegionSslPoliciesRequest request =
           ListAvailableFeaturesRegionSslPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<SslPoliciesListAvailableFeaturesResponse> future =
           regionSslPoliciesClient.listAvailableFeaturesCallable().futureCall(request);
       // Do something.
       SslPoliciesListAvailableFeaturesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAvailableFeaturesRegionSslPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAvailableFeaturesRegionSslPoliciesRequest),[SslPoliciesListAvailableFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPoliciesListAvailableFeaturesResponse)>` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionSslPoliciesRequest,SslPoliciesList> listCallable()

Lists all the SSL policies that have been configured for the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       ListRegionSslPoliciesRequest request =
           ListRegionSslPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         SslPoliciesList response = regionSslPoliciesClient.listCallable().call(request);
         for (SslPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionSslPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSslPoliciesRequest),[SslPoliciesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPoliciesList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionSslPoliciesRequest,RegionSslPoliciesClient.ListPagedResponse> listPagedCallable()

Lists all the SSL policies that have been configured for the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       ListRegionSslPoliciesRequest request =
           ListRegionSslPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<SslPolicy> future = regionSslPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (SslPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionSslPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSslPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslPoliciesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionSslPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionSslPolicyRequest request)

Patches the specified SSL policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       PatchRegionSslPolicyRequest request =
           PatchRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       Operation response = regionSslPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionSslPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String sslPolicy, SslPolicy sslPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String sslPolicy, SslPolicy sslPolicyResource)

Patches the specified SSL policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String sslPolicy = "sslPolicy618174046";
       SslPolicy sslPolicyResource = SslPolicy.newBuilder().build();
       Operation response =
           regionSslPoliciesClient.patchAsync(project, region, sslPolicy, sslPolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`sslPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the SSL policy to update. The name must be 1-63 characters long, and comply with RFC1035.  
`sslPolicyResource` | `[SslPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionSslPolicyRequest,Operation> patchCallable()

Patches the specified SSL policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       PatchRegionSslPolicyRequest request =
           PatchRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = regionSslPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionSslPolicyRequest,Operation,Operation> patchOperationCallable()

Patches the specified SSL policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSslPoliciesClient regionSslPoliciesClient = RegionSslPoliciesClient.create()) {
       PatchRegionSslPolicyRequest request =
           PatchRegionSslPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSslPolicy("sslPolicy618174046")
               .setSslPolicyResource(SslPolicy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionSslPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionSslPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionSslPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
