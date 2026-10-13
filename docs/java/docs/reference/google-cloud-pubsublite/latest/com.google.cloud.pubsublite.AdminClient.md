---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient
title: Interface AdminClient (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:09.883282+00:00
---

# Interface AdminClient (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AdminClient (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public interface AdminClient extends ApiBackgroundResource

A client for performing Pub/Sub Lite admin operations.

## Implements

[ApiBackgroundResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiBackgroundResource)

## Static Methods 

### create(AdminClientSettings settings)
    
    
    public static AdminClient create(AdminClientSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html)` |   
  
## Methods 

### createReservation(Reservation reservation)
    
    
    public abstract ApiFuture<Reservation> createReservation(Reservation reservation)

Create the provided reservation if it does not yet exist.

**Parameter**  
---  
**Name** | **Description**  
`reservation` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)`  
The reservation to create.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the reservation on success.  
  
### createSubscription(Subscription subscription)
    
    
    public default ApiFuture<Subscription> createSubscription(Subscription subscription)

Create the provided subscription if it does not yet exist.

By default, a new subscription will only receive messages published after the subscription was created.

**Parameter**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
The subscription to create.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the subscription on success.  
  
### createSubscription(Subscription subscription, BacklogLocation startingOffset)
    
    
    public abstract ApiFuture<Subscription> createSubscription(Subscription subscription, BacklogLocation startingOffset)

Create the provided subscription at the given starting offset if it does not yet exist.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
The subscription to create.  
`startingOffset` | `[BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation)`  
The offset at which the new subscription will start receiving messages.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the subscription on success.  
  
### createSubscription(Subscription subscription, SeekTarget target)
    
    
    public abstract ApiFuture<Subscription> createSubscription(Subscription subscription, SeekTarget target)

Create the provided subscription at the given target location within the message backlog, if it does not yet exist.

A seek is initiated if the target location is a publish or event time. If the seek fails, the created subscription is not deleted.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
The subscription to create.  
`target` | `[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)`  
The target location that the subscription should be initialized to.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the subscription on success.  
  
### createTopic(Topic topic)
    
    
    public abstract ApiFuture<Topic> createTopic(Topic topic)

Create the provided topic if it does not yet exist.

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)`  
The topic to create.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the topic on success.  
  
### deleteReservation(ReservationPath path)
    
    
    public abstract ApiFuture<Void> deleteReservation(ReservationPath path)

Delete the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
The path of the reservation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or void on success. Deleting nonexistent reservations will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
### deleteSubscription(SubscriptionPath path)
    
    
    public abstract ApiFuture<Void> deleteSubscription(SubscriptionPath path)

Delete the subscription with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
The path of the subscription to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or void on success. Deleting nonexistent subscriptions will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
### deleteTopic(TopicPath path)
    
    
    public abstract ApiFuture<Void> deleteTopic(TopicPath path)

Delete the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The path of the topic to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or void on success. Deleting nonexistent topics will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
### getReservation(ReservationPath path)
    
    
    public abstract ApiFuture<Reservation> getReservation(ReservationPath path)

Get the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
The path of the reservation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the reservation on success.  
  
### getSubscription(SubscriptionPath path)
    
    
    public abstract ApiFuture<Subscription> getSubscription(SubscriptionPath path)

Get the subscription with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
The path of the subscription to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the subscription on success.  
  
### getTopic(TopicPath path)
    
    
    public abstract ApiFuture<Topic> getTopic(TopicPath path)

Get the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The path of the topic to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the topic on success.  
  
### getTopicPartitionCount(TopicPath path)
    
    
    public abstract ApiFuture<Long> getTopicPartitionCount(TopicPath path)

Get the partitioning info for the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The path of the topic to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the number of topic partitions on success.  
  
### listReservationTopics(ReservationPath path)
    
    
    public abstract ApiFuture<List<TopicPath>> listReservationTopics(ReservationPath path)

Get the list of topics for the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
The path of the reservation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)>>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the list of topics on success.  
  
### listReservations(LocationPath path)
    
    
    public abstract ApiFuture<List<Reservation>> listReservations(LocationPath path)

List all reservations for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
The path of the project to list reservations for.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the list of reservation paths on success.  
  
### listSubscriptions(LocationPath path)
    
    
    public abstract ApiFuture<List<Subscription>> listSubscriptions(LocationPath path)

List all subscriptions for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
The path of the project to list subscriptions for.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the list of subscription paths on success.  
  
### listTopicSubscriptions(TopicPath path)
    
    
    public abstract ApiFuture<List<SubscriptionPath>> listTopicSubscriptions(TopicPath path)

Get the list of subscriptions for the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The path of the topic to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)>>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the list of subscriptions on success.  
  
### listTopics(LocationPath path)
    
    
    public abstract ApiFuture<List<Topic>> listTopics(LocationPath path)

List all topics for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
The path of the project to list topics for.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the list of topic paths on success.  
  
### region()
    
    
    public abstract CloudRegion region()

The Google Cloud region this client operates on.

**Returns**  
---  
**Type** | **Description**  
`[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion)` |   
  
### seekSubscription(SubscriptionPath path, SeekTarget target)
    
    
    public abstract OperationFuture<SeekSubscriptionResponse,OperationMetadata> seekSubscription(SubscriptionPath path, SeekTarget target)

Initiate an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog.

See <https://cloud.google.com/pubsub/lite/docs/seek> for more information.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
The path of the subscription to seek.  
`target` | `[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)`  
The location to seek to.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SeekSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SeekSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.OperationMetadata)>` | A [com.google.api.gax.longrunning.OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html) that returns an operation name if the seek was successfully initiated, or otherwise throw an [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html). com.google.api.gax.longrunning.OperationFuture#get() will return a response if the seek operation completes successfully, or otherwise throw an [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html).  
  
### updateReservation(Reservation reservation, FieldMask mask)
    
    
    public abstract ApiFuture<Reservation> updateReservation(Reservation reservation, FieldMask mask)

Update the reservation with path `reservation.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`reservation` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)`  
The reservation to update.  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the resulting reservation on success. Updating nonexistent reservations will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
### updateSubscription(Subscription subscription, FieldMask mask)
    
    
    public abstract ApiFuture<Subscription> updateSubscription(Subscription subscription, FieldMask mask)

Update the subscription with path `subscription.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
The subscription to update.  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the resulting subscription on success. Updating nonexistent subscriptions will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
### updateTopic(Topic topic, FieldMask mask)
    
    
    public abstract ApiFuture<Topic> updateTopic(Topic topic, FieldMask mask)

Update the topic with path `topic.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)`  
The topic to update.  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask indicating which fields should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` | A future that will have either an error [com.google.api.gax.rpc.ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the resulting topic on success. Updating nonexistent topics will cause the future to have an exception with status com.google.api.gax.rpc.StatusCode.Code#NOT_FOUND  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
