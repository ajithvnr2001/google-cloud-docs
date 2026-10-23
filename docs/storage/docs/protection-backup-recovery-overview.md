---
url: https://docs.cloud.google.com/storage/docs/protection-backup-recovery-overview/
title: Data protection, backup, and recovery options \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:34.519132+00:00
---

# Data protection, backup, and recovery options  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/protection-backup-recovery-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Data protection, backup, and recovery options Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage offers a variety of options to help you protect your data from accidental or malicious deletion and recover your data in the event of a disaster. These options can be useful for legal or regulatory compliance, as well as for protecting data that is critical to your business.

Feature | Summary | Use case  
---|---|---  
[Object holds](https://docs.cloud.google.com/storage/docs/object-holds) | Prevent individual objects from being deleted or overwritten by placing metadata flags on the objects you want to retain. | Data protection  
[Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) | Recovers deleted objects and retains them for a specified period of time before they're permanently deleted. | Data protection  
[Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) | Preserves deleted objects as versioned, noncurrent objects that remain accessible in your bucket until explicitly removed. | Data protection  
[Bucket lock](https://docs.cloud.google.com/storage/docs/bucket-lock) | 

  * Retains all objects in a bucket for a specified minimum duration by defining data retention requirements on a per-bucket basis.
  * Locks the bucket's retention policy to prevent it from being reduced or removed.

| Data protection  
[Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) | 

  * Retains objects for a specified minimum duration by defining data retention requirements on a per-object basis.
  * Locks the object's retention policy to prevent it from being reduced or removed.

| Data protection  
[Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr) | Store data simultaneously in two geographically separate regions. | Data redundancy  
[Turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) | Replicates data to both regions within a dual-region with an RPO of 15 minutes. | Data redundancy  
[Cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication) | Asynchronously replicates data from a source bucket to a destination bucket in a different location. | Data redundancy  
[Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) | A managed backup and disaster recovery (DR) service that provides secure storage and centralized backup management at scale for VMs and other workloads running in Google Cloud. With Backup and DR Service, you can:

  * Back up Persistent Disk snapshots of your Compute Engine VMs to Cloud Storage buckets.
  * Get comprehensive monitoring, auditing, and reporting for compliance.
  * Defend against ransomware and other risks through insights into security threat events.

| Data backup, disaster recovery  
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) | Migrates or replicates data to, from, or between object and file storage systems, such as Cloud Storage, Amazon S3, and on-premises. | Data backup, data migration  
[Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview) | Lets you transfer large amounts of data from on-premises to Cloud Storage by using a physical appliance. | Data backup, data migration  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
