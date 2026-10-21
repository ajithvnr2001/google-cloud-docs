---
url: https://docs.cloud.google.com/storage/docs/request-rate/
title: Request rate and access distribution guidelines \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:21.650496+00:00
---

# Request rate and access distribution guidelines  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/request-rate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Request rate and access distribution guidelines Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage is a highly scalable service that uses auto-scaling technology to achieve very high request rates. This page lays out guidelines for optimizing the scaling and performance that Cloud Storage provides.

## Auto-Scaling

Cloud Storage is a multi-tenant service, meaning that users share the same set of underlying resources. In order to make the best use of these shared resources, buckets have an initial IO capacity of:

  * Approximately 1000 object write requests per second, which includes uploading, updating, and deleting objects. Note that Cloud Storage also has a [smaller limit](https://docs.cloud.google.com/storage/quotas) for repeated writes to the _same_ object name.
  * Approximately 5000 object read requests per second, which includes listing objects, reading object data, and reading object metadata.



These initial read and write rates average to 2.5PB written and 13PB read in a month for 1MB objects. As the request rate for a given bucket grows, Cloud Storage autoscales and automatically increases the IO capacity for that bucket by distributing the request load across multiple servers.

### Load redistribution time

As a bucket approaches its IO capacity limit, Cloud Storage typically takes on the order of minutes to detect and accordingly redistribute the load across more servers. Consequently, if the request rate on your bucket increases faster than Cloud Storage can perform this redistribution, you may run into temporary limits, specifically higher latency and error rates. Ramping up the request rate gradually for your buckets, as described below, avoids such latency and errors.

### Object key indexing

Cloud Storage supports [consistent object listing](https://docs.cloud.google.com/storage/docs/consistency), which enables users to run data processing workflows easily against Cloud Storage. In order to provide consistent object listing, Cloud Storage maintains an index of object keys for each bucket. This index is stored in lexicographical order and is updated whenever objects are written to or deleted from a bucket. Adding and deleting objects whose keys all exist in a small range of the index naturally increases the chances of [contention](https://en.wikipedia.org/wiki/Resource_contention#:%7E:text=In%20computer%20science%2C%20resource%20contention,can%20be%20described%20as%20oversubscribed).

Cloud Storage detects such contention, also known as hotspotting, and automatically redistributes the load on the affected index range across multiple servers. Similar to scaling a bucket's IO capacity, when accessing a new range of the index, such as when writing objects under a new prefix, you should ramp up the request rate gradually, as described below. Not doing so may result in temporarily higher latency and error rates.

## Best practices

The following sections provide best practices on how to ramp up the request rate, choose object keys, and distribute requests in order to avoid temporary limits on your bucket. Note that in addition to these per-bucket considerations, there are also [combined bandwidth limits](https://docs.cloud.google.com/storage/quotas#bandwidth) that apply to buckets located in the same location and project.

### Ramp up request rate gradually

To ensure that Cloud Storage auto-scaling always provides the best performance, you should ramp up your request rate gradually for any bucket that hasn't had a high request rate in several days or that has a new range of object keys. If your request rate is less than 1000 write requests per second or 5000 read requests per second, then no ramp-up is needed. If your request rate is expected to go over these thresholds, you should start with a request rate below or near the thresholds and then gradually increase the rate no faster than doubling the rate over a period of 20 minutes.

**Note:** We recommend that you run performance and scalability tests to ensure that this guideline works for your specific use case, prior to ramping up your traffic in production.

If you run into any issues such as increased latency or error rates, pause your ramp-up or reduce the request rate temporarily in order to give Cloud Storage more time to scale your bucket. You should [retry your requests](https://docs.cloud.google.com/storage/docs/retry-strategy) with exponential backoff when:

  * Receiving errors with `408` and `429` response codes.
  * Receiving errors with `5xx` response codes.



Buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled offer up to 8 times higher initial Queries per second (QPS) limits for reading and writing objects compared to buckets without hierarchical namespace enabled. The higher initial QPS makes it easier to scale data-intensive workloads and provides enhanced throughput. For more information about enabling hierarchical namespace on your bucket, see [Create a bucket with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket#create-hns-bucket).

### Use a naming convention that distributes load evenly across key ranges

Auto-scaling of an index range can be slowed when using sequential names, such as object keys based on a sequence of numbers or timestamp. This occurs because requests are constantly shifting to a new index range, making redistributing the load harder and less effective.

In order to maintain a high request rate, avoid using sequential names. Using completely random object names gives you the best load distribution. If you want to use sequential numbers or timestamps as part of your object names, introduce randomness to the object names by adding a hash value before the sequence number or timestamp.

For example, if the original object names you want to use are:
    
    
    my-bucket/2016-05-10-12-00-00/file1
    my-bucket/2016-05-10-12-00-00/file2
    my-bucket/2016-05-10-12-00-01/file3
    ...
    

You can compute the MD5 hash of the original object name and add the first 6 characters of the hash as a prefix to the object name. The new object names become:
    
    
    my-bucket/2fa764-2016-05-10-12-00-00/file1
    my-bucket/5ca42c-2016-05-10-12-00-00/file2
    my-bucket/6e9b84-2016-05-10-12-00-01/file3
    ...
    

A longer randomized prefix provides more effective auto-scaling when ramping to very high read and write rates. For example, a 1-character prefix using a random hex value provides effective auto-scaling from the initial 5000/1000 reads/writes per second up to roughly 80000/16000 reads/writes per second, because the prefix has 16 potential values. If your use case does not need higher rates than this, a 1-character randomized prefix is just as effective at ramping up request rates as a 2-character or longer randomized prefix.

#### Randomness after a common prefix is effective under the prefix

Note that the random string doesn’t necessarily need to be at the beginning of the object name. Adding a random string after a common prefix still allows auto-scaling to work, but the effect is limited to that prefix, with no consideration of the rest of the bucket.

For example:
    
    
    my-bucket/images/animals/4ce4c6af-6d27-4fa3-8a91-5701a8552705/1.jpg
    my-bucket/images/animals/9a495e72-1d85-4637-a243-cbf3e4a90ae7/2.jpg
    ...
    my-bucket/images/landscape/585356ac-ce89-47a8-bdd2-78a86b58fee6/1.jpg
    my-bucket/images/landscape/2550ae5b-395e-4243-a29b-bbf5aece60ef/2.jpg
    ...
    my-bucket/images/clouds/1.jpg
    my-bucket/images/clouds/2.jpg
    ...
    

The above naming allows for efficient auto-scaling of objects in `images/animals` and `images/landscape,` but not `images/clouds`.

#### Randomness after sequential prefixes is not as effective

As mentioned above, using a random string after a common prefix only helps with auto-scaling under that prefix. Once the requests shift to a new prefix, you may no longer benefit from the previous auto-scaling effects. This is especially a problem when the prefixes follow a sequential pattern.

For example, if you write files under a new timestamp-based prefix every hour:
    
    
    my-bucket/2016-05-10-00/cf9a7b95-0d2e-4466-9596-840ff388ddbd
    my-bucket/2016-05-10-00/f1e16a88-16b8-4c66-ba66-a225c87be80c
    my-bucket/2016-05-10-00/646d8272-4a88-4dc2-b2d4-d537c778df41
    ...
    my-bucket/2016-05-10-01/bdcba6de-ac25-4c27-8550-0d08f249e69d
    my-bucket/2016-05-10-01/a32c867c-09a9-4d65-9668-ddd4ebe4138b
    my-bucket/2016-05-10-01/d619485c-5243-4a4e-8ef3-0f7e1d26ce1d
    ...
    

Although auto-scaling helps to increase the write rate under a prefix over time, the write rate resets at the beginning of each hour. This results in a sub-optimal write rate and periodic increases in latency and error rate. If you need to write to different prefixes over time, to avoid this problem, make sure the new prefixes are evenly distributed across the entire key range.

### Reorder bulk operations to distribute load evenly across key ranges

Sometimes you'll want to perform a bulk upload or deletion of data in Cloud Storage. In both cases, you may not have control over the object names. Nevertheless, you can control the order in which the objects are uploaded or deleted to achieve the highest write or deletion rate possible.

To do so, you should distribute the uploads or deletes across multiple prefixes. For example, if you have many folders and many files under each folder to upload, a good strategy is to upload from multiple folders in parallel and randomly choose which folders and files are uploaded. Doing so allows the system to distribute the load more evenly across the entire key range, which allows you to achieve a high request rate after the initial ramp-up.

## What's next

  * Review [Cloud Storage quotas and limits](https://docs.cloud.google.com/storage/quotas).
  * Learn about the [recommended retry strategy](https://docs.cloud.google.com/storage/docs/retry-strategy) for requests to Cloud Storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
