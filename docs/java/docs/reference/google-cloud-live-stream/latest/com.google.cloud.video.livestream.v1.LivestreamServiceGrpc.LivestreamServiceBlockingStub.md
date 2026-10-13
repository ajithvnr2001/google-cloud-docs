---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceBlockingStub
title: Class LivestreamServiceGrpc.LivestreamServiceBlockingStub (0.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:00.295391+00:00
---

# Class LivestreamServiceGrpc.LivestreamServiceBlockingStub (0.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LivestreamServiceGrpc.LivestreamServiceBlockingStub (0.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.101.0 (latest)  0.97.0  0.96.0  0.95.0  0.93.0  0.90.0  0.89.0  0.87.0  0.85.0  0.84.0  0.82.0  0.80.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.72.0  0.70.0  0.69.0  0.66.0  0.65.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.8  0.3.0 
    
    
    public static final class LivestreamServiceGrpc.LivestreamServiceBlockingStub extends AbstractBlockingStub<LivestreamServiceGrpc.LivestreamServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service LivestreamService.

Using Live Stream API, you can generate live streams in the various renditions and streaming formats. The streaming format include HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send a source stream in the various ways, including Real-Time Messaging Protocol (RTMP) and Secure Reliable Transport (SRT).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > LivestreamServiceGrpc.LivestreamServiceBlockingStub

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
    
    
    protected LivestreamServiceGrpc.LivestreamServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceGrpc.LivestreamServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAsset(CreateAssetRequest request)
    
    
    public Operation createAsset(CreateAssetRequest request)

Creates a Asset with the provided unique ID in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createChannel(CreateChannelRequest request)
    
    
    public Operation createChannel(CreateChannelRequest request)

Creates a channel with the provided unique ID in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createClip(CreateClipRequest request)
    
    
    public Operation createClip(CreateClipRequest request)

Creates a clip with the provided clip ID in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createDvrSession(CreateDvrSessionRequest request)
    
    
    public Operation createDvrSession(CreateDvrSessionRequest request)

Creates a DVR session with the provided unique ID in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateDvrSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createEvent(CreateEventRequest request)
    
    
    public Event createEvent(CreateEventRequest request)

Creates an event with the provided unique ID in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)` |   
  
### createInput(CreateInputRequest request)
    
    
    public Operation createInput(CreateInputRequest request)

Creates an input with the provided unique ID in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateInputRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteAsset(DeleteAssetRequest request)
    
    
    public Operation deleteAsset(DeleteAssetRequest request)

Deletes the specified asset if it is not used.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteAssetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteChannel(DeleteChannelRequest request)
    
    
    public Operation deleteChannel(DeleteChannelRequest request)

Deletes the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteClip(DeleteClipRequest request)
    
    
    public Operation deleteClip(DeleteClipRequest request)

Deletes the specified clip job resource. This method only deletes the clip job and does not delete the VOD clip stored in Cloud Storage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteClipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteDvrSession(DeleteDvrSessionRequest request)
    
    
    public Operation deleteDvrSession(DeleteDvrSessionRequest request)

Deletes the specified DVR session.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteDvrSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteEvent(DeleteEventRequest request)
    
    
    public Empty deleteEvent(DeleteEventRequest request)

Deletes the specified event.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteEventRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteInput(DeleteInputRequest request)
    
    
    public Operation deleteInput(DeleteInputRequest request)

Deletes the specified input.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getAsset(GetAssetRequest request)
    
    
    public Asset getAsset(GetAssetRequest request)

Returns the specified asset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetAssetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset)` |   
  
### getChannel(GetChannelRequest request)
    
    
    public Channel getChannel(GetChannelRequest request)

Returns the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel)` |   
  
### getClip(GetClipRequest request)
    
    
    public Clip getClip(GetClipRequest request)

Returns the specified clip.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetClipRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Clip](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Clip)` |   
  
### getDvrSession(GetDvrSessionRequest request)
    
    
    public DvrSession getDvrSession(GetDvrSessionRequest request)

Returns the specified DVR session.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetDvrSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DvrSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DvrSession)` |   
  
### getEvent(GetEventRequest request)
    
    
    public Event getEvent(GetEventRequest request)

Returns the specified event.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetEventRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)` |   
  
### getInput(GetInputRequest request)
    
    
    public Input getInput(GetInputRequest request)

Returns the specified input.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetInputRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Input)` |   
  
### getPool(GetPoolRequest request)
    
    
    public Pool getPool(GetPoolRequest request)

Returns the specified pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetPoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool)` |   
  
### listAssets(ListAssetsRequest request)
    
    
    public ListAssetsResponse listAssets(ListAssetsRequest request)

Returns a list of all assets in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsResponse)` |   
  
### listChannels(ListChannelsRequest request)
    
    
    public ListChannelsResponse listChannels(ListChannelsRequest request)

Returns a list of all channels in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsResponse)` |   
  
### listClips(ListClipsRequest request)
    
    
    public ListClipsResponse listClips(ListClipsRequest request)

Returns a list of all clips in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListClipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsResponse)` |   
  
### listDvrSessions(ListDvrSessionsRequest request)
    
    
    public ListDvrSessionsResponse listDvrSessions(ListDvrSessionsRequest request)

Returns a list of all DVR sessions in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDvrSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDvrSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsResponse)` |   
  
### listEvents(ListEventsRequest request)
    
    
    public ListEventsResponse listEvents(ListEventsRequest request)

Returns a list of all events in the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsResponse)` |   
  
### listInputs(ListInputsRequest request)
    
    
    public ListInputsResponse listInputs(ListInputsRequest request)

Returns a list of all inputs in the specified region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListInputsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsResponse)` |   
  
### previewInput(PreviewInputRequest request)
    
    
    public PreviewInputResponse previewInput(PreviewInputRequest request)

Preview the streaming content of the specified input.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PreviewInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreviewInputResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputResponse)` |   
  
### startChannel(StartChannelRequest request)
    
    
    public Operation startChannel(StartChannelRequest request)

Starts the specified channel. Part of the video pipeline will be created only when the StartChannel request is received by the server.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### startDistribution(StartDistributionRequest request)
    
    
    public Operation startDistribution(StartDistributionRequest request)

Starts distribution which delivers outputs to the destination indicated by the Distribution configuration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartDistributionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### stopChannel(StopChannelRequest request)
    
    
    public Operation stopChannel(StopChannelRequest request)

Stops the specified channel. Part of the video pipeline will be released when the StopChannel request is received by the server.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### stopDistribution(StopDistributionRequest request)
    
    
    public Operation stopDistribution(StopDistributionRequest request)

Stops the specified distribution.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopDistributionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateChannel(UpdateChannelRequest request)
    
    
    public Operation updateChannel(UpdateChannelRequest request)

Updates the specified channel.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateChannelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateDvrSession(UpdateDvrSessionRequest request)
    
    
    public Operation updateDvrSession(UpdateDvrSessionRequest request)

Updates the specified DVR session.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateDvrSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateInput(UpdateInputRequest request)
    
    
    public Operation updateInput(UpdateInputRequest request)

Updates the specified input.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateInputRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updatePool(UpdatePoolRequest request)
    
    
    public Operation updatePool(UpdatePoolRequest request)

Updates the specified pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
