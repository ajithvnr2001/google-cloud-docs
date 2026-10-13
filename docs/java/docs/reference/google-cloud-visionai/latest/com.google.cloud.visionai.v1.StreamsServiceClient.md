---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient
title: Class StreamsServiceClient (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:20.431555+00:00
---

# Class StreamsServiceClient (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamsServiceClient (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-visionai/google-cloud-visionai/src/main/java/com/google/cloud/visionai/v1/StreamsServiceClient.java)| [Product Reference](https://cloud.google.com/vision-ai/docs)| [RPC Documentation](https://cloud.google.com/vision-ai/docs/reference/rpc)  
---|---|---  
  
Service Description: Service describing handlers for resources. Vision API and Vision AI API are two independent APIs developed by the same team. Vision API is for people to annotate their image while Vision AI is an e2e solution for customer to build their own computer vision application.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = streamsServiceClient.getCluster(name);
     }
     

Note: close() needs to be called on the StreamsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListClusters |  Lists Clusters in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClusters(ListClustersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClusters(LocationName parent) 
  * listClusters(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClustersPagedCallable() 
  * listClustersCallable() 

  
GetCluster |  Gets details of a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCluster(GetClusterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCluster(ClusterName name) 
  * getCluster(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClusterCallable() 

  
CreateCluster |  Creates a new Cluster in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClusterAsync(CreateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createClusterAsync(LocationName parent, Cluster cluster, String clusterId) 
  * createClusterAsync(String parent, Cluster cluster, String clusterId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClusterOperationCallable() 
  * createClusterCallable() 

  
UpdateCluster |  Updates the parameters of a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateClusterAsync(UpdateClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateClusterAsync(Cluster cluster, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateClusterOperationCallable() 
  * updateClusterCallable() 

  
DeleteCluster |  Deletes a single Cluster. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteClusterAsync(DeleteClusterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteClusterAsync(ClusterName name) 
  * deleteClusterAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClusterOperationCallable() 
  * deleteClusterCallable() 

  
ListStreams |  Lists Streams in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listStreams(ListStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listStreams(ClusterName parent) 
  * listStreams(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listStreamsPagedCallable() 
  * listStreamsCallable() 

  
GetStream |  Gets details of a single Stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStream(GetStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getStream(StreamName name) 
  * getStream(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStreamCallable() 

  
CreateStream |  Creates a new Stream in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createStreamAsync(CreateStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createStreamAsync(ClusterName parent, Stream stream, String streamId) 
  * createStreamAsync(String parent, Stream stream, String streamId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createStreamOperationCallable() 
  * createStreamCallable() 

  
UpdateStream |  Updates the parameters of a single Stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateStreamAsync(UpdateStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateStreamAsync(Stream stream, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateStreamOperationCallable() 
  * updateStreamCallable() 

  
DeleteStream |  Deletes a single Stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteStreamAsync(DeleteStreamRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteStreamAsync(StreamName name) 
  * deleteStreamAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteStreamOperationCallable() 
  * deleteStreamCallable() 

  
GetStreamThumbnail |  Gets the thumbnail (image snapshot) of a single Stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStreamThumbnailAsync(GetStreamThumbnailRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * getStreamThumbnailAsync(String stream, String gcsObjectName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStreamThumbnailOperationCallable() 
  * getStreamThumbnailCallable() 

  
GenerateStreamHlsToken |  Generate the JWT auth token required to get the stream HLS contents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateStreamHlsToken(GenerateStreamHlsTokenRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateStreamHlsToken(String stream) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateStreamHlsTokenCallable() 

  
ListEvents |  Lists Events in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEvents(ListEventsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEvents(ClusterName parent) 
  * listEvents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEventsPagedCallable() 
  * listEventsCallable() 

  
GetEvent |  Gets details of a single Event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEvent(GetEventRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEvent(EventName name) 
  * getEvent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEventCallable() 

  
CreateEvent |  Creates a new Event in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEventAsync(CreateEventRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEventAsync(ClusterName parent, Event event, String eventId) 
  * createEventAsync(String parent, Event event, String eventId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEventOperationCallable() 
  * createEventCallable() 

  
UpdateEvent |  Updates the parameters of a single Event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEventAsync(UpdateEventRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEventAsync(Event event, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEventOperationCallable() 
  * updateEventCallable() 

  
DeleteEvent |  Deletes a single Event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEventAsync(DeleteEventRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEventAsync(EventName name) 
  * deleteEventAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEventOperationCallable() 
  * deleteEventCallable() 

  
ListSeries |  Lists Series in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSeries(ListSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSeries(ClusterName parent) 
  * listSeries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSeriesPagedCallable() 
  * listSeriesCallable() 

  
GetSeries |  Gets details of a single Series. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSeries(GetSeriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSeries(SeriesName name) 
  * getSeries(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSeriesCallable() 

  
CreateSeries |  Creates a new Series in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSeriesAsync(CreateSeriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSeriesAsync(ClusterName parent, Series series, String seriesId) 
  * createSeriesAsync(String parent, Series series, String seriesId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSeriesOperationCallable() 
  * createSeriesCallable() 

  
UpdateSeries |  Updates the parameters of a single Event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSeriesAsync(UpdateSeriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSeriesAsync(Series series, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSeriesOperationCallable() 
  * updateSeriesCallable() 

  
DeleteSeries |  Deletes a single Series. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSeriesAsync(DeleteSeriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSeriesAsync(SeriesName name) 
  * deleteSeriesAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSeriesOperationCallable() 
  * deleteSeriesCallable() 

  
MaterializeChannel |  Materialize a channel. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * materializeChannelAsync(MaterializeChannelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * materializeChannelAsync(ClusterName parent, Channel channel, String channelId) 
  * materializeChannelAsync(String parent, Channel channel, String channelId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * materializeChannelOperationCallable() 
  * materializeChannelCallable() 

  
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

This class can be customized by passing in a custom instance of StreamsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StreamsServiceSettings streamsServiceSettings =
         StreamsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     StreamsServiceClient streamsServiceClient = StreamsServiceClient.create(streamsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StreamsServiceSettings streamsServiceSettings =
         StreamsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     StreamsServiceClient streamsServiceClient = StreamsServiceClient.create(streamsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StreamsServiceSettings streamsServiceSettings =
         StreamsServiceSettings.newHttpJsonBuilder().build();
     StreamsServiceClient streamsServiceClient = StreamsServiceClient.create(streamsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > StreamsServiceClient

## Static Methods 

### create()
    
    
    public static final StreamsServiceClient create()

Constructs an instance of StreamsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StreamsServiceSettings settings)
    
    
    public static final StreamsServiceClient create(StreamsServiceSettings settings)

Constructs an instance of StreamsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StreamsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StreamsServiceStub stub)
    
    
    public static final StreamsServiceClient create(StreamsServiceStub stub)

Constructs an instance of StreamsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(StreamsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StreamsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.stub.StreamsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient)` |   
  
## Constructors 

### StreamsServiceClient(StreamsServiceSettings settings)
    
    
    protected StreamsServiceClient(StreamsServiceSettings settings)

Constructs an instance of StreamsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StreamsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceSettings)`  
  
  
### StreamsServiceClient(StreamsServiceStub stub)
    
    
    protected StreamsServiceClient(StreamsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StreamsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.stub.StreamsServiceStub)`  
  
  
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

### createClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(@Nullable LocationName parent, Cluster cluster, String clusterId)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = streamsServiceClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.LocationName`  
Required. Value for parent.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)`  
Required. The resource being created.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createClusterAsync(CreateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(CreateClusterRequest request)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Cluster response = streamsServiceClient.createClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createClusterAsync(String parent, Cluster cluster, String clusterId)
    
    
    public final OperationFuture<Cluster,OperationMetadata> createClusterAsync(String parent, Cluster cluster, String clusterId)

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Cluster cluster = Cluster.newBuilder().build();
       String clusterId = "clusterId561939637";
       Cluster response = streamsServiceClient.createClusterAsync(parent, cluster, clusterId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)`  
Required. The resource being created.  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createClusterCallable()
    
    
    public final UnaryCallable<CreateClusterRequest,Operation> createClusterCallable()

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           streamsServiceClient.createClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClusterOperationCallable()
    
    
    public final OperationCallable<CreateClusterRequest,Cluster,OperationMetadata> createClusterOperationCallable()

Creates a new Cluster in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateClusterRequest request =
           CreateClusterRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClusterId("clusterId561939637")
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           streamsServiceClient.createClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createEventAsync(@Nullable ClusterName parent, Event event, String eventId)
    
    
    public final OperationFuture<Event,OperationMetadata> createEventAsync(@Nullable ClusterName parent, Event event, String eventId)

Creates a new Event in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Event event = Event.newBuilder().build();
       String eventId = "eventId-1376502443";
       Event response = streamsServiceClient.createEventAsync(parent, event, eventId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Value for parent.  
`event` | `[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)`  
Required. The resource being created.  
`eventId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createEventAsync(CreateEventRequest request)
    
    
    public final OperationFuture<Event,OperationMetadata> createEventAsync(CreateEventRequest request)

Creates a new Event in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateEventRequest request =
           CreateEventRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setEventId("eventId-1376502443")
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Event response = streamsServiceClient.createEventAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createEventAsync(String parent, Event event, String eventId)
    
    
    public final OperationFuture<Event,OperationMetadata> createEventAsync(String parent, Event event, String eventId)

Creates a new Event in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Event event = Event.newBuilder().build();
       String eventId = "eventId-1376502443";
       Event response = streamsServiceClient.createEventAsync(parent, event, eventId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`event` | `[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)`  
Required. The resource being created.  
`eventId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createEventCallable()
    
    
    public final UnaryCallable<CreateEventRequest,Operation> createEventCallable()

Creates a new Event in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateEventRequest request =
           CreateEventRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setEventId("eventId-1376502443")
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.createEventCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateEventRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEventOperationCallable()
    
    
    public final OperationCallable<CreateEventRequest,Event,OperationMetadata> createEventOperationCallable()

Creates a new Event in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateEventRequest request =
           CreateEventRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setEventId("eventId-1376502443")
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Event, OperationMetadata> future =
           streamsServiceClient.createEventOperationCallable().futureCall(request);
       // Do something.
       Event response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createSeriesAsync(@Nullable ClusterName parent, Series series, String seriesId)
    
    
    public final OperationFuture<Series,OperationMetadata> createSeriesAsync(@Nullable ClusterName parent, Series series, String seriesId)

Creates a new Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Series series = Series.newBuilder().build();
       String seriesId = "seriesId1367098866";
       Series response = streamsServiceClient.createSeriesAsync(parent, series, seriesId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Value for parent.  
`series` | `[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)`  
Required. The resource being created.  
`seriesId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createSeriesAsync(CreateSeriesRequest request)
    
    
    public final OperationFuture<Series,OperationMetadata> createSeriesAsync(CreateSeriesRequest request)

Creates a new Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateSeriesRequest request =
           CreateSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setSeriesId("seriesId1367098866")
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Series response = streamsServiceClient.createSeriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createSeriesAsync(String parent, Series series, String seriesId)
    
    
    public final OperationFuture<Series,OperationMetadata> createSeriesAsync(String parent, Series series, String seriesId)

Creates a new Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Series series = Series.newBuilder().build();
       String seriesId = "seriesId1367098866";
       Series response = streamsServiceClient.createSeriesAsync(parent, series, seriesId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`series` | `[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)`  
Required. The resource being created.  
`seriesId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createSeriesCallable()
    
    
    public final UnaryCallable<CreateSeriesRequest,Operation> createSeriesCallable()

Creates a new Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateSeriesRequest request =
           CreateSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setSeriesId("seriesId1367098866")
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.createSeriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateSeriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSeriesOperationCallable()
    
    
    public final OperationCallable<CreateSeriesRequest,Series,OperationMetadata> createSeriesOperationCallable()

Creates a new Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateSeriesRequest request =
           CreateSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setSeriesId("seriesId1367098866")
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Series, OperationMetadata> future =
           streamsServiceClient.createSeriesOperationCallable().futureCall(request);
       // Do something.
       Series response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateSeriesRequest),[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createStreamAsync(@Nullable ClusterName parent, Stream stream, String streamId)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(@Nullable ClusterName parent, Stream stream, String streamId)

Creates a new Stream in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Stream stream = Stream.newBuilder().build();
       String streamId = "streamId1790933179";
       Stream response = streamsServiceClient.createStreamAsync(parent, stream, streamId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Value for parent.  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)`  
Required. The resource being created.  
`streamId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createStreamAsync(CreateStreamRequest request)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(CreateStreamRequest request)

Creates a new Stream in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Stream response = streamsServiceClient.createStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createStreamAsync(String parent, Stream stream, String streamId)
    
    
    public final OperationFuture<Stream,OperationMetadata> createStreamAsync(String parent, Stream stream, String streamId)

Creates a new Stream in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Stream stream = Stream.newBuilder().build();
       String streamId = "streamId1790933179";
       Stream response = streamsServiceClient.createStreamAsync(parent, stream, streamId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)`  
Required. The resource being created.  
`streamId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the requesting object.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### createStreamCallable()
    
    
    public final UnaryCallable<CreateStreamRequest,Operation> createStreamCallable()

Creates a new Stream in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.createStreamCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStreamOperationCallable()
    
    
    public final OperationCallable<CreateStreamRequest,Stream,OperationMetadata> createStreamOperationCallable()

Creates a new Stream in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       CreateStreamRequest request =
           CreateStreamRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setStreamId("streamId1790933179")
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Stream, OperationMetadata> future =
           streamsServiceClient.createStreamOperationCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(@Nullable ClusterName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(@Nullable ClusterName name)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       streamsServiceClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(DeleteClusterRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(DeleteClusterRequest request)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       streamsServiceClient.deleteClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteClusterAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClusterAsync(String name)

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       streamsServiceClient.deleteClusterAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteClusterCallable()
    
    
    public final UnaryCallable<DeleteClusterRequest,Operation> deleteClusterCallable()

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           streamsServiceClient.deleteClusterCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClusterOperationCallable()
    
    
    public final OperationCallable<DeleteClusterRequest,Empty,OperationMetadata> deleteClusterOperationCallable()

Deletes a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteClusterRequest request =
           DeleteClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           streamsServiceClient.deleteClusterOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteEventAsync(@Nullable EventName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEventAsync(@Nullable EventName name)

Deletes a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       EventName name = EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]");
       streamsServiceClient.deleteEventAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.EventName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteEventAsync(DeleteEventRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEventAsync(DeleteEventRequest request)

Deletes a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteEventRequest request =
           DeleteEventRequest.newBuilder()
               .setName(EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString())
               .setRequestId("requestId693933066")
               .build();
       streamsServiceClient.deleteEventAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteEventAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEventAsync(String name)

Deletes a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString();
       streamsServiceClient.deleteEventAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteEventCallable()
    
    
    public final UnaryCallable<DeleteEventRequest,Operation> deleteEventCallable()

Deletes a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteEventRequest request =
           DeleteEventRequest.newBuilder()
               .setName(EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.deleteEventCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteEventRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEventOperationCallable()
    
    
    public final OperationCallable<DeleteEventRequest,Empty,OperationMetadata> deleteEventOperationCallable()

Deletes a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteEventRequest request =
           DeleteEventRequest.newBuilder()
               .setName(EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           streamsServiceClient.deleteEventOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteEventRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteSeriesAsync(@Nullable SeriesName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSeriesAsync(@Nullable SeriesName name)

Deletes a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       SeriesName name = SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]");
       streamsServiceClient.deleteSeriesAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.SeriesName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteSeriesAsync(DeleteSeriesRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSeriesAsync(DeleteSeriesRequest request)

Deletes a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteSeriesRequest request =
           DeleteSeriesRequest.newBuilder()
               .setName(SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString())
               .setRequestId("requestId693933066")
               .build();
       streamsServiceClient.deleteSeriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteSeriesAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSeriesAsync(String name)

Deletes a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString();
       streamsServiceClient.deleteSeriesAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteSeriesCallable()
    
    
    public final UnaryCallable<DeleteSeriesRequest,Operation> deleteSeriesCallable()

Deletes a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteSeriesRequest request =
           DeleteSeriesRequest.newBuilder()
               .setName(SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.deleteSeriesCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteSeriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSeriesOperationCallable()
    
    
    public final OperationCallable<DeleteSeriesRequest,Empty,OperationMetadata> deleteSeriesOperationCallable()

Deletes a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteSeriesRequest request =
           DeleteSeriesRequest.newBuilder()
               .setName(SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           streamsServiceClient.deleteSeriesOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteSeriesRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(@Nullable StreamName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(@Nullable StreamName name)

Deletes a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       StreamName name = StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]");
       streamsServiceClient.deleteStreamAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.StreamName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(DeleteStreamRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(DeleteStreamRequest request)

Deletes a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       streamsServiceClient.deleteStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteStreamAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteStreamAsync(String name)

Deletes a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString();
       streamsServiceClient.deleteStreamAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### deleteStreamCallable()
    
    
    public final UnaryCallable<DeleteStreamRequest,Operation> deleteStreamCallable()

Deletes a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.deleteStreamCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteStreamOperationCallable()
    
    
    public final OperationCallable<DeleteStreamRequest,Empty,OperationMetadata> deleteStreamOperationCallable()

Deletes a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       DeleteStreamRequest request =
           DeleteStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           streamsServiceClient.deleteStreamOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteStreamRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### generateStreamHlsToken(GenerateStreamHlsTokenRequest request)
    
    
    public final GenerateStreamHlsTokenResponse generateStreamHlsToken(GenerateStreamHlsTokenRequest request)

Generate the JWT auth token required to get the stream HLS contents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GenerateStreamHlsTokenRequest request =
           GenerateStreamHlsTokenRequest.newBuilder().setStream("stream-891990144").build();
       GenerateStreamHlsTokenResponse response =
           streamsServiceClient.generateStreamHlsToken(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateStreamHlsTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GenerateStreamHlsTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStreamHlsTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GenerateStreamHlsTokenResponse)` |   
  
### generateStreamHlsToken(String stream)
    
    
    public final GenerateStreamHlsTokenResponse generateStreamHlsToken(String stream)

Generate the JWT auth token required to get the stream HLS contents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String stream = "stream-891990144";
       GenerateStreamHlsTokenResponse response = streamsServiceClient.generateStreamHlsToken(stream);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`stream` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStreamHlsTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GenerateStreamHlsTokenResponse)` |   
  
### generateStreamHlsTokenCallable()
    
    
    public final UnaryCallable<GenerateStreamHlsTokenRequest,GenerateStreamHlsTokenResponse> generateStreamHlsTokenCallable()

Generate the JWT auth token required to get the stream HLS contents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GenerateStreamHlsTokenRequest request =
           GenerateStreamHlsTokenRequest.newBuilder().setStream("stream-891990144").build();
       ApiFuture<GenerateStreamHlsTokenResponse> future =
           streamsServiceClient.generateStreamHlsTokenCallable().futureCall(request);
       // Do something.
       GenerateStreamHlsTokenResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateStreamHlsTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GenerateStreamHlsTokenRequest),[GenerateStreamHlsTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GenerateStreamHlsTokenResponse)>` |   
  
### getCluster(@Nullable ClusterName name)
    
    
    public final Cluster getCluster(@Nullable ClusterName name)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Cluster response = streamsServiceClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)` |   
  
### getCluster(GetClusterRequest request)
    
    
    public final Cluster getCluster(GetClusterRequest request)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .build();
       Cluster response = streamsServiceClient.getCluster(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)` |   
  
### getCluster(String name)
    
    
    public final Cluster getCluster(String name)

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Cluster response = streamsServiceClient.getCluster(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)` |   
  
### getClusterCallable()
    
    
    public final UnaryCallable<GetClusterRequest,Cluster> getClusterCallable()

Gets details of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetClusterRequest request =
           GetClusterRequest.newBuilder()
               .setName(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .build();
       ApiFuture<Cluster> future = streamsServiceClient.getClusterCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)>` |   
  
### getEvent(@Nullable EventName name)
    
    
    public final Event getEvent(@Nullable EventName name)

Gets details of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       EventName name = EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]");
       Event response = streamsServiceClient.getEvent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.EventName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)` |   
  
### getEvent(GetEventRequest request)
    
    
    public final Event getEvent(GetEventRequest request)

Gets details of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetEventRequest request =
           GetEventRequest.newBuilder()
               .setName(EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString())
               .build();
       Event response = streamsServiceClient.getEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)` |   
  
### getEvent(String name)
    
    
    public final Event getEvent(String name)

Gets details of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString();
       Event response = streamsServiceClient.getEvent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)` |   
  
### getEventCallable()
    
    
    public final UnaryCallable<GetEventRequest,Event> getEventCallable()

Gets details of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetEventRequest request =
           GetEventRequest.newBuilder()
               .setName(EventName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[EVENT]").toString())
               .build();
       ApiFuture<Event> future = streamsServiceClient.getEventCallable().futureCall(request);
       // Do something.
       Event response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)>` |   
  
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
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = streamsServiceClient.getLocation(request);
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
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = streamsServiceClient.getLocationCallable().futureCall(request);
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
  
### getSeries(@Nullable SeriesName name)
    
    
    public final Series getSeries(@Nullable SeriesName name)

Gets details of a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       SeriesName name = SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]");
       Series response = streamsServiceClient.getSeries(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.SeriesName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)` |   
  
### getSeries(GetSeriesRequest request)
    
    
    public final Series getSeries(GetSeriesRequest request)

Gets details of a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetSeriesRequest request =
           GetSeriesRequest.newBuilder()
               .setName(SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString())
               .build();
       Series response = streamsServiceClient.getSeries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)` |   
  
### getSeries(String name)
    
    
    public final Series getSeries(String name)

Gets details of a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString();
       Series response = streamsServiceClient.getSeries(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)` |   
  
### getSeriesCallable()
    
    
    public final UnaryCallable<GetSeriesRequest,Series> getSeriesCallable()

Gets details of a single Series.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetSeriesRequest request =
           GetSeriesRequest.newBuilder()
               .setName(SeriesName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[SERIES]").toString())
               .build();
       ApiFuture<Series> future = streamsServiceClient.getSeriesCallable().futureCall(request);
       // Do something.
       Series response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetSeriesRequest),[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)>` |   
  
### getSettings()
    
    
    public final @Nullable StreamsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.StreamsServiceSettings` |   
  
### getStream(@Nullable StreamName name)
    
    
    public final Stream getStream(@Nullable StreamName name)

Gets details of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       StreamName name = StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]");
       Stream response = streamsServiceClient.getStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.StreamName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)` |   
  
### getStream(GetStreamRequest request)
    
    
    public final Stream getStream(GetStreamRequest request)

Gets details of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetStreamRequest request =
           GetStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString())
               .build();
       Stream response = streamsServiceClient.getStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)` |   
  
### getStream(String name)
    
    
    public final Stream getStream(String name)

Gets details of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String name = StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString();
       Stream response = streamsServiceClient.getStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)` |   
  
### getStreamCallable()
    
    
    public final UnaryCallable<GetStreamRequest,Stream> getStreamCallable()

Gets details of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetStreamRequest request =
           GetStreamRequest.newBuilder()
               .setName(StreamName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[STREAM]").toString())
               .build();
       ApiFuture<Stream> future = streamsServiceClient.getStreamCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)>` |   
  
### getStreamThumbnailAsync(GetStreamThumbnailRequest request)
    
    
    public final OperationFuture<GetStreamThumbnailResponse,OperationMetadata> getStreamThumbnailAsync(GetStreamThumbnailRequest request)

Gets the thumbnail (image snapshot) of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetStreamThumbnailRequest request =
           GetStreamThumbnailRequest.newBuilder()
               .setStream("stream-891990144")
               .setGcsObjectName("gcsObjectName-1987275551")
               .setEvent("event96891546")
               .setRequestId("requestId693933066")
               .build();
       GetStreamThumbnailResponse response =
           streamsServiceClient.getStreamThumbnailAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStreamThumbnailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GetStreamThumbnailResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### getStreamThumbnailAsync(String stream, String gcsObjectName)
    
    
    public final OperationFuture<GetStreamThumbnailResponse,OperationMetadata> getStreamThumbnailAsync(String stream, String gcsObjectName)

Gets the thumbnail (image snapshot) of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String stream = "stream-891990144";
       String gcsObjectName = "gcsObjectName-1987275551";
       GetStreamThumbnailResponse response =
           streamsServiceClient.getStreamThumbnailAsync(stream, gcsObjectName).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stream for to get the thumbnail from.  
`gcsObjectName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GCS object to store the thumbnail image.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GetStreamThumbnailResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### getStreamThumbnailCallable()
    
    
    public final UnaryCallable<GetStreamThumbnailRequest,Operation> getStreamThumbnailCallable()

Gets the thumbnail (image snapshot) of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetStreamThumbnailRequest request =
           GetStreamThumbnailRequest.newBuilder()
               .setStream("stream-891990144")
               .setGcsObjectName("gcsObjectName-1987275551")
               .setEvent("event96891546")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           streamsServiceClient.getStreamThumbnailCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStreamThumbnailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getStreamThumbnailOperationCallable()
    
    
    public final OperationCallable<GetStreamThumbnailRequest,GetStreamThumbnailResponse,OperationMetadata> getStreamThumbnailOperationCallable()

Gets the thumbnail (image snapshot) of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       GetStreamThumbnailRequest request =
           GetStreamThumbnailRequest.newBuilder()
               .setStream("stream-891990144")
               .setGcsObjectName("gcsObjectName-1987275551")
               .setEvent("event96891546")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<GetStreamThumbnailResponse, OperationMetadata> future =
           streamsServiceClient.getStreamThumbnailOperationCallable().futureCall(request);
       // Do something.
       GetStreamThumbnailResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GetStreamThumbnailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailRequest),[GetStreamThumbnailResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetStreamThumbnailResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### getStub()
    
    
    public StreamsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.stub.StreamsServiceStub)` |   
  
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
  
### listClusters(@Nullable LocationName parent)
    
    
    public final StreamsServiceClient.ListClustersPagedResponse listClusters(@Nullable LocationName parent)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Cluster element : streamsServiceClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.LocationName`  
Required. Parent value for ListClustersRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListClustersPagedResponse)` |   
  
### listClusters(ListClustersRequest request)
    
    
    public final StreamsServiceClient.ListClustersPagedResponse listClusters(ListClustersRequest request)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Cluster element : streamsServiceClient.listClusters(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListClustersPagedResponse)` |   
  
### listClusters(String parent)
    
    
    public final StreamsServiceClient.ListClustersPagedResponse listClusters(String parent)

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Cluster element : streamsServiceClient.listClusters(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListClustersRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListClustersPagedResponse)` |   
  
### listClustersCallable()
    
    
    public final UnaryCallable<ListClustersRequest,ListClustersResponse> listClustersCallable()

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListClustersResponse response = streamsServiceClient.listClustersCallable().call(request);
         for (Cluster element : response.getClustersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListClustersResponse)>` |   
  
### listClustersPagedCallable()
    
    
    public final UnaryCallable<ListClustersRequest,StreamsServiceClient.ListClustersPagedResponse> listClustersPagedCallable()

Lists Clusters in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListClustersRequest request =
           ListClustersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Cluster> future =
           streamsServiceClient.listClustersPagedCallable().futureCall(request);
       // Do something.
       for (Cluster element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListClustersRequest),[ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListClustersPagedResponse)>` |   
  
### listEvents(@Nullable ClusterName parent)
    
    
    public final StreamsServiceClient.ListEventsPagedResponse listEvents(@Nullable ClusterName parent)

Lists Events in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (Event element : streamsServiceClient.listEvents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Parent value for ListEventsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListEventsPagedResponse)` |   
  
### listEvents(ListEventsRequest request)
    
    
    public final StreamsServiceClient.ListEventsPagedResponse listEvents(ListEventsRequest request)

Lists Events in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListEventsRequest request =
           ListEventsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Event element : streamsServiceClient.listEvents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListEventsPagedResponse)` |   
  
### listEvents(String parent)
    
    
    public final StreamsServiceClient.ListEventsPagedResponse listEvents(String parent)

Lists Events in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (Event element : streamsServiceClient.listEvents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListEventsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListEventsPagedResponse)` |   
  
### listEventsCallable()
    
    
    public final UnaryCallable<ListEventsRequest,ListEventsResponse> listEventsCallable()

Lists Events in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListEventsRequest request =
           ListEventsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEventsResponse response = streamsServiceClient.listEventsCallable().call(request);
         for (Event element : response.getEventsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListEventsRequest),[ListEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListEventsResponse)>` |   
  
### listEventsPagedCallable()
    
    
    public final UnaryCallable<ListEventsRequest,StreamsServiceClient.ListEventsPagedResponse> listEventsPagedCallable()

Lists Events in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListEventsRequest request =
           ListEventsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Event> future = streamsServiceClient.listEventsPagedCallable().futureCall(request);
       // Do something.
       for (Event element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListEventsRequest),[ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListEventsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final StreamsServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : streamsServiceClient.listLocations(request).iterateAll()) {
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
`[StreamsServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = streamsServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,StreamsServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           streamsServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListLocationsPagedResponse)>` |   
  
### listSeries(@Nullable ClusterName parent)
    
    
    public final StreamsServiceClient.ListSeriesPagedResponse listSeries(@Nullable ClusterName parent)

Lists Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (Series element : streamsServiceClient.listSeries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Parent value for ListSeriesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListSeriesPagedResponse)` |   
  
### listSeries(ListSeriesRequest request)
    
    
    public final StreamsServiceClient.ListSeriesPagedResponse listSeries(ListSeriesRequest request)

Lists Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListSeriesRequest request =
           ListSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Series element : streamsServiceClient.listSeries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListSeriesPagedResponse)` |   
  
### listSeries(String parent)
    
    
    public final StreamsServiceClient.ListSeriesPagedResponse listSeries(String parent)

Lists Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (Series element : streamsServiceClient.listSeries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListSeriesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListSeriesPagedResponse)` |   
  
### listSeriesCallable()
    
    
    public final UnaryCallable<ListSeriesRequest,ListSeriesResponse> listSeriesCallable()

Lists Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListSeriesRequest request =
           ListSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSeriesResponse response = streamsServiceClient.listSeriesCallable().call(request);
         for (Series element : response.getSeriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListSeriesRequest),[ListSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListSeriesResponse)>` |   
  
### listSeriesPagedCallable()
    
    
    public final UnaryCallable<ListSeriesRequest,StreamsServiceClient.ListSeriesPagedResponse> listSeriesPagedCallable()

Lists Series in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListSeriesRequest request =
           ListSeriesRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Series> future = streamsServiceClient.listSeriesPagedCallable().futureCall(request);
       // Do something.
       for (Series element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListSeriesRequest),[ListSeriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListSeriesPagedResponse)>` |   
  
### listStreams(@Nullable ClusterName parent)
    
    
    public final StreamsServiceClient.ListStreamsPagedResponse listStreams(@Nullable ClusterName parent)

Lists Streams in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       for (Stream element : streamsServiceClient.listStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Parent value for ListStreamsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListStreamsPagedResponse)` |   
  
### listStreams(ListStreamsRequest request)
    
    
    public final StreamsServiceClient.ListStreamsPagedResponse listStreams(ListStreamsRequest request)

Lists Streams in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Stream element : streamsServiceClient.listStreams(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListStreamsPagedResponse)` |   
  
### listStreams(String parent)
    
    
    public final StreamsServiceClient.ListStreamsPagedResponse listStreams(String parent)

Lists Streams in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       for (Stream element : streamsServiceClient.listStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListStreamsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[StreamsServiceClient.ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListStreamsPagedResponse)` |   
  
### listStreamsCallable()
    
    
    public final UnaryCallable<ListStreamsRequest,ListStreamsResponse> listStreamsCallable()

Lists Streams in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListStreamsResponse response = streamsServiceClient.listStreamsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListStreamsRequest),[ListStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListStreamsResponse)>` |   
  
### listStreamsPagedCallable()
    
    
    public final UnaryCallable<ListStreamsRequest,StreamsServiceClient.ListStreamsPagedResponse> listStreamsPagedCallable()

Lists Streams in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ListStreamsRequest request =
           ListStreamsRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Stream> future =
           streamsServiceClient.listStreamsPagedCallable().futureCall(request);
       // Do something.
       for (Stream element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListStreamsRequest),[ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamsServiceClient.ListStreamsPagedResponse)>` |   
  
### materializeChannelAsync(@Nullable ClusterName parent, Channel channel, String channelId)
    
    
    public final OperationFuture<Channel,OperationMetadata> materializeChannelAsync(@Nullable ClusterName parent, Channel channel, String channelId)

Materialize a channel.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       ClusterName parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]");
       Channel channel = Channel.newBuilder().build();
       String channelId = "channelId1461735806";
       Channel response =
           streamsServiceClient.materializeChannelAsync(parent, channel, channelId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.visionai.v1.ClusterName`  
Required. Value for parent.  
`channel` | `[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel)`  
Required. The resource being created.  
`channelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the channel.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### materializeChannelAsync(MaterializeChannelRequest request)
    
    
    public final OperationFuture<Channel,OperationMetadata> materializeChannelAsync(MaterializeChannelRequest request)

Materialize a channel.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       MaterializeChannelRequest request =
           MaterializeChannelRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setChannelId("channelId1461735806")
               .setChannel(Channel.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Channel response = streamsServiceClient.materializeChannelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MaterializeChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.MaterializeChannelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### materializeChannelAsync(String parent, Channel channel, String channelId)
    
    
    public final OperationFuture<Channel,OperationMetadata> materializeChannelAsync(String parent, Channel channel, String channelId)

Materialize a channel.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       String parent = ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString();
       Channel channel = Channel.newBuilder().build();
       String channelId = "channelId1461735806";
       Channel response =
           streamsServiceClient.materializeChannelAsync(parent, channel, channelId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`channel` | `[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel)`  
Required. The resource being created.  
`channelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Id of the channel.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### materializeChannelCallable()
    
    
    public final UnaryCallable<MaterializeChannelRequest,Operation> materializeChannelCallable()

Materialize a channel.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       MaterializeChannelRequest request =
           MaterializeChannelRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setChannelId("channelId1461735806")
               .setChannel(Channel.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           streamsServiceClient.materializeChannelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MaterializeChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.MaterializeChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### materializeChannelOperationCallable()
    
    
    public final OperationCallable<MaterializeChannelRequest,Channel,OperationMetadata> materializeChannelOperationCallable()

Materialize a channel.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       MaterializeChannelRequest request =
           MaterializeChannelRequest.newBuilder()
               .setParent(ClusterName.of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
               .setChannelId("channelId1461735806")
               .setChannel(Channel.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Channel, OperationMetadata> future =
           streamsServiceClient.materializeChannelOperationCallable().futureCall(request);
       // Do something.
       Channel response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MaterializeChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.MaterializeChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateClusterAsync(Cluster cluster, FieldMask updateMask)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(Cluster cluster, FieldMask updateMask)

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       Cluster cluster = Cluster.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Cluster response = streamsServiceClient.updateClusterAsync(cluster, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateClusterAsync(UpdateClusterRequest request)
    
    
    public final OperationFuture<Cluster,OperationMetadata> updateClusterAsync(UpdateClusterRequest request)

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Cluster response = streamsServiceClient.updateClusterAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateClusterCallable()
    
    
    public final UnaryCallable<UpdateClusterRequest,Operation> updateClusterCallable()

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           streamsServiceClient.updateClusterCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClusterOperationCallable()
    
    
    public final OperationCallable<UpdateClusterRequest,Cluster,OperationMetadata> updateClusterOperationCallable()

Updates the parameters of a single Cluster.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateClusterRequest request =
           UpdateClusterRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCluster(Cluster.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Cluster, OperationMetadata> future =
           streamsServiceClient.updateClusterOperationCallable().futureCall(request);
       // Do something.
       Cluster response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateEventAsync(Event event, FieldMask updateMask)
    
    
    public final OperationFuture<Event,OperationMetadata> updateEventAsync(Event event, FieldMask updateMask)

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       Event event = Event.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Event response = streamsServiceClient.updateEventAsync(event, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`event` | `[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Event resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateEventAsync(UpdateEventRequest request)
    
    
    public final OperationFuture<Event,OperationMetadata> updateEventAsync(UpdateEventRequest request)

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateEventRequest request =
           UpdateEventRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Event response = streamsServiceClient.updateEventAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateEventCallable()
    
    
    public final UnaryCallable<UpdateEventRequest,Operation> updateEventCallable()

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateEventRequest request =
           UpdateEventRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.updateEventCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateEventRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEventOperationCallable()
    
    
    public final OperationCallable<UpdateEventRequest,Event,OperationMetadata> updateEventOperationCallable()

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateEventRequest request =
           UpdateEventRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEvent(Event.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Event, OperationMetadata> future =
           streamsServiceClient.updateEventOperationCallable().futureCall(request);
       // Do something.
       Event response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Event),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateSeriesAsync(Series series, FieldMask updateMask)
    
    
    public final OperationFuture<Series,OperationMetadata> updateSeriesAsync(Series series, FieldMask updateMask)

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       Series series = Series.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Series response = streamsServiceClient.updateSeriesAsync(series, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`series` | `[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Series resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateSeriesAsync(UpdateSeriesRequest request)
    
    
    public final OperationFuture<Series,OperationMetadata> updateSeriesAsync(UpdateSeriesRequest request)

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateSeriesRequest request =
           UpdateSeriesRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Series response = streamsServiceClient.updateSeriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateSeriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateSeriesCallable()
    
    
    public final UnaryCallable<UpdateSeriesRequest,Operation> updateSeriesCallable()

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateSeriesRequest request =
           UpdateSeriesRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.updateSeriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateSeriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSeriesOperationCallable()
    
    
    public final OperationCallable<UpdateSeriesRequest,Series,OperationMetadata> updateSeriesOperationCallable()

Updates the parameters of a single Event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateSeriesRequest request =
           UpdateSeriesRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSeries(Series.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Series, OperationMetadata> future =
           streamsServiceClient.updateSeriesOperationCallable().futureCall(request);
       // Do something.
       Series response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateSeriesRequest),[Series](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Series),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateStreamAsync(Stream stream, FieldMask updateMask)
    
    
    public final OperationFuture<Stream,OperationMetadata> updateStreamAsync(Stream stream, FieldMask updateMask)

Updates the parameters of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       Stream stream = Stream.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Stream response = streamsServiceClient.updateStreamAsync(stream, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateStreamAsync(UpdateStreamRequest request)
    
    
    public final OperationFuture<Stream,OperationMetadata> updateStreamAsync(UpdateStreamRequest request)

Updates the parameters of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Stream response = streamsServiceClient.updateStreamAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
### updateStreamCallable()
    
    
    public final UnaryCallable<UpdateStreamRequest,Operation> updateStreamCallable()

Updates the parameters of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = streamsServiceClient.updateStreamCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateStreamOperationCallable()
    
    
    public final OperationCallable<UpdateStreamRequest,Stream,OperationMetadata> updateStreamOperationCallable()

Updates the parameters of a single Stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StreamsServiceClient streamsServiceClient = StreamsServiceClient.create()) {
       UpdateStreamRequest request =
           UpdateStreamRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setStream(Stream.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Stream, OperationMetadata> future =
           streamsServiceClient.updateStreamOperationCallable().futureCall(request);
       // Do something.
       Stream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
