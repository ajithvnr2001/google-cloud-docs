---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.AdminServiceGrpc.AdminServiceStub
title: Class AdminServiceGrpc.AdminServiceStub (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:28.939840+00:00
---

# Class AdminServiceGrpc.AdminServiceStub (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.AdminServiceGrpc.AdminServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdminServiceGrpc.AdminServiceStub (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public static final class AdminServiceGrpc.AdminServiceStub extends AbstractAsyncStub<AdminServiceGrpc.AdminServiceStub>

A stub to allow clients to do asynchronous rpc calls to service AdminService.

The service that a client application uses to manage topics and subscriptions, such creating, listing, and deleting topics and subscriptions.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > AdminServiceGrpc.AdminServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected AdminServiceGrpc.AdminServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminServiceGrpc.AdminServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.AdminServiceGrpc.AdminServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createReservation(CreateReservationRequest request, StreamObserver<Reservation> responseObserver)
    
    
    public void createReservation(CreateReservationRequest request, StreamObserver<Reservation> responseObserver)

Creates a new reservation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.CreateReservationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>`  
  
  
### createSubscription(CreateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public void createSubscription(CreateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Creates a new subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.CreateSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>`  
  
  
### createTopic(CreateTopicRequest request, StreamObserver<Topic> responseObserver)
    
    
    public void createTopic(CreateTopicRequest request, StreamObserver<Topic> responseObserver)

Creates a new topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.CreateTopicRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>`  
  
  
### deleteReservation(DeleteReservationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteReservation(DeleteReservationRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified reservation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.DeleteReservationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.DeleteSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteTopic(DeleteTopicRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteTopic(DeleteTopicRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.DeleteTopicRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getReservation(GetReservationRequest request, StreamObserver<Reservation> responseObserver)
    
    
    public void getReservation(GetReservationRequest request, StreamObserver<Reservation> responseObserver)

Returns the reservation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.GetReservationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>`  
  
  
### getSubscription(GetSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public void getSubscription(GetSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Returns the subscription configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.GetSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>`  
  
  
### getTopic(GetTopicRequest request, StreamObserver<Topic> responseObserver)
    
    
    public void getTopic(GetTopicRequest request, StreamObserver<Topic> responseObserver)

Returns the topic configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.GetTopicRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>`  
  
  
### getTopicPartitions(GetTopicPartitionsRequest request, StreamObserver<TopicPartitions> responseObserver)
    
    
    public void getTopicPartitions(GetTopicPartitionsRequest request, StreamObserver<TopicPartitions> responseObserver)

Returns the partition information for the requested topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.GetTopicPartitionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TopicPartitions](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicPartitions)>`  
  
  
### listReservationTopics(ListReservationTopicsRequest request, StreamObserver<ListReservationTopicsResponse> responseObserver)
    
    
    public void listReservationTopics(ListReservationTopicsRequest request, StreamObserver<ListReservationTopicsResponse> responseObserver)

Lists the topics attached to the specified reservation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReservationTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListReservationTopicsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReservationTopicsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListReservationTopicsResponse)>`  
  
  
### listReservations(ListReservationsRequest request, StreamObserver<ListReservationsResponse> responseObserver)
    
    
    public void listReservations(ListReservationsRequest request, StreamObserver<ListReservationsResponse> responseObserver)

Returns the list of reservations for the given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListReservationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReservationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListReservationsResponse)>`  
  
  
### listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)
    
    
    public void listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)

Returns the list of subscriptions for the given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListSubscriptionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListSubscriptionsResponse)>`  
  
  
### listTopicSubscriptions(ListTopicSubscriptionsRequest request, StreamObserver<ListTopicSubscriptionsResponse> responseObserver)
    
    
    public void listTopicSubscriptions(ListTopicSubscriptionsRequest request, StreamObserver<ListTopicSubscriptionsResponse> responseObserver)

Lists the subscriptions attached to the specified topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListTopicSubscriptionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTopicSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListTopicSubscriptionsResponse)>`  
  
  
### listTopics(ListTopicsRequest request, StreamObserver<ListTopicsResponse> responseObserver)
    
    
    public void listTopics(ListTopicsRequest request, StreamObserver<ListTopicsResponse> responseObserver)

Returns the list of topics for the given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTopicsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListTopicsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTopicsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ListTopicsResponse)>`  
  
  
### seekSubscription(SeekSubscriptionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void seekSubscription(SeekSubscriptionRequest request, StreamObserver<Operation> responseObserver)

Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog. Seek translates these targets to cursors for each partition and orchestrates subscribers to start consuming messages from these seek cursors. If an operation is returned, the seek has been registered and subscribers will eventually receive messages from the seek cursors (i.e. eventual consistency), as long as they are using a minimum supported client library version and not a system that tracks cursors independently of Pub/Sub Lite (e.g. Apache Beam, Dataflow, Spark). The seek operation will fail for unsupported clients. If clients would like to know when subscribers react to the seek (or not), they can poll the operation. The seek operation will succeed and complete once subscribers are ready to receive messages from the seek cursors for all partitions of the topic. This means that the seek operation will not complete until all subscribers come online. If the previous seek operation has not yet completed, it will be aborted and the new invocation of seek will supersede it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SeekSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SeekSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateReservation(UpdateReservationRequest request, StreamObserver<Reservation> responseObserver)
    
    
    public void updateReservation(UpdateReservationRequest request, StreamObserver<Reservation> responseObserver)

Updates properties of the specified reservation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.UpdateReservationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>`  
  
  
### updateSubscription(UpdateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public void updateSubscription(UpdateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Updates properties of the specified subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.UpdateSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>`  
  
  
### updateTopic(UpdateTopicRequest request, StreamObserver<Topic> responseObserver)
    
    
    public void updateTopic(UpdateTopicRequest request, StreamObserver<Topic> responseObserver)

Updates properties of the specified topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.UpdateTopicRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
