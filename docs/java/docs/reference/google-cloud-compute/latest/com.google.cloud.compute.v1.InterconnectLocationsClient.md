---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient
title: Class InterconnectLocationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:51.942124+00:00
---

# Class InterconnectLocationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterconnectLocationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InterconnectLocationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InterconnectLocations API.

This client uses InterconnectLocations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       String project = "project-309310695";
       String interconnectLocation = "interconnectLocation220117603";
       InterconnectLocation response =
           interconnectLocationsClient.get(project, interconnectLocation);
     }
     

Note: close() needs to be called on the InterconnectLocationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInterconnectLocationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String interconnectLocation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves the list of interconnect locations available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInterconnectLocationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InterconnectLocationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectLocationsSettings interconnectLocationsSettings =
         InterconnectLocationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create(interconnectLocationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InterconnectLocationsSettings interconnectLocationsSettings =
         InterconnectLocationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create(interconnectLocationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InterconnectLocationsClient

## Static Methods 

### create()
    
    
    public static final InterconnectLocationsClient create()

Constructs an instance of InterconnectLocationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectLocationsSettings settings)
    
    
    public static final InterconnectLocationsClient create(InterconnectLocationsSettings settings)

Constructs an instance of InterconnectLocationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectLocationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InterconnectLocationsStub stub)
    
    
    public static final InterconnectLocationsClient create(InterconnectLocationsStub stub)

Constructs an instance of InterconnectLocationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InterconnectLocationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectLocationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient)` |   
  
## Constructors 

### InterconnectLocationsClient(InterconnectLocationsSettings settings)
    
    
    protected InterconnectLocationsClient(InterconnectLocationsSettings settings)

Constructs an instance of InterconnectLocationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InterconnectLocationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsSettings)`  
  
  
### InterconnectLocationsClient(InterconnectLocationsStub stub)
    
    
    protected InterconnectLocationsClient(InterconnectLocationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InterconnectLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectLocationsStub)`  
  
  
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

### get(GetInterconnectLocationRequest request)
    
    
    public final InterconnectLocation get(GetInterconnectLocationRequest request)

Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       GetInterconnectLocationRequest request =
           GetInterconnectLocationRequest.newBuilder()
               .setInterconnectLocation("interconnectLocation220117603")
               .setProject("project-309310695")
               .build();
       InterconnectLocation response = interconnectLocationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInterconnectLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectLocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocation)` |   
  
### get(String project, String interconnectLocation)
    
    
    public final InterconnectLocation get(String project, String interconnectLocation)

Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       String project = "project-309310695";
       String interconnectLocation = "interconnectLocation220117603";
       InterconnectLocation response =
           interconnectLocationsClient.get(project, interconnectLocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`interconnectLocation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the interconnect location to return.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInterconnectLocationRequest,InterconnectLocation> getCallable()

Returns the details for the specified interconnect location. Gets a list of available interconnect locations by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       GetInterconnectLocationRequest request =
           GetInterconnectLocationRequest.newBuilder()
               .setInterconnectLocation("interconnectLocation220117603")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectLocation> future =
           interconnectLocationsClient.getCallable().futureCall(request);
       // Do something.
       InterconnectLocation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInterconnectLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInterconnectLocationRequest),[InterconnectLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocation)>` |   
  
### getSettings()
    
    
    public final @Nullable InterconnectLocationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InterconnectLocationsSettings` |   
  
### getStub()
    
    
    public InterconnectLocationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InterconnectLocationsStub)` |   
  
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
  
### list(ListInterconnectLocationsRequest request)
    
    
    public final InterconnectLocationsClient.ListPagedResponse list(ListInterconnectLocationsRequest request)

Retrieves the list of interconnect locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       ListInterconnectLocationsRequest request =
           ListInterconnectLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (InterconnectLocation element : interconnectLocationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInterconnectLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectLocationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectLocationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final InterconnectLocationsClient.ListPagedResponse list(String project)

Retrieves the list of interconnect locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       String project = "project-309310695";
       for (InterconnectLocation element : interconnectLocationsClient.list(project).iterateAll()) {
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
`[InterconnectLocationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInterconnectLocationsRequest,InterconnectLocationList> listCallable()

Retrieves the list of interconnect locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       ListInterconnectLocationsRequest request =
           ListInterconnectLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         InterconnectLocationList response =
             interconnectLocationsClient.listCallable().call(request);
         for (InterconnectLocation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectLocationsRequest),[InterconnectLocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInterconnectLocationsRequest,InterconnectLocationsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of interconnect locations available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InterconnectLocationsClient interconnectLocationsClient =
         InterconnectLocationsClient.create()) {
       ListInterconnectLocationsRequest request =
           ListInterconnectLocationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<InterconnectLocation> future =
           interconnectLocationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InterconnectLocation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInterconnectLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInterconnectLocationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InterconnectLocationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
