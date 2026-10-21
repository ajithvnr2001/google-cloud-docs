---
url: https://docs.cloud.google.com/filestore/docs/overview/
title: Filestore overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:15:49.511369+00:00
---

# Filestore overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Filestore overview Stay organized with collections  Save and categorize content based on your preferences. 

Filestore instances are fully managed file servers on Google Cloud that can be connected to a number of client types:

  * [Compute Engine VMs](https://docs.cloud.google.com/filestore/docs/mounting-fileshares)
  * [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/filestore/docs/filestore-for-gke)
  * [External datastores such as Google Cloud VMware Engine](https://docs.cloud.google.com/filestore/docs/gcve-datastores)
  * [On-premises machines](https://docs.cloud.google.com/filestore/docs/remote-mounting)
  * [Cloud Run services](https://docs.cloud.google.com/filestore/docs/mount-filestore-cloud-run)
  * [AI agent fleets and sandboxes](https://docs.cloud.google.com/filestore/docs/agent-volumes-overview)



Once provisioned, you can scale the capacity of your instances according to need without any downtime.

## Why Filestore?

Google Cloud offers three main types of data storage: block, file, and object storage.

As a type of persistent file storage, Filestore supports multiple concurrent application instances accessing the same file system simultaneously.

For Google Kubernetes Engine users, for example, Filestore provides multiple reader, multiple writer access, letting you mount your GKE PersistentVolumes as read-write by many nodes.

Filestore offers a versatile alternative to block storage products, such as Persistent Disk, which support only [limited options for multiple writer access to a disk](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms). 

When compared to object storage, such as Cloud Storage FUSE, while that product does offer some file system [semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md), it [lacks some of the more robust characteristics of file storage](https://docs.cloud.google.com/storage/docs/gcs-fuse#expandable-1) provided by Filestore. Some examples of capabilities supported by Filestore and not Cloud Storage FUSE include the following:

  * POSIX compliance
  * Hard links and file locking
  * Concurrency control for multiple writes on the same object



For more information, see the following resources:

  * [Compare the relative advantages of block, file, and object storage](https://docs.cloud.google.com/architecture/storage-advisor#review_the_storage_options).
  * [Review the storage options for HPC workloads in Google Cloud](https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud).
  * [Learn more about Filestore support for GKE](https://docs.cloud.google.com/filestore/docs/filestore-for-gke).
  * [Learn more about using Custom performance with GKE](https://docs.cloud.google.com/filestore/docs/csi-driver#custom-performance) to scale IOPS independently of capacity.
  * [Learn more about the limitations of Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse#expandable-1).
  * [Learn about storage options and access modes for GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).



## Service tiers

Filestore offers multiple service tiers that vary in capacity, performance, and features. Each service tier is tailored for specific use cases:

  * **Zonal tier:** Optimized for HPC, batch compute, media rendering, and localized workloads requiring high throughput and low latency.
  * **Regional tier:** Designed for mission-critical workloads requiring continuous availability and regional resilience.
  * **Multishares for GKE (Enterprise):** Optimized for GKE workloads that require high availability and multishares.
  * **Basic tiers (legacy):** Suitable for basic file sharing and software development.



For details, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).

## Protocol support

Filestore supports the following file system protocols:

Protocol | Supported service tiers | Highlights  
---|---|---  
NFSv3 | All service tiers | 

  * Supports bidirectional communication between the client and server.
  * Supports [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), and [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

  
NFSv4.1 | [zonal, regional, and enterprise service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers) | 

  * Supports client and server authentication, message integrity checks, and in-transit data encryption.
  * Supports [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), and [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

  
  
For help understanding which protocol may be right for you, see [About supported protocols](https://docs.cloud.google.com/filestore/docs/about-supported-protocols).

## Connectivity

Filestore instances can connect to any clients that are on the same VPC network, including [Shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc). You can also connect to clients on remote networks, such as an on-premises machine, using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

## Networking

For information related to Filestore networking requirements, see the following resources:

  * [Filestore networking and IP resource requirements](https://docs.cloud.google.com/filestore/docs/network-ip-requirements)
  * [Configure NFS ports on client VMs](https://docs.cloud.google.com/filestore/docs/setting-nfs-ports)
  * [Configure firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall)
  * [Create an instance on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc)
  * [Supported file system protocols](https://docs.cloud.google.com/filestore/docs/about-supported-protocols)



## Performance

[Custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) lets you define the performance settings for your Filestore instances independently of the specified capacity. This means you can optimize your Filestore instances for your workload requirements and scale your file shares to meet the demands of your applications without resizing the capacity.

Custom performance is available for regional and zonal [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers). In addition, GKE workloads can dynamically adjust performance for zonal and regional tiers without downtime. 

For details on performance settings, limits, and testing see [performance](https://docs.cloud.google.com/filestore/docs/performance).

## Data protection

The following sections discuss Filestore instance data protection.

### Encryption at rest

By default, Filestore automatically encrypts your data at rest. The durable storage behind each Filestore instance is encrypted with system-defined keys that are managed by Google.

When you delete a Filestore instance, Google discards the encryption information used by the instance, rendering the data irretrievable as per the description in [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

If you need more control over the keys that protect your data, you can also use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/filestore/docs/cmek) with Filestore.

For details, see [Encryption at rest in Google Cloud](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

### Encryption in transit

While NFSv3 does not encrypt data in transit, the NFSv4.1 protocol supports in-transit data encryption using Kerberos (`krb5p`). Additionally, all in-transit data to and within Google Cloud is encrypted.

For details, see the following resources:

  * [Benefits of NFSv4.1](https://docs.cloud.google.com/filestore/docs/about-supported-protocols#benefits-of-nfsv41)
  * [Encryption in Transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit)



### Access control

You can control the level of access that a client has on Filestore instance data based on the client's IP address. [IP-based access control](https://docs.cloud.google.com/filestore/docs/access-control#ip-based_access_control) rules for an instance can be created or modified during and after instance creation.

You can also control which Google Cloud users can create, edit, and view Filestore resources by using [IAM permissions and roles](https://docs.cloud.google.com/filestore/docs/iam).

## Data recovery options

The following sections discuss Filestore instance data recovery options.

### Backups

[Filestore backups](https://docs.cloud.google.com/filestore/docs/backups) are point-in-time copies of a Filestore instance that includes all user data and some instance metadata. You can create a backup of an instance in any region and then use it to restore the instance in any region to an existing Filestore instance or a new instance.

### Snapshots

A [Filestore snapshot](https://docs.cloud.google.com/filestore/docs/snapshots) preserves the state of your Filestore instance data at the time that the snapshot is created. You can use snapshots to restore individual files or directories or completely revert your instance to the state of a snapshot.

## Reliability

Filestore offers several features to ensure the reliability and availability of your data.

### Zonal reliability

Zonal and Basic tier instances are zonal resources with in-zone storage redundancy. If the zone fails due to an outage or maintenance, these instances become unavailable until the zone is restored.

Even if one or more zones in a region fail, you can still create new Zonal or Basic instances in any zone that remains operational. 

### Regional reliability

Regional and Enterprise tier instances are regional resources. 

They provide transparent failover during zone failures, continuing to serve data and accept writes. Filestore uses a strict consistency policy, acknowledging writes only after they are persisted to ensure data integrity during zone failures.

While NFS data access continues without interruption, operations through the Google Cloud console or the Filestore API might be unavailable for several hours during a zone failure. You might also experience some performance degradation until the zone recovers. Note that you cannot create new regional or enterprise instances in a region while it is experiencing a zone failure.

### Instance replication

For enhanced disaster recovery, Filestore offers [instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication). This feature lets you asynchronously replicate data from a source instance to a standby instance in a different region. In the event of a regional outage, you can promote the standby instance to continue serving data.

Instance replication is supported for the Zonal, Regional, and Enterprise tiers. 

### Zone failure identification

You can monitor for zone failures on the [Google Cloud Status Dashboard](https://status.cloud.google.com). 

## What's next

  * Learn more about Filestore's [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers) to decide which service tier is right for you. 
  * See the [regions that support Filestore](https://docs.cloud.google.com/filestore/docs/regions). 
  * [Compare the relative advantages of block, file, and object storage](https://docs.cloud.google.com/architecture/storage-advisor#review_the_storage_options).
  * [Review the storage options for HPC workloads in Google Cloud](https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
