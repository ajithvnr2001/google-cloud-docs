---
url: https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket/
title: Rapid Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:12.172518+00:00
---

# Rapid Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Rapid Bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Rapid Bucket, a capability that lets you store objects in the [Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid) by setting a zone as a [bucket's location](https://docs.cloud.google.com/storage/docs/locations). This approach lets you colocate your data storage with your compute resources, which delivers significantly lower latency and higher throughput compared to other storage classes in Cloud Storage. Workloads in other zones and regions can also access the bucket, with performance relative to the network distance.

To create a zonal bucket using Rapid Bucket, see [Create zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets). You can view the list of supported locations in [Zones](https://docs.cloud.google.com/storage/docs/locations#location-z). To read and append to objects in zonal buckets, see [use objects in zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets).

For Rapid Bucket to be enabled on a bucket, the bucket must also have [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) and [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled.

## Capabilities and benefits

Rapid Bucket is built to remove storage bottlenecks and is ideal to use for your most data-intensive applications, such as AI/ML and data analytics. Rapid Bucket supports sub-millisecond latency, up to 15 TB/s of aggregate throughput, and 20 million queries per second (QPS). The ultra-low latency allows for instantaneous data retrieval and empowers real-time inference applications to perform at scale. The massive throughput and high QPS help keep your expensive GPU clusters fully saturated, dramatically reducing model training times.

In addition to providing low latency and high throughput, zonal buckets enable you to do the following:

  * Append to objects in the zonal bucket without performing a full object rewrite

  * Open objects and maintain a stream as you perform operations, letting you accelerate subsequent reads and writes




### Use cases

Rapid Bucket is most suitable for AI/ML workloads or other data-intensive workloads. Some examples of such workloads are model checkpointing, evaluation, and serving, as well as logging and messaging queues. It can also be used for streaming data or to provide storage for databases.

To take full advantage of the low latency and high throughput provided by Rapid Bucket, make sure to [enable gRPC direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity).

## Rapid Bucket terminology

The Cloud Storage documentation uses the following terms:

  * **Rapid Bucket** : The product that enables buckets to be created with a zonal location and the Rapid storage class.

  * **Rapid storage** : The storage class that offers the highest data access and I/O operation performance in Cloud Storage. When you use Rapid Bucket, you create a bucket that uses Rapid storage. For more information about Rapid storage, see [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).

  * **Zonal bucket** : A bucket that's located in a zone. Objects in zonal buckets are always stored in Rapid storage and are appendable.




## Access to objects in zonal buckets

To get the performance benefits of a zonal bucket, make sure to open objects for streaming and maintain a stream as you perform operations on the objects. When you establish and maintain a stream, you can perform subsequent read or write operations to the object with very low latency. For example, when reading a Parquet file, you can perform both the initial read of the file's metadata (the footer) and the subsequent read of specific rows within a single request. This approach is more efficient than using separate requests for each step.

Once established, object streams are kept open by default when you access zonal bucket objects using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) or the Cloud Storage client libraries.

You can open multiple read streams to an object from any number of hosts. There's no limitation on the number of read streams you can establish to an object.

## Appending objects

You can append data to objects in zonal buckets. When you make appends to objects, the following semantics apply:

  * Appendable objects appear in the bucket namespace as soon as you start writing to them and can be read while still being written.

  * There are no restrictions on the number of appends you can make to an object or the number of bytes you can append at a time. You can make appends up until an object reaches its maximum size of 5 TiB.

  * An object's size will grow in real-time as new appends are permanently written or flushed. When you establish a read stream, you should anticipate a minimal delay in the object's size getting updated.

  * Appendable objects can only have one writer at a time. If a new write stream is established for an object that already has an existing write stream, an error is returned from Cloud Storage to the original stream, and the original stream will no longer be permitted to write. The new writer can resume appending from the last persisted offset without other interleaved appends to the object.




## Finalizing objects

After an object is finalized, you can no longer append to it, but you can still overwrite the object with a new version. The metadata of a finalized object is still mutable; for example, new tags can be added and the object can be renamed.

## Mounting zonal buckets

You can mount and access zonal buckets by using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) or the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver). Make sure to use Cloud Storage FUSE version 3.7.2 or later. To use the Cloud Storage FUSE CSI driver, your Google Kubernetes Engine version must be 1.35.0-gke.3047001 or later.

## Supported tools

You can work with zonal buckets by using most of the [tools for Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction#tools). However, the following limitations apply:

  * You can't write to zonal buckets by using standard client library APIs that are meant for non-zonal buckets. To write to zonal buckets, you must modify your code to use supported APIs for zonal buckets. To learn which APIs you should use, refer to the code samples for your client library in [Use objects in zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets).

  * You can read objects in zonal buckets by using the JSON API, the XML API, or gRPC, including non-bidirectional gRPC read methods such as `ReadObject`.

  * Support for writing to zonal buckets varies by API:

    * **gRPC** : When using gRPC, you can only write to zonal buckets by using the `BidiWriteObject` API. Appendable objects are only supported by the `BidiWriteObject` RPC call in appendable mode. Non-bidirectional gRPC write methods, such as `WriteObject`, aren't supported for zonal buckets.

    * **XML API** : You can write to zonal buckets by using the XML API, except for XML multipart uploads.

    * **JSON API** : You can't write to zonal buckets by using the JSON API.

  * Rapid Bucket is supported by the [GCSFS Python library](https://github.com/fsspec/gcsfs) versions 2026.3.0 and later.

  * Google Cloud CLI limitations:

    * **Minimum supported Google Cloud CLI version** : The minimum version of the gcloud CLI that supports zonal buckets is 553.0.0. Earlier versions aren't compatible with zonal buckets. We recommend using the [latest version of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) to get the latest features and bug fixes. Sliced object downloads and performance optimizations for zonal buckets require gcloud CLI version 583.0.0 or later. For more information, see [Tune gcloud CLI performance for zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/tune-gcloud-performance).

    * **Visibility of incomplete uploads** : Unlike buckets in other storage classes, where objects only appear in the namespace after an upload completes, partially uploaded objects in zonal buckets are immediately visible. If a Google Cloud CLI upload command fails or is interrupted, you might see incomplete objects in your bucket. You can still resume these uploads by re-running the command.

    * **Object overwrites** : Standard Google Cloud CLI behavior applies to zonal buckets: when you overwrite an object, if a file or object with the same name exists at the destination, the Google Cloud CLI `cp`, `mv`, and `rsync` commands will overwrite it by default. To prevent overwrites, use the `--no-clobber` flag. When using the Google Cloud CLI, appending data to an existing object is not supported; the entire source must be re-uploaded.

    * **Object finalization** : Objects uploaded to a zonal bucket by using the Google Cloud CLI might occasionally experience a brief delay before the object's metadata is fully synchronized. Because Cloud Storage uses an eventually consistent model, attempting to download an object immediately after upload can result in a hash mismatch error if the metadata is not yet updated.

If a download fails with a hash mismatch error shortly after an upload, retry the command. Downloads either succeed in full or fail explicitly; partial or corrupted downloads won't occur silently.

  * **Checksum validation performance** : Zonal buckets rely exclusively on CRC32C for data validation, allowing the system to perform checksumming per chunk and for the entire upload or download. By default, Google Cloud CLI uses the `google-crc32c` Python library, which comes pre-installed with Google Cloud CLI. However, if you are using a non-bundled Python installation, you must explicitly install the `google-crc32c` library from [PyPI](https://pypi.org/project/google-crc32c/). Otherwise, Google Cloud CLI falls back to the `gcloud-crc32c` binary, which might lead to slower performance for per-chunk CRC computation.




### Incompatibilities

Zonal buckets are incompatible with the following products and services:

  * Data upload and management

    * Rapid Cache

    * Autoclass

    * Bucket Lock

    * Composite objects

    * XML multipart uploads

    * Object holds

    * The Object Lifecycle Management `SetStorageClass` action

    * Object Retention Lock

    * Bucket relocations

    * Resumable uploads

    * Object rewrites

    * Requester Pays

  * Metadata

    * Objects in zonal buckets don't have an MD5 hash.

    * The metadata properties associated with unsupported features and products don't appear in the resource representation of a zonal bucket or an appendable object, or are otherwise unwriteable. For example:

      * The `softDeleteTime` and `hardDeleteTime` metadata properties don't appear in the resource representation of the [`Objects` resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) because soft delete isn't supported for objects in zonal buckets.

      * The `storageClass` metadata of objects in zonal buckets always have a value of `RAPID` and can't be rewritten because zonal buckets must always use the Rapid storage class.

  * Access control

    * Object-level access control lists (ACLs)

    * CORS configurations

    * Customer-supplied encryption keys (CSEK)

    * HMAC keys

  * Data protection and disaster recovery

    * Object Versioning

    * Soft delete

    * Cross-bucket replication

  * Other Google Cloud services

    * BigQuery



## Quotas

Each zone per project has a default storage capacity quota. Each zone per project also has a default egress quota from Cloud Storage to Google services. To view these quotas, see [Quotas and limits](https://docs.cloud.google.com/storage/quotas).

To learn how to monitor your data egress usage and request more bandwidth, see [Bandwidth usage monitoring](https://docs.cloud.google.com/storage/docs/bandwidth-usage).

## Pricing

Using Rapid Bucket incurs charges for data storage, operations, and networking. For more information, see [Pricing](https://docs.cloud.google.com/storage/pricing).

## Best practices

To optimize performance and resource utilization when working with zonal buckets, consider the following best practices:

  * **Optimize object reads** : When reading objects from zonal buckets by using the gcloud CLI, the CLI automatically applies default concurrency and slicing configurations. To further tune these settings for a specific workload, see [Tune gcloud CLI performance for zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/tune-gcloud-performance).

  * **Cloud Storage FUSE file handles** : To help optimize performance when using zonal buckets with Cloud Storage FUSE, maintain an open file handle to objects in your mounted zonal bucket and use it for multiple operations. This practice improves performance because Cloud Storage FUSE avoids unnecessary network round trips for repeated reads.

  * **Optimize parallel write latency** : If you maintain your own gRPC parallel write logic, consider using a pool of pre-opened writers with unfinalized objects to move stream setup out of the write path. A pool of pre-opened writers opens object streams and creates new, empty appendable objects in the bucket before your application needs them. For more information, see [Optimize write latency](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets#optimize-write-latency).




## What's next

  * Learn how to [create zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).
  * Learn how to [use objects in zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets).
  * [Tune gcloud CLI performance for zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/tune-gcloud-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
