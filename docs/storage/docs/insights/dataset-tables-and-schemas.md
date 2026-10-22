---
url: https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas/
title: Storage Insights datasets tables and schemas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:29.418121+00:00
---

# Storage Insights datasets tables and schemas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage Insights datasets tables and schemas Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the tables and schemas in [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets). You can use these datasets to analyze operational patterns, monitor resource usage, and understand activity across your storage environment.

## Dataset schema of metadata

The following sections describe the metadata fields included in datasets. For more information about BigQuery column modes, see [Modes](https://docs.cloud.google.com/bigquery/docs/schemas#modes). The column modes determine how BigQuery stores and queries the data.

You can connect [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) with Storage Insights datasets to select data dynamically. This approach lets you query dataset columns directly using filter expressions instead of using manual manifest files. The `Storage batch operations filterable` column in the following tables indicates whether a metadata field is supported when constructing Common Expression Language (CEL) filter arguments (`--bucket-filters` or `--object-filters`) directly in Google Cloud CLI. If a field is supported, you can reference its column name directly in your filter expressions. For details about the supported syntax, see the [CEL filters reference](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).

### Bucket metadata

The bucket metadata schema includes the `bucket_attributes_view` and `bucket_attributes_latest_snapshot_view` tables. The bucket metadata tables have the following fields:

Filter this table:  Metadata field | Mode | Type | Description | Storage batch operations filterable  
---|---|---|---|---  
`snapshotTime` | `NULLABLE` | `TIMESTAMP` | The [`snapshotTime`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#snapshotdefinition) field stores the time of the bucket metadata snapshot refresh in [RFC 3339 format](https://tools.ietf.org/html/rfc3339). All records that are generated from the same snapshot refresh have the same `snapshotTime`. |   
`name` | `NULLABLE` | `STRING` | The name of the bucket. |   
`location` | `NULLABLE` | `STRING` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this location. |   
`project` | `NULLABLE` | `INTEGER` | The project number of the project the bucket belongs to. |   
`storageClass` | `NULLABLE` | `STRING` | The bucket's default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). |   
`public` | `NULLABLE` | `RECORD` | Deprecated. This field indicates whether a bucket is publicly accessible. Use `iamConfiguration` instead. |   
`public.bucketPolicyOnly` | `NULLABLE` | `BOOLEAN` | Deprecated. This field, part of the `public` record, indicates whether uniform bucket-level access is enabled, which prevents access through object-level ACLs. |   
`public.publicAccessPrevention` | `NULLABLE` | `STRING` | Deprecated. This field, part of the `public` record, indicates whether public access to the bucket is prevented. |   
`autoclass` | `NULLABLE` | `RECORD` | The bucket's [Autoclass configuration](https://docs.cloud.google.com/storage/docs/autoclass), which, when enabled, controls the storage class of objects based on how and when the objects are accessed. |   
`autoclass.enabled` | `NULLABLE` | `BOOLEAN` | Whether or not Autoclass is enabled. |   
`autoclass.toggleTime` | `NULLABLE` | `TIMESTAMP` | The time at which Autoclass was last enabled or disabled for this bucket, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`versioning` | `NULLABLE` | `BOOLEAN` | Whether or not the bucket has versioning enabled. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). |   
`lifecycle` | `NULLABLE` | `BOOLEAN` | Whether or not the bucket has a lifecycle configuration. See [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) for more information. |   
`metageneration` | `NULLABLE` | `INTEGER` | The metadata generation of this bucket. |   
`timeCreated` | `NULLABLE` | `TIMESTAMP` | The creation time of the bucket in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`tags` | `NULLABLE` | `RECORD` | Deprecated. This field contains user-defined key-value pairs associated with the bucket. Use `resourceTags` instead. |   
`tags.lastUpdatedTime` | `NULLABLE` | `TIMESTAMP` | Deprecated. This field indicates the last time the `tags` were updated. |   
`tags.tagMap` | `REPEATED` | `RECORD` | Deprecated. This field, part of the `tags` record, contains the map of tag keys and values. |   
`tags.tagMap.key` | `NULLABLE` | `STRING` | Deprecated. This field, part of the `tags.tagMap` record, is the key of a tag. |   
`tags.tagMap.value` | `NULLABLE` | `STRING` | Deprecated. This field, part of the `tags.tagMap` record, is the value of a tag. |   
`labels` | `REPEATED` | `RECORD` | User-provided [bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), in key-value pairs. |   
`labels.key` | `NULLABLE` | `STRING` | An individual label entry. |   
`labels.value` | `NULLABLE` | `STRING` | The label's value. |   
`retentionPeriod` | `NULLABLE` | `LONG` | The retention period of the bucket's [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock) in seconds. |   
`retentionMode` | `NULLABLE` | `STRING` | The retention mode of the bucket's retention policy. The possible values are `Locked` or `Unlocked`. |   
`objectRetentionEnabled` | `NULLABLE` | `BOOLEAN` | Whether [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) is enabled on a bucket. The possible values are `True` or `False`. If this field is `True`, objects in the bucket can have object-level retention configurations. |   
`defaultEventBasedHold` | `NULLABLE` | `BOOLEAN` | Whether a bucket has a default event-based property enabled. The possible values are `True` or `False`. |   
`softDeletePolicy` | `NULLABLE` | `RECORD` |  The bucket's [soft delete policy](https://docs.cloud.google.com/storage/docs/soft-delete), which defines the period of time during which objects in the bucket are retained in a soft-deleted state after being deleted. Objects in a soft-deleted state cannot be permanently deleted, and are restorable until their `hardDeleteTime`.  |   
`softDeletePolicy.effectiveTime` | `NULLABLE` | `DATETIME` |  The datetime at which the soft delete policy becomes effective, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. `softDeletePolicy.effectiveTime` is updated whenever `softDeletePolicy.retentionDurationSeconds` is increased. |   
`softDeletePolicy.retentionDurationSeconds` | `NULLABLE` | `LONG` |  The period of time during which a soft-deleted object is retained and cannot be permanently deleted, in seconds. The value must be greater than or equal to 7 days and less than 90 days. The value can also be set to `0`, which disables the soft delete policy.  |   
`enforcedEncryptionAllowedTypes` | `REPEATED` | `STRING` | The [encryption types](https://docs.cloud.google.com/storage/docs/encryption) allowed on the bucket. The possible values are as follows: 

  * `GMEK` (Google-owned and Google-managed encryption keys)
  * `CMEK` (customer-managed encryption keys)
  * `CSEK` (customer-supplied encryption keys)

|   
`encryption` | `NULLABLE` | `RECORD` | The encryption configuration of the bucket. Cloud Storage uses this configuration to encrypt new objects added to the bucket, unless you specify object-level encryption during upload. |   
`encryption.defaultEncryptionType` | `NULLABLE` | `STRING` | The default encryption type of the bucket. If `encryption.defaultKmsKeyName` is set, this value is `CMEK`, otherwise it is `GMEK`. |   
`encryption.defaultKmsKeyName` | `NULLABLE` | `STRING` | The default Cloud Key Management Service key configured to be used for new objects in the bucket. If this field is set, Cloud Key Management Service is used for default encryption (CMEK). If not set, Google-owned and Google-managed encryption keys are used for default encryption (GMEK). |   
`iamConfiguration` | `NULLABLE` | `RECORD` | The IAM configuration for a bucket. |   
`iamConfiguration.uniformBucketLevelAccess` | `NULLABLE` | `RECORD` | The bucket's [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) configuration. |   
`iamConfiguration.uniformBucketLevelAccess.enabled` | `NULLABLE` | `BOOLEAN` | Whether or not the bucket uses uniform bucket-level access. |   
`iamConfiguration.publicAccessPrevention` | `NULLABLE` | `STRING` | The bucket's [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) status, which is either `"inherited"` or `"enforced"`. |   
`resourceTags` | `REPEATED` | `RECORD` | The bucket's [tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags). For more information, see [Cloud Resource Manager API](https://docs.cloud.google.com/resource-manager/reference/rest). |   
`resourceTags.key` | `NULLABLE` | `STRING` | The `resourceTags` key. |   
`resourceTags.value` | `NULLABLE` | `STRING` | The `resourceTags` value. |   
`objectCount` | `NULLABLE` | `INTEGER` | The total number of objects in the bucket.  
`totalSize` | `NULLABLE` | `INTEGER` | The total size of the bucket in bytes.  
  
### Object metadata

The object metadata schema includes the `object_attributes_view` and `object_attributes_latest_snapshot_view` tables. These tables include metadata for live objects, non-current object versions if [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) is enabled, and soft-deleted objects if [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) is enabled. The object metadata tables have the following fields:

Filter this table:  Metadata field | Mode | Type | Description | Storage batch operations filterable  
---|---|---|---|---  
`snapshotTime` | `NULLABLE` | `TIMESTAMP` | The [`snapshotTime`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#snapshotdefinition) field stores the time of the object metadata snapshot refresh in [RFC 3339 format](https://tools.ietf.org/html/rfc3339). All records that are generated from the same snapshot refresh have the same `snapshotTime`. |   
`bucket` | `NULLABLE` | `STRING` | The name of the bucket containing this object. |   
`location` | `NULLABLE` | `STRING` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this location. |   
`componentCount` | `NULLABLE` | `INTEGER` | Returned for [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) only. Number of non-composite objects in the composite object. `componentCount` includes non-composite objects that were part of any composite objects used to [compose](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) the current object. |   
`contentDisposition` | `NULLABLE` | `STRING` | [Content-Disposition](https://datatracker.ietf.org/doc/html/rfc6266) of the object data. |   
`contentEncoding` | `NULLABLE` | `STRING` | [Content-Encoding](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.2.2) of the object data. |   
`contentLanguage` | `NULLABLE` | `STRING` | [Content-Language](https://docs.cloud.google.com/storage/docs/metadata#content-language) of the object data. |   
`contentType` | `NULLABLE` | `STRING` | [Content-Type](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5) of the object data. |   
`contexts` | `REPEATED` | `RECORD` | Contexts attached to an object, in key-value pairs. For more information about object contexts, see [Object contexts overview](https://docs.cloud.google.com/storage/docs/object-contexts). |   
`contexts.key` | `NULLABLE` | `STRING` | The object context key. |   
`contexts.value` | `NULLABLE` | `STRING` | The value of the object context key. |   
`contexts.type` | `NULLABLE` | `STRING` | The object context type, which is always `custom`. |   
`contexts.createTime` | `NULLABLE` | `TIMESTAMP` | The time when this object context key was first added to the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`contexts.updateTime` | `NULLABLE` | `TIMESTAMP` | The time when this object context key was last updated. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`crc32c` | `NULLABLE` | `INTEGER` | CRC32c checksum, as described in [RFC 4960, Appendix B](https://datatracker.ietf.org/doc/html/rfc4960#appendix-B); encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4) in big-endian byte order. This field is not present for objects encrypted with customer-managed encryption keys (CMEK). |   
`customTime` | `NULLABLE` | `TIMESTAMP` | A user-specified timestamp for the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`etag` | `NULLABLE` | `STRING` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the object. |   
`eventBasedHold` | `NULLABLE` | `BOOLEAN` | Whether or not the object is subject to an [event-based hold](https://docs.cloud.google.com/storage/docs/object-holds#hold-types). |   
`generation` | `NULLABLE` | `INTEGER` | The content generation of this object. |   
`md5Hash` | `NULLABLE` | `STRING` | MD5 hash of the data, encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4). This field is not present for [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) and objects encrypted with customer-managed encryption keys (CMEK). |   
`mediaLink` | `NULLABLE` | `STRING` | A URL for downloading the object's data. |   
`metadata` | `REPEATED` | `RECORD` | User-provided metadata, in key-value pairs. |   
`metadata.key` | `NULLABLE` | `STRING` | An individual metadata entry. |   
`metadata.value` | `NULLABLE` | `STRING` | The metadata value. |   
`metageneration` | `NULLABLE` | `INTEGER` | The version of the metadata for this object at this generation. |   
`name` | `NULLABLE` | `STRING` | The name of the object. |   
`selfLink` | `NULLABLE` | `STRING` | A URL for this object. |   
`size` | `NULLABLE` | `INTEGER` | The size of the object in bytes. |   
`storageClass` | `NULLABLE` | `STRING` | [Storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of the object. |   
`temporaryHold` | `NULLABLE` | `BOOLEAN` | Whether or not the object is subject to a [temporary hold](https://docs.cloud.google.com/storage/docs/object-holds#hold-types). |   
`timeCreated` | `NULLABLE` | `TIMESTAMP` | The creation time of the object. This timestamp doesn't change. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`timeDeleted` | `NULLABLE` | `TIMESTAMP` | The deletion time of the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. For non-current object versions, the `timeDeleted` field indicates when the object version became non-current. |   
`updated` | `NULLABLE` | `TIMESTAMP` | The most recent [modification time](https://docs.cloud.google.com/storage/docs/metadata#timestamps) of the object metadata. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`timeStorageClassUpdated` | `NULLABLE` | `TIMESTAMP` | The time at which the object's storage class was last changed. |   
`retentionExpirationTime` | `NULLABLE` | `TIMESTAMP` | The earliest time that the object can be deleted. This value depends on both the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) that is set for the object, and on the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) that is set for the bucket that contains the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`retentionExpirationTimeLockStatus` | `NULLABLE` | `BOOLEAN` | Lock status of `retentionExpirationTime`. |   
`retentionExpirationTimeSource` | `NULLABLE` | `STRING` | Source of `retentionExpirationTime`. |   
`retainUntilTime` | `NULLABLE` | `TIMESTAMP` | Indicates the time set by the [object-level retention policy configuration](https://docs.cloud.google.com/storage/docs/object-lock), reflecting only the object-level setting. The effective date until which the object is retained is provided in the `retentionExpirationTime` field. The `retentionExpirationTime` is the later of the dates specified by any object-level and [bucket-level retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock). |   
`retainUntilTimeLockStatus` | `NULLABLE` | `BOOLEAN` | Lock status of `retainUntilTime`, as set by the object-level retention policy configuration. |   
`softDeleteTime` | `NULLABLE` | `DATETIME` | The time at which the object was [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). Only available for objects in buckets with a soft delete policy. |   
`hardDeleteTime` | `NULLABLE` | `DATETIME` | The time at which a soft-deleted object will be permanently deleted and can no longer be restored. The value is the sum of the `softDeleteTime` value and the `softDeletePolicy.retentionDurationSeconds` value of the bucket. Only available for objects in buckets with a soft delete policy. |   
`project` | `NULLABLE` | `INTEGER` | The project number of the project the bucket belongs to. |   
`ref` | `NULLABLE` | `RECORD` | A BigQuery `ObjectRef` value referencing the Cloud Storage object. To use this column in queries, see [Analyze object data and metadata using BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-data). For objects ending in `/`, this field returns null values. For information about how to troubleshoot, see [Null values in `ref` column when querying datasets](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#null-ref-values).  
`ref.uri` | `NULLABLE` | `STRING` | A BigQuery reference URL for the associated Cloud Storage object, which is equivalent to the object's URI. For example, `gs://bucket_name/object_name`. |   
`ref.version` | `NULLABLE` | `STRING` | The BigQuery version identifier for the associated Cloud Storage object, which is equivalent to the object's `generation` field. |   
`ref.authorizer` | `NULLABLE` | `STRING` | The [Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection) that you can use to access the Cloud Storage object from BigQuery. The value is always `null` in the object metadata schema. |   
`ref.details` | `NULLABLE` | `JSON` | The metadata fields available in the BigQuery representation of the Cloud Storage object, using the following schema:
    
    
    gcs_metadata json {
              "content_type": string,
              "md5_hash": string,
              "size": number,
              "updated": number
            }

|   
`encryptionType` | `NULLABLE` | `STRING` | The [encryption type](https://docs.cloud.google.com/storage/docs/encryption) of the object. The possible values are as follows: 

  * `GMEK` (Google-owned and Google-managed encryption keys)
  * `CMEK` (customer-managed encryption keys)
  * `CSEK` (customer-supplied encryption keys)

|   
`securityInsights` | `NULLABLE` | `RECORD` | Provides the public access status of the object, indicating whether it is publicly readable or writable. For details, see [Identify publicly accessible objects](https://docs.cloud.google.com/storage/docs/insights/datasets#public-accessible-objects).  
`securityInsights.publicAccessInsight` | `NULLABLE` | `RECORD` | Provides the public accessibility status of the object. |   
`securityInsights.publicAccessInsight.readPublicAccess` | `NULLABLE` | `STRING` | The public readability status of the object. The possible values are as follows: 

  * `PUBLIC`: Indicates that the object has permissions that grant public access, and no other policies restrict that access.
  * `NOT_PUBLIC`: Indicates that the object is protected from public access either by permissions or a prevention policy.
  * `UNSUPPORTED`: Indicates that the object is within a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders).
  * `ERROR`: Indicates that a transient internal error has occurred when computing the public status of the object. The failed public status isn't backfilled for existing snapshots. Storage Insights restores the status in the subsequent snapshots.

|   
`securityInsights.publicAccessInsight.readPublicAccessSource` | `NULLABLE` | `STRING` | If `readPublicAccess` is `PUBLIC`, returns the source of the public read permission, otherwise this field is `null`. The possible values are as follows: 

  * `Object`: Indicates object-level permissions.
  * `Bucket`: Indicates bucket-level permissions.
  * `ERROR`: Indicates that a transient internal error has occurred when determining the source of public access.

|   
`securityInsights.publicAccessInsight.writePublicAccess` | `NULLABLE` | `STRING` | The public writability status of the object. The possible values are as follows: 

  * `PUBLIC`: Indicates that the object has permissions that grant public access, and no other policies restrict that access.
  * `NOT_PUBLIC`: Indicates that the object is protected from public access either by permissions or a prevention policy.
  * `UNSUPPORTED`: Indicates that the object is within a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders).
  * `ERROR`: Indicates that a transient internal error has occurred when computing the public status of the object. The failed public status isn't backfilled for existing snapshots. Storage Insights restores the status in the subsequent snapshots.

|   
  
### Latest bucket and object metadata snapshot

The linked dataset exposes the latest snapshot of the bucket and object metadata through the following dedicated views:

  * The `bucket_attributes_latest_snapshot_view` table provides the latest metadata for your Cloud Storage buckets. Its structure matches the Bucket metadata schema.

  * The `object_attributes_latest_snapshot_view` table provides the latest metadata for your Cloud Storage objects. Its structure matches the Object metadata schema.




### Project metadata

The linked dataset exposes project metadata as a view named `project_attributes_view`:

Filter this table:  Metadata field | Mode | Type | Description  
---|---|---|---  
`snapshotTime` | `NULLABLE` | `TIMESTAMP` | The [`snapshotTime`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#snapshotdefinition) field stores the time of the project metadata snapshot refresh in [RFC 3339 format](https://tools.ietf.org/html/rfc3339). All records that are generated from the same snapshot refresh have the same `snapshotTime`.  
`name` | `NULLABLE` | `STRING` | The name of the project.  
`id` | `NULLABLE` | `STRING` | The unique identifier for the project.  
`number` | `NULLABLE` | `INTEGER` | A numeric value associated with the project.  
  
### Object contexts catalog

The linked dataset exposes the latest metadata for [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts), including [extended data](https://docs.cloud.google.com/storage/docs/object-contexts#extended-data) payloads ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), as a view named `object_contexts_catalog_view`.

The `object_contexts_catalog_view` view provides the latest context information for your Cloud Storage objects. The catalog view updates every 24 hours. The initial load takes 24 to 48 hours. Objects in new or relocated buckets appear within 24 to 48 hours.

The `object_contexts_catalog_view` table has the following fields:

Filter this table:  Metadata field | Mode | Type | Description  
---|---|---|---  
`project` | `NULLABLE` | `INTEGER` | The project number of the project that the bucket belongs to.  
`bucket` | `NULLABLE` | `STRING` | The name of the bucket containing this object.  
`name` | `NULLABLE` | `STRING` | The name of the object.  
`generation` | `NULLABLE` | `INTEGER` | The content generation of this object.  
`location` | `NULLABLE` | `STRING` | The location of the object.  
`createdTime` | `NULLABLE` | `STRING` | The creation time of the object.  
`catalogUpdatedTime` | `NULLABLE` | `TIMESTAMP` | The time at which the entry in the catalog was updated.  
`contexts` | `REPEATED` | `RECORD` | Array of [context entries](https://docs.cloud.google.com/storage/docs/object-contexts) attached to the object.  
`contexts.key` | `NULLABLE` | `STRING` | The key for the context entry (for example, `google:annotation:label-detector-v1`).  
`contexts.value` | `NULLABLE` | `STRING` | The string value associated with the context key.  
`contexts.contextCreationTime` | `NULLABLE` | `TIMESTAMP` | Creation time of this specific context entry.  
`contexts.contextUpdateTime` | `NULLABLE` | `TIMESTAMP` | Last update time of this specific context entry.  
`contexts.extendedData` ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | `NULLABLE` | `JSON` | JSON object containing structured extended data payloads for contexts (such as ML model bounding boxes and labels). This field is `NULL` if the context does not have extended data.  
  
## Dataset schema for activity data tables

Storage Insights datasets provide activity data, including operational metrics, error logs, and aggregated views with customizable scopes to support diverse analysis needs. The following sections describe the activity data schemas and the data available in them.

### Object activity data

The `object_events_view` table in your Storage Insights dataset provides queryable records of create, update, and delete object operations, metadata, and details about the errors encountered during these operations. You can use the data to track and troubleshoot changes to your storage assets by querying the `object_events_view` view. The data in the `object_events_view` view is scoped to your Storage Intelligence subscription and lists all the actively enabled objects within it.

The `object_events_view` table includes the following fields:

Filter this table:  Field | Mode | Type | Description  
---|---|---|---  
`requestCompletionTimestamp` | `NULLABLE` | `TIMESTAMP` | The timestamp when the request was completed, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`project` | `NULLABLE` | `INTEGER` | The project number that owns the bucket resource.  
`bucketName` | `NULLABLE` | `STRING` | The name of the bucket specified in the request.  
`objectName` | `NULLABLE` | `STRING` | The name of the object specified in the request. This field can be null.  
`requestOperation` | `NULLABLE` | `STRING` | The Cloud Storage operation performed. This field is limited to write, update, and delete operations and can be null.  
`requestBytes` | `NULLABLE` | `INTEGER` | The number of bytes sent in the request.  
`responseBytes` | `NULLABLE` | `INTEGER` | The number of bytes sent in the response.  
`requestProcessingTimeMicros` | `NULLABLE` | `INTEGER` | The time in microseconds the server took to process the request. This time is measured from when the first byte is received until the response is sent. For [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads), the response to the final upload request determines the endpoint.  
`requestId` | `NULLABLE` | `STRING` | The identifier for the request.  
`requestHost` | `NULLABLE` | `STRING` | The host specified in the original request.  
`requestHttpMethod` | `NULLABLE` | `STRING` | The HTTP method used for this request.  
`responseStatus` | `NULLABLE` | `INTEGER` | The HTTP status code sent in the server's response.  
`requestReferrer` | `NULLABLE` | `STRING` | The HTTP referrer for the request.  
`size` | `NULLABLE` | `INTEGER` | The size of the object in bytes.  
`generation` | `NULLABLE` | `INTEGER` | The content generation of the object, used for object versioning.  
`timeCreated` | `NULLABLE` | `TIMESTAMP` | The object's creation time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`storageClass` | `NULLABLE` | `STRING` | The storage class of the object.  
`errorReason` | `NULLABLE` | `STRING` | The reason for the error (limited to 429 errors).  
`location` | `NULLABLE` | `STRING` | The location of the object.  
  
### Project activity view

The `project_activity_view` table offers aggregated operational insights across your projects. The table summarizes total activity by counting operation types, bytes transferred, and response codes and errors. You can use the project activity insights for monitoring, tracking, and internal cost attribution. The data in the view is determined by your Storage Intelligence subscription scope. The view displays aggregated data only for the buckets and objects that are actively enabled under your subscription. For example, if you enable Storage Intelligence only for ten specific buckets, the view displays data exclusively for those ten buckets. Conversely, if you enable Storage Intelligence at a higher level (organization, folder, or project), all buckets and objects within that scope are automatically included, and the view displays the aggregated data for them.

The `project_activity_view` table includes the following fields:

Filter this table:  Field | Mode | Type | Description  
---|---|---|---  
`snapshotStartTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's start time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`snapshotEndTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's end time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`project` | `NULLABLE` | `INTEGER` | The project number.  
`totalRequests` | `NULLABLE` | `INTEGER` | The total number of requests made across the project.  
`totalReads` | `NULLABLE` | `INTEGER` | The total number of read operations.  
`totalWrites` | `NULLABLE` | `INTEGER` | The total number of write operations.  
`totalUpdates` | `NULLABLE` | `INTEGER` | The total number of update operations.  
`totalDeletes` | `NULLABLE` | `INTEGER` | The total number of delete operations.  
`totalLists` | `NULLABLE` | `INTEGER` | The total number of list operations.  
`totalRequestBytes` | `NULLABLE` | `INTEGER` | The total number of request bytes transferred.  
`totalResponseBytes` | `NULLABLE` | `INTEGER` | The total number of response bytes transferred.  
`count4xx` | `NULLABLE` | `INTEGER` | The total number of 4xx errors.  
`count5xx` | `NULLABLE` | `INTEGER` | The total number of 5xx errors.  
`count2xx` | `NULLABLE` | `INTEGER` | The total number of 2xx success responses.  
`count400` | `NULLABLE` | `INTEGER` | The total number of 400 errors for bad requests.  
`count401` | `NULLABLE` | `INTEGER` | The total number of 401 errors for unauthorized requests.  
`count403` | `NULLABLE` | `INTEGER` | The total number of 403 errors for forbidden requests.  
`count429` | `NULLABLE` | `INTEGER` | The total number of 429 errors for usage limit exceeded requests.  
  
### Bucket activity view

The `bucket_activity_view` table offers aggregated operational insights across your buckets. The table summarizes total activity by counting operation types, bytes transferred, response codes, errors, and includes details about top prefixes. You can use the bucket activity insights for bucket-level monitoring, troubleshooting, metering, and analyzing your most and least active buckets. The data in `bucket_activity_view` table is scoped to your Storage Intelligence subscription and includes records for all actively enabled buckets.

The `bucket_activity_view` table includes the following fields:

Filter this table:  Field | Mode | Type | Description  
---|---|---|---  
`snapshotStartTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's start time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`snapshotEndTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's end time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`name` | `NULLABLE` | `STRING` | The name of the bucket.  
`generation` | `NULLABLE` | `INTEGER` | The bucket's generation number.  
`project` | `NULLABLE` | `INTEGER` | The project number.  
`location` | `NULLABLE` | `STRING` | The location of the bucket.  
`totalRequests` | `NULLABLE` | `INTEGER` | The total number of requests made on the bucket.  
`totalReads` | `NULLABLE` | `INTEGER` | The total number of read operations.  
`totalWrites` | `NULLABLE` | `INTEGER` | The total number of write operations.  
`totalUpdates` | `NULLABLE` | `INTEGER` | The total number of update operations.  
`totalDeletes` | `NULLABLE` | `INTEGER` | The total number of delete operations.  
`totalLists` | `NULLABLE` | `INTEGER` | The total number of list operations.  
`totalRequestBytes` | `NULLABLE` | `INTEGER` | The total number of request bytes transferred.  
`totalResponseBytes` | `NULLABLE` | `INTEGER` | The total number of response bytes transferred.  
`count4xx` | `NULLABLE` | `INTEGER` | The total number of 4xx errors.  
`count5xx` | `NULLABLE` | `INTEGER` | The total number of 5xx errors.  
`count2xx` | `NULLABLE` | `INTEGER` | The total number of 2xx success responses.  
`count400` | `NULLABLE` | `INTEGER` | The total number of 400 errors for bad requests.  
`count401` | `NULLABLE` | `INTEGER` | The total number of 401 errors for unauthorized requests.  
`count403` | `NULLABLE` | `INTEGER` | The total number of 403 errors for forbidden requests.  
`count429` | `NULLABLE` | `INTEGER` | The total number of 429 errors for usage limit exceeded requests.  
`topPrefixes429Errors` | `REPEATED` | `RECORD` | The top 5 bucket prefixes with the most 429 errors, returned as a `RECORD` containing the prefix as a `STRING` and the error count as an `INTEGER`.  
`topPrefixesRequestBytes` | `REPEATED` | `RECORD` | The top 5 bucket prefixes with the highest number of requested bytes, returned as a `RECORD` containing the prefix as a `STRING` and the count as an `INTEGER`.  
`topPrefixesResponseBytes` | `REPEATED` | `RECORD` | The top 5 bucket prefixes with the highest number of response bytes, returned as a `RECORD` containing the prefix as a `STRING` and the count as an `INTEGER`.  
`topPrefixesHighestOperations` | `REPEATED` | `RECORD` | The top 5 bucket prefixes with the highest number of operations, returned as a `RECORD` containing the prefix as a `STRING` and the count as an `INTEGER`.  
  
### Bucket region activity view

The `bucket_region_activity_view` table summarizes the total bytes sent and received for a bucket, aggregated by destination region. Use the bucket activity regional data to identify the most active regions, helping you determine the optimal bucket location, analyze regional egress, and consider [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) as needed to optimize performance, cost, or resilience. The data in `bucket_region_activity_view` table is scoped to your Storage Intelligence subscription and includes records for all actively enabled buckets. 

Filter this table:  Field | Mode | Type | Description  
---|---|---|---  
`snapshotStartTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's start time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`snapshotEndTime` | `NULLABLE` | `TIMESTAMP` | The snapshot's end time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339).  
`project` | `NULLABLE` | `INTEGER` | The project number for the bucket.  
`name` | `NULLABLE` | `STRING` | The name of the bucket.  
`generation` | `NULLABLE` | `INTEGER` | The bucket's generation number.  
`requestLocation` | `NULLABLE` | `STRING` | The Google Cloud location where the request originated.  
`bucketLocation` | `NULLABLE` | `STRING` | The location of the bucket.  
`requestBytes` | `NULLABLE` | `INTEGER` | The total number of bytes transferred for requests between the specified bucket and location.  
`responseBytes` | `NULLABLE` | `INTEGER` | The total number of bytes transferred for responses between the specified bucket and location.  
  
## Dataset schema for events and errors

In the linked dataset, you can also view the snapshot processing events and errors in the `events_view` and `error_attributes_view` views. To troubleshoot the snapshot processing errors, see Troubleshoot dataset errors.

### Events log

You can view event logs in the `events_view` view in the linked dataset:

Filter this table:  Metadata field | Mode | Type | Description  
---|---|---|---  
`manifest.snapshotTime` | `NULLABLE` | `TIMESTAMP` | The time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339), when the snapshot of the events is refreshed.  
`manifest.viewName` | `NULLABLE` | `STRING` | The name of the view that refreshes.  
`manifest.location` | `NULLABLE` | `STRING` | The source location of the data that refreshes.  
`globalManifest.snapshotTime` | `NULLABLE` | `TIMESTAMP` | The ingestion completion time, in [RFC 3339 format](https://tools.ietf.org/html/rfc3339), for the bucket and object attributes tables across all source locations.  
`eventTime` | `NULLABLE` | `TIMESTAMP` | The time the event occurred.  
`eventCode` | `NULLABLE` | `STRING` | The event code associated with the corresponding entry. The `eventCode` values are as follows: 

  * `eventCode 1` indicates that the `manifest.viewName` view is refreshed with all entries for the source location `(manifest.location)` within the snapshot `(manifest.snapshotTime)`.
  * `eventCode 2` indicates that the dataset is refreshed with the bucket and object entries for all source locations. The refresh occurs within the snapshot `(globalManifest.snapshotTime)`.
  * `eventCode 3` refers to the activity data views being refreshed with all entries for the source location `(manifest.location)` within the log window.

  
  
### Error codes

You can view error codes in the `error_attributes_view` table in the linked dataset:

Filter this table:  Metadata field | Mode | Type | Description  
---|---|---|---  
`errorCode` | `NULLABLE` | `INTEGER` | The error code associated with this entry. For a list of valid values and how to resolve these errors, see Troubleshoot dataset errors.  
`errorSource` | `NULLABLE` | `STRING` | The source of the error. Valid value: `CONFIGURATION_PREPROCESSING`.  
`errorTime` | `NULLABLE` | `TIMESTAMP` | The time the error occurs.  
`sourceGcsLocation` | `NULLABLE` | `STRING` | The source Cloud Storage location of the error. For projects, this field is null because projects are not associated with a location.  
`bucketErrorRecord.bucketName` | `NULLABLE` | `STRING` | The name of the bucket involved in the error. You can use this information to debug a bucket error.  
`bucketErrorRecord.serviceAccount` | `NULLABLE` | `STRING` | The service account that needs permission to ingest objects from the bucket. You can use this information to debug a bucket error.  
`projectErrorRecord.projectNumber` | `NULLABLE` | `INTEGER` | The number of the project involved in the error. You can use this information to debug a project error.  
`projectErrorRecord.organizationName` | `NULLABLE` | `STRING` | The name of the organization the project must belong to for processing. A value of `0` indicates that the project is not in the organization. You can use this information to debug a project error.  
  
#### Troubleshoot dataset errors

To troubleshoot the snapshot processing errors that are logged in the `error_attributes_view` view in the linked dataset, see the following table:

**Error code** | **Error case** | **Error message** | **Troubleshooting**  
---|---|---|---  
1 | Source project doesn't belong to the organization | Source project `projectErrorRecord.projectNumber` doesn't belong to the organization `projectErrorRecord.organizationName`. | Add source project `projectErrorRecord.projectNumber` to organization `projectErrorRecord.organizationName`. For instructions to migrate a project between organizations, see [Migrate projects between organizations](https://docs.cloud.google.com/resource-manager/docs/project-migration).  
2 | Bucket authorization error | Permission denied for ingesting objects for bucket `bucketErrorRecord.bucketName`. | Give service account `bucketErrorRecord.serviceAccount` Identity and Access Management (IAM) permissions to allow ingestion of objects for bucket `bucketErrorRecord.bucketName`. For more information, see [Grant required permissions to the service agent](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#grant-permissions-to-service-account).  
3 | Destination project doesn't belong to the organization | Destination project `projectErrorRecord.projectNumber` not in organization `projectErrorRecord.organizationName`. | Add destination project `projectErrorRecord.projectNumber` to organization `projectErrorRecord.organizationName`. For instructions to migrate a project between organizations, see [Migrate projects between organizations](https://docs.cloud.google.com/resource-manager/docs/project-migration).  
4 | Source project doesn't have Storage Intelligence configured. | Source project `projectErrorRecord.projectNumber` doesn't have Storage Intelligence configured. | Configure Storage Intelligence for the source project `projectErrorRecord.projectNumber`. For more information, see [Configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence).  
5 | Bucket doesn't have Storage Intelligence configured. | Bucket `bucketErrorRecord.bucketName` doesn't have Storage Intelligence configured. | Configure Storage Intelligence for the bucket `bucketErrorRecord.bucketName`. For more information, see [Configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence).  
6 | Bucket access authentication error | `ACTIVITY_BUCKET_ACCESS_AUTHORIZATION_ERROR` for bucket `bucketErrorRecord.bucketName`. | Grant service account `bucketErrorRecord.serviceAccount` Identity and Access Management (IAM) permissions to allow ingestion of activity for bucket `bucketErrorRecord.bucketName`. For more information, see [Grant required permissions to the service agent](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#grant-permissions-to-service-account).  
  
## What's next

  * [Configure Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/configure-datasets).
  * [Manage Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/manage-datasets).
  * [Run SQL queries on the datasets in BigQuery](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * [Learn about BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
