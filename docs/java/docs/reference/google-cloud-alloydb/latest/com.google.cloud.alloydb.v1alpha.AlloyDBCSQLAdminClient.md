---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient
title: Class AlloyDBCSQLAdminClient (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:20.261038+00:00
---

# Class AlloyDBCSQLAdminClient (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AlloyDBCSQLAdminClient (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-alloydb/google-cloud-alloydb/src/main/java/com/google/cloud/alloydb/v1alpha/AlloyDBCSQLAdminClient.java)| [Product Reference](https://cloud.google.com/alloydb/)| [REST Documentation](https://cloud.google.com/alloydb/docs/reference/rest)  
---|---|---  
  
Service Description: Service for interactions with CloudSQL.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = alloyDBCSQLAdminClient.getLocation(request);
     }
     

Note: close() needs to be called on the AlloyDBCSQLAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RestoreFromCloudSQL |  Restores an AlloyDB cluster from a CloudSQL resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreFromCloudSQLAsync(RestoreFromCloudSQLRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreFromCloudSQLAsync(LocationName parent, String clusterId) 
  * restoreFromCloudSQLAsync(String parent, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreFromCloudSQLOperationCallable() 
  * restoreFromCloudSQLCallable() 

  
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

This class can be customized by passing in a custom instance of AlloyDBCSQLAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBCSQLAdminSettings alloyDBCSQLAdminSettings =
         AlloyDBCSQLAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AlloyDBCSQLAdminClient alloyDBCSQLAdminClient =
         AlloyDBCSQLAdminClient.create(alloyDBCSQLAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBCSQLAdminSettings alloyDBCSQLAdminSettings =
         AlloyDBCSQLAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     AlloyDBCSQLAdminClient alloyDBCSQLAdminClient =
         AlloyDBCSQLAdminClient.create(alloyDBCSQLAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBCSQLAdminSettings alloyDBCSQLAdminSettings =
         AlloyDBCSQLAdminSettings.newHttpJsonBuilder().build();
     AlloyDBCSQLAdminClient alloyDBCSQLAdminClient =
         AlloyDBCSQLAdminClient.create(alloyDBCSQLAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AlloyDBCSQLAdminClient

## Static Methods 

### create()
    
    
    public static final AlloyDBCSQLAdminClient create()

Constructs an instance of AlloyDBCSQLAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AlloyDBCSQLAdminSettings settings)
    
    
    public static final AlloyDBCSQLAdminClient create(AlloyDBCSQLAdminSettings settings)

Constructs an instance of AlloyDBCSQLAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AlloyDBCSQLAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AlloyDBCSQLAdminStub stub)
    
    
    public static final AlloyDBCSQLAdminClient create(AlloyDBCSQLAdminStub stub)

Constructs an instance of AlloyDBCSQLAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(AlloyDBCSQLAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AlloyDBCSQLAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.stub.AlloyDBCSQLAdminStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient)` |   
  
## Constructors 

### AlloyDBCSQLAdminClient(AlloyDBCSQLAdminSettings settings)
    
    
    protected AlloyDBCSQLAdminClient(AlloyDBCSQLAdminSettings settings)

Constructs an instance of AlloyDBCSQLAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AlloyDBCSQLAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminSettings)`  
  
  
### AlloyDBCSQLAdminClient(AlloyDBCSQLAdminStub stub)
    
    
    protected AlloyDBCSQLAdminClient(AlloyDBCSQLAdminStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AlloyDBCSQLAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.stub.AlloyDBCSQLAdminStub)`  
  
  
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

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = alloyDBCSQLAdminClient.getLocation(request);
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
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = alloyDBCSQLAdminClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AlloyDBCSQLAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminSettings` |   
  
### getStub()
    
    
    public AlloyDBCSQLAdminStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBCSQLAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.stub.AlloyDBCSQLAdminStub)` |   
  
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
    
    
    public final AlloyDBCSQLAdminClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : alloyDBCSQLAdminClient.listLocations(request).iterateAll()) {
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
`[AlloyDBCSQLAdminClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             alloyDBCSQLAdminClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AlloyDBCSQLAdminClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           alloyDBCSQLAdminClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBCSQLAdminClient.ListLocationsPagedResponse)>` |   
  
### restoreFromCloudSQLAsync(@Nullable LocationName parent, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> restoreFromCloudSQLAsync(@Nullable LocationName parent, String clusterId)

Restores an AlloyDB cluster from a CloudSQL resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String clusterId = "clusterId561939637";
       Cluster response = alloyDBCSQLAdminClient.restoreFromCloudSQLAsync(parent, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.alloydb.v1alpha.LocationName`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### restoreFromCloudSQLAsync(RestoreFromCloudSQLRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> restoreFromCloudSQLAsync(RestoreFromCloudSQLRequest request)

Restores an AlloyDB cluster from a CloudSQL resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       RestoreFromCloudSQLRequest request =
           RestoreFromCloudSQLRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .build();
       Cluster response = alloyDBCSQLAdminClient.restoreFromCloudSQLAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestoreFromCloudSQLRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### restoreFromCloudSQLAsync(String parent, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> restoreFromCloudSQLAsync(String parent, String clusterId)

Restores an AlloyDB cluster from a CloudSQL resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String clusterId = "clusterId561939637";
       Cluster response = alloyDBCSQLAdminClient.restoreFromCloudSQLAsync(parent, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location of the new cluster. For the required format, see the comment on Cluster.name field.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### restoreFromCloudSQLCallable()
    
    
    public final UnaryCallable<RestoreFromCloudSQLRequest,Operation> restoreFromCloudSQLCallable()

Restores an AlloyDB cluster from a CloudSQL resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       RestoreFromCloudSQLRequest request =
           RestoreFromCloudSQLRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           alloyDBCSQLAdminClient.restoreFromCloudSQLCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestoreFromCloudSQLRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreFromCloudSQLOperationCallable()
    
    
    public final OperationCallable<RestoreFromCloudSQLRequest,Cluster,OperationMetadata> restoreFromCloudSQLOperationCallable()

Restores an AlloyDB cluster from a CloudSQL resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AlloyDBCSQLAdminClient alloyDBCSQLAdminClient = AlloyDBCSQLAdminClient.create()) {
       RestoreFromCloudSQLRequest request =
           RestoreFromCloudSQLRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           alloyDBCSQLAdminClient.restoreFromCloudSQLOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreFromCloudSQLRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestoreFromCloudSQLRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
