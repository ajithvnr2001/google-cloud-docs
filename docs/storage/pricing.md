---
url: https://docs.cloud.google.com/storage/pricing/
title: Storage pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:48:02.593405+00:00
---

# Storage pricing | Google Cloud

> Source: https://docs.cloud.google.com/storage/pricing/

Page Contents




## Cloud Storage pricing

This document discusses pricing for Cloud Storage. For Google Drive, which offers simple online storage for your personal files, see [Google Drive pricing](https://www.google.com/drive/#pricing).

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### Overview

Cloud Storage pricing is based on the following components:

  * [Data storage](https://docs.cloud.google.com/storage/pricing#data-storage): the amount of data stored in your buckets. Storage rates vary depending on the storage class of your data and location of your buckets.
  * [Data processing](https://docs.cloud.google.com/storage/pricing#data-processing): the processing done by Cloud Storage, which includes operations charges, any applicable retrieval fees, and inter-region replication.
  * [Network usage](https://docs.cloud.google.com/storage/pricing#network): the amount of data read from or moved between your buckets.
  * [Rapid Cache](https://docs.cloud.google.com/storage/pricing#rapid-cache): On-demand accelerated read cache for your buckets.
  * [Rapid Bucket](https://docs.cloud.google.com/storage/pricing#rapid-bucket): High performance object storage in a zonal bucket.



## 

Pricing tables

The pricing tables below show what charges apply when using Cloud Storage.

For example scenarios that show usage and charges, see the [Pricing examples page](https://cloud.google.com/storage/pricing-examples#detailed). For the Google Cloud pricing calculator, see the [Calculator page](https://cloud.google.com/products/calculator).

### 

Data storage

Click on a geographic area to view the at-rest costs for associated [locations](https://cloud.google.com/storage/docs/locations):

**Region**

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Standard storage| Nearline storage| Coldline storage| Archive storage| Rapid Cache storage  
---|---|---|---|---  
$0.000027397 / 1 gibibyte hour, per 1 month / account| $0.000013699 / 1 gibibyte hour| $0.000005479 / 1 gibibyte hour| $0.000001644 / 1 gibibyte hour| $0.0001233 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**Dual-region**

Iowa (us-central1)

  * Taiwan (asia-east1)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Asia 1 (asia1)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe 4 (eur4)
  * Europe 5 (eur5)
  * Europe 7 (eur7)
  * Europe 8 (eur8)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * North America 4 (nam4)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)



HourlyHourly

MonthlyMonthly

Standard storage| Nearline storage| Coldline storage| Archive storage  
---|---|---|---  
$0.000030137 / 1 gibibyte hour| $0.000015068 / 1 gibibyte hour| $0.000006027 / 1 gibibyte hour| $0.000001918 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**Multi-region**

Asia (asia)

  * Asia (asia)
  * Europe (eu)
  * US (us)



HourlyHourly

MonthlyMonthly

Standard storage| Nearline storage| Coldline storage| Archive storage  
---|---|---|---  
$0.000035616 / 1 gibibyte hour| $0.000020548 / 1 gibibyte hour| $0.000011986 / 1 gibibyte hour| $0.00000411 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**Zonal**

Iowa (us-central1)

  * Singapore (asia-southeast1)
  * Belgium (europe-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Las Vegas (us-west4)



HourlyHourly

MonthlyMonthly

Rapid storage  
---  
$0.000150685 / 1 gibibyte hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Dual-regions are billed to both underlying regions at the above prices. For example, Standard storage in a dual-region comprised of Iowa and Oregon will be billed at $0.022 per GB per month for the us-central1 dual-region SKU and $0.022 per GB per month for the us-west1 dual-region SKU. The six predefined dual-regions asia1, eur4, eur5, eur7, eur8, and nam4 bill usage against their locational SKUs at the prices listed.

Data storage charges are [prorated](https://cloud.google.com/storage/pricing-examples#prorate) to the sub-second for each object, and data storage rates are based on the storage class of each object, not the [default storage class](https://cloud.google.com/storage/docs/storage-classes#key-concepts) set on the bucket that contains them. Data storage charges apply in the same way to live objects, noncurrent objects, and soft-deleted objects.

In addition to the data contained in your uploaded objects, the following count toward your monthly storage usage:

  * [Custom metadata](https://cloud.google.com/storage/docs/metadata#custom-metadata). For example, for the custom metadata **NAME:VALUE** , Cloud Storage counts each character in **NAME** and **VALUE** as a byte stored with the object.
  * Uploaded parts of an [XML API multipart upload](https://cloud.google.com/storage/docs/multipart-uploads), until the multipart upload is either completed or aborted.



#### Minimum storage duration

A  _minimum storage duration_ applies to data stored using Nearline storage, Coldline storage, or Archive storage.

The following table shows the minimum storage duration for each storage class:

Standard storage| Nearline storage| Coldline storage| Archive storage| Rapid storage  
---|---|---|---|---  
None| 30 days| 90 days| 365 days| None  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

You can delete, replace, or move an object before it has been stored for the minimum duration, but at the time you delete, replace, or move the object, you are charged as if the object was stored for the minimum duration. See the [early deletion example](https://cloud.google.com/storage/pricing-examples#early-delete) to see how charges apply.

Note the following regarding minimum storage durations and early deletion charges:

  * Early deletion charges are billed through [early delete SKUs](https://cloud.google.com/skus/?filter=early%20delete).
  * Early deletion charges apply when rewriting objects, such as when you [change an object's storage class](https://cloud.google.com/storage/docs/changing-storage-classes), because a rewrite replaces the existing object.
  * Early deletion charges do not apply in the following cases:
  * When [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle) changes an object's storage class.
  * When the object exists in a bucket that has [Autoclass](https://cloud.google.com/storage/docs/autoclass) enabled.
  * In buckets that use [Object Versioning](https://cloud.google.com/storage/docs/object-versioning), early deletion charges apply when a noncurrent object is deleted, not when it became noncurrent. That object will become soft deleted if [soft delete](https://cloud.google.com/storage/docs/soft-delete) is enabled. Otherwise it will be permanently deleted.
  * In buckets that use [soft delete](https://cloud.google.com/storage/docs/soft-delete), early deletion charges apply when an object is soft deleted. These charges are reduced based on the length of the soft delete retention duration.
  * For [XML API multipart uploads](https://cloud.google.com/storage/docs/multipart-uploads), a part is subject to early deletion charges if it's not used when assembling the final object, or if the part is overwritten by another part, or if the multipart upload is aborted.
  * The storage duration for each part in a multipart upload begins at the time the upload of the part completes, and the storage duration for the overall object begins when the object is assembled.



#### Tags

Each [tag](https://cloud.google.com/storage/docs/tags-and-labels#tags) that you attach to a bucket is charged at $0.005 per month.

### 

Data processing

Data processing costs consist of the following:

  * [**Operation charges**](https://docs.cloud.google.com/storage/pricing#operation-charges) for all requests made to Cloud Storage
  * [**Retrieval fees**](https://docs.cloud.google.com/storage/pricing#retrieval-fees) for reading data stored in certain storage classes
  * [**Inter-region replication charges**](https://docs.cloud.google.com/storage/pricing#inter-region-replication) for data written to dual-regions and multi-regions
  * [**Autoclass charges**](https://docs.cloud.google.com/storage/pricing#autoclass-pricing) for buckets with Autoclass enabled
  * [**Storage Intelligence charges**](https://docs.cloud.google.com/storage/pricing#storage-intelligence) for buckets with Storage Intelligence configured.
  * [**Objects Contexts**](https://docs.cloud.google.com/storage/pricing#object-contexts) charges for objects with attached contextual information



### 

Operation charges

Operation charges apply when you perform  _operations_ within Cloud Storage. An operation is an action that makes changes to or requests information about resources such as buckets and objects in Cloud Storage.

Operations are divided into three categories: Class A, Class B, and free. [See below](https://docs.cloud.google.com/storage/pricing#operations-by-class) for a breakdown of which operations fall into each class.

For buckets located in a single [region](https://cloud.google.com/storage/docs/bucket-locations#location-r):

Storage Class1| Class A operations, flat namespace(per 1,000 operations)| Class A operations, hierarchical namespace(per 1,000 operations)| Class B operations, flat namespace(per 1,000 operations)| Class B operations, hierarchical namespace(per 1,000 operations)| Free operations  
---|---|---|---|---|---  
Standard storage| $0.005| $0.0065| $0.0004| $0.0005| Free  
Nearline Storage and Durable Reduced Availability (DRA) storage  
| $0.01| $0.013| $0.001| $0.0013| Free  
Coldline storage| $0.02| $0.026| $0.01| $0.013| Free  
Archive storage| $0.05| $0.065| $0.05| $0.065| Free  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

For buckets located in a [dual-region](https://cloud.google.com/storage/docs/bucket-locations#location-dr) or [multi-region](https://cloud.google.com/storage/docs/bucket-locations#location-mr):

Storage Class1| Class A operations, flat namespace(per 1,000 operations)| Class A operations, hierarchical namespace(per 1,000 operations)| Class B operations, flat namespace(per 1,000 operations)| Class B operations, hierarchical namespace(per 1,000 operations)| Free operations  
---|---|---|---|---|---  
Standard storage| $0.01| $0.013| $0.0004| $0.0005| Free  
Nearline storage and Durable Reduced Availability (DRA) storage| $0.02| $0.026| $0.001| $0.0013| Free  
Coldline storage| $0.04| $0.052| $0.01| $0.013| Free  
Archive storage| $0.10| $0.13| $0.05| $0.065| Free  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

For buckets located in a [zone](https://cloud.google.com/storage/docs/locations#location-z):

Storage Class1| Class A operations, hierarchical namespace(per 1,000 operations)| Class B operations, hierarchical namespace(per 1,000 operations)| Class C operations, hierarchical namespace(per 1,000 operations)| Class D operations, hierarchical namespace(per 1,000 operations)| Free operations  
---|---|---|---|---|---  
Rapid storage| $0.00113| $0.0002| $0.000625| $0.00002| Free  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

1The storage class for an operation is determined by the following considerations:

  * When listing buckets in a project, the Class A Standard storage rate always applies.
  * When an operation applies to a bucket, such as listing the objects in a bucket, the [default storage class](https://cloud.google.com/storage/docs/storage-classes#key-concepts) set for that bucket determines the operation cost.
  * When an operation applies to a [tag](https://cloud.google.com/storage/docs/tags-and-labels#tags), such as attaching or detaching tags, the [default storage class](https://cloud.google.com/storage/docs/storage-classes#key-concepts) set for the tagged bucket determines the operation cost.
  * When an operation applies to an object, the storage class of that object determines the operation cost. The following are exceptions to this rule:
  * When changing the storage class of an object, either [yourself](https://cloud.google.com/storage/docs/changing-storage-classes) or with [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle), the Class A rate associated with the object's destination storage class applies. For example, changing an object from Standard storage to Coldline storage using Object Lifecycle Management counts as a Class A operation and is billed at the Class A operation rate for Coldline storage. Changing storage classes can have a significant billing impact, especially when a high proportion of objects are under 1 MB in size.
  * When changing the storage class of an object using [Autoclass](https://cloud.google.com/storage/docs/autoclass), most transitions are free. However, the Class A Standard storage rate applies for transitions from Coldline storage or Archive storage to Standard storage or Nearline storage.
  * In buckets with [Autoclass](https://cloud.google.com/storage/docs/autoclass) enabled, operations are always charged at the Standard storage rate.
  * In buckets with [soft delete](https://cloud.google.com/storage/docs/soft-delete) enabled, restore operations are always charged at the Standard storage rate.



In buckets that use [soft delete](https://cloud.google.com/storage/docs/soft-delete), one Class A Standard storage operation is charged per 1,000 objects processed as part of a bulk restore operation, rounded up so that at least one Class A operation is always billed. This is in addition to the operations charge assessed per object restored.

**Operations that fall into each class**

The following table lists the operations that fall into each class for the JSON API, XML API, and gRPC. Keep in mind the following:

  * Except as noted in the footnotes, each request is considered one operation, regardless of the content sent or received as part of the request.
  * Tools such as the Google API console, the Google Cloud CLI, and the [Cloud Storage client libraries](https://cloud.google.com/storage/docs/reference/libraries) might use two or more operations to perform a task. For example, when you click on a bucket name in the Google Cloud console, the system performs an operation to get the list of objects in the bucket and a separate operation to get the metadata for the bucket.
  * The Google API console uses the JSON API to make requests. Other tools might use either or both the JSON API and XML API. Consult the tool's reference documentation for information about the underlying API that it uses.



API or Feature| Class A Operations| Class B Operations| Class C Operations| Class D Operations| Free Operations  
---|---|---|---|---|---  
JSON API or gRPC| storage.*.insert1storage.*.patchstorage.*.updatestorage.*.setIamPolicystorage.buckets.liststorage.objects.copystorage.objects.liststorage.objects.movestorage.buckets.lockRetentionPolicystorage.notifications.deletestorage.objects.composestorage.objects.restorestorage.objects.rewrite1storage.objects.watchAllstorage.projects.hmacKeys.createstorage.projects.hmacKeys.liststorage.*AccessControls.deletestorage.folders.liststorage.folders.rename| storage.*.getstorage.*.getIamPolicystorage.*.testIamPermissionsstorage.*AccessControls.liststorage.notifications.listEach object change notification2storage.buckets.getStorageLayout| | | storage.channels.stopstorage.buckets.deletestorage.objects.deletestorage.projects.hmacKeys.deletestorage.folders.delete  
XML API| GET ServiceGET Bucket (when listing objects in a bucket)PUTPOST| GET Bucket (when retrieving bucket configuration or when listing ongoing multipart uploads)GET ObjectHEAD| | | DELETE  
[Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle)| SetStorageClass| | | | AbortIncompleteMultipartUploadDelete  
[Autoclass](https://cloud.google.com/storage/docs/autoclass)| The following storage class transitions:

  * Coldline to Standard
  * Archive to Standard
  * Coldline to Nearline
  * Archive to Nearline

| | | | The following storage class transitions:

  * Nearline to Standard
  * Standard to Nearline
  * Nearline to Coldline
  * Coldline to Archive

  
[Tags](https://cloud.google.com/storage/docs/tags-and-labels#tags)3| Attach a tagDetach a tag| List tags attached to a bucket| | |   
[soft delete](https://cloud.google.com/storage/docs/soft-delete)| Process 1,000 objects during a bulk restoreRestore a soft-deleted object| List soft-deleted objects| | |   
[Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache)| Create CacheUpdate CachePause CacheResume Cache| Get CacheList Cache| | | Disable Cache  
[Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket)| Create Appendable ObjectOpen Write Appendable Object| Open Read Appendable Object| Write to Open Object| Read from Open Object  
| Finalize Appendable ObjectOpen Read Object with HandleOpen Write Object with HandleRefresh Read Access HandleRefresh Write Access Handle  
  
In Hierarchical Namespace buckets, iterative (recursive) folder operations are billed as class A for each child operation. There are two types of iterative folder operations:

  1. Operations that create missing parent folders automatically. Each parent folder created is considered a child operation. This includes the following operations (and their equivalents in the XML API, if applicable):
  2. storage.objects.insert
  3. storage.objects.compose
  4. storage.objects.copy
  5. storage.objects.move
  6. storage.objects.rewrite
  7. storage.objects.restore
  8. storage.managedFolders.insert
  9. storage.folders.insert (when recursive is set to true)
  10. Complete a multipart upload (this is a POST operation in the XML API)
  11. The rename folder operation. Each child folder under the top-level folder being renamed is considered a child operation.



1A [rewrite](https://cloud.google.com/storage/docs/json_api/v1/objects/rewrite) or [resumable upload](https://cloud.google.com/storage/docs/resumable-uploads) of a single object performed using the JSON API or gRPC is billed as a single Class A operation, even though these actions can require multiple requests to complete.

2Applies specifically to [Object Change Notifications](https://cloud.google.com/storage/docs/object-change-notification). For [Pub/Sub notifications](https://cloud.google.com/storage/docs/pubsub-notifications), see [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).

3Tag operations are not eligible for the [Cloud Storage Always Free program](https://docs.cloud.google.com/storage/pricing#cloud-storage-always-free).

**Note:** Generally, you are not charged for operations that return 307, 4xx, or 5xx responses. The exception is 404 responses returned by buckets with [Website Configuration](https://cloud.google.com/storage/docs/hosting-static-website) enabled and the **NotFoundPage** property set to a public object in that bucket.

### 

Retrieval fees

A  _retrieval fee_ applies when you read, copy, move, or rewrite object data or metadata that is stored using Nearline storage, Coldline storage, or Archive storage. This cost is in addition to any [operations charges](https://docs.cloud.google.com/storage/pricing#operation-charges) and [network charges](https://docs.cloud.google.com/storage/pricing#network) associated with reading the data.

The following table shows the retrieval rates for each storage class:

Rapid storage| Standard storage| Nearline storage (USD)| Coldline storage (USD)| Archive storage (USD)  
---|---|---|---|---  
$0| $0| $0.01 / 1 gibibyte| $0.02 / 1 gibibyte| $0.05 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Retrieval fees do not apply when an object exists in a bucket that has [Autoclass](https://cloud.google.com/storage/docs/autoclass) enabled.

Retrieval fees do not apply when restoring soft-deleted objects.

Retrieval fees do not apply for data read from Rapid Cache.

### 

Inter-region replication

[Inter-region replication](https://cloud.google.com/storage/docs/availability-durability#cross-region-redundancy) is billed on a per-GB basis for all data written to buckets located in a dual-region or multi-region location. Writes include puts, rewrites, copies, and any other actions that create new objects.

Inter-region replication fees do not apply when restoring soft-deleted objects.

Click on a geographic area to view the inter-region replication costs for associated [locations](https://cloud.google.com/storage/docs/locations):

Geographic area| Location| Default replication (per GiB)| Turbo replication (per GiB)  
---|---|---|---  
North America| North American dual-regions, including nam4| $0.02| $0.04  
US (multi-region)| $0.02| Not available  
Europe| European dual-regions, including eur4, eur5, eur7, and eur8| $0.02| $0.04  
EU (multi-region)| $0.02| Not available  
Asia  
| Asian dual-regions, including asia1| $0.08| $0.11  
Asia (multi-region)| $0.08| Not available  
Oceania| Oceania dual-regions| $0.08| $0.12  
  
### 

Autoclass charges

The following additional charges are associated with buckets that use the [Autoclass](https://cloud.google.com/storage/docs/autoclass) feature:

**Autoclass management fee** : Buckets that have Autoclass enabled incur a fee of $0.0025 for every 1000 objects stored for 30 days within them.

  * Objects smaller than 128 kibibytes are not managed by Autoclass and are thus not counted when determining the fee.
  * The fee is [prorated](https://cloud.google.com/storage/pricing-examples#prorate) to the millisecond for each object that isn't stored for the 30-day period.
  * The fee is also prorated to the millisecond when disabling Autoclass.
  * Soft-deleted objects do not incur this fee.



**Autoclass enablement charge** : Buckets that enable Autoclass have a one-time charge for configuring existing objects to use Autoclass. This charge applies even if you immediately disable Autoclass and includes the following, as applicable:

  * Early delete charges for objects that haven't met their minimum storage duration
  * Retrieval fees for objects not currently in Standard storage
  * A Class A operation charge for each object in the bucket, in order to transition them to Autoclass pricing and Standard storage
  * Objects that are smaller than 128 kibibytes, and already stored in Standard storage at the time Autoclass is enabled are excluded from this operation charge



The Autoclass enablement charge does not apply to soft-deleted objects, which retain their existing storage classes and are billed as such until the end of their [soft delete](https://cloud.google.com/storage/docs/soft-delete) retention duration.

### 

Network

 _Outbound data transfer_ represents data sent from Cloud Storage in HTTP responses. Data or metadata read from a Cloud Storage bucket are examples of data transfer.

_Inbound data transfer_ represents data sent to Cloud Storage in HTTP requests. Data or metadata written to a Cloud Storage bucket are examples of inbound data transfer.

Network usage charges apply for data transfer and are divided into the following cases:

  * [Data transfer within Google Cloud](https://docs.cloud.google.com/storage/pricing#network-buckets), when data transfer is to other Cloud Storage buckets or to Google Cloud services.
  * [Specialty network services](https://docs.cloud.google.com/storage/pricing#network-special), when data transfer uses certain Google Cloud network products.
  * [General data transfer](https://docs.cloud.google.com/storage/pricing#network-egress), when data transfer is out of Google Cloud or between continents.



### 

Data transfer within Google Cloud

Data transfer within Google Cloud applies when you move or copy data from one Cloud Storage bucket to another or when another Google Cloud service accesses data in your Cloud Storage bucket.

The following cases of data transfer from a Cloud Storage bucket to within Google Cloud are free:

Case| Examples| Notes  
---|---|---  
Data moves within the same location.| 

  * UA-EAST1-A to US-EAST1-B
  * US-EAST1 to US-EAST1
  * EU to EU

| A region is not considered the same location as a multi-region, even if the region is within the geographic limits of a multi-region.Data moves from different zones within the same region are considered within the same location.For data transfer out to BigQuery datasets, Cloud Storage will consider BigQuery US to be equivalent to us-central1 and BigQuery EU to be equivalent to europe-west4. As an example, no data transfer out charges will be assessed when BigQuery US reads data from a bucket in us-central1, or from a dual-region bucket with one region set as us-central1. However, data transfer out charges will apply when BigQuery US reads data from any other Cloud Storage bucket.  
Data moves from a Cloud Storage bucket located in a dual-region to a different Google Cloud service located in one of the regions that make up the dual-region.| 

  * Accessing data in an NAM4 bucket with an US-CENTRAL1 GKE instance

| This case does not include bucket-to-bucket data moves.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

You can use Rapid Cache to avoid data transfer fees associated with multi-region buckets on reads, once data is ingested into the cache.

For all other data transfer from your Cloud Storage buckets to within Google Cloud, pricing is determined by the bucket's location and the destination location, as defined in the following matrix:

Destination location →Bucket location ↓| Northern America| Europe| Asia| Indonesia| Oceania| Middle East| Latin America| Africa  
---|---|---|---|---|---|---|---|---  
**Northern America**|  $0.02| $0.05| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Europe**|  $0.05| $0.02| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Asia**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Indonesia**|  $0.10| $0.10| $0.10| N/A| $0.08| $0.11| $0.14| $0.14  
**Oceania**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Middle East**|  $0.11| $0.11| $0.11| $0.11| $0.11| $0.08| $0.14| $0.11  
**Latin America**|  $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14  
**Africa**|  $0.11| $0.11| $0.11| $0.14| $0.14| $0.11| $0.14| N/A  
  
Prices are in per GiB units

### 

Specialty network services

If you have chosen to use certain Google Cloud network products, data transfer pricing is based on their pricing tables:

  * For Cloud CDN, Cloud Storage data transfer charges are waived, but cache fill charges may apply. For more information, see [Cloud CDN pricing](https://cloud.google.com/cdn/pricing).
  * For Media CDN, Cloud Storage data transfer charges are waived. For more information, [contact sales](https://cloud.google.com/contact).
  * For CDN Interconnect, see [CDN Interconnect pricing](https://cloud.google.com/network-connectivity/docs/cdn-interconnect#pricing).
  * For Cloud Interconnect, see [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing). For more information, see the [Cloud Interconnect overview](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * For Direct Peering, see [Direct Peering pricing](https://cloud.google.com/network-connectivity/docs/direct-peering#pricing).



### 

General network usage

General network usage applies for any data read from your Cloud Storage bucket that does not fall into one of the above categories or the [Always Free usage limits](https://docs.cloud.google.com/storage/pricing#cloud-storage-always-free). For example, general network usage applies when data moves from a Cloud Storage bucket to the Internet. You can view your current usage in the [billing details for your project](https://console.cloud.google.com/billing).

Item| Price (USD)  
---|---  
Data transfer to Worldwide Destinations (excluding Asia & Australia)(per GB)| 0 gibibyte to 10 tebibyte$0.12 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.11 / 1 gibibyte, per 1 month / account150 tebibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data transfer to Asia Destinations (excluding China, but including Hong Kong)(per GB)| 0 gibibyte to 10 tebibyte$0.12 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.11 / 1 gibibyte, per 1 month / account150 tebibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data transfer to China Destinations (excluding Hong Kong)(per GB)| 0 byte to 1 tebibyte$0.23 / 1 gibibyte, per 1 month / account1 tebibyte to 10 tebibyte$0.22 / 1 gibibyte, per 1 month / account10 tebibyte and above$0.20 / 1 gibibyte, per 1 month / account  
Data transfer to Australia Destinations (per GB)| 0 gibibyte to 10 tebibyte$0.19 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.18 / 1 gibibyte, per 1 month / account150 tebibyte and above$0.15 / 1 gibibyte, per 1 month / account  
Inbound data transfer| Free  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Storage Intelligence

AI-powered [Storage Intelligence](https://cloud.google.com/storage/docs/storage-intelligence/overview) provides you with insights to help you manage and optimize storage at scale. Generate [storage insights datasets](https://cloud.google.com/storage/docs/insights/datasets) specific to your environment by querying object metadata & activity data at scale. Use [bucket relocation](https://cloud.google.com/storage/docs/bucket-relocation/overview) to minimize application downtime by automatically moving entire buckets while preserving their bucket names. Perform [batch operations](https://cloud.google.com/storage/docs/batch-operations/overview) at scale using managed jobs on millions of objects.

Storage Intelligence charges apply when configuring and using various capabilities as follows:

**Trial Tier**

The Storage Intelligence [30-day introductory trial](https://cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview) lets you learn and explore Storage Intelligence features and capabilities for up to 30 days. After activation, you can use features such as getting data insights with Gemini assistance, Storage Insights datasets, bucket relocation, and storage batch operations. The Storage Intelligence Object Management Fee is waived during the Trial period for the objects in scope of the trial & the Early Termination Fee does not apply during this period. Other charges as outlined below per feature will continue to apply. The Trial tier defaults to the Standard tier at the end of the 30-day period & charges associated with the Standard tier will begin to accrue.

**Standard Tier**

When configured for Standard tier the Storage Intelligence Standard Object Management Fee ($2.5 per million objects per month) applies to all objects within the specified Organization / Folder / Project. Unless filters are specified all buckets are included even as new ones are added. Any buckets that are removed from Standard Tier within 30 days of inclusion incur Storage Intelligence Early Termination Fee for the remaining duration. Charges are amortized daily and only apply to objects that exist more than 24 hours.

**Insights Datasets**

These can be configured for the same Organization / Folder / Project as the Storage Intelligence tier. When configured, daily snapshots are delivered for all the buckets/objects that have been enabled with Standard tier. Any number of Datasets can be configured for the same buckets and the Standard tier fee is only applied once.

BigQuery storage fees does apply for every instance for Datasets. Typically 1 TB of Cloud Storage data generates 300 MB of metadata daily however this can vary based on custom metadata stored within objects. Customers can configure the duration of snapshot retention. If Storage Intelligence is disabled for a project then new snapshots will not be delivered however the existing BigQuery data will not be deleted and will continue to incur storage charges. Customers can delete the Datasets configuration at any time to remove their data from BigQuery.

**Note:** Active Logical Storage charges in BigQuery will be waived for 90 days after the GA launch date for the data stored in the following new views: object_events_view, bucket_activity_view, project_activity_view, and bucket_region_activity_view. After this 90-day promotional period post the GA launch, standard BigQuery storage fees will be charged for these views. All other BigQuery storage remains subject to standard charges.

**Note:** This will not impact the active logical storage charges for existing metadata tables (bucket_attributes_latest_snapshot_view, bucket_attributes_view, error_attributes_view, events_view, object_attributes_latest_snapshot_view, object_attributes_view, project_attributes_view) which will continue to accrue active logical storage costs.

**Storage batch operations**

  * Storage Batch Operations is exclusively available to Storage Intelligence customers. There are no additional charges for using Batch Operations beyond the subscription fee of Storage Intelligence.
  * **Operations charges** : All operations performed by Batch Operations incur operations charges based on the storage class of the object being acted on.
  * Deletions performed by Batch Operations do not incur any charges.
  * All transformations performed by Batch Operations, except object deletions, incur a Class B operation charge.
  * All transformations performed by Batch Operations, except object deletions, incur a Class A operations charge. This operation charge does not apply if the object is already in the desired end state.
  * Batch operations jobs, including dry-run, may require listing bucket contents. You incur Class A operation charges when batch operations perform a list operation. A single list operation can retrieve a maximum of 1000 objects per bucket.



####   


**Bucket relocation**

When using [bucket relocation](https://cloud.google.com/storage/docs/bucket-relocation/overview), a $0.04 per GB charge applies for all data successfully moved to the destination. In addition, the following charges apply:

  * **Storage Intelligence** : Bucket relocation is a premium feature offered as a part of Storage Intelligence. [Storage Intelligence](https://docs.cloud.google.com/storage/pricing#data-processing) must be enabled on the source bucket to use bucket relocation.
  * **Data transfer charges** : You pay [inter-region data transfer charges](https://docs.cloud.google.com/storage/pricing#network-buckets) for moving the data from the source to the destination region. Data transfer is charged per GB of data moved.
  * [**Operation charges**](https://docs.cloud.google.com/storage/pricing#operation-charges): You pay one Class A operation per object moved. Additional Class A operations are charged to resynchronize object metadata for objects whose metadata have been updated since the move started. This can mean up to N additional Class A operations for an object updated N times after the move started.
  * [**Data storage charges**](https://docs.cloud.google.com/storage/pricing#pricing-tables): You pay for data storage charges in both the source and destination locations while bucket relocation processes the move, temporarily increasing your storage charges. Once the move has completed, you only pay for data storage based on the new, destination location.
  * **Data replication charges** : If the destination of the move is a multi-region or dual-region bucket, [inter-region replication](https://docs.cloud.google.com/storage/pricing#inter-region-replication) charges apply since the destination data must be replicated to a remote region.
  * **Data retrieval charges** : Retrieval fees are not assessed as part of a bucket relocation.
  * **Early deletion charges** : You are not billed early deletion charges for the data cleanup in the source bucket after the move.



Destination→Source↓| Region| Predefined dual-region| Configurable dual-region| Multi-region  
---|---|---|---|---  
Region| All charges apply| All charges apply| All charges apply except with following changes:\- No data transfer charges if there is any overlap of even a single region between source and destination| All charges apply  
Predefined dual-region| All charges apply| All charges apply| All charges apply| All charges apply  
Configurable dual-region| All charges apply except with following changes:\- No data transfer charges if there is any overlap of even a single region between source and destination| All charges apply| All charges apply except with following changes:\- No data transfer charges if there is any overlap of even a single region between source and destination.\- Storage charges applied at either the source or the destination location, if the move is within the same multi-region.| All charges apply except with following changes:\- Storage charges applied at either the source or the destination location, if the move is within the same multi-region.  
Multi-region| All charges apply| All charges apply| All charges apply except with following changes:\- Storage charges applied at either the source or the destination location, if the move is within the same multi-region.| All charges apply  
  
**Pricing example for Storage Intelligence**

If you have 1000 objects in 1000 buckets that are distributed over 10 projects and you enable Storage Intelligence for all 10 projects, or at Organization level that includes these 10 projects, then you will be charged a monthly Storage Intelligence Standard Object Management Fee of $2.5 for the 1 million objects (1000 objects x 1000 buckets). Charges are applied to the same project where buckets are present.

These charges are applied daily, with $/million objects rate amortized over 30 days. If you have less than a million objects then the charges are amortized so you only pay for the set of objects that are under management for the duration of their existence (over 24 hours).

A 30-day early termination fee which applies when a bucket is removed from a subscription within 30 days of enrollment. Any bucket deletions do not incur this 30-day early termination fee. If you disable Storage Intelligence after 24 days of enablement (6 days remaining) then for example a total of $0.5 Early Termination Fee will be applied on the 25th day for the 1000 buckets that were removed.

### 

Inventory Reports

Inventory Reports are subject to pricing, where every one million objects contained in an inventory report is charged at the pricing below, dependent upon storage location. For more information about storage locations, see [Bucket locations](https://cloud.google.com/storage/docs/locations).

**Supported locations**

Iowa (us-central1)

  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Price (USD)| Unit  
---|---  
$0.0025| per one million objects  
  
Asia (asia)

  * Asia (asia)
  * Asia 1 (asia1)
  * Europe 4 (eur4)
  * North America 4 (nam4)
  * US (us)



Price (USD)| Unit  
---|---  
$0.0028| per one million objects  
  
### 

Rapid Cache

Rapid Cache pricing is based on the following components:

  * Cache storage: the amount of data stored in cache
  * Cache ingest: the amount of data written into the cache
  * Cache data transfer out: the amount of data read from the cache
  * Cache data transfer out operations: the amount of read requests served from the cache
  * Cache management operations: the amount of bucket-level cache management requests (normally not significant on bills)



The following pricing applies to any bucket where Rapid Cache is enabled. Rapid Cache pricing is supplemental to the overall service pricing. Unless explicitly stated, the Cloud Storage service prices provided elsewhere in this document continue to apply in addition to Rapid Cache prices.

When reading data that is not already cached in the same zone where the data is being read, all normal Cloud Storage prices apply for the request (for example: Class B operations and multi-region data transfer out charges). In addition, the cache ingest charge applies to load the data being read into the cache. Once data is in the cache, cache storage charges apply until it is evicted from the cache.

When the data being read in a particular zone is already cached in that zone’s cache, cache operations charges apply for requests instead of the normal higher priced Class B operations. Cache data transfer out charges are also assessed based on the volume of data read.

Bucket-level cache configuration and management requests incur normal Class A or Class B operations, per the table in the [Operation section](https://docs.cloud.google.com/storage/pricing#operation-charges).

Please see the [Rapid Cache documentation](https://cloud.google.com/storage/docs/anywhere-cache) for more detailed information on how you can [control costs](https://cloud.google.com/storage/docs/anywhere-cache#cost_controls) using Rapid Cache.

**Cache Storage Charges**

Data cached by Rapid Cache incur a per-GB, per-hour storage fee, with charges pro-rated to the second for each byte of data. Prices are set by region and are listed under the Rapid Cache column under [Data Storage](https://docs.cloud.google.com/storage/pricing#data-storage) above.

**Cache Data Processing Charges**

Charge| Price| Notes  
---|---|---  
Cache ingest| $0.0032 / 1 gibibyte| Data is ingested and charged in 2 MB increments regardless of request size, unless the end of the object is reached in which case the ingest and ingest charges will stop at end of the object. Metadata-only reads do not trigger cache ingest.  
Cache operations| $0.0002 / 1,000 count| Requests entirely served by the cache incur cache operations charges. Otherwise Class B operations apply.  
Cache data transfer out| $0.0006 / 1 gibibyte| Charged for data read from the cache. This is based on the actual size of the read request, with byte sized granularity.  
  
### 

Rapid Bucket

Rapid Bucket is only available in zonal buckets. Pricing is based on the following components:

  * Data storage: the amount of data stored in the bucket.
  * Operation charges: for requests made to the bucket.
  * Data transfer charges: the amount of data read from or written to the bucket.



Please see the [Rapid Bucket documentation](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) for an overview and more detailed information about using Rapid Bucket.

**Data Storage Charges**

Data storage by Rapid Bucket incur a per-GB, per-hour storage fee, with charges pro-rated to the second for each byte of data. Prices are set by zone and are listed in the Rapid storage row under the Zonal section of the [Data Storage](https://docs.cloud.google.com/storage/pricing#data-storage) pricing table above.

**Data Transfer Charges**

Charge| Price| Notes  
---|---|---  
Data transfer out| $0.0006 / 1 gibibyte| Charged for data read from the bucket. This is based on the actual size of the read request, with byte sized granularity.  
Data transfer in| $0.0032 / 1 gibibyte| Charged for data written to the bucket. This is based on the actual size of the write request, with byte sized granularity.  
  
### 

Object Contexts

You can attach descriptive information as key-value pairs to your Cloud Storage objects using object contexts. You can embed contexts to improve how you categorize, track, and search your data. You can apply contexts when you create new objects or add them to existing objects. Object Contexts are charged at $3 per million per month. e.g. 1 million objects with 1 context each will be charged $3 per month. Also 500,000 objects with 2 contexts each will be charged $3 per month. 

### 

Object Enrichments

Google Cloud Storage Object Enrichments pricing is usage-based and depends on the specific enrichment models enabled across your project/buckets.

  * Global SKUs: All Object Enrichment SKUs are global (not regional), meaning pricing is uniform across all storage locations.
  * Component Classification: Charges are incurred per objects enriched for each enabled model, with SKU described in per 1,000 objects enriched.
  * Image Object Detection
  * Image Face Detection
  * Image Labeling
  * Image Explicit Content Detection
  * PDF Classification



### 

Image SKUs Pricing

The following table outlines the tiered pricing rates for image enrichment SKUs. Rates are calculated based on the monthly volume of objects analyzed per project.

Feature / SKU| Tier 1 (< 1,000,000 objects / month)| Tier 2 (>= 1,000,000 objects / month)  
---|---|---  
Image Object Detection| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account  
Image Face Detection| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account  
Image Labeling| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account  
Image Explicit Content Detection| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account| 0 count to 1,000,000 count$0.25 / 1,000 count, per 1 month / account1,000,000 count and above$0.05 / 1,000 count, per 1 month / account  
  
### 

Document SKUs Pricing

Feature / SKU| Rate| Status  
---|---|---  
PDF Classification*| Free| Public Preview (until GA later this year)  
  
_* PDF Classification usage will be limited to 100M objects total per customer during the Public Preview period_

### 

Capacity

No explicit workload size limitations exist, but all workloads are subject to capacity availability. Please note, workloads may be delayed when capacity is limited.

### 

Related Storage & Management Pricing

In addition to enrichment feature SKUs, associated storage, metadata context, and dataset management infrastructure rates may apply, such as:

  * Object Context Binding Fee
  * Object Context Extended Data
  * Storage Intelligence Object Management
  * Storage Insights Dataset Storage
  * Standard GCS Object Storage
  * Storage Operations Fees



### 

End-to-End TCO Pricing Example

Below is a total cost of ownership (TCO) calculation for an enterprise workload processing **10,000,000 image objects per month** using both Image Object Detection and Image Labeling, alongside associated context binding and storage intelligence infrastructure.

Itemized Line-Item Calculations

  * **Image Object Detection:**
  * First 1,000,000 objects: 1,000 × $0.25 = $250.00
  * Next 9,000,000 objects: 9,000 × $0.05 = $450.00
  * Subtotal: **$700.00**
  * **Image Labeling:**
  * First 1,000,000 objects: 1,000 × $0.25 = $250.00
  * Next 9,000,000 objects: 9,000 × $0.05 = $450.00
  * Subtotal: **$700.00**
  * **Object Context Binding Fee:** 10 million contexts × $3.00 / million = **$30**
  * **Storage Intelligence Object Management:** 10 million objects × $2.50 / million = **$25 / month**
  * **Storage Insights Dataset Storage:** 10 GiB dataset × $0.02 / GiB = **$0.20**



Component| One-time fee| Monthly Recurring  
---|---|---  
Image Object Detection| $700.00|   
Image Labeling| $700.00|   
Object Context Binding Fee| | $30  
Storage Intelligence Object Management| | $25  
Storage Insights Dataset Storage| | $0.20  
**Total**| **$1,400.00**| **$55.20**  
  
## 

Pricing notes

  * Storage and network usage are calculated in  _JEDEC binary gigabytes_ (GB), also known as  _IEC gibibytes_ (GiB), where 1 JEDEC GB is 230 bytes. Similarly, 1 JEDEC TB is 240 bytes, or 1024 JEDEC GBs.
  * When rewriting or copying data from one Cloud Storage bucket to another, [inter-region replication charges](https://docs.cloud.google.com/storage/pricing#inter-region-replication), if applicable, are billed to the billing account associated with the destination bucket. All other applicable charges are billed to the billing account associated with the source bucket.
  * [Data transfer costs](https://docs.cloud.google.com/storage/pricing#network) and [retrieval fees](https://docs.cloud.google.com/storage/pricing#retrieval-fees) are based on the amount of data accessed, not the size of the entire object. For example, if you request only the first 8 MB of a 100 MB Nearline storage object or if the download connection is broken after 8 MB is served, the data transfer cost and the retrieval fee are based on 8 MB.
  * Charges accrue daily, but Cloud Storage bills you only at the end of the billing period. You can view unbilled usage in [your project's billing page](https://console.cloud.google.com/billing) in the Google API console.
  * For compressed objects that are [transcoded](https://cloud.google.com/storage/docs/transcoding) during download, storage rates are based on the compressed size of the object. [Data transfer rates](https://docs.cloud.google.com/storage/pricing#network) are based on the uncompressed size of the object.
  * For buckets with [Object Versioning](https://cloud.google.com/storage/docs/object-versioning) enabled, each noncurrent version of an object is charged at the same rate as the live version of the object.
  * Cloud Storage also has the storage class [**Durable Reduced Availability (DRA) storage**](https://cloud.google.com/storage/docs/storage-classes#legacy); however, you should use Standard storage in favor of DRA. Standard storage has lower [pricing for operations](https://docs.cloud.google.com/storage/pricing#operations-charges) but otherwise has the same price structure. Standard storage also provides better performance, particularly in terms of availability.
  * There are no extra costs for using the [Storage Transfer Service](https://cloud.google.com/storage-transfer); however, normal Cloud Storage and external provider costs apply when using the Storage Transfer Service. See [Storage Transfer Service pricing](https://cloud.google.com/storage-transfer/pricing) for a list of potential costs.
  * [Pricing updates](https://cloud.google.com/storage/pricing-announce) for Cloud Storage took effect on October 1, 2022 and on April 1, 2023.



## 

Cloud Storage Always Free usage limits

As part of the [Google Cloud Free Tier](https://cloud.google.com/free), Cloud Storage provides resources that are free to use up to specific limits. These usage limits are available both during and after the free trial period. If you are no longer in the free trial period, usage beyond these Always Free limits is charged according to the [pricing tables above](https://docs.cloud.google.com/storage/pricing#pricing-tables).

Resource| Monthly Free Usage Limits1  
---|---  
Standard storage| 5 GB-months  
Class A Operations| 5,000  
Class B Operations| 50,000  
Data transfer| 100 GB from North America to each Google Cloud Data transfer destination (Australia and China excluded)  
  
1Cloud Storage Always Free quotas apply to usage in US-WEST1, US-CENTRAL1, and US-EAST1 [regions](https://cloud.google.com/storage/docs/bucket-locations#location-r). Usage is aggregated across these 3 regions. Always Free quotas do not apply to Rapid Storage class. Always Free is subject to change. Please see our [FAQ](https://cloud.google.com/free/docs/frequently-asked-questions) for eligibility requirements and other restrictions.

To prevent getting billed for usage beyond the Always Free usage limits, you can [set API request caps](https://cloud.google.com/apis/docs/capping-api-usage).

## 

Usage Policies

The use of this service must adhere to the Google Cloud [Terms of Service](https://cloud.google.com/terms) and [Program Policies](https://cloud.google.com/terms/aup), as well as Google's [Privacy Policy](https://www.google.com/privacypolicy.html).

## What's next

  * Visit the [Cloud Storage documentation](https://cloud.google.com/storage/docs/introduction).
  * Explore [Cloud Storage pricing examples](https://cloud.google.com/storage/pricing-examples).
  * Get started with Cloud Storage by following the [Quickstart using the Console](https://cloud.google.com/storage/docs/discover-object-storage-console).
  * Get started with Cloud Storage using a [Cloud Storage client library](https://cloud.google.com/storage/docs/reference/libraries).
  * Learn about [Cloud Storage solutions and use cases](https://cloud.google.com/architecture?text=Cloud%20Storage).



## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

Contact sales[](https://cloud.google.com/contact?direct=true)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact)



 _search_ _send_




[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/storage/pricing&hl=en-US&prompt=select_account&service=cloudconsole)

Start free[](https://console.cloud.google.com/freetrial)

Start free[](https://console.cloud.google.com/freetrial)

Contact us[](https://cloud.google.com/contact)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)




  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)




  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)




  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)




close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure Modernization
  * Productivity and Collaboration
  * Security
  * Startups and SMB



See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)


  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)


  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)


  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)


  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)


  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)


  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)


  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)


  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)


  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)


  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)


  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)


  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationModernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Application Modernization with AIAI-assisted code refactoring, assessment, and transformation for legacy applications.](https://cloud.google.com/solutions/application-modernization-with-ai)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Mainframe ModernizationAutomated tools and AI-driven guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)


  * [Database ModernizationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Data Lake ModernizationUnify and govern multimodal data on an open, high-performance cloud data lake.](https://cloud.google.com/solutions/data-lakehouse)


  * [Data Warehouse ModernizationMigrate and modernize your enterprise data warehouse for serverless analytics and AI.](https://cloud.google.com/solutions/data-migration)


  * [APIsUnlock legacy applications and build new digital channels using APIs and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [Platform EngManaged services and golden paths to build, manage, and scale internal developer platforms.](https://cloud.google.com/solutions/platform-engineering)


  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)


  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Gemini for enterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)


  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)


  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)


  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)


  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)


  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)


  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)


  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)


  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)


  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)


  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)


  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)


  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)


  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)


  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)


  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)


  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)


  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)


  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)


  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Rapid Migration and Modernization Program (RaMP)End-to-end migration program to simplify and accelerate your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Data Center ExitsMigration solutions for moving VMs, apps, databases, and workloads out of data centers.](https://cloud.google.com/solutions/data-center-migration)


  * [Application Modernization & MigrationDiscovery, assessment, and migration tools for moving and modernizing applications.](https://cloud.google.com/solutions/application-migration)


  * [Database Modernization & MigrationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Cross-Cloud NetworkingSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)


  * [High Performance Computing (HPC)Compute, storage, and networking options to support any high-performance workload.](https://cloud.google.com/solutions/hpc)


  * [VMwareFully managed, native VMware Cloud Foundation software stack on Google Cloud.](https://cloud.google.com/vmware-engine)


  * [SAPCertified infrastructure and AI solutions for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)


  * [WindowsTools, licenses, and partner solutions for running enterprise Windows workloads.](https://cloud.google.com/windows)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)


  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)


  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)


  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)


  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)


  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)


  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)


  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)


  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)


  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)


  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)


  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)



close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3



See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)


  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)


  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)


  * [Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)


  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)


  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)


  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)


  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)


  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)


  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)


  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)



  * Business Intelligence


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)


  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)


  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)


  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)


  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)


  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)


  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)


  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)


  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)


  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)


  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)


  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)


  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)


  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)


  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)


  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)


  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)


  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)


  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)


  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)


  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)


  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)


  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)


  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)


  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)


  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)


  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)



  * Hybrid and Multicloud


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)


  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)


  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)



  * Industry Specific


  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)


  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)


  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)


  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)


  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)


  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)


  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)


  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)


  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)


  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)


  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)


  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)


  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)


  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)


  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)


  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)


  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)


  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)



  * Media Services


  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)


  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)


  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)


  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)


  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)


  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)


  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)


  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)


  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)


  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)


  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)


  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)


  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)


  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)


  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)


  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)


  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)


  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)


  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)


  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)


  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)


  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)


  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)


  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)


  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)


  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)



  * Productivity and Collaboration


  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)


  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)


  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)


  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)


  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)


  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)


  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)


  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)


  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)


  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)


  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)


  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)


  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)


  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)


  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)


  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)


  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)


  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)


  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)


  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)


  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)



close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)




  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)




  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)




  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)




close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)




  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)




  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)




  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)




close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
    * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
    * arrow_forward
  * [Products](https://cloud.google.com/products)
    * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
    * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
    * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)



  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)


  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Application Modernization with AI](https://cloud.google.com/solutions/application-modernization-with-ai)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Mainframe Modernization](https://cloud.google.com/solutions/mainframe-modernization)
  * [Database Modernization](https://cloud.google.com/products/databases)
  * [Data Lake Modernization](https://cloud.google.com/solutions/data-lakehouse)
  * [Data Warehouse Modernization](https://cloud.google.com/solutions/data-migration)
  * [APIs](https://cloud.google.com/solutions/apis-and-applications)
  * [Platform Eng](https://cloud.google.com/solutions/platform-engineering)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini for enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Rapid Migration and Modernization Program (RaMP)](https://cloud.google.com/solutions/cloud-migration-program)
  * [Data Center Exits](https://cloud.google.com/solutions/data-center-migration)
  * [Application Modernization & Migration](https://cloud.google.com/solutions/application-migration)
  * [Database Modernization & Migration](https://cloud.google.com/products/databases)
  * [Cross-Cloud Networking](https://cloud.google.com/solutions/cross-cloud-network)
  * [High Performance Computing (HPC)](https://cloud.google.com/solutions/hpc)
  * [VMware](https://cloud.google.com/vmware-engine)
  * [SAP](https://cloud.google.com/solutions/sap)
  * [Windows](https://cloud.google.com/windows)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)


  * Featured Products
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)


  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)


  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)


