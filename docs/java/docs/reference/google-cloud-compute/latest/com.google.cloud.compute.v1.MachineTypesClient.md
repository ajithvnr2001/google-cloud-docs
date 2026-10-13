---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient
title: Class MachineTypesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:59.687910+00:00
---

# Class MachineTypesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MachineTypesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/MachineTypesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The MachineTypes API.

This client uses MachineTypes version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String machineType = "machineType-218117087";
       MachineType response = machineTypesClient.get(project, zone, machineType);
     }
     

Note: close() needs to be called on the MachineTypesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of machine types.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListMachineTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Get |  Returns the specified machine type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetMachineTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String machineType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves a list of machine types available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListMachineTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MachineTypesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MachineTypesSettings machineTypesSettings =
         MachineTypesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MachineTypesClient machineTypesClient = MachineTypesClient.create(machineTypesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MachineTypesSettings machineTypesSettings =
         MachineTypesSettings.newBuilder().setEndpoint(myEndpoint).build();
     MachineTypesClient machineTypesClient = MachineTypesClient.create(machineTypesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MachineTypesClient

## Static Methods 

### create()
    
    
    public static final MachineTypesClient create()

Constructs an instance of MachineTypesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MachineTypesSettings settings)
    
    
    public static final MachineTypesClient create(MachineTypesSettings settings)

Constructs an instance of MachineTypesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MachineTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MachineTypesStub stub)
    
    
    public static final MachineTypesClient create(MachineTypesStub stub)

Constructs an instance of MachineTypesClient, using the given stub for making calls. This is for advanced usage - prefer using create(MachineTypesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MachineTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.MachineTypesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient)` |   
  
## Constructors 

### MachineTypesClient(MachineTypesSettings settings)
    
    
    protected MachineTypesClient(MachineTypesSettings settings)

Constructs an instance of MachineTypesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MachineTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesSettings)`  
  
  
### MachineTypesClient(MachineTypesStub stub)
    
    
    protected MachineTypesClient(MachineTypesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MachineTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.MachineTypesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListMachineTypesRequest request)
    
    
    public final MachineTypesClient.AggregatedListPagedResponse aggregatedList(AggregatedListMachineTypesRequest request)

Retrieves an aggregated list of machine types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       AggregatedListMachineTypesRequest request =
           AggregatedListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, MachineTypesScopedList> element :
           machineTypesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListMachineTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final MachineTypesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of machine types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, MachineTypesScopedList> element :
           machineTypesClient.aggregatedList(project).iterateAll()) {
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
`[MachineTypesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListMachineTypesRequest,MachineTypeAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of machine types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       AggregatedListMachineTypesRequest request =
           AggregatedListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         MachineTypeAggregatedList response =
             machineTypesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, MachineTypesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListMachineTypesRequest),[MachineTypeAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypeAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListMachineTypesRequest,MachineTypesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of machine types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       AggregatedListMachineTypesRequest request =
           AggregatedListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, MachineTypesScopedList>> future =
           machineTypesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, MachineTypesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListMachineTypesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.AggregatedListPagedResponse)>` |   
  
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

### get(GetMachineTypeRequest request)
    
    
    public final MachineType get(GetMachineTypeRequest request)

Returns the specified machine type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       GetMachineTypeRequest request =
           GetMachineTypeRequest.newBuilder()
               .setMachineType("machineType-218117087")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       MachineType response = machineTypesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetMachineTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineType)` |   
  
### get(String project, String zone, String machineType)
    
    
    public final MachineType get(String project, String zone, String machineType)

Returns the specified machine type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String machineType = "machineType-218117087";
       MachineType response = machineTypesClient.get(project, zone, machineType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`machineType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the machine type to return.  
**Returns**  
---  
**Type** | **Description**  
`[MachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineType)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetMachineTypeRequest,MachineType> getCallable()

Returns the specified machine type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       GetMachineTypeRequest request =
           GetMachineTypeRequest.newBuilder()
               .setMachineType("machineType-218117087")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<MachineType> future = machineTypesClient.getCallable().futureCall(request);
       // Do something.
       MachineType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetMachineTypeRequest),[MachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineType)>` |   
  
### getSettings()
    
    
    public final @Nullable MachineTypesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.MachineTypesSettings` |   
  
### getStub()
    
    
    public MachineTypesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MachineTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.MachineTypesStub)` |   
  
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
  
### list(ListMachineTypesRequest request)
    
    
    public final MachineTypesClient.ListPagedResponse list(ListMachineTypesRequest request)

Retrieves a list of machine types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       ListMachineTypesRequest request =
           ListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (MachineType element : machineTypesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListMachineTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final MachineTypesClient.ListPagedResponse list(String project, String zone)

Retrieves a list of machine types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (MachineType element : machineTypesClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[MachineTypesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListMachineTypesRequest,MachineTypeList> listCallable()

Retrieves a list of machine types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       ListMachineTypesRequest request =
           ListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         MachineTypeList response = machineTypesClient.listCallable().call(request);
         for (MachineType element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListMachineTypesRequest),[MachineTypeList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypeList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListMachineTypesRequest,MachineTypesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of machine types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MachineTypesClient machineTypesClient = MachineTypesClient.create()) {
       ListMachineTypesRequest request =
           ListMachineTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<MachineType> future = machineTypesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (MachineType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMachineTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListMachineTypesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MachineTypesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
