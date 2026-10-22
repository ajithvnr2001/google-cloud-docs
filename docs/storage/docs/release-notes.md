---
url: https://docs.cloud.google.com/storage/docs/release-notes/
title: Cloud Storage release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:49.759696+00:00
---

# Cloud Storage release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Resources ](https://docs.cloud.google.com/storage/docs/resources)



Send feedback 

#  Cloud Storage release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Storage. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/storage-release-notes.xml) directly. 

## October 13, 2026

Feature

Object enrichments is now available in [Preview](https://cloud.google.com/products#product-launch-stages). When you configure object enrichments, Cloud Storage applies Google's pre-trained machine learning models to eligible images and PDF documents in your buckets and attaches the resulting metadata to your objects as [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts). You can inspect enrichments on individual objects or query them at scale in BigQuery by using [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema). For more information, see [About object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview) and [Configure object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments).

Feature

Object contexts with [extended data](https://docs.cloud.google.com/storage/docs/object-contexts#extended-data) are available in [Preview](https://cloud.google.com/products#product-launch-stages). Google services attach these contexts to your objects during automated analysis, such as machine learning labeling. To retrieve a context and its extended data, use the [`viewFullContext`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext) JSON API method.

Feature

Storage Insights datasets include the Object Contexts Catalog view (`object_contexts_catalog_view`), which you can use to analyze object contexts in BigQuery. For more information, see [Object contexts catalog](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema) and [Analyze object contexts](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-contexts).

## September 30, 2026

Feature

Cloud Storage client libraries now provide automated, end-to-end checksumming by default for object read and write operations to help maintain data integrity from client to storage. For more information, see [data validation](https://docs.cloud.google.com/storage/docs/data-validation#client-validation-writes).

## September 10, 2026

Feature

Storage Intelligence advisor is now [generally available](https://cloud.google.com/products#product-launch-stages). Storage Intelligence advisor lets you monitor and manage your Cloud Storage environment at scale across organizations, folders, and projects. For more information, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview).

## September 03, 2026

Feature

You can use Storage batch operations to do the following:

  * Select objects dynamically across a project by using [Common Expression Language (CEL) filters](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference) based on metadata in your [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets), without manual CSV manifests or BigQuery export queries.
  * Target objects across up to 1,000 buckets in a single batch job.
  * Transition objects in bulk to different storage classes.
  * Patch object access control lists (ACLs) in bulk to update or remove permissions.
  * Use dry run to validate job configurations across multiple buckets, and create jobs directly from a dry run to process the same validated objects.



For more information, see [Storage batch operations overview](https://docs.cloud.google.com/storage/docs/batch-operations/overview) and [Create and manage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## August 21, 2026

Feature

Rapid Cache supports prefix-level ingest-on-write filtering, allowing you to selectively ingest objects that match specific prefixes rather than ingesting all objects written to a bucket.

For more information, see [Ingesting data on write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write).

## August 17, 2026

Feature

If you delete your project, buckets that have soft delete enabled are now retained for a limited amount of time before being permanently deleted. If you restore a deleted project during this time period, these buckets are restored to the state that they were in when the project was deleted.

For more information about soft delete and the restoration window, see [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete).

## July 20, 2026

Feature

Object Lifecycle Management conditions for [`sizeAboveBytes` and `sizeBelowBytes`](https://docs.cloud.google.com/storage/docs/lifecycle#size-above-below-bytes) let you define a minimum and maximum size threshold for lifecycle actions.

## June 17, 2026

Feature

When you [create composite objects](https://docs.cloud.google.com/storage/docs/composing-objects), you can delete the temporary source objects as part of the composition process.

## May 28, 2026

Breaking

As of August 26, 2026, in buckets with hierarchical namespace enabled, the [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) `Delete` action will delete empty folders when the empty folder meets all of the conditions in the lifecycle rule.

## April 29, 2026

Feature

You can manage object contexts in the Google Cloud Console. To learn more, see [Use object contexts](https://docs.cloud.google.com/storage/docs/use-object-contexts).

## April 27, 2026

Feature

Cloud Storage now offers support for AI zones. To learn more, see [AI zones](https://docs.cloud.google.com/storage/docs/ai-zones).

## April 20, 2026

Feature

Cloud Storage Model Context Protocol (MCP) server is [generally available](https://cloud.google.com/products#product-launch-stages). You can connect to Cloud Storage from AI applications using the server. It lets AI applications and agents create buckets, retrieve object metadata, read and write object data, and list buckets and objects. For more information, see [Use the Cloud Storage MCP server](https://docs.cloud.google.com/storage/docs/use-cloud-storage-mcp) and [Cloud Storage MCP reference](https://docs.cloud.google.com/storage/docs/reference/mcp).

## April 08, 2026

Feature

You can delete up to 1,000 objects in a single request by using the Cloud Storage multi-object delete XML API. If you use Amazon S3-compatible tools or libraries, you can point your request to the Cloud Storage endpoint to use this feature with your existing workflows. For more information, see [Delete objects](https://docs.cloud.google.com/storage/docs/deleting-objects) and [Delete multiple objects](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket).

## April 06, 2026

Feature

You can now use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) to update [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) for multiple objects in a single job. You can clear all existing contexts from the specified objects, remove contexts with specific keys, or update and insert new context key-value pairs. For more information, see [Create and manage batch operation jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

Feature

[Object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) are now [generally available](https://cloud.google.com/products#product-launch-stages). You can attach key-value pairs to your objects to categorize, track, and search your data. Object contexts are preserved by default during copy, rewrite, and compose operations. You can help control this behavior by using the [`dropContextGroups`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy#dropContextGroups) JSON API parameter or by providing new contexts in the request.

## April 02, 2026

Feature

You can configure which encryption types are allowed or prohibited for creating new objects in a bucket. For more information, see [Enforce or restrict the encryption types for a bucket](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types).

## March 31, 2026

Feature

You can now use Storage Insights datasets to help manage your data security and compliance. The ability to [identify publicly accessible objects](https://docs.cloud.google.com/storage/docs/insights/datasets#public-accessible-objects) is now [generally available](https://developers.google.com/maps/launch-stages#ga). Additionally, new fields in bucket and object metadata schemas, such as `encryption`, `retentionPeriod`, `encryptionType`, and `retentionExpirationTime`, help you audit encryption configurations and monitor data retention policies. For more information, see [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) and [Dataset tables and schemas](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas).

## March 24, 2026

Announcement

Anywhere Cache has been renamed to Rapid Cache.

## March 12, 2026

Change

Object uploads that use customer-managed encryption keys (CMEK) now fail if the Cloud Storage service agent lacks the necessary IAM role to decrypt the object. For steps to grant the required role, see [Assign a Cloud KMS key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access).

## March 10, 2026

Feature

Rapid Bucket is now [generally available](https://developers.google.com/maps/launch-stages#ga). Rapid Bucket lets you store objects in the Rapid storage class by defining a zone as a bucket's location. This architecture optimizes data access and I/O performance between your storage and compute resources. Rapid Bucket is most suitable for data-intensive workloads like AI/ML and high-scale data analytics.

For more information, see [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) and [Create zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).

## March 06, 2026

Feature

You can now [identify publicly accessible objects](https://docs.cloud.google.com/storage/docs/insights/datasets#public-accessible-objects) ([preview](https://cloud.google.com/products#product-launch-stages)) by using Storage Insights datasets. The object metadata schema includes fields that provide the public access status of your objects, which lets you understand, organize, and manage publicly accessible objects at scale.

## March 05, 2026

Feature

You can now analyze object data and metadata from your Storage Insights datasets by using BigQuery `ObjectRef` functions. The `ref` column in the dataset contains a reference to the Cloud Storage object which you can use with `ObjectRef` functions to analyze object content. For example, you can build queries to help detect sensitive information in documents or to generate image descriptions. For more information, see [Analyze object data and metadata using BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-data).

## January 30, 2026

Announcement

Object change notification is deprecated on January 30, 2026. To generate notifications for changes to objects, use [Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/migrate-to-pub-sub-notifications) instead.

## January 28, 2026

Feature

Previously, when [listing buckets](https://docs.cloud.google.com/storage/docs/listing-buckets) by using the client libraries, JSON API, or RPC API, the request returned an error if some buckets couldn't be reached because a location was temporarily unavailable. You can now use a partial success option to return a list of buckets that are available, as well as the names of any buckets that can't be reached.

## January 21, 2026

Feature

Bucket relocation with write downtime now supports completed multipart uploads. If a multipart upload is started before relocation begins and is completed before the final synchronization step, the objects are successfully relocated. In-progress multipart uploads continue to block the final synchronization step until they are either completed or cancelled. For more information, see [Bucket relocation overview](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).

## January 20, 2026

Feature

Cloud Storage now offers support in the Thailand, Bangkok (`asia-southeast3`) region. To learn more about supported locations, see [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations).

## January 16, 2026

Feature

You can now use [dry run](https://docs.cloud.google.com/storage/docs/batch-operations/overview#dry-run) mode to simulate storage batch operations jobs without modifying or deleting data. Dry run helps you to validate your job configuration before running the actual operation.

To learn how to configure a dry run job, see [Create and manage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## January 15, 2026

Feature

When you [bulk restore soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#bulk-restore), you can restore objects that were live at a specific time. You can also choose the objects to restore based on the object creation time.

## December 22, 2025

Libraries

### Java

#### [2.61.0](https://github.com/googleapis/java-storage/compare/v2.60.0...v2.61.0) (2025-12-15)

##### Features

  * Add support for partial success in ListBuckets for json ([#3415](https://github.com/googleapis/java-storage/issues/3415)) ([37ef7f3](https://github.com/googleapis/java-storage/commit/37ef7f3894a867257d5366ab36129043b9a884f8))
  * Modifying getters and setters to be more inline with s3 interface. ([0a8bbea](https://github.com/googleapis/java-storage/commit/0a8bbeaf8babd296fce0690421d2e480b361ca7e))
  * **mpu:** Breaking change modifying getters and setters in MPU to be more inline with s3 interface. ([66d54e2](https://github.com/googleapis/java-storage/commit/66d54e2dc36d90853bae4d529a620f45a7001487))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([511ff51](https://github.com/googleapis/java-storage/commit/511ff514410e55425e968ab900ac1b8825fe507a))



##### Dependencies

  * Update actions/checkout action to v6 ([d934ad9](https://github.com/googleapis/java-storage/commit/d934ad91aa1bf50e04870b1af747f1947fb2cbea))
  * Update actions/checkout action to v6 ([d99dd53](https://github.com/googleapis/java-storage/commit/d99dd53a0401f5460a63be7a6b927a27cdad0997))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20251118-2.0.0 ([f48fa3f](https://github.com/googleapis/java-storage/commit/f48fa3f1dc5feabd89be063b138804b83f722c0c))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20251118-2.0.0 ([#3427](https://github.com/googleapis/java-storage/issues/3427)) ([4612e72](https://github.com/googleapis/java-storage/commit/4612e72051d35b22135811a8723a65646a90d45e))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.2 ([90a71be](https://github.com/googleapis/java-storage/commit/90a71be0899d06995b515d875c65cdc5f852c7b0))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.2 ([#3424](https://github.com/googleapis/java-storage/issues/3424)) ([c989dc3](https://github.com/googleapis/java-storage/commit/c989dc3e65386e55bc25d2f6f63e499deda3fc69))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.59.0 ([f5d8337](https://github.com/googleapis/java-storage/commit/f5d8337ad556770a55cc260975e44e85e8e831b0))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.59.0 ([5480ce3](https://github.com/googleapis/java-storage/commit/5480ce347493ec425b675f462a42f45c22b06c28))
  * Update googleapis/sdk-platform-java action to v2.64.2 ([23494d7](https://github.com/googleapis/java-storage/commit/23494d79d3a2785c30c75f50fd3b0a03598c3599))
  * Update googleapis/sdk-platform-java action to v2.64.2 ([#3425](https://github.com/googleapis/java-storage/issues/3425)) ([fad2d7a](https://github.com/googleapis/java-storage/commit/fad2d7a780a084acd8ccdf2bb2f97a335c438594))



### Java

#### [2.62.0-rc1](https://github.com/googleapis/java-storage/compare/v2.61.0...v2.62.0-rc1) (2025-12-17)

##### Features

  * _breaking behavior_ rewrite Storage.blobAppendableUpload to be non-blocking and have improved throughput ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c3a0aaa](https://github.com/googleapis/java-storage/commit/c3a0aaa68f9ee64d850ef5d7cd1c7bea01113503))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([fac7839](https://github.com/googleapis/java-storage/commit/fac7839739bcf5fb0e63fb39b02b331206cc3630))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8332e1b](https://github.com/googleapis/java-storage/commit/8332e1b3636bdbbd4e550053725e7ab040bff463))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([e4688a0](https://github.com/googleapis/java-storage/commit/e4688a00b7f35a28dd079606b7fdd36851564834))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([b426e7d](https://github.com/googleapis/java-storage/commit/b426e7d3d57f0e147bfc4dda0319665130c970a1))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c601cca](https://github.com/googleapis/java-storage/commit/c601cca381881d4ef52b851fe8edd13037688b9e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c58fe1f](https://github.com/googleapis/java-storage/commit/c58fe1f62ebdaab1ea74de1d05c0b2e6500994bf))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([616256a](https://github.com/googleapis/java-storage/commit/616256aa5850e625faf6f74996dc40c911050952))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ba3af58](https://github.com/googleapis/java-storage/commit/ba3af58df8d296bfc6290107e595219472a16861))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([e12d2ad](https://github.com/googleapis/java-storage/commit/e12d2ad9bd301bbcb4ac227a8327fd1754205595))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([d6044a1](https://github.com/googleapis/java-storage/commit/d6044a1c47345b18a018829e272612bc5c52f4b9))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([eebc6c6](https://github.com/googleapis/java-storage/commit/eebc6c6700d2b94b320777c2bd68377570d3c6da))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([12507e2](https://github.com/googleapis/java-storage/commit/12507e2172b8b59b10e98eb8dda9d1c5050a647f))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([58557a0](https://github.com/googleapis/java-storage/commit/58557a054e52fde1c33b8817fbb3f36d41665d9f))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c109fdb](https://github.com/googleapis/java-storage/commit/c109fdbe515d62bf152bba9803fb25e388656a24))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([d98ecc7](https://github.com/googleapis/java-storage/commit/d98ecc7df39142ea90e51b47f42dffad0ac03c24))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([6858a9d](https://github.com/googleapis/java-storage/commit/6858a9dac8bd622b214c8b9fa9a180b95c2a092d))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([bb7e1b4](https://github.com/googleapis/java-storage/commit/bb7e1b45822741b7d3d470a1e0fa350a963841bf))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([e89ae27](https://github.com/googleapis/java-storage/commit/e89ae2757578adc099442e2b7844949c666468c8))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8beaa03](https://github.com/googleapis/java-storage/commit/8beaa0353f51846cd902ef1568bd1bb8b4936b68))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ff8fd8f](https://github.com/googleapis/java-storage/commit/ff8fd8fdbd78b7cf4b0dad70d93cd6aeaadb0a03))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([944e0bc](https://github.com/googleapis/java-storage/commit/944e0bc57be2e04df0358b85b43167fc4ea0bcfe))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([eb8c5c8](https://github.com/googleapis/java-storage/commit/eb8c5c896c758d36eb114143fb79be74f28f0232))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([50e4589](https://github.com/googleapis/java-storage/commit/50e4589dc0e6ab88fbe869ba4b3a959d2dcfec2b))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([a751971](https://github.com/googleapis/java-storage/commit/a7519715f73b11659608d97bf95eeb690e5f6a44))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([befff3b](https://github.com/googleapis/java-storage/commit/befff3b4b2a3b8da70b514f6489ae6a690e419c0))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ac950ad](https://github.com/googleapis/java-storage/commit/ac950ada45d0408199249a25f93e0c5b0a12ab12))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([f381795](https://github.com/googleapis/java-storage/commit/f3817950fb2ded13904c549718f6baeb73ad5e85))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([84ffb6d](https://github.com/googleapis/java-storage/commit/84ffb6d432e75daf89b4910af3c7f50a39dcb323))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([b95e51d](https://github.com/googleapis/java-storage/commit/b95e51d89101ea4683c944856cb7c19ad6b4b514))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([03aa3e7](https://github.com/googleapis/java-storage/commit/03aa3e735f941ec896c47d4d4ea1bf0700a0b626))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([23f9a79](https://github.com/googleapis/java-storage/commit/23f9a793b69d2d34abecb31f4628fc07923c5e2d))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([e2a3e3c](https://github.com/googleapis/java-storage/commit/e2a3e3c2ca8e323f0e99d2cc67ce1cd1b034a049))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([bee4308](https://github.com/googleapis/java-storage/commit/bee43087ec13eadca435ebccdca56d4ca39e5a57))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([28f2759](https://github.com/googleapis/java-storage/commit/28f27592df6b5a70db3e9cfabaa23ab2b3c15680))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([775ad24](https://github.com/googleapis/java-storage/commit/775ad240569c3b77eb3ab0df023313e675eddf4b))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([f29d825](https://github.com/googleapis/java-storage/commit/f29d825d1521fb3ca8fe94f5904df8e356e3e68e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([2e8a0ee](https://github.com/googleapis/java-storage/commit/2e8a0eef40df70fab703c199a3b5b58c645bb2df))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([5c2cf19](https://github.com/googleapis/java-storage/commit/5c2cf196c202d91618ebedf5ba7a26d8d21790d5))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([2431ee1](https://github.com/googleapis/java-storage/commit/2431ee1a350c9c47b5dfa6da20c4b5788eb9388f))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([aeb621a](https://github.com/googleapis/java-storage/commit/aeb621ad08ef6369dbeba369a2345ba9a50e5218))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3d2520d](https://github.com/googleapis/java-storage/commit/3d2520dd6686dd873a941ceabe602407ec7f8f96))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3e38109](https://github.com/googleapis/java-storage/commit/3e38109a734395cc9324e31d9473b3b7991232bc))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8453281](https://github.com/googleapis/java-storage/commit/8453281c53448323fb83f2dea076886c4a37ff92))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([4170803](https://github.com/googleapis/java-storage/commit/41708031863ea2b50b22c60d8a61f75a6c1f2de0))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([f8e54b5](https://github.com/googleapis/java-storage/commit/f8e54b532a09b39d7690763dda1da640b3012cdd))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([85049b9](https://github.com/googleapis/java-storage/commit/85049b97b3cc8a82bb28d75295e1cdf5e3cc06ae))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([2a92e35](https://github.com/googleapis/java-storage/commit/2a92e359ce1463306bef3415dde4af69ed515873))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3b195fe](https://github.com/googleapis/java-storage/commit/3b195fecc165896fc7654744e82247127e39e535))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ae31163](https://github.com/googleapis/java-storage/commit/ae31163618704a1c37394ccc5b4213773f149ac5))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([b1499d6](https://github.com/googleapis/java-storage/commit/b1499d6b64d82c54e339f2af86422ae0a8aa766b))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([1085216](https://github.com/googleapis/java-storage/commit/1085216acd5fc3191ff043615b0f0b52730e56e2))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3616097](https://github.com/googleapis/java-storage/commit/36160978c767c828921fabc1314c89a81eb612b9))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([6a80994](https://github.com/googleapis/java-storage/commit/6a8099482558b3486b008af632f18094e6461797))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([69d01d4](https://github.com/googleapis/java-storage/commit/69d01d41b731f6c03049c24b954704a672400cbd))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([fa0df98](https://github.com/googleapis/java-storage/commit/fa0df985586466f73aa7bca9a4982402aa802bc8))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3eec2e3](https://github.com/googleapis/java-storage/commit/3eec2e327f4aad1bb46f3389e76d02b55a31ee43))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([1bf497e](https://github.com/googleapis/java-storage/commit/1bf497e3ce2105734daa262589550aca29eee0f2))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([bc7a931](https://github.com/googleapis/java-storage/commit/bc7a931542b22589c39d0be0980eb116dbf2a0dc))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c6f5b57](https://github.com/googleapis/java-storage/commit/c6f5b57e3cdd3747121f50284bca7f823e34f329))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8d4d7a3](https://github.com/googleapis/java-storage/commit/8d4d7a3caed4711a59a9509347ed634a783e390a))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([affb14f](https://github.com/googleapis/java-storage/commit/affb14fbb2738c687a885ad4491e57da7808cb9b))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([09c426b](https://github.com/googleapis/java-storage/commit/09c426b42d4d72d547312e68428373bc6edfc585))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([af52279](https://github.com/googleapis/java-storage/commit/af5227949285419add4398e62dd7276e2e9038f4))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([72491e7](https://github.com/googleapis/java-storage/commit/72491e711054572d90c5b673a128bf5294f07daf))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([2968790](https://github.com/googleapis/java-storage/commit/2968790b77bae8751ae56c306e736c99409da8a7))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([a4d919e](https://github.com/googleapis/java-storage/commit/a4d919ed36d3095653b22abb9bc607e58d39ddaa))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([f437c0a](https://github.com/googleapis/java-storage/commit/f437c0a427d234a4d7afc486e1480e64695e7785))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ba70fd8](https://github.com/googleapis/java-storage/commit/ba70fd8495ee81081dd7a9acbf49b56d296b7d1a))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([95d46a5](https://github.com/googleapis/java-storage/commit/95d46a581be8f1b2aafc137257ddb8aa48009707))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([413d65f](https://github.com/googleapis/java-storage/commit/413d65fe73ae4f5e360f75b22a36b57b1aac1b87))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([52639da](https://github.com/googleapis/java-storage/commit/52639da2676476c734df496bd92054c62f60a226))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([961f3cb](https://github.com/googleapis/java-storage/commit/961f3cb7c1f83eff6a01c6e283f8c2faf47822ee))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([98dbb02](https://github.com/googleapis/java-storage/commit/98dbb02c8c8711219b087c6c702dbeeee5fdf27e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([cbc22f2](https://github.com/googleapis/java-storage/commit/cbc22f22f27f07f4b2ca6bc50890d13fdf715663))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([f7c37f5](https://github.com/googleapis/java-storage/commit/f7c37f576bd801ab15926aaeda6f676050a6a442))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([a7a8945](https://github.com/googleapis/java-storage/commit/a7a894505144333e9ad28fbe0faf840985414f07))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([26db9e3](https://github.com/googleapis/java-storage/commit/26db9e356c4c6b12d2defd587c169d34529ec37e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([3ca4123](https://github.com/googleapis/java-storage/commit/3ca4123a7c307246393f8f441e3b8d623806fe28))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8553cb9](https://github.com/googleapis/java-storage/commit/8553cb9d6153c48f0634a24bdbac9c9f1306e1dc))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([758756f](https://github.com/googleapis/java-storage/commit/758756fce213ad0fe8ef3127d2bb55b1e2f8a7aa))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([065d249](https://github.com/googleapis/java-storage/commit/065d2491cfb19a66bba36a97e2e80c37d6090240))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([61824e6](https://github.com/googleapis/java-storage/commit/61824e6a36b48b7caeb66b88436fa645a4a0f01a))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([67482f7](https://github.com/googleapis/java-storage/commit/67482f7a79eea2d6b16c27b54a4f9d82fb753a69))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([d540a83](https://github.com/googleapis/java-storage/commit/d540a830f341e06dd912b2369f0564dd7f0aea7a))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([8e516e6](https://github.com/googleapis/java-storage/commit/8e516e6a205383c32f4de075bc3494512c7164b7))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([0a2fac5](https://github.com/googleapis/java-storage/commit/0a2fac5ba741198496538ae1047d59d1ca3c22ea))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([35c2fbf](https://github.com/googleapis/java-storage/commit/35c2fbfddf4006d84d4d51d5235730a0e109f2a0))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([e5e1107](https://github.com/googleapis/java-storage/commit/e5e11078e52746f5704f2860a26ce9adf5b8699e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([79bea2c](https://github.com/googleapis/java-storage/commit/79bea2c0f207bc50657566c8da1e7281719bde53))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([9416a8f](https://github.com/googleapis/java-storage/commit/9416a8fad09931bbcd048f10e305116d5f45be26))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([411615d](https://github.com/googleapis/java-storage/commit/411615de9a22493c0dd485c93deaea2da236027a))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([51af43e](https://github.com/googleapis/java-storage/commit/51af43ec08baac82a321d84ec423f0975d0e5916))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([0bfb9ff](https://github.com/googleapis/java-storage/commit/0bfb9ff636458b7983363cc46def051a38aacd72))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c648d38](https://github.com/googleapis/java-storage/commit/c648d38866c5ebb165b05781b46287e0b79cdcc5))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([b8dda33](https://github.com/googleapis/java-storage/commit/b8dda33a9628e5b6f774ff242a725b8031130118))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([264683e](https://github.com/googleapis/java-storage/commit/264683e1829fe2fca84a6ffd8c1b835228f0a79e))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([c653bb6](https://github.com/googleapis/java-storage/commit/c653bb657290306b48a48a2c25f988328d8f7934))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([24be97d](https://github.com/googleapis/java-storage/commit/24be97d755eafd1ae2989633ce9059b4ea385eb8))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([a0535c5](https://github.com/googleapis/java-storage/commit/a0535c5ab6ac566e6b2d143f25ef57e742121b69))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([be3be3f](https://github.com/googleapis/java-storage/commit/be3be3f895b651ae36acb07d53c21a2241d56df1))
  * add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([ec59078](https://github.com/googleapis/java-storage/commit/ec590781093686ba44f1bf5c1960226be2ad7c97))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c3a0aaa](https://github.com/googleapis/java-storage/commit/c3a0aaa68f9ee64d850ef5d7cd1c7bea01113503))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([fac7839](https://github.com/googleapis/java-storage/commit/fac7839739bcf5fb0e63fb39b02b331206cc3630))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8332e1b](https://github.com/googleapis/java-storage/commit/8332e1b3636bdbbd4e550053725e7ab040bff463))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([e4688a0](https://github.com/googleapis/java-storage/commit/e4688a00b7f35a28dd079606b7fdd36851564834))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([b426e7d](https://github.com/googleapis/java-storage/commit/b426e7d3d57f0e147bfc4dda0319665130c970a1))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c601cca](https://github.com/googleapis/java-storage/commit/c601cca381881d4ef52b851fe8edd13037688b9e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c58fe1f](https://github.com/googleapis/java-storage/commit/c58fe1f62ebdaab1ea74de1d05c0b2e6500994bf))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([616256a](https://github.com/googleapis/java-storage/commit/616256aa5850e625faf6f74996dc40c911050952))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ba3af58](https://github.com/googleapis/java-storage/commit/ba3af58df8d296bfc6290107e595219472a16861))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([e12d2ad](https://github.com/googleapis/java-storage/commit/e12d2ad9bd301bbcb4ac227a8327fd1754205595))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([d6044a1](https://github.com/googleapis/java-storage/commit/d6044a1c47345b18a018829e272612bc5c52f4b9))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([eebc6c6](https://github.com/googleapis/java-storage/commit/eebc6c6700d2b94b320777c2bd68377570d3c6da))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([12507e2](https://github.com/googleapis/java-storage/commit/12507e2172b8b59b10e98eb8dda9d1c5050a647f))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([58557a0](https://github.com/googleapis/java-storage/commit/58557a054e52fde1c33b8817fbb3f36d41665d9f))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c109fdb](https://github.com/googleapis/java-storage/commit/c109fdbe515d62bf152bba9803fb25e388656a24))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([d98ecc7](https://github.com/googleapis/java-storage/commit/d98ecc7df39142ea90e51b47f42dffad0ac03c24))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([6858a9d](https://github.com/googleapis/java-storage/commit/6858a9dac8bd622b214c8b9fa9a180b95c2a092d))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([bb7e1b4](https://github.com/googleapis/java-storage/commit/bb7e1b45822741b7d3d470a1e0fa350a963841bf))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([e89ae27](https://github.com/googleapis/java-storage/commit/e89ae2757578adc099442e2b7844949c666468c8))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8beaa03](https://github.com/googleapis/java-storage/commit/8beaa0353f51846cd902ef1568bd1bb8b4936b68))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ff8fd8f](https://github.com/googleapis/java-storage/commit/ff8fd8fdbd78b7cf4b0dad70d93cd6aeaadb0a03))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([944e0bc](https://github.com/googleapis/java-storage/commit/944e0bc57be2e04df0358b85b43167fc4ea0bcfe))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([eb8c5c8](https://github.com/googleapis/java-storage/commit/eb8c5c896c758d36eb114143fb79be74f28f0232))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([50e4589](https://github.com/googleapis/java-storage/commit/50e4589dc0e6ab88fbe869ba4b3a959d2dcfec2b))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([a751971](https://github.com/googleapis/java-storage/commit/a7519715f73b11659608d97bf95eeb690e5f6a44))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([befff3b](https://github.com/googleapis/java-storage/commit/befff3b4b2a3b8da70b514f6489ae6a690e419c0))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ac950ad](https://github.com/googleapis/java-storage/commit/ac950ada45d0408199249a25f93e0c5b0a12ab12))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([f381795](https://github.com/googleapis/java-storage/commit/f3817950fb2ded13904c549718f6baeb73ad5e85))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([84ffb6d](https://github.com/googleapis/java-storage/commit/84ffb6d432e75daf89b4910af3c7f50a39dcb323))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([b95e51d](https://github.com/googleapis/java-storage/commit/b95e51d89101ea4683c944856cb7c19ad6b4b514))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([03aa3e7](https://github.com/googleapis/java-storage/commit/03aa3e735f941ec896c47d4d4ea1bf0700a0b626))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([23f9a79](https://github.com/googleapis/java-storage/commit/23f9a793b69d2d34abecb31f4628fc07923c5e2d))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([e2a3e3c](https://github.com/googleapis/java-storage/commit/e2a3e3c2ca8e323f0e99d2cc67ce1cd1b034a049))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([bee4308](https://github.com/googleapis/java-storage/commit/bee43087ec13eadca435ebccdca56d4ca39e5a57))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([28f2759](https://github.com/googleapis/java-storage/commit/28f27592df6b5a70db3e9cfabaa23ab2b3c15680))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([775ad24](https://github.com/googleapis/java-storage/commit/775ad240569c3b77eb3ab0df023313e675eddf4b))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([f29d825](https://github.com/googleapis/java-storage/commit/f29d825d1521fb3ca8fe94f5904df8e356e3e68e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([2e8a0ee](https://github.com/googleapis/java-storage/commit/2e8a0eef40df70fab703c199a3b5b58c645bb2df))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([5c2cf19](https://github.com/googleapis/java-storage/commit/5c2cf196c202d91618ebedf5ba7a26d8d21790d5))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([2431ee1](https://github.com/googleapis/java-storage/commit/2431ee1a350c9c47b5dfa6da20c4b5788eb9388f))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([aeb621a](https://github.com/googleapis/java-storage/commit/aeb621ad08ef6369dbeba369a2345ba9a50e5218))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3d2520d](https://github.com/googleapis/java-storage/commit/3d2520dd6686dd873a941ceabe602407ec7f8f96))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3e38109](https://github.com/googleapis/java-storage/commit/3e38109a734395cc9324e31d9473b3b7991232bc))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8453281](https://github.com/googleapis/java-storage/commit/8453281c53448323fb83f2dea076886c4a37ff92))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([4170803](https://github.com/googleapis/java-storage/commit/41708031863ea2b50b22c60d8a61f75a6c1f2de0))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([f8e54b5](https://github.com/googleapis/java-storage/commit/f8e54b532a09b39d7690763dda1da640b3012cdd))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([85049b9](https://github.com/googleapis/java-storage/commit/85049b97b3cc8a82bb28d75295e1cdf5e3cc06ae))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([2a92e35](https://github.com/googleapis/java-storage/commit/2a92e359ce1463306bef3415dde4af69ed515873))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3b195fe](https://github.com/googleapis/java-storage/commit/3b195fecc165896fc7654744e82247127e39e535))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ae31163](https://github.com/googleapis/java-storage/commit/ae31163618704a1c37394ccc5b4213773f149ac5))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([b1499d6](https://github.com/googleapis/java-storage/commit/b1499d6b64d82c54e339f2af86422ae0a8aa766b))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([1085216](https://github.com/googleapis/java-storage/commit/1085216acd5fc3191ff043615b0f0b52730e56e2))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3616097](https://github.com/googleapis/java-storage/commit/36160978c767c828921fabc1314c89a81eb612b9))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([6a80994](https://github.com/googleapis/java-storage/commit/6a8099482558b3486b008af632f18094e6461797))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([69d01d4](https://github.com/googleapis/java-storage/commit/69d01d41b731f6c03049c24b954704a672400cbd))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([fa0df98](https://github.com/googleapis/java-storage/commit/fa0df985586466f73aa7bca9a4982402aa802bc8))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3eec2e3](https://github.com/googleapis/java-storage/commit/3eec2e327f4aad1bb46f3389e76d02b55a31ee43))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([1bf497e](https://github.com/googleapis/java-storage/commit/1bf497e3ce2105734daa262589550aca29eee0f2))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([bc7a931](https://github.com/googleapis/java-storage/commit/bc7a931542b22589c39d0be0980eb116dbf2a0dc))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c6f5b57](https://github.com/googleapis/java-storage/commit/c6f5b57e3cdd3747121f50284bca7f823e34f329))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8d4d7a3](https://github.com/googleapis/java-storage/commit/8d4d7a3caed4711a59a9509347ed634a783e390a))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([affb14f](https://github.com/googleapis/java-storage/commit/affb14fbb2738c687a885ad4491e57da7808cb9b))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([09c426b](https://github.com/googleapis/java-storage/commit/09c426b42d4d72d547312e68428373bc6edfc585))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([af52279](https://github.com/googleapis/java-storage/commit/af5227949285419add4398e62dd7276e2e9038f4))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([72491e7](https://github.com/googleapis/java-storage/commit/72491e711054572d90c5b673a128bf5294f07daf))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([2968790](https://github.com/googleapis/java-storage/commit/2968790b77bae8751ae56c306e736c99409da8a7))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([a4d919e](https://github.com/googleapis/java-storage/commit/a4d919ed36d3095653b22abb9bc607e58d39ddaa))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([f437c0a](https://github.com/googleapis/java-storage/commit/f437c0a427d234a4d7afc486e1480e64695e7785))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ba70fd8](https://github.com/googleapis/java-storage/commit/ba70fd8495ee81081dd7a9acbf49b56d296b7d1a))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([95d46a5](https://github.com/googleapis/java-storage/commit/95d46a581be8f1b2aafc137257ddb8aa48009707))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([413d65f](https://github.com/googleapis/java-storage/commit/413d65fe73ae4f5e360f75b22a36b57b1aac1b87))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([52639da](https://github.com/googleapis/java-storage/commit/52639da2676476c734df496bd92054c62f60a226))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([961f3cb](https://github.com/googleapis/java-storage/commit/961f3cb7c1f83eff6a01c6e283f8c2faf47822ee))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([98dbb02](https://github.com/googleapis/java-storage/commit/98dbb02c8c8711219b087c6c702dbeeee5fdf27e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([cbc22f2](https://github.com/googleapis/java-storage/commit/cbc22f22f27f07f4b2ca6bc50890d13fdf715663))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([f7c37f5](https://github.com/googleapis/java-storage/commit/f7c37f576bd801ab15926aaeda6f676050a6a442))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([a7a8945](https://github.com/googleapis/java-storage/commit/a7a894505144333e9ad28fbe0faf840985414f07))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([26db9e3](https://github.com/googleapis/java-storage/commit/26db9e356c4c6b12d2defd587c169d34529ec37e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([3ca4123](https://github.com/googleapis/java-storage/commit/3ca4123a7c307246393f8f441e3b8d623806fe28))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8553cb9](https://github.com/googleapis/java-storage/commit/8553cb9d6153c48f0634a24bdbac9c9f1306e1dc))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([758756f](https://github.com/googleapis/java-storage/commit/758756fce213ad0fe8ef3127d2bb55b1e2f8a7aa))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([065d249](https://github.com/googleapis/java-storage/commit/065d2491cfb19a66bba36a97e2e80c37d6090240))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([61824e6](https://github.com/googleapis/java-storage/commit/61824e6a36b48b7caeb66b88436fa645a4a0f01a))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([67482f7](https://github.com/googleapis/java-storage/commit/67482f7a79eea2d6b16c27b54a4f9d82fb753a69))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([d540a83](https://github.com/googleapis/java-storage/commit/d540a830f341e06dd912b2369f0564dd7f0aea7a))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([8e516e6](https://github.com/googleapis/java-storage/commit/8e516e6a205383c32f4de075bc3494512c7164b7))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([0a2fac5](https://github.com/googleapis/java-storage/commit/0a2fac5ba741198496538ae1047d59d1ca3c22ea))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([35c2fbf](https://github.com/googleapis/java-storage/commit/35c2fbfddf4006d84d4d51d5235730a0e109f2a0))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([e5e1107](https://github.com/googleapis/java-storage/commit/e5e11078e52746f5704f2860a26ce9adf5b8699e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([79bea2c](https://github.com/googleapis/java-storage/commit/79bea2c0f207bc50657566c8da1e7281719bde53))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([9416a8f](https://github.com/googleapis/java-storage/commit/9416a8fad09931bbcd048f10e305116d5f45be26))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([411615d](https://github.com/googleapis/java-storage/commit/411615de9a22493c0dd485c93deaea2da236027a))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([51af43e](https://github.com/googleapis/java-storage/commit/51af43ec08baac82a321d84ec423f0975d0e5916))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([0bfb9ff](https://github.com/googleapis/java-storage/commit/0bfb9ff636458b7983363cc46def051a38aacd72))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c648d38](https://github.com/googleapis/java-storage/commit/c648d38866c5ebb165b05781b46287e0b79cdcc5))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([b8dda33](https://github.com/googleapis/java-storage/commit/b8dda33a9628e5b6f774ff242a725b8031130118))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([264683e](https://github.com/googleapis/java-storage/commit/264683e1829fe2fca84a6ffd8c1b835228f0a79e))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([c653bb6](https://github.com/googleapis/java-storage/commit/c653bb657290306b48a48a2c25f988328d8f7934))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([24be97d](https://github.com/googleapis/java-storage/commit/24be97d755eafd1ae2989633ce9059b4ea385eb8))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([a0535c5](https://github.com/googleapis/java-storage/commit/a0535c5ab6ac566e6b2d143f25ef57e742121b69))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([be3be3f](https://github.com/googleapis/java-storage/commit/be3be3f895b651ae36acb07d53c21a2241d56df1))
  * add @BetaApi Storage#blobReadSession for gRPC Transport ([ec59078](https://github.com/googleapis/java-storage/commit/ec590781093686ba44f1bf5c1960226be2ad7c97))
  * Add Anywhere cache control APIs ([81c8c61](https://github.com/googleapis/java-storage/commit/81c8c611ab51a706d63670dff86db5bfd04ef544))
  * Add Anywhere cache control APIs ([81c8c61](https://github.com/googleapis/java-storage/commit/81c8c611ab51a706d63670dff86db5bfd04ef544))
  * add AppendableUploadWriteableByteChannel#flush() ([#3261](https://github.com/googleapis/java-storage/issues/3261)) ([950c56f](https://github.com/googleapis/java-storage/commit/950c56f0e622d75faff51257d5cbc9f3ddc7e1ce))
  * add BlobInfo.ObjectContexts ([#3259](https://github.com/googleapis/java-storage/issues/3259)) ([485aefd](https://github.com/googleapis/java-storage/commit/485aefd3047c52c98d8bd913033c8aee1473e988))
  * add BucketInfo.IpFilter ([#3177](https://github.com/googleapis/java-storage/issues/3177)) ([14a91ec](https://github.com/googleapis/java-storage/commit/14a91ec208067e6afc55923cffda5f69aa33d8b4))
  * add default end-to-end checksumming for JournalingBlobWriteSessionConfig [#3180](https://github.com/googleapis/java-storage/issues/3180) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * add default end-to-end crc32c checksumming for several upload methods via grpc transport [#3176](https://github.com/googleapis/java-storage/issues/3176) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * add MinFlushSizeFlushPolicy#withMaxPendingBytes(long) ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * add MoveObject RPC ([34b8ac4](https://github.com/googleapis/java-storage/commit/34b8ac4239bab67b53c73050d2341615254a3ae0))
  * add new Options to allow per method header values ([#2941](https://github.com/googleapis/java-storage/issues/2941)) ([297802d](https://github.com/googleapis/java-storage/commit/297802d1715e3289dd720fba851c563004b8c5f2))
  * add new preview Bucket encryption policy configuration ([#3204](https://github.com/googleapis/java-storage/issues/3204)) ([7b250dd](https://github.com/googleapis/java-storage/commit/7b250dd53cfa29bbb6a0a4cb4a345aeb2dab5c86))
  * add new Storage#moveBlob method to atomically rename an object ([#2882](https://github.com/googleapis/java-storage/issues/2882)) ([c49fd08](https://github.com/googleapis/java-storage/commit/c49fd08582c7235919270c1dd4eb2ece6933d302))
  * add per-message checksum validation for gRPC ReadObject operations ([#3336](https://github.com/googleapis/java-storage/issues/3336)) ([6eef1b0](https://github.com/googleapis/java-storage/commit/6eef1b0f587b9f32041ac4bcef1a16b1b0bc4bb3))
  * add preview MultipartUploadClient#abortMultipartUpload https://github.com/googleapis/java-storage/pull/3361 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add preview MultipartUploadClient#completeMultipartUpload https://github.com/googleapis/java-storage/pull/3372 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add preview MultipartUploadClient#createMultipartUpload https://github.com/googleapis/java-storage/pull/3356 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add preview MultipartUploadClient#listParts https://github.com/googleapis/java-storage/pull/3359 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add preview MultipartUploadClient#uploadPart https://github.com/googleapis/java-storage/pull/3375 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add preview MultipartUploadSettings ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * add Storage.BlobListOption#includeTrailingDelimiter ([#3038](https://github.com/googleapis/java-storage/issues/3038)) ([0b7a0df](https://github.com/googleapis/java-storage/commit/0b7a0dff91af0e22e84ba3ca08862141292b3b30))
  * add StorageChannelUtils to provide helper methods to perform blocking read/write to/from non-blocking channels ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * expose BucketInfo.getProject as a BigInteger ([#3119](https://github.com/googleapis/java-storage/issues/3119)) ([64bbb60](https://github.com/googleapis/java-storage/commit/64bbb608033f757cb6e31e75a78740d8ed1dccab)), closes [#3023](https://github.com/googleapis/java-storage/issues/3023)
  * implement improved retry context information ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))
  * implement improved retry context information ([c3a0aaa](https://github.com/googleapis/java-storage/commit/c3a0aaa68f9ee64d850ef5d7cd1c7bea01113503))
  * implement improved retry context information ([fac7839](https://github.com/googleapis/java-storage/commit/fac7839739bcf5fb0e63fb39b02b331206cc3630))
  * implement improved retry context information ([8332e1b](https://github.com/googleapis/java-storage/commit/8332e1b3636bdbbd4e550053725e7ab040bff463))
  * implement improved retry context information ([e4688a0](https://github.com/googleapis/java-storage/commit/e4688a00b7f35a28dd079606b7fdd36851564834))
  * implement improved retry context information ([b426e7d](https://github.com/googleapis/java-storage/commit/b426e7d3d57f0e147bfc4dda0319665130c970a1))
  * implement improved retry context information ([c601cca](https://github.com/googleapis/java-storage/commit/c601cca381881d4ef52b851fe8edd13037688b9e))
  * implement improved retry context information ([c58fe1f](https://github.com/googleapis/java-storage/commit/c58fe1f62ebdaab1ea74de1d05c0b2e6500994bf))
  * implement improved retry context information ([616256a](https://github.com/googleapis/java-storage/commit/616256aa5850e625faf6f74996dc40c911050952))
  * implement improved retry context information ([ba3af58](https://github.com/googleapis/java-storage/commit/ba3af58df8d296bfc6290107e595219472a16861))
  * implement improved retry context information ([e12d2ad](https://github.com/googleapis/java-storage/commit/e12d2ad9bd301bbcb4ac227a8327fd1754205595))
  * implement improved retry context information ([d6044a1](https://github.com/googleapis/java-storage/commit/d6044a1c47345b18a018829e272612bc5c52f4b9))
  * implement improved retry context information ([eebc6c6](https://github.com/googleapis/java-storage/commit/eebc6c6700d2b94b320777c2bd68377570d3c6da))
  * implement improved retry context information ([12507e2](https://github.com/googleapis/java-storage/commit/12507e2172b8b59b10e98eb8dda9d1c5050a647f))
  * implement improved retry context information ([58557a0](https://github.com/googleapis/java-storage/commit/58557a054e52fde1c33b8817fbb3f36d41665d9f))
  * implement improved retry context information ([c109fdb](https://github.com/googleapis/java-storage/commit/c109fdbe515d62bf152bba9803fb25e388656a24))
  * implement improved retry context information ([d98ecc7](https://github.com/googleapis/java-storage/commit/d98ecc7df39142ea90e51b47f42dffad0ac03c24))
  * implement improved retry context information ([6858a9d](https://github.com/googleapis/java-storage/commit/6858a9dac8bd622b214c8b9fa9a180b95c2a092d))
  * implement improved retry context information ([bb7e1b4](https://github.com/googleapis/java-storage/commit/bb7e1b45822741b7d3d470a1e0fa350a963841bf))
  * implement improved retry context information ([e89ae27](https://github.com/googleapis/java-storage/commit/e89ae2757578adc099442e2b7844949c666468c8))
  * implement improved retry context information ([8beaa03](https://github.com/googleapis/java-storage/commit/8beaa0353f51846cd902ef1568bd1bb8b4936b68))
  * implement improved retry context information ([ff8fd8f](https://github.com/googleapis/java-storage/commit/ff8fd8fdbd78b7cf4b0dad70d93cd6aeaadb0a03))
  * implement improved retry context information ([944e0bc](https://github.com/googleapis/java-storage/commit/944e0bc57be2e04df0358b85b43167fc4ea0bcfe))
  * implement improved retry context information ([eb8c5c8](https://github.com/googleapis/java-storage/commit/eb8c5c896c758d36eb114143fb79be74f28f0232))
  * implement improved retry context information ([50e4589](https://github.com/googleapis/java-storage/commit/50e4589dc0e6ab88fbe869ba4b3a959d2dcfec2b))
  * implement improved retry context information ([a751971](https://github.com/googleapis/java-storage/commit/a7519715f73b11659608d97bf95eeb690e5f6a44))
  * implement improved retry context information ([befff3b](https://github.com/googleapis/java-storage/commit/befff3b4b2a3b8da70b514f6489ae6a690e419c0))
  * implement improved retry context information ([ac950ad](https://github.com/googleapis/java-storage/commit/ac950ada45d0408199249a25f93e0c5b0a12ab12))
  * implement improved retry context information ([f381795](https://github.com/googleapis/java-storage/commit/f3817950fb2ded13904c549718f6baeb73ad5e85))
  * implement improved retry context information ([84ffb6d](https://github.com/googleapis/java-storage/commit/84ffb6d432e75daf89b4910af3c7f50a39dcb323))
  * implement improved retry context information ([b95e51d](https://github.com/googleapis/java-storage/commit/b95e51d89101ea4683c944856cb7c19ad6b4b514))
  * implement improved retry context information ([03aa3e7](https://github.com/googleapis/java-storage/commit/03aa3e735f941ec896c47d4d4ea1bf0700a0b626))
  * implement improved retry context information ([23f9a79](https://github.com/googleapis/java-storage/commit/23f9a793b69d2d34abecb31f4628fc07923c5e2d))
  * implement improved retry context information ([e2a3e3c](https://github.com/googleapis/java-storage/commit/e2a3e3c2ca8e323f0e99d2cc67ce1cd1b034a049))
  * implement improved retry context information ([bee4308](https://github.com/googleapis/java-storage/commit/bee43087ec13eadca435ebccdca56d4ca39e5a57))
  * implement improved retry context information ([28f2759](https://github.com/googleapis/java-storage/commit/28f27592df6b5a70db3e9cfabaa23ab2b3c15680))
  * implement improved retry context information ([775ad24](https://github.com/googleapis/java-storage/commit/775ad240569c3b77eb3ab0df023313e675eddf4b))
  * implement improved retry context information ([f29d825](https://github.com/googleapis/java-storage/commit/f29d825d1521fb3ca8fe94f5904df8e356e3e68e))
  * implement improved retry context information ([2e8a0ee](https://github.com/googleapis/java-storage/commit/2e8a0eef40df70fab703c199a3b5b58c645bb2df))
  * implement improved retry context information ([5c2cf19](https://github.com/googleapis/java-storage/commit/5c2cf196c202d91618ebedf5ba7a26d8d21790d5))
  * implement improved retry context information ([2431ee1](https://github.com/googleapis/java-storage/commit/2431ee1a350c9c47b5dfa6da20c4b5788eb9388f))
  * implement improved retry context information ([aeb621a](https://github.com/googleapis/java-storage/commit/aeb621ad08ef6369dbeba369a2345ba9a50e5218))
  * implement improved retry context information ([3d2520d](https://github.com/googleapis/java-storage/commit/3d2520dd6686dd873a941ceabe602407ec7f8f96))
  * implement improved retry context information ([3e38109](https://github.com/googleapis/java-storage/commit/3e38109a734395cc9324e31d9473b3b7991232bc))
  * implement improved retry context information ([8453281](https://github.com/googleapis/java-storage/commit/8453281c53448323fb83f2dea076886c4a37ff92))
  * implement improved retry context information ([4170803](https://github.com/googleapis/java-storage/commit/41708031863ea2b50b22c60d8a61f75a6c1f2de0))
  * implement improved retry context information ([f8e54b5](https://github.com/googleapis/java-storage/commit/f8e54b532a09b39d7690763dda1da640b3012cdd))
  * implement improved retry context information ([85049b9](https://github.com/googleapis/java-storage/commit/85049b97b3cc8a82bb28d75295e1cdf5e3cc06ae))
  * implement improved retry context information ([2a92e35](https://github.com/googleapis/java-storage/commit/2a92e359ce1463306bef3415dde4af69ed515873))
  * implement improved retry context information ([3b195fe](https://github.com/googleapis/java-storage/commit/3b195fecc165896fc7654744e82247127e39e535))
  * implement improved retry context information ([ae31163](https://github.com/googleapis/java-storage/commit/ae31163618704a1c37394ccc5b4213773f149ac5))
  * implement improved retry context information ([b1499d6](https://github.com/googleapis/java-storage/commit/b1499d6b64d82c54e339f2af86422ae0a8aa766b))
  * implement improved retry context information ([1085216](https://github.com/googleapis/java-storage/commit/1085216acd5fc3191ff043615b0f0b52730e56e2))
  * implement improved retry context information ([3616097](https://github.com/googleapis/java-storage/commit/36160978c767c828921fabc1314c89a81eb612b9))
  * implement improved retry context information ([6a80994](https://github.com/googleapis/java-storage/commit/6a8099482558b3486b008af632f18094e6461797))
  * implement improved retry context information ([69d01d4](https://github.com/googleapis/java-storage/commit/69d01d41b731f6c03049c24b954704a672400cbd))
  * implement improved retry context information ([fa0df98](https://github.com/googleapis/java-storage/commit/fa0df985586466f73aa7bca9a4982402aa802bc8))
  * implement improved retry context information ([3eec2e3](https://github.com/googleapis/java-storage/commit/3eec2e327f4aad1bb46f3389e76d02b55a31ee43))
  * implement improved retry context information ([1bf497e](https://github.com/googleapis/java-storage/commit/1bf497e3ce2105734daa262589550aca29eee0f2))
  * implement improved retry context information ([bc7a931](https://github.com/googleapis/java-storage/commit/bc7a931542b22589c39d0be0980eb116dbf2a0dc))
  * implement improved retry context information ([c6f5b57](https://github.com/googleapis/java-storage/commit/c6f5b57e3cdd3747121f50284bca7f823e34f329))
  * implement improved retry context information ([8d4d7a3](https://github.com/googleapis/java-storage/commit/8d4d7a3caed4711a59a9509347ed634a783e390a))
  * implement improved retry context information ([affb14f](https://github.com/googleapis/java-storage/commit/affb14fbb2738c687a885ad4491e57da7808cb9b))
  * implement improved retry context information ([09c426b](https://github.com/googleapis/java-storage/commit/09c426b42d4d72d547312e68428373bc6edfc585))
  * implement improved retry context information ([af52279](https://github.com/googleapis/java-storage/commit/af5227949285419add4398e62dd7276e2e9038f4))
  * implement improved retry context information ([72491e7](https://github.com/googleapis/java-storage/commit/72491e711054572d90c5b673a128bf5294f07daf))
  * implement improved retry context information ([2968790](https://github.com/googleapis/java-storage/commit/2968790b77bae8751ae56c306e736c99409da8a7))
  * implement improved retry context information ([a4d919e](https://github.com/googleapis/java-storage/commit/a4d919ed36d3095653b22abb9bc607e58d39ddaa))
  * implement improved retry context information ([f437c0a](https://github.com/googleapis/java-storage/commit/f437c0a427d234a4d7afc486e1480e64695e7785))
  * implement improved retry context information ([ba70fd8](https://github.com/googleapis/java-storage/commit/ba70fd8495ee81081dd7a9acbf49b56d296b7d1a))
  * implement improved retry context information ([95d46a5](https://github.com/googleapis/java-storage/commit/95d46a581be8f1b2aafc137257ddb8aa48009707))
  * implement improved retry context information ([413d65f](https://github.com/googleapis/java-storage/commit/413d65fe73ae4f5e360f75b22a36b57b1aac1b87))
  * implement improved retry context information ([52639da](https://github.com/googleapis/java-storage/commit/52639da2676476c734df496bd92054c62f60a226))
  * implement improved retry context information ([961f3cb](https://github.com/googleapis/java-storage/commit/961f3cb7c1f83eff6a01c6e283f8c2faf47822ee))
  * implement improved retry context information ([98dbb02](https://github.com/googleapis/java-storage/commit/98dbb02c8c8711219b087c6c702dbeeee5fdf27e))
  * implement improved retry context information ([cbc22f2](https://github.com/googleapis/java-storage/commit/cbc22f22f27f07f4b2ca6bc50890d13fdf715663))
  * implement improved retry context information ([f7c37f5](https://github.com/googleapis/java-storage/commit/f7c37f576bd801ab15926aaeda6f676050a6a442))
  * implement improved retry context information ([a7a8945](https://github.com/googleapis/java-storage/commit/a7a894505144333e9ad28fbe0faf840985414f07))
  * implement improved retry context information ([26db9e3](https://github.com/googleapis/java-storage/commit/26db9e356c4c6b12d2defd587c169d34529ec37e))
  * implement improved retry context information ([3ca4123](https://github.com/googleapis/java-storage/commit/3ca4123a7c307246393f8f441e3b8d623806fe28))
  * implement improved retry context information ([8553cb9](https://github.com/googleapis/java-storage/commit/8553cb9d6153c48f0634a24bdbac9c9f1306e1dc))
  * implement improved retry context information ([758756f](https://github.com/googleapis/java-storage/commit/758756fce213ad0fe8ef3127d2bb55b1e2f8a7aa))
  * implement improved retry context information ([065d249](https://github.com/googleapis/java-storage/commit/065d2491cfb19a66bba36a97e2e80c37d6090240))
  * implement improved retry context information ([61824e6](https://github.com/googleapis/java-storage/commit/61824e6a36b48b7caeb66b88436fa645a4a0f01a))
  * implement improved retry context information ([67482f7](https://github.com/googleapis/java-storage/commit/67482f7a79eea2d6b16c27b54a4f9d82fb753a69))
  * implement improved retry context information ([d540a83](https://github.com/googleapis/java-storage/commit/d540a830f341e06dd912b2369f0564dd7f0aea7a))
  * implement improved retry context information ([8e516e6](https://github.com/googleapis/java-storage/commit/8e516e6a205383c32f4de075bc3494512c7164b7))
  * implement improved retry context information ([0a2fac5](https://github.com/googleapis/java-storage/commit/0a2fac5ba741198496538ae1047d59d1ca3c22ea))
  * implement improved retry context information ([35c2fbf](https://github.com/googleapis/java-storage/commit/35c2fbfddf4006d84d4d51d5235730a0e109f2a0))
  * implement improved retry context information ([e5e1107](https://github.com/googleapis/java-storage/commit/e5e11078e52746f5704f2860a26ce9adf5b8699e))
  * implement improved retry context information ([79bea2c](https://github.com/googleapis/java-storage/commit/79bea2c0f207bc50657566c8da1e7281719bde53))
  * implement improved retry context information ([9416a8f](https://github.com/googleapis/java-storage/commit/9416a8fad09931bbcd048f10e305116d5f45be26))
  * implement improved retry context information ([411615d](https://github.com/googleapis/java-storage/commit/411615de9a22493c0dd485c93deaea2da236027a))
  * implement improved retry context information ([51af43e](https://github.com/googleapis/java-storage/commit/51af43ec08baac82a321d84ec423f0975d0e5916))
  * implement improved retry context information ([0bfb9ff](https://github.com/googleapis/java-storage/commit/0bfb9ff636458b7983363cc46def051a38aacd72))
  * implement improved retry context information ([c648d38](https://github.com/googleapis/java-storage/commit/c648d38866c5ebb165b05781b46287e0b79cdcc5))
  * implement improved retry context information ([b8dda33](https://github.com/googleapis/java-storage/commit/b8dda33a9628e5b6f774ff242a725b8031130118))
  * implement improved retry context information ([264683e](https://github.com/googleapis/java-storage/commit/264683e1829fe2fca84a6ffd8c1b835228f0a79e))
  * implement improved retry context information ([c653bb6](https://github.com/googleapis/java-storage/commit/c653bb657290306b48a48a2c25f988328d8f7934))
  * implement improved retry context information ([24be97d](https://github.com/googleapis/java-storage/commit/24be97d755eafd1ae2989633ce9059b4ea385eb8))
  * implement improved retry context information ([a0535c5](https://github.com/googleapis/java-storage/commit/a0535c5ab6ac566e6b2d143f25ef57e742121b69))
  * implement improved retry context information ([be3be3f](https://github.com/googleapis/java-storage/commit/be3be3f895b651ae36acb07d53c21a2241d56df1))
  * implement improved retry context information ([ec59078](https://github.com/googleapis/java-storage/commit/ec590781093686ba44f1bf5c1960226be2ad7c97))
  * introductory beta level support for OpenTelemetry tracing on c.g.c.storage.Storage methods ([#2837](https://github.com/googleapis/java-storage/issues/2837)) ([dd889ea](https://github.com/googleapis/java-storage/commit/dd889ea0d0a57490ef106ab92ba557f26d414406))
  * next release from main branch is 2.48.0 ([#2885](https://github.com/googleapis/java-storage/issues/2885)) ([34e5903](https://github.com/googleapis/java-storage/commit/34e5903df9b7221ba9ebabc07046d7b819f9f209))
  * next release from main branch is 2.50.0 ([#2968](https://github.com/googleapis/java-storage/issues/2968)) ([4a69fcc](https://github.com/googleapis/java-storage/commit/4a69fcc16787904675e5ba15f42bcab67553a7aa))
  * **storagecontrol:** Add Anywhere cache control APIs ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))
  * **storagecontrol:** Add Client Libraries Storage IntelligenceConfig ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))
  * **storagecontrol:** add GetIamPolicy, SetIamPolicy, and TestIamPermissions RPCs ([c884551](https://github.com/googleapis/java-storage/commit/c884551048a323f2a3fd7aaf4fce469d4d4f543e))
  * **transfer-manager:** add ParallelUploadConfig.Builder#setUploadBlobInfoFactory ([#2936](https://github.com/googleapis/java-storage/issues/2936)) ([86e9ae8](https://github.com/googleapis/java-storage/commit/86e9ae80772aa202d0b6563b8dd37722d8b5e0e0)), closes [#2638](https://github.com/googleapis/java-storage/issues/2638)



##### Bug Fixes

  * add case insensitive check for X-Goog-Content-SHA256 in SignatureInfo ([#3337](https://github.com/googleapis/java-storage/issues/3337)) ([54bc2c1](https://github.com/googleapis/java-storage/commit/54bc2c12f2d0e8c164e4ddcaa1a61d2de3911131))
  * add new system property (com.google.cloud.storage.grpc.bound_token) to allow disabling bound token use with grpc ([#3365](https://github.com/googleapis/java-storage/issues/3365)) ([ebf5e6d](https://github.com/googleapis/java-storage/commit/ebf5e6d30d8dc197ab388a70cc0d465c0f740496))
  * call response.disconnect() after resolving resumable upload url ([#3385](https://github.com/googleapis/java-storage/issues/3385)) ([ac3be4b](https://github.com/googleapis/java-storage/commit/ac3be4b7e82d9340ede7d527a26ffe3e2ba58909))
  * cancel the future in RemoteStorageHelper#forceDelete when TimeoutException happens ([#3136](https://github.com/googleapis/java-storage/issues/3136)) ([e6007d5](https://github.com/googleapis/java-storage/commit/e6007d56e8801be65209cb5761f62749369425c9))
  * categorize a WatchdogTimeoutException as retriable for grpc ReadObject ([#2954](https://github.com/googleapis/java-storage/issues/2954)) ([b53bd53](https://github.com/googleapis/java-storage/commit/b53bd53c26984b3e850355ced608b511688b74d1))
  * de-beta storage-v2 artifacts ([#2852](https://github.com/googleapis/java-storage/issues/2852)) ([77a2e8a](https://github.com/googleapis/java-storage/commit/77a2e8af341528a4ff3c34a880a7983f828b8cfd))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.0 ([34b8ac4](https://github.com/googleapis/java-storage/commit/34b8ac4239bab67b53c73050d2341615254a3ae0))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.1 ([09ed029](https://github.com/googleapis/java-storage/commit/09ed02995f4688db69c0e0db1c3d72cadce0c395))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.52.0 ([00754bc](https://github.com/googleapis/java-storage/commit/00754bc0b30da4ebc13e75f55525d9bd885b0572))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.53.0 ([9946d6b](https://github.com/googleapis/java-storage/commit/9946d6bdc7ec8398bf1bd1df63f272df1351539e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.54.0 ([22e7e3d](https://github.com/googleapis/java-storage/commit/22e7e3d4e8c56184f9c91b1e0bf52d5c4aa4cf9f))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.55.1 ([81c8c61](https://github.com/googleapis/java-storage/commit/81c8c611ab51a706d63670dff86db5bfd04ef544))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.0 ([8f9f5ec](https://github.com/googleapis/java-storage/commit/8f9f5ec4506bde58fbf2351c99f0d67cdcfcd88e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.2 ([74c46dd](https://github.com/googleapis/java-storage/commit/74c46ddcd91553bcb8145c536389bbe0ca32886c))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.58.0 ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.59.0 ([7dba9f0](https://github.com/googleapis/java-storage/commit/7dba9f09f100062cc8c04e5a2735a4349d8e7ed1))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.60.2 ([bd1f199](https://github.com/googleapis/java-storage/commit/bd1f199cf57c2b8039c303586d5beac64aeca0ba))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.61.0 ([f98b686](https://github.com/googleapis/java-storage/commit/f98b686ef940879458acb1e56339adf869400b94))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.1 ([0e348db](https://github.com/googleapis/java-storage/commit/0e348dbee247e1e65713d0155e1aa29ae5c5e0e4))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.2 ([984f8ca](https://github.com/googleapis/java-storage/commit/984f8ca23a38c7a892a2256a694b72431e44aa27))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.3 ([ba84793](https://github.com/googleapis/java-storage/commit/ba847937e553f6a47aa459f634f63ed42310762d))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.63.0 ([c1a8968](https://github.com/googleapis/java-storage/commit/c1a8968799c1cf5a970fe9f303adccdad0a117c8))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.64.1 ([511ff51](https://github.com/googleapis/java-storage/commit/511ff514410e55425e968ab900ac1b8825fe507a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.65.0-rc1 ([c3267aa](https://github.com/googleapis/java-storage/commit/c3267aabeb6c6dab96b60547ac6d06a498aa8f8b))
  * enable ALTS bound token (for DirectPath) in the grpc channel provider ([#2919](https://github.com/googleapis/java-storage/issues/2919)) ([38d248d](https://github.com/googleapis/java-storage/commit/38d248d9511e808e88c1bac0b6bb2ba54897830d))
  * ensure object generation is sent for Storage#update(BlobInfo) using HTTP Transport ([#3006](https://github.com/googleapis/java-storage/issues/3006)) ([2a3e0e7](https://github.com/googleapis/java-storage/commit/2a3e0e7453c5e3e45bc06eec1ba6d2bc193143e6)), closes [#2980](https://github.com/googleapis/java-storage/issues/2980)
  * fix a possible NPE that could happen when shutting down a grpc Storage instance ([#3089](https://github.com/googleapis/java-storage/issues/3089)) ([56f5d0a](https://github.com/googleapis/java-storage/commit/56f5d0ae8826d3d03c436fd0b91630cd09c09a3d))
  * fix appendable upload finalization race condition ([#3295](https://github.com/googleapis/java-storage/issues/3295)) ([485be18](https://github.com/googleapis/java-storage/commit/485be184c08c7b857d8c9a9443f32903df879b23))
  * fix DefaultBlobWriteSessionConfig init to work when grpc classes are excluded ([#3147](https://github.com/googleapis/java-storage/issues/3147)) ([8571ba8](https://github.com/googleapis/java-storage/commit/8571ba8eee82d055cdeb5f0b6970d5b814eaa24e))
  * fix grpc ReadObject memory leak introduced in 2.51.0 ([#3080](https://github.com/googleapis/java-storage/issues/3080)) ([7057629](https://github.com/googleapis/java-storage/commit/705762947fad452462ad0e55ec5898e6389a0ac3))
  * fix IllegalMonitorStateException thrown from BlobAppendableUpload.isOpen() ([#3302](https://github.com/googleapis/java-storage/issues/3302)) ([aa90468](https://github.com/googleapis/java-storage/commit/aa904688b784d7427454318196ef88628e415246))
  * fix interrupt spiral in grpc ReadObject drainQueue ([#2850](https://github.com/googleapis/java-storage/issues/2850)) ([c1dac83](https://github.com/googleapis/java-storage/commit/c1dac837387ffc40f00344c8fb0e86e09d009358))
  * fix Journaling BlobWriteSessionConfig to properly handle multiple consecutive retries ([#3166](https://github.com/googleapis/java-storage/issues/3166)) ([895bfbd](https://github.com/googleapis/java-storage/commit/895bfbda902a77d16a33fe5238349a6b3d397c10))
  * give user provided checksum precondition priority for Storage#create methods that accept byte[] [#3182](https://github.com/googleapis/java-storage/issues/3182) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * improve 503 handling for json resumable uploads ([#2987](https://github.com/googleapis/java-storage/issues/2987)) ([9bc2b14](https://github.com/googleapis/java-storage/commit/9bc2b14a0058cded0321e5afa3ea3fc59bf3421b))
  * make FlushPolicy${Min,Max}FlushSizeFlushPolicy constructors private ([#3217](https://github.com/googleapis/java-storage/issues/3217)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * migrate away from GoogleCredentials.fromStream() usages ([#3339](https://github.com/googleapis/java-storage/issues/3339)) ([7e42c2f](https://github.com/googleapis/java-storage/commit/7e42c2fbca53ca6b1266f784e58cee00cfed7d62))
  * move crc32c computation before writing to disk for BufferToDiskThenUpload BlobWriteSession config [#3187](https://github.com/googleapis/java-storage/issues/3187) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * next release candidate ([eec9efa](https://github.com/googleapis/java-storage/commit/eec9efaa88f14bea4f20e1883455a9e5331c278f))
  * update 416 handling for ReadChannel ([#3018](https://github.com/googleapis/java-storage/issues/3018)) ([4a9c3e4](https://github.com/googleapis/java-storage/commit/4a9c3e46e8d4fa64813869cadf247cf77f1844d5))
  * update batch handling to ensure each operation has its own unique idempotency-token ([#2905](https://github.com/googleapis/java-storage/issues/2905)) ([8d79b8d](https://github.com/googleapis/java-storage/commit/8d79b8d9cea30c6bba0d2550fa397b8c8b7acc3c))
  * update BlobAppendableUpload implementation to periodically flush for large writes ([#3278](https://github.com/googleapis/java-storage/issues/3278)) ([d0ffe18](https://github.com/googleapis/java-storage/commit/d0ffe18084b32936c889bb280005294c7ae7064d))
  * update BlobAppendableUploadConfig and FlushPolicy.MinFlushSizeFlushPolicy to default to 4MiB minFlushSize and 16MiB maxPendingBytes ([#3249](https://github.com/googleapis/java-storage/issues/3249)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * update BlobReadSession channels to not implicitly close once EOF is observed ([#3344](https://github.com/googleapis/java-storage/issues/3344)) ([9f0a93e](https://github.com/googleapis/java-storage/commit/9f0a93eb4c6bb8aab13915ca1cb40ba9e229a2f9))
  * update BlobReadSession ScatteringByteChannel projection to use less CPU ([#3324](https://github.com/googleapis/java-storage/issues/3324)) ([678fecc](https://github.com/googleapis/java-storage/commit/678feccc972e557380e9ba5fcd52be099440197d))
  * update DefaultRetryContext to trap and forward RejectedExceptionException to onFailure ([#3327](https://github.com/googleapis/java-storage/issues/3327)) ([1be31bd](https://github.com/googleapis/java-storage/commit/1be31bdfbc0283733e86b049d3be1911db50fb96))
  * update grpc based Storage to defer project id validation ([#2930](https://github.com/googleapis/java-storage/issues/2930)) ([cc03784](https://github.com/googleapis/java-storage/commit/cc037848be7d21cb827c97d7f71618f1bfae941d))
  * update gRPC Bidi resumable upload to have more robust error message generation ([#2998](https://github.com/googleapis/java-storage/issues/2998)) ([79b5d85](https://github.com/googleapis/java-storage/commit/79b5d8559b2e655178db2ba75116ddba5a581a7b))
  * update grpc client side metrics detection to be graceful when not running on gcp ([#3097](https://github.com/googleapis/java-storage/issues/3097)) ([10cd32d](https://github.com/googleapis/java-storage/commit/10cd32d51aa061304b5b4d0d632a2eed694cd1d6))
  * update gRPC implementation for storage.buckets.get to translate NOT_FOUND to null ([#3005](https://github.com/googleapis/java-storage/issues/3005)) ([704af65](https://github.com/googleapis/java-storage/commit/704af65b25fe38d146b960775a69644cd80f2e78))
  * update grpc single-shot uploads to attach the callers stracktrace as suppressed exception if an error happens in the background ([#3330](https://github.com/googleapis/java-storage/issues/3330)) ([64e2b2e](https://github.com/googleapis/java-storage/commit/64e2b2ef839e69da0605b9e53989c1f5a2b09e66))
  * update kms key handling when opening a resumable upload to clear the value in the json to be null rather than empty string ([#2939](https://github.com/googleapis/java-storage/issues/2939)) ([43553de](https://github.com/googleapis/java-storage/commit/43553dedce33093e751143fadb372024d975706c))
  * update object context diff logic to be shallow rather than deep ([#3287](https://github.com/googleapis/java-storage/issues/3287)) ([2fd15f6](https://github.com/googleapis/java-storage/commit/2fd15f69e93a3df2b8dbbd4f08edd07c087e957c))
  * update otel integration to properly activate span context for lazy RPCs such as reads & writes ([#3255](https://github.com/googleapis/java-storage/issues/3255)) ([d6587f4](https://github.com/googleapis/java-storage/commit/d6587f42b65a586a2e3f30e0559975801726a812))
  * update otel integration to properly activate span context for lazy RPCs such as reads & writes pt.2 ([#3277](https://github.com/googleapis/java-storage/issues/3277)) ([3240f67](https://github.com/googleapis/java-storage/commit/3240f67c192a855c92256526aeb2fa689ea15445))
  * update PCU request building logic to properly clear crc32c and md5 ([#3323](https://github.com/googleapis/java-storage/issues/3323)) ([4da9f31](https://github.com/googleapis/java-storage/commit/4da9f3108d27f5c2ed3cc39eec161651f421e4db))
  * update request handling of gRPC based CopyWriter ([#2858](https://github.com/googleapis/java-storage/issues/2858)) ([093cb87](https://github.com/googleapis/java-storage/commit/093cb8759d5cfaafa6fd9df43de1bb91c1285f35))
  * update retry lifecycle when attempting to decompress a gzip object ([#2840](https://github.com/googleapis/java-storage/issues/2840)) ([7dba13c](https://github.com/googleapis/java-storage/commit/7dba13cbbfd38d3c2147b25264934f33c5dc78e3))
  * update retry logic for grpc start resumable upload to properly handle client side deadline_exceeded ([#3354](https://github.com/googleapis/java-storage/issues/3354)) ([6eb3331](https://github.com/googleapis/java-storage/commit/6eb33311d8dd7344e30ddcb92334fd52c7c63b4d))
  * update Signed URL default scheme to resolve from storage options host ([#2880](https://github.com/googleapis/java-storage/issues/2880)) ([7ae7e39](https://github.com/googleapis/java-storage/commit/7ae7e3998930c1bec72ff7c06ebc2b66343852ca)), closes [#2870](https://github.com/googleapis/java-storage/issues/2870)
  * update StorageException translation of an ApiException to include error details ([#2872](https://github.com/googleapis/java-storage/issues/2872)) ([8ad5010](https://github.com/googleapis/java-storage/commit/8ad501012fab0dfd8d0f0dce49d7c681540022a9))
  * update usages of String.format to explicitly pass Locale.US ([#2974](https://github.com/googleapis/java-storage/issues/2974)) ([8bcb2de](https://github.com/googleapis/java-storage/commit/8bcb2de22ea39cfc0b4dda07daba78ea192b5e98)), closes [#2972](https://github.com/googleapis/java-storage/issues/2972)



##### Dependencies

  * remove explicit version declarations for packages that are in shared-dependencies ([#3014](https://github.com/googleapis/java-storage/issues/3014)) ([61cdb30](https://github.com/googleapis/java-storage/commit/61cdb30f250d2fdaaf79e0d060eb573197c7a90e))
  * update actions/checkout action to v5 ([#3239](https://github.com/googleapis/java-storage/issues/3239)) ([33f024b](https://github.com/googleapis/java-storage/commit/33f024b1ae094bf3e3605e1a835cb55eb5c9e750))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20241206-2.0.0 ([#2839](https://github.com/googleapis/java-storage/issues/2839)) ([8f3cdd3](https://github.com/googleapis/java-storage/commit/8f3cdd39dbbbbd63c560c3cb44d1032c0bd41749))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250224-2.0.0 ([#2969](https://github.com/googleapis/java-storage/issues/2969)) ([80a40c4](https://github.com/googleapis/java-storage/commit/80a40c41527a5fb83a41ac4754d5be22f5cd5c2b))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250312-2.0.0 ([#3000](https://github.com/googleapis/java-storage/issues/3000)) ([78fc076](https://github.com/googleapis/java-storage/commit/78fc0763c89fb0e603d75b20c9c67eabc2b9f729))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250416-2.0.0 ([#3063](https://github.com/googleapis/java-storage/issues/3063)) ([d496d5b](https://github.com/googleapis/java-storage/commit/d496d5bcc1f6ee922bb8f02bfc91d4aeffb8f9a7))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250420-2.0.0 ([#3070](https://github.com/googleapis/java-storage/issues/3070)) ([1ef50f2](https://github.com/googleapis/java-storage/commit/1ef50f2936e62602db689cffbe166c9494ac58f6))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250424-2.0.0 ([#3084](https://github.com/googleapis/java-storage/issues/3084)) ([c7afbde](https://github.com/googleapis/java-storage/commit/c7afbde3b1a78a56c017283850f90938d66e44fd))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250509-2.0.0 ([#3103](https://github.com/googleapis/java-storage/issues/3103)) ([1fd1090](https://github.com/googleapis/java-storage/commit/1fd109094814bfb6270e10a3e4fd5ec4d20e7fba))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250521-2.0.0 ([#3118](https://github.com/googleapis/java-storage/issues/3118)) ([e1be49e](https://github.com/googleapis/java-storage/commit/e1be49e6c987daccf9542c15c6ba418c007d2fb7))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250524-2.0.0 ([#3127](https://github.com/googleapis/java-storage/issues/3127)) ([2a4499d](https://github.com/googleapis/java-storage/commit/2a4499d1686e93e8495f29b5198488d166caaa06))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250605-2.0.0 ([#3143](https://github.com/googleapis/java-storage/issues/3143)) ([17a80d8](https://github.com/googleapis/java-storage/commit/17a80d8b49fef65557215b310895b0f08ee25235))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250629-2.0.0 ([#3185](https://github.com/googleapis/java-storage/issues/3185)) ([4ce8281](https://github.com/googleapis/java-storage/commit/4ce8281246cbe84ed068205532cac4a03853c331))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250718-2.0.0 ([#3203](https://github.com/googleapis/java-storage/issues/3203)) ([18978e4](https://github.com/googleapis/java-storage/commit/18978e4ec54790df2939490ef76fc19b9f72eb04))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250815-2.0.0 ([#3245](https://github.com/googleapis/java-storage/issues/3245)) ([87afe1a](https://github.com/googleapis/java-storage/commit/87afe1ac5f500053e4c0639d5b824304d03796f4))
  * update dependency com.google.apis:google-api-services-storage to v1-rev20250925-2.0.0 ([#3313](https://github.com/googleapis/java-storage/issues/3313)) ([ab310eb](https://github.com/googleapis/java-storage/commit/ab310eb5af51ed332329abd6c3441d18f9965571))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#2895](https://github.com/googleapis/java-storage/issues/2895)) ([145afb0](https://github.com/googleapis/java-storage/commit/145afb0d3a783fe73a388a7be174b598a195a2c6))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#3061](https://github.com/googleapis/java-storage/issues/3061)) ([cb43a6c](https://github.com/googleapis/java-storage/commit/cb43a6c368367e15dfd7c2205689df04547d1a9c))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#3189](https://github.com/googleapis/java-storage/issues/3189)) ([7fbfb01](https://github.com/googleapis/java-storage/commit/7fbfb013a8cfb72d49e3d752ad25e73b6ccaab4f))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#3201](https://github.com/googleapis/java-storage/issues/3201)) ([782c3c4](https://github.com/googleapis/java-storage/commit/782c3c416583704a196b17f23e9c12c33659f67d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#3213](https://github.com/googleapis/java-storage/issues/3213)) ([86ff697](https://github.com/googleapis/java-storage/commit/86ff69788b30d8f82b6b95d010df507093852889))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#3250](https://github.com/googleapis/java-storage/issues/3250)) ([0782e62](https://github.com/googleapis/java-storage/commit/0782e62fc9534e3cecfaaa4d78b58904ecf699d6))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#3280](https://github.com/googleapis/java-storage/issues/3280)) ([d046ea3](https://github.com/googleapis/java-storage/commit/d046ea3da19288b64c48300bdd4f94a0ebf35458))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#3298](https://github.com/googleapis/java-storage/issues/3298)) ([1489f3a](https://github.com/googleapis/java-storage/commit/1489f3a74c8a27f0888c40600c83adedcfd9a9ec))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#3325](https://github.com/googleapis/java-storage/issues/3325)) ([4d3e3be](https://github.com/googleapis/java-storage/commit/4d3e3be27811ad92becc93321048c4268cec2fcf))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#3351](https://github.com/googleapis/java-storage/issues/3351)) ([e64565a](https://github.com/googleapis/java-storage/commit/e64565ab674f586ea4850408a3f30544997f4b1b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#3381](https://github.com/googleapis/java-storage/issues/3381)) ([e3d3700](https://github.com/googleapis/java-storage/commit/e3d3700e06de2b0113e1cb01e99ef4aeed3c62c9))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2873](https://github.com/googleapis/java-storage/issues/2873)) ([39509d5](https://github.com/googleapis/java-storage/commit/39509d53ee283694526efbec58daa24c3d8ca080))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2904](https://github.com/googleapis/java-storage/issues/2904)) ([2a5242e](https://github.com/googleapis/java-storage/commit/2a5242e580185a5952181f922c4eca25790bcec6))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.34.0 ([#2938](https://github.com/googleapis/java-storage/issues/2938)) ([ff6f696](https://github.com/googleapis/java-storage/commit/ff6f696e8c4a539b5e6755fbd550096ee4688ecc))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.36.0 ([#3162](https://github.com/googleapis/java-storage/issues/3162)) ([41a1030](https://github.com/googleapis/java-storage/commit/41a1030a2e77036cf961a16d472068b07e624192))
  * update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.51.0 ([#2860](https://github.com/googleapis/java-storage/issues/2860)) ([980ac4e](https://github.com/googleapis/java-storage/commit/980ac4ebe09636d0de255e89f747bde8cc9ce041))
  * update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.52.0 ([#2883](https://github.com/googleapis/java-storage/issues/2883)) ([a64a3d5](https://github.com/googleapis/java-storage/commit/a64a3d58410dd2e9db20a36cd7169037f71eaeeb))
  * update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.59.0 ([f5d8337](https://github.com/googleapis/java-storage/commit/f5d8337ad556770a55cc260975e44e85e8e831b0))
  * update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.59.0 ([5480ce3](https://github.com/googleapis/java-storage/commit/5480ce347493ec425b675f462a42f45c22b06c28))
  * update googleapis/sdk-platform-java action to v2.51.1 ([#2864](https://github.com/googleapis/java-storage/issues/2864)) ([b731c06](https://github.com/googleapis/java-storage/commit/b731c06b11186e9695fb89f32abf35988d558bc9))
  * update googleapis/sdk-platform-java action to v2.55.1 ([#2985](https://github.com/googleapis/java-storage/issues/2985)) ([e22a2de](https://github.com/googleapis/java-storage/commit/e22a2de0fe1dc66e6e5b6d311f4812c290177203))
  * update googleapis/sdk-platform-java action to v2.56.2 ([#3055](https://github.com/googleapis/java-storage/issues/3055)) ([7025ad7](https://github.com/googleapis/java-storage/commit/7025ad7db438741ab6d74d5e3f768d0a2bd4da5c))
  * update googleapis/sdk-platform-java action to v2.60.1 ([#3196](https://github.com/googleapis/java-storage/issues/3196)) ([6ba56e5](https://github.com/googleapis/java-storage/commit/6ba56e5a4b86a75a9f48beccf79ff6d5fdd3e19f))
  * update googleapis/sdk-platform-java action to v2.62.1 ([#3281](https://github.com/googleapis/java-storage/issues/3281)) ([c9078bb](https://github.com/googleapis/java-storage/commit/c9078bb98e3999234f95ab2e4c842c9dd7191c3d))
  * update googleapis/sdk-platform-java action to v2.62.2 ([#3299](https://github.com/googleapis/java-storage/issues/3299)) ([c3b05ac](https://github.com/googleapis/java-storage/commit/c3b05ac8798140f9ddcab098948a3a2f3638dc6b))
  * update googleapis/sdk-platform-java action to v2.62.3 ([#3322](https://github.com/googleapis/java-storage/issues/3322)) ([a5808ea](https://github.com/googleapis/java-storage/commit/a5808ea168a81f07040276c1a05da67108fda37f))
  * update sdk-platform-java dependencies ([#2841](https://github.com/googleapis/java-storage/issues/2841)) ([2a70481](https://github.com/googleapis/java-storage/commit/2a704815ee60b8ec7ff2c1af557fee4366ea2e19))
  * update sdk-platform-java dependencies ([#2866](https://github.com/googleapis/java-storage/issues/2866)) ([562df7f](https://github.com/googleapis/java-storage/commit/562df7f087b34db0f3d49c6e0b87643a606ef9c6))
  * update sdk-platform-java dependencies ([#2921](https://github.com/googleapis/java-storage/issues/2921)) ([fa9b0a8](https://github.com/googleapis/java-storage/commit/fa9b0a8d6e2b185c0588d824329b409718bef302))
  * update sdk-platform-java dependencies ([#2957](https://github.com/googleapis/java-storage/issues/2957)) ([40cfda6](https://github.com/googleapis/java-storage/commit/40cfda62d4bff72a857d0269eaa7c0225f216650))
  * update sdk-platform-java dependencies ([#2983](https://github.com/googleapis/java-storage/issues/2983)) ([9eeb82a](https://github.com/googleapis/java-storage/commit/9eeb82af81ad8095c21542808a8eaa5098dee074))
  * update sdk-platform-java dependencies ([#2986](https://github.com/googleapis/java-storage/issues/2986)) ([10b922a](https://github.com/googleapis/java-storage/commit/10b922a8ae831fcd0107abf54091566442ae5fde))
  * update sdk-platform-java dependencies ([#3046](https://github.com/googleapis/java-storage/issues/3046)) ([861f958](https://github.com/googleapis/java-storage/commit/861f9586e041f65061fb3da7f88955c4214d450c))
  * update sdk-platform-java dependencies ([#3053](https://github.com/googleapis/java-storage/issues/3053)) ([921d1ba](https://github.com/googleapis/java-storage/commit/921d1ba0a547242c70cbb7dfb2cb190fa761398f))
  * update sdk-platform-java dependencies ([#3087](https://github.com/googleapis/java-storage/issues/3087)) ([762ca13](https://github.com/googleapis/java-storage/commit/762ca1374a8e738fbafc49d17fd38375962d026f))
  * update sdk-platform-java dependencies ([#3102](https://github.com/googleapis/java-storage/issues/3102)) ([3b53b94](https://github.com/googleapis/java-storage/commit/3b53b942f31805c5291ca109b4f3e501fbc6fc0d))
  * update sdk-platform-java dependencies ([#3129](https://github.com/googleapis/java-storage/issues/3129)) ([31cd058](https://github.com/googleapis/java-storage/commit/31cd058dcaf5a891ecb7a955602b09634d912560))
  * update sdk-platform-java dependencies ([#3152](https://github.com/googleapis/java-storage/issues/3152)) ([2f78192](https://github.com/googleapis/java-storage/commit/2f78192d97e9d3ca29c97a52a66a074777dce196))
  * update sdk-platform-java dependencies ([#3164](https://github.com/googleapis/java-storage/issues/3164)) ([c22a131](https://github.com/googleapis/java-storage/commit/c22a1319d8e2d92beeb03abac6bf2af8d09d49ee))
  * update sdk-platform-java-config to 3.55.0-rc1 ([#3434](https://github.com/googleapis/java-storage/issues/3434)) ([25283cb](https://github.com/googleapis/java-storage/commit/25283cb7ecc6ef4e22d4b551821641a1a218eaf9))



##### Documentation

  * add explicit Optional annotations to fields that have always been treated as optional ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
  * add note about HNS support to moveBlob ([#2929](https://github.com/googleapis/java-storage/issues/2929)) ([c461546](https://github.com/googleapis/java-storage/commit/c461546bfd016b21eb99f8e25604ee3fd001c9c6))
  * add note that Bucket.project output format is always project number format ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
  * add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
  * add samples for soft delete (objects) ([#2754](https://github.com/googleapis/java-storage/issues/2754)) ([41bc807](https://github.com/googleapis/java-storage/commit/41bc807e94f1c0eebd41b4a7baa12301858cc16f))
  * Create OpenTelemetry Quickstart Sample ([#2861](https://github.com/googleapis/java-storage/issues/2861)) ([31df9b7](https://github.com/googleapis/java-storage/commit/31df9b7a6350714ff354934ccbd27c5dd68762f5))
  * update storage_copy_file to include MegabytesCopiedPerChunk ([#2910](https://github.com/googleapis/java-storage/issues/2910)) ([971ca5d](https://github.com/googleapis/java-storage/commit/971ca5d107967960e6db6ca76a55e44b9aefc605))



## December 16, 2025

Feature

You can now generate [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) for activity data to receive insights about object mutations, errors, and activity trends across projects, buckets, and regions. For more information, see [Dataset schema for activity data tables](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema).

Feature

You can now use Rapid Cache to serve data for object read requests issued by BigQuery to accelerate data reads for your applications. For more information, see [Using Rapid Cache to accelerate reads for BigQuery](https://docs.cloud.google.com/storage/docs/anywhere-cache#integrations).

## December 15, 2025

Libraries

### Python

#### [3.7.0](https://github.com/googleapis/python-storage/compare/v3.6.0...v3.7.0) (2025-12-09)

##### Features

  * Auto enable mTLS when supported certificates are detected ([#1637](https://github.com/googleapis/python-storage/issues/1637)) ([4e91c54](https://github.com/googleapis/python-storage/commit/4e91c541363f0e583bf9dd1b81a95ff2cb618bac))
  * Send entire object checksum in the final api call of resumable upload ([#1654](https://github.com/googleapis/python-storage/issues/1654)) ([ddce7e5](https://github.com/googleapis/python-storage/commit/ddce7e53a13e6c0487221bb14e88161da7ed9e08))
  * Support urllib3 >= 2.6.0 ([#1658](https://github.com/googleapis/python-storage/issues/1658)) ([57405e9](https://github.com/googleapis/python-storage/commit/57405e956a7ca579b20582bf6435cec42743c478))



##### Bug Fixes

  * **bucket:** Move blob fails when the new blob name contains characters that need to be url encoded ([#1605](https://github.com/googleapis/python-storage/issues/1605)) ([ec470a2](https://github.com/googleapis/python-storage/commit/ec470a270e189e137c7229cc359367d5a897cdb9))



## November 24, 2025

Libraries

### Python

#### [3.6.0](https://github.com/googleapis/python-storage/compare/v3.5.0...v3.6.0) (2025-11-17)

##### Features

  * Add support for partial list buckets ([#1606](https://github.com/googleapis/python-storage/issues/1606)) ([92fc2b0](https://github.com/googleapis/python-storage/commit/92fc2b00429415b9fbe7cba0167778eee60449e2))
  * Make return_partial_success and unreachable fields public for list Bucket ([#1601](https://github.com/googleapis/python-storage/issues/1601)) ([323cddd](https://github.com/googleapis/python-storage/commit/323cddd5d439e04e12614106eab1928fd4008c0b))
  * **zb-experimental:** Add async write object stream ([5ab8103](https://github.com/googleapis/python-storage/commit/5ab81032268e875f82a66431d666fe61c9eb394b))
  * **zb-experimental:** Add async write object stream ([#1612](https://github.com/googleapis/python-storage/issues/1612)) ([5ab8103](https://github.com/googleapis/python-storage/commit/5ab81032268e875f82a66431d666fe61c9eb394b))



##### Bug Fixes

  * Don't pass credentials to StorageClient ([#1608](https://github.com/googleapis/python-storage/issues/1608)) ([195d644](https://github.com/googleapis/python-storage/commit/195d644c4d4feec98e9a9cd9fad67fc774c50dc8))



## November 14, 2025

Feature

You can now use the Google Cloud console to [relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview). Using bucket relocation, you can move an existing bucket from one location to another without changing the bucket's name or requiring manual transfer of data within the bucket.

## November 11, 2025

Feature

You can now enable [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

## November 10, 2025

Libraries

### Python

#### [3.5.0](https://github.com/googleapis/python-storage/compare/v3.4.1...v3.5.0) (2025-11-05)

##### Features

  * Ensure that Python in FIPS mode can fetch MD5 implementation ([#1522](https://github.com/googleapis/python-storage/issues/1522)) ([961536c](https://github.com/googleapis/python-storage/commit/961536c7bf3652a824c207754317030526b9dd28))
  * Provide option to update `user_agent` ([#1596](https://github.com/googleapis/python-storage/issues/1596)) ([02f1451](https://github.com/googleapis/python-storage/commit/02f1451aaa8dacd10a862e97abb62ae48249b9b4))



##### Bug Fixes

  * Deprecate credentials_file argument ([74415a2](https://github.com/googleapis/python-storage/commit/74415a2a120e9bfa42f4f5fc8bd2f8e0d4cf5d18))
  * Flaky system tests for resumable_media ([#1592](https://github.com/googleapis/python-storage/issues/1592)) ([7fee3dd](https://github.com/googleapis/python-storage/commit/7fee3dd3390cfb5475a39d8f8272ea825dbda449))
  * Make `download_ranges` compatible with `asyncio.create_task(..)` ([#1591](https://github.com/googleapis/python-storage/issues/1591)) ([faf8b83](https://github.com/googleapis/python-storage/commit/faf8b83b1f0ac378f8f6f47ce33dc23a866090c9))
  * Make `download_ranges` compatible with `asyncio.create_task(..)` ([#1591](https://github.com/googleapis/python-storage/issues/1591)) ([faf8b83](https://github.com/googleapis/python-storage/commit/faf8b83b1f0ac378f8f6f47ce33dc23a866090c9))
  * Redact sensitive data from OTEL traces and fix env var parsing ([#1553](https://github.com/googleapis/python-storage/issues/1553)) ([a38ca19](https://github.com/googleapis/python-storage/commit/a38ca1977694def98f65ae7239e300a987bbd262))
  * Redact sensitive data from OTEL traces and fix env var parsing ([#1553](https://github.com/googleapis/python-storage/issues/1553)) ([a38ca19](https://github.com/googleapis/python-storage/commit/a38ca1977694def98f65ae7239e300a987bbd262))
  * Use separate header object for each upload in Transfer Manager MPU ([#1595](https://github.com/googleapis/python-storage/issues/1595)) ([0d867bd](https://github.com/googleapis/python-storage/commit/0d867bd4f405d2dbeca1edfc8072080c5a96c1cd))



### Java

#### [2.60.0](https://github.com/googleapis/java-storage/compare/v2.59.0...v2.60.0) (2025-11-07)

##### Features

  * Add preview MultipartUploadClient#abortMultipartUpload https://github.com/googleapis/java-storage/pull/3361 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * Add preview MultipartUploadClient#completeMultipartUpload https://github.com/googleapis/java-storage/pull/3372 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * Add preview MultipartUploadClient#createMultipartUpload https://github.com/googleapis/java-storage/pull/3356 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * Add preview MultipartUploadClient#listParts https://github.com/googleapis/java-storage/pull/3359 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * Add preview MultipartUploadClient#uploadPart https://github.com/googleapis/java-storage/pull/3375 ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))
  * Add preview MultipartUploadSettings ([160fa9a](https://github.com/googleapis/java-storage/commit/160fa9af7aa492373a9d9b40f65a6c56d7cab5ef))



##### Bug Fixes

  * Add new system property (com.google.cloud.storage.grpc.bound_token) to allow disabling bound token use with grpc ([#3365](https://github.com/googleapis/java-storage/issues/3365)) ([ebf5e6d](https://github.com/googleapis/java-storage/commit/ebf5e6d30d8dc197ab388a70cc0d465c0f740496))
  * Call response.disconnect() after resolving resumable upload url ([#3385](https://github.com/googleapis/java-storage/issues/3385)) ([ac3be4b](https://github.com/googleapis/java-storage/commit/ac3be4b7e82d9340ede7d527a26ffe3e2ba58909))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([c1a8968](https://github.com/googleapis/java-storage/commit/c1a8968799c1cf5a970fe9f303adccdad0a117c8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#3381](https://github.com/googleapis/java-storage/issues/3381)) ([e3d3700](https://github.com/googleapis/java-storage/commit/e3d3700e06de2b0113e1cb01e99ef4aeed3c62c9))



## November 03, 2025

Libraries

### Go

#### [1.57.1](https://github.com/googleapis/google-cloud-go/compare/storage/v1.57.0...storage/v1.57.1) (2025-10-28)

##### Bug Fixes

  * **storage:** Takeover idempotence. ([#13230](https://github.com/googleapis/google-cloud-go/issues/13230)) ([cc5d2a1](https://github.com/googleapis/google-cloud-go/commit/cc5d2a12293a509a14da9bea8a86c8655eaf4a71))
  * **storage:** Copy metadata when using Copier with grpc ([#12919](https://github.com/googleapis/google-cloud-go/issues/12919)) ([57a2e80](https://github.com/googleapis/google-cloud-go/commit/57a2e804f690ec8d4c55fd1c73b0dafd5cff46e5))
  * **storage:** Fix takeover response handling. ([#13239](https://github.com/googleapis/google-cloud-go/issues/13239)) ([26d75bc](https://github.com/googleapis/google-cloud-go/commit/26d75bc08e242348d26691877aba7fa68cf30f7f))
  * **storage:** Remove default timeout for gRPC operations ([#13022](https://github.com/googleapis/google-cloud-go/issues/13022)) ([b94c3ba](https://github.com/googleapis/google-cloud-go/commit/b94c3ba69994d9c56ae8f302449dd8df6f287296))
  * **storage:** Skip download of file outside of target dir ([#12945](https://github.com/googleapis/google-cloud-go/issues/12945)) ([6259aee](https://github.com/googleapis/google-cloud-go/commit/6259aeec393d0d996961cac38396daa57ad1a290))
  * **storage:** Upgrade gRPC service registration func ([8fffca2](https://github.com/googleapis/google-cloud-go/commit/8fffca2819fa3dc858c213aa0c503e0df331b084))



## October 27, 2025

Libraries

### Java

#### [2.59.0](https://github.com/googleapis/java-storage/compare/v2.58.1...v2.59.0) (2025-10-21)

##### Features

  * Add per-message checksum validation for gRPC ReadObject operations ([#3336](https://github.com/googleapis/java-storage/issues/3336)) ([6eef1b0](https://github.com/googleapis/java-storage/commit/6eef1b0f587b9f32041ac4bcef1a16b1b0bc4bb3))



##### Bug Fixes

  * Add case insensitive check for X-Goog-Content-SHA256 in SignatureInfo ([#3337](https://github.com/googleapis/java-storage/issues/3337)) ([54bc2c1](https://github.com/googleapis/java-storage/commit/54bc2c12f2d0e8c164e4ddcaa1a61d2de3911131))
  * Migrate away from GoogleCredentials.fromStream() usages ([#3339](https://github.com/googleapis/java-storage/issues/3339)) ([7e42c2f](https://github.com/googleapis/java-storage/commit/7e42c2fbca53ca6b1266f784e58cee00cfed7d62))
  * Update BlobReadSession channels to not implicitly close once EOF is observed ([#3344](https://github.com/googleapis/java-storage/issues/3344)) ([9f0a93e](https://github.com/googleapis/java-storage/commit/9f0a93eb4c6bb8aab13915ca1cb40ba9e229a2f9))
  * Update grpc single-shot uploads to attach the callers stracktrace as suppressed exception if an error happens in the background ([#3330](https://github.com/googleapis/java-storage/issues/3330)) ([64e2b2e](https://github.com/googleapis/java-storage/commit/64e2b2ef839e69da0605b9e53989c1f5a2b09e66))
  * Update retry logic for grpc start resumable upload to properly handle client side deadline_exceeded ([#3354](https://github.com/googleapis/java-storage/issues/3354)) ([6eb3331](https://github.com/googleapis/java-storage/commit/6eb33311d8dd7344e30ddcb92334fd52c7c63b4d))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#3351](https://github.com/googleapis/java-storage/issues/3351)) ([e64565a](https://github.com/googleapis/java-storage/commit/e64565ab674f586ea4850408a3f30544997f4b1b))



## October 23, 2025

Feature

You can now use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) to create and manage [retention configurations](https://docs.cloud.google.com/storage/docs/metadata#retention-config) for objects in bulk using the `PutMetadata` transformation.

## October 20, 2025

Libraries

### Go

#### [1.56.3](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.2...storage/v1.56.3) (2025-10-14)

##### Bug Fixes

  * **storage:** Persist resource in append retry ([#13128](https://github.com/googleapis/google-cloud-go/issues/13128)) ([9ad2100](https://github.com/googleapis/google-cloud-go/commit/9ad2100ab53801be483492e8ff87662c43c846f8))



## October 13, 2025

Libraries

### Java

#### [2.58.1](https://github.com/googleapis/java-storage/compare/v2.58.0...v2.58.1) (2025-10-06)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([ba84793](https://github.com/googleapis/java-storage/commit/ba847937e553f6a47aa459f634f63ed42310762d))
  * Update BlobReadSession ScatteringByteChannel projection to use less CPU ([#3324](https://github.com/googleapis/java-storage/issues/3324)) ([678fecc](https://github.com/googleapis/java-storage/commit/678feccc972e557380e9ba5fcd52be099440197d))
  * Update DefaultRetryContext to trap and forward RejectedExceptionException to onFailure ([#3327](https://github.com/googleapis/java-storage/issues/3327)) ([1be31bd](https://github.com/googleapis/java-storage/commit/1be31bdfbc0283733e86b049d3be1911db50fb96))
  * Update PCU request building logic to properly clear crc32c and md5 ([#3323](https://github.com/googleapis/java-storage/issues/3323)) ([4da9f31](https://github.com/googleapis/java-storage/commit/4da9f3108d27f5c2ed3cc39eec161651f421e4db))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250925-2.0.0 ([#3313](https://github.com/googleapis/java-storage/issues/3313)) ([ab310eb](https://github.com/googleapis/java-storage/commit/ab310eb5af51ed332329abd6c3441d18f9965571))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#3325](https://github.com/googleapis/java-storage/issues/3325)) ([4d3e3be](https://github.com/googleapis/java-storage/commit/4d3e3be27811ad92becc93321048c4268cec2fcf))
  * Update googleapis/sdk-platform-java action to v2.62.3 ([#3322](https://github.com/googleapis/java-storage/issues/3322)) ([a5808ea](https://github.com/googleapis/java-storage/commit/a5808ea168a81f07040276c1a05da67108fda37f))



### Python

#### [3.4.1](https://github.com/googleapis/python-storage/compare/v3.4.0...v3.4.1) (2025-10-08)

##### Bug Fixes

  * Fixes [#1561](https://github.com/googleapis/python-storage/issues/1561) by adding an option to specify the entire object checksum for resumable uploads via the `upload_from_string`, `upload_from_file`, and `upload_from_filename` methods ([acb918e](https://github.com/googleapis/python-storage/commit/acb918e20f7092e13d72fc63fe4ae2560bfecd40))



## September 30, 2025

Feature

[Object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) are now available in [Preview](https://cloud.google.com/products#product-launch-stages). Object contexts let you attach contextual information to your objects to help you manage and discover data.

## September 29, 2025

Libraries

### Java

#### [2.58.0](https://github.com/googleapis/java-storage/compare/v2.57.0...v2.58.0) (2025-09-23)

##### Features

  * **storagecontrol:** Add GetIamPolicy, SetIamPolicy, and TestIamPermissions RPCs ([c884551](https://github.com/googleapis/java-storage/commit/c884551048a323f2a3fd7aaf4fce469d4d4f543e))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([984f8ca](https://github.com/googleapis/java-storage/commit/984f8ca23a38c7a892a2256a694b72431e44aa27))
  * Fix appendable upload finalization race condition ([#3295](https://github.com/googleapis/java-storage/issues/3295)) ([485be18](https://github.com/googleapis/java-storage/commit/485be184c08c7b857d8c9a9443f32903df879b23))
  * Fix IllegalMonitorStateException thrown from BlobAppendableUpload.isOpen() ([#3302](https://github.com/googleapis/java-storage/issues/3302)) ([aa90468](https://github.com/googleapis/java-storage/commit/aa904688b784d7427454318196ef88628e415246))
  * Update object context diff logic to be shallow rather than deep ([#3287](https://github.com/googleapis/java-storage/issues/3287)) ([2fd15f6](https://github.com/googleapis/java-storage/commit/2fd15f69e93a3df2b8dbbd4f08edd07c087e957c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#3298](https://github.com/googleapis/java-storage/issues/3298)) ([1489f3a](https://github.com/googleapis/java-storage/commit/1489f3a74c8a27f0888c40600c83adedcfd9a9ec))
  * Update googleapis/sdk-platform-java action to v2.62.2 ([#3299](https://github.com/googleapis/java-storage/issues/3299)) ([c3b05ac](https://github.com/googleapis/java-storage/commit/c3b05ac8798140f9ddcab098948a3a2f3638dc6b))



### Go

#### [1.57.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.1...storage/v1.57.0) (2025-09-23)

##### Features

  * **storage/control:** Add new GetIamPolicy, SetIamPolicy, and TestIamPermissions RPCs ([d73f912](https://github.com/googleapis/google-cloud-go/commit/d73f9123be77bb3278f48d510cd0fb22feb605bc))
  * **storage:** Post support dynamic key name ([#12677](https://github.com/googleapis/google-cloud-go/issues/12677)) ([9e761f9](https://github.com/googleapis/google-cloud-go/commit/9e761f961a2c4351b3e0793ed655314ac5853903))
  * **storage:** WithMeterProvider allows custom meter provider configuration ([#12668](https://github.com/googleapis/google-cloud-go/issues/12668)) ([7f574b0](https://github.com/googleapis/google-cloud-go/commit/7f574b01e0b454c1ef5c13e6a58075e394ee990d))



##### Bug Fixes

  * **storage:** Free buffers in Bidi Reader ([#12839](https://github.com/googleapis/google-cloud-go/issues/12839)) ([bc247fd](https://github.com/googleapis/google-cloud-go/commit/bc247fdc3f5234a8bd6934e58d5b0b578f1335cb))
  * **storage:** Make Writer thread-safe. ([#12753](https://github.com/googleapis/google-cloud-go/issues/12753)) ([9ea380b](https://github.com/googleapis/google-cloud-go/commit/9ea380bea5b980a9054d201be4f315a195da2182))
  * **storage:** No progress report for oneshot write ([#12746](https://github.com/googleapis/google-cloud-go/issues/12746)) ([b97c286](https://github.com/googleapis/google-cloud-go/commit/b97c286ec369a10a81b1a8a3a1aae18b46d2dfbc))



##### Performance Improvements

  * **storage:** Pipeline gRPC writes ([#12422](https://github.com/googleapis/google-cloud-go/issues/12422)) ([1f2c5fe](https://github.com/googleapis/google-cloud-go/commit/1f2c5fe2843724302086fe04cb8dab8b515969c5))



## September 22, 2025

Libraries

### Python

#### [3.4.0](https://github.com/googleapis/python-storage/compare/v3.3.1...v3.4.0) (2025-09-15)

##### Features

  * **experimental:** Add async grpc client ([#1537](https://github.com/googleapis/python-storage/issues/1537)) ([ac57b8d](https://github.com/googleapis/python-storage/commit/ac57b8d819a49aef0ed0cb5bb630bf11012f43e3))
  * **experimental:** Add grpc client ([#1533](https://github.com/googleapis/python-storage/issues/1533)) ([5674587](https://github.com/googleapis/python-storage/commit/5674587f2aa347ec2787f2bc1e847eaa294bc1ca))



##### Bug Fixes

  * GAPIC generation failed with 'Directory not empty' ([#1542](https://github.com/googleapis/python-storage/issues/1542)) ([c80d820](https://github.com/googleapis/python-storage/commit/c80d8207a8661b84c56cd66bb34de7b5704675b8))



### Go

#### [1.56.2](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.1...storage/v1.56.2) (2025-09-15)

##### Bug Fixes

  * **storage:** Free buffers in Bidi Reader ([#12839](https://github.com/googleapis/google-cloud-go/issues/12839)) ([10c8fac](https://github.com/googleapis/google-cloud-go/commit/10c8faccc2dae2a8177ff30ab16d67413df9f536))



## September 17, 2025

Feature

The `bucket_attributes_view` and `bucket_attributes_latest_snapshot_view` tables in [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) are updated with two new fields: `objectCount` and `totalSize`. `objectCount` reflects the total number of objects in the bucket and `totalSize` reflects the total size of the bucket in bytes. The tables are automatically updated with the new fields in all existing datasets and are included in all new dataset configurations.

## September 15, 2025

Libraries

### Java

#### [2.57.0](https://github.com/googleapis/java-storage/compare/v2.56.0...v2.57.0) (2025-09-09)

##### Features

  * Add BlobInfo.ObjectContexts ([#3259](https://github.com/googleapis/java-storage/issues/3259)) ([485aefd](https://github.com/googleapis/java-storage/commit/485aefd3047c52c98d8bd913033c8aee1473e988))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([0e348db](https://github.com/googleapis/java-storage/commit/0e348dbee247e1e65713d0155e1aa29ae5c5e0e4))
  * Update BlobAppendableUpload implementation to periodically flush for large writes ([#3278](https://github.com/googleapis/java-storage/issues/3278)) ([d0ffe18](https://github.com/googleapis/java-storage/commit/d0ffe18084b32936c889bb280005294c7ae7064d))
  * Update otel integration to properly activate span context for lazy RPCs such as reads & writes pt.2 ([#3277](https://github.com/googleapis/java-storage/issues/3277)) ([3240f67](https://github.com/googleapis/java-storage/commit/3240f67c192a855c92256526aeb2fa689ea15445))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#3280](https://github.com/googleapis/java-storage/issues/3280)) ([d046ea3](https://github.com/googleapis/java-storage/commit/d046ea3da19288b64c48300bdd4f94a0ebf35458))
  * Update googleapis/sdk-platform-java action to v2.62.1 ([#3281](https://github.com/googleapis/java-storage/issues/3281)) ([c9078bb](https://github.com/googleapis/java-storage/commit/c9078bb98e3999234f95ab2e4c842c9dd7191c3d))



## September 10, 2025

Feature

Cloud Storage FUSE now supports buffered reads, which can improve sequential read performance for large files by two to five times. When enabled, Cloud Storage FUSE asynchronously prefetches parts of a file into an in-memory buffer, allowing subsequent reads to be served from the buffer instead of requiring network calls.

To learn more about buffered reads, see [Enable buffered reads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#enable-buffered-reads).

## September 01, 2025

Libraries

### Java

#### [2.56.0](https://github.com/googleapis/java-storage/compare/v2.55.0...v2.56.0) (2025-08-25)

##### Features

  * _breaking behavior_ rewrite Storage.blobAppendableUpload to be non-blocking and have improved throughput ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * Add AppendableUploadWriteableByteChannel#flush() ([#3261](https://github.com/googleapis/java-storage/issues/3261)) ([950c56f](https://github.com/googleapis/java-storage/commit/950c56f0e622d75faff51257d5cbc9f3ddc7e1ce))
  * Add MinFlushSizeFlushPolicy#withMaxPendingBytes(long) ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * Add StorageChannelUtils to provide helper methods to perform blocking read/write to/from non-blocking channels ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))



##### Bug Fixes

  * Make FlushPolicy${Min,Max}FlushSizeFlushPolicy constructors private ([#3217](https://github.com/googleapis/java-storage/issues/3217)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * Update BlobAppendableUploadConfig and FlushPolicy.MinFlushSizeFlushPolicy to default to 4MiB minFlushSize and 16MiB maxPendingBytes ([#3249](https://github.com/googleapis/java-storage/issues/3249)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
  * Update otel integration to properly activate span context for lazy RPCs such as reads & writes ([#3255](https://github.com/googleapis/java-storage/issues/3255)) ([d6587f4](https://github.com/googleapis/java-storage/commit/d6587f42b65a586a2e3f30e0559975801726a812))



##### Dependencies

  * Update actions/checkout action to v5 ([#3239](https://github.com/googleapis/java-storage/issues/3239)) ([33f024b](https://github.com/googleapis/java-storage/commit/33f024b1ae094bf3e3605e1a835cb55eb5c9e750))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250815-2.0.0 ([#3245](https://github.com/googleapis/java-storage/issues/3245)) ([87afe1a](https://github.com/googleapis/java-storage/commit/87afe1ac5f500053e4c0639d5b824304d03796f4))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#3250](https://github.com/googleapis/java-storage/issues/3250)) ([0782e62](https://github.com/googleapis/java-storage/commit/0782e62fc9534e3cecfaaa4d78b58904ecf699d6))



### Python

#### [3.3.1](https://github.com/googleapis/python-storage/compare/v3.3.0...v3.3.1) (2025-08-25)

##### Bug Fixes

  * Provide option to user to set entire object checksum at "initiate a resumable upload session" and send the same.([#1525](https://github.com/googleapis/python-storage/issues/1525)) ([a8109e0](https://github.com/googleapis/python-storage/commit/a8109e0d02c62542f1bea20373b53864fb776caa))
  * Send part's checksum for XML MPU part upload ([#1529](https://github.com/googleapis/python-storage/issues/1529)) ([2ad77c7](https://github.com/googleapis/python-storage/commit/2ad77c7d949e84c515c051a0fd4b37b822788dd8))



## August 28, 2025

Change

Beginning October 31, 2025, if you set an object's `age` condition to a value of `0` when setting Object Lifecycle Management rules, the condition is satisfied at midnight UTC after the object is created, which helps reduce unintended data loss. To learn more about the `age` condition, see [Lifecycle conditions](https://docs.cloud.google.com/storage/docs/lifecycle#conditions).

## August 25, 2025

Libraries

### Go

#### [1.56.1](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.0...storage/v1.56.1) (2025-08-19)

##### Bug Fixes

  * **storage:** Fix redirect logic in MRD ([#12733](https://github.com/googleapis/google-cloud-go/issues/12733)) ([9f369f9](https://github.com/googleapis/google-cloud-go/commit/9f369f931853220550cabb3d67a5a5d3d9e137ba))
  * **storage:** Pass all user options to NewService ([#12615](https://github.com/googleapis/google-cloud-go/issues/12615)) ([77cdb83](https://github.com/googleapis/google-cloud-go/commit/77cdb832a374eba29e4de7699324a87f1d20eea3))
  * **storage:** ZB Reader redirect support ([#12703](https://github.com/googleapis/google-cloud-go/issues/12703)) ([3c7ea5c](https://github.com/googleapis/google-cloud-go/commit/3c7ea5ceb199d5787d36bf8f415f028bea66e3b5))



## August 18, 2025

Libraries

### Python

#### [3.3.0](https://github.com/googleapis/python-storage/compare/v3.2.0...v3.3.0) (2025-08-05)

##### Features

  * Add support for bucket IP filter ([#1516](https://github.com/googleapis/python-storage/issues/1516)) ([a29073c](https://github.com/googleapis/python-storage/commit/a29073cf58df9c5667305e05c6378284057cda23))



##### Bug Fixes

  * Add logs on AssertionError for issue [#1512](https://github.com/googleapis/python-storage/issues/1512) ([#1518](https://github.com/googleapis/python-storage/issues/1518)) ([6a9923e](https://github.com/googleapis/python-storage/commit/6a9923e4fc944f7a7c3906eb7800d23677bd2481))



##### Documentation

  * Update the documentation of move_blob function ([#1507](https://github.com/googleapis/python-storage/issues/1507)) ([72252e9](https://github.com/googleapis/python-storage/commit/72252e940909ce2e3da9cfd80f5b7b43a026f45c))



## August 12, 2025

Feature

You can now use Anywhere Cache in the `asia-south1-b` and `asia-south1-c` zones. For more information, see [Anywhere Cache supported locations](https://docs.cloud.google.com/storage/docs/anywhere-cache#supported-locations).

## August 11, 2025

Libraries

### Java

#### [2.55.0](https://github.com/googleapis/java-storage/compare/v2.54.0...v2.55.0) (2025-08-05)

##### Features

  * Add new preview Bucket encryption policy configuration ([#3204](https://github.com/googleapis/java-storage/issues/3204)) ([7b250dd](https://github.com/googleapis/java-storage/commit/7b250dd53cfa29bbb6a0a4cb4a345aeb2dab5c86))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([f98b686](https://github.com/googleapis/java-storage/commit/f98b686ef940879458acb1e56339adf869400b94))
  * Enable ALTS bound token (for DirectPath) in the grpc channel provider ([#2919](https://github.com/googleapis/java-storage/issues/2919)) ([38d248d](https://github.com/googleapis/java-storage/commit/38d248d9511e808e88c1bac0b6bb2ba54897830d))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#3213](https://github.com/googleapis/java-storage/issues/3213)) ([86ff697](https://github.com/googleapis/java-storage/commit/86ff69788b30d8f82b6b95d010df507093852889))



Feature

You can now use Anywhere Cache in the `asia-south1-a` zone. For more information, see [Anywhere Cache supported locations](https://docs.cloud.google.com/storage/docs/anywhere-cache#supported-locations).

## August 04, 2025

Libraries

### Java

#### [2.54.0](https://github.com/googleapis/java-storage/compare/v2.53.3...v2.54.0) (2025-07-24)

##### Features

  * Add BucketInfo.IpFilter ([#3177](https://github.com/googleapis/java-storage/issues/3177)) ([14a91ec](https://github.com/googleapis/java-storage/commit/14a91ec208067e6afc55923cffda5f69aa33d8b4))
  * Add default end-to-end checksumming for JournalingBlobWriteSessionConfig [#3180](https://github.com/googleapis/java-storage/issues/3180) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * Add default end-to-end crc32c checksumming for several upload methods via grpc transport [#3176](https://github.com/googleapis/java-storage/issues/3176) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([bd1f199](https://github.com/googleapis/java-storage/commit/bd1f199cf57c2b8039c303586d5beac64aeca0ba))
  * Give user provided checksum precondition priority for Storage#create methods that accept byte[] [#3182](https://github.com/googleapis/java-storage/issues/3182) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
  * Move crc32c computation before writing to disk for BufferToDiskThenUpload BlobWriteSession config [#3187](https://github.com/googleapis/java-storage/issues/3187) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250718-2.0.0 ([#3203](https://github.com/googleapis/java-storage/issues/3203)) ([18978e4](https://github.com/googleapis/java-storage/commit/18978e4ec54790df2939490ef76fc19b9f72eb04))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#3201](https://github.com/googleapis/java-storage/issues/3201)) ([782c3c4](https://github.com/googleapis/java-storage/commit/782c3c416583704a196b17f23e9c12c33659f67d))
  * Update googleapis/sdk-platform-java action to v2.60.1 ([#3196](https://github.com/googleapis/java-storage/issues/3196)) ([6ba56e5](https://github.com/googleapis/java-storage/commit/6ba56e5a4b86a75a9f48beccf79ff6d5fdd3e19f))



## July 28, 2025

Libraries

### Go

#### [1.56.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.55.0...storage/v1.56.0) (2025-07-24)

##### Features

  * **storage/control:** Update BUILD configs to support rest transportation for all client ([116a33a](https://github.com/googleapis/google-cloud-go/commit/116a33ab13c9fac6f6830dded55c24d38504707b))



##### Bug Fixes

  * **storage:** Avoid integration test segfaults. ([#12419](https://github.com/googleapis/google-cloud-go/issues/12419)) ([a9dec07](https://github.com/googleapis/google-cloud-go/commit/a9dec0763f85f083cc1da451249caae7ad97d904))
  * **storage:** Current object generation takeover. ([#12383](https://github.com/googleapis/google-cloud-go/issues/12383)) ([9ca8e01](https://github.com/googleapis/google-cloud-go/commit/9ca8e015405a523bbe68cbff2defbdff3dac0a61))
  * **storage:** Fix MultiRangeDownloader deadlock ([#12548](https://github.com/googleapis/google-cloud-go/issues/12548)) ([2eb23bb](https://github.com/googleapis/google-cloud-go/commit/2eb23bb01ffe92c967e772ef66c846357fbf5419))
  * **storage:** Remove object length limit for unfinalized reads ([#12489](https://github.com/googleapis/google-cloud-go/issues/12489)) ([5566d7d](https://github.com/googleapis/google-cloud-go/commit/5566d7dd5cc83afce38821961c447f5945e48456))



##### Performance Improvements

  * **storage:** Zero copy for MultiRangeDownloader ([#12542](https://github.com/googleapis/google-cloud-go/issues/12542)) ([a5e6a68](https://github.com/googleapis/google-cloud-go/commit/a5e6a681164d5be62270cde16891685a9f03bb12))



##### Documentation

  * **storage/internal:** Fix broken link for message `CustomPlacementConfig` ([9614487](https://github.com/googleapis/google-cloud-go/commit/96144875e01bfc8a59c2671c6eae87233710cef7))
  * **storage:** Fix typo in storage/doc.go ([#12391](https://github.com/googleapis/google-cloud-go/issues/12391)) ([bf74408](https://github.com/googleapis/google-cloud-go/commit/bf744088f0ed23ea510b914c994e1754ca1fc7c4))
  * **storage:** Improve error inspection documentation ([#12301](https://github.com/googleapis/google-cloud-go/issues/12301)) ([420da1a](https://github.com/googleapis/google-cloud-go/commit/420da1a64ac4040c8b2e6d6f0d66e7633426ac25))



## July 14, 2025

Libraries

### Java

#### [2.53.3](https://github.com/googleapis/java-storage/compare/v2.53.2...v2.53.3) (2025-07-09)

##### Bug Fixes

  * Fix DefaultBlobWriteSessionConfig init to work when grpc classes are excluded ([#3147](https://github.com/googleapis/java-storage/issues/3147)) ([8571ba8](https://github.com/googleapis/java-storage/commit/8571ba8eee82d055cdeb5f0b6970d5b814eaa24e))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250629-2.0.0 ([#3185](https://github.com/googleapis/java-storage/issues/3185)) ([4ce8281](https://github.com/googleapis/java-storage/commit/4ce8281246cbe84ed068205532cac4a03853c331))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#3189](https://github.com/googleapis/java-storage/issues/3189)) ([7fbfb01](https://github.com/googleapis/java-storage/commit/7fbfb013a8cfb72d49e3d752ad25e73b6ccaab4f))



Feature

[Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) offer the latest snapshot of the bucket and object metadata. The `bucket_attributes_latest_snapshot_view` and `object_attributes_latest_snapshot_view` views give you access to the latest metadata. Also, the `events_view` view has been updated with a `globalManifest.snapshotTime` column and an `eventCode` to track when the dataset was last refreshed.

## July 08, 2025

Feature

You can now create caches with Anywhere Cache in the `us-west3-a`, `us-west3-b`, and `us-west3-c` zones. For more information about supported locations for Anywhere Cache, see [Supported locations](https://docs.cloud.google.com/storage/docs/anywhere-cache#supported-locations).

## July 07, 2025

Libraries

### Python

#### [3.2.0](https://github.com/googleapis/python-storage/compare/v3.1.1...v3.2.0) (2025-07-04)

##### Features

  * Adding support of single shot download ([#1493](https://github.com/googleapis/python-storage/issues/1493)) ([61c5d5f](https://github.com/googleapis/python-storage/commit/61c5d5f62c88506f200bc6d86b399a2c28715bc4))



## July 02, 2025

Feature

[Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) for Cloud Storage is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Bucket IP filtering provides enhanced control over access to your data, allowing you to restrict incoming requests to your Cloud Storage buckets based on their source IP addresses or their Google Cloud Virtual Private Cloud.

## June 30, 2025

Libraries

### Java

#### [2.53.2](https://github.com/googleapis/java-storage/compare/v2.53.1...v2.53.2) (2025-06-25)

##### Bug Fixes

  * Fix Journaling BlobWriteSessionConfig to properly handle multiple consecutive retries ([#3166](https://github.com/googleapis/java-storage/issues/3166)) ([895bfbd](https://github.com/googleapis/java-storage/commit/895bfbda902a77d16a33fe5238349a6b3d397c10))



##### Dependencies

  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.36.0 ([#3162](https://github.com/googleapis/java-storage/issues/3162)) ([41a1030](https://github.com/googleapis/java-storage/commit/41a1030a2e77036cf961a16d472068b07e624192))
  * Update sdk-platform-java dependencies ([#3164](https://github.com/googleapis/java-storage/issues/3164)) ([c22a131](https://github.com/googleapis/java-storage/commit/c22a1319d8e2d92beeb03abac6bf2af8d09d49ee))



## June 23, 2025

Libraries

### Python

#### [3.1.1](https://github.com/googleapis/python-storage/compare/v3.1.0...v3.1.1) (2025-06-13)

##### Bug Fixes

  * Add a check for partial response data ([#1487](https://github.com/googleapis/python-storage/issues/1487)) ([7e0412a](https://github.com/googleapis/python-storage/commit/7e0412a4fdfedcaa4683d5ef7d9155d5d58efa11))
  * Add trove classifier for Python 3.13 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
  * **deps:** Require google-crc32c >= 1.1.3 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
  * **deps:** Require protobuf >= 3.20.2, < 7.0.0 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
  * **deps:** Require requests >= 2.22.0 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
  * Remove setup.cfg configuration for creating universal wheels ([#1448](https://github.com/googleapis/python-storage/issues/1448)) ([d3b6b3f](https://github.com/googleapis/python-storage/commit/d3b6b3f96a6f94aa7c371902f48d1363ae6bfb5c))
  * Resolve issue where pre-release versions of dependencies are installed ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
  * Segmentation fault in tink while writing data ([#1490](https://github.com/googleapis/python-storage/issues/1490)) ([2a46c0b](https://github.com/googleapis/python-storage/commit/2a46c0b9e6ec561ae3151d2a9a80c7452634487e))



##### Documentation

  * Move quickstart to top of readme ([#1451](https://github.com/googleapis/python-storage/issues/1451)) ([53257cf](https://github.com/googleapis/python-storage/commit/53257cf20a4de3810156ae9576a7092f5527df98))
  * Update README to break infinite redirect loop ([#1450](https://github.com/googleapis/python-storage/issues/1450)) ([03f1594](https://github.com/googleapis/python-storage/commit/03f1594eb90ea1298a3a23927537c86ac35d33d5))



### Java

#### [2.53.1](https://github.com/googleapis/java-storage/compare/v2.53.0...v2.53.1) (2025-06-18)

##### Bug Fixes

  * Cancel the future in RemoteStorageHelper#forceDelete when TimeoutException happens ([#3136](https://github.com/googleapis/java-storage/issues/3136)) ([e6007d5](https://github.com/googleapis/java-storage/commit/e6007d56e8801be65209cb5761f62749369425c9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([7dba9f0](https://github.com/googleapis/java-storage/commit/7dba9f09f100062cc8c04e5a2735a4349d8e7ed1))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250605-2.0.0 ([#3143](https://github.com/googleapis/java-storage/issues/3143)) ([17a80d8](https://github.com/googleapis/java-storage/commit/17a80d8b49fef65557215b310895b0f08ee25235))
  * Update sdk-platform-java dependencies ([#3152](https://github.com/googleapis/java-storage/issues/3152)) ([2f78192](https://github.com/googleapis/java-storage/commit/2f78192d97e9d3ca29c97a52a66a074777dce196))



Feature

The Cloud Storage Cloud Audit Logs have expanded support to include error scenario coverage and produce a more comprehensive error message with code, error messages, and details, in an easy to understand format. The Gemini Cloud Assist (GCA) service can then easily analyze the log and provide tailored recommendations on how to mitigate issues as they arise. Before this enhancement, error logs were generated for only a specific set of scenarios, and the status field solely contained the gRPC error code without any additional information. To learn more about Cloud Audit Logs, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).

## June 16, 2025

Feature

Cloud Storage FUSE version 3.0 is now available with new features and enhancements designed to improve performance and simplify configuration. Improvements include [automated configurations for high-performance machines](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations), a comprehensive [performance tuning guide](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance) to help optimize performance, and the new [`global-max-blocks` configuration option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#write-global-max-blocks), which gives you granular control over streaming write operations.

## June 09, 2025

Libraries

### Java

#### [2.53.0](https://github.com/googleapis/java-storage/compare/v2.52.3...v2.53.0) (2025-06-04)

##### Features

  * Expose BucketInfo.getProject as a BigInteger ([#3119](https://github.com/googleapis/java-storage/issues/3119)) ([64bbb60](https://github.com/googleapis/java-storage/commit/64bbb608033f757cb6e31e75a78740d8ed1dccab)), closes [#3023](https://github.com/googleapis/java-storage/issues/3023)
  * **storagecontrol:** Add Anywhere cache control APIs ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))
  * **storagecontrol:** Add Client Libraries Storage IntelligenceConfig ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250521-2.0.0 ([#3118](https://github.com/googleapis/java-storage/issues/3118)) ([e1be49e](https://github.com/googleapis/java-storage/commit/e1be49e6c987daccf9542c15c6ba418c007d2fb7))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250524-2.0.0 ([#3127](https://github.com/googleapis/java-storage/issues/3127)) ([2a4499d](https://github.com/googleapis/java-storage/commit/2a4499d1686e93e8495f29b5198488d166caaa06))
  * Update sdk-platform-java dependencies ([#3129](https://github.com/googleapis/java-storage/issues/3129)) ([31cd058](https://github.com/googleapis/java-storage/commit/31cd058dcaf5a891ecb7a955602b09634d912560))



##### Documentation

  * Add explicit Optional annotations to fields that have always been treated as optional ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
  * Add note that Bucket.project output format is always project number format ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
  * Add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))



## June 05, 2025

Change

The limit for the maximum number of prefixes and suffixes when using [matchesPrefix and matchesSuffix lifecycle conditions](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix) across all rules on a bucket is increased from 50 to 1,000. For more information, see [Quotas and limits](https://docs.cloud.google.com/storage/quotas#buckets).

## June 02, 2025

Libraries

### Go

#### [1.55.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.54.0...storage/v1.55.0) (2025-05-29)

##### Features

  * **storage/control:** Add Client Libraries Storage IntelligenceConfig ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
  * **storage/internal:** Add IpFilter to Bucket ([#12309](https://github.com/googleapis/google-cloud-go/issues/12309)) ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
  * **storage/internal:** Add Object.Retention message ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))



##### Bug Fixes

  * **storage:** Add EnableNewAuthLibrary internalOption to HTTP newClient ([#12320](https://github.com/googleapis/google-cloud-go/issues/12320)) ([0036073](https://github.com/googleapis/google-cloud-go/commit/0036073affee5451894654a983fba6b2638433cb))
  * **storage:** Migrate oauth2/google usages to cloud.google.com/go/auth ([#11191](https://github.com/googleapis/google-cloud-go/issues/11191)) ([3a22349](https://github.com/googleapis/google-cloud-go/commit/3a22349c1ba6a192d70269f77e5804a9957aa572))
  * **storage:** Omit check on MultiRangeDownloader ([#12342](https://github.com/googleapis/google-cloud-go/issues/12342)) ([774621c](https://github.com/googleapis/google-cloud-go/commit/774621c5baa5110f57fe79d817143416bd671d1e))
  * **storage:** Retry url.Error and net.OpErrors when they wrap an io.EOF ([#12289](https://github.com/googleapis/google-cloud-go/issues/12289)) ([080f6b0](https://github.com/googleapis/google-cloud-go/commit/080f6b05c5e8bd5baaef71ed47f8d54c695f63d3))



##### Documentation

  * **storage/internal:** Add explicit Optional annotations to fields that have always been treated as optional ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
  * **storage/internal:** Add note that Bucket.project output format is always project number format ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
  * **storage/internal:** Add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))



## May 26, 2025

Libraries

### Java

#### [2.52.3](https://github.com/googleapis/java-storage/compare/v2.52.2...v2.52.3) (2025-05-19)

##### Bug Fixes

  * Update grpc client side metrics detection to be graceful when not running on gcp ([#3097](https://github.com/googleapis/java-storage/issues/3097)) ([10cd32d](https://github.com/googleapis/java-storage/commit/10cd32d51aa061304b5b4d0d632a2eed694cd1d6))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250509-2.0.0 ([#3103](https://github.com/googleapis/java-storage/issues/3103)) ([1fd1090](https://github.com/googleapis/java-storage/commit/1fd109094814bfb6270e10a3e4fd5ec4d20e7fba))
  * Update sdk-platform-java dependencies ([#3102](https://github.com/googleapis/java-storage/issues/3102)) ([3b53b94](https://github.com/googleapis/java-storage/commit/3b53b942f31805c5291ca109b4f3e501fbc6fc0d))



## May 19, 2025

Libraries

### Go

#### [1.54.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.53.0...storage/v1.54.0) (2025-05-12)

##### Features

  * **storage:** Add experimental ZB API option ([#12214](https://github.com/googleapis/google-cloud-go/issues/12214)) ([f669982](https://github.com/googleapis/google-cloud-go/commit/f669982de2abf64759eccf5c38bd669488b9cf6a))



##### Bug Fixes

  * **storage:** Fix append writer hang ([#12201](https://github.com/googleapis/google-cloud-go/issues/12201)) ([7ce2a2a](https://github.com/googleapis/google-cloud-go/commit/7ce2a2ad3ae9deff28c73c1bcc2e7001770464eb))
  * **storage:** Retry unwrapped EOFs ([#12202](https://github.com/googleapis/google-cloud-go/issues/12202)) ([b2d42bd](https://github.com/googleapis/google-cloud-go/commit/b2d42bda6a398f3aa00030b6e99bbcb40f132ff7))



## May 12, 2025

Libraries

### Java

#### [2.52.2](https://github.com/googleapis/java-storage/compare/v2.52.1...v2.52.2) (2025-05-06)

##### Bug Fixes

  * Fix a possible NPE that could happen when shutting down a grpc Storage instance ([#3089](https://github.com/googleapis/java-storage/issues/3089)) ([56f5d0a](https://github.com/googleapis/java-storage/commit/56f5d0ae8826d3d03c436fd0b91630cd09c09a3d))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250424-2.0.0 ([#3084](https://github.com/googleapis/java-storage/issues/3084)) ([c7afbde](https://github.com/googleapis/java-storage/commit/c7afbde3b1a78a56c017283850f90938d66e44fd))
  * Update sdk-platform-java dependencies ([#3087](https://github.com/googleapis/java-storage/issues/3087)) ([762ca13](https://github.com/googleapis/java-storage/commit/762ca1374a8e738fbafc49d17fd38375962d026f))



## May 05, 2025

Libraries

### Java

#### [2.52.0](https://github.com/googleapis/java-storage/compare/v2.51.0...v2.52.0) (2025-04-28)

> [!IMPORTANT] This release has a direct memory leak when using a `StorageOptions.grpc()` instance and performing downloads.
> 
> Please update to [2.52.1](https://github.com/googleapis/java-storage/releases/tag/v2.52.1) or later which contains the fix.

##### Features

  * Add Storage.BlobListOption#includeTrailingDelimiter ([#3038](https://github.com/googleapis/java-storage/issues/3038)) ([0b7a0df](https://github.com/googleapis/java-storage/commit/0b7a0dff91af0e22e84ba3ca08862141292b3b30))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([74c46dd](https://github.com/googleapis/java-storage/commit/74c46ddcd91553bcb8145c536389bbe0ca32886c))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250416-2.0.0 ([#3063](https://github.com/googleapis/java-storage/issues/3063)) ([d496d5b](https://github.com/googleapis/java-storage/commit/d496d5bcc1f6ee922bb8f02bfc91d4aeffb8f9a7))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250420-2.0.0 ([#3070](https://github.com/googleapis/java-storage/issues/3070)) ([1ef50f2](https://github.com/googleapis/java-storage/commit/1ef50f2936e62602db689cffbe166c9494ac58f6))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#3061](https://github.com/googleapis/java-storage/issues/3061)) ([cb43a6c](https://github.com/googleapis/java-storage/commit/cb43a6c368367e15dfd7c2205689df04547d1a9c))
  * Update googleapis/sdk-platform-java action to v2.56.2 ([#3055](https://github.com/googleapis/java-storage/issues/3055)) ([7025ad7](https://github.com/googleapis/java-storage/commit/7025ad7db438741ab6d74d5e3f768d0a2bd4da5c))



### Java

#### [2.52.1](https://github.com/googleapis/java-storage/compare/v2.52.0...v2.52.1) (2025-05-01)

##### Bug Fixes

  * Fix grpc ReadObject memory leak introduced in 2.51.0 ([#3080](https://github.com/googleapis/java-storage/issues/3080)) ([7057629](https://github.com/googleapis/java-storage/commit/705762947fad452462ad0e55ec5898e6389a0ac3))



### Go

#### [1.53.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.52.0...storage/v1.53.0) (2025-05-02)

##### Features

  * **storage/control:** Add Anywhere cache control APIs ([83ae06c](https://github.com/googleapis/google-cloud-go/commit/83ae06c3ec7d190e38856ba4cfd8a13f08356b4d))



##### Bug Fixes

  * **storage:** Fix append edge cases ([#12074](https://github.com/googleapis/google-cloud-go/issues/12074)) ([0eee1f9](https://github.com/googleapis/google-cloud-go/commit/0eee1f99a7dc0d1bfc36fa43d78933cae47962ee))
  * **storage:** Fix retries for redirection errors. ([#12093](https://github.com/googleapis/google-cloud-go/issues/12093)) ([3e177e7](https://github.com/googleapis/google-cloud-go/commit/3e177e755f5bf6aa96e8712cc4adcba7eb6f04f6))
  * **storage:** Handle gRPC deadlines in tests. ([#12092](https://github.com/googleapis/google-cloud-go/issues/12092)) ([30b7cd2](https://github.com/googleapis/google-cloud-go/commit/30b7cd27771ccbd49b70ee106da36362ba8f1e87))
  * **storage:** Update offset on resumable upload retry ([#12086](https://github.com/googleapis/google-cloud-go/issues/12086)) ([6ce8fe5](https://github.com/googleapis/google-cloud-go/commit/6ce8fe5aec0ec7916eda4d1405cab5f5f65a5de8))
  * **storage:** Validate Bidi option for MRD ([#12033](https://github.com/googleapis/google-cloud-go/issues/12033)) ([d9018cf](https://github.com/googleapis/google-cloud-go/commit/d9018cf640a9ac25e2b23b75b3bcfa734379ab09))



##### Documentation

  * **storage/control:** Added comments for Anywhere cache messages ([83ae06c](https://github.com/googleapis/google-cloud-go/commit/83ae06c3ec7d190e38856ba4cfd8a13f08356b4d))



## April 28, 2025

Libraries

### Go

#### [1.52.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.51.0...storage/v1.52.0) (2025-04-22)

##### Features

  * **storage/control:** Add Anywhere cache control APIs ([#11807](https://github.com/googleapis/google-cloud-go/issues/11807)) ([12bfa98](https://github.com/googleapis/google-cloud-go/commit/12bfa984f87099dbfbd5abf3436e440e62b04bad))
  * **storage:** Add CurrentState function to determine state of stream in MRD ([#11688](https://github.com/googleapis/google-cloud-go/issues/11688)) ([14e8e13](https://github.com/googleapis/google-cloud-go/commit/14e8e132d9d5808d1ca789792e7e39f0857991da))
  * **storage:** Add OwnerEntity to bucketAttrs ([#11857](https://github.com/googleapis/google-cloud-go/issues/11857)) ([4cd4a0c](https://github.com/googleapis/google-cloud-go/commit/4cd4a0ca1f6132ea6ed9df7b27310a3238a9c3fd))
  * **storage:** Takeover appendable object ([#11977](https://github.com/googleapis/google-cloud-go/issues/11977)) ([513b937](https://github.com/googleapis/google-cloud-go/commit/513b937420b945c4a76e20711f305c6ad8a77812))
  * **storage:** Unfinalized appendable objects. ([#11647](https://github.com/googleapis/google-cloud-go/issues/11647)) ([52c0218](https://github.com/googleapis/google-cloud-go/commit/52c02183fabf43fcba3893f493140ac28a7836d1))



##### Bug Fixes

  * **storage:** Fix Attrs for append takeover ([#11989](https://github.com/googleapis/google-cloud-go/issues/11989)) ([6db35b1](https://github.com/googleapis/google-cloud-go/commit/6db35b10567b7f1463bfef722b0fd72257190ee7))
  * **storage:** Fix panic when Flush called early ([#11934](https://github.com/googleapis/google-cloud-go/issues/11934)) ([7d0b8a7](https://github.com/googleapis/google-cloud-go/commit/7d0b8a75ae55731ae765c01f24920f9f11038f44))
  * **storage:** Fix unfinalized write size ([#12016](https://github.com/googleapis/google-cloud-go/issues/12016)) ([6217f8f](https://github.com/googleapis/google-cloud-go/commit/6217f8fd3cd8680a7e6b7b46fc9b7bda6ee6292e))
  * **storage:** Force first message on next sendBuffer when nothing sent on current ([#11871](https://github.com/googleapis/google-cloud-go/issues/11871)) ([a1a2292](https://github.com/googleapis/google-cloud-go/commit/a1a22927d6a4399e7392787bccb9707bc9e8f149))
  * **storage:** Populate Writer.Attrs after Flush() ([#12021](https://github.com/googleapis/google-cloud-go/issues/12021)) ([8e56f74](https://github.com/googleapis/google-cloud-go/commit/8e56f745e7f2175660838f96c1a12a46841cac40))
  * **storage:** Remove check for FinalizeOnClose ([#11992](https://github.com/googleapis/google-cloud-go/issues/11992)) ([2664b8c](https://github.com/googleapis/google-cloud-go/commit/2664b8cec00a606001184cb17c074fd0e79e66b8))
  * **storage:** Wrap read response parsing errors ([#11951](https://github.com/googleapis/google-cloud-go/issues/11951)) ([d2e6583](https://github.com/googleapis/google-cloud-go/commit/d2e658387b80ec8a3e41e048a9d520b8dd13dd00))



### Java

#### [2.51.0](https://github.com/googleapis/java-storage/compare/v2.50.0...v2.51.0) (2025-04-23)

> [!IMPORTANT] This release has a direct memory leak when using a `StorageOptions.grpc()` instance and performing downloads.
> 
> Please update to [2.52.1](https://github.com/googleapis/java-storage/releases/tag/v2.52.1) or later which contains the fix.

##### Features

  * Add @BetaApi Storage#blobAppendableUpload for gRPC Transport ([#3020](https://github.com/googleapis/java-storage/pull/3020)) ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))
  * Add @BetaApi Storage#blobReadSession for gRPC Transport ([#3020](https://github.com/googleapis/java-storage/pull/3020)) ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))
  * Implement improved retry context information ([#3020](https://github.com/googleapis/java-storage/pull/3020)) ([62b6248](https://github.com/googleapis/java-storage/commit/62b62482c10d79c9f7d1b7c6cedd9e7d422a58ad))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.0 ([8f9f5ec](https://github.com/googleapis/java-storage/commit/8f9f5ec4506bde58fbf2351c99f0d67cdcfcd88e))
  * Ensure object generation is sent for Storage#update(BlobInfo) using HTTP Transport ([#3006](https://github.com/googleapis/java-storage/issues/3006)) ([2a3e0e7](https://github.com/googleapis/java-storage/commit/2a3e0e7453c5e3e45bc06eec1ba6d2bc193143e6)), closes [#2980](https://github.com/googleapis/java-storage/issues/2980)
  * Update 416 handling for ReadChannel ([#3018](https://github.com/googleapis/java-storage/issues/3018)) ([4a9c3e4](https://github.com/googleapis/java-storage/commit/4a9c3e46e8d4fa64813869cadf247cf77f1844d5))
  * Update gRPC Bidi resumable upload to have more robust error message generation ([#2998](https://github.com/googleapis/java-storage/issues/2998)) ([79b5d85](https://github.com/googleapis/java-storage/commit/79b5d8559b2e655178db2ba75116ddba5a581a7b))
  * Update gRPC implementation for storage.buckets.get to translate NOT_FOUND to null ([#3005](https://github.com/googleapis/java-storage/issues/3005)) ([704af65](https://github.com/googleapis/java-storage/commit/704af65b25fe38d146b960775a69644cd80f2e78))



##### Dependencies

  * Remove explicit version declarations for packages that are in shared-dependencies ([#3014](https://github.com/googleapis/java-storage/issues/3014)) ([61cdb30](https://github.com/googleapis/java-storage/commit/61cdb30f250d2fdaaf79e0d060eb573197c7a90e))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250312-2.0.0 ([#3000](https://github.com/googleapis/java-storage/issues/3000)) ([78fc076](https://github.com/googleapis/java-storage/commit/78fc0763c89fb0e603d75b20c9c67eabc2b9f729))
  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.34.0 ([#2938](https://github.com/googleapis/java-storage/issues/2938)) ([ff6f696](https://github.com/googleapis/java-storage/commit/ff6f696e8c4a539b5e6755fbd550096ee4688ecc))
  * Update sdk-platform-java dependencies ([#3046](https://github.com/googleapis/java-storage/issues/3046)) ([861f958](https://github.com/googleapis/java-storage/commit/861f9586e041f65061fb3da7f88955c4214d450c))
  * Update sdk-platform-java dependencies ([#3053](https://github.com/googleapis/java-storage/issues/3053)) ([921d1ba](https://github.com/googleapis/java-storage/commit/921d1ba0a547242c70cbb7dfb2cb190fa761398f))



## April 17, 2025

Change

[Best practices for using Cloud Storage with media workloads](https://docs.cloud.google.com/storage/docs/best-practices-media-workload) are now available.

## March 31, 2025

Feature

You can now use metrics to monitor Cloud Storage FUSE performance. For more information, see [Cloud Storage FUSE metrics](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics).

Feature

Storage batch operations for Cloud Storage is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Using storage batch operations, you can perform operations on billions of Cloud Storage objects in a serverless manner. To learn more about storage batch operations, see [Overview of storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

Change

Additional functionality is now available for the [bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) feature:

  * You can use IP filtering for buckets in all [regions](https://docs.cloud.google.com/storage/docs/locations#location-r), [dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr), and [multi-regions](https://docs.cloud.google.com/storage/docs/locations#location-mr).

  * You can use [custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints) to enforce IP filtering.




## March 21, 2025

Feature

[Cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use cross-bucket replication to copy new and updated objects asynchronously from a source bucket to a destination bucket.

Feature

Storage Intelligence for Cloud Storage is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Storage Intelligence simplifies data management in Cloud Storage at scale by providing a unified platform for data exploration, cost optimization, security enforcement, and governance implementation. To learn more about Storage Intelligence, see [Overview of Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).

Feature

Storage Insights datasets is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Storage Insights datasets helps you get insights for your Cloud Storage resources and export the data to BigQuery. Storage Insights datasets is an exclusive feature only available through the [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) subscription. To learn more about Storage Insights, see [Overview of Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

## March 17, 2025

Libraries

### Go

#### [1.51.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.50.0...storage/v1.51.0) (2025-03-12)

##### Features

  * **storage/append:** Support appends in w1r3. ([#11483](https://github.com/googleapis/google-cloud-go/issues/11483)) ([48bb391](https://github.com/googleapis/google-cloud-go/commit/48bb39154479a2cf2d379316e0915f39d7b7a518))
  * **storage:** Benchmark with experimental MRD. ([#11501](https://github.com/googleapis/google-cloud-go/issues/11501)) ([7b49152](https://github.com/googleapis/google-cloud-go/commit/7b491520a693d258d3370a19c43c9dff6c8558c7))
  * **storage:** Implement RetryChunkDeadline for grpc writes ([#11476](https://github.com/googleapis/google-cloud-go/issues/11476)) ([03575d7](https://github.com/googleapis/google-cloud-go/commit/03575d74f5241cc714e4d3ac63635569a34f5633))
  * **storage:** Specify benchmark integrity check. ([#11465](https://github.com/googleapis/google-cloud-go/issues/11465)) ([da18845](https://github.com/googleapis/google-cloud-go/commit/da188453e0254c49a01d28788d0849a2d0e98e0c))
  * **storage:** Use ReadHandle for faster re-connect ([#11510](https://github.com/googleapis/google-cloud-go/issues/11510)) ([cac52f7](https://github.com/googleapis/google-cloud-go/commit/cac52f79a73d46774d33d76e3075c0a5b3e0b9f3))
  * **storage:** Wrap NotFound errors for buckets and objects ([#11519](https://github.com/googleapis/google-cloud-go/issues/11519)) ([0dd7d3d](https://github.com/googleapis/google-cloud-go/commit/0dd7d3d62e54c6c3bca395fcca8450ad3347a5a0))



##### Bug Fixes

  * **storage/append:** Report progress for appends. ([#11503](https://github.com/googleapis/google-cloud-go/issues/11503)) ([96dbb6c](https://github.com/googleapis/google-cloud-go/commit/96dbb6c12398fb3cbffab2bf61836bef2f704f66))
  * **storage:** Add a safety check for readhandle ([#11549](https://github.com/googleapis/google-cloud-go/issues/11549)) ([c9edb37](https://github.com/googleapis/google-cloud-go/commit/c9edb379ece70f065650702c9240ee540ca2f610))
  * **storage:** Add universe domain to defaultSignBytesFunc ([#11521](https://github.com/googleapis/google-cloud-go/issues/11521)) ([511608b](https://github.com/googleapis/google-cloud-go/commit/511608b8e8554aa06f9fe2e2e4f51ead0f484031))
  * **storage:** Clone the defaultRetry to avoid modifying it directly ([#11533](https://github.com/googleapis/google-cloud-go/issues/11533)) ([7f8d69d](https://github.com/googleapis/google-cloud-go/commit/7f8d69dcd6a7b1ad6c1df8d9fe8dfb5fe0947479))
  * **storage:** Fix adding multiple range on stream with same read id ([#11584](https://github.com/googleapis/google-cloud-go/issues/11584)) ([0bb3434](https://github.com/googleapis/google-cloud-go/commit/0bb3434e0e12563ff21ef72ad2e52ad7eb61d66e))
  * **storage:** Modify the callback of mrd to return length of data read instead of limit. ([#11687](https://github.com/googleapis/google-cloud-go/issues/11687)) ([9e359f0](https://github.com/googleapis/google-cloud-go/commit/9e359f0089f744c32d12bf77889d69a4db155357))
  * **storage:** Propagate ctx from invoke to grpc upload reqs ([#11475](https://github.com/googleapis/google-cloud-go/issues/11475)) ([9ad9d76](https://github.com/googleapis/google-cloud-go/commit/9ad9d7665ca2f4cfdcee75f5e683084ac49536a6))
  * **storage:** Remove duplicate routing header ([#11534](https://github.com/googleapis/google-cloud-go/issues/11534)) ([8eeb59c](https://github.com/googleapis/google-cloud-go/commit/8eeb59cbfb16d8f379f7aa4c6f11e53cebbd38a6))
  * **storage:** Return sentinel ErrObjectNotExist for copy and compose ([#11369](https://github.com/googleapis/google-cloud-go/issues/11369)) ([74d0c10](https://github.com/googleapis/google-cloud-go/commit/74d0c1096f897ca3c15646f3049ea540bed0a6a0)), refs [#10760](https://github.com/googleapis/google-cloud-go/issues/10760)
  * **storage:** Wait for XML read req to finish to avoid data races ([#11527](https://github.com/googleapis/google-cloud-go/issues/11527)) ([782e12a](https://github.com/googleapis/google-cloud-go/commit/782e12a11c1dfe6d831f5d0b9b5f4409993e4d9e))



### Java

#### [2.50.0](https://github.com/googleapis/java-storage/compare/v2.49.0...v2.50.0) (2025-03-14)

##### Features

  * Next release from main branch is 2.50.0 ([#2968](https://github.com/googleapis/java-storage/issues/2968)) ([4a69fcc](https://github.com/googleapis/java-storage/commit/4a69fcc16787904675e5ba15f42bcab67553a7aa))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([22e7e3d](https://github.com/googleapis/java-storage/commit/22e7e3d4e8c56184f9c91b1e0bf52d5c4aa4cf9f))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([81c8c61](https://github.com/googleapis/java-storage/commit/81c8c611ab51a706d63670dff86db5bfd04ef544))
  * Improve 503 handling for json resumable uploads ([#2987](https://github.com/googleapis/java-storage/issues/2987)) ([9bc2b14](https://github.com/googleapis/java-storage/commit/9bc2b14a0058cded0321e5afa3ea3fc59bf3421b))
  * Update usages of String.format to explicitly pass Locale.US ([#2974](https://github.com/googleapis/java-storage/issues/2974)) ([8bcb2de](https://github.com/googleapis/java-storage/commit/8bcb2de22ea39cfc0b4dda07daba78ea192b5e98)), closes [#2972](https://github.com/googleapis/java-storage/issues/2972)



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20250224-2.0.0 ([#2969](https://github.com/googleapis/java-storage/issues/2969)) ([80a40c4](https://github.com/googleapis/java-storage/commit/80a40c41527a5fb83a41ac4754d5be22f5cd5c2b))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#2985](https://github.com/googleapis/java-storage/issues/2985)) ([e22a2de](https://github.com/googleapis/java-storage/commit/e22a2de0fe1dc66e6e5b6d311f4812c290177203))
  * Update sdk-platform-java dependencies ([#2983](https://github.com/googleapis/java-storage/issues/2983)) ([9eeb82a](https://github.com/googleapis/java-storage/commit/9eeb82af81ad8095c21542808a8eaa5098dee074))
  * Update sdk-platform-java dependencies ([#2986](https://github.com/googleapis/java-storage/issues/2986)) ([10b922a](https://github.com/googleapis/java-storage/commit/10b922a8ae831fcd0107abf54091566442ae5fde))



Feature

Cloud Storage now offers the `DE` configurable dual-region code, which can be used when creating a dual-region bucket in `europe-west3` (Frankfurt) and `europe-west10` (Berlin). To learn more about Cloud Storage configurable dual-regions, see [Configurable dual-regions](https://docs.cloud.google.com/storage/docs/locations#configurable)

## March 13, 2025

Feature

Anywhere Cache for Cloud Storage is now [generally available (GA)](https://developers.google.com/maps/launch-stages#ga). Anywhere Cache enables you to create SSD-backed caches in the same zones as your workloads, helping you get access to your data faster and avoid multi-region data transfer fees. To learn more about Anywhere Cache, see [Overview of Anywhere Cache](https://docs.cloud.google.com/storage/docs/anywhere-cache).

## March 05, 2025

Feature

Configurable dual-regions now include the Turin, Italy (`europe-west12`) region. For more information, see [Cloud Storage configurable dual-regions](https://docs.cloud.google.com/storage/docs/locations#configurable).

## March 04, 2025

Feature

Cloud Storage now offers support in the Stockholm, Sweden (`europe-north2`) region. To learn more about supported locations, see [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations).

## March 03, 2025

Libraries

### Java

#### [2.49.0](https://github.com/googleapis/java-storage/compare/v2.48.2...v2.49.0) (2025-02-26)

##### Features

  * Add new Options to allow per method header values ([#2941](https://github.com/googleapis/java-storage/issues/2941)) ([297802d](https://github.com/googleapis/java-storage/commit/297802d1715e3289dd720fba851c563004b8c5f2))
  * **transfer-manager:** Add ParallelUploadConfig.Builder#setUploadBlobInfoFactory ([#2936](https://github.com/googleapis/java-storage/issues/2936)) ([86e9ae8](https://github.com/googleapis/java-storage/commit/86e9ae80772aa202d0b6563b8dd37722d8b5e0e0)), closes [#2638](https://github.com/googleapis/java-storage/issues/2638)



##### Bug Fixes

  * Categorize a WatchdogTimeoutException as retriable for grpc ReadObject ([#2954](https://github.com/googleapis/java-storage/issues/2954)) ([b53bd53](https://github.com/googleapis/java-storage/commit/b53bd53c26984b3e850355ced608b511688b74d1))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.53.0 ([9946d6b](https://github.com/googleapis/java-storage/commit/9946d6bdc7ec8398bf1bd1df63f272df1351539e))
  * Update grpc based Storage to defer project id validation ([#2930](https://github.com/googleapis/java-storage/issues/2930)) ([cc03784](https://github.com/googleapis/java-storage/commit/cc037848be7d21cb827c97d7f71618f1bfae941d))
  * Update kms key handling when opening a resumable upload to clear the value in the json to be null rather than empty string ([#2939](https://github.com/googleapis/java-storage/issues/2939)) ([43553de](https://github.com/googleapis/java-storage/commit/43553dedce33093e751143fadb372024d975706c))



##### Dependencies

  * Update sdk-platform-java dependencies ([#2957](https://github.com/googleapis/java-storage/issues/2957)) ([40cfda6](https://github.com/googleapis/java-storage/commit/40cfda62d4bff72a857d0269eaa7c0225f216650))



##### Documentation

  * Add note about HNS support to moveBlob ([#2929](https://github.com/googleapis/java-storage/issues/2929)) ([c461546](https://github.com/googleapis/java-storage/commit/c461546bfd016b21eb99f8e25604ee3fd001c9c6))



### Python

#### [3.1.0](https://github.com/googleapis/python-storage/compare/v3.0.0...v3.1.0) (2025-02-27)

##### Features

  * Add api_key argument to Client constructor ([#1441](https://github.com/googleapis/python-storage/issues/1441)) ([c869e15](https://github.com/googleapis/python-storage/commit/c869e15ec535a0aa50029d30b6a3ce64ff119b5f))
  * Add Bucket.move_blob() for HNS-enabled buckets ([#1431](https://github.com/googleapis/python-storage/issues/1431)) ([24c000f](https://github.com/googleapis/python-storage/commit/24c000fb7b9f576e6d6c6ec5733f3971fe133655))



## February 26, 2025

Feature

[Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) for Cloud Storage is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use bucket relocation to relocate buckets between geographic locations.

## February 24, 2025

Feature

The [`Objects: move`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move) method supports moving objects in both flat and hierarchical namespace buckets.

## February 17, 2025

Libraries

### Java

#### [2.48.2](https://github.com/googleapis/java-storage/compare/v2.48.1...v2.48.2) (2025-02-11)

##### Dependencies

  * Update sdk-platform-java dependencies ([#2921](https://github.com/googleapis/java-storage/issues/2921)) ([fa9b0a8](https://github.com/googleapis/java-storage/commit/fa9b0a8d6e2b185c0588d824329b409718bef302))



##### Documentation

  * Update storage_copy_file to include MegabytesCopiedPerChunk ([#2910](https://github.com/googleapis/java-storage/issues/2910)) ([971ca5d](https://github.com/googleapis/java-storage/commit/971ca5d107967960e6db6ca76a55e44b9aefc605))



## February 10, 2025

Libraries

### Java

#### [2.48.1](https://github.com/googleapis/java-storage/compare/v2.48.0...v2.48.1) (2025-02-03)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([00754bc](https://github.com/googleapis/java-storage/commit/00754bc0b30da4ebc13e75f55525d9bd885b0572))
  * Update batch handling to ensure each operation has its own unique idempotency-token ([#2905](https://github.com/googleapis/java-storage/issues/2905)) ([8d79b8d](https://github.com/googleapis/java-storage/commit/8d79b8d9cea30c6bba0d2550fa397b8c8b7acc3c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#2895](https://github.com/googleapis/java-storage/issues/2895)) ([145afb0](https://github.com/googleapis/java-storage/commit/145afb0d3a783fe73a388a7be174b598a195a2c6))
  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2904](https://github.com/googleapis/java-storage/issues/2904)) ([2a5242e](https://github.com/googleapis/java-storage/commit/2a5242e580185a5952181f922c4eca25790bcec6))



##### Documentation

  * Create OpenTelemetry Quickstart Sample ([#2861](https://github.com/googleapis/java-storage/issues/2861)) ([31df9b7](https://github.com/googleapis/java-storage/commit/31df9b7a6350714ff354934ccbd27c5dd68762f5))



## February 05, 2025

Announcement

[Announced billing changes](https://cloud.google.com/resources/storage/billing-fix-bigquery) for accessing Cloud Storage through BigQuery take effect Feb 21, 2025. These changes were originally set to take effect on February 01, 2025.

## February 03, 2025

Libraries

### Java

#### [2.48.0](https://github.com/googleapis/java-storage/compare/v2.47.0...v2.48.0) (2025-01-27)

##### Features

  * Add new Storage#moveBlob method to atomically rename an object ([#2882](https://github.com/googleapis/java-storage/issues/2882)) ([c49fd08](https://github.com/googleapis/java-storage/commit/c49fd08582c7235919270c1dd4eb2ece6933d302))
  * Next release from main branch is 2.48.0 ([#2885](https://github.com/googleapis/java-storage/issues/2885)) ([34e5903](https://github.com/googleapis/java-storage/commit/34e5903df9b7221ba9ebabc07046d7b819f9f209))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([09ed029](https://github.com/googleapis/java-storage/commit/09ed02995f4688db69c0e0db1c3d72cadce0c395))
  * Update Signed URL default scheme to resolve from storage options host ([#2880](https://github.com/googleapis/java-storage/issues/2880)) ([7ae7e39](https://github.com/googleapis/java-storage/commit/7ae7e3998930c1bec72ff7c06ebc2b66343852ca)), closes [#2870](https://github.com/googleapis/java-storage/issues/2870)
  * Update StorageException translation of an ApiException to include error details ([#2872](https://github.com/googleapis/java-storage/issues/2872)) ([8ad5010](https://github.com/googleapis/java-storage/commit/8ad501012fab0dfd8d0f0dce49d7c681540022a9))



##### Dependencies

  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2873](https://github.com/googleapis/java-storage/issues/2873)) ([39509d5](https://github.com/googleapis/java-storage/commit/39509d53ee283694526efbec58daa24c3d8ca080))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.52.0 ([#2883](https://github.com/googleapis/java-storage/issues/2883)) ([a64a3d5](https://github.com/googleapis/java-storage/commit/a64a3d58410dd2e9db20a36cd7169037f71eaeeb))



### Python

#### [3.0.0](https://github.com/googleapis/python-storage/compare/v2.19.0...v3.0.0) (2025-01-28)

##### ⚠ BREAKING CHANGES

Please consult the README for details on this major version release.

  * The default checksum strategy for uploads has changed from None to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383))
  * The default checksum strategy for downloads has changed from "md5" to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383))
  * Deprecated positional argument "num_retries" has been removed ([#1377](https://github.com/googleapis/python-storage/issues/1377))
  * Deprecated argument "text_mode" has been removed ([#1379](https://github.com/googleapis/python-storage/issues/1379))
  * Blob.download_to_filename() now deletes the empty destination file on a 404 ([#1394](https://github.com/googleapis/python-storage/pull/1394))
  * Media operations now use the same retry backoff, timeout and custom predicate system as non-media operations, which may slightly impact default retry behavior ([#1385](https://github.com/googleapis/python-storage/issues/1385))
  * Retries are now enabled by default for uploads, blob deletes and blob metadata updates ([#1400](https://github.com/googleapis/python-storage/issues/1400))



##### Features

  * Add "auto" checksum option and make default ([#1383](https://github.com/googleapis/python-storage/issues/1383)) ([5375fa0](https://github.com/googleapis/python-storage/commit/5375fa07385c60cac694025aee123e20cb25bb65))
  * Blob.download_to_filename() deletes the empty destination file on a 404 ([#1394](https://github.com/googleapis/python-storage/pull/1394)) ([066be2d](https://github.com/googleapis/python-storage/commit/066be2db789cfd28d47d143ca0f7ccc9da183682))
  * Enable custom predicates for media operations ([#1385](https://github.com/googleapis/python-storage/issues/1385)) ([f3517bf](https://github.com/googleapis/python-storage/commit/f3517bfcb9e4ab8e4d761eb64a753e64b3d5871d))
  * Integrate google-resumable-media ([#1283](https://github.com/googleapis/python-storage/issues/1283)) ([bd917b4](https://github.com/googleapis/python-storage/commit/bd917b49d2a20e2e1edee2d32dc65b66da8d6aba))
  * Retry by default for uploads, blob deletes, metadata updates ([#1400](https://github.com/googleapis/python-storage/issues/1400)) ([0426005](https://github.com/googleapis/python-storage/commit/0426005175079ebdd73c299642a83b8193086d60))



##### Bug Fixes

  * Cancel upload when BlobWriter exits with exception ([#1243](https://github.com/googleapis/python-storage/issues/1243)) ([df107d2](https://github.com/googleapis/python-storage/commit/df107d20a772e9b955d9978cd4a7731869e92cbe))
  * Changed name of methods `Blob.from_string()` and `Bucket.from_string()` to `from_uri()` ([#1335](https://github.com/googleapis/python-storage/issues/1335)) ([58c1d03](https://github.com/googleapis/python-storage/commit/58c1d038198046665317a0d00eb9630608349476))
  * Correctly calculate starting offset for retries of ranged reads ([#1376](https://github.com/googleapis/python-storage/issues/1376)) ([7b6c9a0](https://github.com/googleapis/python-storage/commit/7b6c9a0fb3a79d713f951176a690f6e72c4d77c5))
  * Filter download_kwargs in BlobReader ([#1411](https://github.com/googleapis/python-storage/issues/1411)) ([0c21210](https://github.com/googleapis/python-storage/commit/0c21210450319f6da920982116ee52075105c45a))
  * Remove deprecated num_retries argument ([#1377](https://github.com/googleapis/python-storage/issues/1377)) ([58b5040](https://github.com/googleapis/python-storage/commit/58b5040933d4b21e0be94357ed5aa14c87969f73))
  * Remove deprecated text_mode argument ([#1379](https://github.com/googleapis/python-storage/issues/1379)) ([4d20a8e](https://github.com/googleapis/python-storage/commit/4d20a8efa8cf37bb7f099b20a8c352c9a0c42659))



##### Documentation

  * Correct formatting and update README.rst ([#1427](https://github.com/googleapis/python-storage/issues/1427)) ([2945853](https://github.com/googleapis/python-storage/commit/29458539773e834b202fef0c77dc439c393b37e8))
  * Fix issue with exceptions.py documentation ([#1328](https://github.com/googleapis/python-storage/issues/1328)) ([22b8c30](https://github.com/googleapis/python-storage/commit/22b8c304afc7199fbc2dec448a4a3c5eba7d4e3a))



## January 31, 2025

Feature

You can now enable client-side traces with OpenTelemetry when you use Cloud Storage client libraries. To learn more about how client-side traces work and how to configure tracing for your application, see [Use client-side traces](https://docs.cloud.google.com/storage/docs/traces).

## January 13, 2025

Libraries

### Java

#### [2.47.0](https://github.com/googleapis/java-storage/compare/v2.46.0...v2.47.0) (2025-01-08)

##### Features

  * Add MoveObject RPC ([34b8ac4](https://github.com/googleapis/java-storage/commit/34b8ac4239bab67b53c73050d2341615254a3ae0))
  * Introductory beta level support for OpenTelemetry tracing on c.g.c.storage.Storage methods ([#2837](https://github.com/googleapis/java-storage/issues/2837)) ([dd889ea](https://github.com/googleapis/java-storage/commit/dd889ea0d0a57490ef106ab92ba557f26d414406))



##### Bug Fixes

  * De-beta storage-v2 artifacts ([#2852](https://github.com/googleapis/java-storage/issues/2852)) ([77a2e8a](https://github.com/googleapis/java-storage/commit/77a2e8af341528a4ff3c34a880a7983f828b8cfd))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.0 ([34b8ac4](https://github.com/googleapis/java-storage/commit/34b8ac4239bab67b53c73050d2341615254a3ae0))
  * Fix interrupt spiral in grpc ReadObject drainQueue ([#2850](https://github.com/googleapis/java-storage/issues/2850)) ([c1dac83](https://github.com/googleapis/java-storage/commit/c1dac837387ffc40f00344c8fb0e86e09d009358))
  * Update request handling of gRPC based CopyWriter ([#2858](https://github.com/googleapis/java-storage/issues/2858)) ([093cb87](https://github.com/googleapis/java-storage/commit/093cb8759d5cfaafa6fd9df43de1bb91c1285f35))



##### Dependencies

  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.51.0 ([#2860](https://github.com/googleapis/java-storage/issues/2860)) ([980ac4e](https://github.com/googleapis/java-storage/commit/980ac4ebe09636d0de255e89f747bde8cc9ce041))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#2864](https://github.com/googleapis/java-storage/issues/2864)) ([b731c06](https://github.com/googleapis/java-storage/commit/b731c06b11186e9695fb89f32abf35988d558bc9))
  * Update sdk-platform-java dependencies ([#2866](https://github.com/googleapis/java-storage/issues/2866)) ([562df7f](https://github.com/googleapis/java-storage/commit/562df7f087b34db0f3d49c6e0b87643a606ef9c6))



### Go

#### [1.50.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.49.0...storage/v1.50.0) (2025-01-09)

##### Features

  * **storage/internal:** Add new appendable Object to BidiWrite API ([2e4feb9](https://github.com/googleapis/google-cloud-go/commit/2e4feb938ce9ab023c8aa6bd1dbdf36fe589213a))
  * **storage/internal:** Add new preview BidiReadObject API ([2e4feb9](https://github.com/googleapis/google-cloud-go/commit/2e4feb938ce9ab023c8aa6bd1dbdf36fe589213a))
  * **storage:** Add support for gRPC bi-directional multi-range reads. This API is in private preview and not generally and is not yet available for general use. ([#11377](https://github.com/googleapis/google-cloud-go/issues/11377)) ([b4d86a5](https://github.com/googleapis/google-cloud-go/commit/b4d86a52bd319a602115cdb710a743c71494a88b))
  * **storage:** Add support for ReadHandle, a gRPC feature that allows for accelerated resumption of streams when one is interrupted. ReadHandle requires the bi-directional read API, which is in private preview and is not yet available for general use. ([#11377](https://github.com/googleapis/google-cloud-go/issues/11377)) ([b4d86a5](https://github.com/googleapis/google-cloud-go/commit/b4d86a52bd319a602115cdb710a743c71494a88b))
  * **storage:** Support appendable semantics for writes in gRPC. This API is in preview. ([#11377](https://github.com/googleapis/google-cloud-go/issues/11377)) ([b4d86a5](https://github.com/googleapis/google-cloud-go/commit/b4d86a52bd319a602115cdb710a743c71494a88b))
  * **storage:** Refactor gRPC writer flow ([#11377](https://github.com/googleapis/google-cloud-go/issues/11377)) ([b4d86a5](https://github.com/googleapis/google-cloud-go/commit/b4d86a52bd319a602115cdb710a743c71494a88b))



##### Bug Fixes

  * **storage:** Add mutex around uses of mrd variables ([#11405](https://github.com/googleapis/google-cloud-go/issues/11405)) ([54bfc32](https://github.com/googleapis/google-cloud-go/commit/54bfc32db7a0ff40a493de4d466f21ad624de04e))
  * **storage:** Return the appropriate error for method not supported ([#11416](https://github.com/googleapis/google-cloud-go/issues/11416)) ([56d704e](https://github.com/googleapis/google-cloud-go/commit/56d704e3037840aeb87b22cc83f2b6088c79bcee))



##### Documentation

  * **storage/internal:** Add IAM information to RPC comments for reference documentation ([2e4feb9](https://github.com/googleapis/google-cloud-go/commit/2e4feb938ce9ab023c8aa6bd1dbdf36fe589213a))
  * **storage:** Add preview comment to NewMultiRangeDownloader ([#11420](https://github.com/googleapis/google-cloud-go/issues/11420)) ([4ec1d66](https://github.com/googleapis/google-cloud-go/commit/4ec1d66ee180e800606568e8693a282645ec7369))



## December 23, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.49.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.48.0...storage/v1.49.0) (2024-12-21)

##### Features

  * **storage/internal:** Add finalize_time field in Object metadata ([46fc993](https://github.com/googleapis/google-cloud-go/commit/46fc993a3195203a230e2831bee456baaa9f7b1c))
  * **storage/internal:** Add MoveObject RPC ([46fc993](https://github.com/googleapis/google-cloud-go/commit/46fc993a3195203a230e2831bee456baaa9f7b1c))
  * **storage:** Add ObjectHandle.Move method ([#11302](https://github.com/googleapis/google-cloud-go/issues/11302)) ([a3cb8c4](https://github.com/googleapis/google-cloud-go/commit/a3cb8c4fc48883b54d4e830ae5f5ef4f1a3b8ca3))
  * **storage:** Return file metadata on read ([#11212](https://github.com/googleapis/google-cloud-go/issues/11212)) ([d49263b](https://github.com/googleapis/google-cloud-go/commit/d49263b2ab614cad801e26b4a169eafe08d4a2a0))



##### Bug Fixes

  * **storage/dataflux:** Address deadlock when reading from ranges ([#11303](https://github.com/googleapis/google-cloud-go/issues/11303)) ([32cbf56](https://github.com/googleapis/google-cloud-go/commit/32cbf561590541eb0387787bf729be6ddf68e4ee))
  * **storage:** Disable allow non-default credentials flag ([#11337](https://github.com/googleapis/google-cloud-go/issues/11337)) ([145ddf4](https://github.com/googleapis/google-cloud-go/commit/145ddf4f6123d9561856d2b6adeefdfae462b3f7))
  * **storage:** Monitored resource detection ([#11197](https://github.com/googleapis/google-cloud-go/issues/11197)) ([911bcd8](https://github.com/googleapis/google-cloud-go/commit/911bcd8b1816256482bd52e85da7eaf00c315293))
  * **storage:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))



## December 16, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.46.0](https://github.com/googleapis/java-storage/compare/v2.45.0...v2.46.0) (2024-12-13)

##### Features

  * Introduce `java.time` methods and variables ([#2826](https://github.com/googleapis/java-storage/issues/2826)) ([baf30ee](https://github.com/googleapis/java-storage/commit/baf30ee91febbcda7d0f64b0083b789c4384a3c0))



##### Bug Fixes

  * Update retry lifecycle when attempting to decompress a gzip object ([#2840](https://github.com/googleapis/java-storage/issues/2840)) ([7dba13c](https://github.com/googleapis/java-storage/commit/7dba13cbbfd38d3c2147b25264934f33c5dc78e3))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20241113-2.0.0 ([#2823](https://github.com/googleapis/java-storage/issues/2823)) ([503e518](https://github.com/googleapis/java-storage/commit/503e518550b67870c3e856957fdadbc012eff1ed))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20241206-2.0.0 ([#2839](https://github.com/googleapis/java-storage/issues/2839)) ([8f3cdd3](https://github.com/googleapis/java-storage/commit/8f3cdd39dbbbbd63c560c3cb44d1032c0bd41749))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.50.0 ([#2825](https://github.com/googleapis/java-storage/issues/2825)) ([9aa68a6](https://github.com/googleapis/java-storage/commit/9aa68a67d931b19175e23f883a109f22b99411ca))
  * Update sdk-platform-java dependencies ([#2841](https://github.com/googleapis/java-storage/issues/2841)) ([2a70481](https://github.com/googleapis/java-storage/commit/2a704815ee60b8ec7ff2c1af557fee4366ea2e19))



##### Documentation

  * Add samples for soft delete (objects) ([#2754](https://github.com/googleapis/java-storage/issues/2754)) ([41bc807](https://github.com/googleapis/java-storage/commit/41bc807e94f1c0eebd41b4a7baa12301858cc16f))



### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.0.0rc1](https://github.com/googleapis/python-storage/compare/v2.19.0...v3.0.0rc1) (2024-12-12)

##### ⚠ BREAKING CHANGES

  * The default checksum strategy for uploads has changed from None to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383)) (5375fa0)
  * The default checksum strategy for downloads has changed from "md5" to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383)) (5375fa0)
  * Deprecated positional argument "num_retries" has been removed ([#1377](https://github.com/googleapis/python-storage/issues/1377)) (58b5040)
  * Deprecated argument "text_mode" has been removed ([#1379](https://github.com/googleapis/python-storage/issues/1379)) (4d20a8e)
  * Media operation retries now work identically to other retries, which may impact default retry settings ([#1385](https://github.com/googleapis/python-storage/issues/1385)) (f3517bf)
  * Blob.download_to_filename() deletes the empty destination file on a 404



##### Features

  * Add "auto" checksum option and make default ([#1383](https://github.com/googleapis/python-storage/issues/1383)) ([5375fa0](https://github.com/googleapis/python-storage/commit/5375fa07385c60cac694025aee123e20cb25bb65))
  * Blob.download_to_filename() deletes the empty destination file on a 404 ([066be2d](https://github.com/googleapis/python-storage/commit/066be2db789cfd28d47d143ca0f7ccc9da183682))
  * Deprecated argument "text_mode" has been removed ([#1379](https://github.com/googleapis/python-storage/issues/1379)) (4d20a8e) ([4e9a382](https://github.com/googleapis/python-storage/commit/4e9a382dd91f7d951cb9b95319b05e0cdda06415))
  * Deprecated positional argument "num_retries" has been removed ([#1377](https://github.com/googleapis/python-storage/issues/1377)) (58b5040) ([4e9a382](https://github.com/googleapis/python-storage/commit/4e9a382dd91f7d951cb9b95319b05e0cdda06415))
  * Enable custom predicates for media operations ([#1385](https://github.com/googleapis/python-storage/issues/1385)) ([f3517bf](https://github.com/googleapis/python-storage/commit/f3517bfcb9e4ab8e4d761eb64a753e64b3d5871d))
  * Integrate google-resumable-media ([#1283](https://github.com/googleapis/python-storage/issues/1283)) ([bd917b4](https://github.com/googleapis/python-storage/commit/bd917b49d2a20e2e1edee2d32dc65b66da8d6aba))
  * Media operation retries now work identically to other retries, which may impact default retry settings ([#1385](https://github.com/googleapis/python-storage/issues/1385)) (f3517bf) ([4e9a382](https://github.com/googleapis/python-storage/commit/4e9a382dd91f7d951cb9b95319b05e0cdda06415))
  * The default checksum strategy for downloads has changed from "md5" to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383)) (5375fa0) ([4e9a382](https://github.com/googleapis/python-storage/commit/4e9a382dd91f7d951cb9b95319b05e0cdda06415))
  * The default checksum strategy for uploads has changed from None to "auto" ([#1383](https://github.com/googleapis/python-storage/issues/1383)) (5375fa0) ([4e9a382](https://github.com/googleapis/python-storage/commit/4e9a382dd91f7d951cb9b95319b05e0cdda06415))



##### Bug Fixes

  * Cancel upload when BlobWriter exits with exception ([#1243](https://github.com/googleapis/python-storage/issues/1243)) ([df107d2](https://github.com/googleapis/python-storage/commit/df107d20a772e9b955d9978cd4a7731869e92cbe))
  * Changed name of methods `Blob.from_string()` and `Bucket.from_string()` to `from_uri()` ([#1335](https://github.com/googleapis/python-storage/issues/1335)) ([58c1d03](https://github.com/googleapis/python-storage/commit/58c1d038198046665317a0d00eb9630608349476))
  * Correctly calculate starting offset for retries of ranged reads ([#1376](https://github.com/googleapis/python-storage/issues/1376)) ([7b6c9a0](https://github.com/googleapis/python-storage/commit/7b6c9a0fb3a79d713f951176a690f6e72c4d77c5))
  * Remove deprecated num_retries argument ([#1377](https://github.com/googleapis/python-storage/issues/1377)) ([58b5040](https://github.com/googleapis/python-storage/commit/58b5040933d4b21e0be94357ed5aa14c87969f73))
  * Remove deprecated text_mode argument ([#1379](https://github.com/googleapis/python-storage/issues/1379)) ([4d20a8e](https://github.com/googleapis/python-storage/commit/4d20a8efa8cf37bb7f099b20a8c352c9a0c42659))



##### Documentation

  * Fix issue with exceptions.py documentation ([#1328](https://github.com/googleapis/python-storage/issues/1328)) ([22b8c30](https://github.com/googleapis/python-storage/commit/22b8c304afc7199fbc2dec448a4a3c5eba7d4e3a))



## December 09, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.48.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.47.0...storage/v1.48.0) (2024-12-05)

##### Features

  * **storage/dataflux:** Run worksteal listing parallel to sequential listing ([#10966](https://github.com/googleapis/google-cloud-go/issues/10966)) ([3005f5a](https://github.com/googleapis/google-cloud-go/commit/3005f5a86c18254e569b8b1782bf014aa62f33cc))
  * **storage:** Add Writer.ChunkTransferTimeout ([#11111](https://github.com/googleapis/google-cloud-go/issues/11111)) ([fd1db20](https://github.com/googleapis/google-cloud-go/commit/fd1db203d0de898891b9920aacb141ea39228609))
  * **storage:** Allow non default service account ([#11137](https://github.com/googleapis/google-cloud-go/issues/11137)) ([19f01c3](https://github.com/googleapis/google-cloud-go/commit/19f01c3c48ed1272c8fc0af9e5f69646cb662808))



##### Bug Fixes

  * **storage:** Add backoff to gRPC write retries ([#11200](https://github.com/googleapis/google-cloud-go/issues/11200)) ([a7db927](https://github.com/googleapis/google-cloud-go/commit/a7db927da9cf4c6cf242a5db83e44a16d75a8291))
  * **storage:** Correct direct connectivity check ([#11152](https://github.com/googleapis/google-cloud-go/issues/11152)) ([a75c8b0](https://github.com/googleapis/google-cloud-go/commit/a75c8b0f72c38d9a85c908715c3e37eb5cffb131))
  * **storage:** Disable soft delete policy using 0 retentionDurationSeconds ([#11226](https://github.com/googleapis/google-cloud-go/issues/11226)) ([f087721](https://github.com/googleapis/google-cloud-go/commit/f087721b7b20ad28ded1d0a84756a8bbaa2bb95a))
  * **storage:** Retry SignBlob call for URL signing ([#11154](https://github.com/googleapis/google-cloud-go/issues/11154)) ([f198452](https://github.com/googleapis/google-cloud-go/commit/f198452fd2b29e779e9080ba79d7e873eb0c32ef))



### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [2.19.0](https://github.com/googleapis/python-storage/compare/v2.18.2...v2.19.0) (2024-11-21)

##### Features

  * Add integration test for universe domain ([#1346](https://github.com/googleapis/python-storage/issues/1346)) ([02a972d](https://github.com/googleapis/python-storage/commit/02a972d35fae6d05edfb26381f6a71e3b8f59d6d))
  * Add restore_bucket and handling for soft-deleted buckets ([#1365](https://github.com/googleapis/python-storage/issues/1365)) ([ab94efd](https://github.com/googleapis/python-storage/commit/ab94efda83f68c974ec91d6b869b09047501031a))
  * Add support for restore token ([#1369](https://github.com/googleapis/python-storage/issues/1369)) ([06ed15b](https://github.com/googleapis/python-storage/commit/06ed15b33dc884da6dffbef5119e47f0fc4e1285))
  * IAM signBlob retry and universe domain support ([#1380](https://github.com/googleapis/python-storage/issues/1380)) ([abc8061](https://github.com/googleapis/python-storage/commit/abc80615ee00a14bc0e6b095252f6d1eb09c4b45))



##### Bug Fixes

  * Allow signed post policy v4 with service account and token ([#1356](https://github.com/googleapis/python-storage/issues/1356)) ([8ec02c0](https://github.com/googleapis/python-storage/commit/8ec02c0e656a4e6786f256798f4b93b95b50acec))
  * Do not spam the log with checksum related INFO messages when downloading using transfer_manager ([#1357](https://github.com/googleapis/python-storage/issues/1357)) ([42392ef](https://github.com/googleapis/python-storage/commit/42392ef8e38527ce4e50454cdd357425b3f57c87))



## November 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.45.0](https://github.com/googleapis/java-storage/compare/v2.44.1...v2.45.0) (2024-11-18)

##### Features

  * Adds support for restore token ([aef367d](https://github.com/googleapis/java-storage/commit/aef367dac146147bfbbb46b64aa91a7aebe05b6c))
  * Adds support for restore token ([#2768](https://github.com/googleapis/java-storage/issues/2768)) ([0394354](https://github.com/googleapis/java-storage/commit/0394354c81b35b66d46d84b9afb090d891ee6a12))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.49.0 ([aef367d](https://github.com/googleapis/java-storage/commit/aef367dac146147bfbbb46b64aa91a7aebe05b6c))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.50.0 ([281cccb](https://github.com/googleapis/java-storage/commit/281cccbafd2ef17c56ab4095e1f14aab2d11427e))
  * Set default values for monitored resource ([#2809](https://github.com/googleapis/java-storage/issues/2809)) ([27829a4](https://github.com/googleapis/java-storage/commit/27829a48813a2cd89d4ddf78cf8f925b64388cd8))



##### Dependencies

  * Update sdk-platform-java dependencies ([#2817](https://github.com/googleapis/java-storage/issues/2817)) ([9e961c4](https://github.com/googleapis/java-storage/commit/9e961c4a5058234f04bf71eb45185f5641c0b9a4))



## November 18, 2024

Change

Cloud Storage is now available in Querétaro, Mexico (`northamerica-south1` region). For more information, see [Cloud Storage regions](https://docs.cloud.google.com/storage/docs/locations#location-r).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.47.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.46.0...storage/v1.47.0) (2024-11-14)

##### Features

  * **storage:** Introduce dp detector based on grpc metrics ([#11100](https://github.com/googleapis/google-cloud-go/issues/11100)) ([60c2323](https://github.com/googleapis/google-cloud-go/commit/60c2323102b623e042fc508e2b1bb830a03f9577))



##### Bug Fixes

  * **storage:** Bump auth dep ([#11135](https://github.com/googleapis/google-cloud-go/issues/11135)) ([9620a51](https://github.com/googleapis/google-cloud-go/commit/9620a51b2c6904d8d93e124494bc297fb98553d2))



## November 15, 2024

Change

You can now use the [`x-amz-decoded-content-length` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xamzdecodedcontentlength) to allow an XML API upload that uses chunked transfer encoding to include a [signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) in its `Authorization` header.

## November 07, 2024

Feature

You can now restore soft-deleted buckets. If you delete a bucket with an active soft delete policy, Cloud Storage retains the bucket for the specified soft delete retention duration, during which the bucket can be restored to a live state. To learn more about the bucket restore feature, see [Use soft-deleted buckets](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).

## November 04, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.14.0](https://github.com/googleapis/nodejs-storage/compare/v7.13.0...v7.14.0) (2024-10-29)

##### Features

  * Add support for restore token ([#2548](https://github.com/googleapis/nodejs-storage/issues/2548)) ([8241e91](https://github.com/googleapis/nodejs-storage/commit/8241e91e78d47b4cdaea2d941f75fd6a4fa29230))
  * Adds integration tests for Universe Domain configuration ([#2538](https://github.com/googleapis/nodejs-storage/issues/2538)) ([53db6ba](https://github.com/googleapis/nodejs-storage/commit/53db6ba7406b99e507cacfa6195cb5a7d308914b))
  * Adds integration tests for Universe Domain configuration with ([53db6ba](https://github.com/googleapis/nodejs-storage/commit/53db6ba7406b99e507cacfa6195cb5a7d308914b))
  * **storage:** Add support for 'skipIfExists' option for downloadMany ([#2526](https://github.com/googleapis/nodejs-storage/issues/2526)) ([729efb2](https://github.com/googleapis/nodejs-storage/commit/729efb213f96b1a406a1caa54870f50e96796639))



### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.46.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.45.0...storage/v1.46.0) (2024-10-31)

##### Features

  * **storage:** Add grpc metrics experimental options ([#10984](https://github.com/googleapis/google-cloud-go/issues/10984)) ([5b7397b](https://github.com/googleapis/google-cloud-go/commit/5b7397b169176f030049e1511859a883422c774e))



##### Bug Fixes

  * **storage:** Skip only specific transport tests. ([#11016](https://github.com/googleapis/google-cloud-go/issues/11016)) ([d40fbff](https://github.com/googleapis/google-cloud-go/commit/d40fbff9c1984aeed0224a4ac93eb95c5af17126))
  * **storage:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **storage:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([2b8ca4b](https://github.com/googleapis/google-cloud-go/commit/2b8ca4b4127ce3025c7a21cc7247510e07cc5625))



##### Miscellaneous Chores

  * **storage/internal:** Remove notification, service account, and hmac RPCS. These API have been migrated to Storage Control and are available via the JSON API. ([#11008](https://github.com/googleapis/google-cloud-go/issues/11008)) ([e0759f4](https://github.com/googleapis/google-cloud-go/commit/e0759f46639b4c542e5b49e4dc81340d8e123370))



## October 29, 2024

Change

[Data Access logs](https://docs.cloud.google.com/storage/docs/audit-logging#available-logs) are now compatible with all [authenticated browser downloads](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth).

  * When an authenticated browser download occurs outside of the Google Cloud console, a resulting Data Access log has its `principalEmail` and `callerIp` fields redacted.



## October 28, 2024

Change

Additional functionality is now available for the [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) and [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) features:

  * You can now [enable Object Retention Lock on existing buckets using the Console](https://docs.cloud.google.com/storage/docs/using-object-lock#enable-retentions).

  * Enabling Object Retention Lock on a bucket will cause a [lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) to be placed, at best effort, on the project containing the bucket.

  * Buckets can now have Bucket Lock and [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled at the same time.




Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.44.1](https://github.com/googleapis/java-storage/compare/v2.44.0...v2.44.1) (2024-10-25)

##### Dependencies

  * Update sdk-platform-java dependencies ([#2795](https://github.com/googleapis/java-storage/issues/2795)) ([aeb86e5](https://github.com/googleapis/java-storage/commit/aeb86e5467269d55f9019638fe8b05331b423e55))



#### [2.44.0](https://github.com/googleapis/java-storage/compare/v2.43.2...v2.44.0) (2024-10-23)

##### Features

  * Promote gRPC transport to GA ([#2766](https://github.com/googleapis/java-storage/issues/2766)) ([41fd72a](https://github.com/googleapis/java-storage/commit/41fd72a57e3577217e98f7a179d8958c14c5676a))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.47.0 ([c517798](https://github.com/googleapis/java-storage/commit/c5177983a48b1bf26e8abb5d4d27355bfcd62d3b))
  * Fix createFrom resumable upload retry offset calculation ([#2771](https://github.com/googleapis/java-storage/issues/2771)) ([1126cdc](https://github.com/googleapis/java-storage/commit/1126cdcde07fed3c57d99dfa2b2505b06d5cd25a)), closes [#2770](https://github.com/googleapis/java-storage/issues/2770)
  * Update gRPC ReadObject retry to avoid double retry ([#2765](https://github.com/googleapis/java-storage/issues/2765)) ([1fc57b9](https://github.com/googleapis/java-storage/commit/1fc57b9b4fe2ec2d08333fb62be66f272294deca))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20241008-2.0.0 ([#2776](https://github.com/googleapis/java-storage/issues/2776)) ([0545b5e](https://github.com/googleapis/java-storage/commit/0545b5e7d7e292da38fb42a9160fb1938628684b))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.38.0 ([#2787](https://github.com/googleapis/java-storage/issues/2787)) ([a470e88](https://github.com/googleapis/java-storage/commit/a470e880f348a4950102546c7ee844761e1c5b57))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.48.0 ([#2781](https://github.com/googleapis/java-storage/issues/2781)) ([8fa013e](https://github.com/googleapis/java-storage/commit/8fa013e09e3c02c6deeb6d49911c051b940ef79c))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.49.0 ([#2782](https://github.com/googleapis/java-storage/issues/2782)) ([a7baffb](https://github.com/googleapis/java-storage/commit/a7baffb9579f865a20fe42d189f8ba9d8b4ee716))
  * Update googleapis/sdk-platform-java action to v2.48.0 ([#2786](https://github.com/googleapis/java-storage/issues/2786)) ([2893e61](https://github.com/googleapis/java-storage/commit/2893e617b865717959da34a47d2a972ad90cde72))



Feature

You can now use the Google Cloud console to get [soft delete recommendations](https://docs.cloud.google.com/storage/docs/soft-delete-recommender) for buckets. Soft delete recommendations help you determine when it's best to enable or disable the soft delete feature on a bucket based on impact to cost and security.

## October 23, 2024

Announcement

[Announced billing changes](https://cloud.google.com/resources/storage/billing-fix-bigquery) for BigQuery users who are accessing Cloud Storage will now take effect February 1, 2025. These changes were originally set to take effect November 1, 2024.

## October 22, 2024

Feature

You can now emit client-side metrics for gRPC. To learn which metrics are supported and how to emit them, see [Use gRPC client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics).

Feature

[Connecting to Cloud Storage using gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can use [gRPC](https://grpc.io/) to interact with Cloud Storage.

## October 21, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.45.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.44.0...storage/v1.45.0) (2024-10-17)

##### Features

  * **storage/internal:** Adds support for restore token ([70d82fe](https://github.com/googleapis/google-cloud-go/commit/70d82fe93f60f1075298a077ce1616f9ae7e13fe))
  * **storage:** Adding bucket-specific dynamicDelay ([#10987](https://github.com/googleapis/google-cloud-go/issues/10987)) ([a807a7e](https://github.com/googleapis/google-cloud-go/commit/a807a7e7f9fb002374407622c126102c5e61af82))
  * **storage:** Dynamic read request stall timeout ([#10958](https://github.com/googleapis/google-cloud-go/issues/10958)) ([a09f00e](https://github.com/googleapis/google-cloud-go/commit/a09f00eeecac82af98ae769bab284ee58a3a66cb))



##### Documentation

  * **storage:** Remove preview wording from NewGRPCClient ([#11002](https://github.com/googleapis/google-cloud-go/issues/11002)) ([40c3a5b](https://github.com/googleapis/google-cloud-go/commit/40c3a5b9c4cd4db2f1695e180419197b6a03ed7f))



## October 15, 2024

Feature

Hierarchical namespace for Cloud Storage buckets is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). With hierarchical namespace, you can store your data in a logical file system structure.

## October 14, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.43.2](https://github.com/googleapis/java-storage/compare/v2.43.1...v2.43.2) (2024-10-08)

##### Bug Fixes

  * Plumb list blobs match glob option for grpc transport ([#2759](https://github.com/googleapis/java-storage/issues/2759)) ([207abd1](https://github.com/googleapis/java-storage/commit/207abd110ac2e1854804332025e6ea7806df1785))



##### Dependencies

  * Update dependency com.google.api:gapic-generator-java to v2.47.0 ([#2750](https://github.com/googleapis/java-storage/issues/2750)) ([9041f24](https://github.com/googleapis/java-storage/commit/9041f242c185a8a96361a087d42c5be7ba06a583))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240924-2.0.0 ([#2719](https://github.com/googleapis/java-storage/issues/2719)) ([7b19831](https://github.com/googleapis/java-storage/commit/7b19831b48153bb7f6744f5d7b8559c244d483d7))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.37.0 ([#2751](https://github.com/googleapis/java-storage/issues/2751)) ([003d6fa](https://github.com/googleapis/java-storage/commit/003d6faaa3d64310cf91a1e304247e2f44a5c9c7))
  * Update googleapis/sdk-platform-java action to v2.47.0 ([#2749](https://github.com/googleapis/java-storage/issues/2749)) ([befa415](https://github.com/googleapis/java-storage/commit/befa415d69743faf079930315c5ebd8afaa52d7f))



## October 07, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.44.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.43.0...storage/v1.44.0) (2024-10-03)

##### Features

  * **storage/dataflux:** Add dataflux interface ([#10748](https://github.com/googleapis/google-cloud-go/issues/10748)) ([cb7b0a1](https://github.com/googleapis/google-cloud-go/commit/cb7b0a1b285de9d4182155a123747419232dd35f))
  * **storage/dataflux:** Add range_splitter [#10748](https://github.com/googleapis/google-cloud-go/issues/10748) ([#10899](https://github.com/googleapis/google-cloud-go/issues/10899)) ([d49da26](https://github.com/googleapis/google-cloud-go/commit/d49da26be7dc52fad37c392c2876f62b1a5625a2))
  * **storage/dataflux:** Add worksteal algorithm to fast-listing ([#10913](https://github.com/googleapis/google-cloud-go/issues/10913)) ([015b52c](https://github.com/googleapis/google-cloud-go/commit/015b52c345df75408be3edcfda96d37145794f9f))
  * **storage/internal:** Add managed folder to testIamPermissions method ([2f0aec8](https://github.com/googleapis/google-cloud-go/commit/2f0aec894179304d234be6c792d82cf4336b6d0a))
  * **storage/transfermanager:** Add option to StripPrefix on directory download ([#10894](https://github.com/googleapis/google-cloud-go/issues/10894)) ([607534c](https://github.com/googleapis/google-cloud-go/commit/607534cdd5edf2d15d3de891cf6a0b6cbaa7d545))
  * **storage/transfermanager:** Add SkipIfExists option ([#10893](https://github.com/googleapis/google-cloud-go/issues/10893)) ([7daa1bd](https://github.com/googleapis/google-cloud-go/commit/7daa1bdc78844adac80f6378b1f6f2dd415b80a8))
  * **storage/transfermanager:** Checksum full object downloads ([#10569](https://github.com/googleapis/google-cloud-go/issues/10569)) ([c366c90](https://github.com/googleapis/google-cloud-go/commit/c366c908534ef09442f1f3e8a4f74bd545a474fb))
  * **storage:** Add direct google access side-effect imports by default ([#10757](https://github.com/googleapis/google-cloud-go/issues/10757)) ([9ad8324](https://github.com/googleapis/google-cloud-go/commit/9ad83248a7049c82580bc45d9685c329811bce88))
  * **storage:** Add full object checksum to reader.Attrs ([#10538](https://github.com/googleapis/google-cloud-go/issues/10538)) ([245d2ea](https://github.com/googleapis/google-cloud-go/commit/245d2eaddb4862da7c8d1892d5d462bf390adb2b))
  * **storage:** Add support for Go 1.23 iterators ([84461c0](https://github.com/googleapis/google-cloud-go/commit/84461c0ba464ec2f951987ba60030e37c8a8fc18))
  * **storage:** Add update time in bucketAttrs ([#10710](https://github.com/googleapis/google-cloud-go/issues/10710)) ([5f06ae1](https://github.com/googleapis/google-cloud-go/commit/5f06ae1a331c46ded47c96c205b3f1be92d64d29)), refs [#9361](https://github.com/googleapis/google-cloud-go/issues/9361)
  * **storage:** GA gRPC client ([#10859](https://github.com/googleapis/google-cloud-go/issues/10859)) ([c7a55a2](https://github.com/googleapis/google-cloud-go/commit/c7a55a26c645905317fe27505d503c338f50ee34))
  * **storage:** Introduce gRPC client-side metrics ([#10639](https://github.com/googleapis/google-cloud-go/issues/10639)) ([437bcb1](https://github.com/googleapis/google-cloud-go/commit/437bcb1e0b514959648eed36ba3963aa4fbeffc8))
  * **storage:** Support IncludeFoldersAsPrefixes for gRPC ([#10767](https://github.com/googleapis/google-cloud-go/issues/10767)) ([65bcc59](https://github.com/googleapis/google-cloud-go/commit/65bcc59a6c0753f8fbd66c8792bc69300e95ec62))



##### Bug Fixes

  * **storage/transfermanager:** Correct Attrs.StartOffset for sharded downloads ([#10512](https://github.com/googleapis/google-cloud-go/issues/10512)) ([01a5cbb](https://github.com/googleapis/google-cloud-go/commit/01a5cbba6d9d9f425f045b58fa16d8c85804c29c))
  * **storage:** Add retryalways policy to encryption test ([#10644](https://github.com/googleapis/google-cloud-go/issues/10644)) ([59cfd12](https://github.com/googleapis/google-cloud-go/commit/59cfd12ce5650279c99787da4a273db1e3253c76)), refs [#10567](https://github.com/googleapis/google-cloud-go/issues/10567)
  * **storage:** Add unknown host to retriable errors ([#10619](https://github.com/googleapis/google-cloud-go/issues/10619)) ([4ec0452](https://github.com/googleapis/google-cloud-go/commit/4ec0452a393341b1036ac6e1e7287843f097d978))
  * **storage:** Bump dependencies ([2ddeb15](https://github.com/googleapis/google-cloud-go/commit/2ddeb1544a53188a7592046b98913982f1b0cf04))
  * **storage:** Bump google.golang.org/grpc@v1.64.1 ([8ecc4e9](https://github.com/googleapis/google-cloud-go/commit/8ecc4e9622e5bbe9b90384d5848ab816027226c5))
  * **storage:** Check for grpc NotFound error in HMAC test ([#10645](https://github.com/googleapis/google-cloud-go/issues/10645)) ([3c8e88a](https://github.com/googleapis/google-cloud-go/commit/3c8e88a085bab3142dfff6ef9a8e49c29a5c877d))
  * **storage:** Disable grpc metrics using emulator ([#10870](https://github.com/googleapis/google-cloud-go/issues/10870)) ([35ad73d](https://github.com/googleapis/google-cloud-go/commit/35ad73d3be5485ac592e2ef1ea6c0854f1eff4a0))
  * **storage:** Retry gRPC DEADLINE_EXCEEDED errors ([#10635](https://github.com/googleapis/google-cloud-go/issues/10635)) ([0018415](https://github.com/googleapis/google-cloud-go/commit/0018415295a5fd964b923db6a4785e9eed46a2e2))
  * **storage:** Update dependencies ([257c40b](https://github.com/googleapis/google-cloud-go/commit/257c40bd6d7e59730017cf32bda8823d7a232758))
  * **storage:** Update google.golang.org/api to v0.191.0 ([5b32644](https://github.com/googleapis/google-cloud-go/commit/5b32644eb82eb6bd6021f80b4fad471c60fb9d73))



##### Performance Improvements

  * **storage:** GRPC zerocopy codec ([#10888](https://github.com/googleapis/google-cloud-go/issues/10888)) ([aeba28f](https://github.com/googleapis/google-cloud-go/commit/aeba28ffffcd82ac5540e45247112bdacc5c530d))



##### Documentation

  * **storage/internal:** Clarify possible objectAccessControl roles ([2f0aec8](https://github.com/googleapis/google-cloud-go/commit/2f0aec894179304d234be6c792d82cf4336b6d0a))
  * **storage/internal:** Update dual-region bucket link ([2f0aec8](https://github.com/googleapis/google-cloud-go/commit/2f0aec894179304d234be6c792d82cf4336b6d0a))



## September 30, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.43.1](https://github.com/googleapis/java-storage/compare/v2.43.0...v2.43.1) (2024-09-26)

##### Bug Fixes

  * Add managed folder to testIamPermissions method ([556dd95](https://github.com/googleapis/java-storage/commit/556dd95c2cf7180cb14c12a2f7ecc288c0c49ea9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.46.0 ([556dd95](https://github.com/googleapis/java-storage/commit/556dd95c2cf7180cb14c12a2f7ecc288c0c49ea9))
  * Remove server unimplemented GrpcStorageImpl#{get,list,create,delete,Update}HmacKey ([#2717](https://github.com/googleapis/java-storage/issues/2717)) ([06f7292](https://github.com/googleapis/java-storage/commit/06f7292036c39ca7f10119a1b906c604a0c34344))
  * Remove server unimplemented GrpcStorageImpl#{get,list,create,delete}Notification ([#2710](https://github.com/googleapis/java-storage/issues/2710)) ([310c9b2](https://github.com/googleapis/java-storage/commit/310c9b285024573a7e58dfb07f41b482a8a3372f))
  * Remove server unimplemented GrpcStorageImpl#getServiceAccount ([#2718](https://github.com/googleapis/java-storage/issues/2718)) ([51076a8](https://github.com/googleapis/java-storage/commit/51076a87eae57ec6763bdbfa20dcc390b688fc82))
  * Update grpc based ReadObject rpcs to remove race condition between cancellation and message handling ([#2708](https://github.com/googleapis/java-storage/issues/2708)) ([2c7f088](https://github.com/googleapis/java-storage/commit/2c7f08868df8adba623178d679a100f19d10f070))
  * Update grpc upload error diagnostics to be tolerant of receiving an error if no request has been sent ([#2732](https://github.com/googleapis/java-storage/issues/2732)) ([fff72d5](https://github.com/googleapis/java-storage/commit/fff72d5cfeca9ad3348e7c9b72e2740024dcbbb6))
  * Update GrpcStorageOptions to attempt direct path by default ([#2715](https://github.com/googleapis/java-storage/issues/2715)) ([9de9a92](https://github.com/googleapis/java-storage/commit/9de9a92be05f36bbe6afabeffcc597470a92b5a3))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.36.0 ([#2721](https://github.com/googleapis/java-storage/issues/2721)) ([11f09fe](https://github.com/googleapis/java-storage/commit/11f09febb76a50fc0e19ec096c9bbad485764c8b))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#2738](https://github.com/googleapis/java-storage/issues/2738)) ([eb320e1](https://github.com/googleapis/java-storage/commit/eb320e104bca9e5a7c192d58147045bf7201ffc7))
  * Update googleapis/sdk-platform-java action to v2.46.1 ([#2736](https://github.com/googleapis/java-storage/issues/2736)) ([795f2c3](https://github.com/googleapis/java-storage/commit/795f2c34c1bc389179c2ca2bafba0803fff5e38e))



## September 25, 2024

Feature

[Cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication) is now available in Cloud Storage. You can use cross-bucket replication to copy new and updated objects asynchronously from a source bucket to a destination bucket. For more information on how to use cross-bucket replication, see [Using cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication).

## September 24, 2024

Feature

Cloud Storage is now enabled for use with Cloud KMS Autokey.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys). To learn more about Cloud KMS Autokey, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## September 23, 2024

Feature

You can now use [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) with Cloud Storage FUSE. To learn more about how mounting buckets with hierarchical namespace enabled can help improve performance, see [Mount buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/gcsfuse-performance#hierarchical-namespace).

Change

In order to set a bucket to store [Cloud Storage usage logs and storage logs](https://docs.cloud.google.com/storage/docs/access-logs), the bucket must now reside within the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) as the bucket being logged.

  * If the bucket being logged is not associated with an organization, then the bucket storing the logs must reside within the same [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) instead.



Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.13.0](https://github.com/googleapis/nodejs-storage/compare/v7.12.1...v7.13.0) (2024-09-17)

##### Features

  * **storage:** Add support for 'fields' query parameter to getFiles ([#2521](https://github.com/googleapis/nodejs-storage/issues/2521)) ([f78fe92](https://github.com/googleapis/nodejs-storage/commit/f78fe92348a0b383314b4fbfb55638d47af052ff))



##### Bug Fixes

  * **retry:** Export RETRYABLE_ERR_FN_DEFAULT ([#2517](https://github.com/googleapis/nodejs-storage/issues/2517)) ([db890fd](https://github.com/googleapis/nodejs-storage/commit/db890fd1b25d5cd94e3bcd97ec21fa8f77b1b724))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.43.0](https://github.com/googleapis/java-storage/compare/v2.42.0...v2.43.0) (2024-09-13)

##### Features

  * Allow specifying an expected object size for resumable operations. ([#2661](https://github.com/googleapis/java-storage/issues/2661)) ([3405611](https://github.com/googleapis/java-storage/commit/3405611f20153246691910aa33fed800ab989669)), closes [#2511](https://github.com/googleapis/java-storage/issues/2511)



##### Bug Fixes

  * Close pending zero-copy responses when Storage#close is called ([#2696](https://github.com/googleapis/java-storage/issues/2696)) ([1855308](https://github.com/googleapis/java-storage/commit/185530823a7d2378add1f95589f191326c9ae173))
  * GitHub workflow vulnerable to script injection ([#2663](https://github.com/googleapis/java-storage/issues/2663)) ([9151ac2](https://github.com/googleapis/java-storage/commit/9151ac27638e4491628d5bbb51643abc6bcd5f54))
  * Make ParallelCompositeUploadBlobWriteSessionConfig.ExecutorSupplier#cachedPool a singleton ([#2691](https://github.com/googleapis/java-storage/issues/2691)) ([1494809](https://github.com/googleapis/java-storage/commit/1494809af5624d7076b70087da8f81f31c6f61e7))



##### Dependencies

  * Promote storage-v2 artifacts to beta ([9d22597](https://github.com/googleapis/java-storage/commit/9d225978639cdf49601759d6f7c65a420be71c7a))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240819-2.0.0 ([#2665](https://github.com/googleapis/java-storage/issues/2665)) ([3df1000](https://github.com/googleapis/java-storage/commit/3df1000f137d54ef42c9b25e90a301c512644e2b))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.35.0 ([#2698](https://github.com/googleapis/java-storage/issues/2698)) ([1dd51c3](https://github.com/googleapis/java-storage/commit/1dd51c32948cae2cadbc6e3be1b23ab0bd6063a3))



## September 11, 2024

Feature

You can now specify United States regions when using [regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints).

## September 09, 2024

Feature

You can now use the Google Cloud console to do the following:

  * Create buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. To learn more, see [Create a bucket](https://docs.cloud.google.com/storage/docs/create-hns-bucket#storage-create-bucket-console).

  * Create and manage [folders](https://docs.cloud.google.com/storage/docs/folders-overview) in buckets with hierarchical namespace enabled. To learn more, see [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).

  * Rename and move folders. To learn more, see [Rename and move folders](https://docs.cloud.google.com/storage/docs/rename-hns-folders#console).




## August 26, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.42.0](https://github.com/googleapis/java-storage/compare/v2.41.0...v2.42.0) (2024-08-19)

##### Features

  * Enable grpc.lb.locality label for client-side metrics ([#2659](https://github.com/googleapis/java-storage/issues/2659)) ([b681ee0](https://github.com/googleapis/java-storage/commit/b681ee0d7c535db3dc4ede0c2b67bf2306aaf9f0))



##### Bug Fixes

  * Update modified field handling for blob and bucket with json transport to properly clear fields ([#2664](https://github.com/googleapis/java-storage/issues/2664)) ([e2f5537](https://github.com/googleapis/java-storage/commit/e2f553788eb3f3685056728de75c358893887604)), closes [#2662](https://github.com/googleapis/java-storage/issues/2662)



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.34.0 ([#2673](https://github.com/googleapis/java-storage/issues/2673)) ([453c29a](https://github.com/googleapis/java-storage/commit/453c29abb8e970a1a639a39af3c0e3e8516fdda5))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.45.0 ([#2667](https://github.com/googleapis/java-storage/issues/2667)) ([1f66dff](https://github.com/googleapis/java-storage/commit/1f66dfff67dcab49596f25aa43651c7f098f12ad))



## August 12, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.12.1](https://github.com/googleapis/nodejs-storage/compare/v7.12.0...v7.12.1) (2024-08-07)

##### Bug Fixes

  * **deps:** Update fast-xml-parser to 4.4.1 due to security vulnerability ([#2505](https://github.com/googleapis/nodejs-storage/issues/2505)) ([b97d474](https://github.com/googleapis/nodejs-storage/commit/b97d474445efbcde91e690f6ea4160cfc9fd1ed4))



### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [2.18.2](https://github.com/googleapis/python-storage/compare/v2.18.1...v2.18.2) (2024-08-08)

##### Bug Fixes

  * Add regression test for range read retry issue and bump dependency to fix ([#1338](https://github.com/googleapis/python-storage/issues/1338)) ([0323647](https://github.com/googleapis/python-storage/commit/0323647d768b3be834cfab53efb3c557a47d41c3))



#### [2.18.1](https://github.com/googleapis/python-storage/compare/v2.18.0...v2.18.1) (2024-08-05)

##### Bug Fixes

  * Properly escape URL construction for XML MPU API ([#1333](https://github.com/googleapis/python-storage/issues/1333)) ([bf4d0e0](https://github.com/googleapis/python-storage/commit/bf4d0e0a2ef1d608d679c22b13d8f5d90b39c7b2))



## August 05, 2024

Feature

You can now use parallel downloads with Cloud Storage FUSE to accelerate read performance of large files over 1 GB in size. When enabled, parallel downloads use multiple workers to download a file in parallel, accelerating file reads. For more information, see [Improve read performance using parallel downloads](https://docs.cloud.google.com/storage/docs/gcsfuse-performance-and-best-practices#parallel-downloads).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.41.0](https://github.com/googleapis/java-storage/compare/v2.40.1...v2.41.0) (2024-07-31)

##### Features

  * Enable gRPC client open telemetry metrics reporting ([#2590](https://github.com/googleapis/java-storage/issues/2590)) ([d153228](https://github.com/googleapis/java-storage/commit/d153228a301007b5952de9722f370dda0784473a))



##### Bug Fixes

  * Add UnknownHostException to set of retriable exception ([#2651](https://github.com/googleapis/java-storage/issues/2651)) ([18de9fc](https://github.com/googleapis/java-storage/commit/18de9fcdb831132336eca4112dfe0515174bba7b))
  * Update grpc resumable upload error categorization to be more tolerant ([#2644](https://github.com/googleapis/java-storage/issues/2644)) ([95697dd](https://github.com/googleapis/java-storage/commit/95697dd3d744351058c13793c6ae576820f6b638))
  * Update Storage#readAllBytes to respect shouldReturnRawInputStream option ([#2635](https://github.com/googleapis/java-storage/issues/2635)) ([dc883cc](https://github.com/googleapis/java-storage/commit/dc883cce5f547def7cfb34c4f8a2d409493e4cb9))
  * Update TransferManager downloads to reduce in memory buffering ([#2630](https://github.com/googleapis/java-storage/issues/2630)) ([fc2fd75](https://github.com/googleapis/java-storage/commit/fc2fd750ed60b840e6285a4b1f4ecce739df4c09))
  * Use fast calculation for totalRemaining number of bytes from multiple ByteBuffers ([#2633](https://github.com/googleapis/java-storage/issues/2633)) ([758b3dd](https://github.com/googleapis/java-storage/commit/758b3dd3cc4f6dfc2dfc12c3a77472d97c31c5d5))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240625-2.0.0 ([#2616](https://github.com/googleapis/java-storage/issues/2616)) ([b22babb](https://github.com/googleapis/java-storage/commit/b22babbe26572d8c4289a65a0b125b2a60e8ef79))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240706-2.0.0 ([#2634](https://github.com/googleapis/java-storage/issues/2634)) ([1ccaa0c](https://github.com/googleapis/java-storage/commit/1ccaa0c64887a0661438957e9427237ee005ccf1))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.33.0 ([#2647](https://github.com/googleapis/java-storage/issues/2647)) ([8196259](https://github.com/googleapis/java-storage/commit/8196259927330ecfe3e604c24d248f7935e7fe0d))
  * Update dependency net.jqwik:jqwik to v1.9.0 ([#2608](https://github.com/googleapis/java-storage/issues/2608)) ([a20eb66](https://github.com/googleapis/java-storage/commit/a20eb660ddfa4b68d79ce04496064f3025676d5a))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.3 ([#2604](https://github.com/googleapis/java-storage/issues/2604)) ([8c79f39](https://github.com/googleapis/java-storage/commit/8c79f39ad78d100065c189bcf8e18644b29ff9ed))
  * Update junit-platform.version to v5.10.3 ([#2605](https://github.com/googleapis/java-storage/issues/2605)) ([a532ee4](https://github.com/googleapis/java-storage/commit/a532ee49e2ff5972ea8a2aabbab2dcf6fe0df774))



## August 01, 2024

Announcement

Beginning November 1, 2024, BigQuery users will start seeing charges for Cloud Storage usage as per [pricing documentation](https://cloud.google.com/storage/pricing), which was not metered before due to a billing bug.

  * Retrieval fees for Nearline, Coldline, and Archive storage classes will be charged per existing [pricing documentation](https://cloud.google.com/storage/pricing#retrieval-pricing) and [retrieval SKUs](https://cloud.google.com/skus?filter=95FF-2EF5-5EA1+Retrieval&currency=USD).

  * Inter Region Network Data Transfer fees will be charged when a BigQuery job in one location reads data stored in a Cloud Storage bucket in a different location. These charges are covered by [**GCP Storage Data Transfer** SKUs](https://cloud.google.com/skus?filter=%22GCP+Storage+Data+Transfer+between%22) and [**Network Data Transfer GCP Inter Region** SKUs](https://cloud.google.com/skus?filter=%22Network+Data+Transfer+GCP+Inter+Region%22+95ff-2ef5-5ea1). **Network Data Transfer GCP Multi-region** SKUs are not applicable to this change.

  * Refer to the [announcement](https://cloud.google.com/resources/storage/billing-fix-bigquery) for more information.




## July 31, 2024

Feature

You can now use the Google Cloud console to set a default soft delete retention duration. For more information, see [Use tags to set a default soft delete retention duration for new buckets](https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete#overview).

Feature

You can now use list caching with Cloud Storage FUSE, which is a cache for directory and file list, or `ls`, responses that improves list operation speeds. To learn more about list caching and how to enable it, see the [Cloud Storage FUSE caching overview page](https://docs.cloud.google.com/storage/docs/gcsfuse-cache#list-cache-overview).

## July 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [2.18.0](https://github.com/googleapis/python-storage/compare/v2.17.0...v2.18.0) (2024-07-09)

##### Features

  * Add OpenTelemetry Tracing support as a preview feature ([#1288](https://github.com/googleapis/python-storage/issues/1288)) ([c2ab0e0](https://github.com/googleapis/python-storage/commit/c2ab0e035b179a919b27c7f50318472f14656e00))



##### Bug Fixes

  * Allow Protobuf 5.x ([#1317](https://github.com/googleapis/python-storage/issues/1317)) ([152b249](https://github.com/googleapis/python-storage/commit/152b249472a09342777237d47b6c09f99c2d28e6))
  * Correct notification error message ([#1290](https://github.com/googleapis/python-storage/issues/1290)) ([1cb977d](https://github.com/googleapis/python-storage/commit/1cb977daa2d97c255a382ce81f56a43168b0637d)), closes [#1289](https://github.com/googleapis/python-storage/issues/1289)



## July 23, 2024

Feature

You can now use tags to set a default soft delete retention duration on newly created buckets in your organization. To learn how to customize a default soft delete retention duration, see [Set a default soft delete retention duration](https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete).

## July 22, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.12.0](https://github.com/googleapis/nodejs-storage/compare/v7.11.3...v7.12.0) (2024-07-15)

##### Features

  * Add function to allow user to set destination in transfer manager ([#2497](https://github.com/googleapis/nodejs-storage/issues/2497)) ([dc1e488](https://github.com/googleapis/nodejs-storage/commit/dc1e488b50dd7e2deab3e8b28c7d6ece36b90b0e))



## July 15, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.11.3](https://github.com/googleapis/nodejs-storage/compare/v7.11.2...v7.11.3) (2024-07-09)

##### Bug Fixes

  * Error serialization in resumable-upload.ts ([#2493](https://github.com/googleapis/nodejs-storage/issues/2493)) ([c2e555c](https://github.com/googleapis/nodejs-storage/commit/c2e555c95f7a8e3e231e57e2fa3967caeb860772))
  * Handle unhandled error in `startResumableUpload_` ([#2495](https://github.com/googleapis/nodejs-storage/issues/2495)) ([d5257ba](https://github.com/googleapis/nodejs-storage/commit/d5257ba4aa9efc1dd70c303286782d23a95e8568))
  * Make CreateBucketRequest extend from BucketMetadata to allow all… ([#2489](https://github.com/googleapis/nodejs-storage/issues/2489)) ([013a5a4](https://github.com/googleapis/nodejs-storage/commit/013a5a45aed8734f797837deb0e805f0ca43a9a6))



## July 11, 2024

Feature

You can now specify Frankfurt (europe-west3) and Zürich (europe-west6) as a predefined dual-region pairing. For more information, see [Predefined dual-regions](https://docs.cloud.google.com/storage/docs/locations#predefined).

## July 08, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.43.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.42.0...storage/v1.43.0) (2024-07-03)

##### Features

  * **storage/transfermanager:** Add DownloadDirectory ([#10430](https://github.com/googleapis/google-cloud-go/issues/10430)) ([0d0e5dd](https://github.com/googleapis/google-cloud-go/commit/0d0e5dd5214769cc2c197991c2ece1303bd600de))
  * **storage/transfermanager:** Automatically shard downloads ([#10379](https://github.com/googleapis/google-cloud-go/issues/10379)) ([05816f9](https://github.com/googleapis/google-cloud-go/commit/05816f9fafd3132c371da37f3a879bb9e8e7e604))



##### Bug Fixes

  * **storage/transfermanager:** WaitAndClose waits for Callbacks to finish ([#10504](https://github.com/googleapis/google-cloud-go/issues/10504)) ([0e81002](https://github.com/googleapis/google-cloud-go/commit/0e81002b3a5e560c874d814d28a35a102311d9ef)), refs [#10502](https://github.com/googleapis/google-cloud-go/issues/10502)
  * **storage:** Allow empty soft delete on Create ([#10394](https://github.com/googleapis/google-cloud-go/issues/10394)) ([d8bd2c1](https://github.com/googleapis/google-cloud-go/commit/d8bd2c1ffc4f27503a74ded438d8bfbdd7707c63)), refs [#10380](https://github.com/googleapis/google-cloud-go/issues/10380)
  * **storage:** Bump google.golang.org/api@v0.187.0 ([8fa9e39](https://github.com/googleapis/google-cloud-go/commit/8fa9e398e512fd8533fd49060371e61b5725a85b))
  * **storage:** Retry broken pipe error ([#10374](https://github.com/googleapis/google-cloud-go/issues/10374)) ([2f4daa1](https://github.com/googleapis/google-cloud-go/commit/2f4daa11acf9d3f260fa888333090359c4d9198e)), refs [#9178](https://github.com/googleapis/google-cloud-go/issues/9178)



##### Documentation

  * **storage/control:** Remove allowlist note from Folders RPCs ([d6c543c](https://github.com/googleapis/google-cloud-go/commit/d6c543c3969016c63e158a862fc173dff60fb8d9))



Feature

You can now specify London (`europe-west2`) and Frankfurt (`europe-west3`) as a predefined dual-region pairing. For more information, see [Predefined dual-regions](https://docs.cloud.google.com/storage/docs/locations#predefined).

## July 02, 2024

Feature

You can now disable soft delete for multiple buckets at a time or for all buckets in a project. To learn more, see [Bulk disable soft delete](https://docs.cloud.google.com/storage/docs/use-soft-delete#bulk-turn-off-soft-delete-policy).

## July 01, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.40.1](https://github.com/googleapis/java-storage/compare/v2.40.0...v2.40.1) (2024-06-26)

##### Bug Fixes

  * Add a workaround to make sure grpc clients' hosts always match their universe domain ([#2588](https://github.com/googleapis/java-storage/issues/2588)) ([87bf737](https://github.com/googleapis/java-storage/commit/87bf7371b6c4300b0f306ca36d1918d52adf721b))
  * Include x-goog-user-project on resumable upload puts for grpc transport ([#2586](https://github.com/googleapis/java-storage/issues/2586)) ([6f2f504](https://github.com/googleapis/java-storage/commit/6f2f5045bb7c1dabdd9b1c19ce7d2b02163c0eb8))
  * Update grpc bidi resumable uploads to validate ack'd object size ([#2570](https://github.com/googleapis/java-storage/issues/2570)) ([5c9cecf](https://github.com/googleapis/java-storage/commit/5c9cecf04ceb3858d58b4e2e487ffd1dddf933ab))
  * Update grpc finalize on close resumable uploads to validate ack'd object size ([#2572](https://github.com/googleapis/java-storage/issues/2572)) ([55a6d15](https://github.com/googleapis/java-storage/commit/55a6d155e4c6a4c33f22ec87ff0b9f6ccfab7a83))
  * Update grpc single-shot uploads to validate ack'd object size ([#2567](https://github.com/googleapis/java-storage/issues/2567)) ([65c8808](https://github.com/googleapis/java-storage/commit/65c8808da9094365171f165dcf0654f56cf51207))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240524-2.0.0 ([#2565](https://github.com/googleapis/java-storage/issues/2565)) ([d193243](https://github.com/googleapis/java-storage/commit/d193243e1bcc41d09d46f9aa521ed5dd1b374b52))
  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240621-2.0.0 ([#2596](https://github.com/googleapis/java-storage/issues/2596)) ([73b8753](https://github.com/googleapis/java-storage/commit/73b8753c244ca8ac9605c1430251b6aebaf82905))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.32.0 ([#2597](https://github.com/googleapis/java-storage/issues/2597)) ([25940a4](https://github.com/googleapis/java-storage/commit/25940a4e8c8f178dcfb35ef7c77748650d7b1639))



##### Documentation

  * Add Hierarchical Namespace Bucket and Folders samples ([#2583](https://github.com/googleapis/java-storage/issues/2583)) ([3030081](https://github.com/googleapis/java-storage/commit/30300815f2faeef5780877dd74e2f8381b4a8caa)), closes [#2569](https://github.com/googleapis/java-storage/issues/2569)
  * Remove allowlist note from Folders RPCs ([#2593](https://github.com/googleapis/java-storage/issues/2593)) ([82161de](https://github.com/googleapis/java-storage/commit/82161dedfb1962f39f5186ac6d8443046d6b1e88))
  * Update DeleteObject Sample to be clearer on object versioning behavior ([#2595](https://github.com/googleapis/java-storage/issues/2595)) ([79b7cf0](https://github.com/googleapis/java-storage/commit/79b7cf05326ea135c552cbeee1b97e7ff115189f))



## June 28, 2024

Feature

You can now specify the Frankfurt, Germany (`europe-west3`) and Paris, France (`europe-west9`) regions when using [regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints).

## June 18, 2024

Feature

Hierarchical namespace for Cloud Storage buckets is now available in [Preview](https://developers.google.com/maps/launch-stages#preview). With hierarchical namespace, you can store your data in a logical file system structure.

Issue

[Renaming a folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders) in a bucket with hierarchical namespace enabled using command line is not supported.

## June 17, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.42.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.41.0...storage/v1.42.0) (2024-06-10)

##### Features

  * **storage:** Add new package transfermanager. This package is intended for parallel uploads and downloads, and is in preview. It is not stable, and is likely to change. ([#10045](https://github.com/googleapis/google-cloud-go/issues/10045)) ([cde5cbb](https://github.com/googleapis/google-cloud-go/commit/cde5cbba3145d5a702683656a42158621234fe71))
  * **storage:** Add bucket HierarchicalNamespace ([#10315](https://github.com/googleapis/google-cloud-go/issues/10315)) ([b92406c](https://github.com/googleapis/google-cloud-go/commit/b92406ccfadfdcee379e86d6f78c901d772401a9)), refs [#10146](https://github.com/googleapis/google-cloud-go/issues/10146)
  * **storage:** Add BucketName to BucketHandle ([#10127](https://github.com/googleapis/google-cloud-go/issues/10127)) ([203cc59](https://github.com/googleapis/google-cloud-go/commit/203cc599e5e2f2f821dc75b47c5a4c9073333f05))



##### Bug Fixes

  * **storage:** Set invocation headers on xml reads ([#10250](https://github.com/googleapis/google-cloud-go/issues/10250)) ([c87e1ab](https://github.com/googleapis/google-cloud-go/commit/c87e1ab6f9618b8b3f4d0005ac159abd87b0daaf))



##### Documentation

  * **storage:** Update autoclass doc ([#10135](https://github.com/googleapis/google-cloud-go/issues/10135)) ([e4b2737](https://github.com/googleapis/google-cloud-go/commit/e4b2737ddc16d3bf8139a6def7326ac905f62acd))



### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [2.17.0](https://github.com/googleapis/python-storage/compare/v2.16.0...v2.17.0) (2024-05-22)

##### Features

  * Support HNS enablement in bucket metadata ([#1278](https://github.com/googleapis/python-storage/issues/1278)) ([add3c01](https://github.com/googleapis/python-storage/commit/add3c01f0974e22df7f0b50504d5e83e4235fd81))
  * Support page_size in bucket.list_blobs ([#1275](https://github.com/googleapis/python-storage/issues/1275)) ([c52e882](https://github.com/googleapis/python-storage/commit/c52e882f65583a7739392926308cc34984561165))



##### Bug Fixes

  * Remove deprecated methods in samples and tests ([#1274](https://github.com/googleapis/python-storage/issues/1274)) ([4db96c9](https://github.com/googleapis/python-storage/commit/4db96c960b07e503c1031c9fa879cf2af195f513))



##### Documentation

  * Reference Storage Control in readme ([#1254](https://github.com/googleapis/python-storage/issues/1254)) ([3d6d369](https://github.com/googleapis/python-storage/commit/3d6d3693d5c1b24cd3d2bbdeabfd78b8bfd4161a))
  * Update DEFAULT_RETRY_IF_GENERATION_SPECIFIED docstrings ([#1234](https://github.com/googleapis/python-storage/issues/1234)) ([bdd426a](https://github.com/googleapis/python-storage/commit/bdd426adf5901faa36115885af868ef50e356a36))



## June 10, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.11.2](https://github.com/googleapis/nodejs-storage/compare/v7.11.1...v7.11.2) (2024-06-07)

##### Bug Fixes

  * Support uint8array in file.save ([#2480](https://github.com/googleapis/nodejs-storage/issues/2480)) ([1477fe1](https://github.com/googleapis/nodejs-storage/commit/1477fe15e5b6dae7cdfb2a1d00121e5d674c8f7c))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.40.0](https://github.com/googleapis/java-storage/compare/v2.39.0...v2.40.0) (2024-06-06)

##### Features

  * Promote google-cloud-storage-control to GA ([#2575](https://github.com/googleapis/java-storage/issues/2575)) ([129f188](https://github.com/googleapis/java-storage/commit/129f188a9877b3bd71db3b00ba3d8d6e4095fb67))



##### Bug Fixes

  * Reduce Java 21 Virtual Thread Pinning in IO operations ([#2553](https://github.com/googleapis/java-storage/issues/2553)) ([498fd0b](https://github.com/googleapis/java-storage/commit/498fd0b391c9d1d01c453fe31abea7890c0b498f))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.31.0 ([#2571](https://github.com/googleapis/java-storage/issues/2571)) ([67ce3d6](https://github.com/googleapis/java-storage/commit/67ce3d6505e1e48f496ab52884f5f5c2852aa445))
  * Update dependency net.jqwik:jqwik to v1.8.5 ([#2563](https://github.com/googleapis/java-storage/issues/2563)) ([88f7d86](https://github.com/googleapis/java-storage/commit/88f7d86d960aa6986cf41165d80d03a551502ec2))



##### Documentation

  * Managed Folders samples ([#2562](https://github.com/googleapis/java-storage/issues/2562)) ([5ffc1f2](https://github.com/googleapis/java-storage/commit/5ffc1f2fa75ac2e1c0022301e02b6ea6627faf03))
  * Update javadoc for createFrom ([#2522](https://github.com/googleapis/java-storage/issues/2522)) ([dc31e95](https://github.com/googleapis/java-storage/commit/dc31e95158e66d0eb4c85122edd29431a610a204))



## June 06, 2024

Feature

Cloud Storage now offers a new pre-defined dual region, `EUROPE-WEST2` (London) and `EUROPE-WEST1` (Belgium). To learn more about Cloud Storage pre-defined dual regions, see the [Bucket locations page](https://docs.cloud.google.com/storage/docs/locations#predefined).

## May 27, 2024

Feature

Cloud Storage FUSE now offers the following features: 

  * You now have the option to disable authentication on custom endpoints using the `--anonymous-access` flag. For more information about the new global option, see the [Cloud Storage FUSE CLI options page](https://docs.cloud.google.com/storage/docs/gcsfuse-cli).
  * Cloud Storage FUSE now supports Rocky Linux versions 8.9 or later. For more information, see [Cloud Storage FUSE instructions on how to configure the package manager](https://docs.cloud.google.com/storage/docs/gcsfuse-install#configure-package-manager).
  * The Cloud Storage FUSE `max-conns-per-host` flag has been updated to offer a default value which specifies no limit on TCP connections except for limitations set by your machine's specifications. For more information, see the [Cloud Storage FUSE CLI page](https://docs.cloud.google.com/storage/docs/gcsfuse-cli).



Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.11.1](https://github.com/googleapis/nodejs-storage/compare/v7.11.0...v7.11.1) (2024-05-21)

##### Bug Fixes

  * Add missing projectIdentifier to GetServiceAccountOptions ([#2468](https://github.com/googleapis/nodejs-storage/issues/2468)) ([d49e9d2](https://github.com/googleapis/nodejs-storage/commit/d49e9d2cbab42eb2390eeeccc562e3283df6384c))
  * Allow files in directories to be downloaded onto local machine ([#2199](https://github.com/googleapis/nodejs-storage/issues/2199)) ([9f62429](https://github.com/googleapis/nodejs-storage/commit/9f62429dad234167dc6f0969b40c7942bab83aee))
  * Do not set `customEndpoint` if `apiEndpoint === default` ([#2460](https://github.com/googleapis/nodejs-storage/issues/2460)) ([b4dbd73](https://github.com/googleapis/nodejs-storage/commit/b4dbd73189b9fae4c23d614753670ee562bc717b))
  * Improve GetFilesResponse interface ([#2466](https://github.com/googleapis/nodejs-storage/issues/2466)) ([918db28](https://github.com/googleapis/nodejs-storage/commit/918db2818395488ff925324a9962879bb56368d7))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.39.0](https://github.com/googleapis/java-storage/compare/v2.38.0...v2.39.0) (2024-05-22)

##### Features

  * Plumb PartNamingStrategy for Parallel Composite Uploads in Transfer Manager ([#2547](https://github.com/googleapis/java-storage/issues/2547)) ([79d721d](https://github.com/googleapis/java-storage/commit/79d721dc44d1c5f4b2df3697f62b958a3b9b999c))



##### Bug Fixes

  * Update GapicUnbufferedChunkedResumableWritableByteChannel to be tolerant of non-quantum writes ([#2537](https://github.com/googleapis/java-storage/issues/2537)) ([1701fde](https://github.com/googleapis/java-storage/commit/1701fde04a80aa8ce97c5e762158406024456782))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.30.1 ([#2550](https://github.com/googleapis/java-storage/issues/2550)) ([e9807ec](https://github.com/googleapis/java-storage/commit/e9807ecda46615c8d1108bcea7a25ecba8154b6c))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.2 ([#2552](https://github.com/googleapis/java-storage/issues/2552)) ([a207829](https://github.com/googleapis/java-storage/commit/a207829040c176909141de100e4273f5aa32e78f))



## May 20, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.41.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.40.0...storage/v1.41.0) (2024-05-13)

##### Features

  * **storage/control:** Make Managed Folders operations public ([264a6dc](https://github.com/googleapis/google-cloud-go/commit/264a6dcddbffaec987dce1dc00f6550c263d2df7))
  * **storage:** Support for soft delete policies and restore ([#9520](https://github.com/googleapis/google-cloud-go/issues/9520)) ([985deb2](https://github.com/googleapis/google-cloud-go/commit/985deb2bdd1c79944cdd960bd3fbfa38cbfa1c91))



##### Bug Fixes

  * **storage/control:** An existing resource pattern value `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder=**}` to resource definition `storage.googleapis.com/ManagedFolder` is removed ([3e25053](https://github.com/googleapis/google-cloud-go/commit/3e250530567ee81ed4f51a3856c5940dbec35289))
  * **storage:** Add internaloption.WithDefaultEndpointTemplate ([3b41408](https://github.com/googleapis/google-cloud-go/commit/3b414084450a5764a0248756e95e13383a645f90))
  * **storage:** Bump x/net to v0.24.0 ([ba31ed5](https://github.com/googleapis/google-cloud-go/commit/ba31ed5fda2c9664f2e1cf972469295e63deb5b4))
  * **storage:** Disable gax retries for gRPC ([#9747](https://github.com/googleapis/google-cloud-go/issues/9747)) ([bbfc0ac](https://github.com/googleapis/google-cloud-go/commit/bbfc0acc272f21bf1f558ea23648183d5a11cda5))
  * **storage:** More strongly match regex ([#9706](https://github.com/googleapis/google-cloud-go/issues/9706)) ([3cfc8eb](https://github.com/googleapis/google-cloud-go/commit/3cfc8eb418e064d734bf3d8708162062dbbe988f)), refs [#9705](https://github.com/googleapis/google-cloud-go/issues/9705)
  * **storage:** Retry net.OpError on connection reset ([#10154](https://github.com/googleapis/google-cloud-go/issues/10154)) ([54fab10](https://github.com/googleapis/google-cloud-go/commit/54fab107f98b4f79c9df2959a05b981be0a613c1)), refs [#9478](https://github.com/googleapis/google-cloud-go/issues/9478)
  * **storage:** Wrap error when MaxAttempts is hit ([#9767](https://github.com/googleapis/google-cloud-go/issues/9767)) ([9cb262b](https://github.com/googleapis/google-cloud-go/commit/9cb262bb65a162665bfb8bed0022615131bae1f2)), refs [#9720](https://github.com/googleapis/google-cloud-go/issues/9720)



##### Documentation

  * **storage/control:** Update storage control documentation and add PHP for publishing ([1d757c6](https://github.com/googleapis/google-cloud-go/commit/1d757c66478963d6cbbef13fee939632c742759c))



## May 13, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.11.0](https://github.com/googleapis/nodejs-storage/compare/v7.10.2...v7.11.0) (2024-05-03)

##### Features

  * Add ability to enable hierarchical namespace on buckets ([#2453](https://github.com/googleapis/nodejs-storage/issues/2453)) ([4e5726f](https://github.com/googleapis/nodejs-storage/commit/4e5726fe60ecede6bec6508e4b4ec214f2e173dd))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.38.0](https://github.com/googleapis/java-storage/compare/v2.37.0...v2.38.0) (2024-05-09)

##### Features

  * Promoted google-cloud-storage-control to beta ([#2531](https://github.com/googleapis/java-storage/issues/2531)) ([09f7191](https://github.com/googleapis/java-storage/commit/09f719194fd9296ecb21758096b8e65eb208dfc2))



##### Bug Fixes

  * Add strict client side response validation for gRPC chunked resumable uploads ([#2527](https://github.com/googleapis/java-storage/issues/2527)) ([c1d1f4a](https://github.com/googleapis/java-storage/commit/c1d1f4a5c88d27296f69df0a832659e2b1eb9ca0))
  * An existing resource pattern value `projects/{project}/buckets/{bucket}/managedFolders/{managedFolder=**}` to resource definition `storage.googleapis.com/ManagedFolder` is removed ([#2524](https://github.com/googleapis/java-storage/issues/2524)) ([7d7f526](https://github.com/googleapis/java-storage/commit/7d7f5263f7e7f5357c5970c68c4d6ff117fc9e93))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.39.0 ([#2501](https://github.com/googleapis/java-storage/issues/2501)) ([518d4be](https://github.com/googleapis/java-storage/commit/518d4beefdc3738fd19168baccd4016dd002d4fa))
  * ParallelCompositeUpload in Transfer Manager hangs when encountering OOM ([#2526](https://github.com/googleapis/java-storage/issues/2526)) ([67a7c6b](https://github.com/googleapis/java-storage/commit/67a7c6b6582b5afab9272b32e01897d009e7c0bf))
  * Update grpc WriteObject response handling to provide context when a failure happens ([#2532](https://github.com/googleapis/java-storage/issues/2532)) ([170a3f5](https://github.com/googleapis/java-storage/commit/170a3f54c8ccb6af108c35992e652c07ebb1109c))
  * Update GzipReadableByteChannel to be tolerant of one byte reads ([#2512](https://github.com/googleapis/java-storage/issues/2512)) ([87b63f4](https://github.com/googleapis/java-storage/commit/87b63f4995f7b9654f40a9585996ec4a73235858))
  * Update StorageOptions to carry forward fields that aren't part of ServiceOptions ([#2521](https://github.com/googleapis/java-storage/issues/2521)) ([b84654e](https://github.com/googleapis/java-storage/commit/b84654e79ee53087badc0315ea3fb2d1b0b9ca57))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.30.0 ([#2523](https://github.com/googleapis/java-storage/issues/2523)) ([3e573f7](https://github.com/googleapis/java-storage/commit/3e573f79b3935e423e200537549507ab1f252ada))
  * Update dependency info.picocli:picocli to v4.7.6 ([#2535](https://github.com/googleapis/java-storage/issues/2535)) ([f26888a](https://github.com/googleapis/java-storage/commit/f26888ab1467d6bbcad9bfced9360daa4abd2824))



##### Documentation

  * Add in Transfer Manager chunked upload/download samples ([#2518](https://github.com/googleapis/java-storage/issues/2518)) ([d1f6bcc](https://github.com/googleapis/java-storage/commit/d1f6bccc2c9b5da5c4ff196711c5cd410649d60f))
  * Update readme to include gradle instructions for storage control ([#2503](https://github.com/googleapis/java-storage/issues/2503)) ([50ac93b](https://github.com/googleapis/java-storage/commit/50ac93b6b61806911737e389253739436dfb515c))
  * Update TransportCompatibility annotation for Storage#blobWriteSession ([#2520](https://github.com/googleapis/java-storage/issues/2520)) ([b7d673c](https://github.com/googleapis/java-storage/commit/b7d673cbac52407d470eace9d08e1cea2584da30))



## April 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.10.2](https://github.com/googleapis/nodejs-storage/compare/v7.10.1...v7.10.2) (2024-04-26)

##### Bug Fixes

  * Use correct indices for file.from and fix tests to verify names ([#2449](https://github.com/googleapis/nodejs-storage/issues/2449)) ([d4240fa](https://github.com/googleapis/nodejs-storage/commit/d4240fa5c8c0353de81cc8c052eea2915c3e383c))



#### [7.10.1](https://github.com/googleapis/nodejs-storage/compare/v7.10.0...v7.10.1) (2024-04-22)

##### Bug Fixes

  * Change copyoptions type ([#2439](https://github.com/googleapis/nodejs-storage/issues/2439)) ([2ebd7ac](https://github.com/googleapis/nodejs-storage/commit/2ebd7aca6c474147e5a1d1fb2a96b7d052a08a21))
  * Expand types of custom metadata within FileMetadata ([#2442](https://github.com/googleapis/nodejs-storage/issues/2442)) ([1d434a9](https://github.com/googleapis/nodejs-storage/commit/1d434a905392b00bb48ebbb812034e062ed27dd2))



## April 23, 2024

Change

[Default replication](https://docs.cloud.google.com/storage/docs/availability-durability) monitoring for multi-region and dual-region buckets in the Google Cloud console is now available for the following graphs:

  * Percent of minutes out of RPO
  * Percent of objects out of target
  * Meeting RPO



## April 22, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.10.0](https://github.com/googleapis/nodejs-storage/compare/v7.9.0...v7.10.0) (2024-04-15)

##### Features

  * Add ability to create a File object from URL ([#2432](https://github.com/googleapis/nodejs-storage/issues/2432)) ([1b71fcc](https://github.com/googleapis/nodejs-storage/commit/1b71fcc7687fb8d66e04fb92b15671729f1407e7))
  * Allow setting contentEncoding during compose ([#2431](https://github.com/googleapis/nodejs-storage/issues/2431)) ([6e81e05](https://github.com/googleapis/nodejs-storage/commit/6e81e05b2615f1b8307fcca9a147362677e95e7f))



##### Bug Fixes

  * Destroy pipeline streams when returned stream errors ([#2437](https://github.com/googleapis/nodejs-storage/issues/2437)) ([fe1ac65](https://github.com/googleapis/nodejs-storage/commit/fe1ac655a8d321e225f4828c7adf57342c4a8455))
  * Remove extraneous mime-types package in favor of mime ([#2435](https://github.com/googleapis/nodejs-storage/issues/2435)) ([63a71f2](https://github.com/googleapis/nodejs-storage/commit/63a71f2e81181ad976e982ef79d6148913a87c1f))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.37.0](https://github.com/googleapis/java-storage/compare/v2.36.1...v2.37.0) (2024-04-19)

##### Features

  * Adds a ZeroCopy response marshaller for grpc ReadObject handling ([#2489](https://github.com/googleapis/java-storage/issues/2489)) ([8c7404d](https://github.com/googleapis/java-storage/commit/8c7404dea8ef16a7b61accad4fe614e033a5ad2c))
  * Port BufferToDiskThenUpload to work with HttpStorageOptions ([#2473](https://github.com/googleapis/java-storage/issues/2473)) ([d84e255](https://github.com/googleapis/java-storage/commit/d84e25559afecc27026c7f4fe7aeaf0d0ce705b4))
  * Port DefaultBlobWriteSessionConfig to work with HttpStorageOptions ([#2472](https://github.com/googleapis/java-storage/issues/2472)) ([e5772a4](https://github.com/googleapis/java-storage/commit/e5772a4f4ec5d747fcd403477a35ceeb94492280))
  * Port ParallelCompositeUploadBlobWriteSessionConfig to work with HttpStorageOptions ([#2474](https://github.com/googleapis/java-storage/issues/2474)) ([3bf6026](https://github.com/googleapis/java-storage/commit/3bf60264f47aad8101bb4b4cff9cc0449cf1c4f3))
  * Transfer Manager ParallelCompositeUploads ([#2494](https://github.com/googleapis/java-storage/issues/2494)) ([8b54549](https://github.com/googleapis/java-storage/commit/8b5454910c74563c9598f9d5cc23fa509ec749d9))



##### Bug Fixes

  * Ensure all BlobWriteSession types conform to the semantics specified in BlobWriteSession ([#2482](https://github.com/googleapis/java-storage/issues/2482)) ([d47afcf](https://github.com/googleapis/java-storage/commit/d47afcfe2bcb2e7e266a5197456b6f9661e91004))
  * Fix BidiBlobWriteSessionConfigs to respect preconditions ([#2481](https://github.com/googleapis/java-storage/issues/2481)) ([955d78a](https://github.com/googleapis/java-storage/commit/955d78af0fecd4b65506df4bfd44fc683e23c2ec))
  * Update ApiaryUnbufferedWritableByteChannel to be graceful of non-quantum aligned write calls ([#2493](https://github.com/googleapis/java-storage/issues/2493)) ([f548335](https://github.com/googleapis/java-storage/commit/f5483356a3ba6327a712ef2f5534b61a649174df))
  * Update BidiBlobWriteSessionConfig to respect a provided bufferSize ([#2471](https://github.com/googleapis/java-storage/issues/2471)) ([e1fb857](https://github.com/googleapis/java-storage/commit/e1fb8577e6b7a36981fb78937fe8c5dd606a4c2a))
  * Update grpc handling of IAM Policy etag to account for base64 encoding ([#2499](https://github.com/googleapis/java-storage/issues/2499)) ([032f2f2](https://github.com/googleapis/java-storage/commit/032f2f2693c6c75cc4ae0339be805c0bb94fa064))
  * Update Grpc Retry Conformance after new additions to testbench ([#2309](https://github.com/googleapis/java-storage/issues/2309)) ([09043c5](https://github.com/googleapis/java-storage/commit/09043c5587ae9e6adeb425f5c2f7c4f65ec5e20e))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240319-2.0.0 ([#2460](https://github.com/googleapis/java-storage/issues/2460)) ([9c2ee90](https://github.com/googleapis/java-storage/commit/9c2ee909d02fef5afc201589f5ced4062e2f14e8))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#2467](https://github.com/googleapis/java-storage/issues/2467)) ([c12f329](https://github.com/googleapis/java-storage/commit/c12f3290a029c25cdac458cda44835c0a43c33e7))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.29.0 ([#2502](https://github.com/googleapis/java-storage/issues/2502)) ([7ed8446](https://github.com/googleapis/java-storage/commit/7ed8446dcbff165408331df97e2d15a1cd70b7be))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.43.0 ([#2459](https://github.com/googleapis/java-storage/issues/2459)) ([2dc4748](https://github.com/googleapis/java-storage/commit/2dc4748353be4fe06ec7df2e413ed5752d350f8b))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.44.0 ([#2497](https://github.com/googleapis/java-storage/issues/2497)) ([9b0253c](https://github.com/googleapis/java-storage/commit/9b0253ca1a03d6a90a1008794b00c6825d26ff0c))



##### Documentation

  * Add summary and reference docs for Storage Control API to readme ([#2485](https://github.com/googleapis/java-storage/issues/2485)) ([70fd088](https://github.com/googleapis/java-storage/commit/70fd088975280ed9a650ca09825ccb28297d89f7))
  * Create Samples for transfer manager ([#2492](https://github.com/googleapis/java-storage/issues/2492)) ([e2030b2](https://github.com/googleapis/java-storage/commit/e2030b281d45b69840962e0a80c4b6b85e300b20))



## April 05, 2024

Feature

[Custom constraints](https://docs.cloud.google.com/storage/docs/custom-constraints) for Cloud Storage are now available. You can use custom constraints to enforce policies on Cloud Storage resources, such as a policy that enforces all buckets to have Object Versioning enabled.

## April 03, 2024

Feature

Managed folders are now available in the Google Cloud Console.

You can now use managed folders in your Cloud Storage buckets using the Cloud Console. You can create, list, move, and delete your managed folders in the Console, as well as set IAM policies. To learn more, see [Create and manage managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders).

## April 01, 2024

Feature

Google Cloud Storage now offers Dual-region Google Egress Bandwidth quotas per dual-region location. See [Bandwidth usage in Cloud Storage](https://docs.cloud.google.com/storage/docs/bandwidth-usage).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.40.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.39.1...storage/v1.40.0) (2024-03-29)

##### Features

  * **storage:** Implement io.WriterTo in Reader ([#9659](https://github.com/googleapis/google-cloud-go/issues/9659)) ([8264a96](https://github.com/googleapis/google-cloud-go/commit/8264a962d1c21d52e8fca50af064c5535c3708d3))
  * **storage:** New storage control client ([#9631](https://github.com/googleapis/google-cloud-go/issues/9631)) ([1f4d279](https://github.com/googleapis/google-cloud-go/commit/1f4d27957743878976d6b4549cc02a5bb894d330))



##### Bug Fixes

  * **storage:** Retry errors from last recv on uploads ([#9616](https://github.com/googleapis/google-cloud-go/issues/9616)) ([b6574aa](https://github.com/googleapis/google-cloud-go/commit/b6574aa42ebad0532c2749b6ece879b932f95cb9))
  * **storage:** Update protobuf dep to v1.33.0 ([30b038d](https://github.com/googleapis/google-cloud-go/commit/30b038d8cac0b8cd5dd4761c87f3f298760dd33a))



##### Performance Improvements

  * **storage:** Remove protobuf's copy of data on unmarshalling ([#9526](https://github.com/googleapis/google-cloud-go/issues/9526)) ([81281c0](https://github.com/googleapis/google-cloud-go/commit/81281c04e503fd83301baf88cc352c77f5d476ca))



## March 29, 2024

Feature

The Storage Control API is now available for use. The Storage Control API lets you perform metadata-specific, control plane, and long-running operations. To learn more about the Storage Control API and operations you can perform, see [Storage Control API overview](https://docs.cloud.google.com/storage/docs/reference/rpc).

## March 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.9.0](https://github.com/googleapis/nodejs-storage/compare/v7.8.0...v7.9.0) (2024-03-18)

##### Features

  * Add ability to configure and utilize soft-delete and restore ([#2425](https://github.com/googleapis/nodejs-storage/issues/2425)) ([7da5a7d](https://github.com/googleapis/nodejs-storage/commit/7da5a7da86ad649a8132e3183f4b3e3f9bb2eace))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.36.1](https://github.com/googleapis/java-storage/compare/v2.36.0...v2.36.1) (2024-03-20)

##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240311-2.0.0 ([#2446](https://github.com/googleapis/java-storage/issues/2446)) ([27b4780](https://github.com/googleapis/java-storage/commit/27b4780ff64ce068555887c1cc4f88489dde0a83))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#2450](https://github.com/googleapis/java-storage/issues/2450)) ([bf35a9a](https://github.com/googleapis/java-storage/commit/bf35a9a041f012b56e4a858d48b018f1270f319d))



### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [2.16.0](https://github.com/googleapis/python-storage/compare/v2.15.0...v2.16.0) (2024-03-18)

##### Features

  * Add support for soft delete ([#1229](https://github.com/googleapis/python-storage/issues/1229)) ([3928aa0](https://github.com/googleapis/python-storage/commit/3928aa0680ec03addae1f792c73abb5c9dc8586f))
  * Support includeFoldersAsPrefixes ([#1223](https://github.com/googleapis/python-storage/issues/1223)) ([7bb8065](https://github.com/googleapis/python-storage/commit/7bb806538cf3d7a5e16390db1983620933d5e51a))



## March 18, 2024

Feature

You can now use the GCS FUSE file cache feature, a client-based read cache that lets repeat file reads to be served from a faster cache storage of your choice. To learn more about caching, see [GCS FUSE caching documentation](https://docs.cloud.google.com/storage/docs/gcsfuse-cache).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.39.1](https://github.com/googleapis/google-cloud-go/compare/storage/v1.39.0...storage/v1.39.1) (2024-03-11)

##### Bug Fixes

  * **storage:** Add object validation case and test ([#9521](https://github.com/googleapis/google-cloud-go/issues/9521)) ([386bef3](https://github.com/googleapis/google-cloud-go/commit/386bef319b4678beaa926ddfe4edef190f11b68d))



### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.36.0](https://github.com/googleapis/java-storage/compare/v2.35.0...v2.36.0) (2024-03-15)

##### Features

  * Add Custom Part Metadata Decorator to ParallelCompositeUploadConfig ([#2434](https://github.com/googleapis/java-storage/issues/2434)) ([43b8006](https://github.com/googleapis/java-storage/commit/43b800645ba3622e5de635825e1d082c6d26c2eb))
  * Add hierarchical namespace and folders features ([#2445](https://github.com/googleapis/java-storage/issues/2445)) ([8074fff](https://github.com/googleapis/java-storage/commit/8074fffed5208a8578e5afe694fdd3d8df627b8c))
  * Add soft delete feature ([#2403](https://github.com/googleapis/java-storage/issues/2403)) ([989f36f](https://github.com/googleapis/java-storage/commit/989f36fbb206832a6a3584c77546d3d560ac0df8))



##### Bug Fixes

  * Fix name digest for noprefix ([#2448](https://github.com/googleapis/java-storage/issues/2448)) ([12c9db8](https://github.com/googleapis/java-storage/commit/12c9db8935f25a5f9e4633af85ea96acaa914d23))
  * Missing serialVersionUID of serializable classes ([#2344](https://github.com/googleapis/java-storage/issues/2344)) ([736865b](https://github.com/googleapis/java-storage/commit/736865b4b97aa3940e1eab6a582d0ef38db31bba))



##### Dependencies

  * Update dependency com.google.apis:google-api-services-storage to v1-rev20240307-2.0.0 ([#2442](https://github.com/googleapis/java-storage/issues/2442)) ([1352203](https://github.com/googleapis/java-storage/commit/1352203859c3798423ef78823ed10577b93eebef))
  * Update dependency net.jqwik:jqwik to v1.8.4 ([#2447](https://github.com/googleapis/java-storage/issues/2447)) ([110b80c](https://github.com/googleapis/java-storage/commit/110b80cdde24da4868e46c3909020db7b02d5491))
  * Update gcr.io/cloud-devrel-public-resources/storage-testbench docker tag to v0.42.0 ([#2441](https://github.com/googleapis/java-storage/issues/2441)) ([80745d4](https://github.com/googleapis/java-storage/commit/80745d415810353b3466a3eda12f6ca50a2c71b0))



## March 12, 2024

Feature

You can now view granular bucket-level cost data in the [Cloud Billing Detailed data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## January 31, 2024

Feature

Cloud Storage is now available in Johannesburg, South Africa (`africa-south1` region).

## January 22, 2024

Change

You can now work with the [Object Retention Lock feature](https://docs.cloud.google.com/storage/docs/object-lock) within the Cloud Console.

## January 15, 2024

Change

Newly created organizations now have the [`uniformBucketLevelAccess` constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access) enabled by default.

  * This lets you build your organization resources in a secure posture from Day 0.
  * You can opt out of this constraint. To opt out, contact your organization administrator.



## December 07, 2023

Feature

Cloud Storage FUSE now provides the ability to configure [log rotation](https://docs.cloud.google.com/storage/docs/gcsfuse-config-file).

## December 04, 2023

Feature

The [restrict unencrypted HTTP requests](https://docs.cloud.google.com/storage/docs/org-policy-constraints#block-unencrypted-http) organization policy constraint is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This constraint blocks all unencrypted HTTP access to Cloud Storage resources.

## November 21, 2023

Feature

The [Object Retention Lock feature](https://docs.cloud.google.com/storage/docs/object-lock) is now available.

  * Using this feature, you can [place a retention configuration on individual objects](https://docs.cloud.google.com/storage/docs/using-object-lock#set-object-config).

  * A retention configuration defines a date prior to which the object cannot be deleted or overwritten.

  * A retention configuration can optionally be locked to prevent the retention date from being shortened or removed.




## November 20, 2023

Feature

[Regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints) are now available in Preview. Regional endpoints let you run your workloads in a manner that complies with data residency and data sovereignty requirements, where your request traffic is routed directly to the region specified in the endpoint.

## November 14, 2023

Change

New [bandwidth quotas](https://docs.cloud.google.com/storage/quotas#bandwidth) are now in effect.

  * Bandwidth quotas are now variable and based in part on a project's billing account history. Previously, the same default value applied to all projects.
  * For most projects, egress bandwidth quotas either remain unchanged or have increased.
  * You can [view your project's egress bandwidth quotas in the Console](https://console.cloud.google.com/apis/api/storage.googleapis.com/quotas).



## November 03, 2023

Change

The [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) can now be enabled for existing buckets.

  * Previously, Autoclass could only be enabled when creating a new bucket.
  * Enabling Autoclass on an existing bucket incurs [additional charges](https://cloud.google.com/storage/pricing#autoclass-pricing).



## October 27, 2023

Change

[Turbo replication performance monitoring](https://docs.cloud.google.com/storage/docs/monitoring#per-bucket) in the Google Cloud console has been moved and expanded.

  * Monitoring graphs have been moved from a bucket's Configuration tab to its Observability tab.

  * A new, real-time _Maximum delay in turbo replication_ graph is also available in the Observability tab.




## October 26, 2023

Feature

[Managed folders](https://docs.cloud.google.com/storage/docs/folders#managed-folders-overview) are now available in Preview. When using managed folders, you can organize your objects by group and set IAM policies that offer more granular access control over data segments within a bucket.

## October 16, 2023

Change

Changes to the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) that were [announced on July 17, 2023](https://docs.cloud.google.com/storage/docs/release-notes#July_17_2023) begin taking effect today.

## October 12, 2023

Feature

The Node.js and Python client libraries now have parallelized upload and download options, improving their performance.

  * Both client libraries have improved [bulk uploads](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object), [bulk downloads](https://docs.cloud.google.com/storage/docs/downloading-objects#downloading-an-object), [large object uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads#behavior), and [large object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads#behavior).



## September 28, 2023

Announcement

Beginning Oct 30, 2023, Cloud Storage will change how it enforces egress bandwidth quotas.

  * Instead of using the same default value for all projects, egress bandwidth quotas will depend on each project's history, such whether the billing account is in good standing.
  * For most projects, egress bandwidth quotas will either remain unchanged or will increase.
  * Once this change takes effect, you can [view your project's egress bandwidth quotas in the Console](https://console.cloud.google.com/apis/api/storage.googleapis.com/quotas).



## September 26, 2023

Feature

You can now control the mounting behavior of Cloud Storage FUSE by using a [configuration file](https://docs.cloud.google.com/storage/docs/gcsfuse-cli#config-file) instead of global options.

Change

Cloud Storage FUSE is now available for use on ARM64-based machines.

## September 20, 2023

Change

The gcloud CLI now supports setting a [user-defined prefix](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations#parallel_composite_upload_component_prefix) for naming temporary components of a [parallel composite upload](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

## September 19, 2023

Feature

Cloud Storage is now available in Dammam, Saudi Arabia (`me-central2` region).

## September 15, 2023

Feature

[Manifest files](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#shards) are now available in Storage Insights. A manifest file is generated when an inventory report is split into shards. You can use the manifest file to easily locate the shards you want to download.

## September 14, 2023

Change

The following [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) pairs are now generally available:

  * Montréal and Toronto, Canada
  * Sydney and Melbourne, Australia



## August 23, 2023

Feature

The Storage Object User role (`roles/storage.objectUser`) is now available. This role allows you to create, view, list, update, and delete objects and their metadata, without granting access to the object's ACLs.

## August 22, 2023

Feature

Cloud Storage is now available in Berlin, Germany (`europe-west10` region).

## August 01, 2023

Feature

You can now use [locational endpoints](https://docs.cloud.google.com/storage/docs/locational-endpoints) to perform operations in a manner that's compliant with International Traffic in Arms Regulations (ITAR).

## July 18, 2023

Breaking

The `gcloud storage` command-line tool has changed some of the metadata it returns for buckets and objects, as well as changed the format of some metadata names it returns.

  * To output metadata in the form used prior to July 18, 2023, include the flag `--raw` in your `list` and `describe` commands for objects and buckets.



Announcement

[gcloud storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage) GA release 1.3 is now available.

  * The 1.3 release adds support for the [`rsync` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync), which synchronizes content between a source and destination.
  * The 1.3 release also adds support for [generating signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers), [managing HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys), [calculating bucket sizes](https://docs.cloud.google.com/storage/docs/getting-bucket-size) and [calculating hashes](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hash).



## July 17, 2023

Announcement

Beginning October 16, 2023, the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) will change its storage class transition behavior.

  * By default, new buckets with Autoclass enabled will only transition objects between the Standard and Nearline storage classes.

  * However, you can continue to create buckets that transition objects between all storage classes by choosing to opt-in.




Announcement

Beginning October 16, 2023, the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) and the [`matchesStorageClass` condition](https://docs.cloud.google.com/storage/docs/lifecycle#matchesstorageclass) for [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) will be incompatible.

  * You will not be able to modify any other bucket metadata for affected buckets until either the `matchesStorageClass` condition is removed or the Autoclass feature is disabled.



Announcement

Beginning October 16, 2023, the following pricing changes apply to buckets that use the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass):

  * Each storage class transition from Coldline or Archive storage to Standard storage will change from being free to being charged as a Class A operation at the Standard storage rate.

  * Each Class B operation, such as reading object data, will change from being charged at the rate of the object's storage class at the time of the operation to being charged at the Standard storage rate.

  * After October 30, 2023, billing for objects in Autoclass buckets will use Autoclass-specific SKUs.




## July 07, 2023

Feature

[Custom audit logging](https://docs.cloud.google.com/storage/docs/audit-logging#add-custom-metadata) for Cloud Storage is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). In addition to using the Cloud Storage JSON API, you can now attach custom information to audit logs for requests by using the following tools:

  * The gcloud or gsutil command-line tools
  * The Cloud Storage client libraries
  * The Cloud Storage XML API
  * Signed URLs



## June 28, 2023

Change

You can now have a maximum of 10 [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) per service account.

## June 26, 2023

Feature

[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## June 23, 2023

Change

Objects created using [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) can now be copied and rewritten normally.

  * Previously, you had to perform an [object composition](https://docs.cloud.google.com/storage/docs/composing-objects) on such objects before the output could be copied or rewritten.



## May 26, 2023

Change

You can now add [custom object metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata) in the final request of a JSON API [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads) by using the [`X-Goog-Meta-` header](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#xgoogmeta).

## May 11, 2023

Feature

[Custom audit logging](https://docs.cloud.google.com/storage/docs/audit-logging#add-custom-metadata) for Cloud Storage is now available in Preview.

  * JSON API requests now support user-defined headers that are prefixed with `x-goog-custom-audit-`.
  * Cloud Audit Logs can subsequently include these headers as part of your request's audit log entry.



## April 17, 2023

Feature

The [Storage Insights inventory reports feature](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) is now generally available. Inventory reports provide an overview of metadata for all objects in a bucket.

Announcement

On July 17, 2023, the `gcloud storage` command-line tool will change some of the metadata it returns for buckets and objects, as well as change the format of some metadata names it returns.

  * To continue outputting metadata in its current form, you should include the flag `--raw` in your `list` and `describe` commands for objects and buckets.



## April 05, 2023

Feature

[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) is now available in Preview. You can use Cloud Storage FUSE to mount and access storage buckets as local file systems.

  * Get started with [mounting buckets using Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/quickstart-mount-bucket).
  * Learn about [integrations between Cloud Storage FUSE and other Google Cloud products](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#integrations).



## April 01, 2023

Announcement

All [announced pricing changes for Cloud Storage](https://cloud.google.com/storage/pricing-announce) are now in effect.

## March 30, 2023

Feature

Cloud Storage is now available in Doha, Qatar (`me-central1` region).

## March 23, 2023

Feature

Cloud Storage is now available in Turin, Italy (`europe-west12` region).

Change

Objects smaller than 128KiB stored in buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) enabled are no longer managed by Autoclass.

  * Such objects are not subject to the Autoclass management fee and are statically set to Standard Storage.
  * Any such objects in Autoclass buckets that are currently stored in a different storage class are being transitioned to Standard Storage automatically and free of charge.



## March 20, 2023

Feature

The following US regions are now available for [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) storage:

  * Los Angeles (`us-west2`)
  * Salt Lake City (`us-west3`)



Feature

The following EU regions are now available for [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) storage:

  * Warsaw (`europe-central2`)
  * Madrid (`europe-southwest1`)
  * Frankfurt (`europe-west3`)
  * Milan (`europe-west8`)
  * Paris (`europe-west9`)



## March 17, 2023

Feature

Expanded [Cloud Storage monitoring dashboards](https://docs.cloud.google.com/storage/docs/monitoring) are now generally available (GA).

  * Available metrics include server and client error rates, write request counts, network ingress rates, and network egress rates.
  * Dashboards can be filtered by bucket location.
  * Dashboards are customizable, including the ability to [set up alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).



## March 07, 2023

Change

In buckets with [turbo replication](https://docs.cloud.google.com/storage/docs/turbo-replication) enabled, objects uploaded using [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) are now included in the turbo replication RPO.

## February 21, 2023

Change

You can now attach a maximum of 50 [tag bindings](https://docs.cloud.google.com/storage/docs/tags-and-labels) to a storage bucket.

## February 02, 2023

Announcement

The [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass) will stop managing Cloud Storage objects smaller than 128KiB after March 6, 2023.

  * Affected objects will be transitioned to the Standard storage class at no cost to customers and without requiring any action from customers.

  * Affected objects will always remain in Standard storage and will not be subject to the [Autoclass Management Fee](https://cloud.google.com/storage/pricing#autoclass-pricing).

  * The change is occurring because the Autoclass Management Fee typically outweighs storage fee savings for such small objects.




## January 31, 2023

Fixed

The issue for gsutil commands that use the `-m` global flag, which was documented on [January 19, 2023](https://docs.cloud.google.com/storage/docs/release-notes#January_19_2023), has been fixed in the most recent versions of the Cloud SDK and gsutil.

## January 19, 2023

Issue

Some gsutil commands that use the `-m` global flag, such as `cp` and `rsync`, are currently failing if the requester does not have the `storage.buckets.get` permission.

  * If you installed gsutil as part of the Cloud SDK, you can work around this issue by reverting to an earlier version. To do so, run the command `gcloud components update --version=413.0.0`

  * If you installed gsutil as a standalone tool, you can work around this issue by reverting to version 5.17




## January 18, 2023

Announcement

[gcloud storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage) GA release 1.2 is now available.

  * The 1.2 release adds support for managing access with [IAM](https://docs.cloud.google.com/storage/docs/access-control/iam) and [ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists) at the bucket and object level.
  * The 1.2 release also adds support for managing the [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) and [turbo replication](https://docs.cloud.google.com/storage/docs/turbo-replication) features.



## November 16, 2022

Change

[Turbo replication](https://docs.cloud.google.com/storage/docs/turbo-replication#availability) is now available for all [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) combinations.

Change

The following regions are now [generally available](https://cloud.google.com/products#product-launch-stages) for [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) storage:

  * Mumbai (`asia-south1`) 
  * Delhi (`asia-south2`)
  * Columbus (`us-east5`)
  * Dallas (`us-south1`)
  * Las Vegas (`us-west4`)



## November 10, 2022

Feature

You can now use the Google Cloud console to get [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets) and [policy insights](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets) for buckets. Role recommendations and policy insights help you understand and manage permission usage for your buckets.

## November 09, 2022

Feature

Expanded [Cloud Storage monitoring dashboards](https://console.cloud.google.com/storage/monitoring) are now available in Preview.

  * Available metrics include server and client error rates, write request counts, network ingress rates, and network egress rates.
  * Dashboards can be filtered by bucket location.
  * Dashboards are customizable, including the ability to [set up alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).



In addition to the project-wide dashboard, per-bucket dashboards are available in a new **Observability** tab in the Bucket Details for each bucket.

## November 08, 2022

Feature

The [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) feature is now available.

  * When enabled, Autoclass transitions the [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) of your objects automatically based on their access patterns.
  * Currently, Autoclass can only be enabled at the time of bucket creation.



Announcement

[gcloud storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage) GA release 1.1 is now available.

  * The 1.1 release adds more support for managing bucket settings, including lifecycle configurations, CORS configurations, and labels.



## October 27, 2022

Feature

[Bucket tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## October 21, 2022

Feature

New public dataset stored in Cloud Storage.

  * Data for [ERA5](https://docs.cloud.google.com/storage/docs/public-datasets/era5) are now hosted publicly in Cloud Storage.



## September 28, 2022

Change

New buckets created using the Cloud Console now have [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) enabled by default.

  * During the bucket creation process, you can choose to change this setting.



## September 13, 2022

Feature

Cloud Storage is now available in Tel Aviv, Israel (`me-west1` region).

Announcement

[`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) is now in GA

  * `gcloud storage` provides faster uploading and downloading performance when compared to the gsutil command line tool.



## August 24, 2022

Feature

The [restrict authentication types](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types) organization policy constraint is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). This constraint allows you to restrict the authentication types that can be used in requests for Cloud Storage resources.

## August 02, 2022

Feature

Customer-managed encryption key (CMEK) organization policy constraints are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

  * [`constraints/gcp.restrictNonCmekServices`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-noncmek-services) allows you to control which resources require the use of CMEK.
  * [`constraints/gcp.restrictCmekCryptoKeyProjects`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-cmek-projects) allows you to control the projects from which a Cloud KMS key can be used to validate requests.
  * You can use both constraints together to enforce the use of CMEK from allowed projects.



Feature

New commands are now available [`gcloud alpha storage`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage).

  * Commands include the ability to create buckets, view metadata for buckets and objects, and edit metadata for buckets and objects.
  * Note that all Cloud Storage `gcloud` commands continue to be in [Preview](https://cloud.google.com/products/#product-launch-stages).



## August 01, 2022

Feature

[Bucket tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags) are now available in [Preview](https://cloud.google.com/products/#product-launch-stages). You can apply tags to buckets for fine-grained access control.

## July 28, 2022

Feature

Configurable [dual-region](https://docs.cloud.google.com/storage/docs/dual-regions) storage is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## June 27, 2022

Feature

[Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) now supports new conditions and a new action.

  * The [`MatchesPrefix` and `MatchesSuffix` conditions](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix) allow you to restrict lifecycle actions to objects with specific prefixes and suffixes.

  * The [`AbortIncompleteMultipartUpload` action](https://docs.cloud.google.com/storage/docs/lifecycle#abort-mpu) allows you to remove abandoned XML API multipart uploads.




Change

The XML API now supports setting a [default Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) on a bucket when [creating the bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create).

## June 06, 2022

Feature

Cloud Storage is now available in Dallas, Texas (`us-south1` region).

## June 02, 2022

Announcement

[Turbo replication](https://docs.cloud.google.com/storage/docs/turbo-replication) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 24, 2022

Feature

Cloud Storage is now available in Columbus, Ohio (`us-east5` region).

## May 23, 2022

Change

[JSON copy requests](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy) and [XML copy requests](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy) now return a permanent error on timeouts for objects larger than 2.5 GiB and a retryable error on timeouts for objects smaller than 2.5 GiB.

## May 10, 2022

Feature

Cloud Storage is now available in Madrid, Spain (`europe-southwest1` region).

## May 06, 2022

Change

[`Us-east4`](https://docs.cloud.google.com/storage/docs/locations#location-dr) is now available for [dual-region storage](https://docs.cloud.google.com/storage/docs/dual-regions). This feature is now in [Preview.](https://cloud.google.com/products#product-launch-stages)

## May 02, 2022

Feature

Cloud Storage is now available in Paris, France (`europe-west9` region).

## April 20, 2022

Feature

Cloud Storage is now available in Milan, Italy (`europe-west8` region).

## April 05, 2022

Feature

With [dual-region storage](https://docs.cloud.google.com/storage/docs/dual-regions), users can now specify two regions within the same continent to create a dual-region of their choosing. This feature is now in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 25, 2022

Feature

Customer-managed encryption key (CMEK) organization policy constraints are now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

  * [`constraints/gcp.restrictNonCmekServices`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-noncmek-services) allows you to control which resources require the use of CMEK.
  * [`constraints/gcp.restrictCmekCryptoKeyProjects`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-cmek-projects) allows you to control the projects from which a Cloud KMS key can be used to validate requests.
  * You can use both constraints together to enforce the use of CMEK from allowed projects.



## March 14, 2022

Announcement

On October 1, 2022, certain prices in Cloud Storage will be changing. For a list of pricing changes, see the [announcement](https://cloud.google.com/storage/pricing-announce).

## February 24, 2022

Feature

The [restrict authentication types](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types) organizational constraint is now in Preview.

  * The constraint allows you to restrict the authentication types that can be used in requests for Cloud Storage resources.



## January 27, 2022

Fixed

The [Storage Object Admin IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) now correctly includes all `storage.multipartUploads` permissions.

## December 15, 2021

Change

[Public Access Prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) is now in GA.

Change

`orgpolicy.policy.get` permission is now included in certain [Cloud Storage IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

  * This permission is now included in the following roles when they're set at the project-level: **Storage Object Creator** , **Storage Object Admin** , **Storage HMAC Key Admin** , and **Storage Admin**.
  * This permission allows principals to know the [organizational policy constraints](https://docs.cloud.google.com/storage/docs/org-policy-constraints) that a project is subject to.



## November 19, 2021

Change

[Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)Preview now uses `inherited` in place of `unspecified`.

  * Name change more clearly expresses how the state of public access prevention is determined for affected buckets.



## November 16, 2021

Feature

Santiago region (`southamerica-west1`) launched.

New [location](https://docs.cloud.google.com/storage/docs/locations#location-r) for storing your data.

## November 01, 2021

Feature

[List Object V2](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#listtype) is [generally available (GA)](https://cloud.google.com/products/#product-launch-stages).

## October 13, 2021

Feature

[Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) keys can now be used to encrypt Cloud Storage data.

  * Cloud EKM keys [encrypt your Cloud Storage data](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) in the same way as other customer-managed encryption keys.



## October 12, 2021

Issue

Objects uploaded using [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) cannot be rewritten or copied within Cloud Storage.

## October 05, 2021

Feature

[Turbo replication](https://docs.cloud.google.com/storage/docs/turbo-replication) is a premium feature designed to provide inter-region replication for newly written objects within 15 minutes.

This feature is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 27, 2021

Announcement

Cloud Storage now [more effectively batches Cloud KMS requests](https://docs.cloud.google.com/blog/products/storage-data-transfer/learn-about-the-latest-cloud-storage-encryption-releases).

  * No changes to how you use Cloud Storage.
  * When working with objects encrypted with Cloud KMS keys, you may see improved performance in your high intensity workloads, a decrease in the number of Cloud KMS audit logs, and a reduction in Cloud KMS charges.
  * These improvements apply to objects written to and rewritten within Cloud Storage using Cloud KMS keys after September 2021.



## September 22, 2021

Fixed

Object listing is no longer impacted when performing large-scale object deletion.

  * Previously, object listing performance could be degraded for up to several days when deleting millions of objects at once in a bucket.



## September 20, 2021

Feature

[Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) can now be managed in the Cloud Console.

  * You can [enable and disable](https://docs.cloud.google.com/storage/docs/using-object-versioning#set) Object Versioning using the Cloud Console.

  * You can [list, restore, copy, move, and delete versioned objects](https://docs.cloud.google.com/storage/docs/using-versioned-objects) from within the Cloud Console.




## August 03, 2021

Feature

Toronto region (`northamerica-northeast2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations#location-r) for storing your data.



## August 01, 2021

Change

Cloud Storage now has [bandwidth quotas](https://docs.cloud.google.com/storage/quotas#bandwidth) for egress to other Google services.

## July 20, 2021

Feature

[`gcloud alpha storage`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage) commands are now available.

  * These commands provide faster uploading and downloading performance over the gsutil command line tool.



## July 12, 2021

Change

[XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) is now in GA.

Feature

[List object V2 for the XML API](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list)Preview launched.

  * List object V2 provides improved interoperability with Amazon S3 tools and libraries.



## July 01, 2021

Feature

[Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)Preview launched.

  * [Enforcing public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention) prevents data in your organization or project from being accidentally exposed to the public.



## June 29, 2021

Feature

Delhi region (`asia-south2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations#location-r) for storing your data.



## June 21, 2021

Feature

Melbourne region (`australia-southeast2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations#location-r) for storing your data.



## May 14, 2021

Feature

[XML API multipart uploads](https://docs.cloud.google.com/storage/docs/xml-api/post-object-multipart)Preview launched.

## April 27, 2021

Change

You can now [compose objects](https://docs.cloud.google.com/storage/docs/composing-objects) using source objects that were encrypted with [Cloud KMS keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).

## March 29, 2021

Security

Cloud CDN, external HTTP(S) Load Balancing, and Cloud Storage services use [BoringSSL](https://boringssl.googlesource.com/boringssl/), and are not affected by the [recent OpenSSL security advisory](https://www.openssl.org/news/secadv/20210325.txt) that relates to CA certificate checks (CVE-2021-3450) and TLS renegotiation (CVE-2021-3449).

## March 24, 2021

Feature

Warsaw region (`europe-central2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## September 28, 2020

Feature

Tokyo+Osaka dual-region (`asia1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## September 08, 2020

Feature

[Custom time](https://docs.cloud.google.com/storage/docs/metadata#custom-time) metadata is now available for objects.

  * Custom time metadata allows you to associate an arbitrary date and time with objects.



Feature

New [conditions](https://docs.cloud.google.com/storage/docs/lifecycle#conditions) available for Object Lifecycle Management:

  * Noncurrent time conditions allow you to define lifecycle actions based on when an object became [noncurrent](https://docs.cloud.google.com/storage/docs/object-versioning#intro).
  * Custom time conditions allow you to define lifecycle actions based on a [custom time](https://docs.cloud.google.com/storage/docs/metadata#custom-time) that you define for objects.



## July 20, 2020

Feature

[Detailed audit logging mode](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging) launched.

## June 08, 2020

Feature

Jakarta region (`asia-southeast2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## May 18, 2020

Change

The V4 signing process is now in GA.

  * The V4 signing process is an improved method for creating [signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures) using RSA or HMAC keys.



## April 20, 2020

Feature

Las Vegas region (`us-west4`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## February 28, 2020

Change

[IAM Conditions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam) is now in GA.

## February 24, 2020

Feature

Salt Lake City region (`us-west3`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## January 24, 2020

Feature

Seoul region (`asia-northeast3`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## January 08, 2020

Feature

Archive Storage now available.

  * New [storage class](https://docs.cloud.google.com/storage/docs/storage-classes#archive) for storing your long-term, rarely accessed data.



## December 13, 2019

Feature

IAM ConditionsBETA for Cloud Storage is now available.

  * [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) allows you to grant permissions for a specified period of time, or to a subset of objects in your buckets.
  * See [Using IAM Conditions on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam) for step-by-step instructions.



## November 18, 2019

Change

[Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is now in GA.

## November 15, 2019

Change

JSON API requests should now be made through the `storage.googleapis.com` endpoint.

  * New preferred [request endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints) for the JSON API.



Change

New display for bucket lists in the Google Cloud Console.

  * The **Name** column is now always visible in the bucket list.
  * The column selector now appears as an icon (![Column options icon.](https://docs.cloud.google.com/static/storage/images/bucket-column-options.png)).



## November 07, 2019

Change

The name of the Bucket Policy Only feature is now changed to [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).

  * The organization policy and API fields referring to Bucket Policy Only are still supported, but we recommend using the equivalent uniform bucket-level access organization policy and API fields.



## October 29, 2019

Change

HMAC keys for service accounts are now in GA.

  * Use the XML API to [manage your HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys).



## September 06, 2019

Change

New Stackdriver metric available to [check for ACL usage.](https://docs.cloud.google.com/storage/docs/using-bucket-policy-only#acl-check)

  * Use [Stackdriver](https://docs.cloud.google.com/monitoring) to determine if enabling Bucket Policy Only would break your workflow.



## August 14, 2019

Change

Multi-Regional Storage and Regional Storage are now Standard Storage.

  * Combining these into a single [Standard Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard) separates your storage class considerations from your location considerations.



## August 09, 2019

Feature

HMAC keys for service accountsBETA are now available.

  * Use [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) to create signed requests for the XML API.
  * [Creating HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys) replaces the need to have HMAC keys for user accounts.



## June 28, 2019

Feature

[Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr) are now in GA.

## June 20, 2019

Feature

You can now inspect buckets for sensitive information using Cloud Data Loss Prevention in the [Google Cloud Console](https://console.cloud.google.com/storage/browser).

  * See [Inspect a Cloud Storage location](https://docs.cloud.google.com/dlp/docs/inspecting-storage#inspecting-gcs) for step-by-step instructions.



## June 18, 2019

Change

Improved object interaction in the Google Cloud Console.

  * [Object downloads](https://docs.cloud.google.com/storage/docs/downloading-objects) can be performed using the **more options** menu associated with each object.
  * Clicking on an object's name opens a page dedicated to details about the object.



## June 17, 2019

Issue

[Object composition](https://docs.cloud.google.com/storage/docs/composite-objects) cannot be performed if any of the source objects are encrypted with [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).

## May 30, 2019

Change

Improved workflow for creating new buckets in the [Google Cloud Console](https://console.cloud.google.com/storage/browser).

  * See the [Creating storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) guide for step-by-step instructions.
  * Estimate your bucket's monthly costs during the bucket creation process.



## April 18, 2019

Feature

Osaka region (`asia-northeast2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



Change

The C++ Cloud Storage Client Library is now in GA.

  * See the [list of Cloud Storage guides](https://docs.cloud.google.com/storage/docs/how-to) for code samples that use the client library.



## April 05, 2019

Feature

V4 signing processBETA launched.

  * The V4 signing process is an improved method for creating signed requests using RSA or HMAC signatures.
  * Use the process to [create signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually).



## March 11, 2019

Feature

Zürich region (`europe-west6`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## March 01, 2019

Change

Price reduction for storing Coldline Storage data in regional locations.

  * Data storage rate is now [as low as $0.004/GB/month](https://cloud.google.com/storage/pricing#storage-pricing).



## February 15, 2019

Feature

Bucket Policy OnlyBETA launched.

  * [Bucket Policy Only](https://docs.cloud.google.com/storage/docs/bucket-policy-only) unifies your access controls by [disabling object-level ACLs](https://docs.cloud.google.com/storage/docs/using-bucket-policy-only#enable).
  * You can [set an organizational policy](https://docs.cloud.google.com/storage/docs/setting-org-policies#bucket-policy) that helps to enforce the use of Bucket Policy Only in your buckets.



## February 13, 2019

Change

The C++ Cloud Storage Client Library is now in BETA.

  * See the [list of Cloud Storage guides](https://docs.cloud.google.com/storage/docs/how-to) for code samples that use the client library.



## January 24, 2019

Fixed

Bucket updates - such as editing lifecycle policies, adding bucket labels, or enabling bucket features - no longer require the updater to have the `storage.buckets.setIamPolicy` permission.

## December 20, 2018

Change

[Customer-Managed Encryption Keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) can now be used with data stored in the `eur4` and `nam4` bucket locations.

## October 22, 2018

Change

[Limit](https://docs.cloud.google.com/storage/quotas) change for [object composition](https://docs.cloud.google.com/storage/docs/composite-objects).

  * There is no longer a limit to the rate at which objects can be composed.



Feature

Hong Kong region (`asia-east2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## October 19, 2018

Feature

Retention policies and object holds are now available.

  * [Retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock) allow you to [set a minimum age](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) that objects must reach before they can be deleted or overwritten.
  * You can [lock your policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#lock-bucket) so that it can not be removed or reduced.
  * You can [place holds on your objects](https://docs.cloud.google.com/storage/docs/holding-objects) as another way to prevent unintended deletion or overwrite.



## October 11, 2018

Change

Geo-redundancy expanded in multi-regional locations.

  * All data stored in [multi-regional locations](https://docs.cloud.google.com/storage/docs/locations#location-mr) are now [geo-redundant](https://docs.cloud.google.com/storage/docs/key-terms#geo-redundant), regardless of storage class.



Feature

[Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr)BETA launched.

  * Data stored in a dual-regional location have copies stored in two specific locations.



## October 09, 2018

Feature

[C++ Cloud Storage Client Library](https://docs.cloud.google.com/storage/docs/reference/libraries)ALPHA

  * See the [list of Cloud Storage guides](https://docs.cloud.google.com/storage/docs/how-to) for code samples that use the client library.



## August 15, 2018

Change

[Cloud Key Management Service keys with Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) is now in GA.

## July 18, 2018

Change

Improved security in the Google Cloud Platform Console.

  * Objects can no longer be made public through one-click actions. See [Making data public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public) for updated guides.
  * [Public access columns](https://docs.cloud.google.com/storage/docs/cloud-console#_publicaccess) for buckets and objects show you when the general public has access to your resources.



## July 10, 2018

Feature

Los Angeles region (`us-west2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## June 21, 2018

Change

[Limit](https://docs.cloud.google.com/storage/quotas) changes for [object composition](https://docs.cloud.google.com/storage/docs/composite-objects).

  * There is no longer a limit to the number of components in a composite object.
  * The composition rate is now measured by the number of source objects, instead of the number of components within those source objects.
  * Copying a composite object is no longer considered when determining a project's composition rate.



## June 11, 2018

Feature

Finland region (`europe-north1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## May 29, 2018

Change

New query parameter in JSON API object listing.

  * The optional query parameter `includeTrailingDelimiter` can now be used in your [JSON API object listing requests](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list).



## May 07, 2018

Feature

Customer-Managed Encryption KeysBETA.

  * [Cloud Key Management Service keys with Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) allow you to manage the encryption keys used on your Cloud Storage objects.
  * Google Cloud Platform Console functionality for the feature is fully available starting April 20.



## February 07, 2018

Change

Changed endpoint for batch requests to the JSON API.

  * When making [HTTP batch requests](https://docs.cloud.google.com/storage/docs/json_api/v1/how-tos/batch) to the JSON API, users should utilize the `www.googleapis.com/batch/storage/v1` endpoint instead of the `www.googleapis.com/batch` endpoint.



## February 01, 2018

Change

Price reduction for Nearline Storage and Coldline Storage in select regions.

  * Nearline Storage price reductions apply to the following regions: Northern Virginia, London, and Frankfurt.
  * Coldline Storage price reductions apply to the following regions: London, Frankfurt, Mumbai, and Sydney.
  * Details regarding Cloud Storage pricing can be found on the [Pricing page](https://cloud.google.com/storage/pricing).



## January 10, 2018

Feature

Montréal region (`northamerica-northeast1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



Feature

Netherlands region (`europe-west4`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## January 04, 2018

Change

The [Cloud Pub/Sub Notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) feature can now have up to 10 different notification configurations send notifications for the same event.

## November 14, 2017

Feature

[Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature is now available.

  * When [enabled on a bucket](https://docs.cloud.google.com/storage/docs/using-requester-pays#enable), users accessing the bucket or its contents must specify a project to bill for charges that arise from their request.
  * Callers can [specify a billing project](https://docs.cloud.google.com/storage/docs/using-requester-pays#using) on requests to buckets both with and without Requester Pays enabled.



Deprecated

The **resource** attribute of [Cloud Pub/Sub Notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) is now deprecated. It does not appear for new subscriptions and will not appear in any subscription after June 1, 2018.

Change

The [Cloud Pub/Sub Notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/pubsub-notifications) feature is now in GA.

## October 31, 2017

Feature

Mumbai region (`asia-south1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## September 18, 2017

Issue

Bucket metadata `PATCH` requests to the JSON API require the `storage.buckets.setIamPolicy` permission if the requester has `storage.buckets.getIamPolicy` permission. This is true even for patches that _do not change_ ACLs or IAM permissions.

See [IAM permissions for JSON](https://docs.cloud.google.com/storage/docs/access-control/iam-json) and [IAM permissions for gsutil](https://docs.cloud.google.com/storage/docs/access-control/iam-gsutil) for affected methods and commands.

## September 05, 2017

Feature

São Paulo region (`southamerica-east1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## August 14, 2017

Change

You can now [control Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/managing-lifecycles) from the [Storage Console](https://console.cloud.google.com/storage/browser).

## August 01, 2017

Feature

Frankfurt region (`europe-west3`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## June 20, 2017

Feature

Sydney region (`australia-southeast1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## June 06, 2017

Feature

New public dataset stored in Cloud Storage.

  * Data for [NEXRAD](https://docs.cloud.google.com/storage/docs/public-datasets/nexrad) are now hosted publicly in Cloud Storage.



Feature

London region (`europe-west2`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## May 31, 2017

Change

[Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) policies are now GA for buckets. Policies applied at the bucket level can be used to control access to individual buckets as well as all the objects within them.

## May 24, 2017

Change

Attempts to access a non-existent object returns a 403 error instead of a 404 error if the requester lacks object listing permission for the associated bucket.

## May 09, 2017

Feature

Northern Virginia region (`us-east4`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## April 26, 2017

Change

The [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries) for the Cloud Storage API is now in GA.

## April 11, 2017

Feature

Singapore region (`asia-southeast1`) launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## April 06, 2017

Feature

[Labels](https://docs.cloud.google.com/storage/docs/key-terms#bucket-labels) can now be [used with your buckets](https://docs.cloud.google.com/storage/docs/using-bucket-labels) in order to better organize all of your Google Cloud Platform resources.

## March 27, 2017

Feature

Cloud Pub/Sub Notifications for Cloud StorageBETA

  * [Track changes](https://docs.cloud.google.com/storage/docs/reporting-changes) to objects in your buckets through notifications sent to Cloud Pub/Sub.
  * You can set the [event types](https://docs.cloud.google.com/storage/docs/pubsub-notifications#events) that generate notifications as well as the [information contained within notifications](https://docs.cloud.google.com/storage/docs/pubsub-notifications#format).



## December 07, 2016

Change

The [per-object storage class](https://docs.cloud.google.com/storage/docs/per-object-storage-class) feature is now in GA.

## November 07, 2016

Feature

`asia-northeast1` region launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## October 20, 2016

Feature

Per-object storage classesBETA

  * Users can [set the storage class at the object level](https://docs.cloud.google.com/storage/docs/per-object-storage-class).
  * Users can configure [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) to automatically change the storage class of an object when designated criteria are met.



Feature

Coldline, a new [archival storage class](https://docs.cloud.google.com/storage/docs/storage-classes), is now available.

  * The [Coldline Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#coldline) provides low price, immediately accessible data storage for your backup, archival and disaster recovery needs.
  * Ideal for data that intends to be accessed less than once a year.



Change

Standard Storage class is now Multi-Regional Storage and Regional Storage.

  * The [Multi-Regional Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#multi-regional) provides the same price and performance along with geo-redundant copies of your data and a 99.95% availability SLA.
  * The [Regional Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#regional) provides the same performance at a reduced price.



## October 04, 2016

Feature

Public datasets stored in Cloud Storage

  * Datasets for the Landsat and Sentinel-2 missions are now hosted publicly in Cloud Storage.
  * [Read about the Landsat dataset](https://docs.cloud.google.com/storage/docs/public-datasets/landsat)
  * [Read about the Sentinel-2 dataset](https://docs.cloud.google.com/storage/docs/public-datasets/sentinel-2)



## September 26, 2016

Feature

Alpha release for bucket-level IAM.

  * _Access to this feature is currently by[request/invite](https://docs.google.com/a/google.com/forms/d/e/1FAIpQLSeZkzvcpwwXZhffC9-N9YHXsWQxnMETSSMmhASukCvD0JwI_g/viewform) only._ [Apply IAM permissions to individual buckets](https://docs.cloud.google.com/storage/docs/access-control/iam) in your projects.



## August 29, 2016

Change

Improved upload experience in the [Storage Console](https://console.cloud.google.com/storage/browser).

  * Users can retry failed uploads.
  * The upload drawer persists when navigating to other parts of the Storage Console.
  * Users are immediately notified when an upload starts and ends.



## August 03, 2016

Change

Nearline latency times reduced.

  * Buckets created in the [Nearline storage class](https://docs.cloud.google.com/storage/docs/storage-classes#nearline) now have the same sub-second latency as other storage class buckets.



## August 01, 2016

Change

Object generation numbers no longer have ordering guarantees.

  * [Generation numbers](https://docs.cloud.google.com/storage/docs/generations-preconditions) associated with Cloud Storage objects no longer increase monotonically or have ordering guarantees between generations.
  * Generation numbers continue to be unique resource identifiers.
  * [See the announcement](https://groups.google.com/forum/#!msg/gs-announce/XdSq25nsHio/-GuZxzyOAwAJ).



## July 20, 2016

Feature

`us-west1` region launched.

  * New [location](https://docs.cloud.google.com/storage/docs/locations) for storing your data.



## June 24, 2016

Feature

`X-Goog-Content-Length-Range` custom header available.

  * New header for [XML](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcontentlengthrange) and [JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#xgoogcontentlengthrange).
  * Allows for checking the size of content sent to Cloud Storage.



## June 13, 2016

Change

On-Demand I/O for Nearline-class buckets no longer necessary.

  * Buckets created in the [Nearline storage class](https://docs.cloud.google.com/storage/docs/storage-classes#nearline) now have throughput and QPS that automatically scale with your needs, at no extra cost.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
