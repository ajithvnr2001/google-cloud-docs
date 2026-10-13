---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient
title: Class RegionHealthAggregationPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:35.190789+00:00
---

# Class RegionHealthAggregationPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionHealthAggregationPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionHealthAggregationPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionHealthAggregationPolicies API.

This client uses RegionHealthAggregationPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthAggregationPolicy = "healthAggregationPolicy755484600";
       HealthAggregationPolicy response =
           regionHealthAggregationPoliciesClient.get(project, region, healthAggregationPolicy);
     }
     

Note: close() needs to be called on the RegionHealthAggregationPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListRegionHealthAggregationPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified HealthAggregationPolicy in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionHealthAggregationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String healthAggregationPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified HealthAggregationPolicy resource in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionHealthAggregationPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String healthAggregationPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionHealthAggregationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, HealthAggregationPolicy healthAggregationPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the HealthAggregationPolicies for a project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionHealthAggregationPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified regional HealthAggregationPolicy resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionHealthAggregationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String healthAggregationPolicy, HealthAggregationPolicy healthAggregationPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionHealthAggregationPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionHealthAggregationPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionHealthAggregationPoliciesSettings regionHealthAggregationPoliciesSettings =
         RegionHealthAggregationPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create(regionHealthAggregationPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionHealthAggregationPoliciesSettings regionHealthAggregationPoliciesSettings =
         RegionHealthAggregationPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create(regionHealthAggregationPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionHealthAggregationPoliciesClient

## Static Methods 

### create()
    
    
    public static final RegionHealthAggregationPoliciesClient create()

Constructs an instance of RegionHealthAggregationPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionHealthAggregationPoliciesSettings settings)
    
    
    public static final RegionHealthAggregationPoliciesClient create(RegionHealthAggregationPoliciesSettings settings)

Constructs an instance of RegionHealthAggregationPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionHealthAggregationPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionHealthAggregationPoliciesStub stub)
    
    
    public static final RegionHealthAggregationPoliciesClient create(RegionHealthAggregationPoliciesStub stub)

Constructs an instance of RegionHealthAggregationPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionHealthAggregationPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionHealthAggregationPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthAggregationPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient)` |   
  
## Constructors 

### RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesSettings settings)
    
    
    protected RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesSettings settings)

Constructs an instance of RegionHealthAggregationPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionHealthAggregationPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesSettings)`  
  
  
### RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesStub stub)
    
    
    protected RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionHealthAggregationPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthAggregationPoliciesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListRegionHealthAggregationPoliciesRequest request)
    
    
    public final RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse aggregatedList(AggregatedListRegionHealthAggregationPoliciesRequest request)

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       AggregatedListRegionHealthAggregationPoliciesRequest request =
           AggregatedListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, HealthAggregationPoliciesScopedList> element :
           regionHealthAggregationPoliciesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthAggregationPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, HealthAggregationPoliciesScopedList> element :
           regionHealthAggregationPoliciesClient.aggregatedList(project).iterateAll()) {
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
`[RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListRegionHealthAggregationPoliciesRequest,HealthAggregationPolicyAggregatedList> aggregatedListCallable()

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       AggregatedListRegionHealthAggregationPoliciesRequest request =
           AggregatedListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         HealthAggregationPolicyAggregatedList response =
             regionHealthAggregationPoliciesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, HealthAggregationPoliciesScopedList> element :
             response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthAggregationPoliciesRequest),[HealthAggregationPolicyAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicyAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListRegionHealthAggregationPoliciesRequest,RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       AggregatedListRegionHealthAggregationPoliciesRequest request =
           AggregatedListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, HealthAggregationPoliciesScopedList>> future =
           regionHealthAggregationPoliciesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, HealthAggregationPoliciesScopedList> element :
           future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthAggregationPoliciesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteRegionHealthAggregationPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionHealthAggregationPolicyRequest request)

Deletes the specified HealthAggregationPolicy in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       DeleteRegionHealthAggregationPolicyRequest request =
           DeleteRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthAggregationPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthAggregationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String healthAggregationPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String healthAggregationPolicy)

Deletes the specified HealthAggregationPolicy in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthAggregationPolicy = "healthAggregationPolicy755484600";
       Operation response =
           regionHealthAggregationPoliciesClient
               .deleteAsync(project, region, healthAggregationPolicy)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthAggregationPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthAggregationPolicy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionHealthAggregationPolicyRequest,Operation> deleteCallable()

Deletes the specified HealthAggregationPolicy in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       DeleteRegionHealthAggregationPolicyRequest request =
           DeleteRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionHealthAggregationPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionHealthAggregationPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified HealthAggregationPolicy in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       DeleteRegionHealthAggregationPolicyRequest request =
           DeleteRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthAggregationPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionHealthAggregationPolicyRequest request)
    
    
    public final HealthAggregationPolicy get(GetRegionHealthAggregationPolicyRequest request)

Returns the specified HealthAggregationPolicy resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       GetRegionHealthAggregationPolicyRequest request =
           GetRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       HealthAggregationPolicy response = regionHealthAggregationPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionHealthAggregationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HealthAggregationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicy)` |   
  
### get(String project, String region, String healthAggregationPolicy)
    
    
    public final HealthAggregationPolicy get(String project, String region, String healthAggregationPolicy)

Returns the specified HealthAggregationPolicy resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthAggregationPolicy = "healthAggregationPolicy755484600";
       HealthAggregationPolicy response =
           regionHealthAggregationPoliciesClient.get(project, region, healthAggregationPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthAggregationPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthAggregationPolicy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[HealthAggregationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionHealthAggregationPolicyRequest,HealthAggregationPolicy> getCallable()

Returns the specified HealthAggregationPolicy resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       GetRegionHealthAggregationPolicyRequest request =
           GetRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<HealthAggregationPolicy> future =
           regionHealthAggregationPoliciesClient.getCallable().futureCall(request);
       // Do something.
       HealthAggregationPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionHealthAggregationPolicyRequest),[HealthAggregationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionHealthAggregationPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionHealthAggregationPoliciesSettings` |   
  
### getStub()
    
    
    public RegionHealthAggregationPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthAggregationPoliciesStub)` |   
  
### insertAsync(InsertRegionHealthAggregationPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionHealthAggregationPolicyRequest request)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       InsertRegionHealthAggregationPolicyRequest request =
           InsertRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthAggregationPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthAggregationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, HealthAggregationPolicy healthAggregationPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, HealthAggregationPolicy healthAggregationPolicyResource)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       HealthAggregationPolicy healthAggregationPolicyResource =
           HealthAggregationPolicy.newBuilder().build();
       Operation response =
           regionHealthAggregationPoliciesClient
               .insertAsync(project, region, healthAggregationPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthAggregationPolicyResource` | `[HealthAggregationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionHealthAggregationPolicyRequest,Operation> insertCallable()

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       InsertRegionHealthAggregationPolicyRequest request =
           InsertRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionHealthAggregationPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionHealthAggregationPolicyRequest,Operation,Operation> insertOperationCallable()

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       InsertRegionHealthAggregationPolicyRequest request =
           InsertRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthAggregationPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionHealthAggregationPoliciesRequest request)
    
    
    public final RegionHealthAggregationPoliciesClient.ListPagedResponse list(ListRegionHealthAggregationPoliciesRequest request)

Lists the HealthAggregationPolicies for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       ListRegionHealthAggregationPoliciesRequest request =
           ListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (HealthAggregationPolicy element :
           regionHealthAggregationPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthAggregationPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthAggregationPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionHealthAggregationPoliciesClient.ListPagedResponse list(String project, String region)

Lists the HealthAggregationPolicies for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (HealthAggregationPolicy element :
           regionHealthAggregationPoliciesClient.list(project, region).iterateAll()) {
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
`[RegionHealthAggregationPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionHealthAggregationPoliciesRequest,HealthAggregationPolicyList> listCallable()

Lists the HealthAggregationPolicies for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       ListRegionHealthAggregationPoliciesRequest request =
           ListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         HealthAggregationPolicyList response =
             regionHealthAggregationPoliciesClient.listCallable().call(request);
         for (HealthAggregationPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthAggregationPoliciesRequest),[HealthAggregationPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionHealthAggregationPoliciesRequest,RegionHealthAggregationPoliciesClient.ListPagedResponse> listPagedCallable()

Lists the HealthAggregationPolicies for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       ListRegionHealthAggregationPoliciesRequest request =
           ListRegionHealthAggregationPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<HealthAggregationPolicy> future =
           regionHealthAggregationPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (HealthAggregationPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionHealthAggregationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthAggregationPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthAggregationPoliciesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionHealthAggregationPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionHealthAggregationPolicyRequest request)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       PatchRegionHealthAggregationPolicyRequest request =
           PatchRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthAggregationPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthAggregationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String healthAggregationPolicy, HealthAggregationPolicy healthAggregationPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String healthAggregationPolicy, HealthAggregationPolicy healthAggregationPolicyResource)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthAggregationPolicy = "healthAggregationPolicy755484600";
       HealthAggregationPolicy healthAggregationPolicyResource =
           HealthAggregationPolicy.newBuilder().build();
       Operation response =
           regionHealthAggregationPoliciesClient
               .patchAsync(project, region, healthAggregationPolicy, healthAggregationPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthAggregationPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthAggregationPolicy to update. The name must be 1-63 characters long, and comply with RFC1035.  
`healthAggregationPolicyResource` | `[HealthAggregationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthAggregationPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionHealthAggregationPolicyRequest,Operation> patchCallable()

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       PatchRegionHealthAggregationPolicyRequest request =
           PatchRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionHealthAggregationPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionHealthAggregationPolicyRequest,Operation,Operation> patchOperationCallable()

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       PatchRegionHealthAggregationPolicyRequest request =
           PatchRegionHealthAggregationPolicyRequest.newBuilder()
               .setHealthAggregationPolicy("healthAggregationPolicy755484600")
               .setHealthAggregationPolicyResource(HealthAggregationPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthAggregationPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthAggregationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionHealthAggregationPolicyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionHealthAggregationPolicyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       TestIamPermissionsRegionHealthAggregationPolicyRequest request =
           TestIamPermissionsRegionHealthAggregationPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response =
           regionHealthAggregationPoliciesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionHealthAggregationPolicyRequest)`  
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
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionHealthAggregationPoliciesClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionHealthAggregationPolicyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthAggregationPoliciesClient regionHealthAggregationPoliciesClient =
         RegionHealthAggregationPoliciesClient.create()) {
       TestIamPermissionsRegionHealthAggregationPolicyRequest request =
           TestIamPermissionsRegionHealthAggregationPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionHealthAggregationPoliciesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionHealthAggregationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionHealthAggregationPolicyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
