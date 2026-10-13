---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcGrpc.EventarcBlockingV2Stub
title: Class EventarcGrpc.EventarcBlockingV2Stub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:39.841309+00:00
---

# Class EventarcGrpc.EventarcBlockingV2Stub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcGrpc.EventarcBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EventarcGrpc.EventarcBlockingV2Stub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.2.4 
    
    
    public static final class EventarcGrpc.EventarcBlockingV2Stub extends AbstractBlockingStub<EventarcGrpc.EventarcBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service Eventarc.

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > EventarcGrpc.EventarcBlockingV2Stub

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
    
    
    protected EventarcGrpc.EventarcBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[EventarcGrpc.EventarcBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.EventarcGrpc.EventarcBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createChannel(CreateChannelRequest request)
    
    
    public Operation createChannel(CreateChannelRequest request)

Create a new channel in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createChannelConnection(CreateChannelConnectionRequest request)
    
    
    public Operation createChannelConnection(CreateChannelConnectionRequest request)

Create a new ChannelConnection in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateChannelConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createEnrollment(CreateEnrollmentRequest request)
    
    
    public Operation createEnrollment(CreateEnrollmentRequest request)

Create a new Enrollment in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateEnrollmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createGoogleApiSource(CreateGoogleApiSourceRequest request)
    
    
    public Operation createGoogleApiSource(CreateGoogleApiSourceRequest request)

Create a new GoogleApiSource in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateGoogleApiSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createMessageBus(CreateMessageBusRequest request)
    
    
    public Operation createMessageBus(CreateMessageBusRequest request)

Create a new MessageBus in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateMessageBusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createPipeline(CreatePipelineRequest request)
    
    
    public Operation createPipeline(CreatePipelineRequest request)

Create a new Pipeline in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreatePipelineRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createTrigger(CreateTriggerRequest request)
    
    
    public Operation createTrigger(CreateTriggerRequest request)

Create a new trigger in a particular project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.CreateTriggerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteChannel(DeleteChannelRequest request)
    
    
    public Operation deleteChannel(DeleteChannelRequest request)

Delete a single channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteChannelConnection(DeleteChannelConnectionRequest request)
    
    
    public Operation deleteChannelConnection(DeleteChannelConnectionRequest request)

Delete a single ChannelConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteChannelConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteEnrollment(DeleteEnrollmentRequest request)
    
    
    public Operation deleteEnrollment(DeleteEnrollmentRequest request)

Delete a single Enrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteEnrollmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteGoogleApiSource(DeleteGoogleApiSourceRequest request)
    
    
    public Operation deleteGoogleApiSource(DeleteGoogleApiSourceRequest request)

Delete a single GoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteGoogleApiSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteMessageBus(DeleteMessageBusRequest request)
    
    
    public Operation deleteMessageBus(DeleteMessageBusRequest request)

Delete a single message bus.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteMessageBusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deletePipeline(DeletePipelineRequest request)
    
    
    public Operation deletePipeline(DeletePipelineRequest request)

Delete a single pipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeletePipelineRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTrigger(DeleteTriggerRequest request)
    
    
    public Operation deleteTrigger(DeleteTriggerRequest request)

Delete a single trigger.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.DeleteTriggerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getChannel(GetChannelRequest request)
    
    
    public Channel getChannel(GetChannelRequest request)

Get a single Channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Channel)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getChannelConnection(GetChannelConnectionRequest request)
    
    
    public ChannelConnection getChannelConnection(GetChannelConnectionRequest request)

Get a single ChannelConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChannelConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetChannelConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChannelConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ChannelConnection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getEnrollment(GetEnrollmentRequest request)
    
    
    public Enrollment getEnrollment(GetEnrollmentRequest request)

Get a single Enrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetEnrollmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Enrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Enrollment)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGoogleApiSource(GetGoogleApiSourceRequest request)
    
    
    public GoogleApiSource getGoogleApiSource(GetGoogleApiSourceRequest request)

Get a single GoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetGoogleApiSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleApiSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleApiSource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGoogleChannelConfig(GetGoogleChannelConfigRequest request)
    
    
    public GoogleChannelConfig getGoogleChannelConfig(GetGoogleChannelConfigRequest request)

Get a GoogleChannelConfig. The name of the GoogleChannelConfig in the response is ALWAYS coded with projectID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGoogleChannelConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetGoogleChannelConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleChannelConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMessageBus(GetMessageBusRequest request)
    
    
    public MessageBus getMessageBus(GetMessageBusRequest request)

Get a single MessageBus.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetMessageBusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageBus](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.MessageBus)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getPipeline(GetPipelineRequest request)
    
    
    public Pipeline getPipeline(GetPipelineRequest request)

Get a single Pipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetPipelineRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Pipeline)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getProvider(GetProviderRequest request)
    
    
    public Provider getProvider(GetProviderRequest request)

Get a single Provider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Provider](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Provider)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTrigger(GetTriggerRequest request)
    
    
    public Trigger getTrigger(GetTriggerRequest request)

Get a single trigger.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GetTriggerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.Trigger)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listChannelConnections(ListChannelConnectionsRequest request)
    
    
    public ListChannelConnectionsResponse listChannelConnections(ListChannelConnectionsRequest request)

List channel connections.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChannelConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelConnectionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListChannelConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelConnectionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listChannels(ListChannelsRequest request)
    
    
    public ListChannelsResponse listChannels(ListChannelsRequest request)

List channels.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListChannelsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listEnrollments(ListEnrollmentsRequest request)
    
    
    public ListEnrollmentsResponse listEnrollments(ListEnrollmentsRequest request)

List Enrollments.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListEnrollmentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListEnrollmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListEnrollmentsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGoogleApiSources(ListGoogleApiSourcesRequest request)
    
    
    public ListGoogleApiSourcesResponse listGoogleApiSources(ListGoogleApiSourcesRequest request)

List GoogleApiSources.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGoogleApiSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListGoogleApiSourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGoogleApiSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListGoogleApiSourcesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMessageBusEnrollments(ListMessageBusEnrollmentsRequest request)
    
    
    public ListMessageBusEnrollmentsResponse listMessageBusEnrollments(ListMessageBusEnrollmentsRequest request)

List message bus enrollments.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusEnrollmentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMessageBuses(ListMessageBusesRequest request)
    
    
    public ListMessageBusesResponse listMessageBuses(ListMessageBusesRequest request)

List message buses.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMessageBusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMessageBusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListMessageBusesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listPipelines(ListPipelinesRequest request)
    
    
    public ListPipelinesResponse listPipelines(ListPipelinesRequest request)

List pipelines.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListPipelinesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPipelinesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListPipelinesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listProviders(ListProvidersRequest request)
    
    
    public ListProvidersResponse listProviders(ListProvidersRequest request)

List providers.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListProvidersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListProvidersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTriggers(ListTriggersRequest request)
    
    
    public ListTriggersResponse listTriggers(ListTriggersRequest request)

List triggers.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListTriggersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTriggersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.ListTriggersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateChannel(UpdateChannelRequest request)
    
    
    public Operation updateChannel(UpdateChannelRequest request)

Update a single channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateEnrollment(UpdateEnrollmentRequest request)
    
    
    public Operation updateEnrollment(UpdateEnrollmentRequest request)

Update a single Enrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateEnrollmentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGoogleApiSource(UpdateGoogleApiSourceRequest request)
    
    
    public Operation updateGoogleApiSource(UpdateGoogleApiSourceRequest request)

Update a single GoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGoogleApiSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateGoogleApiSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGoogleChannelConfig(UpdateGoogleChannelConfigRequest request)
    
    
    public GoogleChannelConfig updateGoogleChannelConfig(UpdateGoogleChannelConfigRequest request)

Update a single GoogleChannelConfig

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGoogleChannelConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateGoogleChannelConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GoogleChannelConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.GoogleChannelConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateMessageBus(UpdateMessageBusRequest request)
    
    
    public Operation updateMessageBus(UpdateMessageBusRequest request)

Update a single message bus.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMessageBusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateMessageBusRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updatePipeline(UpdatePipelineRequest request)
    
    
    public Operation updatePipeline(UpdatePipelineRequest request)

Update a single pipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdatePipelineRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTrigger(UpdateTriggerRequest request)
    
    
    public Operation updateTrigger(UpdateTriggerRequest request)

Update a single trigger.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-eventarc/latest/com.google.cloud.eventarc.v1.UpdateTriggerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
