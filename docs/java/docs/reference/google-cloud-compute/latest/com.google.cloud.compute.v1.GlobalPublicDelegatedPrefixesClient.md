---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient
title: Class GlobalPublicDelegatedPrefixesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:25.769622+00:00
---

# Class GlobalPublicDelegatedPrefixesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalPublicDelegatedPrefixesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalPublicDelegatedPrefixesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalPublicDelegatedPrefixes API.

This client uses GlobalPublicDelegatedPrefixes version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix response =
           globalPublicDelegatedPrefixesClient.get(project, publicDelegatedPrefix);
     }
     

Note: close() needs to be called on the GlobalPublicDelegatedPrefixesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified global PublicDelegatedPrefix. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteGlobalPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified global PublicDelegatedPrefix resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalPublicDelegatedPrefixeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertGlobalPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, PublicDelegatedPrefix publicDelegatedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the global PublicDelegatedPrefixes for a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalPublicDelegatedPrefixesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchGlobalPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalPublicDelegatedPrefixesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalPublicDelegatedPrefixesSettings globalPublicDelegatedPrefixesSettings =
         GlobalPublicDelegatedPrefixesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create(globalPublicDelegatedPrefixesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalPublicDelegatedPrefixesSettings globalPublicDelegatedPrefixesSettings =
         GlobalPublicDelegatedPrefixesSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create(globalPublicDelegatedPrefixesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalPublicDelegatedPrefixesClient

## Static Methods 

### create()
    
    
    public static final GlobalPublicDelegatedPrefixesClient create()

Constructs an instance of GlobalPublicDelegatedPrefixesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalPublicDelegatedPrefixesSettings settings)
    
    
    public static final GlobalPublicDelegatedPrefixesClient create(GlobalPublicDelegatedPrefixesSettings settings)

Constructs an instance of GlobalPublicDelegatedPrefixesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalPublicDelegatedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalPublicDelegatedPrefixesStub stub)
    
    
    public static final GlobalPublicDelegatedPrefixesClient create(GlobalPublicDelegatedPrefixesStub stub)

Constructs an instance of GlobalPublicDelegatedPrefixesClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalPublicDelegatedPrefixesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalPublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalPublicDelegatedPrefixesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient)` |   
  
## Constructors 

### GlobalPublicDelegatedPrefixesClient(GlobalPublicDelegatedPrefixesSettings settings)
    
    
    protected GlobalPublicDelegatedPrefixesClient(GlobalPublicDelegatedPrefixesSettings settings)

Constructs an instance of GlobalPublicDelegatedPrefixesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalPublicDelegatedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesSettings)`  
  
  
### GlobalPublicDelegatedPrefixesClient(GlobalPublicDelegatedPrefixesStub stub)
    
    
    protected GlobalPublicDelegatedPrefixesClient(GlobalPublicDelegatedPrefixesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalPublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalPublicDelegatedPrefixesStub)`  
  
  
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

### deleteAsync(DeleteGlobalPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteGlobalPublicDelegatedPrefixeRequest request)

Deletes the specified global PublicDelegatedPrefix.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       DeleteGlobalPublicDelegatedPrefixeRequest request =
           DeleteGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalPublicDelegatedPrefixesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String publicDelegatedPrefix)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String publicDelegatedPrefix)

Deletes the specified global PublicDelegatedPrefix.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       Operation response =
           globalPublicDelegatedPrefixesClient.deleteAsync(project, publicDelegatedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalPublicDelegatedPrefixeRequest,Operation> deleteCallable()

Deletes the specified global PublicDelegatedPrefix.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       DeleteGlobalPublicDelegatedPrefixeRequest request =
           DeleteGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalPublicDelegatedPrefixesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteGlobalPublicDelegatedPrefixeRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified global PublicDelegatedPrefix.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       DeleteGlobalPublicDelegatedPrefixeRequest request =
           DeleteGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalPublicDelegatedPrefixesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetGlobalPublicDelegatedPrefixeRequest request)
    
    
    public final PublicDelegatedPrefix get(GetGlobalPublicDelegatedPrefixeRequest request)

Returns the specified global PublicDelegatedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       GetGlobalPublicDelegatedPrefixeRequest request =
           GetGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .build();
       PublicDelegatedPrefix response = globalPublicDelegatedPrefixesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)` |   
  
### get(String project, String publicDelegatedPrefix)
    
    
    public final PublicDelegatedPrefix get(String project, String publicDelegatedPrefix)

Returns the specified global PublicDelegatedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix response =
           globalPublicDelegatedPrefixesClient.get(project, publicDelegatedPrefix);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalPublicDelegatedPrefixeRequest,PublicDelegatedPrefix> getCallable()

Returns the specified global PublicDelegatedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       GetGlobalPublicDelegatedPrefixeRequest request =
           GetGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .build();
       ApiFuture<PublicDelegatedPrefix> future =
           globalPublicDelegatedPrefixesClient.getCallable().futureCall(request);
       // Do something.
       PublicDelegatedPrefix response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalPublicDelegatedPrefixeRequest),[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalPublicDelegatedPrefixesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesSettings` |   
  
### getStub()
    
    
    public GlobalPublicDelegatedPrefixesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalPublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalPublicDelegatedPrefixesStub)` |   
  
### insertAsync(InsertGlobalPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertGlobalPublicDelegatedPrefixeRequest request)

Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       InsertGlobalPublicDelegatedPrefixeRequest request =
           InsertGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalPublicDelegatedPrefixesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, PublicDelegatedPrefix publicDelegatedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, PublicDelegatedPrefix publicDelegatedPrefixResource)

Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       PublicDelegatedPrefix publicDelegatedPrefixResource =
           PublicDelegatedPrefix.newBuilder().build();
       Operation response =
           globalPublicDelegatedPrefixesClient
               .insertAsync(project, publicDelegatedPrefixResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicDelegatedPrefixResource` | `[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertGlobalPublicDelegatedPrefixeRequest,Operation> insertCallable()

Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       InsertGlobalPublicDelegatedPrefixeRequest request =
           InsertGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalPublicDelegatedPrefixesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertGlobalPublicDelegatedPrefixeRequest,Operation,Operation> insertOperationCallable()

Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       InsertGlobalPublicDelegatedPrefixeRequest request =
           InsertGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalPublicDelegatedPrefixesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListGlobalPublicDelegatedPrefixesRequest request)
    
    
    public final GlobalPublicDelegatedPrefixesClient.ListPagedResponse list(ListGlobalPublicDelegatedPrefixesRequest request)

Lists the global PublicDelegatedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       ListGlobalPublicDelegatedPrefixesRequest request =
           ListGlobalPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (PublicDelegatedPrefix element :
           globalPublicDelegatedPrefixesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalPublicDelegatedPrefixesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalPublicDelegatedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final GlobalPublicDelegatedPrefixesClient.ListPagedResponse list(String project)

Lists the global PublicDelegatedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       for (PublicDelegatedPrefix element :
           globalPublicDelegatedPrefixesClient.list(project).iterateAll()) {
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
`[GlobalPublicDelegatedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalPublicDelegatedPrefixesRequest,PublicDelegatedPrefixList> listCallable()

Lists the global PublicDelegatedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       ListGlobalPublicDelegatedPrefixesRequest request =
           ListGlobalPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         PublicDelegatedPrefixList response =
             globalPublicDelegatedPrefixesClient.listCallable().call(request);
         for (PublicDelegatedPrefix element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalPublicDelegatedPrefixesRequest),[PublicDelegatedPrefixList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalPublicDelegatedPrefixesRequest,GlobalPublicDelegatedPrefixesClient.ListPagedResponse> listPagedCallable()

Lists the global PublicDelegatedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       ListGlobalPublicDelegatedPrefixesRequest request =
           ListGlobalPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<PublicDelegatedPrefix> future =
           globalPublicDelegatedPrefixesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (PublicDelegatedPrefix element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalPublicDelegatedPrefixesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalPublicDelegatedPrefixesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchGlobalPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchGlobalPublicDelegatedPrefixeRequest request)

Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       PatchGlobalPublicDelegatedPrefixeRequest request =
           PatchGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalPublicDelegatedPrefixesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource)

Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix publicDelegatedPrefixResource =
           PublicDelegatedPrefix.newBuilder().build();
       Operation response =
           globalPublicDelegatedPrefixesClient
               .patchAsync(project, publicDelegatedPrefix, publicDelegatedPrefixResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to patch.  
`publicDelegatedPrefixResource` | `[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchGlobalPublicDelegatedPrefixeRequest,Operation> patchCallable()

Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       PatchGlobalPublicDelegatedPrefixeRequest request =
           PatchGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalPublicDelegatedPrefixesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchGlobalPublicDelegatedPrefixeRequest,Operation,Operation> patchOperationCallable()

Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalPublicDelegatedPrefixesClient globalPublicDelegatedPrefixesClient =
         GlobalPublicDelegatedPrefixesClient.create()) {
       PatchGlobalPublicDelegatedPrefixeRequest request =
           PatchGlobalPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalPublicDelegatedPrefixesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchGlobalPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
