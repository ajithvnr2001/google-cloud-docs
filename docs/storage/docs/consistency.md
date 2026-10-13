---
url: https://docs.cloud.google.com/storage/docs/consistency/
title: Cloud Storage consistency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:41.044600+00:00
---

# Cloud Storage consistency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/consistency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage consistency Stay organized with collections  Save and categorize content based on your preferences. 

This page describes strongly consistent and eventually consistent Cloud Storage operations. Consistency behavior determines when changes to objects, buckets, and access permissions take effect. For cacheable, publicly readable objects, you control the consistency of operations.

## Strongly consistent operations

Cloud Storage provides strong global consistency for the following operations:

  * Bucket listing
  * Bucket read-after-create
  * Bucket read-after-metadata-update
  * Bucket read-after-delete
  * Object read-after-write
  * Object read-after-metadata-update
  * Object read-after-delete
  * Object listing



When you write an object to Cloud Storage, such as when you upload, compose, or copy an object, the object is immediately available for reading and metadata operations as soon as you receive a success response to your write request. This behavior is true for all buckets and storage classes, and the consistency model applies to both creating new objects and replacing existing objects. Cloud Storage also offers read-after-create, read-after-metadata-update, read-after-delete, and listing consistency for resources such as folders and managed folders.

Because writes are strongly consistent, you never receive a `404 Not Found` response or stale data for an object read-after-write or object read-after-metadata-update operation, even for buckets located in [dual-regions or multi-regions](https://docs.cloud.google.com/storage/docs/locations#available-locations). In the rare event where your data has not yet been [replicated across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy), but the location your object was first written to becomes unavailable, attempts to access the object return a [retryable](https://docs.cloud.google.com/storage/docs/retry-strategy) `500` error response.

Strong global consistency also extends to deletion operations on objects. If a deletion request succeeds, an immediate attempt to download the object or its metadata results in a `404 Not Found` status code. You get the `404` error because the object no longer exists after the delete operation succeeds.

Bucket listing and object listing are strongly consistent: when you create a bucket or object and then immediately perform the relevant `list` operation, the newly created bucket or object appears in the returned list.

**Important:** Cached objects that are publicly readable might not exhibit strong consistency. See Cache control and consistency for details.

For buckets, while metadata updates are strongly consistent for read-after-metadata-update operations, the resulting configuration changes may take time to propagate. For example, if you enable [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning) on a bucket, you should wait at least 30 seconds before deleting or replacing objects.

Similarly for [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys), there is a delay of up to 3 minutes between when you request to change the key state and when the state change takes effect. For example, if you [disable an HMAC key](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys#update), you should wait at least 3 minutes before making a request to delete the key, because attempts to do so in the first 3 minutes could fail.

## Eventually consistent operations

The following operations are eventually consistent:

  * Granting access to or revoking access from resources.
  * Recreating buckets after deletion.



It typically takes about a minute for these operations to take effect. In some cases, it might take several minutes longer.

As an example of behavior that can arise from eventual consistency, if you remove a user's access to a bucket, this change is immediately reflected in the metadata for the bucket; however, the user may still have access to the bucket for a short period of time.

Buckets that are recreated after deletion might take several minutes to become accessible.

## Cache control and consistency

Cached objects that are publicly readable might not exhibit strong consistency. If you allow an object to be cached, and the object is in the cache when it is updated or deleted, the cached object is not updated or deleted until its cache lifetime expires.

The cache lifetime of an object is defined by the [`Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control) associated with the object. The `Cache-Control` metadata can be set using a `Cache-Control` request header included in the initial upload of the object, or in a subsequent [update to the metadata of the object](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit). Because you control the `Cache-Control` metadata, you also control the degree to which cached objects are consistent. Moreover, while requests for the object can include their own `Cache-Control` header, these headers are ignored by Cloud Storage if they're set to avoid cached content.

**Note:** If you do not specify a cache lifetime, a publicly accessible object can be cached for up to 60 minutes.

## Atomic operations

Cloud Storage provides atomicity guarantees for most operations involving individual objects, such as uploading an object, updating an object's metadata, overwriting an object, and deleting an object. For example, if an object upload is interrupted due to a network failure, no partial data is uploaded to the bucket. The object only becomes visible in the bucket once the entire upload has successfully completed and the server has sent a success response.

Batch requests, which aggregate individual operations into a single request, are not atomic, because it's possible for some of the operations contained within the batch to fail while others succeed.

[Caching](https://docs.cloud.google.com/storage/docs/caching) can cause you to receive stale versions of an object, and if you [perform ranged reads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads) without specifying a generation number, your data might become corrupted if the object becomes overwritten between successive ranged reads. As a best practice, use [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to make sure you're fetching the correct object version.

## What's next

  * Learn about using [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to prevent race conditions.
  * Learn more about [caching in Cloud Storage](https://docs.cloud.google.com/storage/docs/caching).
  * Learn about [request rate and access distribution guidelines](https://docs.cloud.google.com/storage/docs/request-rate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
