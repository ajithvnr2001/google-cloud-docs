---
url: https://docs.cloud.google.com/storage/docs/introduction/
title: Cloud Storage overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:38.874563+00:00
---

# Cloud Storage overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage lets you store, manage, and retrieve unstructured data with high durability and global availability. You can use Cloud Storage to distribute web content, store datasets for analytics and machine learning workloads, and archive backups for compliance and disaster recovery.

## How Cloud Storage works

Cloud Storage is a scalable and managed storage service offered by Google Cloud that lets you store data as _objects_ in containers called _buckets_.

All buckets are associated with a _project_ , and you group your projects under an _organization_. After you create a project, you can [create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets), [upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects) to your buckets, and [download objects](https://docs.cloud.google.com/storage/docs/downloading-objects) from your buckets. You can also grant permissions to make your data accessible to principals you specify or [accessible to everyone on the public internet](https://docs.cloud.google.com/storage/docs/access-control/making-data-public). Directory capabilities let you utilize Cloud Storage more similarly to a hard drive or Network Attached Storage (NAS): folders let you organize objects in a directory structure, and managed folders let you simplify access control to your objects.

Each project, bucket, object, folder, and managed folder is a _resource_ in Google Cloud, as are things such as [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).

## The Google Cloud hierarchy

Here's how the Cloud Storage structure can apply to a real-world case:

  * [Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations): Your company, called Example Inc., creates a Google Cloud organization called `exampleinc.org`.

  * [Project](https://docs.cloud.google.com/storage/docs/projects): Example Inc. is building several applications, and each one is associated with a project. Each project has its own set of Cloud Storage APIs, as well as other resources.

  * [Bucket](https://docs.cloud.google.com/storage/docs/buckets): Each project can contain multiple buckets, which are containers to store your objects. For example, you might create a `photos` bucket for all the image files your app generates and a separate `videos` bucket. Cloud Storage offers different [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) and [locations](https://docs.cloud.google.com/storage/docs/locations) for your buckets, letting you choose the durability and availability of your data to suit the needs of your workloads.

Buckets serve as a primary data foundation in the broader Google Cloud ecosystem. You can connect your buckets as storage backends for other Google Cloud services, such as AI Hypercomputer, Vertex AI, and Google Kubernetes Engine.

  * [Object](https://docs.cloud.google.com/storage/docs/objects): Buckets contain objects, such as an image called `puppy.png`. An object is an immutable piece of data consisting of a file of any format. Each bucket can contain essentially unlimited individual objects.

  * [Folder](https://docs.cloud.google.com/storage/docs/folders-overview): Buckets with hierarchical namespace enabled can contain folders. Folders enable a real file system for storing objects, as opposed to a simulated file system. You can atomically rename a folder and all the objects within it in one operation.

  * [Managed folder](https://docs.cloud.google.com/storage/docs/managed-folders): Each bucket can also contain managed folders, which grant or revoke additional access beyond the IAM permissions set on the bucket. Managed folders don't use a true directory tree structure; rather, a managed folder is a resource overlay used only for permission checking.




### Resource names

**Note:** The use of resource names within Cloud Storage is limited to [Pub/Sub Notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) and [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam).

Each resource has a unique name that identifies it, much like a filename. Buckets have a resource name in the form of `projects/_/buckets/BUCKET_NAME`, where `BUCKET_NAME` is the ID of the bucket. Objects have a resource name in the form of `projects/_/buckets/BUCKET_NAME/objects/OBJECT_NAME`, where `OBJECT_NAME` is the ID of the object.

A `#NUMBER` appended to the end of the resource name indicates a specific generation of the object. `#0` is a special identifier for the most recent version of an object. `#0` is useful to add when the name of the object ends in a string that would otherwise be interpreted as a generation number.

## Tools for Cloud Storage

You can interact with Cloud Storage by using the following tools:

  * [Google Cloud console](https://console.cloud.google.com/storage/browser): The Google Cloud console provides a visual interface for you to manage your data in a browser.

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud): The gcloud CLI lets you interact with Cloud Storage through a terminal using [`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

  * [Client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries): The Cloud Storage client libraries allow you to manage your data using one of your preferred languages, including C++, C#, Go, Java, Node.js, PHP, Python, and Ruby.

  * REST APIs: Manage your data using the [JSON](https://docs.cloud.google.com/storage/docs/json_api) or [XML](https://docs.cloud.google.com/storage/docs/xml-api/overview) API.

  * [Terraform](https://www.terraform.io/): Terraform is an infrastructure-as-code (IaC) tool that you can use to provision the infrastructure for Cloud Storage. For more information, see [Provision resources with Cloud Storage](https://docs.cloud.google.com/storage/docs/terraform-for-cloud-storage).

  * [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api): gRPC lets you interact with Cloud Storage. gRPC is a high performance, open source universal RPC framework developed by Google that you can use to define your services using Protocol Buffers. 

  * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse): Cloud Storage FUSE lets you mount Cloud Storage buckets to your local file system. This enables your applications to read from a bucket or write to a bucket by using standard file system semantics.

  * [GCSFS Python library](https://github.com/fsspec/gcsfs): GCSFS is a Python library that provides a Pythonic file-system interface to Cloud Storage.




## Use cases and key features

Cloud Storage provides durable, globally available object storage that's adaptable to a wide range of enterprise workloads, from high-performance Artificial Intelligence (AI) and Machine Learning (ML) training to regulatory archiving.

### Store and access data for AI/ML and data analytics

Accelerate your AI/ML pipelines and analytical insights with high-throughput, low-latency data access designed for large-scale processing.

Capability | Capability, product, or feature  
---|---  
[Cloud Storage Rapid](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) | High-performance storage colocated with compute for sub-millisecond access and multi-TB/s aggregate throughput. Includes:   


  * [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket): Zonal object storage in the Rapid storage class designed for data-intensive AI/ML and analytics workloads.
  * [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache): Fully managed, SSD-backed zonal read cache that automatically scales capacity and bandwidth to accelerate read performance.

  
[Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) | Organizes data into a logical directory structure with atomic folder operations and up to 8x higher initial QPS limits than buckets without hierarchical namespace. Hierarchical namespace can only be [enabled at the time of bucket creation](https://docs.cloud.google.com/storage/docs/create-hns-bucket) and can't be enabled on an existing bucket.  
[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) | Mounts buckets to your local file system, which enables your applications to read from a bucket or write to a bucket by using standard file system semantics.  
  
For more details on optimizing performance, see [Optimizing storage for AI/ML and data analytics](https://docs.cloud.google.com/storage/docs/agents-skills-overview).

### Data security and compliance

Protect your assets and meet global regulatory standards with built-in encryption, access controls, and immutable data retention policies.

Security layer | Capability, product, or feature  
---|---  
[Access control](https://docs.cloud.google.com/storage/docs/access-control) | Enforce least-privilege access and restrict traffic to trusted networks. Products and features include:   


  * [Identity and Access Management](https://docs.cloud.google.com/storage/docs/access-control/iam): Authorize specific users, groups, or service accounts to perform actions on Cloud Storage resources through role-based access controls.
  * [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access): Unify access control for your Cloud Storage resources by disabling object-level Access Control Lists (ACLs) and exclusively using bucket-level IAM policies.
  * [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview): Restrict access to a bucket based on the source IP address of the request and secure your data from unauthorized access from specific IP addresses or Virtual Private Cloud (VPC).

  
[Data encryption](https://docs.cloud.google.com/storage/docs/encryption) | Encrypt data at rest and in transit. Products and features include:   


  * [Google-managed keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys): Encrypt your Cloud Storage data at rest automatically by default by using server-side keys owned and maintained by Google.
  * [CMEK (Cloud KMS)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys): Control the rotation schedules, access permissions, and lifecycles of your encryption keys to protect your Cloud Storage resources.
  * [CSEK](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys): Secure your Cloud Storage data at rest by providing your own cryptographic keys with each individual API request, instead of Google storing or recovering your key material.

  
[Data retention and immutability](https://docs.cloud.google.com/storage/docs/using-bucket-lock) | Prevent accidental deletion and help satisfy data compliance. Products and features include:   


  * [Bucket Lock](https://docs.cloud.google.com/storage/docs/using-bucket-lock): Govern how long objects in buckets must be retained by specifying a retention policy for the bucket to enforce regulatory and compliance data retention rules.
  * [Object Retention](https://docs.cloud.google.com/storage/docs/object-lock): Govern the lifespan of individual objects by applying an immutable retain-until date and time to specific objects, preventing them from being deleted or replaced until that duration expires.
  * [Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning): Preserve historical copies of your data by automatically archiving overwritten or deleted live objects as noncurrent versions, enabling you to restore past object states at any time.
  * [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete): Prevent permanent loss of data against accidental or malicious deletion by retaining recently deleted objects and buckets. By default, Cloud Storage enables soft delete for all buckets with a seven day retention period.

  
  
### Backup, disaster recovery, and business continuity

Protect your business against data loss, disaster events, and regional outages with multi-region availability and fast cross-region replication.

Capability, product, or feature | Description  
---|---  
[Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr) and [multi-regions](https://docs.cloud.google.com/storage/docs/locations#location-mr) | Automatically replicate data across geographically separated Google Cloud regions for 99.99% availability.  
[Turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) | Replicate 100% of newly written objects between dual-region pairs within 15 minutes.  
[Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) and [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) | Retain previous iterations and recently deleted objects for rollback after accidental overwrites or ransomware events.  
  
### Cost optimization and data lifecycle management

Reduce storage spend across the data lifecycle by matching access frequency to cost-effective storage tiers.

Storage class, product, or feature | Description  
---|---  
[Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) | Choose between [Standard storage](https://docs.cloud.google.com/storage/docs/storage-classes#standard), [Nearline storage](https://docs.cloud.google.com/storage/docs/storage-classes#nearline), [Coldline storage](https://docs.cloud.google.com/storage/docs/storage-classes#coldline), [Archive storage](https://docs.cloud.google.com/storage/docs/storage-classes#archive), and [Rapid storage](https://docs.cloud.google.com/storage/docs/storage-classes#rapid) based on data access frequency.  
[Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) | Automatically transition objects between storage classes based on object access patterns.  
[Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) | Delete or transition objects by using custom rule-based policies.  
  
### Content distribution and web serving

Distribute digital assets, downloads, and media files globally with low latency and high availability.

Capability, product, or feature | Description  
---|---  
[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) and [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) | Cache static assets at Google's global edge locations for ultra-low latency web delivery.  
[Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) | Provide time-limited read or write access to private objects without requiring Google credentials.  
[Static website hosting](https://docs.cloud.google.com/storage/docs/hosting-static-website) | Serve static HTML, CSS, JavaScript, and media assets directly from a public bucket.  
  
### Data migration and event-driven ingestion

Streamline the movement of external data into Google Cloud and trigger automated processing workflows upon object upload.

Integration | Description  
---|---  
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) | Managed, high-scale transfer of online data from Amazon S3, Microsoft Azure Blob Storage, HTTP sources, or on-premises storage.  
[Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview) | Ruggedized hardware appliances that ship up to hundreds of petabytes of offline data to Google Cloud.  
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) and [Pub/Sub](https://docs.cloud.google.com/storage/docs/pubsub-notifications) | Emit real-time event notifications on object creation, deletion, or metadata updates to trigger Cloud Run functions or Cloud Run services.  
  
### Analyze and manage data storage

Gain insights into your stored data and manage it at scale across your Cloud Storage environment.

Capability, product, or feature | Description  
---|---  
[Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) | Gain visibility into your storage environment to help optimize costs and enforce data governance policies.  
[Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview) | Monitor stored data and receive actionable findings to help optimize costs, improve performance, and strengthen security.  
[Object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | Generate structured metadata for your unstructured images and PDF documents by using machine learning models.  
[Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) | Query and analyze indexes of your bucket and object metadata in BigQuery.  
[Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) | Perform bulk operations, such as deleting objects, updating metadata, or applying retention policies across millions or billions of objects.  
[Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) | Move an existing bucket and its data to a new location while preserving the bucket name and object metadata with minimal downtime.  
  
## Quickstart guides

To learn the fundamentals of using Cloud Storage, visit the following guides:

  * [Google Cloud console quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)
  * [gcloud CLI quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud)
  * [Terraform quickstart](https://docs.cloud.google.com/storage/docs/terraform-create-bucket-upload-object)



## Looking for other products?

If Cloud Storage is not the right storage solution for you, see more information about the following storage services:

  * [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview): Store your data in a high-performance, fully managed parallel file system that's optimized for AI and HPC workloads.

  * [Google Drive](https://www.google.com/intl/en/drive/): Store, manage, and share your personal files.

  * [Cloud Storage for Firebase](https://firebase.google.com/docs/storage/): Manage data for your mobile applications.

  * [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks): Add block storage to your Compute Engine virtual machine.

  * [Filestore](https://docs.cloud.google.com/filestore/docs/overview): Add file storage for multiwriter access to your GKE clusters.

  * Explore more [storage services](https://docs.cloud.google.com/products/storage) offered by Google.




## What's next

  * Learn the fundamentals of Cloud Storage through the [Google Cloud console](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) or [Google Cloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud). 
  * Try [Google Cloud jump start solutions that use Cloud Storage](https://docs.cloud.google.com/architecture/storage). 
  * Get started with [client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries). 
  * Automate storage workflows with AI coding assistants using [Cloud Storage agent skills](https://docs.cloud.google.com/storage/docs/agents-skills-overview). 
  * Quickly import online data into Cloud Storage or between Cloud Storage buckets using [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
