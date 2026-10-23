---
url: https://docs.cloud.google.com/storage/docs/storage-classes/
title: Storage classes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:54.217154+00:00
---

# Storage classes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage classes Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the concept of _storage class_ and the differences between storage classes.

  * To learn how to change the storage class of an object, see [Changing object storage classes](https://docs.cloud.google.com/storage/docs/changing-storage-classes).

  * To learn how to change a bucket's default storage class, see [Changing the default storage class](https://docs.cloud.google.com/storage/docs/changing-default-storage-class).




## Key concepts

  * A _storage class_ is a piece of [metadata](https://docs.cloud.google.com/storage/docs/metadata) that is used by every object.

  * The storage class set for an object affects the object's availability and [pricing model](https://docs.cloud.google.com/storage/pricing).

  * When you [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets), you can specify a _default storage class_ for the bucket. When you add objects to the bucket, they inherit this storage class unless explicitly set otherwise.

    * If you don't specify a default storage class when you create a bucket, that bucket's default storage class is set to Standard storage.

    * [Changing the default storage class of a bucket](https://docs.cloud.google.com/storage/docs/changing-default-storage-class) does not affect any of the objects that already exist in the bucket.

  * You can change the storage class of an existing object either by [rewriting the object](https://docs.cloud.google.com/storage/docs/changing-storage-classes) or by using [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).

  * You can enable the [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) feature on a bucket to let Cloud Storage manage storage class transitions for you automatically.




## Available storage classes

The following table summarizes the primary storage classes offered by Cloud Storage. See class descriptions for a complete discussion.

Storage Class | Name for APIs and CLIs | [Minimum storage duration](https://docs.cloud.google.com/storage/pricing#early-delete) | [Retrieval fees](https://docs.cloud.google.com/storage/pricing#retrieval-pricing) | Typical monthly availability1  
---|---|---|---|---  
Rapid storage2 | `RAPID` | None | None | 

  * >99.95% in zones

  
Standard storage | `STANDARD` | None | None | 

  * >99.99% in multi-regions and dual-regions
  * 99.99% in regions

  
Nearline storage | `NEARLINE` | 30 days | Yes | 

  * 99.95% in multi-regions and dual-regions
  * 99.9% in regions

  
Coldline storage | `COLDLINE` | 90 days | Yes | 

  * 99.95% in multi-regions and dual-regions
  * 99.9% in regions

  
Archive storage | `ARCHIVE` | 365 days | Yes | 

  * 99.95% in multi-regions and dual-regions
  * 99.9% in regions

  
  
1See the class descriptions for the _availability SLA_ for each storage class.

2The Rapid storage class is only available with [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).

## Class descriptions

The following features apply to all storage classes:

  * Unlimited storage with unlimited access. Rapid storage is an exception; to see storage size limit for zonal buckets, see [Quotas for buckets](https://docs.cloud.google.com/storage/quotas).
  * No minimum object size.
  * Worldwide accessibility and worldwide [storage locations](https://docs.cloud.google.com/storage/docs/locations).
  * Low latency with no offline data retrieval.
  * [High durability](https://docs.cloud.google.com/storage/docs/availability-durability#key-concepts) (99.999999999% annual durability).
  * [Redundancy across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy) when data is stored in a multi-region or dual-region.
  * A uniform experience with Cloud Storage features, security, tools, and APIs.



### Rapid storage

Rapid storage is a high-performance storage class that's optimized for I/O-intensive workloads. When you use Rapid storage as a bucket's storage class, you can store your data in [zonal locations](https://docs.cloud.google.com/storage/docs/locations#location-z). Storing your objects in the same zones as your compute resources enables significantly lower latency and higher throughput compared to other storage classes. This approach makes Rapid storage ideal for your most data-intensive use cases, such as Artificial Intelligence (AI), Machine Learning (ML), and data analytics.

Rapid storage is only compatible with zonal buckets through [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).

The availability of Rapid storage data is as follows:

Location type | Availability SLA1 | Typical monthly availability  
---|---|---  
zone | 99.9% | >99.95%  
  
1The availability SLA is the monthly uptime percentage backed by the [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla). If Google fails to meet that uptime, customers are eligible to receive a credit as described in the Cloud Storage SLA.

### Standard storage

Standard storage is best for data that is frequently accessed ("hot" data), as well as data that is stored for only brief periods of time.

When used in a region, Standard storage is appropriate for storing data in the same location as [Google Kubernetes Engine clusters](https://docs.cloud.google.com/kubernetes-engine/docs/clusters) or [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) that use the data. Co-locating your resources maximizes the performance for data-intensive computations and can reduce network charges.

When used in a dual-region, you still get optimized performance when accessing Google Cloud products that are located in one of the associated regions, but you also get the improved availability that comes from storing data in geographically separate locations.

When used in a multi-region, Standard storage is appropriate for storing data that is accessed around the world, such as serving website content, streaming videos, executing interactive workloads, or serving data supporting mobile and gaming applications.

#### Availability

The availability of Standard storage data is:

Location type | Availability SLA1 | Typical monthly availability  
---|---|---  
multi-region | 99.95% | >99.99%  
dual-region | 99.95% | >99.99%  
region | 99.9% | 99.99%  
  
1The availability SLA is the monthly uptime percentage backed by the [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla). If Google fails to meet that uptime, customers are eligible to receive a credit as described in the Cloud Storage SLA.

### Nearline storage

Nearline storage is a low-cost, highly durable storage service for storing infrequently accessed data. Nearline storage is a better choice than Standard storage in scenarios where slightly lower availability, a 30-day minimum storage duration, and costs for data access are acceptable trade-offs for lowered [at-rest storage costs](https://docs.cloud.google.com/storage/pricing#storage-pricing).

Nearline storage is ideal for data you plan to read or modify on average once per month or less. For example, if you want to continuously add files to Cloud Storage and plan to access those files once a month for analysis, Nearline storage is a great choice.

Nearline storage is also appropriate for data backup, long-tail multimedia content, and data archiving. Note, however, that for data accessed less frequently than once a quarter, Coldline storage or Archive storage are more cost-effective, as they offer lower storage costs.

#### Availability

The availability of Nearline storage data is:

Location type | Availability SLA1 | Typical monthly availability  
---|---|---  
multi-region | 99.9% | 99.95%  
dual-region | 99.9% | 99.95%  
region | 99.0% | 99.9%  
  
1The availability SLA is the monthly uptime percentage backed by the [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla). If Google fails to meet that uptime, customers are eligible to receive a credit as described in the Cloud Storage SLA.

### Coldline storage

Coldline storage is a very-low-cost, highly durable storage service for storing infrequently accessed data. Coldline storage is a better choice than Standard storage or Nearline storage in scenarios where slightly lower availability, a 90-day minimum storage duration, and higher costs for data access are acceptable trade-offs for lowered [at-rest storage costs](https://docs.cloud.google.com/storage/pricing#storage-pricing).

Coldline storage is ideal for data you plan to read or modify at most once a quarter. Note, however, that for data being kept entirely for backup or archiving purposes, Archive storage is more cost-effective, as it offers the lowest storage costs.

#### Availability

The availability of Coldline storage data is:

Location type | Availability SLA1 | Typical monthly availability  
---|---|---  
multi-region | 99.9% | 99.95%  
dual-region | 99.9% | 99.95%  
region | 99.0% | 99.9%  
  
1The availability SLA is the monthly uptime percentage backed by the [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla). If Google fails to meet that uptime, customers are eligible to receive a credit as described in the Cloud Storage SLA.

### Archive storage

Archive storage is the lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery. Unlike the "coldest" storage services offered by other Cloud providers, your data is available within milliseconds, not hours or days.

Like Nearline storage and Coldline storage, Archive storage has a slightly lower availability than Standard storage. Archive storage also has higher costs for data access and operations, as well as a 365-day minimum storage duration. Archive storage is the best choice for data that you plan to access less than once a year. For example:

  * Cold data storage - Archived data, such as data stored for legal or regulatory reasons, can be stored at low cost as Archive storage, yet still be available if you need it.

  * Disaster recovery - In the event of a disaster recovery event, recovery time is key. Cloud Storage provides low latency access to data stored as Archive storage.




#### Availability

The availability of Archive storage data is:

Location Type | Availability SLA1 | Typical monthly availability  
---|---|---  
multi-region | 99.9% | 99.95%  
dual-region | 99.9% | 99.95%  
region | 99.0% | 99.9%  
  
1The availability SLA is the monthly uptime percentage backed by the [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla). If Google fails to meet that uptime, customers are eligible to receive a credit as described in the Cloud Storage SLA.

### Additional classes

Cloud Storage supports several additional legacy storage classes; however, these legacy classes cannot be set using the Google Cloud console. Unless you already are using one of these legacy classes, you should use Standard storage instead.

  * **Multi-Regional storage** : Equivalent to Standard storage, except Multi-Regional storage can only be used for objects stored in [multi-regions](https://docs.cloud.google.com/storage/docs/locations#location-mr) or [dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr).

  * **Regional storage** : Equivalent to Standard storage, except Regional storage can only be used for objects stored in [regions](https://docs.cloud.google.com/storage/docs/locations#location-r).

  * **Durable Reduced Availability (DRA) storage** : Similar to Standard storage except:

    * DRA has higher pricing for operations.
    * DRA has lower performance, particularly in terms of availability (DRA has a 99% availability SLA).

You can move your data from DRA to other storage classes by [performing a storage transfer](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-console).


**Note:** When [enabling Autoclass on your bucket](https://docs.cloud.google.com/storage/docs/autoclass#autoclass_for_existing_buckets), legacy storage classes are considered to be different from Standard storage. For example, objects in your bucket other than soft-deleted objects transition to Standard storage when Autoclass is enabled, and this includes objects stored in legacy classes.

## Pricing

Storage classes affect the pricing model of objects and the operations you perform. For information about how storage classes affect pricing, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

## What's next

  * [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * [Compare storage costs for different storage classes](https://docs.cloud.google.com/storage/pricing#storage-pricing).
  * [Upload an object to Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).
  * [Change the storage class of an individual object](https://docs.cloud.google.com/storage/docs/changing-storage-classes).
  * [Learn about the Object Lifecycle Management feature](https://docs.cloud.google.com/storage/docs/lifecycle).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
