---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient
title: Class HostsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:31.834465+00:00
---

# Class HostsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HostsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/HostsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Hosts API.

This client uses Hosts version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String association = "association-87499647";
       String host = "host3208616";
       Host response = hostsClient.get(project, zone, association, host);
     }
     

Note: close() needs to be called on the HostsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Retrieves information about the specified host. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetHostRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String association, String host) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetVersion |  Allows customers to get SBOM versions of a host. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVersionAsync(GetVersionHostRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * getVersionAsync(String project, String zone, String association, String host, HostsGetVersionRequest hostsGetVersionRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVersionOperationCallable() 
  * getVersionCallable() 

  
List |  Retrieves a list of hosts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListHostsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone, String association) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of HostsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HostsSettings hostsSettings =
         HostsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     HostsClient hostsClient = HostsClient.create(hostsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HostsSettings hostsSettings = HostsSettings.newBuilder().setEndpoint(myEndpoint).build();
     HostsClient hostsClient = HostsClient.create(hostsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HostsClient

## Static Methods 

### create()
    
    
    public static final HostsClient create()

Constructs an instance of HostsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[HostsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HostsSettings settings)
    
    
    public static final HostsClient create(HostsSettings settings)

Constructs an instance of HostsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HostsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HostsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HostsStub stub)
    
    
    public static final HostsClient create(HostsStub stub)

Constructs an instance of HostsClient, using the given stub for making calls. This is for advanced usage - prefer using create(HostsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HostsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.HostsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HostsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient)` |   
  
## Constructors 

### HostsClient(HostsSettings settings)
    
    
    protected HostsClient(HostsSettings settings)

Constructs an instance of HostsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HostsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsSettings)`  
  
  
### HostsClient(HostsStub stub)
    
    
    protected HostsClient(HostsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HostsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.HostsStub)`  
  
  
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

### get(GetHostRequest request)
    
    
    public final Host get(GetHostRequest request)

Retrieves information about the specified host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       GetHostRequest request =
           GetHostRequest.newBuilder()
               .setAssociation("association-87499647")
               .setHost("host3208616")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Host response = hostsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHostRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Host)` |   
  
### get(String project, String zone, String association, String host)
    
    
    public final Host get(String project, String zone, String association, String host)

Retrieves information about the specified host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String association = "association-87499647";
       String host = "host3208616";
       Host response = hostsClient.get(project, zone, association, host);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request, formatted as RFC1035.  
`association` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource association for the Host. This field specifies the hierarchical context (e.g., reservation, block, sub-block) when accessing the host. For example, reservations/reservation_name, reservations/reservation_name/reservationBlocks/reservation_block_name or reservations/reservation_name/reservationBlocks/reservation_block_name/reservationSubBlocks/reservation_sub_block_name.  
`host` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the host, formatted as RFC1035 or a resource ID number.  
**Returns**  
---  
**Type** | **Description**  
`[Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Host)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetHostRequest,Host> getCallable()

Retrieves information about the specified host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       GetHostRequest request =
           GetHostRequest.newBuilder()
               .setAssociation("association-87499647")
               .setHost("host3208616")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Host> future = hostsClient.getCallable().futureCall(request);
       // Do something.
       Host response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHostRequest),[Host](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Host)>` |   
  
### getSettings()
    
    
    public final @Nullable HostsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.HostsSettings` |   
  
### getStub()
    
    
    public HostsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[HostsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.HostsStub)` |   
  
### getVersionAsync(GetVersionHostRequest request)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(GetVersionHostRequest request)

Allows customers to get SBOM versions of a host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       GetVersionHostRequest request =
           GetVersionHostRequest.newBuilder()
               .setAssociation("association-87499647")
               .setHost("host3208616")
               .setHostsGetVersionRequestResource(HostsGetVersionRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = hostsClient.getVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVersionHostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionHostRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionAsync(String project, String zone, String association, String host, HostsGetVersionRequest hostsGetVersionRequestResource)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(String project, String zone, String association, String host, HostsGetVersionRequest hostsGetVersionRequestResource)

Allows customers to get SBOM versions of a host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String association = "association-87499647";
       String host = "host3208616";
       HostsGetVersionRequest hostsGetVersionRequestResource =
           HostsGetVersionRequest.newBuilder().build();
       Operation response =
           hostsClient
               .getVersionAsync(project, zone, association, host, hostsGetVersionRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Zone name should conform to RFC1035.  
`association` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource association for the Host. This field specifies the hierarchical context (e.g., reservation, block, sub-block) when accessing the host.  
`host` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the host, formatted as RFC1035 or a resource ID number.  
`hostsGetVersionRequestResource` | `[HostsGetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsGetVersionRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionCallable()
    
    
    public final UnaryCallable<GetVersionHostRequest,Operation> getVersionCallable()

Allows customers to get SBOM versions of a host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       GetVersionHostRequest request =
           GetVersionHostRequest.newBuilder()
               .setAssociation("association-87499647")
               .setHost("host3208616")
               .setHostsGetVersionRequestResource(HostsGetVersionRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = hostsClient.getVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVersionHostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionHostRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionOperationCallable()
    
    
    public final OperationCallable<GetVersionHostRequest,Operation,Operation> getVersionOperationCallable()

Allows customers to get SBOM versions of a host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       GetVersionHostRequest request =
           GetVersionHostRequest.newBuilder()
               .setAssociation("association-87499647")
               .setHost("host3208616")
               .setHostsGetVersionRequestResource(HostsGetVersionRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           hostsClient.getVersionOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GetVersionHostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionHostRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListHostsRequest request)
    
    
    public final HostsClient.ListPagedResponse list(ListHostsRequest request)

Retrieves a list of hosts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       ListHostsRequest request =
           ListHostsRequest.newBuilder()
               .setAssociation("association-87499647")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Host element : hostsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHostsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListHostsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HostsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient.ListPagedResponse)` |   
  
### list(String project, String zone, String association)
    
    
    public final HostsClient.ListPagedResponse list(String project, String zone, String association)

Retrieves a list of hosts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String association = "association-87499647";
       for (Host element : hostsClient.list(project, zone, association).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request, formatted as RFC1035.  
`association` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource association for the Host. This field specifies the hierarchical context (e.g., reservation, block, sub-block) when accessing the host. For example, reservations/reservation_name, reservations/reservation_name/reservationBlocks/reservation_block_name or reservations/reservation_name/reservationBlocks/reservation_block_name/reservationSubBlocks/reservation_sub_block_name.  
**Returns**  
---  
**Type** | **Description**  
`[HostsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListHostsRequest,HostsListResponse> listCallable()

Retrieves a list of hosts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       ListHostsRequest request =
           ListHostsRequest.newBuilder()
               .setAssociation("association-87499647")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         HostsListResponse response = hostsClient.listCallable().call(request);
         for (Host element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHostsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListHostsRequest),[HostsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListHostsRequest,HostsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of hosts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HostsClient hostsClient = HostsClient.create()) {
       ListHostsRequest request =
           ListHostsRequest.newBuilder()
               .setAssociation("association-87499647")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Host> future = hostsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Host element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHostsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListHostsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HostsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
