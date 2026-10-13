---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient
title: Class GlobalOrganizationOperationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:24.222959+00:00
---

# Class GlobalOrganizationOperationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalOrganizationOperationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalOrganizationOperationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalOrganizationOperations API.

This client uses GlobalOrganizationOperations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       String operation = "operation1662702951";
       DeleteGlobalOrganizationOperationResponse response =
           globalOrganizationOperationsClient.delete(operation);
     }
     

Note: close() needs to be called on the GlobalOrganizationOperationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified Operations resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(DeleteGlobalOrganizationOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * delete(String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalOrganizationOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves a list of Operation resources contained within the specified organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalOrganizationOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalOrganizationOperationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalOrganizationOperationsSettings globalOrganizationOperationsSettings =
         GlobalOrganizationOperationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create(globalOrganizationOperationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalOrganizationOperationsSettings globalOrganizationOperationsSettings =
         GlobalOrganizationOperationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create(globalOrganizationOperationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalOrganizationOperationsClient

## Static Methods 

### create()
    
    
    public static final GlobalOrganizationOperationsClient create()

Constructs an instance of GlobalOrganizationOperationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalOrganizationOperationsSettings settings)
    
    
    public static final GlobalOrganizationOperationsClient create(GlobalOrganizationOperationsSettings settings)

Constructs an instance of GlobalOrganizationOperationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalOrganizationOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalOrganizationOperationsStub stub)
    
    
    public static final GlobalOrganizationOperationsClient create(GlobalOrganizationOperationsStub stub)

Constructs an instance of GlobalOrganizationOperationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalOrganizationOperationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalOrganizationOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOrganizationOperationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient)` |   
  
## Constructors 

### GlobalOrganizationOperationsClient(GlobalOrganizationOperationsSettings settings)
    
    
    protected GlobalOrganizationOperationsClient(GlobalOrganizationOperationsSettings settings)

Constructs an instance of GlobalOrganizationOperationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalOrganizationOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsSettings)`  
  
  
### GlobalOrganizationOperationsClient(GlobalOrganizationOperationsStub stub)
    
    
    protected GlobalOrganizationOperationsClient(GlobalOrganizationOperationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalOrganizationOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOrganizationOperationsStub)`  
  
  
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

### delete(DeleteGlobalOrganizationOperationRequest request)
    
    
    public final DeleteGlobalOrganizationOperationResponse delete(DeleteGlobalOrganizationOperationRequest request)

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       DeleteGlobalOrganizationOperationRequest request =
           DeleteGlobalOrganizationOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setParentId("parentId1175162725")
               .build();
       DeleteGlobalOrganizationOperationResponse response =
           globalOrganizationOperationsClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOrganizationOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOrganizationOperationResponse)` |   
  
### delete(String operation)
    
    
    public final DeleteGlobalOrganizationOperationResponse delete(String operation)

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       String operation = "operation1662702951";
       DeleteGlobalOrganizationOperationResponse response =
           globalOrganizationOperationsClient.delete(operation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to delete, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOrganizationOperationResponse)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalOrganizationOperationRequest,DeleteGlobalOrganizationOperationResponse> deleteCallable()

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       DeleteGlobalOrganizationOperationRequest request =
           DeleteGlobalOrganizationOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<DeleteGlobalOrganizationOperationResponse> future =
           globalOrganizationOperationsClient.deleteCallable().futureCall(request);
       // Do something.
       DeleteGlobalOrganizationOperationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOrganizationOperationRequest),[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOrganizationOperationResponse)>` |   
  
### get(GetGlobalOrganizationOperationRequest request)
    
    
    public final Operation get(GetGlobalOrganizationOperationRequest request)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       GetGlobalOrganizationOperationRequest request =
           GetGlobalOrganizationOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setParentId("parentId1175162725")
               .build();
       Operation response = globalOrganizationOperationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalOrganizationOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### get(String operation)
    
    
    public final Operation get(String operation)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       String operation = "operation1662702951";
       Operation response = globalOrganizationOperationsClient.get(operation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to return. Parent is derived from this field.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalOrganizationOperationRequest,Operation> getCallable()

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       GetGlobalOrganizationOperationRequest request =
           GetGlobalOrganizationOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<Operation> future =
           globalOrganizationOperationsClient.getCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalOrganizationOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalOrganizationOperationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalOrganizationOperationsSettings` |   
  
### getStub()
    
    
    public GlobalOrganizationOperationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOrganizationOperationsStub)` |   
  
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
  
### list()
    
    
    public final GlobalOrganizationOperationsClient.ListPagedResponse list()

Retrieves a list of Operation resources contained within the specified organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       for (Operation element : globalOrganizationOperationsClient.list().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient.ListPagedResponse)` |   
  
### list(ListGlobalOrganizationOperationsRequest request)
    
    
    public final GlobalOrganizationOperationsClient.ListPagedResponse list(ListGlobalOrganizationOperationsRequest request)

Retrieves a list of Operation resources contained within the specified organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       ListGlobalOrganizationOperationsRequest request =
           ListGlobalOrganizationOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       for (Operation element : globalOrganizationOperationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOrganizationOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalOrganizationOperationsRequest,OperationList> listCallable()

Retrieves a list of Operation resources contained within the specified organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       ListGlobalOrganizationOperationsRequest request =
           ListGlobalOrganizationOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       while (true) {
         OperationList response = globalOrganizationOperationsClient.listCallable().call(request);
         for (Operation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOrganizationOperationsRequest),[OperationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OperationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalOrganizationOperationsRequest,GlobalOrganizationOperationsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of Operation resources contained within the specified organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOrganizationOperationsClient globalOrganizationOperationsClient =
         GlobalOrganizationOperationsClient.create()) {
       ListGlobalOrganizationOperationsRequest request =
           ListGlobalOrganizationOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<Operation> future =
           globalOrganizationOperationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Operation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOrganizationOperationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationOperationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
