---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient
title: Class InterconnectGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:50.314621+00:00
---

# Class InterconnectGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterconnectGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InterconnectGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InterconnectGroups API.

This client uses InterconnectGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       InterconnectGroup response = interconnectGroupsClient.get(project, interconnectGroup);
     }
     

Note: close() needs to be called on the InterconnectGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateMembers |  Create Interconnects with redundancy by creating them in a specified interconnect group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMembersAsync(CreateMembersInterconnectGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMembersAsync(String project, String interconnectGroup, InterconnectGroupsCreateMembersRequest interconnectGroupsCreateMembersRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMembersOperationCallable() 
  * createMembersCallable() 

  
Delete |  Deletes the specified InterconnectGroup in the given scope |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInterconnectGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String interconnectGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified InterconnectGroup resource in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInterconnectGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String interconnectGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyInterconnectGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetOperationalStatus |  Returns the interconnectStatuses for the specified InterconnectGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOperationalStatus(GetOperationalStatusInterconnectGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOperationalStatus(String project, String interconnectGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOperationalStatusCallable() 

  
Insert |  Creates a InterconnectGroup in the specified project in the given scope using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInterconnectGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, InterconnectGroup interconnectGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the InterconnectGroups for a project in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInterconnectGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified InterconnectGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchInterconnectGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String interconnectGroup, InterconnectGroup interconnectGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyInterconnectGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInterconnectGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InterconnectGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectGroupsSettings interconnectGroupsSettings =
         InterconnectGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InterconnectGroupsClient interconnectGroupsClient =
         InterconnectGroupsClient.create(interconnectGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectGroupsSettings interconnectGroupsSettings =
         InterconnectGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InterconnectGroupsClient interconnectGroupsClient =
         InterconnectGroupsClient.create(interconnectGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InterconnectGroupsClient

## Static Methods 

### create()
    
    
    public static final InterconnectGroupsClient create()

Constructs an instance of InterconnectGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectGroupsSettings settings)
    
    
    public static final InterconnectGroupsClient create(InterconnectGroupsSettings settings)

Constructs an instance of InterconnectGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectGroupsStub stub)
    
    
    public static final InterconnectGroupsClient create(InterconnectGroupsStub stub)

Constructs an instance of InterconnectGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InterconnectGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient)` |   
  
## Constructors 

### InterconnectGroupsClient(InterconnectGroupsSettings settings)
    
    
    protected InterconnectGroupsClient(InterconnectGroupsSettings settings)

Constructs an instance of InterconnectGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsSettings)`  
  
  
### InterconnectGroupsClient(InterconnectGroupsStub stub)
    
    
    protected InterconnectGroupsClient(InterconnectGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectGroupsStub)`  
  
  
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

### createMembersAsync(CreateMembersInterconnectGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> createMembersAsync(CreateMembersInterconnectGroupRequest request)

Create Interconnects with redundancy by creating them in a specified interconnect group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       CreateMembersInterconnectGroupRequest request =
           CreateMembersInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupsCreateMembersRequestResource(
                   InterconnectGroupsCreateMembersRequest.newBuilder().build())
               .setProject("project-309310695")
               .build();
       Operation response = interconnectGroupsClient.createMembersAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMembersInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateMembersInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createMembersAsync(String project, String interconnectGroup, InterconnectGroupsCreateMembersRequest interconnectGroupsCreateMembersRequestResource)
    
    
    public final OperationFuture<Operation,Operation> createMembersAsync(String project, String interconnectGroup, InterconnectGroupsCreateMembersRequest interconnectGroupsCreateMembersRequestResource)

Create Interconnects with redundancy by creating them in a specified interconnect group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       InterconnectGroupsCreateMembersRequest interconnectGroupsCreateMembersRequestResource =
           InterconnectGroupsCreateMembersRequest.newBuilder().build();
       Operation response =
           interconnectGroupsClient
               .createMembersAsync(
                   project, interconnectGroup, interconnectGroupsCreateMembersRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the group resource to create members for.  
`interconnectGroupsCreateMembersRequestResource` | `[InterconnectGroupsCreateMembersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsCreateMembersRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createMembersCallable()
    
    
    public final UnaryCallable<CreateMembersInterconnectGroupRequest,Operation> createMembersCallable()

Create Interconnects with redundancy by creating them in a specified interconnect group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       CreateMembersInterconnectGroupRequest request =
           CreateMembersInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupsCreateMembersRequestResource(
                   InterconnectGroupsCreateMembersRequest.newBuilder().build())
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future =
           interconnectGroupsClient.createMembersCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMembersInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateMembersInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createMembersOperationCallable()
    
    
    public final OperationCallable<CreateMembersInterconnectGroupRequest,Operation,Operation> createMembersOperationCallable()

Create Interconnects with redundancy by creating them in a specified interconnect group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       CreateMembersInterconnectGroupRequest request =
           CreateMembersInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupsCreateMembersRequestResource(
                   InterconnectGroupsCreateMembersRequest.newBuilder().build())
               .setProject("project-309310695")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectGroupsClient.createMembersOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMembersInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateMembersInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteInterconnectGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInterconnectGroupRequest request)

Deletes the specified InterconnectGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       DeleteInterconnectGroupRequest request =
           DeleteInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String interconnectGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String interconnectGroup)

Deletes the specified InterconnectGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       Operation response = interconnectGroupsClient.deleteAsync(project, interconnectGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectGroup resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInterconnectGroupRequest,Operation> deleteCallable()

Deletes the specified InterconnectGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       DeleteInterconnectGroupRequest request =
           DeleteInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = interconnectGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInterconnectGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified InterconnectGroup in the given scope

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       DeleteInterconnectGroupRequest request =
           DeleteInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInterconnectGroupRequest request)
    
    
    public final InterconnectGroup get(GetInterconnectGroupRequest request)

Returns the specified InterconnectGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetInterconnectGroupRequest request =
           GetInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .build();
       InterconnectGroup response = interconnectGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroup)` |   
  
### get(String project, String interconnectGroup)
    
    
    public final InterconnectGroup get(String project, String interconnectGroup)

Returns the specified InterconnectGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       InterconnectGroup response = interconnectGroupsClient.get(project, interconnectGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectGroup resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInterconnectGroupRequest,InterconnectGroup> getCallable()

Returns the specified InterconnectGroup resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetInterconnectGroupRequest request =
           GetInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectGroup> future =
           interconnectGroupsClient.getCallable().futureCall(request);
       // Do something.
       InterconnectGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectGroupRequest),[InterconnectGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroup)>` |   
  
### getIamPolicy(GetIamPolicyInterconnectGroupRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyInterconnectGroupRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetIamPolicyInterconnectGroupRequest request =
           GetIamPolicyInterconnectGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = interconnectGroupsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInterconnectGroupRequest)`  
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
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = interconnectGroupsClient.getIamPolicy(project, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyInterconnectGroupRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetIamPolicyInterconnectGroupRequest request =
           GetIamPolicyInterconnectGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           interconnectGroupsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInterconnectGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getOperationalStatus(GetOperationalStatusInterconnectGroupRequest request)
    
    
    public final InterconnectGroupsGetOperationalStatusResponse getOperationalStatus(GetOperationalStatusInterconnectGroupRequest request)

Returns the interconnectStatuses for the specified InterconnectGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetOperationalStatusInterconnectGroupRequest request =
           GetOperationalStatusInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .build();
       InterconnectGroupsGetOperationalStatusResponse response =
           interconnectGroupsClient.getOperationalStatus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOperationalStatusInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOperationalStatusInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsGetOperationalStatusResponse)` |   
  
### getOperationalStatus(String project, String interconnectGroup)
    
    
    public final InterconnectGroupsGetOperationalStatusResponse getOperationalStatus(String project, String interconnectGroup)

Returns the interconnectStatuses for the specified InterconnectGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       InterconnectGroupsGetOperationalStatusResponse response =
           interconnectGroupsClient.getOperationalStatus(project, interconnectGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnectGroup resource to query.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsGetOperationalStatusResponse)` |   
  
### getOperationalStatusCallable()
    
    
    public final UnaryCallable<GetOperationalStatusInterconnectGroupRequest,InterconnectGroupsGetOperationalStatusResponse> getOperationalStatusCallable()

Returns the interconnectStatuses for the specified InterconnectGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       GetOperationalStatusInterconnectGroupRequest request =
           GetOperationalStatusInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectGroupsGetOperationalStatusResponse> future =
           interconnectGroupsClient.getOperationalStatusCallable().futureCall(request);
       // Do something.
       InterconnectGroupsGetOperationalStatusResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOperationalStatusInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOperationalStatusInterconnectGroupRequest),[InterconnectGroupsGetOperationalStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsGetOperationalStatusResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable InterconnectGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InterconnectGroupsSettings` |   
  
### getStub()
    
    
    public InterconnectGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectGroupsStub)` |   
  
### insertAsync(InsertInterconnectGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInterconnectGroupRequest request)

Creates a InterconnectGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       InsertInterconnectGroupRequest request =
           InsertInterconnectGroupRequest.newBuilder()
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = interconnectGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, InterconnectGroup interconnectGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, InterconnectGroup interconnectGroupResource)

Creates a InterconnectGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       InterconnectGroup interconnectGroupResource = InterconnectGroup.newBuilder().build();
       Operation response =
           interconnectGroupsClient.insertAsync(project, interconnectGroupResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroupResource` | `[InterconnectGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInterconnectGroupRequest,Operation> insertCallable()

Creates a InterconnectGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       InsertInterconnectGroupRequest request =
           InsertInterconnectGroupRequest.newBuilder()
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = interconnectGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInterconnectGroupRequest,Operation,Operation> insertOperationCallable()

Creates a InterconnectGroup in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       InsertInterconnectGroupRequest request =
           InsertInterconnectGroupRequest.newBuilder()
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInterconnectGroupsRequest request)
    
    
    public final InterconnectGroupsClient.ListPagedResponse list(ListInterconnectGroupsRequest request)

Lists the InterconnectGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       ListInterconnectGroupsRequest request =
           ListInterconnectGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (InterconnectGroup element : interconnectGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final InterconnectGroupsClient.ListPagedResponse list(String project)

Lists the InterconnectGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       for (InterconnectGroup element : interconnectGroupsClient.list(project).iterateAll()) {
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
`[InterconnectGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInterconnectGroupsRequest,InterconnectGroupsListResponse> listCallable()

Lists the InterconnectGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       ListInterconnectGroupsRequest request =
           ListInterconnectGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         InterconnectGroupsListResponse response =
             interconnectGroupsClient.listCallable().call(request);
         for (InterconnectGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectGroupsRequest),[InterconnectGroupsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectGroupsRequest,InterconnectGroupsClient.ListPagedResponse> listPagedCallable()

Lists the InterconnectGroups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       ListInterconnectGroupsRequest request =
           ListInterconnectGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectGroup> future =
           interconnectGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroupsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchInterconnectGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchInterconnectGroupRequest request)

Patches the specified InterconnectGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       PatchInterconnectGroupRequest request =
           PatchInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = interconnectGroupsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String interconnectGroup, InterconnectGroup interconnectGroupResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String interconnectGroup, InterconnectGroup interconnectGroupResource)

Patches the specified InterconnectGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String interconnectGroup = "interconnectGroup2103544465";
       InterconnectGroup interconnectGroupResource = InterconnectGroup.newBuilder().build();
       Operation response =
           interconnectGroupsClient
               .patchAsync(project, interconnectGroup, interconnectGroupResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InterconnectGroup resource to patch.  
`interconnectGroupResource` | `[InterconnectGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchInterconnectGroupRequest,Operation> patchCallable()

Patches the specified InterconnectGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       PatchInterconnectGroupRequest request =
           PatchInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future = interconnectGroupsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchInterconnectGroupRequest,Operation,Operation> patchOperationCallable()

Patches the specified InterconnectGroup resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       PatchInterconnectGroupRequest request =
           PatchInterconnectGroupRequest.newBuilder()
               .setInterconnectGroup("interconnectGroup2103544465")
               .setInterconnectGroupResource(InterconnectGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           interconnectGroupsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInterconnectGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyInterconnectGroupRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyInterconnectGroupRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       SetIamPolicyInterconnectGroupRequest request =
           SetIamPolicyInterconnectGroupRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = interconnectGroupsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInterconnectGroupRequest)`  
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
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           interconnectGroupsClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicyInterconnectGroupRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       SetIamPolicyInterconnectGroupRequest request =
           SetIamPolicyInterconnectGroupRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           interconnectGroupsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInterconnectGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsInterconnectGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInterconnectGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       TestIamPermissionsInterconnectGroupRequest request =
           TestIamPermissionsInterconnectGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = interconnectGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInterconnectGroupRequest)`  
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
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           interconnectGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsInterconnectGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectGroupsClient interconnectGroupsClient = InterconnectGroupsClient.create()) {
       TestIamPermissionsInterconnectGroupRequest request =
           TestIamPermissionsInterconnectGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           interconnectGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInterconnectGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInterconnectGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
