---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceClient
title: Class AdviceClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:50.417457+00:00
---

# Class AdviceClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdviceClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/AdviceClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Advice API.

This client uses Advice version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       CalendarModeAdviceRequest calendarModeAdviceRequestResource =
           CalendarModeAdviceRequest.newBuilder().build();
       CalendarModeAdviceResponse response =
           adviceClient.calendarMode(project, region, calendarModeAdviceRequestResource);
     }
     

Note: close() needs to be called on the AdviceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CalendarMode |  Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * calendarMode(CalendarModeAdviceRpcRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * calendarMode(String project, String region, CalendarModeAdviceRequest calendarModeAdviceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * calendarModeCallable() 

  
Capacity |  Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * capacity(CapacityAdviceRpcRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * capacity(String project, String region, CapacityAdviceRequest capacityAdviceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * capacityCallable() 

  
CapacityHistory |  Gets the capacity history. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * capacityHistory(CapacityHistoryAdviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * capacityHistory(String project, String region, CapacityHistoryRequest capacityHistoryRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * capacityHistoryCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdviceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdviceSettings adviceSettings =
         AdviceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdviceClient adviceClient = AdviceClient.create(adviceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdviceSettings adviceSettings = AdviceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdviceClient adviceClient = AdviceClient.create(adviceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdviceClient

## Static Methods 

### create()
    
    
    public static final AdviceClient create()

Constructs an instance of AdviceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdviceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdviceSettings settings)
    
    
    public static final AdviceClient create(AdviceSettings settings)

Constructs an instance of AdviceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdviceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdviceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdviceStub stub)
    
    
    public static final AdviceClient create(AdviceStub stub)

Constructs an instance of AdviceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdviceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdviceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AdviceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdviceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceClient)` |   
  
## Constructors 

### AdviceClient(AdviceSettings settings)
    
    
    protected AdviceClient(AdviceSettings settings)

Constructs an instance of AdviceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdviceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdviceSettings)`  
  
  
### AdviceClient(AdviceStub stub)
    
    
    protected AdviceClient(AdviceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdviceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AdviceStub)`  
  
  
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
  
### calendarMode(CalendarModeAdviceRpcRequest request)
    
    
    public final CalendarModeAdviceResponse calendarMode(CalendarModeAdviceRpcRequest request)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CalendarModeAdviceRpcRequest request =
           CalendarModeAdviceRpcRequest.newBuilder()
               .setCalendarModeAdviceRequestResource(CalendarModeAdviceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       CalendarModeAdviceResponse response = adviceClient.calendarMode(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceResponse)` |   
  
### calendarMode(String project, String region, CalendarModeAdviceRequest calendarModeAdviceRequestResource)
    
    
    public final CalendarModeAdviceResponse calendarMode(String project, String region, CalendarModeAdviceRequest calendarModeAdviceRequestResource)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       CalendarModeAdviceRequest calendarModeAdviceRequestResource =
           CalendarModeAdviceRequest.newBuilder().build();
       CalendarModeAdviceResponse response =
           adviceClient.calendarMode(project, region, calendarModeAdviceRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`calendarModeAdviceRequestResource` | `[CalendarModeAdviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceResponse)` |   
  
### calendarModeCallable()
    
    
    public final UnaryCallable<CalendarModeAdviceRpcRequest,CalendarModeAdviceResponse> calendarModeCallable()

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CalendarModeAdviceRpcRequest request =
           CalendarModeAdviceRpcRequest.newBuilder()
               .setCalendarModeAdviceRequestResource(CalendarModeAdviceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CalendarModeAdviceResponse> future =
           adviceClient.calendarModeCallable().futureCall(request);
       // Do something.
       CalendarModeAdviceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceRpcRequest),[CalendarModeAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CalendarModeAdviceResponse)>` |   
  
### capacity(CapacityAdviceRpcRequest request)
    
    
    public final CapacityAdviceResponse capacity(CapacityAdviceRpcRequest request)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CapacityAdviceRpcRequest request =
           CapacityAdviceRpcRequest.newBuilder()
               .setCapacityAdviceRequestResource(CapacityAdviceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       CapacityAdviceResponse response = adviceClient.capacity(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceRpcRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceResponse)` |   
  
### capacity(String project, String region, CapacityAdviceRequest capacityAdviceRequestResource)
    
    
    public final CapacityAdviceResponse capacity(String project, String region, CapacityAdviceRequest capacityAdviceRequestResource)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       CapacityAdviceRequest capacityAdviceRequestResource =
           CapacityAdviceRequest.newBuilder().build();
       CapacityAdviceResponse response =
           adviceClient.capacity(project, region, capacityAdviceRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`capacityAdviceRequestResource` | `[CapacityAdviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceResponse)` |   
  
### capacityCallable()
    
    
    public final UnaryCallable<CapacityAdviceRpcRequest,CapacityAdviceResponse> capacityCallable()

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CapacityAdviceRpcRequest request =
           CapacityAdviceRpcRequest.newBuilder()
               .setCapacityAdviceRequestResource(CapacityAdviceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CapacityAdviceResponse> future =
           adviceClient.capacityCallable().futureCall(request);
       // Do something.
       CapacityAdviceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CapacityAdviceRpcRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceRpcRequest),[CapacityAdviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityAdviceResponse)>` |   
  
### capacityHistory(CapacityHistoryAdviceRequest request)
    
    
    public final CapacityHistoryResponse capacityHistory(CapacityHistoryAdviceRequest request)

Gets the capacity history.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CapacityHistoryAdviceRequest request =
           CapacityHistoryAdviceRequest.newBuilder()
               .setCapacityHistoryRequestResource(CapacityHistoryRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       CapacityHistoryResponse response = adviceClient.capacityHistory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryAdviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryResponse)` |   
  
### capacityHistory(String project, String region, CapacityHistoryRequest capacityHistoryRequestResource)
    
    
    public final CapacityHistoryResponse capacityHistory(String project, String region, CapacityHistoryRequest capacityHistoryRequestResource)

Gets the capacity history.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       CapacityHistoryRequest capacityHistoryRequestResource =
           CapacityHistoryRequest.newBuilder().build();
       CapacityHistoryResponse response =
           adviceClient.capacityHistory(project, region, capacityHistoryRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`capacityHistoryRequestResource` | `[CapacityHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryResponse)` |   
  
### capacityHistoryCallable()
    
    
    public final UnaryCallable<CapacityHistoryAdviceRequest,CapacityHistoryResponse> capacityHistoryCallable()

Gets the capacity history.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdviceClient adviceClient = AdviceClient.create()) {
       CapacityHistoryAdviceRequest request =
           CapacityHistoryAdviceRequest.newBuilder()
               .setCapacityHistoryRequestResource(CapacityHistoryRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CapacityHistoryResponse> future =
           adviceClient.capacityHistoryCallable().futureCall(request);
       // Do something.
       CapacityHistoryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryAdviceRequest),[CapacityHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CapacityHistoryResponse)>` |   
  
### close()
    
    
    public final void close()

### getSettings()
    
    
    public final @Nullable AdviceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.AdviceSettings` |   
  
### getStub()
    
    
    public AdviceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdviceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AdviceStub)` |   
  
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
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
