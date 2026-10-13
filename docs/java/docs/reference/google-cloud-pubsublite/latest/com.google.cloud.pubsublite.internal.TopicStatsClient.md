---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClient
title: Interface TopicStatsClient (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:23.072536+00:00
---

# Interface TopicStatsClient (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TopicStatsClient (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public interface TopicStatsClient extends ApiBackgroundResource

## Implements

[ApiBackgroundResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiBackgroundResource)

## Static Methods 

### create(TopicStatsClientSettings settings)
    
    
    public static TopicStatsClient create(TopicStatsClientSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TopicStatsClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClientSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TopicStatsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.TopicStatsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html)` |   
  
## Methods 

### computeCursorForEventTime(TopicPath path, Partition partition, Timestamp eventTime)
    
    
    public abstract ApiFuture<Optional<Cursor>> computeCursorForEventTime(TopicPath path, Partition partition, Timestamp eventTime)

Compute the cursor of the first message with event time greater than or equal to the specified event time, for a topic partition. If messages are missing an event time, the publish time is used as a fallback. As event times are user supplied, subsequent messages may have event times less than the specified event time and should be filtered by the client, if necessary.

If such a message cannot be found, the returned Optional will be empty.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The topic to compute cursor for  
`partition` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)`  
The partition to compute cursor for  
`eventTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
The target event time  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Optional](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)<[Cursor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Cursor)>>` | A future that will have either an error [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), an empty Optional or a non-null [Cursor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Cursor).  
  
### computeCursorForPublishTime(TopicPath path, Partition partition, Timestamp publishTime)
    
    
    public abstract ApiFuture<Optional<Cursor>> computeCursorForPublishTime(TopicPath path, Partition partition, Timestamp publishTime)

Compute the cursor of the first message with publish time greater than or equal to the specified publish time, for a topic partition. All messages thereafter are guaranteed to have publish times greater than or equal to the specified publish time.

If such a message cannot be found, the returned Optional will be empty.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The topic to compute cursor for  
`partition` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)`  
The partition to compute cursor for  
`publishTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
The target publish time  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Optional](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)<[Cursor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Cursor)>>` | A future that will have either an error [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), an empty Optional or a non-null [Cursor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Cursor).  
  
### computeHeadCursor(TopicPath path, Partition partition)
    
    
    public abstract ApiFuture<Cursor> computeHeadCursor(TopicPath path, Partition partition)

Compute the head cursor for the partition. The head cursor's offset is guaranteed to be before or equal to all messages which have not yet been acknowledged to be published, and greater than the offset of any message whose publish has already been acknowledged. It is 0 if there have never been messages on the partition.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The topic to compute head cursor on  
`partition` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)`  
The partition to compute head cursor for  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Cursor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Cursor)>` | A future that will have either an error [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the head cursor on success.  
  
### computeMessageStats(TopicPath path, Partition partition, Offset start, Offset end)
    
    
    public abstract ApiFuture<ComputeMessageStatsResponse> computeMessageStats(TopicPath path, Partition partition, Offset start, Offset end)

Compute statistics about the messages between two cursors in a topic partition.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
The topic to compute statistics on  
`partition` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)`  
The partition to compute statistics for  
`start` | `[Offset](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Offset)`  
The start cursor  
`end` | `[Offset](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Offset)`  
The end cursor  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ComputeMessageStatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeMessageStatsResponse)>` | A future that will have either an error [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) or the ComputeMessageStatistics on success.  
  
### region()
    
    
    public abstract CloudRegion region()

The Google Cloud region this client operates on.

**Returns**  
---  
**Type** | **Description**  
`[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
