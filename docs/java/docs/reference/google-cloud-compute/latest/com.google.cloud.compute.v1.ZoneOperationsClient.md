---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient
title: Class ZoneOperationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:50.308376+00:00
---

# Class ZoneOperationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ZoneOperationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ZoneOperationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ZoneOperations API.

This client uses ZoneOperations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String operation = "operation1662702951";
       DeleteZoneOperationResponse response = zoneOperationsClient.delete(project, zone, operation);
     }
     

Note: close() needs to be called on the ZoneOperationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified zone-specific Operations resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(DeleteZoneOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * delete(String project, String zone, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves the specified zone-specific Operations resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetZoneOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves a list of Operation resources contained within the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListZoneOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Wait |  Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method waits for no more than the 2 minutes and then returns the current state of the operation, which might be `DONE` or still in progress.  This method is called on a best-effort basis. Specifically:  \- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * wait(WaitZoneOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * wait(String project, String zone, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * waitCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ZoneOperationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ZoneOperationsSettings zoneOperationsSettings =
         ZoneOperationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create(zoneOperationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ZoneOperationsSettings zoneOperationsSettings =
         ZoneOperationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create(zoneOperationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ZoneOperationsClient

## Static Methods 

### create()
    
    
    public static final ZoneOperationsClient create()

Constructs an instance of ZoneOperationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ZoneOperationsSettings settings)
    
    
    public static final ZoneOperationsClient create(ZoneOperationsSettings settings)

Constructs an instance of ZoneOperationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ZoneOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ZoneOperationsStub stub)
    
    
    public static final ZoneOperationsClient create(ZoneOperationsStub stub)

Constructs an instance of ZoneOperationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ZoneOperationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ZoneOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneOperationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient)` |   
  
## Constructors 

### ZoneOperationsClient(ZoneOperationsSettings settings)
    
    
    protected ZoneOperationsClient(ZoneOperationsSettings settings)

Constructs an instance of ZoneOperationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ZoneOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsSettings)`  
  
  
### ZoneOperationsClient(ZoneOperationsStub stub)
    
    
    protected ZoneOperationsClient(ZoneOperationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ZoneOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneOperationsStub)`  
  
  
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

### delete(DeleteZoneOperationRequest request)
    
    
    public final DeleteZoneOperationResponse delete(DeleteZoneOperationRequest request)

Deletes the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       DeleteZoneOperationRequest request =
           DeleteZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       DeleteZoneOperationResponse response = zoneOperationsClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteZoneOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneOperationResponse)` |   
  
### delete(String project, String zone, String operation)
    
    
    public final DeleteZoneOperationResponse delete(String project, String zone, String operation)

Deletes the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String operation = "operation1662702951";
       DeleteZoneOperationResponse response = zoneOperationsClient.delete(project, zone, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to delete, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteZoneOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneOperationResponse)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteZoneOperationRequest,DeleteZoneOperationResponse> deleteCallable()

Deletes the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       DeleteZoneOperationRequest request =
           DeleteZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<DeleteZoneOperationResponse> future =
           zoneOperationsClient.deleteCallable().futureCall(request);
       // Do something.
       DeleteZoneOperationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneOperationRequest),[DeleteZoneOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteZoneOperationResponse)>` |   
  
### get(GetZoneOperationRequest request)
    
    
    public final Operation get(GetZoneOperationRequest request)

Retrieves the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       GetZoneOperationRequest request =
           GetZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Operation response = zoneOperationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetZoneOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### get(String project, String zone, String operation)
    
    
    public final Operation get(String project, String zone, String operation)

Retrieves the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String operation = "operation1662702951";
       Operation response = zoneOperationsClient.get(project, zone, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to return, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetZoneOperationRequest,Operation> getCallable()

Retrieves the specified zone-specific Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       GetZoneOperationRequest request =
           GetZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = zoneOperationsClient.getCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetZoneOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getSettings()
    
    
    public final @Nullable ZoneOperationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ZoneOperationsSettings` |   
  
### getStub()
    
    
    public ZoneOperationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ZoneOperationsStub)` |   
  
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
  
### list(ListZoneOperationsRequest request)
    
    
    public final ZoneOperationsClient.ListPagedResponse list(ListZoneOperationsRequest request)

Retrieves a list of Operation resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       ListZoneOperationsRequest request =
           ListZoneOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Operation element : zoneOperationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final ZoneOperationsClient.ListPagedResponse list(String project, String zone)

Retrieves a list of Operation resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (Operation element : zoneOperationsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for request.  
**Returns**  
---  
**Type** | **Description**  
`[ZoneOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListZoneOperationsRequest,OperationList> listCallable()

Retrieves a list of Operation resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       ListZoneOperationsRequest request =
           ListZoneOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         OperationList response = zoneOperationsClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest),[OperationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OperationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListZoneOperationsRequest,ZoneOperationsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of Operation resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       ListZoneOperationsRequest request =
           ListZoneOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = zoneOperationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Operation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListZoneOperationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### wait(WaitZoneOperationRequest request)
    
    
    public final Operation wait(WaitZoneOperationRequest request)

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method waits for no more than the 2 minutes and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       WaitZoneOperationRequest request =
           WaitZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Operation response = zoneOperationsClient.wait(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WaitZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WaitZoneOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### wait(String project, String zone, String operation)
    
    
    public final Operation wait(String project, String zone, String operation)

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method waits for no more than the 2 minutes and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String operation = "operation1662702951";
       Operation response = zoneOperationsClient.wait(project, zone, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to return, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### waitCallable()
    
    
    public final UnaryCallable<WaitZoneOperationRequest,Operation> waitCallable()

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method waits for no more than the 2 minutes and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ZoneOperationsClient zoneOperationsClient = ZoneOperationsClient.create()) {
       WaitZoneOperationRequest request =
           WaitZoneOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = zoneOperationsClient.waitCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WaitZoneOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WaitZoneOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
