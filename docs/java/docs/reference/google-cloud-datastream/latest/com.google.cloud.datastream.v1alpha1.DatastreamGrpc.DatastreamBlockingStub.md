---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DatastreamGrpc.DatastreamBlockingStub
title: Class DatastreamGrpc.DatastreamBlockingStub (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:24.489687+00:00
---

# Class DatastreamGrpc.DatastreamBlockingStub (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DatastreamGrpc.DatastreamBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastreamGrpc.DatastreamBlockingStub (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 
    
    
    public static final class DatastreamGrpc.DatastreamBlockingStub extends AbstractBlockingStub<DatastreamGrpc.DatastreamBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service Datastream.

Datastream service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > DatastreamGrpc.DatastreamBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected DatastreamGrpc.DatastreamBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamGrpc.DatastreamBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DatastreamGrpc.DatastreamBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createConnectionProfile(CreateConnectionProfileRequest request)
    
    
    public Operation createConnectionProfile(CreateConnectionProfileRequest request)

Use this method to create a connection profile in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.CreateConnectionProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createPrivateConnection(CreatePrivateConnectionRequest request)
    
    
    public Operation createPrivateConnection(CreatePrivateConnectionRequest request)

Use this method to create a private connectivity configuration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.CreatePrivateConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createRoute(CreateRouteRequest request)
    
    
    public Operation createRoute(CreateRouteRequest request)

Use this method to create a route for a private connectivity in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.CreateRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createStream(CreateStreamRequest request)
    
    
    public Operation createStream(CreateStreamRequest request)

Use this method to create a stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.CreateStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteConnectionProfile(DeleteConnectionProfileRequest request)
    
    
    public Operation deleteConnectionProfile(DeleteConnectionProfileRequest request)

Use this method to delete a connection profile..

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DeleteConnectionProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deletePrivateConnection(DeletePrivateConnectionRequest request)
    
    
    public Operation deletePrivateConnection(DeletePrivateConnectionRequest request)

Use this method to delete a private connectivity configuration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DeletePrivateConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteRoute(DeleteRouteRequest request)
    
    
    public Operation deleteRoute(DeleteRouteRequest request)

Use this method to delete a route.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DeleteRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteStream(DeleteStreamRequest request)
    
    
    public Operation deleteStream(DeleteStreamRequest request)

Use this method to delete a stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DeleteStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### discoverConnectionProfile(DiscoverConnectionProfileRequest request)
    
    
    public DiscoverConnectionProfileResponse discoverConnectionProfile(DiscoverConnectionProfileRequest request)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects under a parent data object that's optionally supplied in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DiscoverConnectionProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DiscoverConnectionProfileResponse)` |   
  
### fetchErrors(FetchErrorsRequest request)
    
    
    public Operation fetchErrors(FetchErrorsRequest request)

Use this method to fetch any errors associated with a stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchErrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.FetchErrorsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### fetchStaticIps(FetchStaticIpsRequest request)
    
    
    public FetchStaticIpsResponse fetchStaticIps(FetchStaticIpsRequest request)

The FetchStaticIps API call exposes the static ips used by Datastream. Typically, a request returns children data objects under a parent data object that's optionally supplied in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.FetchStaticIpsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchStaticIpsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.FetchStaticIpsResponse)` |   
  
### getConnectionProfile(GetConnectionProfileRequest request)
    
    
    public ConnectionProfile getConnectionProfile(GetConnectionProfileRequest request)

Use this method to get details about a connection profile.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.GetConnectionProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ConnectionProfile)` |   
  
### getPrivateConnection(GetPrivateConnectionRequest request)
    
    
    public PrivateConnection getPrivateConnection(GetPrivateConnectionRequest request)

Use this method to get details about a private connectivity configuration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.GetPrivateConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.PrivateConnection)` |   
  
### getRoute(GetRouteRequest request)
    
    
    public Route getRoute(GetRouteRequest request)

Use this method to get details about a route.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.GetRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.Route)` |   
  
### getStream(GetStreamRequest request)
    
    
    public Stream getStream(GetStreamRequest request)

Use this method to get details about a stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.GetStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.Stream)` |   
  
### listConnectionProfiles(ListConnectionProfilesRequest request)
    
    
    public ListConnectionProfilesResponse listConnectionProfiles(ListConnectionProfilesRequest request)

Use this method to list connection profiles created in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListConnectionProfilesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListConnectionProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListConnectionProfilesResponse)` |   
  
### listPrivateConnections(ListPrivateConnectionsRequest request)
    
    
    public ListPrivateConnectionsResponse listPrivateConnections(ListPrivateConnectionsRequest request)

Use this method to list private connectivity configurations in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListPrivateConnectionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListPrivateConnectionsResponse)` |   
  
### listRoutes(ListRoutesRequest request)
    
    
    public ListRoutesResponse listRoutes(ListRoutesRequest request)

Use this method to list routes created for a private connectivity in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListRoutesResponse)` |   
  
### listStreams(ListStreamsRequest request)
    
    
    public ListStreamsResponse listStreams(ListStreamsRequest request)

Use this method to list streams in a project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListStreamsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.ListStreamsResponse)` |   
  
### updateConnectionProfile(UpdateConnectionProfileRequest request)
    
    
    public Operation updateConnectionProfile(UpdateConnectionProfileRequest request)

Use this method to update the parameters of a connection profile.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.UpdateConnectionProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateStream(UpdateStreamRequest request)
    
    
    public Operation updateStream(UpdateStreamRequest request)

Use this method to update the configuration of a stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.UpdateStreamRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
