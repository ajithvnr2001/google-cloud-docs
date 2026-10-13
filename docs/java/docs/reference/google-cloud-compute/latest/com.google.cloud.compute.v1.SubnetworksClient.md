---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient
title: Class SubnetworksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:32.086149+00:00
---

# Class SubnetworksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SubnetworksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/SubnetworksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Subnetworks API.

This client uses Subnetworks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       Subnetwork response = subnetworksClient.get(project, region, subnetwork);
     }
     

Note: close() needs to be called on the SubnetworksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of subnetworks.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListSubnetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified subnetwork. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteSubnetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String subnetwork) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
ExpandIpCidrRange |  Expands the IP CIDR range of the subnetwork to a specified value. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * expandIpCidrRangeAsync(ExpandIpCidrRangeSubnetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * expandIpCidrRangeAsync(String project, String region, String subnetwork, SubnetworksExpandIpCidrRangeRequest subnetworksExpandIpCidrRangeRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * expandIpCidrRangeOperationCallable() 
  * expandIpCidrRangeCallable() 

  
Get |  Returns the specified subnetwork. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetSubnetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String subnetwork) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicySubnetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String region, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a subnetwork in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertSubnetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, Subnetwork subnetworkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of subnetworks available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListSubnetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListUsable |  Retrieves an aggregated list of all usable subnetworks in the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUsable(ListUsableSubnetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUsable(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUsablePagedCallable() 
  * listUsableCallable() 

  
Patch |  Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchSubnetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String subnetwork, Subnetwork subnetworkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicySubnetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetPrivateIpGoogleAccess |  Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setPrivateIpGoogleAccessAsync(SetPrivateIpGoogleAccessSubnetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setPrivateIpGoogleAccessAsync(String project, String region, String subnetwork, SubnetworksSetPrivateIpGoogleAccessRequest subnetworksSetPrivateIpGoogleAccessRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setPrivateIpGoogleAccessOperationCallable() 
  * setPrivateIpGoogleAccessCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsSubnetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SubnetworksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SubnetworksSettings subnetworksSettings =
         SubnetworksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SubnetworksClient subnetworksClient = SubnetworksClient.create(subnetworksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SubnetworksSettings subnetworksSettings =
         SubnetworksSettings.newBuilder().setEndpoint(myEndpoint).build();
     SubnetworksClient subnetworksClient = SubnetworksClient.create(subnetworksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SubnetworksClient

## Static Methods 

### create()
    
    
    public static final SubnetworksClient create()

Constructs an instance of SubnetworksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SubnetworksSettings settings)
    
    
    public static final SubnetworksClient create(SubnetworksSettings settings)

Constructs an instance of SubnetworksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SubnetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SubnetworksStub stub)
    
    
    public static final SubnetworksClient create(SubnetworksStub stub)

Constructs an instance of SubnetworksClient, using the given stub for making calls. This is for advanced usage - prefer using create(SubnetworksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SubnetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SubnetworksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient)` |   
  
## Constructors 

### SubnetworksClient(SubnetworksSettings settings)
    
    
    protected SubnetworksClient(SubnetworksSettings settings)

Constructs an instance of SubnetworksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SubnetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksSettings)`  
  
  
### SubnetworksClient(SubnetworksStub stub)
    
    
    protected SubnetworksClient(SubnetworksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SubnetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SubnetworksStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListSubnetworksRequest request)
    
    
    public final SubnetworksClient.AggregatedListPagedResponse aggregatedList(AggregatedListSubnetworksRequest request)

Retrieves an aggregated list of subnetworks.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       AggregatedListSubnetworksRequest request =
           AggregatedListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .setViews("views112204398")
               .build();
       for (Map.Entry<String, SubnetworksScopedList> element :
           subnetworksClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListSubnetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final SubnetworksClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of subnetworks.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, SubnetworksScopedList> element :
           subnetworksClient.aggregatedList(project).iterateAll()) {
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
`[SubnetworksClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListSubnetworksRequest,SubnetworkAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of subnetworks.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       AggregatedListSubnetworksRequest request =
           AggregatedListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .setViews("views112204398")
               .build();
       while (true) {
         SubnetworkAggregatedList response =
             subnetworksClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, SubnetworksScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListSubnetworksRequest),[SubnetworkAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworkAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListSubnetworksRequest,SubnetworksClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of subnetworks.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       AggregatedListSubnetworksRequest request =
           AggregatedListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .setViews("views112204398")
               .build();
       ApiFuture<Map.Entry<String, SubnetworksScopedList>> future =
           subnetworksClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, SubnetworksScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListSubnetworksRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteSubnetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteSubnetworkRequest request)

Deletes the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       DeleteSubnetworkRequest request =
           DeleteSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .build();
       Operation response = subnetworksClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String subnetwork)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String subnetwork)

Deletes the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       Operation response = subnetworksClient.deleteAsync(project, region, subnetwork).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Subnetwork resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteSubnetworkRequest,Operation> deleteCallable()

Deletes the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       DeleteSubnetworkRequest request =
           DeleteSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .build();
       ApiFuture<Operation> future = subnetworksClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteSubnetworkRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       DeleteSubnetworkRequest request =
           DeleteSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .build();
       OperationFuture<Operation, Operation> future =
           subnetworksClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### expandIpCidrRangeAsync(ExpandIpCidrRangeSubnetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> expandIpCidrRangeAsync(ExpandIpCidrRangeSubnetworkRequest request)

Expands the IP CIDR range of the subnetwork to a specified value.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ExpandIpCidrRangeSubnetworkRequest request =
           ExpandIpCidrRangeSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksExpandIpCidrRangeRequestResource(
                   SubnetworksExpandIpCidrRangeRequest.newBuilder().build())
               .build();
       Operation response = subnetworksClient.expandIpCidrRangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExpandIpCidrRangeSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExpandIpCidrRangeSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### expandIpCidrRangeAsync(String project, String region, String subnetwork, SubnetworksExpandIpCidrRangeRequest subnetworksExpandIpCidrRangeRequestResource)
    
    
    public final OperationFuture<Operation,Operation> expandIpCidrRangeAsync(String project, String region, String subnetwork, SubnetworksExpandIpCidrRangeRequest subnetworksExpandIpCidrRangeRequestResource)

Expands the IP CIDR range of the subnetwork to a specified value.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       SubnetworksExpandIpCidrRangeRequest subnetworksExpandIpCidrRangeRequestResource =
           SubnetworksExpandIpCidrRangeRequest.newBuilder().build();
       Operation response =
           subnetworksClient
               .expandIpCidrRangeAsync(
                   project, region, subnetwork, subnetworksExpandIpCidrRangeRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Subnetwork resource to update.  
`subnetworksExpandIpCidrRangeRequestResource` | `[SubnetworksExpandIpCidrRangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksExpandIpCidrRangeRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### expandIpCidrRangeCallable()
    
    
    public final UnaryCallable<ExpandIpCidrRangeSubnetworkRequest,Operation> expandIpCidrRangeCallable()

Expands the IP CIDR range of the subnetwork to a specified value.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ExpandIpCidrRangeSubnetworkRequest request =
           ExpandIpCidrRangeSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksExpandIpCidrRangeRequestResource(
                   SubnetworksExpandIpCidrRangeRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           subnetworksClient.expandIpCidrRangeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExpandIpCidrRangeSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExpandIpCidrRangeSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### expandIpCidrRangeOperationCallable()
    
    
    public final OperationCallable<ExpandIpCidrRangeSubnetworkRequest,Operation,Operation> expandIpCidrRangeOperationCallable()

Expands the IP CIDR range of the subnetwork to a specified value.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ExpandIpCidrRangeSubnetworkRequest request =
           ExpandIpCidrRangeSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksExpandIpCidrRangeRequestResource(
                   SubnetworksExpandIpCidrRangeRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           subnetworksClient.expandIpCidrRangeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExpandIpCidrRangeSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExpandIpCidrRangeSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetSubnetworkRequest request)
    
    
    public final Subnetwork get(GetSubnetworkRequest request)

Returns the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       GetSubnetworkRequest request =
           GetSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSubnetwork("subnetwork-1302785042")
               .setViews("views112204398")
               .build();
       Subnetwork response = subnetworksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Subnetwork)` |   
  
### get(String project, String region, String subnetwork)
    
    
    public final Subnetwork get(String project, String region, String subnetwork)

Returns the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       Subnetwork response = subnetworksClient.get(project, region, subnetwork);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Subnetwork resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[Subnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Subnetwork)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetSubnetworkRequest,Subnetwork> getCallable()

Returns the specified subnetwork.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       GetSubnetworkRequest request =
           GetSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSubnetwork("subnetwork-1302785042")
               .setViews("views112204398")
               .build();
       ApiFuture<Subnetwork> future = subnetworksClient.getCallable().futureCall(request);
       // Do something.
       Subnetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSubnetworkRequest),[Subnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Subnetwork)>` |   
  
### getIamPolicy(GetIamPolicySubnetworkRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicySubnetworkRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       GetIamPolicySubnetworkRequest request =
           GetIamPolicySubnetworkRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       Policy response = subnetworksClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicySubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicySubnetworkRequest)`  
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
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       Policy response = subnetworksClient.getIamPolicy(project, region, resource);
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
    
    
    public final UnaryCallable<GetIamPolicySubnetworkRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       GetIamPolicySubnetworkRequest request =
           GetIamPolicySubnetworkRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = subnetworksClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicySubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicySubnetworkRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable SubnetworksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.SubnetworksSettings` |   
  
### getStub()
    
    
    public SubnetworksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SubnetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SubnetworksStub)` |   
  
### insertAsync(InsertSubnetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertSubnetworkRequest request)

Creates a subnetwork in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       InsertSubnetworkRequest request =
           InsertSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       Operation response = subnetworksClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, Subnetwork subnetworkResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, Subnetwork subnetworkResource)

Creates a subnetwork in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Subnetwork subnetworkResource = Subnetwork.newBuilder().build();
       Operation response = subnetworksClient.insertAsync(project, region, subnetworkResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetworkResource` | `[Subnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Subnetwork)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertSubnetworkRequest,Operation> insertCallable()

Creates a subnetwork in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       InsertSubnetworkRequest request =
           InsertSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       ApiFuture<Operation> future = subnetworksClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertSubnetworkRequest,Operation,Operation> insertOperationCallable()

Creates a subnetwork in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       InsertSubnetworkRequest request =
           InsertSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           subnetworksClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListSubnetworksRequest request)
    
    
    public final SubnetworksClient.ListPagedResponse list(ListSubnetworksRequest request)

Retrieves a list of subnetworks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListSubnetworksRequest request =
           ListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setViews("views112204398")
               .build();
       for (Subnetwork element : subnetworksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSubnetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final SubnetworksClient.ListPagedResponse list(String project, String region)

Retrieves a list of subnetworks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (Subnetwork element : subnetworksClient.list(project, region).iterateAll()) {
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
`[SubnetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListSubnetworksRequest,SubnetworkList> listCallable()

Retrieves a list of subnetworks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListSubnetworksRequest request =
           ListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setViews("views112204398")
               .build();
       while (true) {
         SubnetworkList response = subnetworksClient.listCallable().call(request);
         for (Subnetwork element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSubnetworksRequest),[SubnetworkList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworkList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListSubnetworksRequest,SubnetworksClient.ListPagedResponse> listPagedCallable()

Retrieves a list of subnetworks available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListSubnetworksRequest request =
           ListSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setViews("views112204398")
               .build();
       ApiFuture<Subnetwork> future = subnetworksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Subnetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSubnetworksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListPagedResponse)>` |   
  
### listUsable(ListUsableSubnetworksRequest request)
    
    
    public final SubnetworksClient.ListUsablePagedResponse listUsable(ListUsableSubnetworksRequest request)

Retrieves an aggregated list of all usable subnetworks in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProject("serviceProject1947145892")
               .build();
       for (UsableSubnetwork element : subnetworksClient.listUsable(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableSubnetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SubnetworksClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListUsablePagedResponse)` |   
  
### listUsable(String project)
    
    
    public final SubnetworksClient.ListUsablePagedResponse listUsable(String project)

Retrieves an aggregated list of all usable subnetworks in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       for (UsableSubnetwork element : subnetworksClient.listUsable(project).iterateAll()) {
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
`[SubnetworksClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListUsablePagedResponse)` |   
  
### listUsableCallable()
    
    
    public final UnaryCallable<ListUsableSubnetworksRequest,UsableSubnetworksAggregatedList> listUsableCallable()

Retrieves an aggregated list of all usable subnetworks in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProject("serviceProject1947145892")
               .build();
       while (true) {
         UsableSubnetworksAggregatedList response =
             subnetworksClient.listUsableCallable().call(request);
         for (UsableSubnetwork element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableSubnetworksRequest),[UsableSubnetworksAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsableSubnetworksAggregatedList)>` |   
  
### listUsablePagedCallable()
    
    
    public final UnaryCallable<ListUsableSubnetworksRequest,SubnetworksClient.ListUsablePagedResponse> listUsablePagedCallable()

Retrieves an aggregated list of all usable subnetworks in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       ListUsableSubnetworksRequest request =
           ListUsableSubnetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProject("serviceProject1947145892")
               .build();
       ApiFuture<UsableSubnetwork> future =
           subnetworksClient.listUsablePagedCallable().futureCall(request);
       // Do something.
       for (UsableSubnetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableSubnetworksRequest),[ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksClient.ListUsablePagedResponse)>` |   
  
### patchAsync(PatchSubnetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchSubnetworkRequest request)

Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       PatchSubnetworkRequest request =
           PatchSubnetworkRequest.newBuilder()
               .setDrainTimeoutSeconds(1431448922)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       Operation response = subnetworksClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String subnetwork, Subnetwork subnetworkResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String subnetwork, Subnetwork subnetworkResource)

Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       Subnetwork subnetworkResource = Subnetwork.newBuilder().build();
       Operation response =
           subnetworksClient.patchAsync(project, region, subnetwork, subnetworkResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Subnetwork resource to patch.  
`subnetworkResource` | `[Subnetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Subnetwork)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchSubnetworkRequest,Operation> patchCallable()

Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       PatchSubnetworkRequest request =
           PatchSubnetworkRequest.newBuilder()
               .setDrainTimeoutSeconds(1431448922)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       ApiFuture<Operation> future = subnetworksClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchSubnetworkRequest,Operation,Operation> patchOperationCallable()

Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       PatchSubnetworkRequest request =
           PatchSubnetworkRequest.newBuilder()
               .setDrainTimeoutSeconds(1431448922)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworkResource(Subnetwork.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           subnetworksClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicySubnetworkRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicySubnetworkRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       SetIamPolicySubnetworkRequest request =
           SetIamPolicySubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = subnetworksClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicySubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicySubnetworkRequest)`  
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
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetPolicyRequest regionSetPolicyRequestResource =
           RegionSetPolicyRequest.newBuilder().build();
       Policy response =
           subnetworksClient.setIamPolicy(project, region, resource, regionSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicySubnetworkRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       SetIamPolicySubnetworkRequest request =
           SetIamPolicySubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = subnetworksClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicySubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicySubnetworkRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setPrivateIpGoogleAccessAsync(SetPrivateIpGoogleAccessSubnetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> setPrivateIpGoogleAccessAsync(SetPrivateIpGoogleAccessSubnetworkRequest request)

Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       SetPrivateIpGoogleAccessSubnetworkRequest request =
           SetPrivateIpGoogleAccessSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksSetPrivateIpGoogleAccessRequestResource(
                   SubnetworksSetPrivateIpGoogleAccessRequest.newBuilder().build())
               .build();
       Operation response = subnetworksClient.setPrivateIpGoogleAccessAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetPrivateIpGoogleAccessSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetPrivateIpGoogleAccessSubnetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setPrivateIpGoogleAccessAsync(String project, String region, String subnetwork, SubnetworksSetPrivateIpGoogleAccessRequest subnetworksSetPrivateIpGoogleAccessRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setPrivateIpGoogleAccessAsync(String project, String region, String subnetwork, SubnetworksSetPrivateIpGoogleAccessRequest subnetworksSetPrivateIpGoogleAccessRequestResource)

Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String subnetwork = "subnetwork-1302785042";
       SubnetworksSetPrivateIpGoogleAccessRequest
           subnetworksSetPrivateIpGoogleAccessRequestResource =
               SubnetworksSetPrivateIpGoogleAccessRequest.newBuilder().build();
       Operation response =
           subnetworksClient
               .setPrivateIpGoogleAccessAsync(
                   project, region, subnetwork, subnetworksSetPrivateIpGoogleAccessRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`subnetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Subnetwork resource.  
`subnetworksSetPrivateIpGoogleAccessRequestResource` | `[SubnetworksSetPrivateIpGoogleAccessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SubnetworksSetPrivateIpGoogleAccessRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setPrivateIpGoogleAccessCallable()
    
    
    public final UnaryCallable<SetPrivateIpGoogleAccessSubnetworkRequest,Operation> setPrivateIpGoogleAccessCallable()

Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       SetPrivateIpGoogleAccessSubnetworkRequest request =
           SetPrivateIpGoogleAccessSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksSetPrivateIpGoogleAccessRequestResource(
                   SubnetworksSetPrivateIpGoogleAccessRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           subnetworksClient.setPrivateIpGoogleAccessCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetPrivateIpGoogleAccessSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetPrivateIpGoogleAccessSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setPrivateIpGoogleAccessOperationCallable()
    
    
    public final OperationCallable<SetPrivateIpGoogleAccessSubnetworkRequest,Operation,Operation> setPrivateIpGoogleAccessOperationCallable()

Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       SetPrivateIpGoogleAccessSubnetworkRequest request =
           SetPrivateIpGoogleAccessSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSubnetwork("subnetwork-1302785042")
               .setSubnetworksSetPrivateIpGoogleAccessRequestResource(
                   SubnetworksSetPrivateIpGoogleAccessRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           subnetworksClient.setPrivateIpGoogleAccessOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetPrivateIpGoogleAccessSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetPrivateIpGoogleAccessSubnetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsSubnetworkRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsSubnetworkRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       TestIamPermissionsSubnetworkRequest request =
           TestIamPermissionsSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = subnetworksClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsSubnetworkRequest)`  
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
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           subnetworksClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsSubnetworkRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SubnetworksClient subnetworksClient = SubnetworksClient.create()) {
       TestIamPermissionsSubnetworkRequest request =
           TestIamPermissionsSubnetworkRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           subnetworksClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsSubnetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsSubnetworkRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
