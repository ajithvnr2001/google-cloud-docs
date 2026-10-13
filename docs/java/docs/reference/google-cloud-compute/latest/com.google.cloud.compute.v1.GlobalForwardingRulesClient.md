---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient
title: Class GlobalForwardingRulesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:20.576882+00:00
---

# Class GlobalForwardingRulesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalForwardingRulesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalForwardingRulesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalForwardingRules API.

This client uses GlobalForwardingRules version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule response = globalForwardingRulesClient.get(project, forwardingRule);
     }
     

Note: close() needs to be called on the GlobalForwardingRulesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified GlobalForwardingRule resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteGlobalForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String forwardingRule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified GlobalForwardingRule resource. Gets a list of available forwarding rules by making a list() request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalForwardingRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String forwardingRule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a GlobalForwardingRule resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertGlobalForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, ForwardingRule forwardingRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of GlobalForwardingRule resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalForwardingRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchGlobalForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String forwardingRule, ForwardingRule forwardingRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetLabels |  Sets the labels on the specified resource. To learn more about labels, read the Labeling resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsGlobalForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
SetTarget |  Changes target URL for the GlobalForwardingRule resource. The new target should be of the same type as the old target. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setTargetAsync(SetTargetGlobalForwardingRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setTargetAsync(String project, String forwardingRule, TargetReference targetReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setTargetOperationCallable() 
  * setTargetCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalForwardingRulesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalForwardingRulesSettings globalForwardingRulesSettings =
         GlobalForwardingRulesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create(globalForwardingRulesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalForwardingRulesSettings globalForwardingRulesSettings =
         GlobalForwardingRulesSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create(globalForwardingRulesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalForwardingRulesClient

## Static Methods 

### create()
    
    
    public static final GlobalForwardingRulesClient create()

Constructs an instance of GlobalForwardingRulesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalForwardingRulesSettings settings)
    
    
    public static final GlobalForwardingRulesClient create(GlobalForwardingRulesSettings settings)

Constructs an instance of GlobalForwardingRulesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalForwardingRulesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalForwardingRulesStub stub)
    
    
    public static final GlobalForwardingRulesClient create(GlobalForwardingRulesStub stub)

Constructs an instance of GlobalForwardingRulesClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalForwardingRulesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalForwardingRulesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalForwardingRulesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient)` |   
  
## Constructors 

### GlobalForwardingRulesClient(GlobalForwardingRulesSettings settings)
    
    
    protected GlobalForwardingRulesClient(GlobalForwardingRulesSettings settings)

Constructs an instance of GlobalForwardingRulesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalForwardingRulesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesSettings)`  
  
  
### GlobalForwardingRulesClient(GlobalForwardingRulesStub stub)
    
    
    protected GlobalForwardingRulesClient(GlobalForwardingRulesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalForwardingRulesStub)`  
  
  
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

### deleteAsync(DeleteGlobalForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteGlobalForwardingRuleRequest request)

Deletes the specified GlobalForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       DeleteGlobalForwardingRuleRequest request =
           DeleteGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalForwardingRulesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String forwardingRule)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String forwardingRule)

Deletes the specified GlobalForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String forwardingRule = "forwardingRule-1429104743";
       Operation response = globalForwardingRulesClient.deleteAsync(project, forwardingRule).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalForwardingRuleRequest,Operation> deleteCallable()

Deletes the specified GlobalForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       DeleteGlobalForwardingRuleRequest request =
           DeleteGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalForwardingRulesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteGlobalForwardingRuleRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified GlobalForwardingRule resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       DeleteGlobalForwardingRuleRequest request =
           DeleteGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalForwardingRulesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetGlobalForwardingRuleRequest request)
    
    
    public final ForwardingRule get(GetGlobalForwardingRuleRequest request)

Returns the specified GlobalForwardingRule resource. Gets a list of available forwarding rules by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       GetGlobalForwardingRuleRequest request =
           GetGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setView("view3619493")
               .build();
       ForwardingRule response = globalForwardingRulesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)` |   
  
### get(String project, String forwardingRule)
    
    
    public final ForwardingRule get(String project, String forwardingRule)

Returns the specified GlobalForwardingRule resource. Gets a list of available forwarding rules by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule response = globalForwardingRulesClient.get(project, forwardingRule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalForwardingRuleRequest,ForwardingRule> getCallable()

Returns the specified GlobalForwardingRule resource. Gets a list of available forwarding rules by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       GetGlobalForwardingRuleRequest request =
           GetGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setView("view3619493")
               .build();
       ApiFuture<ForwardingRule> future =
           globalForwardingRulesClient.getCallable().futureCall(request);
       // Do something.
       ForwardingRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalForwardingRuleRequest),[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalForwardingRulesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalForwardingRulesSettings` |   
  
### getStub()
    
    
    public GlobalForwardingRulesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalForwardingRulesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalForwardingRulesStub)` |   
  
### insertAsync(InsertGlobalForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertGlobalForwardingRuleRequest request)

Creates a GlobalForwardingRule resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       InsertGlobalForwardingRuleRequest request =
           InsertGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalForwardingRulesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, ForwardingRule forwardingRuleResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, ForwardingRule forwardingRuleResource)

Creates a GlobalForwardingRule resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       ForwardingRule forwardingRuleResource = ForwardingRule.newBuilder().build();
       Operation response =
           globalForwardingRulesClient.insertAsync(project, forwardingRuleResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`forwardingRuleResource` | `[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertGlobalForwardingRuleRequest,Operation> insertCallable()

Creates a GlobalForwardingRule resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       InsertGlobalForwardingRuleRequest request =
           InsertGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalForwardingRulesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertGlobalForwardingRuleRequest,Operation,Operation> insertOperationCallable()

Creates a GlobalForwardingRule resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       InsertGlobalForwardingRuleRequest request =
           InsertGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalForwardingRulesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListGlobalForwardingRulesRequest request)
    
    
    public final GlobalForwardingRulesClient.ListPagedResponse list(ListGlobalForwardingRulesRequest request)

Retrieves a list of GlobalForwardingRule resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       ListGlobalForwardingRulesRequest request =
           ListGlobalForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (ForwardingRule element : globalForwardingRulesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalForwardingRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalForwardingRulesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final GlobalForwardingRulesClient.ListPagedResponse list(String project)

Retrieves a list of GlobalForwardingRule resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       for (ForwardingRule element : globalForwardingRulesClient.list(project).iterateAll()) {
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
`[GlobalForwardingRulesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalForwardingRulesRequest,ForwardingRuleList> listCallable()

Retrieves a list of GlobalForwardingRule resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       ListGlobalForwardingRulesRequest request =
           ListGlobalForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         ForwardingRuleList response = globalForwardingRulesClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalForwardingRulesRequest),[ForwardingRuleList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRuleList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalForwardingRulesRequest,GlobalForwardingRulesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of GlobalForwardingRule resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       ListGlobalForwardingRulesRequest request =
           ListGlobalForwardingRulesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<ForwardingRule> future =
           globalForwardingRulesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ForwardingRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalForwardingRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalForwardingRulesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalForwardingRulesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchGlobalForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchGlobalForwardingRuleRequest request)

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       PatchGlobalForwardingRuleRequest request =
           PatchGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalForwardingRulesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String forwardingRule, ForwardingRule forwardingRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String forwardingRule, ForwardingRule forwardingRuleResource)

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String forwardingRule = "forwardingRule-1429104743";
       ForwardingRule forwardingRuleResource = ForwardingRule.newBuilder().build();
       Operation response =
           globalForwardingRulesClient
               .patchAsync(project, forwardingRule, forwardingRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource to patch.  
`forwardingRuleResource` | `[ForwardingRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ForwardingRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchGlobalForwardingRuleRequest,Operation> patchCallable()

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       PatchGlobalForwardingRuleRequest request =
           PatchGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = globalForwardingRulesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchGlobalForwardingRuleRequest,Operation,Operation> patchOperationCallable()

Updates the specified forwarding rule with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. Currently, you can only patch the network_tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       PatchGlobalForwardingRuleRequest request =
           PatchGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setForwardingRuleResource(ForwardingRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalForwardingRulesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(SetLabelsGlobalForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsGlobalForwardingRuleRequest request)

Sets the labels on the specified resource. To learn more about labels, read the Labeling resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetLabelsGlobalForwardingRuleRequest request =
           SetLabelsGlobalForwardingRuleRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Operation response = globalForwardingRulesClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)

Sets the labels on the specified resource. To learn more about labels, read the Labeling resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetLabelsRequest globalSetLabelsRequestResource =
           GlobalSetLabelsRequest.newBuilder().build();
       Operation response =
           globalForwardingRulesClient
               .setLabelsAsync(project, resource, globalSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsGlobalForwardingRuleRequest,Operation> setLabelsCallable()

Sets the labels on the specified resource. To learn more about labels, read the Labeling resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetLabelsGlobalForwardingRuleRequest request =
           SetLabelsGlobalForwardingRuleRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future =
           globalForwardingRulesClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsGlobalForwardingRuleRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on the specified resource. To learn more about labels, read the Labeling resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetLabelsGlobalForwardingRuleRequest request =
           SetLabelsGlobalForwardingRuleRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           globalForwardingRulesClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetAsync(SetTargetGlobalForwardingRuleRequest request)
    
    
    public final OperationFuture<Operation,Operation> setTargetAsync(SetTargetGlobalForwardingRuleRequest request)

Changes target URL for the GlobalForwardingRule resource. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetTargetGlobalForwardingRuleRequest request =
           SetTargetGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       Operation response = globalForwardingRulesClient.setTargetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetTargetGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetGlobalForwardingRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetAsync(String project, String forwardingRule, TargetReference targetReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setTargetAsync(String project, String forwardingRule, TargetReference targetReferenceResource)

Changes target URL for the GlobalForwardingRule resource. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       String project = "project-309310695";
       String forwardingRule = "forwardingRule-1429104743";
       TargetReference targetReferenceResource = TargetReference.newBuilder().build();
       Operation response =
           globalForwardingRulesClient
               .setTargetAsync(project, forwardingRule, targetReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`forwardingRule` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the ForwardingRule resource in which target is to be set.  
`targetReferenceResource` | `[TargetReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetCallable()
    
    
    public final UnaryCallable<SetTargetGlobalForwardingRuleRequest,Operation> setTargetCallable()

Changes target URL for the GlobalForwardingRule resource. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetTargetGlobalForwardingRuleRequest request =
           SetTargetGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           globalForwardingRulesClient.setTargetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetTargetGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetOperationCallable()
    
    
    public final OperationCallable<SetTargetGlobalForwardingRuleRequest,Operation,Operation> setTargetOperationCallable()

Changes target URL for the GlobalForwardingRule resource. The new target should be of the same type as the old target.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalForwardingRulesClient globalForwardingRulesClient =
         GlobalForwardingRulesClient.create()) {
       SetTargetGlobalForwardingRuleRequest request =
           SetTargetGlobalForwardingRuleRequest.newBuilder()
               .setForwardingRule("forwardingRule-1429104743")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetReferenceResource(TargetReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           globalForwardingRulesClient.setTargetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetTargetGlobalForwardingRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetGlobalForwardingRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
