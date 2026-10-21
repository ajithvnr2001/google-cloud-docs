---
url: https://docs.cloud.google.com/pubsub/lite/quotas/
title: Pub/Sub Lite quotas and limits \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:25.167761+00:00
---

# Pub/Sub Lite quotas and limits  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Resources ](https://docs.cloud.google.com/pubsub/lite/docs/resources)



Send feedback 

#  Pub/Sub Lite quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about quotas and resource limits for Pub/Sub Lite. Unless mentioned otherwise, Pub/Sub Lite topics refer to both zonal and regional Lite topics.

**Key Point:** You can request increases to quotas, but limits cannot be adjusted.

## Overview of quotas and limits

Google Cloud uses quotas to restrict how much of a particular shared Google Cloud resource that you can use. Each quota represents a specific countable resource, such as API calls to a particular service, the number of bytes sent to a particular service, or the storage used by your project.

Many services also have system limits. These are fixed constraints, such as maximum message sizes or the number of Pub/Sub Lite resources you can create in a project, which cannot be increased or decreased.

## Pub/Sub Lite quotas

Quotas apply to the following properties of a Pub/Sub Lite service:

  * Throughput for a zone in case of a zonal Lite topic without reservations and throughput reservation capacity units in a region
  * Storage for a region
  * Rate of administrative Pub/Sub Lite requests for a project



### Throughput quotas

Regional Lite topic require throughput reservations. Zonal Lite topics can use reservations or allocate throughput capacity directly to a topic. Zonal Lite topics without reservations consume publish and subscribe throughput quota of their respective zones. Lite topic with reservations only consume throughput quota through their reservations.

The following default quotas apply to each project and [location](https://docs.cloud.google.com/pubsub/lite/docs/locations):

Resource quota | Location type | Value  
---|---|---  
Reservation throughput | region | 128 capacity units  
Publishing throughput for zonal Lite topics without reservations | zone | 64 MiBps  
Subscribing throughput for zonal Lite topics without reservations | zone | 128 MiBps  
  
### Storage quotas

The storage of both zonal and regional Lite topics in a project counts towards the same regional quota. A regional Lite topic stores data in two zones in a region, whereas a zonal Lite topic stores data only in one zone in a region.

For example, if you create a zonal Lite topic with one partition containing 30 GiB of storage space, you use 30 GiB of your storage quota. Alternatively, if you create a regional Lite topic with one partition containing 30 GiB of storage space, you use 60 GiB (30 x 2) of your storage quota.

Lite topics store messages in partitions, and each message uses 256 bytes to 10 MiB of storage space. If the message is larger than 256 bytes, then the size of the message is the sum of the following:

  * The number of bytes in the encoded message body string
  * The number of bytes in the key and value of each attribute
  * The number of bytes in the ordering key
  * 12 bytes for the event timestamp



For more information about the message format, see the [message resource in the Pub/Sub Lite API reference](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PubSubMessage).

The following default quotas apply to each project and [location](https://docs.cloud.google.com/pubsub/lite/docs/locations):

Resource quota | Location type | Value  
---|---|---  
Storage | region | 20 TiB  
  
### Rate quotas

The following quotas apply to Pub/Sub Lite requests in each region:

Quota | Value | Description  
---|---|---  
Administrative read requests per min | 600 | Getting and listing Lite topics and Lite subscriptions  
Administrative write requests per min | 600 | Creating, updating, and deleting Lite topics and Lite subscriptions, or manually changing the offset of a committed cursor.  
Message stats computation requests per min | 600 | Computing backlog statistics  
Head cursor computation requests per min | 600 | Computing the current head cursor  
  
These quotas apply to each Google Cloud console project and are shared across all applications using that project.

### Quota increases

If you want to increase any of your quotas for Pub/Sub Lite, you can use the Google Cloud console to request a quota increase. For details, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Pub/Sub Lite limits

As mentioned before, you cannot increase resources that have limits.

### Subscription limits

Pub/Sub Lite enforces a limit of 1,000 Lite subscriptions for a Lite topic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
