---
url: https://docs.cloud.google.com/docs/security/deletion/
title: Data deletion on Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:22.125010+00:00
---

# Data deletion on Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Data deletion on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in May 2024, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._

This document gives an overview of the secured process that occurs when you delete your customer data on Google Cloud. As defined in the [Google Cloud Terms of Service](https://cloud.google.com/terms), _customer data_ is data that is provided to Google by customers or end users through the services under the account.

This document describes how customer data is stored in Google Cloud, the deletion pipeline, and how we prevent any reconstruction of data that is stored in our platform.

For information about our data deletion commitments, see [Cloud Data Processing Addendum (Customers)](https://cloud.google.com/terms/data-processing-addendum).

## Data storage and replication

Google Cloud offers [storage services](https://cloud.google.com/products#section-21) and [databases services](https://cloud.google.com/products#section-8) such as [Bigtable](https://docs.cloud.google.com/bigtable) and [Spanner](https://docs.cloud.google.com/spanner). Most Google Cloud applications and services access Google's storage infrastructure indirectly using these cloud services.

Data replication is critical to achieving low latency, highly available, scalable, and durable solutions. Redundant copies of customer data can be stored locally and regionally and even globally, depending on your configuration and the demands of your projects. Actions taken on data in Google Cloud may be simultaneously replicated in multiple data centers, so that customer data is highly available. When performance-impacting changes occur in the hardware, software, or network environment, customer data is automatically shifted from one system or facility to another, subject to customers' configuration settings, so that customer projects continue performing at scale and without interruption.

At the physical storage level, customer data is stored at rest in two types of systems: active storage systems and backup storage systems. These two types of systems process data differently. Active storage systems are Google Cloud's production servers that run Google's application and storage layers. Active systems are mass arrays of disks and drives used to write new data as well as store and retrieve data in multiple replicated copies. Active storage systems are optimized to perform live read and write operations on customer data at speed and scale.

Google's backup storage systems store full and incremental copies of Google's active systems for a defined period of time to help Google recover data and systems in the event of a catastrophic outage or disaster. Unlike active systems, backup systems are designed to receive periodic snapshots of Google systems and backup copies are retired after a limited window of time as new backup copies are made.

Throughout the storage systems described above, customer data is encrypted when stored at rest. For more information, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

## Data deletion pipeline

After customer data is stored in Google Cloud, our systems are designed to store the data securely until the data deletion pipeline completes its stages. This section describes the deletion stages.

### Stage 1: Deletion request

The deletion of customer data begins when you initiate a deletion request. Generally, a deletion request is directed to a specific resource, a Google Cloud project, or your Google account. Deletion requests might be handled in different ways depending on the scope of your request:

  * **Resource Deletion:** Individual resources containing customer data, such as Cloud Storage buckets, can be deleted in a number of ways from the Google Cloud console or using API. For example, you can issue a remove bucket or [`gcloud storage rm`](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud#delete_an_object) command to delete a storage bucket through the command line or you can select a storage bucket and delete it from the Google Cloud console.
  * **Project Deletion:** As a Google Cloud project owner, you can shut down a project. Deleting a project acts as a bulk deletion request for all resources tied to the corresponding [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * **Google account deletion:** When you delete your Google account, it deletes all projects that aren't associated with an organization and that are solely owned by you. When there are multiple owners for a non-organization project, the project is not deleted until all owners are removed from the project or delete their Google accounts. This process ensures that projects continue so long as they have an owner.
  * **Google Workspace or Cloud Identity account deletion:** Organizations that are bound to a Google Workspace or Cloud Identity account are deleted when you delete a Google Workspace or Cloud Identity account. For more information, see [Delete your organization's Google Account](https://support.google.com/a/answer/9468554).



You use deletion requests primarily to manage your data. However, Google can issue deletion requests automatically; for instance when you end your relationship with Google.

### Stage 2: Soft deletion

Soft deletion is the point in the process to provide a brief internal staging and recovery period to help ensure that there is time to recover any data that has been marked for deletion by accident or error. Individual Google Cloud products might adopt and configure such a defined recovery period before the data is deleted from the underlying storage systems so long as the period fits within Google's overall deletion timeline.

When [projects are deleted](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects?visit_id=638488820299910219-3376512512&rd=1#shutting_down_projects), Google Cloud first identifies the unique project number then it broadcasts a suspension signal to the Google Cloud products (for example, for example Compute Engine and Bigtable) that contain that project number. In this case, Compute Engine suspends operations that are keyed to that project number and the relevant tables in Bigtable enter an internal recovery period of up to 30 days. At the end of the recovery period, Google Cloud broadcasts a signal to the same products to begin logical deletion of resources tied to the unique project number. Then Google waits (and, when necessary, rebroadcasts the signal) to collect an acknowledgement signal (ACK) from the applicable products to complete project deletion.

When a Google account is closed, Google Cloud might impose an internal recovery period up to 30 days, depending on past account activity. After that grace period expires, a signal that contains the deleted billing account user ID is broadcasted to Google products and Google Cloud resources tied solely to that user ID are marked for deletion.

### Stage 3: Logical deletion from active systems

After the data is marked for deletion and any recovery period has expired, the data is deleted successively from Google's active and backup storage systems. On active systems, data is deleted in two ways.

In all Google Cloud products under the [Compute](https://cloud.google.com/products/compute), [Storage](https://cloud.google.com/products/storage), and [Database](https://cloud.google.com/products/databases) project categories, except Cloud Storage, copies of the deleted data are marked as available storage and overwritten over time. In an active storage system like Bigtable, deleted data is stored as entries within a massive structured table. Compacting existing tables to overwrite deleted data can be expensive, as it requires re-writing tables of existing (non-deleted) data, so mark-and-sweep garbage collection and major compaction events are scheduled to occur at regular intervals to reclaim storage space and overwrite deleted data.

In Cloud Storage, customer data is also deleted through cryptographic erasure. This is an industry standard technique that renders data unreadable by deleting the encryption keys that are needed to decrypt that data. One advantage of using cryptographic erasure, whether it involves Google-supplied or customer-supplied encryption keys, is that logical deletion can be completed even before all deleted blocks of that data are overwritten in Google Cloud's active and backup storage systems.

### Stage 4: Expiration from backup systems

Similar to deletion from Google's active systems, deleted data is eliminated from backup systems using both overwriting and cryptographic techniques. In the case of backup systems, however, customer data is typically stored within large aggregate snapshots of active systems that are retained for static periods of time to ensure business continuity in the event of a disaster (for example, an outage affecting an entire data center), when the time and expense of restoring a system entirely from backup systems might become necessary. Consistent with reasonable business continuity practices, full and incremental snapshots of active systems are made on a daily, weekly, and monthly cycles and retired after a predefined period of time to make room for the newest snapshots.

When a backup is retired, it is marked as available space and overwritten as new daily, weekly, or monthly backups are performed.

Note that any reasonable backup cycle imposes a pre-defined delay in propagating a data deletion request through backup systems. When customer data is deleted from active systems, it is no longer copied into backup systems. Backups that were performed before deletion are expired regularly based on the pre-defined backup cycle.

Finally, cryptographic erasure of the deleted data might occur before the backup that contains customer data has expired. Without the encryption key that was used to encrypt specific customer data, the customer data is unrecoverable even during its remaining lifespan on Google's backup systems.

### Deletion timeline

Google Cloud is engineered to achieve a high degree of speed, availability, durability, and consistency. The design of systems optimized for these performance attributes must be balanced carefully with the need to achieve timely data deletion. Google Cloud commits to delete customer data within a maximum period of about six months (180 days). This commitment incorporates the stages of Google's deletion pipeline described above, including the following:

  * **Stage 2:** After the deletion request is made, data is typically marked for deletion immediately and our goal is to perform this step within a maximum period of 24 hours. After the data is marked for deletion, an internal recovery period of up to 30 days might apply depending on the service or deletion request.
  * **Stage 3:** The time needed to complete garbage collection tasks and achieve logical deletion from active systems. These processes might occur immediately after the deletion request is received, depending on the level of data replication and the timing of ongoing garbage collection cycles. After the deletion request is made, it generally takes about two months to delete data from active systems, which is typically enough time to complete two major garbage collection cycles and ensure that logical deletion is completed.
  * **Stage 4:** The Google backup cycle is designed to expire deleted data within data center backups within six months of the deletion request. Deletion may occur sooner depending on the level of data replication and the timing of Google's ongoing backup cycles.



The following diagram shows the stages of Google Cloud's deletion pipeline and when data is erased from active and backup systems.

![Deletion pipeline diagram.](https://docs.cloud.google.com/static/docs/security/images/data-deletion.svg)

## Ensure safe and secure media sanitization

A disciplined media sanitization program enhances the security of the deletion process by preventing forensic or laboratory attacks on the physical storage media after it has reached the end of its lifecycle.

Google meticulously tracks the location and status of all storage equipment within our data centers, through acquisition, installation, retirement, and destruction, using barcodes and asset tags that are tracked in Google's asset database. Various techniques such as biometric identification, metal detection, cameras, vehicle barriers, and laser-based intrusion detection systems are used to prevent equipment from leaving the data center floor without authorization. For more information, see the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

Physical storage media can be decommissioned for a range of reasons. If a component fails to pass a performance test at any point during its lifecycle, it is removed from inventory and retired. Google also upgrades obsolete hardware to improve processing speed and energy efficiency, or increase storage capacity. Whether hardware is decommissioned due to failure, upgrade, or any other reason, storage media is decommissioned using appropriate safeguards. Google hard drives use technologies like full disk encryption (FDE) and drive locking to help protect data at rest during decommission. When a hard drive is retired, authorized individuals verify that the disk is erased by overwriting the drive with zeros and performing a multi-step verification process to ensure the drive contains no data.

If the storage media cannot be erased for any reason, it is stored securely until it can be physically destroyed. Depending on available equipment, we either crush and deform the drive or shred the drive into small pieces. In either case, the disk is recycled at a secure facility, ensuring that no one will be able to read data on retired Google disks. Each data center adheres to a strict disposal policy and uses the techniques described to achieve compliance with [NIST SP 800-88 Revision 1 _Guidelines for Media Sanitization_](https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final) and [DoD 5220.22-M _National Industrial Security Program Operating Manual_](https://www.federalregister.gov/documents/2020/12/21/2020-27698/national-industrial-security-program-operating-manual-nispom).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
