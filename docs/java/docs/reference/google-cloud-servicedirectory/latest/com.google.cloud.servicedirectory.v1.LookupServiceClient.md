---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient
title: Class LookupServiceClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:11.037811+00:00
---

# Class LookupServiceClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LookupServiceClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.5  2.2.7 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-servicedirectory/google-cloud-servicedirectory/src/main/java/com/google/cloud/servicedirectory/v1/LookupServiceClient.java)| [Product Reference](https://cloud.google.com/service-directory/)| [REST Documentation](https://cloud.google.com/service-directory/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/service-directory/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service Directory API for looking up service data at runtime.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ResolveServiceRequest request =
           ResolveServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setMaxEndpoints(2074789987)
               .setEndpointFilter("endpointFilter-1834249875")
               .build();
       ResolveServiceResponse response = lookupServiceClient.resolveService(request);
     }
     

Note: close() needs to be called on the LookupServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ResolveService |  Returns a service and its associated endpoints. Resolving a service is not considered an active developer method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resolveService(ResolveServiceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resolveServiceCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LookupServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LookupServiceSettings lookupServiceSettings =
         LookupServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LookupServiceClient lookupServiceClient = LookupServiceClient.create(lookupServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LookupServiceSettings lookupServiceSettings =
         LookupServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LookupServiceClient lookupServiceClient = LookupServiceClient.create(lookupServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LookupServiceSettings lookupServiceSettings =
         LookupServiceSettings.newHttpJsonBuilder().build();
     LookupServiceClient lookupServiceClient = LookupServiceClient.create(lookupServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LookupServiceClient

## Static Methods 

### create()
    
    
    public static final LookupServiceClient create()

Constructs an instance of LookupServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LookupServiceSettings settings)
    
    
    public static final LookupServiceClient create(LookupServiceSettings settings)

Constructs an instance of LookupServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LookupServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LookupServiceStub stub)
    
    
    public static final LookupServiceClient create(LookupServiceStub stub)

Constructs an instance of LookupServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LookupServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LookupServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.LookupServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient)` |   
  
## Constructors 

### LookupServiceClient(LookupServiceSettings settings)
    
    
    protected LookupServiceClient(LookupServiceSettings settings)

Constructs an instance of LookupServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LookupServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceSettings)`  
  
  
### LookupServiceClient(LookupServiceStub stub)
    
    
    protected LookupServiceClient(LookupServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LookupServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.LookupServiceStub)`  
  
  
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

### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = lookupServiceClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = lookupServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable LookupServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.servicedirectory.v1.LookupServiceSettings` |   
  
### getStub()
    
    
    public LookupServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LookupServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.stub.LookupServiceStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final LookupServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : lookupServiceClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = lookupServiceClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,LookupServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           lookupServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient.ListLocationsPagedResponse)>` |   
  
### resolveService(ResolveServiceRequest request)
    
    
    public final ResolveServiceResponse resolveService(ResolveServiceRequest request)

Returns a service and its associated endpoints. Resolving a service is not considered an active developer method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ResolveServiceRequest request =
           ResolveServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setMaxEndpoints(2074789987)
               .setEndpointFilter("endpointFilter-1834249875")
               .build();
       ResolveServiceResponse response = lookupServiceClient.resolveService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResolveServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse)` |   
  
### resolveServiceCallable()
    
    
    public final UnaryCallable<ResolveServiceRequest,ResolveServiceResponse> resolveServiceCallable()

Returns a service and its associated endpoints. Resolving a service is not considered an active developer method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LookupServiceClient lookupServiceClient = LookupServiceClient.create()) {
       ResolveServiceRequest request =
           ResolveServiceRequest.newBuilder()
               .setName(
                   ServiceName.of("[PROJECT]", "[LOCATION]", "[NAMESPACE]", "[SERVICE]").toString())
               .setMaxEndpoints(2074789987)
               .setEndpointFilter("endpointFilter-1834249875")
               .build();
       ApiFuture<ResolveServiceResponse> future =
           lookupServiceClient.resolveServiceCallable().futureCall(request);
       // Do something.
       ResolveServiceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResolveServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceRequest),[ResolveServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
