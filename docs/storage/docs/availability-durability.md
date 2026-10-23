---
url: https://docs.cloud.google.com/storage/docs/availability-durability/
title: Data availability and durability \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:42.934002+00:00
---

# Data availability and durability  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/availability-durability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Data availability and durability Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the concepts of availability and durability within Cloud Storage:

  * Availability: The ability to access data immediately upon request.

  * Durability: Long-term protection to ensure data remains intact and uncorrupted.




The following sections cover how Cloud Storage redundantly stores data, the default replication behavior for dual-regions and multi-regions, and advanced features like turbo replication and cross-bucket replication.

## Key concepts

  * The monthly availability of data stored in Cloud Storage depends on the storage class of the data and the location type of the bucket. For more information, see [available storage classes](https://docs.cloud.google.com/storage/docs/storage-classes#classes).

  * Cloud Storage is designed for at least 99.999999999% (11 9's) annual durability, regardless of storage class and location type.

    * To achieve this, Cloud Storage uses erasure coding and stores data pieces redundantly across multiple devices.

    * Writes to Cloud Storage are only confirmed as successful after data has been redundantly stored.

    * Checksums are stored and regularly revalidated to proactively verify the integrity of all data at rest, as well as to detect corruption of data in transit. If required, corrections are automatically made using redundant data.




## How a bucket's location type affects availability and durability

  * [Regional](https://docs.cloud.google.com/storage/docs/locations#location-r) buckets store data redundantly in at least two availability [zones](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) in the region you select. They are designed to tolerate the loss of any one availability zone in the region.

    * Object writes to a bucket are only confirmed as successful after data has been redundantly stored across at least two different availability zones.

    * In the unlikely event of an availability zone outage, such as one caused by a natural disaster, regional buckets remain available, with no need to change storage paths.

  * [Dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) and [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) buckets store data redundantly in at least two separate geographic places.

    * For dual-regions, you select the specific regions in which your objects are stored.

    * For multi-regions, the specific data centers used for storing your data are determined by Cloud Storage as needed, but are located within the geographic boundary of the multi-region and are separated by at least 100 miles. This provides redundancy across regions at a lower storage cost than dual-regions.

    * Object writes to a bucket are only confirmed as successful after data has been redundantly stored in one initial region, across at least two different availability zones (same as writes to a regional bucket). Data is then asynchronously replicated using default replication to provide the expected redundancy across regions.

      * If one of the regions in which an object is stored becomes unavailable after the object is successfully uploaded but prior to it being replicated for georedundancy, Cloud Storage's [strong consistency](https://docs.cloud.google.com/storage/docs/consistency) ensures that stale versions of the object won't be served and that subsequent overwrites aren't reverted when the region becomes available again.

      * As a premium offering, you can optionally enable turbo replication on dual-region buckets to achieve faster, more predictable replication times across regions for newly written data.

    * In the unlikely event of a region-wide outage, such as one caused by a natural disaster, dual-region and multi-region buckets remain available, with no need to change storage paths.

    * To achieve redundancy between a region pairing not available as a dual-region, consider creating a separate bucket for each region and using Storage Transfer Service [event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) or cross-bucket replication to keep the buckets in sync.

  * Locally redundant data, such as data in a zonal bucket, provides 99.999999999% (11 9's) annual durability against hardware failures like host, rack, or drive failures. However, because data is not redundant across availability zones, it may become unavailable or permanently lost in the event of an availability zone failure. As a result, locally redundant storage is most suitable for data that can be replaced or reconstructed.




## Redundancy across regions

While traditional storage models often rely on an active-passive approach with "primary" and "secondary" geographic locations, Cloud Storage dual-regions and multi-regions provide an active-active architecture based on a single bucket with redundancy across regions. This simplifies the [disaster recovery](https://docs.cloud.google.com/learn/what-is-disaster-recovery) process by eliminating the need for users to replicate data from one bucket to another or manually failover to a secondary bucket in the case of primary region downtime.

Cloud Storage always understands the current state of a bucket and transparently serves objects from an available region as required. As a result, dual-region and multi-region buckets are designed to have a [recovery time objective (RTO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) of zero, and temporary regional failures are normally invisible to users; in the case of a regional outage, dual-region and multi-region buckets automatically continue serving all data that has been replicated across regions.

However, redundancy across regions occurs asynchronously, and any data that does not finish replicating across regions prior to a region becoming unavailable is inaccessible until the downed region comes back online. Data could potentially be lost in the very unlikely case of physical destruction of the region.

Default replication in Cloud Storage is designed to provide redundancy across regions for 99.9% of newly written objects within a target of one hour and 100% of newly written objects within a target of 12 hours. Newly written objects include uploads, rewrites, copies, and compositions.

Cloud Storage also offers a [cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication) capability that can be used to replicate data between independent buckets to meet additional data replication needs that aren't met by dual-region or multi-region locations.

### Turbo replication

Turbo replication provides faster redundancy across regions for data in your dual-region buckets, which [reduces the risk of data loss exposure](https://docs.cloud.google.com/architecture/disaster-recovery#step_1_gather_existing_requirements) and [helps support uninterrupted service](https://docs.cloud.google.com/architecture/disaster-recovery#cloud-storage) following a regional outage. When enabled, turbo replication is designed to replicate 100% of newly written objects to the two regions that constitute a dual-region within the [recovery point objective of 15 minutes](https://docs.cloud.google.com/storage/sla), regardless of object size.

Note that even for default replication, most objects finish replication within minutes.

While redundancy across regions and turbo replication help support [business continuity and disaster recovery (BCDR)](https://docs.cloud.google.com/learn/what-is-disaster-recovery) efforts, administrators should plan and implement a full BCDR architecture that's appropriate for their workload.

For more information, see the [Step-by-step guide to designing disaster recovery for applications in Google Cloud](https://docs.cloud.google.com/architecture/disaster-recovery#step-by-step_guide_to_designing_disaster_recovery_for_applications_in).

#### Limitations

  * Turbo replication is only available for buckets in [dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr).

  * Turbo replication cannot be managed through the XML API, including creating a new bucket with turbo replication enabled.

  * When turbo replication is enabled on a bucket, it can take up to 10 seconds before it begins to apply to newly written objects.

  * Object writes that began prior to enabling turbo replication on a bucket replicate across regions at the default replication rate.

    * [Object composition](https://docs.cloud.google.com/storage/docs/composing-objects) that uses any source objects written using default replication in the last 12 hours creates a composite object that also uses default replication.



## Cross-bucket replication

In some cases, you might want to maintain a copy of your data in a second bucket. Cross-bucket replication copies new and updated objects asynchronously from a source bucket to a destination bucket.

Cross-bucket replication differs from default replication and turbo replication in that your data exists in two independent buckets, each with their own configurations such as storage location, encryption, access, and storage class. It is especially suitable for:

  * **Data sovereignty** : Maintain data across geographically distant regions.
  * **Maintaining separate development and production versions** : Create distinct buckets and namespaces, so that development doesn't affect your production workload.
  * **Sharing data** : Replicate data to a bucket owned by a vendor or partner.
  * **Aggregating data** : Combine data from different buckets into a single bucket to run analytics workloads.
  * **Managing cost, security, and compliance** : Maintain your data under different ownerships, storage classes, and retention periods.



Cross-bucket replication uses [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) to replicate objects and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) to get alerted of changes to the source and destination buckets. You can enable cross-bucket replication on new buckets you create and on existing buckets.

For buckets where the object change rate is under 3,000 per second and objects are under one GiB, cross-bucket replication commonly takes minutes to tens of minutes, but no specific upper bound is supported. Also, buckets experiencing higher change rates or having larger objects can expect to see higher replication delays.

For instructions on using cross-bucket replication, see [Use cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication).

**Note:** When using cross-bucket replication, you might incur charges from data transfer, data storage, data processing, data retrieval, and operations from Cloud Storage, Storage Transfer Service, and Pub/Sub. For details on pricing, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing), [Storage Transfer Service pricing](https://docs.cloud.google.com/storage-transfer/pricing), and [Pub/Sub pricing](https://docs.cloud.google.com/pubsub/pricing).

### Limitations

  * Custom names are not supported for cross-bucket replication jobs. Create requests that contain a value for the `name` field return an error.

  * Cross-bucket replication is not supported for hierarchical namespace buckets or zonal buckets.

  * Object deletions in the source bucket are not replicated to the destination bucket.

  * Object lifecycle configurations aren't replicated.

  * When objects are replicated, timestamp metadata (for example, `timeCreated` and `timeUpdated`) is not preserved. See [Transfers between Cloud Storage buckets](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#between-cloud-buckets) for details on metadata preservation.

  * Because cross-bucket replication can be used to replicate data between buckets located in any Google Cloud location, cross-bucket replication performance varies based on the locations selected. Consequently, cross-bucket replication does not offer a Recovery Point Objective (RPO).

  * Objects that are already in the bucket when a replication job is created are not automatically replicated. Only new and updated objects are replicated. To replicate existing objects, create a one-time Storage Transfer Service transfer job from your existing bucket to the new bucket. See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) for instructions.




## Performance monitoring

Cloud Storage monitors the oldest unreplicated objects in dual-region and multi-region buckets using default replication or turbo replication. If an object remains unreplicated for longer than its RPO (Recovery Point Objective) time, it's considered to be out of RPO. Each minute in which one or more objects are out of RPO is counted as a "bad" minute.

For example, if one object yielded 20 bad minutes from 9:00-9:20 AM, and another object yielded 10 bad minutes from 9:15-9:25 AM, then there are two objects for the month that are out of RPO. The total number of bad minutes for the month is 25 minutes, because from 9:00 AM to 9:25 AM there was at least one object that was missing its RPO.

  * For buckets using turbo replication, the RPO for objects is 15 minutes.

  * For buckets using default replication, the RPO for objects is 12 hours.

    * For buckets that use default replication, objects are typically replicated in one hour or less.
  * Cross-bucket replication doesn't provide an RPO.




Within the Google Cloud console, the **Percent of minutes out of RPO** graph lets you monitor the percentage of bad minutes during the past 30 days for your bucket when using default replication or turbo replication within dual-region or multi-region buckets. This service level indicator can be used to monitor your bucket's Monthly Replication Time Conformance. Similarly, the **Percent of objects out of target** tracks object replications that did not occur within the RPO. This service level indicator can be used to monitor the bucket's Monthly Replication Volume Conformance. For more information, see [Cloud Storage monitoring](https://docs.cloud.google.com/storage/docs/monitoring#per-bucket) and [Cloud Storage SLA](https://docs.cloud.google.com/storage/sla).

## What's next

  * [Enable turbo replication](https://docs.cloud.google.com/storage/docs/managing-turbo-replication) on an existing dual-region bucket.
  * Learn more about [turbo replication pricing](https://docs.cloud.google.com/storage/pricing#inter-region-replication).
  * [Move data to a different bucket](https://docs.cloud.google.com/storage/docs/moving-buckets) in a new location.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
