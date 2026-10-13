---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient
title: Class InstanceTemplatesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:38.076754+00:00
---

# Class InstanceTemplatesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstanceTemplatesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InstanceTemplatesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InstanceTemplates API.

This client uses InstanceTemplates version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String instanceTemplate = "instanceTemplate1009541167";
       InstanceTemplate response = instanceTemplatesClient.get(project, instanceTemplate);
     }
     

Note: close() needs to be called on the InstanceTemplatesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all InstanceTemplates resources, regional and global, available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInstanceTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInstanceTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String instanceTemplate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified instance template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInstanceTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String instanceTemplate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyInstanceTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInstanceTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, InstanceTemplate instanceTemplateResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of instance templates that are contained within the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInstanceTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyInstanceTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInstanceTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InstanceTemplatesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceTemplatesSettings instanceTemplatesSettings =
         InstanceTemplatesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InstanceTemplatesClient instanceTemplatesClient =
         InstanceTemplatesClient.create(instanceTemplatesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceTemplatesSettings instanceTemplatesSettings =
         InstanceTemplatesSettings.newBuilder().setEndpoint(myEndpoint).build();
     InstanceTemplatesClient instanceTemplatesClient =
         InstanceTemplatesClient.create(instanceTemplatesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstanceTemplatesClient

## Static Methods 

### create()
    
    
    public static final InstanceTemplatesClient create()

Constructs an instance of InstanceTemplatesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceTemplatesSettings settings)
    
    
    public static final InstanceTemplatesClient create(InstanceTemplatesSettings settings)

Constructs an instance of InstanceTemplatesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceTemplatesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceTemplatesStub stub)
    
    
    public static final InstanceTemplatesClient create(InstanceTemplatesStub stub)

Constructs an instance of InstanceTemplatesClient, using the given stub for making calls. This is for advanced usage - prefer using create(InstanceTemplatesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceTemplatesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient)` |   
  
## Constructors 

### InstanceTemplatesClient(InstanceTemplatesSettings settings)
    
    
    protected InstanceTemplatesClient(InstanceTemplatesSettings settings)

Constructs an instance of InstanceTemplatesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceTemplatesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesSettings)`  
  
  
### InstanceTemplatesClient(InstanceTemplatesStub stub)
    
    
    protected InstanceTemplatesClient(InstanceTemplatesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceTemplatesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListInstanceTemplatesRequest request)
    
    
    public final InstanceTemplatesClient.AggregatedListPagedResponse aggregatedList(AggregatedListInstanceTemplatesRequest request)

Retrieves the list of all InstanceTemplates resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       AggregatedListInstanceTemplatesRequest request =
           AggregatedListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InstanceTemplatesScopedList> element :
           instanceTemplatesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InstanceTemplatesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all InstanceTemplates resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InstanceTemplatesScopedList> element :
           instanceTemplatesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceTemplatesRequest,InstanceTemplateAggregatedList> aggregatedListCallable()

Retrieves the list of all InstanceTemplates resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       AggregatedListInstanceTemplatesRequest request =
           AggregatedListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InstanceTemplateAggregatedList response =
             instanceTemplatesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InstanceTemplatesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceTemplatesRequest),[InstanceTemplateAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplateAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceTemplatesRequest,InstanceTemplatesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all InstanceTemplates resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       AggregatedListInstanceTemplatesRequest request =
           AggregatedListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InstanceTemplatesScopedList>> future =
           instanceTemplatesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InstanceTemplatesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceTemplatesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteInstanceTemplateRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInstanceTemplateRequest request)

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       DeleteInstanceTemplateRequest request =
           DeleteInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = instanceTemplatesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String instanceTemplate)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String instanceTemplate)

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String instanceTemplate = "instanceTemplate1009541167";
       Operation response = instanceTemplatesClient.deleteAsync(project, instanceTemplate).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`instanceTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance template to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInstanceTemplateRequest,Operation> deleteCallable()

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       DeleteInstanceTemplateRequest request =
           DeleteInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = instanceTemplatesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceTemplateRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       DeleteInstanceTemplateRequest request =
           DeleteInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceTemplatesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInstanceTemplateRequest request)
    
    
    public final InstanceTemplate get(GetInstanceTemplateRequest request)

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       GetInstanceTemplateRequest request =
           GetInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .build();
       InstanceTemplate response = instanceTemplatesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)` |   
  
### get(String project, String instanceTemplate)
    
    
    public final InstanceTemplate get(String project, String instanceTemplate)

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String instanceTemplate = "instanceTemplate1009541167";
       InstanceTemplate response = instanceTemplatesClient.get(project, instanceTemplate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`instanceTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance template.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInstanceTemplateRequest,InstanceTemplate> getCallable()

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       GetInstanceTemplateRequest request =
           GetInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstanceTemplate> future =
           instanceTemplatesClient.getCallable().futureCall(request);
       // Do something.
       InstanceTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceTemplateRequest),[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)>` |   
  
### getIamPolicy(GetIamPolicyInstanceTemplateRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyInstanceTemplateRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       GetIamPolicyInstanceTemplateRequest request =
           GetIamPolicyInstanceTemplateRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = instanceTemplatesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstanceTemplateRequest)`  
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
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = instanceTemplatesClient.getIamPolicy(project, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyInstanceTemplateRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       GetIamPolicyInstanceTemplateRequest request =
           GetIamPolicyInstanceTemplateRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = instanceTemplatesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstanceTemplateRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable InstanceTemplatesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InstanceTemplatesSettings` |   
  
### getStub()
    
    
    public InstanceTemplatesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceTemplatesStub)` |   
  
### insertAsync(InsertInstanceTemplateRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInstanceTemplateRequest request)

Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       InsertInstanceTemplateRequest request =
           InsertInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = instanceTemplatesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, InstanceTemplate instanceTemplateResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, InstanceTemplate instanceTemplateResource)

Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       InstanceTemplate instanceTemplateResource = InstanceTemplate.newBuilder().build();
       Operation response =
           instanceTemplatesClient.insertAsync(project, instanceTemplateResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`instanceTemplateResource` | `[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInstanceTemplateRequest,Operation> insertCallable()

Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       InsertInstanceTemplateRequest request =
           InsertInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = instanceTemplatesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInstanceTemplateRequest,Operation,Operation> insertOperationCallable()

Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       InsertInstanceTemplateRequest request =
           InsertInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceTemplatesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInstanceTemplatesRequest request)
    
    
    public final InstanceTemplatesClient.ListPagedResponse list(ListInstanceTemplatesRequest request)

Retrieves a list of instance templates that are contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       ListInstanceTemplatesRequest request =
           ListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (InstanceTemplate element : instanceTemplatesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplatesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final InstanceTemplatesClient.ListPagedResponse list(String project)

Retrieves a list of instance templates that are contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       for (InstanceTemplate element : instanceTemplatesClient.list(project).iterateAll()) {
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
`[InstanceTemplatesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInstanceTemplatesRequest,InstanceTemplateList> listCallable()

Retrieves a list of instance templates that are contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       ListInstanceTemplatesRequest request =
           ListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         InstanceTemplateList response = instanceTemplatesClient.listCallable().call(request);
         for (InstanceTemplate element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceTemplatesRequest),[InstanceTemplateList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplateList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInstanceTemplatesRequest,InstanceTemplatesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of instance templates that are contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       ListInstanceTemplatesRequest request =
           ListInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InstanceTemplate> future =
           instanceTemplatesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceTemplatesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyInstanceTemplateRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyInstanceTemplateRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       SetIamPolicyInstanceTemplateRequest request =
           SetIamPolicyInstanceTemplateRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = instanceTemplatesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstanceTemplateRequest)`  
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
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           instanceTemplatesClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicyInstanceTemplateRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       SetIamPolicyInstanceTemplateRequest request =
           SetIamPolicyInstanceTemplateRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = instanceTemplatesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstanceTemplateRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsInstanceTemplateRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInstanceTemplateRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       TestIamPermissionsInstanceTemplateRequest request =
           TestIamPermissionsInstanceTemplateRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = instanceTemplatesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceTemplateRequest)`  
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
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           instanceTemplatesClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsInstanceTemplateRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
       TestIamPermissionsInstanceTemplateRequest request =
           TestIamPermissionsInstanceTemplateRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           instanceTemplatesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceTemplateRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
