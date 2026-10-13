---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.AdminClientImpl
title: Class AdminClientImpl (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:36.705454+00:00
---

# Class AdminClientImpl (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.AdminClientImpl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdminClientImpl (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public class AdminClientImpl extends ApiResourceAggregation implements AdminClient

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ApiResourceAggregation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation) > AdminClientImpl

## Implements

[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient)

## Inherited Members

[ApiResourceAggregation.awaitTermination(long,TimeUnit)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_awaitTermination_long_java_util_concurrent_TimeUnit_)

[ApiResourceAggregation.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_close__)

[ApiResourceAggregation.isShutdown()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_isShutdown__)

[ApiResourceAggregation.isTerminated()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_isTerminated__)

[ApiResourceAggregation.shutdown()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_shutdown__)

[ApiResourceAggregation.shutdownNow()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiResourceAggregation#com_google_cloud_pubsublite_internal_ApiResourceAggregation_shutdownNow__)

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

## Constructors 

### AdminClientImpl(CloudRegion region, AdminServiceClient serviceClient)
    
    
    public AdminClientImpl(CloudRegion region, AdminServiceClient serviceClient)

**Parameters**  
---  
**Name** | **Description**  
`region` | `[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion)`  
  
`serviceClient` | `[AdminServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.v1.AdminServiceClient)`  
  
  
## Methods 

### createReservation(Reservation reservation)
    
    
    public ApiFuture<Reservation> createReservation(Reservation reservation)

Create the provided reservation if it does not yet exist.

**Parameter**  
---  
**Name** | **Description**  
`reservation` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` |   
  
### createSubscription(Subscription subscription, BacklogLocation startingOffset)
    
    
    public ApiFuture<Subscription> createSubscription(Subscription subscription, BacklogLocation startingOffset)

Create the provided subscription at the given starting offset if it does not yet exist.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
  
`startingOffset` | `[BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` |   
  
### createSubscription(Subscription subscription, SeekTarget target)
    
    
    public ApiFuture<Subscription> createSubscription(Subscription subscription, SeekTarget target)

Create the provided subscription at the given target location within the message backlog, if it does not yet exist.

A seek is initiated if the target location is a publish or event time. If the seek fails, the created subscription is not deleted.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
  
`target` | `[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` |   
  
### createTopic(Topic topic)
    
    
    public ApiFuture<Topic> createTopic(Topic topic)

Create the provided topic if it does not yet exist.

**Parameter**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` |   
  
### deleteReservation(ReservationPath path)
    
    
    public ApiFuture<Void> deleteReservation(ReservationPath path)

Delete the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### deleteSubscription(SubscriptionPath path)
    
    
    public ApiFuture<Void> deleteSubscription(SubscriptionPath path)

Delete the subscription with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### deleteTopic(TopicPath path)
    
    
    public ApiFuture<Void> deleteTopic(TopicPath path)

Delete the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### getReservation(ReservationPath path)
    
    
    public ApiFuture<Reservation> getReservation(ReservationPath path)

Get the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` |   
  
### getSubscription(SubscriptionPath path)
    
    
    public ApiFuture<Subscription> getSubscription(SubscriptionPath path)

Get the subscription with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` |   
  
### getTopic(TopicPath path)
    
    
    public ApiFuture<Topic> getTopic(TopicPath path)

Get the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` |   
  
### getTopicPartitionCount(TopicPath path)
    
    
    public ApiFuture<Long> getTopicPartitionCount(TopicPath path)

Get the partitioning info for the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` |   
  
### listReservationTopics(ReservationPath path)
    
    
    public ApiFuture<List<TopicPath>> listReservationTopics(ReservationPath path)

Get the list of topics for the reservation with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[ReservationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)>>` |   
  
### listReservations(LocationPath path)
    
    
    public ApiFuture<List<Reservation>> listReservations(LocationPath path)

List all reservations for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>>` |   
  
### listSubscriptions(LocationPath path)
    
    
    public ApiFuture<List<Subscription>> listSubscriptions(LocationPath path)

List all subscriptions for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>>` |   
  
### listTopicSubscriptions(TopicPath path)
    
    
    public ApiFuture<List<SubscriptionPath>> listTopicSubscriptions(TopicPath path)

Get the list of subscriptions for the topic with id `id` if it exists.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)>>` |   
  
### listTopics(LocationPath path)
    
    
    public ApiFuture<List<Topic>> listTopics(LocationPath path)

List all topics for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>>` |   
  
### region()
    
    
    public CloudRegion region()

The Google Cloud region this client operates on.

**Returns**  
---  
**Type** | **Description**  
`[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion)` |   
  
### seekSubscription(SubscriptionPath path, SeekTarget target)
    
    
    public OperationFuture<SeekSubscriptionResponse,OperationMetadata> seekSubscription(SubscriptionPath path, SeekTarget target)

Initiate an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog.

See <https://cloud.google.com/pubsub/lite/docs/seek> for more information.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
  
`target` | `[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SeekSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SeekSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.OperationMetadata)>` |   
  
### updateReservation(Reservation reservation, FieldMask mask)
    
    
    public ApiFuture<Reservation> updateReservation(Reservation reservation, FieldMask mask)

Update the reservation with path `reservation.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`reservation` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)`  
  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Reservation)>` |   
  
### updateSubscription(Subscription subscription, FieldMask mask)
    
    
    public ApiFuture<Subscription> updateSubscription(Subscription subscription, FieldMask mask)

Update the subscription with path `subscription.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`subscription` | `[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)`  
  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription)>` |   
  
### updateTopic(Topic topic, FieldMask mask)
    
    
    public ApiFuture<Topic> updateTopic(Topic topic, FieldMask mask)

Update the topic with path `topic.getPath()` if it exists.

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)`  
  
`mask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Topic)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
