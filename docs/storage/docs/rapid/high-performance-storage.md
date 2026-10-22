---
url: https://docs.cloud.google.com/storage/docs/rapid/high-performance-storage/
title: Optimizing storage for AI/ML and data analytics by using Cloud Storage Rapid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:20.949857+00:00
---

# Optimizing storage for AI/ML and data analytics by using Cloud Storage Rapid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/high-performance-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Optimizing storage for AI/ML and data analytics by using Cloud Storage Rapid Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage offers a variety of options to help you optimize your data storage for use cases that require high performance, such as artificial intelligence (AI), machine learning (ML), and data-intensive analytics. This page introduces you to these options and guides you through selecting an option that's appropriate for the needs of your workloads.

## The Cloud Storage Rapid product family

Cloud Storage Rapid is a family of high-performance products in Cloud Storage that are designed to clear data bottlenecks for your AI/ML and data analytics workloads. As AI/ML models grow in complexity and datasets reach petabyte scales, storage performance often becomes the primary bottleneck for expensive GPU and TPU clusters. Cloud Storage Rapid leverages zonal architectures to bring your data closer to your compute resources, helping your accelerators stay saturated, reduce training times, and lower the total cost of ownership (TCO) for your most demanding workloads.

Cloud Storage Rapid includes Rapid Bucket and Rapid Cache.

### Store data in the Rapid storage class by using Rapid Bucket

[Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) is a high-performance, zonal object storage solution that lets you store data in the [Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid) by defining a [zone](https://docs.cloud.google.com/storage/docs/locations#location-z) as a bucket's location. Rapid Bucket lets you colocate your data in the same physical zone as your AI accelerators and helps you achieve the lowest latency and highest throughput among other Cloud Storage product offerings. Rapid Bucket delivers sub-millisecond latency, up to 15 TB/s of aggregate throughput, and supports up to 20 million queries per second (QPS).

Rapid Bucket supports stateful, streaming object appends, allowing applications to write data to existing objects in real-time. This capability lets you avoid expensive object rewrites and enables immediate data visibility, allowing consumer applications to read data as it's being written.

**Best used for** : training, checkpointing, and serving AI models that require ultra low latency and high deterministic performance

**Use this option if** : you want dedicated high performance for both reads and writes

To learn how to create zonal buckets with Rapid Bucket, see [Create zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).

### Create zonal caches with Rapid Cache

[Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) is a fully managed, SSD-backed zonal read cache that works with your existing regional, dual-region, or multi-region buckets without requiring API changes. A cache gives you temporary storage capacity and bandwidth that [automatically scale up or down](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#size-bandwidth-autoscaling) according to the needs of your workloads. Data is automatically ingested into the cache from your bucket when the data is read by a VM that resides in the same zone as the cache.

Rapid Cache provides 2.5 TB/s of aggregate throughput and reduces latency for faster reads by colocating your data in the same zones as your VMs. In addition to serving data faster, data served from a cache can incur lower data transfer fees, data retrieval fees, and operational fees than data that's served directly from a bucket. For more information, see [Benefits](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#benefits) for Rapid Cache.

**Best used for** : training, checkpointing restores, and serving AI models that require high read bandwidth from an existing Cloud Storage bucket

**Use this option if** : you have existing data storage in a Cloud Storage bucket that you want to accelerate

To learn how to use Rapid Cache, see [Create and manage caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
