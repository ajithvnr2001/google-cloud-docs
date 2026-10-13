---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient
title: Class InterconnectAttachmentGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:47.828240+00:00
---

# Class InterconnectAttachmentGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterconnectAttachmentGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InterconnectAttachmentGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InterconnectAttachmentGroups API.

This client uses InterconnectAttachmentGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectAttachmentGroup = "interconnectAttachmentGroup-1652813650";
       InterconnectAttachmentGroup response =
           interconnectAttachmentGroupsClient.get(project, interconnectAttachmentGroup);
     }
     

Note: close() needs to be called on the InterconnectAttachmentGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified InterconnectAttachmentGroup in the given scope |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInterconnectAttachmentGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String interconnectAttachmentGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified InterconnectAttachmentGroup resource in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInterconnectAttachmentGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String interconnectAttachmentGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyInterconnectAttachmentGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetOperationalStatus |  Returns the InterconnectAttachmentStatuses for the specified InterconnectAttachmentGroup resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOperationalStatus(GetOperationalStatusInterconnectAttachmentGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOperationalStatus(String project, String interconnectAttachmentGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOperationalStatusCallable() 

  
Insert |  Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInterconnectAttachmentGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, InterconnectAttachmentGroup interconnectAttachmentGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the InterconnectAttachmentGroups for a project in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInterconnectAttachmentGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchInterconnectAttachmentGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String interconnectAttachmentGroup, InterconnectAttachmentGroup interconnectAttachmentGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyInterconnectAttachmentGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInterconnectAttachmentGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InterconnectAttachmentGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectAttachmentGroupsSettings interconnectAttachmentGroupsSettings =
         InterconnectAttachmentGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create(interconnectAttachmentGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectAttachmentGroupsSettings interconnectAttachmentGroupsSettings =
         InterconnectAttachmentGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create(interconnectAttachmentGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InterconnectAttachmentGroupsClient

## Static Methods 

### create()
    
    
    public static final InterconnectAttachmentGroupsClient create()

Constructs an instance of InterconnectAttachmentGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectAttachmentGroupsSettings settings)
    
    
    public static final InterconnectAttachmentGroupsClient create(InterconnectAttachmentGroupsSettings settings)

Constructs an instance of InterconnectAttachmentGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectAttachmentGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectAttachmentGroupsStub stub)
    
    
    public static final InterconnectAttachmentGroupsClient create(InterconnectAttachmentGroupsStub stub)

Constructs an instance of InterconnectAttachmentGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InterconnectAttachmentGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectAttachmentGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient)` |   
  
## Constructors 

### InterconnectAttachmentGroupsClient(InterconnectAttachmentGroupsSettings settings)
    
    
    protected InterconnectAttachmentGroupsClient(InterconnectAttachmentGroupsSettings settings)

Constructs an instance of InterconnectAttachmentGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectAttachmentGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsSettings)`  
  
  
### InterconnectAttachmentGroupsClient(InterconnectAttachmentGroupsStub stub)
    
    
    protected InterconnectAttachmentGroupsClient(InterconnectAttachmentGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectAttachmentGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentGroupsStub)`  
  
  
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

### deleteAsync(DeleteInterconnectAttachmentGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInterconnectAttachmentGroupRequest request)

Deletes the specified InterconnectAttachmentGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       DeleteInterconnectAttachmentGroupRequest request =
           DeleteInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectAttachmentGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String interconnectAttachmentGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String interconnectAttachmentGroup)

Deletes the specified InterconnectAttachmentGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectAttachmentGroup = "interconnectAttachmentGroup-1652813650";
       Operation response =
           interconnectAttachmentGroupsClient
               .deleteAsync(project, interconnectAttachmentGroup)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectAttachmentGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectAttachmentGroup resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInterconnectAttachmentGroupRequest,Operation> deleteCallable()

Deletes the specified InterconnectAttachmentGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       DeleteInterconnectAttachmentGroupRequest request =
           DeleteInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInterconnectAttachmentGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified InterconnectAttachmentGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       DeleteInterconnectAttachmentGroupRequest request =
           DeleteInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInterconnectAttachmentGroupRequest request)
    
    
    public final InterconnectAttachmentGroup get(GetInterconnectAttachmentGroupRequest request)

Returns the specified InterconnectAttachmentGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetInterconnectAttachmentGroupRequest request =
           GetInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .build();
       InterconnectAttachmentGroup response = interconnectAttachmentGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroup)` |   
  
### get(String project, String interconnectAttachmentGroup)
    
    
    public final InterconnectAttachmentGroup get(String project, String interconnectAttachmentGroup)

Returns the specified InterconnectAttachmentGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectAttachmentGroup = "interconnectAttachmentGroup-1652813650";
       InterconnectAttachmentGroup response =
           interconnectAttachmentGroupsClient.get(project, interconnectAttachmentGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectAttachmentGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectAttachmentGroup resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInterconnectAttachmentGroupRequest,InterconnectAttachmentGroup> getCallable()

Returns the specified InterconnectAttachmentGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetInterconnectAttachmentGroupRequest request =
           GetInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectAttachmentGroup> future =
           interconnectAttachmentGroupsClient.getCallable().futureCall(request);
       // Do something.
       InterconnectAttachmentGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectAttachmentGroupRequest),[InterconnectAttachmentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroup)>` |   
  
### getIamPolicy(GetIamPolicyInterconnectAttachmentGroupRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyInterconnectAttachmentGroupRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetIamPolicyInterconnectAttachmentGroupRequest request =
           GetIamPolicyInterconnectAttachmentGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = interconnectAttachmentGroupsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = interconnectAttachmentGroupsClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyInterconnectAttachmentGroupRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetIamPolicyInterconnectAttachmentGroupRequest request =
           GetIamPolicyInterconnectAttachmentGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           interconnectAttachmentGroupsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInterconnectAttachmentGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getOperationalStatus(GetOperationalStatusInterconnectAttachmentGroupRequest request)
    
    
    public final InterconnectAttachmentGroupsGetOperationalStatusResponse getOperationalStatus(GetOperationalStatusInterconnectAttachmentGroupRequest request)

Returns the InterconnectAttachmentStatuses for the specified InterconnectAttachmentGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetOperationalStatusInterconnectAttachmentGroupRequest request =
           GetOperationalStatusInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .build();
       InterconnectAttachmentGroupsGetOperationalStatusResponse response =
           interconnectAttachmentGroupsClient.getOperationalStatus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOperationalStatusInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOperationalStatusInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsGetOperationalStatusResponse)` |   
  
### getOperationalStatus(String project, String interconnectAttachmentGroup)
    
    
    public final InterconnectAttachmentGroupsGetOperationalStatusResponse getOperationalStatus(String project, String interconnectAttachmentGroup)

Returns the InterconnectAttachmentStatuses for the specified InterconnectAttachmentGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectAttachmentGroup = "interconnectAttachmentGroup-1652813650";
       InterconnectAttachmentGroupsGetOperationalStatusResponse response =
           interconnectAttachmentGroupsClient.getOperationalStatus(
               project, interconnectAttachmentGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectAttachmentGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnectAttachmentGroup resource to query.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsGetOperationalStatusResponse)` |   
  
### getOperationalStatusCallable()
    
    
    public final UnaryCallable<GetOperationalStatusInterconnectAttachmentGroupRequest,InterconnectAttachmentGroupsGetOperationalStatusResponse> getOperationalStatusCallable()

Returns the InterconnectAttachmentStatuses for the specified InterconnectAttachmentGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       GetOperationalStatusInterconnectAttachmentGroupRequest request =
           GetOperationalStatusInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectAttachmentGroupsGetOperationalStatusResponse> future =
           interconnectAttachmentGroupsClient.getOperationalStatusCallable().futureCall(request);
       // Do something.
       InterconnectAttachmentGroupsGetOperationalStatusResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOperationalStatusInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOperationalStatusInterconnectAttachmentGroupRequest),[InterconnectAttachmentGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsGetOperationalStatusResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable InterconnectAttachmentGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InterconnectAttachmentGroupsSettings` |   
  
### getStub()
    
    
    public InterconnectAttachmentGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectAttachmentGroupsStub)` |   
  
### insertAsync(InsertInterconnectAttachmentGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInterconnectAttachmentGroupRequest request)

Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       InsertInterconnectAttachmentGroupRequest request =
           InsertInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectAttachmentGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, InterconnectAttachmentGroup interconnectAttachmentGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, InterconnectAttachmentGroup interconnectAttachmentGroupResource)

Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       InterconnectAttachmentGroup interconnectAttachmentGroupResource =
           InterconnectAttachmentGroup.newBuilder().build();
       Operation response =
           interconnectAttachmentGroupsClient
               .insertAsync(project, interconnectAttachmentGroupResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectAttachmentGroupResource` | `[InterconnectAttachmentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInterconnectAttachmentGroupRequest,Operation> insertCallable()

Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       InsertInterconnectAttachmentGroupRequest request =
           InsertInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInterconnectAttachmentGroupRequest,Operation,Operation> insertOperationCallable()

Creates a InterconnectAttachmentGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       InsertInterconnectAttachmentGroupRequest request =
           InsertInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInterconnectAttachmentGroupsRequest request)
    
    
    public final InterconnectAttachmentGroupsClient.ListPagedResponse list(ListInterconnectAttachmentGroupsRequest request)

Lists the InterconnectAttachmentGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       ListInterconnectAttachmentGroupsRequest request =
           ListInterconnectAttachmentGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (InterconnectAttachmentGroup element :
           interconnectAttachmentGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectAttachmentGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final InterconnectAttachmentGroupsClient.ListPagedResponse list(String project)

Lists the InterconnectAttachmentGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       for (InterconnectAttachmentGroup element :
           interconnectAttachmentGroupsClient.list(project).iterateAll()) {
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
`[InterconnectAttachmentGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentGroupsRequest,InterconnectAttachmentGroupsListResponse> listCallable()

Lists the InterconnectAttachmentGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       ListInterconnectAttachmentGroupsRequest request =
           ListInterconnectAttachmentGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         InterconnectAttachmentGroupsListResponse response =
             interconnectAttachmentGroupsClient.listCallable().call(request);
         for (InterconnectAttachmentGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentGroupsRequest),[InterconnectAttachmentGroupsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectAttachmentGroupsRequest,InterconnectAttachmentGroupsClient.ListPagedResponse> listPagedCallable()

Lists the InterconnectAttachmentGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       ListInterconnectAttachmentGroupsRequest request =
           ListInterconnectAttachmentGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectAttachmentGroup> future =
           interconnectAttachmentGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectAttachmentGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectAttachmentGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectAttachmentGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroupsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchInterconnectAttachmentGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchInterconnectAttachmentGroupRequest request)

Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       PatchInterconnectAttachmentGroupRequest request =
           PatchInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = interconnectAttachmentGroupsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String interconnectAttachmentGroup, InterconnectAttachmentGroup interconnectAttachmentGroupResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String interconnectAttachmentGroup, InterconnectAttachmentGroup interconnectAttachmentGroupResource)

Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectAttachmentGroup = "interconnectAttachmentGroup-1652813650";
       InterconnectAttachmentGroup interconnectAttachmentGroupResource =
           InterconnectAttachmentGroup.newBuilder().build();
       Operation response =
           interconnectAttachmentGroupsClient
               .patchAsync(project, interconnectAttachmentGroup, interconnectAttachmentGroupResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectAttachmentGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectAttachmentGroup resource to patch.  
`interconnectAttachmentGroupResource` | `[InterconnectAttachmentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectAttachmentGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchInterconnectAttachmentGroupRequest,Operation> patchCallable()

Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       PatchInterconnectAttachmentGroupRequest request =
           PatchInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future =
           interconnectAttachmentGroupsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchInterconnectAttachmentGroupRequest,Operation,Operation> patchOperationCallable()

Patches the specified InterconnectAttachmentGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       PatchInterconnectAttachmentGroupRequest request =
           PatchInterconnectAttachmentGroupRequest.newBuilder()
               .setInterconnectAttachmentGroup("interconnectAttachmentGroup-1652813650")
               .setInterconnectAttachmentGroupResource(
                   InterconnectAttachmentGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectAttachmentGroupsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectAttachmentGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyInterconnectAttachmentGroupRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyInterconnectAttachmentGroupRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       SetIamPolicyInterconnectAttachmentGroupRequest request =
           SetIamPolicyInterconnectAttachmentGroupRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = interconnectAttachmentGroupsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInterconnectAttachmentGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           interconnectAttachmentGroupsClient.setIamPolicy(
               project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyInterconnectAttachmentGroupRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       SetIamPolicyInterconnectAttachmentGroupRequest request =
           SetIamPolicyInterconnectAttachmentGroupRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           interconnectAttachmentGroupsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInterconnectAttachmentGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsInterconnectAttachmentGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInterconnectAttachmentGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       TestIamPermissionsInterconnectAttachmentGroupRequest request =
           TestIamPermissionsInterconnectAttachmentGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response =
           interconnectAttachmentGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInterconnectAttachmentGroupRequest)`  
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
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           interconnectAttachmentGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsInterconnectAttachmentGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectAttachmentGroupsClient interconnectAttachmentGroupsClient =
         InterconnectAttachmentGroupsClient.create()) {
       TestIamPermissionsInterconnectAttachmentGroupRequest request =
           TestIamPermissionsInterconnectAttachmentGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           interconnectAttachmentGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInterconnectAttachmentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInterconnectAttachmentGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
