---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClient
title: Interface CursorClient (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:21.211959+00:00
---

# Interface CursorClient (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CursorClient (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public interface CursorClient extends ApiBackgroundResource

## Implements

[ApiBackgroundResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ApiBackgroundResource)

## Static Methods 

### create(CursorClientSettings settings)
    
    
    public static CursorClient create(CursorClientSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CursorClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClientSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CursorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.CursorClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html)` |   
  
## Methods 

### commitCursor(SubscriptionPath path, Partition partition, Offset offset)
    
    
    public abstract ApiFuture<Void> commitCursor(SubscriptionPath path, Partition partition, Offset offset)

Commit a single cursor.

**Parameters**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
The subscription to commit a cursor for.  
`partition` | `[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)`  
The partition to commit a cursor for.  
`offset` | `[Offset](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Offset)`  
The offset to commit.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A future for the operation's completion.  
  
### listPartitionCursors(SubscriptionPath path)
    
    
    public abstract ApiFuture<Map<Partition,Offset>> listPartitionCursors(SubscriptionPath path)

List the cursors for a given subscription.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
The subscription to list cursors for.  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition),[Offset](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Offset)>>` | A future holding the map of Partition to Offset of the cursors.  
  
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
