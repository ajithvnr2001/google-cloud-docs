---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient
title: Class DatastreamClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:40.750003+00:00
---

# Class DatastreamClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastreamClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-datastream/google-cloud-datastream/src/main/java/com/google/cloud/datastream/v1/DatastreamClient.java)| [Product Reference](https://cloud.google.com/datastream/docs)| [REST Documentation](https://cloud.google.com/datastream/docs/reference/rest)  
---|---|---  
  
Service Description: Datastream service

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ConnectionProfileName name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
       ConnectionProfile response = datastreamClient.getConnectionProfile(name);
     }
     

Note: close() needs to be called on the DatastreamClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListConnectionProfiles |  Use this method to list connection profiles created in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConnectionProfiles(ListConnectionProfilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConnectionProfiles(LocationName parent) 
  * listConnectionProfiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConnectionProfilesPagedCallable() 
  * listConnectionProfilesCallable() 

  
GetConnectionProfile |  Use this method to get details about a connection profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnectionProfile(GetConnectionProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConnectionProfile(ConnectionProfileName name) 
  * getConnectionProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectionProfileCallable() 

  
CreateConnectionProfile |  Use this method to create a connection profile in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConnectionProfileAsync(CreateConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createConnectionProfileAsync(LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId) 
  * createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConnectionProfileOperationCallable() 
  * createConnectionProfileCallable() 

  
UpdateConnectionProfile |  Use this method to update the parameters of a connection profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConnectionProfileAsync(UpdateConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConnectionProfileOperationCallable() 
  * updateConnectionProfileCallable() 

  
DeleteConnectionProfile |  Use this method to delete a connection profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConnectionProfileAsync(DeleteConnectionProfileRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteConnectionProfileAsync(ConnectionProfileName name) 
  * deleteConnectionProfileAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConnectionProfileOperationCallable() 
  * deleteConnectionProfileCallable() 

  
DiscoverConnectionProfile |  Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * discoverConnectionProfile(DiscoverConnectionProfileRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * discoverConnectionProfileCallable() 

  
ListStreams |  Use this method to list streams in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listStreams(ListStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listStreams(LocationName parent) 
  * listStreams(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listStreamsPagedCallable() 
  * listStreamsCallable() 

  
GetStream |  Use this method to get details about a stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStream(GetStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getStream(StreamName name) 
  * getStream(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStreamCallable() 

  
CreateStream |  Use this method to create a stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createStreamAsync(CreateStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createStreamAsync(LocationName parent, Stream stream, String streamId) 
  * createStreamAsync(String parent, Stream stream, String streamId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createStreamOperationCallable() 
  * createStreamCallable() 

  
UpdateStream |  Use this method to update the configuration of a stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateStreamAsync(UpdateStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateStreamAsync(Stream stream, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateStreamOperationCallable() 
  * updateStreamCallable() 

  
DeleteStream |  Use this method to delete a stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteStreamAsync(DeleteStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteStreamAsync(StreamName name) 
  * deleteStreamAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteStreamOperationCallable() 
  * deleteStreamCallable() 

  
RunStream |  Use this method to start, resume or recover a stream with a non default CDC strategy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runStreamAsync(RunStreamRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runStreamOperationCallable() 
  * runStreamCallable() 

  
GetStreamObject |  Use this method to get details about a stream object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStreamObject(GetStreamObjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getStreamObject(StreamObjectName name) 
  * getStreamObject(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStreamObjectCallable() 

  
LookupStreamObject |  Use this method to look up a stream object by its source object identifier. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupStreamObject(LookupStreamObjectRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupStreamObjectCallable() 

  
ListStreamObjects |  Use this method to list the objects of a specific stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listStreamObjects(ListStreamObjectsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listStreamObjects(StreamName parent) 
  * listStreamObjects(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listStreamObjectsPagedCallable() 
  * listStreamObjectsCallable() 

  
StartBackfillJob |  Use this method to start a backfill job for the specified stream object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startBackfillJob(StartBackfillJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * startBackfillJob(StreamObjectName object) 
  * startBackfillJob(String object) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startBackfillJobCallable() 

  
StopBackfillJob |  Use this method to stop a backfill job for the specified stream object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopBackfillJob(StopBackfillJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * stopBackfillJob(StreamObjectName object) 
  * stopBackfillJob(String object) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopBackfillJobCallable() 

  
FetchStaticIps |  The FetchStaticIps API call exposes the static IP addresses used by Datastream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchStaticIps(FetchStaticIpsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchStaticIps(LocationName name) 
  * fetchStaticIps(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchStaticIpsPagedCallable() 
  * fetchStaticIpsCallable() 

  
CreatePrivateConnection |  Use this method to create a private connectivity configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPrivateConnectionAsync(CreatePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPrivateConnectionAsync(LocationName parent, PrivateConnection privateConnection, String privateConnectionId) 
  * createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPrivateConnectionOperationCallable() 
  * createPrivateConnectionCallable() 

  
GetPrivateConnection |  Use this method to get details about a private connectivity configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPrivateConnection(GetPrivateConnectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPrivateConnection(PrivateConnectionName name) 
  * getPrivateConnection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPrivateConnectionCallable() 

  
ListPrivateConnections |  Use this method to list private connectivity configurations in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPrivateConnections(ListPrivateConnectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPrivateConnections(LocationName parent) 
  * listPrivateConnections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPrivateConnectionsPagedCallable() 
  * listPrivateConnectionsCallable() 

  
DeletePrivateConnection |  Use this method to delete a private connectivity configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePrivateConnectionAsync(DeletePrivateConnectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePrivateConnectionAsync(PrivateConnectionName name) 
  * deletePrivateConnectionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePrivateConnectionOperationCallable() 
  * deletePrivateConnectionCallable() 

  
CreateRoute |  Use this method to create a route for a private connectivity configuration in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRouteAsync(CreateRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRouteAsync(PrivateConnectionName parent, Route route, String routeId) 
  * createRouteAsync(String parent, Route route, String routeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRouteOperationCallable() 
  * createRouteCallable() 

  
GetRoute |  Use this method to get details about a route. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRoute(GetRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRoute(RouteName name) 
  * getRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRouteCallable() 

  
ListRoutes |  Use this method to list routes created for a private connectivity configuration in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRoutes(ListRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRoutes(PrivateConnectionName parent) 
  * listRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRoutesPagedCallable() 
  * listRoutesCallable() 

  
DeleteRoute |  Use this method to delete a route. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRouteAsync(DeleteRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRouteAsync(RouteName name) 
  * deleteRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRouteOperationCallable() 
  * deleteRouteCallable() 

  
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

This class can be customized by passing in a custom instance of DatastreamSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatastreamSettings datastreamSettings =
         DatastreamSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DatastreamClient datastreamClient = DatastreamClient.create(datastreamSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatastreamSettings datastreamSettings =
         DatastreamSettings.newBuilder().setEndpoint(myEndpoint).build();
     DatastreamClient datastreamClient = DatastreamClient.create(datastreamSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatastreamSettings datastreamSettings = DatastreamSettings.newHttpJsonBuilder().build();
     DatastreamClient datastreamClient = DatastreamClient.create(datastreamSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastreamClient

## Static Methods 

### create()
    
    
    public static final DatastreamClient create()

Constructs an instance of DatastreamClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DatastreamSettings settings)
    
    
    public static final DatastreamClient create(DatastreamSettings settings)

Constructs an instance of DatastreamClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DatastreamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DatastreamStub stub)
    
    
    public static final DatastreamClient create(DatastreamStub stub)

Constructs an instance of DatastreamClient, using the given stub for making calls. This is for advanced usage - prefer using create(DatastreamSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DatastreamStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.stub.DatastreamStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient)` |   
  
## Constructors 

### DatastreamClient(DatastreamSettings settings)
    
    
    protected DatastreamClient(DatastreamSettings settings)

Constructs an instance of DatastreamClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DatastreamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings)`  
  
  
### DatastreamClient(DatastreamStub stub)
    
    
    protected DatastreamClient(DatastreamStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DatastreamStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.stub.DatastreamStub)`  
  
  
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

### createConnectionProfileAsync(@Nullable LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(@Nullable LocationName parent, ConnectionProfile connectionProfile, String connectionProfileId)

Use this method to create a connection profile in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       String connectionProfileId = "connectionProfileId597575526";
       ConnectionProfile response =
           datastreamClient
               .createConnectionProfileAsync(parent, connectionProfile, connectionProfileId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The connection profile identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createConnectionProfileAsync(CreateConnectionProfileRequest request)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(CreateConnectionProfileRequest request)

Use this method to create a connection profile in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ConnectionProfile response = datastreamClient.createConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> createConnectionProfileAsync(String parent, ConnectionProfile connectionProfile, String connectionProfileId)

Use this method to create a connection profile in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       String connectionProfileId = "connectionProfileId597575526";
       ConnectionProfile response =
           datastreamClient
               .createConnectionProfileAsync(parent, connectionProfile, connectionProfileId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of ConnectionProfiles.  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)`  
Required. The connection profile resource to create.  
`connectionProfileId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The connection profile identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createConnectionProfileCallable()
    
    
    public final UnaryCallable<CreateConnectionProfileRequest,Operation> createConnectionProfileCallable()

Use this method to create a connection profile in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           datastreamClient.createConnectionProfileCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConnectionProfileOperationCallable()
    
    
    public final OperationCallable<CreateConnectionProfileRequest,ConnectionProfile,OperationMetadata> createConnectionProfileOperationCallable()

Use this method to create a connection profile in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateConnectionProfileRequest request =
           CreateConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setConnectionProfileId("connectionProfileId597575526")
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       OperationFuture<ConnectionProfile, OperationMetadata> future =
           datastreamClient.createConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(@Nullable LocationName parent, PrivateConnection privateConnection, String privateConnectionId)

Use this method to create a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           datastreamClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The private connectivity identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(CreatePrivateConnectionRequest request)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(CreatePrivateConnectionRequest request)

Use this method to create a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setValidateOnly(true)
               .build();
       PrivateConnection response = datastreamClient.createPrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreatePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)
    
    
    public final OperationFuture<PrivateConnection,OperationMetadata> createPrivateConnectionAsync(String parent, PrivateConnection privateConnection, String privateConnectionId)

Use this method to create a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PrivateConnection privateConnection = PrivateConnection.newBuilder().build();
       String privateConnectionId = "privateConnectionId-1926654532";
       PrivateConnection response =
           datastreamClient
               .createPrivateConnectionAsync(parent, privateConnection, privateConnectionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of PrivateConnections.  
`privateConnection` | `[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)`  
Required. The Private Connectivity resource to create.  
`privateConnectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The private connectivity identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createPrivateConnectionCallable()
    
    
    public final UnaryCallable<CreatePrivateConnectionRequest,Operation> createPrivateConnectionCallable()

Use this method to create a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           datastreamClient.createPrivateConnectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateConnectionOperationCallable()
    
    
    public final OperationCallable<CreatePrivateConnectionRequest,PrivateConnection,OperationMetadata> createPrivateConnectionOperationCallable()

Use this method to create a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreatePrivateConnectionRequest request =
           CreatePrivateConnectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPrivateConnectionId("privateConnectionId-1926654532")
               .setPrivateConnection(PrivateConnection.newBuilder().build())
               .setRequestId("requestId693933066")
               .setForce(true)
               .setValidateOnly(true)
               .build();
       OperationFuture<PrivateConnection, OperationMetadata> future =
           datastreamClient.createPrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createRouteAsync(@Nullable PrivateConnectionName parent, Route route, String routeId)
    
    
    public final OperationFuture<Route,OperationMetadata> createRouteAsync(@Nullable PrivateConnectionName parent, Route route, String routeId)

Use this method to create a route for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       PrivateConnectionName parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       Route route = Route.newBuilder().build();
       String routeId = "routeId1385647428";
       Route response = datastreamClient.createRouteAsync(parent, route, routeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.PrivateConnectionName`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)`  
Required. The Route resource to create.  
`routeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Route identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createRouteAsync(CreateRouteRequest request)
    
    
    public final OperationFuture<Route,OperationMetadata> createRouteAsync(CreateRouteRequest request)

Use this method to create a route for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateRouteRequest request =
           CreateRouteRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRouteId("routeId1385647428")
               .setRoute(Route.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Route response = datastreamClient.createRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createRouteAsync(String parent, Route route, String routeId)
    
    
    public final OperationFuture<Route,OperationMetadata> createRouteAsync(String parent, Route route, String routeId)

Use this method to create a route for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       Route route = Route.newBuilder().build();
       String routeId = "routeId1385647428";
       Route response = datastreamClient.createRouteAsync(parent, route, routeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of Routes.  
`route` | `[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)`  
Required. The Route resource to create.  
`routeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Route identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createRouteCallable()
    
    
    public final UnaryCallable<CreateRouteRequest,Operation> createRouteCallable()

Use this method to create a route for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateRouteRequest request =
           CreateRouteRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRouteId("routeId1385647428")
               .setRoute(Route.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = datastreamClient.createRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRouteOperationCallable()
    
    
    public final OperationCallable<CreateRouteRequest,Route,OperationMetadata> createRouteOperationCallable()

Use this method to create a route for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateRouteRequest request =
           CreateRouteRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRouteId("routeId1385647428")
               .setRoute(Route.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Route, OperationMetadata> future =
           datastreamClient.createRouteOperationCallable().futureCall(request);
       // Do something.
       Route response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createStreamAsync(@Nullable LocationName parent, Stream stream, String streamId)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(@Nullable LocationName parent, Stream stream, String streamId)

Use this method to create a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Stream stream = Stream.newBuilder().build();
       String streamId = "streamId1790933179";
       Stream response = datastreamClient.createStreamAsync(parent, stream, streamId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The stream identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createStreamAsync(CreateStreamRequest request)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(CreateStreamRequest request)

Use this method to create a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       Stream response = datastreamClient.createStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createStreamAsync(String parent, Stream stream, String streamId)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(String parent, Stream stream, String streamId)

Use this method to create a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Stream stream = Stream.newBuilder().build();
       String streamId = "streamId1790933179";
       Stream response = datastreamClient.createStreamAsync(parent, stream, streamId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of streams.  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)`  
Required. The stream resource to create.  
`streamId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The stream identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createStreamCallable()
    
    
    public final UnaryCallable<CreateStreamRequest,Operation> createStreamCallable()

Use this method to create a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ApiFuture<Operation> future = datastreamClient.createStreamCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStreamOperationCallable()
    
    
    public final OperationCallable<CreateStreamRequest,Stream,OperationMetadata> createStreamOperationCallable()

Use this method to create a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       OperationFuture<Stream, OperationMetadata> future =
           datastreamClient.createStreamOperationCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(@Nullable ConnectionProfileName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(@Nullable ConnectionProfileName name)

Use this method to delete a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ConnectionProfileName name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
       datastreamClient.deleteConnectionProfileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.ConnectionProfileName`  
Required. The name of the connection profile resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(DeleteConnectionProfileRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(DeleteConnectionProfileRequest request)

Use this method to delete a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       datastreamClient.deleteConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteConnectionProfileAsync(String name)

Use this method to delete a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]").toString();
       datastreamClient.deleteConnectionProfileAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the connection profile resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileCallable()
    
    
    public final UnaryCallable<DeleteConnectionProfileRequest,Operation> deleteConnectionProfileCallable()

Use this method to delete a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           datastreamClient.deleteConnectionProfileCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConnectionProfileOperationCallable()
    
    
    public final OperationCallable<DeleteConnectionProfileRequest,Empty,OperationMetadata> deleteConnectionProfileOperationCallable()

Use this method to delete a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteConnectionProfileRequest request =
           DeleteConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           datastreamClient.deleteConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteConnectionProfileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(@Nullable PrivateConnectionName name)

Use this method to delete a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       datastreamClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.PrivateConnectionName`  
Required. The name of the private connectivity configuration to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(DeletePrivateConnectionRequest request)

Use this method to delete a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       datastreamClient.deletePrivateConnectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeletePrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePrivateConnectionAsync(String name)

Use this method to delete a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       datastreamClient.deletePrivateConnectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the private connectivity configuration to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionCallable()
    
    
    public final UnaryCallable<DeletePrivateConnectionRequest,Operation> deletePrivateConnectionCallable()

Use this method to delete a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           datastreamClient.deletePrivateConnectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeletePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateConnectionOperationCallable()
    
    
    public final OperationCallable<DeletePrivateConnectionRequest,Empty,OperationMetadata> deletePrivateConnectionOperationCallable()

Use this method to delete a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeletePrivateConnectionRequest request =
           DeletePrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           datastreamClient.deletePrivateConnectionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeletePrivateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteRouteAsync(@Nullable RouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouteAsync(@Nullable RouteName name)

Use this method to delete a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       RouteName name = RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
       datastreamClient.deleteRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.RouteName`  
Required. The name of the Route resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteRouteAsync(DeleteRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouteAsync(DeleteRouteRequest request)

Use this method to delete a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteRouteRequest request =
           DeleteRouteRequest.newBuilder()
               .setName(
                   RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       datastreamClient.deleteRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRouteAsync(String name)

Use this method to delete a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]").toString();
       datastreamClient.deleteRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Route resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteRouteCallable()
    
    
    public final UnaryCallable<DeleteRouteRequest,Operation> deleteRouteCallable()

Use this method to delete a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteRouteRequest request =
           DeleteRouteRequest.newBuilder()
               .setName(
                   RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = datastreamClient.deleteRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRouteOperationCallable()
    
    
    public final OperationCallable<DeleteRouteRequest,Empty,OperationMetadata> deleteRouteOperationCallable()

Use this method to delete a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteRouteRequest request =
           DeleteRouteRequest.newBuilder()
               .setName(
                   RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           datastreamClient.deleteRouteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(@Nullable StreamName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(@Nullable StreamName name)

Use this method to delete a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamName name = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]");
       datastreamClient.deleteStreamAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamName`  
Required. The name of the stream resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(DeleteStreamRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(DeleteStreamRequest request)

Use this method to delete a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       datastreamClient.deleteStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(String name)

Use this method to delete a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString();
       datastreamClient.deleteStreamAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteStreamCallable()
    
    
    public final UnaryCallable<DeleteStreamRequest,Operation> deleteStreamCallable()

Use this method to delete a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = datastreamClient.deleteStreamCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteStreamOperationCallable()
    
    
    public final OperationCallable<DeleteStreamRequest,Empty,OperationMetadata> deleteStreamOperationCallable()

Use this method to delete a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           datastreamClient.deleteStreamOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteStreamRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### discoverConnectionProfile(DiscoverConnectionProfileRequest request)
    
    
    public final DiscoverConnectionProfileResponse discoverConnectionProfile(DiscoverConnectionProfileRequest request)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DiscoverConnectionProfileRequest request =
           DiscoverConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       DiscoverConnectionProfileResponse response =
           datastreamClient.discoverConnectionProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileResponse)` |   
  
### discoverConnectionProfileCallable()
    
    
    public final UnaryCallable<DiscoverConnectionProfileRequest,DiscoverConnectionProfileResponse> discoverConnectionProfileCallable()

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       DiscoverConnectionProfileRequest request =
           DiscoverConnectionProfileRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<DiscoverConnectionProfileResponse> future =
           datastreamClient.discoverConnectionProfileCallable().futureCall(request);
       // Do something.
       DiscoverConnectionProfileResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileRequest),[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileResponse)>` |   
  
### fetchStaticIps(@Nullable LocationName name)
    
    
    public final DatastreamClient.FetchStaticIpsPagedResponse fetchStaticIps(@Nullable LocationName name)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName name = LocationName.of("[PROJECT]", "[LOCATION]");
       for (String element : datastreamClient.fetchStaticIps(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIps(FetchStaticIpsRequest request)
    
    
    public final DatastreamClient.FetchStaticIpsPagedResponse fetchStaticIps(FetchStaticIpsRequest request)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : datastreamClient.fetchStaticIps(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIps(String name)
    
    
    public final DatastreamClient.FetchStaticIpsPagedResponse fetchStaticIps(String name)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (String element : datastreamClient.fetchStaticIps(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.FetchStaticIpsPagedResponse)` |   
  
### fetchStaticIpsCallable()
    
    
    public final UnaryCallable<FetchStaticIpsRequest,FetchStaticIpsResponse> fetchStaticIpsCallable()

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchStaticIpsResponse response = datastreamClient.fetchStaticIpsCallable().call(request);
         for (String element : response.getStaticIpsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsRequest),[FetchStaticIpsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsResponse)>` |   
  
### fetchStaticIpsPagedCallable()
    
    
    public final UnaryCallable<FetchStaticIpsRequest,DatastreamClient.FetchStaticIpsPagedResponse> fetchStaticIpsPagedCallable()

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       FetchStaticIpsRequest request =
           FetchStaticIpsRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future = datastreamClient.fetchStaticIpsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsRequest),[FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.FetchStaticIpsPagedResponse)>` |   
  
### getConnectionProfile(@Nullable ConnectionProfileName name)
    
    
    public final ConnectionProfile getConnectionProfile(@Nullable ConnectionProfileName name)

Use this method to get details about a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ConnectionProfileName name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]");
       ConnectionProfile response = datastreamClient.getConnectionProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.ConnectionProfileName`  
Required. The name of the connection profile resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
  
### getConnectionProfile(GetConnectionProfileRequest request)
    
    
    public final ConnectionProfile getConnectionProfile(GetConnectionProfileRequest request)

Use this method to get details about a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetConnectionProfileRequest request =
           GetConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .build();
       ConnectionProfile response = datastreamClient.getConnectionProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
  
### getConnectionProfile(String name)
    
    
    public final ConnectionProfile getConnectionProfile(String name)

Use this method to get details about a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]").toString();
       ConnectionProfile response = datastreamClient.getConnectionProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the connection profile resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
  
### getConnectionProfileCallable()
    
    
    public final UnaryCallable<GetConnectionProfileRequest,ConnectionProfile> getConnectionProfileCallable()

Use this method to get details about a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetConnectionProfileRequest request =
           GetConnectionProfileRequest.newBuilder()
               .setName(
                   ConnectionProfileName.of("[PROJECT]", "[LOCATION]", "[CONNECTION_PROFILE]")
                       .toString())
               .build();
       ApiFuture<ConnectionProfile> future =
           datastreamClient.getConnectionProfileCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)>` |   
  
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
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = datastreamClient.getLocation(request);
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
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = datastreamClient.getLocationCallable().futureCall(request);
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
  
### getPrivateConnection(@Nullable PrivateConnectionName name)
    
    
    public final PrivateConnection getPrivateConnection(@Nullable PrivateConnectionName name)

Use this method to get details about a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       PrivateConnectionName name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       PrivateConnection response = datastreamClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.PrivateConnectionName`  
Required. The name of the private connectivity configuration to get.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)` |   
  
### getPrivateConnection(GetPrivateConnectionRequest request)
    
    
    public final PrivateConnection getPrivateConnection(GetPrivateConnectionRequest request)

Use this method to get details about a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       PrivateConnection response = datastreamClient.getPrivateConnection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetPrivateConnectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)` |   
  
### getPrivateConnection(String name)
    
    
    public final PrivateConnection getPrivateConnection(String name)

Use this method to get details about a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       PrivateConnection response = datastreamClient.getPrivateConnection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the private connectivity configuration to get.  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)` |   
  
### getPrivateConnectionCallable()
    
    
    public final UnaryCallable<GetPrivateConnectionRequest,PrivateConnection> getPrivateConnectionCallable()

Use this method to get details about a private connectivity configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetPrivateConnectionRequest request =
           GetPrivateConnectionRequest.newBuilder()
               .setName(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .build();
       ApiFuture<PrivateConnection> future =
           datastreamClient.getPrivateConnectionCallable().futureCall(request);
       // Do something.
       PrivateConnection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetPrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)>` |   
  
### getRoute(@Nullable RouteName name)
    
    
    public final Route getRoute(@Nullable RouteName name)

Use this method to get details about a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       RouteName name = RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]");
       Route response = datastreamClient.getRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.RouteName`  
Required. The name of the Route resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)` |   
  
### getRoute(GetRouteRequest request)
    
    
    public final Route getRoute(GetRouteRequest request)

Use this method to get details about a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetRouteRequest request =
           GetRouteRequest.newBuilder()
               .setName(
                   RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]")
                       .toString())
               .build();
       Route response = datastreamClient.getRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)` |   
  
### getRoute(String name)
    
    
    public final Route getRoute(String name)

Use this method to get details about a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]").toString();
       Route response = datastreamClient.getRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Route resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)` |   
  
### getRouteCallable()
    
    
    public final UnaryCallable<GetRouteRequest,Route> getRouteCallable()

Use this method to get details about a route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetRouteRequest request =
           GetRouteRequest.newBuilder()
               .setName(
                   RouteName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]", "[ROUTE]")
                       .toString())
               .build();
       ApiFuture<Route> future = datastreamClient.getRouteCallable().futureCall(request);
       // Do something.
       Route response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)>` |   
  
### getSettings()
    
    
    public final @Nullable DatastreamSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.DatastreamSettings` |   
  
### getStream(@Nullable StreamName name)
    
    
    public final Stream getStream(@Nullable StreamName name)

Use this method to get details about a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamName name = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]");
       Stream response = datastreamClient.getStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamName`  
Required. The name of the stream resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)` |   
  
### getStream(GetStreamRequest request)
    
    
    public final Stream getStream(GetStreamRequest request)

Use this method to get details about a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetStreamRequest request =
           GetStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .build();
       Stream response = datastreamClient.getStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)` |   
  
### getStream(String name)
    
    
    public final Stream getStream(String name)

Use this method to get details about a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString();
       Stream response = datastreamClient.getStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)` |   
  
### getStreamCallable()
    
    
    public final UnaryCallable<GetStreamRequest,Stream> getStreamCallable()

Use this method to get details about a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetStreamRequest request =
           GetStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .build();
       ApiFuture<Stream> future = datastreamClient.getStreamCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)>` |   
  
### getStreamObject(@Nullable StreamObjectName name)
    
    
    public final StreamObject getStreamObject(@Nullable StreamObjectName name)

Use this method to get details about a stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamObjectName name =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
       StreamObject response = datastreamClient.getStreamObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamObjectName`  
Required. The name of the stream object resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)` |   
  
### getStreamObject(GetStreamObjectRequest request)
    
    
    public final StreamObject getStreamObject(GetStreamObjectRequest request)

Use this method to get details about a stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetStreamObjectRequest request =
           GetStreamObjectRequest.newBuilder()
               .setName(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       StreamObject response = datastreamClient.getStreamObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)` |   
  
### getStreamObject(String name)
    
    
    public final StreamObject getStreamObject(String name)

Use this method to get details about a stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String name =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString();
       StreamObject response = datastreamClient.getStreamObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream object resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)` |   
  
### getStreamObjectCallable()
    
    
    public final UnaryCallable<GetStreamObjectRequest,StreamObject> getStreamObjectCallable()

Use this method to get details about a stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       GetStreamObjectRequest request =
           GetStreamObjectRequest.newBuilder()
               .setName(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       ApiFuture<StreamObject> future =
           datastreamClient.getStreamObjectCallable().futureCall(request);
       // Do something.
       StreamObject response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamObjectRequest),[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)>` |   
  
### getStub()
    
    
    public DatastreamStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DatastreamStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.stub.DatastreamStub)` |   
  
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
  
### listConnectionProfiles(@Nullable LocationName parent)
    
    
    public final DatastreamClient.ListConnectionProfilesPagedResponse listConnectionProfiles(@Nullable LocationName parent)

Use this method to list connection profiles created in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ConnectionProfile element :
           datastreamClient.listConnectionProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of connection profiles.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfiles(ListConnectionProfilesRequest request)
    
    
    public final DatastreamClient.ListConnectionProfilesPagedResponse listConnectionProfiles(ListConnectionProfilesRequest request)

Use this method to list connection profiles created in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ConnectionProfile element :
           datastreamClient.listConnectionProfiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfiles(String parent)
    
    
    public final DatastreamClient.ListConnectionProfilesPagedResponse listConnectionProfiles(String parent)

Use this method to list connection profiles created in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ConnectionProfile element :
           datastreamClient.listConnectionProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of connection profiles.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListConnectionProfilesPagedResponse)` |   
  
### listConnectionProfilesCallable()
    
    
    public final UnaryCallable<ListConnectionProfilesRequest,ListConnectionProfilesResponse> listConnectionProfilesCallable()

Use this method to list connection profiles created in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListConnectionProfilesResponse response =
             datastreamClient.listConnectionProfilesCallable().call(request);
         for (ConnectionProfile element : response.getConnectionProfilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesRequest),[ListConnectionProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesResponse)>` |   
  
### listConnectionProfilesPagedCallable()
    
    
    public final UnaryCallable<ListConnectionProfilesRequest,DatastreamClient.ListConnectionProfilesPagedResponse> listConnectionProfilesPagedCallable()

Use this method to list connection profiles created in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListConnectionProfilesRequest request =
           ListConnectionProfilesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ConnectionProfile> future =
           datastreamClient.listConnectionProfilesPagedCallable().futureCall(request);
       // Do something.
       for (ConnectionProfile element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesRequest),[ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListConnectionProfilesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DatastreamClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : datastreamClient.listLocations(request).iterateAll()) {
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
`[DatastreamClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = datastreamClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DatastreamClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           datastreamClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListLocationsPagedResponse)>` |   
  
### listPrivateConnections(@Nullable LocationName parent)
    
    
    public final DatastreamClient.ListPrivateConnectionsPagedResponse listPrivateConnections(@Nullable LocationName parent)

Use this method to list private connectivity configurations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PrivateConnection element :
           datastreamClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of private connectivity configurations.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(ListPrivateConnectionsRequest request)
    
    
    public final DatastreamClient.ListPrivateConnectionsPagedResponse listPrivateConnections(ListPrivateConnectionsRequest request)

Use this method to list private connectivity configurations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PrivateConnection element :
           datastreamClient.listPrivateConnections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnections(String parent)
    
    
    public final DatastreamClient.ListPrivateConnectionsPagedResponse listPrivateConnections(String parent)

Use this method to list private connectivity configurations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PrivateConnection element :
           datastreamClient.listPrivateConnections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of private connectivity configurations.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListPrivateConnectionsPagedResponse)` |   
  
### listPrivateConnectionsCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,ListPrivateConnectionsResponse> listPrivateConnectionsCallable()

Use this method to list private connectivity configurations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPrivateConnectionsResponse response =
             datastreamClient.listPrivateConnectionsCallable().call(request);
         for (PrivateConnection element : response.getPrivateConnectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsResponse)>` |   
  
### listPrivateConnectionsPagedCallable()
    
    
    public final UnaryCallable<ListPrivateConnectionsRequest,DatastreamClient.ListPrivateConnectionsPagedResponse> listPrivateConnectionsPagedCallable()

Use this method to list private connectivity configurations in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListPrivateConnectionsRequest request =
           ListPrivateConnectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PrivateConnection> future =
           datastreamClient.listPrivateConnectionsPagedCallable().futureCall(request);
       // Do something.
       for (PrivateConnection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListPrivateConnectionsPagedResponse)>` |   
  
### listRoutes(@Nullable PrivateConnectionName parent)
    
    
    public final DatastreamClient.ListRoutesPagedResponse listRoutes(@Nullable PrivateConnectionName parent)

Use this method to list routes created for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       PrivateConnectionName parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]");
       for (Route element : datastreamClient.listRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.PrivateConnectionName`  
Required. The parent that owns the collection of Routess.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListRoutesPagedResponse)` |   
  
### listRoutes(ListRoutesRequest request)
    
    
    public final DatastreamClient.ListRoutesPagedResponse listRoutes(ListRoutesRequest request)

Use this method to list routes created for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Route element : datastreamClient.listRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListRoutesPagedResponse)` |   
  
### listRoutes(String parent)
    
    
    public final DatastreamClient.ListRoutesPagedResponse listRoutes(String parent)

Use this method to list routes created for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent =
           PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]").toString();
       for (Route element : datastreamClient.listRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of Routess.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListRoutesPagedResponse)` |   
  
### listRoutesCallable()
    
    
    public final UnaryCallable<ListRoutesRequest,ListRoutesResponse> listRoutesCallable()

Use this method to list routes created for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListRoutesResponse response = datastreamClient.listRoutesCallable().call(request);
         for (Route element : response.getRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesRequest),[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesResponse)>` |   
  
### listRoutesPagedCallable()
    
    
    public final UnaryCallable<ListRoutesRequest,DatastreamClient.ListRoutesPagedResponse> listRoutesPagedCallable()

Use this method to list routes created for a private connectivity configuration in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListRoutesRequest request =
           ListRoutesRequest.newBuilder()
               .setParent(
                   PrivateConnectionName.of("[PROJECT]", "[LOCATION]", "[PRIVATE_CONNECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Route> future = datastreamClient.listRoutesPagedCallable().futureCall(request);
       // Do something.
       for (Route element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesRequest),[ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListRoutesPagedResponse)>` |   
  
### listStreamObjects(@Nullable StreamName parent)
    
    
    public final DatastreamClient.ListStreamObjectsPagedResponse listStreamObjects(@Nullable StreamName parent)

Use this method to list the objects of a specific stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamName parent = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]");
       for (StreamObject element : datastreamClient.listStreamObjects(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamName`  
Required. The parent stream that owns the collection of objects.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamObjectsPagedResponse)` |   
  
### listStreamObjects(ListStreamObjectsRequest request)
    
    
    public final DatastreamClient.ListStreamObjectsPagedResponse listStreamObjects(ListStreamObjectsRequest request)

Use this method to list the objects of a specific stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamObjectsRequest request =
           ListStreamObjectsRequest.newBuilder()
               .setParent(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (StreamObject element : datastreamClient.listStreamObjects(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamObjectsPagedResponse)` |   
  
### listStreamObjects(String parent)
    
    
    public final DatastreamClient.ListStreamObjectsPagedResponse listStreamObjects(String parent)

Use this method to list the objects of a specific stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString();
       for (StreamObject element : datastreamClient.listStreamObjects(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent stream that owns the collection of objects.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamObjectsPagedResponse)` |   
  
### listStreamObjectsCallable()
    
    
    public final UnaryCallable<ListStreamObjectsRequest,ListStreamObjectsResponse> listStreamObjectsCallable()

Use this method to list the objects of a specific stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamObjectsRequest request =
           ListStreamObjectsRequest.newBuilder()
               .setParent(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListStreamObjectsResponse response =
             datastreamClient.listStreamObjectsCallable().call(request);
         for (StreamObject element : response.getStreamObjectsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsRequest),[ListStreamObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsResponse)>` |   
  
### listStreamObjectsPagedCallable()
    
    
    public final UnaryCallable<ListStreamObjectsRequest,DatastreamClient.ListStreamObjectsPagedResponse> listStreamObjectsPagedCallable()

Use this method to list the objects of a specific stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamObjectsRequest request =
           ListStreamObjectsRequest.newBuilder()
               .setParent(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<StreamObject> future =
           datastreamClient.listStreamObjectsPagedCallable().futureCall(request);
       // Do something.
       for (StreamObject element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsRequest),[ListStreamObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamObjectsPagedResponse)>` |   
  
### listStreams(@Nullable LocationName parent)
    
    
    public final DatastreamClient.ListStreamsPagedResponse listStreams(@Nullable LocationName parent)

Use this method to list streams in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Stream element : datastreamClient.listStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.LocationName`  
Required. The parent that owns the collection of streams.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamsPagedResponse)` |   
  
### listStreams(ListStreamsRequest request)
    
    
    public final DatastreamClient.ListStreamsPagedResponse listStreams(ListStreamsRequest request)

Use this method to list streams in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Stream element : datastreamClient.listStreams(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamsPagedResponse)` |   
  
### listStreams(String parent)
    
    
    public final DatastreamClient.ListStreamsPagedResponse listStreams(String parent)

Use this method to list streams in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Stream element : datastreamClient.listStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns the collection of streams.  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamsPagedResponse)` |   
  
### listStreamsCallable()
    
    
    public final UnaryCallable<ListStreamsRequest,ListStreamsResponse> listStreamsCallable()

Use this method to list streams in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListStreamsResponse response = datastreamClient.listStreamsCallable().call(request);
         for (Stream element : response.getStreamsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsRequest),[ListStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsResponse)>` |   
  
### listStreamsPagedCallable()
    
    
    public final UnaryCallable<ListStreamsRequest,DatastreamClient.ListStreamsPagedResponse> listStreamsPagedCallable()

Use this method to list streams in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Stream> future = datastreamClient.listStreamsPagedCallable().futureCall(request);
       // Do something.
       for (Stream element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsRequest),[ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamsPagedResponse)>` |   
  
### lookupStreamObject(LookupStreamObjectRequest request)
    
    
    public final StreamObject lookupStreamObject(LookupStreamObjectRequest request)

Use this method to look up a stream object by its source object identifier.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LookupStreamObjectRequest request =
           LookupStreamObjectRequest.newBuilder()
               .setParent(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setSourceObjectIdentifier(SourceObjectIdentifier.newBuilder().build())
               .build();
       StreamObject response = datastreamClient.lookupStreamObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.LookupStreamObjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)` |   
  
### lookupStreamObjectCallable()
    
    
    public final UnaryCallable<LookupStreamObjectRequest,StreamObject> lookupStreamObjectCallable()

Use this method to look up a stream object by its source object identifier.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       LookupStreamObjectRequest request =
           LookupStreamObjectRequest.newBuilder()
               .setParent(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setSourceObjectIdentifier(SourceObjectIdentifier.newBuilder().build())
               .build();
       ApiFuture<StreamObject> future =
           datastreamClient.lookupStreamObjectCallable().futureCall(request);
       // Do something.
       StreamObject response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.LookupStreamObjectRequest),[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)>` |   
  
### runStreamAsync(RunStreamRequest request)
    
    
    public final OperationFuture<Stream,OperationMetadata> runStreamAsync(RunStreamRequest request)

Use this method to start, resume or recover a stream with a non default CDC strategy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       RunStreamRequest request =
           RunStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setCdcStrategy(CdcStrategy.newBuilder().build())
               .setForce(true)
               .build();
       Stream response = datastreamClient.runStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.RunStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### runStreamCallable()
    
    
    public final UnaryCallable<RunStreamRequest,Operation> runStreamCallable()

Use this method to start, resume or recover a stream with a non default CDC strategy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       RunStreamRequest request =
           RunStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setCdcStrategy(CdcStrategy.newBuilder().build())
               .setForce(true)
               .build();
       ApiFuture<Operation> future = datastreamClient.runStreamCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.RunStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runStreamOperationCallable()
    
    
    public final OperationCallable<RunStreamRequest,Stream,OperationMetadata> runStreamOperationCallable()

Use this method to start, resume or recover a stream with a non default CDC strategy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       RunStreamRequest request =
           RunStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[STREAM]").toString())
               .setCdcStrategy(CdcStrategy.newBuilder().build())
               .setForce(true)
               .build();
       OperationFuture<Stream, OperationMetadata> future =
           datastreamClient.runStreamOperationCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.RunStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startBackfillJob(@Nullable StreamObjectName object)
    
    
    public final StartBackfillJobResponse startBackfillJob(@Nullable StreamObjectName object)

Use this method to start a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamObjectName object =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
       StartBackfillJobResponse response = datastreamClient.startBackfillJob(object);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`object` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamObjectName`  
Required. The name of the stream object resource to start a backfill job for.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobResponse)` |   
  
### startBackfillJob(StartBackfillJobRequest request)
    
    
    public final StartBackfillJobResponse startBackfillJob(StartBackfillJobRequest request)

Use this method to start a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StartBackfillJobRequest request =
           StartBackfillJobRequest.newBuilder()
               .setObject(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       StartBackfillJobResponse response = datastreamClient.startBackfillJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobResponse)` |   
  
### startBackfillJob(String object)
    
    
    public final StartBackfillJobResponse startBackfillJob(String object)

Use this method to start a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String object =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString();
       StartBackfillJobResponse response = datastreamClient.startBackfillJob(object);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`object` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream object resource to start a backfill job for.  
**Returns**  
---  
**Type** | **Description**  
`[StartBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobResponse)` |   
  
### startBackfillJobCallable()
    
    
    public final UnaryCallable<StartBackfillJobRequest,StartBackfillJobResponse> startBackfillJobCallable()

Use this method to start a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StartBackfillJobRequest request =
           StartBackfillJobRequest.newBuilder()
               .setObject(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       ApiFuture<StartBackfillJobResponse> future =
           datastreamClient.startBackfillJobCallable().futureCall(request);
       // Do something.
       StartBackfillJobResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobRequest),[StartBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobResponse)>` |   
  
### stopBackfillJob(@Nullable StreamObjectName object)
    
    
    public final StopBackfillJobResponse stopBackfillJob(@Nullable StreamObjectName object)

Use this method to stop a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StreamObjectName object =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]");
       StopBackfillJobResponse response = datastreamClient.stopBackfillJob(object);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`object` | `@org.jspecify.annotations.Nullable com.google.cloud.datastream.v1.StreamObjectName`  
Required. The name of the stream object resource to stop the backfill job for.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobResponse)` |   
  
### stopBackfillJob(StopBackfillJobRequest request)
    
    
    public final StopBackfillJobResponse stopBackfillJob(StopBackfillJobRequest request)

Use this method to stop a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StopBackfillJobRequest request =
           StopBackfillJobRequest.newBuilder()
               .setObject(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       StopBackfillJobResponse response = datastreamClient.stopBackfillJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobResponse)` |   
  
### stopBackfillJob(String object)
    
    
    public final StopBackfillJobResponse stopBackfillJob(String object)

Use this method to stop a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       String object =
           StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString();
       StopBackfillJobResponse response = datastreamClient.stopBackfillJob(object);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`object` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream object resource to stop the backfill job for.  
**Returns**  
---  
**Type** | **Description**  
`[StopBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobResponse)` |   
  
### stopBackfillJobCallable()
    
    
    public final UnaryCallable<StopBackfillJobRequest,StopBackfillJobResponse> stopBackfillJobCallable()

Use this method to stop a backfill job for the specified stream object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       StopBackfillJobRequest request =
           StopBackfillJobRequest.newBuilder()
               .setObject(
                   StreamObjectName.of("[PROJECT]", "[LOCATION]", "[STREAM]", "[OBJECT]").toString())
               .build();
       ApiFuture<StopBackfillJobResponse> future =
           datastreamClient.stopBackfillJobCallable().futureCall(request);
       // Do something.
       StopBackfillJobResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobRequest),[StopBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobResponse)>` |   
  
### updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> updateConnectionProfileAsync(ConnectionProfile connectionProfile, FieldMask updateMask)

Use this method to update the parameters of a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       ConnectionProfile connectionProfile = ConnectionProfile.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConnectionProfile response =
           datastreamClient.updateConnectionProfileAsync(connectionProfile, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`connectionProfile` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)`  
Required. The connection profile to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ConnectionProfile resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateConnectionProfileAsync(UpdateConnectionProfileRequest request)
    
    
    public final OperationFuture<ConnectionProfile,OperationMetadata> updateConnectionProfileAsync(UpdateConnectionProfileRequest request)

Use this method to update the parameters of a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ConnectionProfile response = datastreamClient.updateConnectionProfileAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateConnectionProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateConnectionProfileCallable()
    
    
    public final UnaryCallable<UpdateConnectionProfileRequest,Operation> updateConnectionProfileCallable()

Use this method to update the parameters of a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           datastreamClient.updateConnectionProfileCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateConnectionProfileOperationCallable()
    
    
    public final OperationCallable<UpdateConnectionProfileRequest,ConnectionProfile,OperationMetadata> updateConnectionProfileOperationCallable()

Use this method to update the parameters of a connection profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateConnectionProfileRequest request =
           UpdateConnectionProfileRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setConnectionProfile(ConnectionProfile.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       OperationFuture<ConnectionProfile, OperationMetadata> future =
           datastreamClient.updateConnectionProfileOperationCallable().futureCall(request);
       // Do something.
       ConnectionProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateStreamAsync(Stream stream, FieldMask updateMask)
    
    
    public final OperationFuture<Stream,OperationMetadata> updateStreamAsync(Stream stream, FieldMask updateMask)

Use this method to update the configuration of a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       Stream stream = Stream.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Stream response = datastreamClient.updateStreamAsync(stream, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)`  
Required. The stream resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateStreamAsync(UpdateStreamRequest request)
    
    
    public final OperationFuture<Stream,OperationMetadata> updateStreamAsync(UpdateStreamRequest request)

Use this method to update the configuration of a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       Stream response = datastreamClient.updateStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateStreamCallable()
    
    
    public final UnaryCallable<UpdateStreamRequest,Operation> updateStreamCallable()

Use this method to update the configuration of a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       ApiFuture<Operation> future = datastreamClient.updateStreamCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateStreamOperationCallable()
    
    
    public final OperationCallable<UpdateStreamRequest,Stream,OperationMetadata> updateStreamOperationCallable()

Use this method to update the configuration of a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DatastreamClient datastreamClient = DatastreamClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setForce(true)
               .build();
       OperationFuture<Stream, OperationMetadata> future =
           datastreamClient.updateStreamOperationCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
