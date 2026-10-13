---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient
title: Class GlobalVmExtensionPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:28.436726+00:00
---

# Class GlobalVmExtensionPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalVmExtensionPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalVmExtensionPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalVmExtensionPolicies API.

This client uses GlobalVmExtensionPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String globalVmExtensionPolicy = "globalVmExtensionPolicy-869114569";
       GlobalVmExtensionPolicy response =
           globalVmExtensionPoliciesClient.get(project, globalVmExtensionPolicy);
     }
     

Note: close() needs to be called on the GlobalVmExtensionPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all VM Extension Policy resources available to the specified project.  To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListGlobalVmExtensionPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Purge scoped resources (zonal policies) from a global VM extension policy, and then delete the global VM extension policy. Purge of the scoped resources is a pre-condition of the global VM extension policy deletion. The deletion of the global VM extension policy happens after the purge rollout is done, so it's not a part of the LRO. It's an automatic process that triggers in the backend. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteGlobalVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicyRolloutOperationRolloutInput globalVmExtensionPolicyRolloutOperationRolloutInputResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Gets details of a global VM extension policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalVmExtensionPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String globalVmExtensionPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new project level GlobalVmExtensionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertGlobalVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, GlobalVmExtensionPolicy globalVmExtensionPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists global VM extension policies. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalVmExtensionPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Update |  Updates a global VM extension policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateGlobalVmExtensionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicy globalVmExtensionPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalVmExtensionPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalVmExtensionPoliciesSettings globalVmExtensionPoliciesSettings =
         GlobalVmExtensionPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create(globalVmExtensionPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalVmExtensionPoliciesSettings globalVmExtensionPoliciesSettings =
         GlobalVmExtensionPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create(globalVmExtensionPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalVmExtensionPoliciesClient

## Static Methods 

### create()
    
    
    public static final GlobalVmExtensionPoliciesClient create()

Constructs an instance of GlobalVmExtensionPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalVmExtensionPoliciesSettings settings)
    
    
    public static final GlobalVmExtensionPoliciesClient create(GlobalVmExtensionPoliciesSettings settings)

Constructs an instance of GlobalVmExtensionPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalVmExtensionPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalVmExtensionPoliciesStub stub)
    
    
    public static final GlobalVmExtensionPoliciesClient create(GlobalVmExtensionPoliciesStub stub)

Constructs an instance of GlobalVmExtensionPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalVmExtensionPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalVmExtensionPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient)` |   
  
## Constructors 

### GlobalVmExtensionPoliciesClient(GlobalVmExtensionPoliciesSettings settings)
    
    
    protected GlobalVmExtensionPoliciesClient(GlobalVmExtensionPoliciesSettings settings)

Constructs an instance of GlobalVmExtensionPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalVmExtensionPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesSettings)`  
  
  
### GlobalVmExtensionPoliciesClient(GlobalVmExtensionPoliciesStub stub)
    
    
    protected GlobalVmExtensionPoliciesClient(GlobalVmExtensionPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalVmExtensionPoliciesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListGlobalVmExtensionPoliciesRequest request)
    
    
    public final GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse aggregatedList(AggregatedListGlobalVmExtensionPoliciesRequest request)

Retrieves the list of all VM Extension Policy resources available to the specified project.

To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       AggregatedListGlobalVmExtensionPoliciesRequest request =
           AggregatedListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, VmExtensionPoliciesScopedList> element :
           globalVmExtensionPoliciesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalVmExtensionPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all VM Extension Policy resources available to the specified project.

To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, VmExtensionPoliciesScopedList> element :
           globalVmExtensionPoliciesClient.aggregatedList(project).iterateAll()) {
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
`[GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListGlobalVmExtensionPoliciesRequest,VmExtensionPolicyAggregatedListResponse> aggregatedListCallable()

Retrieves the list of all VM Extension Policy resources available to the specified project.

To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       AggregatedListGlobalVmExtensionPoliciesRequest request =
           AggregatedListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         VmExtensionPolicyAggregatedListResponse response =
             globalVmExtensionPoliciesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, VmExtensionPoliciesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalVmExtensionPoliciesRequest),[VmExtensionPolicyAggregatedListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmExtensionPolicyAggregatedListResponse)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListGlobalVmExtensionPoliciesRequest,GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all VM Extension Policy resources available to the specified project.

To prevent failure, it's recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       AggregatedListGlobalVmExtensionPoliciesRequest request =
           AggregatedListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, VmExtensionPoliciesScopedList>> future =
           globalVmExtensionPoliciesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, VmExtensionPoliciesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalVmExtensionPoliciesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteGlobalVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteGlobalVmExtensionPolicyRequest request)

Purge scoped resources (zonal policies) from a global VM extension policy, and then delete the global VM extension policy. Purge of the scoped resources is a pre-condition of the global VM extension policy deletion. The deletion of the global VM extension policy happens after the purge rollout is done, so it's not a part of the LRO. It's an automatic process that triggers in the backend.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       DeleteGlobalVmExtensionPolicyRequest request =
           DeleteGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyRolloutOperationRolloutInputResource(
                   GlobalVmExtensionPolicyRolloutOperationRolloutInput.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalVmExtensionPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicyRolloutOperationRolloutInput globalVmExtensionPolicyRolloutOperationRolloutInputResource)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicyRolloutOperationRolloutInput globalVmExtensionPolicyRolloutOperationRolloutInputResource)

Purge scoped resources (zonal policies) from a global VM extension policy, and then delete the global VM extension policy. Purge of the scoped resources is a pre-condition of the global VM extension policy deletion. The deletion of the global VM extension policy happens after the purge rollout is done, so it's not a part of the LRO. It's an automatic process that triggers in the backend.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String globalVmExtensionPolicy = "globalVmExtensionPolicy-869114569";
       GlobalVmExtensionPolicyRolloutOperationRolloutInput
           globalVmExtensionPolicyRolloutOperationRolloutInputResource =
               GlobalVmExtensionPolicyRolloutOperationRolloutInput.newBuilder().build();
       Operation response =
           globalVmExtensionPoliciesClient
               .deleteAsync(
                   project,
                   globalVmExtensionPolicy,
                   globalVmExtensionPolicyRolloutOperationRolloutInputResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`globalVmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the global VM extension policy to purge scoped resources for.  
`globalVmExtensionPolicyRolloutOperationRolloutInputResource` | `[GlobalVmExtensionPolicyRolloutOperationRolloutInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicyRolloutOperationRolloutInput)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalVmExtensionPolicyRequest,Operation> deleteCallable()

Purge scoped resources (zonal policies) from a global VM extension policy, and then delete the global VM extension policy. Purge of the scoped resources is a pre-condition of the global VM extension policy deletion. The deletion of the global VM extension policy happens after the purge rollout is done, so it's not a part of the LRO. It's an automatic process that triggers in the backend.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       DeleteGlobalVmExtensionPolicyRequest request =
           DeleteGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyRolloutOperationRolloutInputResource(
                   GlobalVmExtensionPolicyRolloutOperationRolloutInput.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalVmExtensionPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteGlobalVmExtensionPolicyRequest,Operation,Operation> deleteOperationCallable()

Purge scoped resources (zonal policies) from a global VM extension policy, and then delete the global VM extension policy. Purge of the scoped resources is a pre-condition of the global VM extension policy deletion. The deletion of the global VM extension policy happens after the purge rollout is done, so it's not a part of the LRO. It's an automatic process that triggers in the backend.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       DeleteGlobalVmExtensionPolicyRequest request =
           DeleteGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyRolloutOperationRolloutInputResource(
                   GlobalVmExtensionPolicyRolloutOperationRolloutInput.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalVmExtensionPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetGlobalVmExtensionPolicyRequest request)
    
    
    public final GlobalVmExtensionPolicy get(GetGlobalVmExtensionPolicyRequest request)

Gets details of a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       GetGlobalVmExtensionPolicyRequest request =
           GetGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setProject("project-309310695")
               .build();
       GlobalVmExtensionPolicy response = globalVmExtensionPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicy)` |   
  
### get(String project, String globalVmExtensionPolicy)
    
    
    public final GlobalVmExtensionPolicy get(String project, String globalVmExtensionPolicy)

Gets details of a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String globalVmExtensionPolicy = "globalVmExtensionPolicy-869114569";
       GlobalVmExtensionPolicy response =
           globalVmExtensionPoliciesClient.get(project, globalVmExtensionPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`globalVmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the GlobalVmExtensionPolicy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalVmExtensionPolicyRequest,GlobalVmExtensionPolicy> getCallable()

Gets details of a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       GetGlobalVmExtensionPolicyRequest request =
           GetGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setProject("project-309310695")
               .build();
       ApiFuture<GlobalVmExtensionPolicy> future =
           globalVmExtensionPoliciesClient.getCallable().futureCall(request);
       // Do something.
       GlobalVmExtensionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalVmExtensionPolicyRequest),[GlobalVmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalVmExtensionPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalVmExtensionPoliciesSettings` |   
  
### getStub()
    
    
    public GlobalVmExtensionPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalVmExtensionPoliciesStub)` |   
  
### insertAsync(InsertGlobalVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertGlobalVmExtensionPolicyRequest request)

Creates a new project level GlobalVmExtensionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       InsertGlobalVmExtensionPolicyRequest request =
           InsertGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalVmExtensionPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, GlobalVmExtensionPolicy globalVmExtensionPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, GlobalVmExtensionPolicy globalVmExtensionPolicyResource)

Creates a new project level GlobalVmExtensionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       GlobalVmExtensionPolicy globalVmExtensionPolicyResource =
           GlobalVmExtensionPolicy.newBuilder().build();
       Operation response =
           globalVmExtensionPoliciesClient
               .insertAsync(project, globalVmExtensionPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`globalVmExtensionPolicyResource` | `[GlobalVmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertGlobalVmExtensionPolicyRequest,Operation> insertCallable()

Creates a new project level GlobalVmExtensionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       InsertGlobalVmExtensionPolicyRequest request =
           InsertGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalVmExtensionPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertGlobalVmExtensionPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new project level GlobalVmExtensionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       InsertGlobalVmExtensionPolicyRequest request =
           InsertGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalVmExtensionPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListGlobalVmExtensionPoliciesRequest request)
    
    
    public final GlobalVmExtensionPoliciesClient.ListPagedResponse list(ListGlobalVmExtensionPoliciesRequest request)

Lists global VM extension policies.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       ListGlobalVmExtensionPoliciesRequest request =
           ListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (GlobalVmExtensionPolicy element :
           globalVmExtensionPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalVmExtensionPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalVmExtensionPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final GlobalVmExtensionPoliciesClient.ListPagedResponse list(String project)

Lists global VM extension policies.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       for (GlobalVmExtensionPolicy element :
           globalVmExtensionPoliciesClient.list(project).iterateAll()) {
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
`[GlobalVmExtensionPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalVmExtensionPoliciesRequest,GlobalVmExtensionPolicyList> listCallable()

Lists global VM extension policies.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       ListGlobalVmExtensionPoliciesRequest request =
           ListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         GlobalVmExtensionPolicyList response =
             globalVmExtensionPoliciesClient.listCallable().call(request);
         for (GlobalVmExtensionPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalVmExtensionPoliciesRequest),[GlobalVmExtensionPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalVmExtensionPoliciesRequest,GlobalVmExtensionPoliciesClient.ListPagedResponse> listPagedCallable()

Lists global VM extension policies.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       ListGlobalVmExtensionPoliciesRequest request =
           ListGlobalVmExtensionPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<GlobalVmExtensionPolicy> future =
           globalVmExtensionPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (GlobalVmExtensionPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalVmExtensionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalVmExtensionPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPoliciesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdateGlobalVmExtensionPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateGlobalVmExtensionPolicyRequest request)

Updates a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       UpdateGlobalVmExtensionPolicyRequest request =
           UpdateGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalVmExtensionPoliciesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateGlobalVmExtensionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicy globalVmExtensionPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String globalVmExtensionPolicy, GlobalVmExtensionPolicy globalVmExtensionPolicyResource)

Updates a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       String project = "project-309310695";
       String globalVmExtensionPolicy = "globalVmExtensionPolicy-869114569";
       GlobalVmExtensionPolicy globalVmExtensionPolicyResource =
           GlobalVmExtensionPolicy.newBuilder().build();
       Operation response =
           globalVmExtensionPoliciesClient
               .updateAsync(project, globalVmExtensionPolicy, globalVmExtensionPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`globalVmExtensionPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the global VM extension policy to update.  
`globalVmExtensionPolicyResource` | `[GlobalVmExtensionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalVmExtensionPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateGlobalVmExtensionPolicyRequest,Operation> updateCallable()

Updates a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       UpdateGlobalVmExtensionPolicyRequest request =
           UpdateGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalVmExtensionPoliciesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateGlobalVmExtensionPolicyRequest,Operation,Operation> updateOperationCallable()

Updates a global VM extension policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalVmExtensionPoliciesClient globalVmExtensionPoliciesClient =
         GlobalVmExtensionPoliciesClient.create()) {
       UpdateGlobalVmExtensionPolicyRequest request =
           UpdateGlobalVmExtensionPolicyRequest.newBuilder()
               .setGlobalVmExtensionPolicy("globalVmExtensionPolicy-869114569")
               .setGlobalVmExtensionPolicyResource(GlobalVmExtensionPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalVmExtensionPoliciesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGlobalVmExtensionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateGlobalVmExtensionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
