---
url: https://docs.cloud.google.com/storage/docs/best-practices-media-workload/
title: Best practices for media workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:38.651139+00:00
---

# Best practices for media workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/best-practices-media-workload/

  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



#  Best practices for media workloads Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage lets you store and serve audio and video assets while optimizing streaming performance, minimizing playback latency, and managing costs. To support media workflows, you can integrate Cloud Storage with Google Cloud products like [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview), [Live Stream API](https://docs.cloud.google.com/livestream/docs/overview), [Transcoder API](https://docs.cloud.google.com/transcoder/docs/concepts/overview), and [Video Stitcher API](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview). This document describes the best practices when using Cloud Storage for media workloads.

## Overview of media workloads

Google Cloud offers solutions to optimize the following types of media workloads:

  * **Media production** : Includes workloads such as post production of movies including video editing that are compute heavy and often use GPUs for high performance computing. Often, media-related data residing in Cloud Storage is processed by applications running in Compute Engine or Google Kubernetes Engine, and the output of this process is written back to Cloud Storage. These workloads require scaling aggregate read and write throughput from Cloud Storage to a compute cluster with a lower GPU idle time. They also require low read and write latencies as it's crucial in reducing tail latency.
  * **Media asset management** : Includes organizing your media assets for efficient storage, retrieval, and usage.
  * **Content serving and distribution** : Includes streaming media to users, including video on demand (VoD) and livestreaming services. During VoD, when users' request content that isn't cached on the content delivery network (CDN), the content is fetched from the Cloud Storage buckets. For livestreaming requests, the content is written to the Storage bucket and read from the CDN simultaneously.



## Best practices for media workloads

For best practices that apply to media workloads, see the following sections.

### Data transfer

Use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) to upload more than 1 TiB of raw media files from an on-premises source, such as video camera or on-premises storage to Cloud Storage. Storage Transfer Service enables seamless data movement across object and file storage systems. For smaller transfers, choose the service to [transfer data to and from Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/transfer-options) or between file systems based on your transfer scenario.

### Bucket location

For workloads that require compute resources such as media production, you should create buckets in the same region or dual-regions as the compute resources. This method helps to optimize the performance by lowering read and write latencies for your processing workloads, [cost](https://docs.cloud.google.com/storage/pricing#storage-pricing), and [bandwidth](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring). For more guidance about choosing the bucket location, see [Bucket location considerations](https://docs.cloud.google.com/storage/docs/locations#considerations).

### Storage class

Depending on the type of media workload, the storage class you should select differs. The recommended storage class types for different media workloads are as follows:

  * For managing media assets, such as archive videos, the default storage class of a bucket should be Archive storage. You can specify a different storage class for objects that have different availability or access needs.
  * For media production and content serving workloads, as data is read frequently from a Cloud Storage bucket, you should store the data in Standard storage.



For more guidance about choosing the storage class for your bucket, see [Storage class](https://docs.cloud.google.com/storage/docs/storage-classes).

### Data lifecycle management

For managing your media assets, you should manage object lifecycle for your buckets by defining a [lifecycle configuration](https://docs.cloud.google.com/storage/docs/lifecycle#configuration). With the [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) feature, you can manage the data lifecycle including setting a Time to Live (TTL) for objects, retaining noncurrent versions of objects, and downgrading storage classes of objects to help manage costs.

When data access patterns are predictable, you can [set the lifecycle configuration for a bucket](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set). For unknown or unpredictable access patterns for your data, you can [set the Autoclass feature for your bucket](https://docs.cloud.google.com/storage/docs/using-autoclass#set-autoclass). With Autoclass, Cloud Storage automatically moves data that is not frequently accessed to colder storage classes.

## Best practices for content serving and distribution workloads

For both VoD and livestreaming workloads, the goal is to avoid any playback errors, playback start delays, or buffering while playing a video on the end-users' video player. These workloads also require scaling of reads to account for a large number of concurrent viewers. In all cases, customer traffic reads should go through a CDN.

For best practices that apply to content serving and distribution workloads, see the following sections.

### Use the CDN effectively

Using a content delivery network (CDN) in front of the Cloud Storage bucket improves the end-user experience as the CDN caches content by reducing latency and increasing bandwidth efficiency. A CDN lets you reduce the total cost of ownership (TCO) by reducing bandwidth costs, optimizing resource utilization, and improving performance. Using [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) helps reduce the TCO for serving the content to end users as cache-fill cost for Media CDN is zero. You can use Media CDN to serve as the source of other third-party CDNs. With other CDNs, you still get some TCO reduction when serving content from this Media CDN cache instead of from the origin.

If you are using a third-party CDN, [CDN Interconnect](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect) enables selected providers to establish direct peering links with Google's edge network at various locations. Your network traffic egressing from Google Cloud through one of these links benefits from the direct connectivity to supported CDN providers and is billed automatically with reduced pricing. For a list of approved providers, see [Google-approved service providers](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect#cdn-interconnect-providers).

The following lists the options to configure when setting up a CDN:

  * Select the origin shield location
  * Request coalescing
  * Configure the retry behavior on CDN



#### Select the origin shield location

The origin shield location is a cache between the CDN and Cloud Storage. If your CDN lets you select the origin shield location, follow the CDN guidelines on whether it's recommended to choose the origin shield to be closer to the region of your Cloud Storage bucket or your end-user traffic concentration location. An origin shield is a protective measure that protects your origin server from overloading. CDNs with origin shielding help increase origin offload by adding an extra cache between the origin and CDN. For example, [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) provides a deeply tiered edge infrastructure that is designed to actively minimize cache fill wherever possible.

#### Enable request coalescing

Ensure that request collapsing is enabled for your CDN. Collapsing multiple requests into a single request reduces the Cloud Storage class B operation cost. CDNs have distributed caches deployed across the globe but provide a way to collapse multiple end-user requests into a single request to origin. For example, Media CDN actively collapses multiple user-driven cache fill requests for the same cache key into a single origin request per edge node, thereby reducing the number of requests made to the buckets.

#### Configure the retry behavior on CDN

Ensure that you configure retry for any server issues with HTTP 5xx response code–502, 503, 504 on your CDN. CDNs support origin retries, allowing retry of unsuccessful requests to the origin. Most CDNs let you specify the number of retries for the current origin. For information about retrying origin requests in Media CDN, see [Retry origin requests](https://docs.cloud.google.com/media-cdn/docs/origins#retry-origin-requests).

### Location options for content distribution

For workloads reading data from Cloud Storage that isn't cached on CDN, such as content serving and distribution of a VoD type content, consider the following factors when selecting a location for your bucket:

  * To optimize for cost, buckets created in a single region have the lowest [storage cost](https://docs.cloud.google.com/storage/pricing#storage-pricing).
  * To optimize for availability, consider the following: 
    * For most media workloads, using dual-region buckets is recommended because it replicates your objects in two regions for better availability.
    * For use cases that require content serving and analytics with geo-redundancy, use buckets in multi-regions for highest availability.
  * To optimize for latency and reduce network costs, consider the following: 
    * For VoD, choose regions closest to where most of your end users are or the region with the most traffic concentration.
    * During livestreaming, buckets receive write requests from transcoders and read requests from a CDN that cache and distribute the content to end users. For an enhanced streaming performance, choose regional buckets which are colocated with the compute resources used for transcoding.



### Optimize video segment length for livestreams

For livestreams, the lowest recommended segment size is two seconds because short video segments are more sensitive to long-tail write latencies. Long-tail write latencies refers to the slow or delayed write operations for content that is infrequently accessed or has a low volume of requests.

The physical distance between the bucket location and the end-users' playback location affects the transmission time. If your end users are far from the bucket location, we recommend having a longer video segment size.

In order to provide viewers the best experience, it's recommended to [use the retry strategy](https://docs.cloud.google.com/storage/docs/retry-strategy) and request hedging for writes on the transcoders to mitigate long tail latencies of more than two seconds for writes to Cloud Storage and to experiment with longer buffer times of approximately ten seconds.

### Ramp up QPS gradually

Cloud Storage buckets have an [initial IO capacity](https://docs.cloud.google.com/storage/docs/request-rate#auto-scaling) of 1,000 object writes per second and 5,000 object reads per second. For livestream workloads, the guideline is to scale your requests gradually by starting at 1,000 writes per second and 5,000 reads per second, and incrementally doubling the request rate every 20 minutes. This method lets Cloud Storage redistribute the load across multiple servers, and improves the availability and latency of your bucket by reducing the chances of playback issues.

For a livestream event with higher QPS, you should implement scaling on your bucket by either prewarming your bucket  or by enabling hierarchical namespace on your bucket. Before implementing scaling on your bucket, you should perform the following tasks:

  * Estimate your QPS to the origin
  * Monitor the QPS and troubleshoot any scaling errors



#### Estimate your QPS to the origin

Suppose for a livestream with one million viewers, the CDN will receive one million QPS. Assuming your CDN has a cache hit rate of 99.0%, the resulting traffic to Cloud Storage will be 1%. The QPS will be 1% of the total viewers (one million), which equals to 10,000 QPS. This value is more than the initial IO capacity.

#### Monitor the QPS and troubleshoot any scaling errors

You should monitor the QPS and troubleshoot any scaling errors. For more information, see [Overview of monitoring in Cloud Storage ](https://docs.cloud.google.com/storage/docs/monitoring). To monitor the read and write requests, observe the **Total read/list/get request count** chart and the **Total write request count** chart respectively in the [Google Cloud console](https://console.cloud.google.com/storage/monitoring). If you scale the QPS on buckets faster than the specified ramp-up guidelines mentioned in the preceding section, you might encounter the _429 Too many requests_ error. Learn how to resolve the [429 Too many requests](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes#429_Too_Many_Requests) error.

The following sections describe how to scale your bucket for higher QPS after you have estimated the QPS to the origin.

#### Implement QPS scaling on your bucket by prewarming your bucket

You can expedite the scaling process ahead of a livestreaming event by prewarming your bucket. Before the livestreaming event, generate synthetic traffic to your bucket that matches the expected max QPS you expect the [CDN's origin server](https://docs.cloud.google.com/media-cdn/docs/origins) will receive to the event plus additional 50% buffer factoring in the expected cache-hit rate of your CDN. For example, if you estimated the QPS to your origin to be 10,000, then your simulated traffic should target 15,000 requests per second to prepare your origin for the event.

For this simulated traffic, you can either use the previous event's live feed files such as segments and manifest or test files. Ensure that you have distinct files throughout the warmup process.

When generating this simulated traffic, follow a gradual scaling approach, starting at 5,000 requests per second and progressively increasing until you reach your target. Allocate sufficient time before your event to achieve the estimated load. For example, reaching 15,000 requests per second, doubling the load every 20 minutes from an initial 5,000 requests per second, will take approximately 30 minutes.

The origin server maintains the capacity until the traffic is consistent. The origin server's capacity gradually decreases to its baseline level over 24 hours. If your origin server experiences multi-hour gaps between the livestream events, we recommend that you simulate traffic before each event.

#### Use hierarchical namespace enabled buckets for high initial QPS

Cloud Storage buckets with [hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/hns-overview) provide up to eight times the initial QPS compared to the buckets without HNS. The higher initial QPS makes it easier to scale data-intensive workloads and provides enhanced throughput. For information about limitations in buckets with hierarchical namespace enabled, see [Limitations](https://docs.cloud.google.com/storage/docs/hns-overview#hns-limitations).

### Avoid sequential names for video segments for scaling QPS

With QPS scaling, requests are redistributed across multiple servers. However, you might encounter performance bottlenecks when all the objects use a non-randomized or sequential prefix. Using completely random names over sequential names gives you the best load distribution. However, if you want to use sequential numbers or timestamps as part of your object names, introduce randomness to the object names by adding a hash value before the sequence number or timestamp. For example, if the original object name you want to use is `my-bucket/2016-05-10-12-00-00/file1`, you can compute the MD5 hash of the original object name and add the first six characters of the hash as a prefix to the object name. The new object becomes `my-bucket/2fa764-2016-05-10-12-00-00/file1.` For more information, see [Use a naming convention that distributes load evenly across key ranges](https://docs.cloud.google.com/storage/docs/request-rate#naming-convention). If you can't avoid sequential naming for video segments, use buckets with [hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/hns-overview) to get higher QPS.

### Use different buckets for each livestream

For concurrent livestreams, using different buckets for each livestream will help you scale the read and write load effectively without reaching the [IO limits for the bucket](https://docs.cloud.google.com/storage/docs/request-rate#auto-scaling). Using different buckets for each livestream decreases large outlier latencies due to scaling delays.

## What's next

  * [Media and Entertainment solutions for Google Cloud](https://docs.cloud.google.com/solutions/media-entertainment)
  * [Codelab on Google Cloud with Media CDN, Live-streaming API and Cloud Storage](https://codelabs.developers.google.com/mediacdn-ls-codelab#0)
  * [Media CDN overview](https://docs.cloud.google.com/media-cdn/docs/overview)
  * [Overview of the Live Stream API](https://docs.cloud.google.com/livestream/docs/overview)
  * [Overview of the Transcoder API](https://docs.cloud.google.com/transcoder/docs/concepts/overview)
  * [Best practices for Cloud Storage](https://docs.cloud.google.com/storage/docs/best-practices)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
