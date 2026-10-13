---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient
title: Class InterconnectRemoteLocationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:53.024997+00:00
---

# Class InterconnectRemoteLocationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterconnectRemoteLocationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InterconnectRemoteLocationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InterconnectRemoteLocations API.

This client uses InterconnectRemoteLocations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       String project = "project-309310695";
       String interconnectRemoteLocation = "interconnectRemoteLocation-993839543";
       InterconnectRemoteLocation response =
           interconnectRemoteLocationsClient.get(project, interconnectRemoteLocation);
     }
     

Note: close() needs to be called on the InterconnectRemoteLocationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making alist() request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInterconnectRemoteLocationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String interconnectRemoteLocation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves the list of interconnect remote locations available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInterconnectRemoteLocationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InterconnectRemoteLocationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectRemoteLocationsSettings interconnectRemoteLocationsSettings =
         InterconnectRemoteLocationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create(interconnectRemoteLocationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectRemoteLocationsSettings interconnectRemoteLocationsSettings =
         InterconnectRemoteLocationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create(interconnectRemoteLocationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InterconnectRemoteLocationsClient

## Static Methods 

### create()
    
    
    public static final InterconnectRemoteLocationsClient create()

Constructs an instance of InterconnectRemoteLocationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectRemoteLocationsSettings settings)
    
    
    public static final InterconnectRemoteLocationsClient create(InterconnectRemoteLocationsSettings settings)

Constructs an instance of InterconnectRemoteLocationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectRemoteLocationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectRemoteLocationsStub stub)
    
    
    public static final InterconnectRemoteLocationsClient create(InterconnectRemoteLocationsStub stub)

Constructs an instance of InterconnectRemoteLocationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InterconnectRemoteLocationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectRemoteLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectRemoteLocationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient)` |   
  
## Constructors 

### InterconnectRemoteLocationsClient(InterconnectRemoteLocationsSettings settings)
    
    
    protected InterconnectRemoteLocationsClient(InterconnectRemoteLocationsSettings settings)

Constructs an instance of InterconnectRemoteLocationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectRemoteLocationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsSettings)`  
  
  
### InterconnectRemoteLocationsClient(InterconnectRemoteLocationsStub stub)
    
    
    protected InterconnectRemoteLocationsClient(InterconnectRemoteLocationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectRemoteLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectRemoteLocationsStub)`  
  
  
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

### get(GetInterconnectRemoteLocationRequest request)
    
    
    public final InterconnectRemoteLocation get(GetInterconnectRemoteLocationRequest request)

Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making alist() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       GetInterconnectRemoteLocationRequest request =
           GetInterconnectRemoteLocationRequest.newBuilder()
               .setInterconnectRemoteLocation("interconnectRemoteLocation-993839543")
               .setProject("project-309310695")
               .build();
       InterconnectRemoteLocation response = interconnectRemoteLocationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectRemoteLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectRemoteLocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocation)` |   
  
### get(String project, String interconnectRemoteLocation)
    
    
    public final InterconnectRemoteLocation get(String project, String interconnectRemoteLocation)

Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making alist() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       String project = "project-309310695";
       String interconnectRemoteLocation = "interconnectRemoteLocation-993839543";
       InterconnectRemoteLocation response =
           interconnectRemoteLocationsClient.get(project, interconnectRemoteLocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectRemoteLocation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnect remote location to return.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInterconnectRemoteLocationRequest,InterconnectRemoteLocation> getCallable()

Returns the details for the specified interconnect remote location. Gets a list of available interconnect remote locations by making alist() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       GetInterconnectRemoteLocationRequest request =
           GetInterconnectRemoteLocationRequest.newBuilder()
               .setInterconnectRemoteLocation("interconnectRemoteLocation-993839543")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectRemoteLocation> future =
           interconnectRemoteLocationsClient.getCallable().futureCall(request);
       // Do something.
       InterconnectRemoteLocation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectRemoteLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectRemoteLocationRequest),[InterconnectRemoteLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocation)>` |   
  
### getSettings()
    
    
    public final @Nullable InterconnectRemoteLocationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InterconnectRemoteLocationsSettings` |   
  
### getStub()
    
    
    public InterconnectRemoteLocationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectRemoteLocationsStub)` |   
  
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
  
### list(ListInterconnectRemoteLocationsRequest request)
    
    
    public final InterconnectRemoteLocationsClient.ListPagedResponse list(ListInterconnectRemoteLocationsRequest request)

Retrieves the list of interconnect remote locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       ListInterconnectRemoteLocationsRequest request =
           ListInterconnectRemoteLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (InterconnectRemoteLocation element :
           interconnectRemoteLocationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectRemoteLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectRemoteLocationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectRemoteLocationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final InterconnectRemoteLocationsClient.ListPagedResponse list(String project)

Retrieves the list of interconnect remote locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       String project = "project-309310695";
       for (InterconnectRemoteLocation element :
           interconnectRemoteLocationsClient.list(project).iterateAll()) {
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
`[InterconnectRemoteLocationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInterconnectRemoteLocationsRequest,InterconnectRemoteLocationList> listCallable()

Retrieves the list of interconnect remote locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       ListInterconnectRemoteLocationsRequest request =
           ListInterconnectRemoteLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         InterconnectRemoteLocationList response =
             interconnectRemoteLocationsClient.listCallable().call(request);
         for (InterconnectRemoteLocation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectRemoteLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectRemoteLocationsRequest),[InterconnectRemoteLocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectRemoteLocationsRequest,InterconnectRemoteLocationsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of interconnect remote locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectRemoteLocationsClient interconnectRemoteLocationsClient =
         InterconnectRemoteLocationsClient.create()) {
       ListInterconnectRemoteLocationsRequest request =
           ListInterconnectRemoteLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectRemoteLocation> future =
           interconnectRemoteLocationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectRemoteLocation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectRemoteLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectRemoteLocationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectRemoteLocationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
