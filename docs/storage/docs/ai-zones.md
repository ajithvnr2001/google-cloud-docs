---
url: https://docs.cloud.google.com/storage/docs/ai-zones/
title: AI zones \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:23.524351+00:00
---

# AI zones  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/ai-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  AI zones Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** When AI zone visibility is turned off, your Google Cloud project's access to AI zones is restricted. To view and access AI zones, [turn on AI zone visibility](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#turn_on_ai_zones).

This document provides an overview of AI zones for Cloud Storage. AI zones are specialized Google Cloud zones that are designed to offer computing capacity for artificial intelligence (AI) and machine learning (ML) workloads. They provide significant ML accelerator (GPU and TPU) capacity.

AI zones are optimized for AI and ML workloads like the following:

  * Large-scale training
  * Small-scale training, fine-tuning, bulk inference, and retraining
  * Real-time ML inference



For background information about AI zones, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) in the Compute Engine documentation.

Within a region, AI zones might be geographically located away from standard (non-AI) zones.

AI zones are compatible with other Cloud Storage and Google Cloud features.

## Storage architecture recommendations

We recommend that you use a tiered storage architecture to balance cost, durability, and performance:

  * **Cold storage layer** : use regional Cloud Storage buckets in standard zones for persistent, highly durable storage (the "source of truth") of your training datasets and model checkpoints.

  * **Performance layer** : use specialized zonal storage services to act as a high-speed cache or temporary scratch space. This approach eliminates inter-zonal latency and maximizes throughput during active jobs.




The following storage solutions are recommended for optimizing AI and ML system performance with AI zones:

Storage service or product | Description | Use cases  
---|---|---  
[Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) product of Cloud Storage |  A fully managed, SSD-backed zonal read cache that brings frequently read data from a bucket into the AI zone. Create a Rapid Cache instance in an AI zone for the regional source bucket that contains the training datasets or models that you want to serve. When your training job reads a file, the file is pulled into the fast, in-zone cache. Subsequent reads are served directly from the cache, bypassing the regional network. This is ideal for the repetitive data access patterns in model training and for low-latency model serving. |  Recommended for:

  * Read-heavy workloads
  * Low-latency model training and serving

  
[Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) product of Cloud Storage |  A high-performance capability that lets you locate buckets in zones and use the Rapid storage class. Optimized for I/O-intensive workloads, specifically designed for AI/ML applications that require colocation with the data they need to access. To optimize your data storage for workloads that require low latency and high throughput, [create a zonal bucket](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets) that uses Rapid storage and then mount the bucket as a directory on your virtual machine by using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview). You can then configure your application to store or access data in the zonal bucket through the bucket's mount point. For example, to store model checkpoints in your zonal bucket, configure your checkpointing directory to the mount point in your training code. For regional resilience, you can back up your checkpoints to regional, multi-regional, or dual-regional buckets. Use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) to move data from a zonal bucket to a bucket in a different location. Use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to expire and delete data after a set time period. |  Recommended for:

  * High-throughput read and write workloads
  * High-speed checkpointing
  * Low-latency model training and serving

  
  
## Best practices

Follow these best practices for storage when using AI zones:

  * Provision your performance layer in the same AI zone as your compute resources. Colocating compute and storage helps to ensure that GPUs and TPUs remain fully saturated, maximizing "goodput" (useful throughput).

  * For Rapid Cache, before you start the primary training epoch, perform a pre-read of your dataset to populate, or warm, the SSD-backed cache.




## Available AI zones

The following table shows the AI zones and their parent Google Cloud regions.

Geographic area | Parent region | AI zone  
---|---|---  
Europe | `europe-west4` | `europe-west4-ai1a`  
United States | `us-central1` | `us-central1-ai1a`  
United States | `us-south1` | `us-south1-ai1b`  
  
## Considerations

  * You can access Google Cloud products in a Google Cloud region from the region's AI zone. However, accessing services in a Google Cloud region from an AI zone can add network latency, because the location of the AI zone might be physically separate from the locations of the region's standard zones.

  * We recommend that you run non-ML workloads in standard zones, not AI zones, because AI zones don't offer all Google Cloud services locally.




## What's next

  * [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * Learn more about [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache).
  * Read about [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations).
  * Read the [Architecture Center design guidance for AI and ML workloads](https://docs.cloud.google.com/architecture/ai-ml/storage-for-ai-ml).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
