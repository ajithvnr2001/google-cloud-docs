---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient
title: Class ForwardingRulesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:37.876248+00:00
---

# Class ForwardingRulesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ForwardingRulesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ForwardingRulesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ForwardingRules API.

This client uses ForwardingRules version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule response = forwardingRulesClient.get(project, region, forwardingRule);
     }
     

Note: close() needs to be called on the ForwardingRulesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of forwarding rules.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListForwardingRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified ForwardingRule resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String forwardingRule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified ForwardingRule resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetForwardingRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String forwardingRule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a ForwardingRule resource in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, ForwardingRule forwardingRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of ForwardingRule resources available to the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListForwardingRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String forwardingRule, ForwardingRule forwardingRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetLabels |  Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
SetTarget |  Changes target URL for forwarding rule. The new target should be of the same type as the old target. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setTargetAsync(SetTargetForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setTargetAsync(String project, String region, String forwardingRule, TargetReference targetReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setTargetOperationCallable() 
  * setTargetCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ForwardingRulesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ForwardingRulesSettings forwardingRulesSettings =
         ForwardingRulesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ForwardingRulesClient forwardingRulesClient =
         ForwardingRulesClient.create(forwardingRulesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ForwardingRulesSettings forwardingRulesSettings =
         ForwardingRulesSettings.newBuilder().setEndpoint(myEndpoint).build();
     ForwardingRulesClient forwardingRulesClient =
         ForwardingRulesClient.create(forwardingRulesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ForwardingRulesClient

## Static Methods 

### create()
    
    
    public static final ForwardingRulesClient create()

Constructs an instance of ForwardingRulesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ForwardingRulesSettings settings)
    
    
    public static final ForwardingRulesClient create(ForwardingRulesSettings settings)

Constructs an instance of ForwardingRulesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ForwardingRulesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ForwardingRulesStub stub)
    
    
    public static final ForwardingRulesClient create(ForwardingRulesStub stub)

Constructs an instance of ForwardingRulesClient, using the given stub for making calls. This is for advanced usage - prefer using create(ForwardingRulesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ForwardingRulesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient)` |   
  
## Constructors 

### ForwardingRulesClient(ForwardingRulesSettings settings)
    
    
    protected ForwardingRulesClient(ForwardingRulesSettings settings)

Constructs an instance of ForwardingRulesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ForwardingRulesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesSettings)`  
  
  
### ForwardingRulesClient(ForwardingRulesStub stub)
    
    
    protected ForwardingRulesClient(ForwardingRulesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ForwardingRulesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListForwardingRulesRequest request)
    
    
    public final ForwardingRulesClient.AggregatedListPagedResponse aggregatedList(AggregatedListForwardingRulesRequest request)

Retrieves an aggregated list of forwarding rules.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       AggregatedListForwardingRulesRequest request =
           AggregatedListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, ForwardingRulesScopedList> element :
           forwardingRulesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListForwardingRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final ForwardingRulesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of forwarding rules.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, ForwardingRulesScopedList> element :
           forwardingRulesClient.aggregatedList(project).iterateAll()) {
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
`[ForwardingRulesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListForwardingRulesRequest,ForwardingRuleAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of forwarding rules.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       AggregatedListForwardingRulesRequest request =
           AggregatedListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         ForwardingRuleAggregatedList response =
             forwardingRulesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, ForwardingRulesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListForwardingRulesRequest),[ForwardingRuleAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRuleAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListForwardingRulesRequest,ForwardingRulesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of forwarding rules.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       AggregatedListForwardingRulesRequest request =
           AggregatedListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, ForwardingRulesScopedList>> future =
           forwardingRulesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, ForwardingRulesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListForwardingRulesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteForwardingRuleRequest request)

Deletes the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       DeleteForwardingRuleRequest request =
           DeleteForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = forwardingRulesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String forwardingRule)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String forwardingRule)

Deletes the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String forwardingRule = "forwardingRule-1429104743";
       Operation response = forwardingRulesClient.deleteAsync(project, region, forwardingRule).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteForwardingRuleRequest,Operation> deleteCallable()

Deletes the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       DeleteForwardingRuleRequest request =
           DeleteForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = forwardingRulesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteForwardingRuleRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       DeleteForwardingRuleRequest request =
           DeleteForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           forwardingRulesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetForwardingRuleRequest request)
    
    
    public final ForwardingRule get(GetForwardingRuleRequest request)

Returns the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       GetForwardingRuleRequest request =
           GetForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setView("view3619493")
               .build();
       ForwardingRule response = forwardingRulesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)` |   
  
### get(String project, String region, String forwardingRule)
    
    
    public final ForwardingRule get(String project, String region, String forwardingRule)

Returns the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule response = forwardingRulesClient.get(project, region, forwardingRule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetForwardingRuleRequest,ForwardingRule> getCallable()

Returns the specified ForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       GetForwardingRuleRequest request =
           GetForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setView("view3619493")
               .build();
       ApiFuture<ForwardingRule> future = forwardingRulesClient.getCallable().futureCall(request);
       // Do something.
       ForwardingRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetForwardingRuleRequest),[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)>` |   
  
### getSettings()
    
    
    public final @Nullable ForwardingRulesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ForwardingRulesSettings` |   
  
### getStub()
    
    
    public ForwardingRulesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ForwardingRulesStub)` |   
  
### insertAsync(InsertForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertForwardingRuleRequest request)

Creates a ForwardingRule resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       InsertForwardingRuleRequest request =
           InsertForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = forwardingRulesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, ForwardingRule forwardingRuleResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, ForwardingRule forwardingRuleResource)

Creates a ForwardingRule resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       ForwardingRule forwardingRuleResource = ForwardingRule.newBuilder().build();
       Operation response =
           forwardingRulesClient.insertAsync(project, region, forwardingRuleResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`forwardingRuleResource` | `[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertForwardingRuleRequest,Operation> insertCallable()

Creates a ForwardingRule resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       InsertForwardingRuleRequest request =
           InsertForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = forwardingRulesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertForwardingRuleRequest,Operation,Operation> insertOperationCallable()

Creates a ForwardingRule resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       InsertForwardingRuleRequest request =
           InsertForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           forwardingRulesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListForwardingRulesRequest request)
    
    
    public final ForwardingRulesClient.ListPagedResponse list(ListForwardingRulesRequest request)

Retrieves a list of ForwardingRule resources available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       ListForwardingRulesRequest request =
           ListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (ForwardingRule element : forwardingRulesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListForwardingRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRulesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final ForwardingRulesClient.ListPagedResponse list(String project, String region)

Retrieves a list of ForwardingRule resources available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (ForwardingRule element : forwardingRulesClient.list(project, region).iterateAll()) {
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
`[ForwardingRulesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListForwardingRulesRequest,ForwardingRuleList> listCallable()

Retrieves a list of ForwardingRule resources available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       ListForwardingRulesRequest request =
           ListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         ForwardingRuleList response = forwardingRulesClient.listCallable().call(request);
         for (ForwardingRule element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListForwardingRulesRequest),[ForwardingRuleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRuleList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListForwardingRulesRequest,ForwardingRulesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of ForwardingRule resources available to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       ListForwardingRulesRequest request =
           ListForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<ForwardingRule> future =
           forwardingRulesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ForwardingRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListForwardingRulesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRulesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchForwardingRuleRequest request)

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       PatchForwardingRuleRequest request =
           PatchForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = forwardingRulesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String forwardingRule, ForwardingRule forwardingRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String forwardingRule, ForwardingRule forwardingRuleResource)

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule forwardingRuleResource = ForwardingRule.newBuilder().build();
       Operation response =
           forwardingRulesClient
               .patchAsync(project, region, forwardingRule, forwardingRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to patch.  
`forwardingRuleResource` | `[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchForwardingRuleRequest,Operation> patchCallable()

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       PatchForwardingRuleRequest request =
           PatchForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = forwardingRulesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchForwardingRuleRequest,Operation,Operation> patchOperationCallable()

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       PatchForwardingRuleRequest request =
           PatchForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           forwardingRulesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(SetLabelsForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsForwardingRuleRequest request)

Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetLabelsForwardingRuleRequest request =
           SetLabelsForwardingRuleRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       Operation response = forwardingRulesClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)

Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetLabelsRequest regionSetLabelsRequestResource =
           RegionSetLabelsRequest.newBuilder().build();
       Operation response =
           forwardingRulesClient
               .setLabelsAsync(project, region, resource, regionSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsForwardingRuleRequest,Operation> setLabelsCallable()

Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetLabelsForwardingRuleRequest request =
           SetLabelsForwardingRuleRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future = forwardingRulesClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsForwardingRuleRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on the specified resource. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetLabelsForwardingRuleRequest request =
           SetLabelsForwardingRuleRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           forwardingRulesClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetAsync(SetTargetForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> setTargetAsync(SetTargetForwardingRuleRequest request)

Changes target URL for forwarding rule. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetTargetForwardingRuleRequest request =
           SetTargetForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       Operation response = forwardingRulesClient.setTargetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetTargetForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetAsync(String project, String region, String forwardingRule, TargetReference targetReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setTargetAsync(String project, String region, String forwardingRule, TargetReference targetReferenceResource)

Changes target URL for forwarding rule. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String forwardingRule = "forwardingRule-1429104743";
       TargetReference targetReferenceResource = TargetReference.newBuilder().build();
       Operation response =
           forwardingRulesClient
               .setTargetAsync(project, region, forwardingRule, targetReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource in which target is to be set.  
`targetReferenceResource` | `[TargetReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetCallable()
    
    
    public final UnaryCallable<SetTargetForwardingRuleRequest,Operation> setTargetCallable()

Changes target URL for forwarding rule. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetTargetForwardingRuleRequest request =
           SetTargetForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future = forwardingRulesClient.setTargetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetTargetForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetOperationCallable()
    
    
    public final OperationCallable<SetTargetForwardingRuleRequest,Operation,Operation> setTargetOperationCallable()

Changes target URL for forwarding rule. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ForwardingRulesClient forwardingRulesClient = ForwardingRulesClient.create()) {
       SetTargetForwardingRuleRequest request =
           SetTargetForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           forwardingRulesClient.setTargetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetTargetForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
