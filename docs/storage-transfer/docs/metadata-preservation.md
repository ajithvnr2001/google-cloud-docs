---
url: https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation/
title: Metadata preservation \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:02.940989+00:00
---

# Metadata preservation  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Metadata preservation Stay organized with collections  Save and categorize content based on your preferences. 

This document describes metadata that is preserved when you use Storage Transfer Service to transfer data between various sources and destinations.

## Overview

Storage Transfer Service preserves the following metadata:

  * User-created [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata) for transfers that originate from Cloud Storage, Amazon S3, or Microsoft Azure Blob Storage is preserved.

  * Transfers between Cloud Storage buckets can optionally preserve object ACLs, customer-managed encryption keys, storage class, object creation time (as the value of a `customTime` field), and temporary holds.

  * For transfers from any source to a Cloud Storage bucket, the object's storage class in the destination bucket can be set to any supported class as part of the transfer.

  * File size and last modified time (`mtime`) are preserved for transfers that originate from POSIX file systems. `mtime` is not preserved for folders.

  * Optionally, symlinks, numeric UID, numeric GID, and numeric MODE can be preserved for transfers to and from POSIX file systems.

  * For transfers between file systems only, if UID, GID, or MODE are preserved, that metadata is also preserved for folders. Cloud Storage recreates folders on the destination file system and restores UID, GID, and/or MODE. This includes empty folders. `mtime` is not preserved.

Folder-level metadata is not preserved if the transfer is by [manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).




Metadata fields that are not explicitly mentioned in this document are not preserved.

## Metadata preservation behavior

The following sections list metadata examples from different source storage systems and how Storage Transfer Service preserves metadata from each. For an exhaustive list of metadata, refer to the source storage system's documentation.

### Amazon S3 or S3-compatible storage to Cloud Storage

Metadata example | Preservation behavior  
---|---  
Amazon S3 fixed-key metadata fields, such as: `Cache-Control`, `Content-Disposition`, and `Content-Type`.  | Preserved as fixed-key metadata.  
Amazon S3 user-defined metadata, formatted as key:value pairs. For more information, see the [ User-defined object metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata) section of [ Object key and metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html).  |  Preserved as a custom metadata field in destination Cloud Storage objects, which you can edit later or remove.  
`ETag` |  Preserved as a custom metadata field with the key `x-goog-source-etag`, which you can edit later or remove.   
Object size.  |  Preserved as `size`.   
Amazon S3 access control lists (ACLs). For a complete list, see the [Condition Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#acl-specific-condition-keys) section of [ Access Control List (ACL) Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html). | Not preserved.  
Amazon S3 object tags, defined by you as key-value pairs. For more information, see [ Object Tags](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-object-tags.html). | Not preserved.  
Amazon S3 system-defined metadata, except for `ETag` and object size. For a complete list, see the [System-defined object metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata) section of [Object key and metadata](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html). |  Not preserved. Timestamp metadata from the source isn't preserved. Creation time, `timeCreated`, reflects the time that an object is created in Cloud Storage. Similarly, `updated` reflects the time that metadata for an object is modified in Cloud Storage.   
Storage class |  There are multiple options for setting storage class during a transfer.

  * Set each object's storage class to that of the destination bucket. This is the default behavior.
  * Set a specific storage class on all objects being transferred.

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
  
### Microsoft Azure Storage to Cloud Storage

Metadata example | Preservation behavior  
---|---  
Microsoft Azure Storage fixed-key metadata fields, such as: `Cache-Control`, `Content-Disposition`, and `Content-Type`.  |  Preserved as fixed-key metadata.   
Microsoft Azure Storage user-defined metadata, formatted as key:value pairs. For more information, see [ Settings and retrieving properties and metadata for Blob service resources ](https://docs.microsoft.com/en-us/rest/api/storageservices/setting-and-retrieving-properties-and-metadata-for-blob-resources).  |  Preserved as a custom metadata field in destination Cloud Storage objects, which you can edit later or remove.   
`ETag` |  Preserved as a custom metadata field with the key `x-goog-source-etag`, which you can edit later or remove.   
Object size.  |  Preserved as `size`.   
POSIX file system permissions supported by Azure Data Lake Storage (ADLS) Gen 2.  |  Not preserved.   
Microsoft Azure Storage access control, specifically `x-ms-blob-public-access`. For more information, see the [ Response Headers ](https://docs.microsoft.com/en-us/rest/api/storageservices/get-container-acl#response-headers) section of [ Get Container ACL ](https://docs.microsoft.com/en-us/rest/api/storageservices/get-container-acl).  |  Not preserved.   
Microsoft Azure Storage index tags. For more information, see [ Manage and find Azure Blob data with blob index tags ](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-manage-find-blobs).  |  Not preserved.   
Microsoft Azure Storage timestamp metadata, such as: `Last-Modified`, `x-ms-creation-time`, `x-ms-version`, `x-ms-request-server-encrypted`, and `x-ms-encryption-scope`. For more information, see [ Set Blob Metadata ](https://docs.microsoft.com/en-us/rest/api/storageservices/set-blob-metadata).  |  Not preserved. Timestamp metadata from the source isn't preserved. Creation time, `timeCreated`, reflects the time that an object is created in Cloud Storage. Similarly, `updated` reflects the time that metadata for an object is modified in Cloud Storage.   
Storage class |  There are multiple options for setting storage class during a transfer.

  * Set each object's storage class to that of the destination bucket. This is the default behavior.
  * Set a specific storage class on all objects being transferred.

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
  
### Transfers between Cloud Storage buckets

Metadata example | Preservation behavior  
---|---  
Cloud Storage fixed-key metadata fields, such as: `Cache-Control`, `Content-Disposition`, and `Content-Type`.  For more information, see [Object metadata](https://docs.cloud.google.com/storage/docs/metadata) |  Preserved as fixed-key metadata.  
Cloud Storage user-defined metadata, formatted as key:value pairs. For more information, see [Custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata).  |  Preserved as a custom metadata field in destination Cloud Storage objects, which you can edit later or remove.   
Object size  |  Preserved as `size`.   
[Object generation](https://docs.cloud.google.com/storage/docs/metadata#generation-number) |  Preserved as a custom metadata field with the key `x-goog-reserved-source-generation`, which you can edit later or remove.   
Object holds |  Event-based holds are not preserved. If the destination bucket has the [default event-based hold property](https://docs.cloud.google.com/storage/docs/object-holds#default-holds) enabled, an event-based hold is applied to transferred objects. Temporary holds are preserved by default. To discard temporary holds during the transfer, set the `temporaryHold` field of the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) object to `TEMPORARY_HOLD_SKIP`.  
Access Control Lists (ACLs) |  ACLs can optionally be preserved. See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details. When preserving ACLs be careful to avoid creating [inaccessible objects](https://docs.cloud.google.com/storage/docs/access-control#best-practices). For more information, see the Cloud Storage [Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/lists) documentation.  
Storage class |  There are multiple options for setting storage class during a transfer.

  * Set each object's storage class to that of the destination bucket. This is the default behavior.
  * Preserve the source object's storage class.
  * Set a specific storage class on all objects being transferred.

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
Customer-managed encryption key  |  If a [ customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) (CMEK) is being used on an object, the object can optionally use the same key when it is written to the destination bucket. The default behavior is to write the object to the destination bucket using the bucket's encryption method. When preserving the original CMEK, be aware of the following limitations:

  * The destination bucket must be in the same location as the CMEK.
  * If the destination bucket is in another project, you must [ add the destination project's Cloud Storage service account to the key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access).

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
Timestamp metadata  |  `timeCreated` can optionally be preserved. The preserved value is stored in the `customTime` field of the transferred object in Cloud Storage. See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  `updated` metadata is not preserved.   
Other Cloud Storage non-editable metadata, such as `etag` and `componentCount`.  |  Not Preserved.   
  
For a list of metadata in Cloud Storage, see [Objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects).

### URL list transfer to Cloud Storage

For more information about URL lists, see [Creating a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list).

Metadata example | Preservation behavior  
---|---  
Fixed-key metadata fields, such as: `Cache-Control`, `Content-Disposition`, and `Content-Type`.  |  Preserved as editable metadata.   
`Content-Length` and `MD5` |  Preserved as non-editable metadata.  If the source doesn't provide an `MD5` hash value, then we don't preserve a value.  This preservation behavior is specific to `Content-Length` and `MD5`. Any other non-editable metadata not listed is not preserved.   
Timestamp metadata, such as: Creation time, modified time, and other source-specific metadata.  |  Not preserved.  Timestamp metadata from the source isn't preserved. Creation time, `timeCreated`, reflects the time that an object is created in Cloud Storage. Similarly, `updated` reflects the time that metadata for an object is modified in Cloud Storage.   
Storage class |  There are multiple options for setting storage class during a transfer.

  * Set each object's storage class to that of the destination bucket. This is the default behavior.
  * Set a specific storage class on all objects being transferred.

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
  
### POSIX file system transfers

When transferring files from POSIX file systems, Storage Transfer Service can optionally preserve certain attributes as custom metadata. If these files are later written back to a file system, Storage Transfer Service can convert the preserved metadata back to POSIX attributes.

Metadata example | Preservation behavior  
---|---  
Modified time (`mtime`)  |  Preserved. `mtime` is preserved as custom metadata with the key `goog-reserved-file-mtime`.  
File size |  Preserved. File size is preserved as `size`.  
Numeric UID  
Numeric GID  
Numeric MODE  
Symbolic links | Optional. Preservation behavior is specified with the [`metadataOptions`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) object. See Preserving optional POSIX metadata for details. Default behavior is to not preserve any metadata.  
Folder metadata | Folder-level metadata is only preserved for transfers between file systems. The transfer's UID, GID, and MODE preservation settings apply to files and folders for these transfers. `mtime` is not preserved for folders. `mtime` is set to the create time of the folder on the destination file system. Folder metadata is not preserved for [manifest transfers](https://docs.cloud.google.com/storage-transfer/docs/manifest).  
Storage class |  There are multiple options for setting storage class during a transfer.

  * Set each object's storage class to that of the destination bucket. This is the default behavior.
  * Set a specific storage class on all objects being transferred.

See the [ metadataOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) reference documentation for details.  
  
### Preserving optional POSIX metadata

To preserve one or more of numeric UID, numeric GID, numeric MODE, and symbolic links, specify a [ `metadataOptions`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferOptions#MetadataOptions) object in the body of your transfer job.

These options apply to both POSIX-to-Cloud Storage transfers and Cloud Storage-to-POSIX transfers. For the latter, the metadata must have been preserved when files were initially transferred to Cloud Storage.
    
    
    {
      "description": "metadata-example",
      "projectId": "example-project-id"
      "transferSpec": {
        ...
        "transferOptions": {
          "metadataOptions": {
            "gid":     "GID_NUMBER",       # Default is "GID_SKIP"
            "uid":     "UID_NUMBER",       # Default is "UID_SKIP"
            "mode":    "MODE_PRESERVE",    # Default is "MODE_SKIP"
            "symlink": "SYMLINK_PRESERVE"  # Default is "SYMLINK_SKIP"
          }
        }
      }
    }
    

#### POSIX to Cloud Storage

Preserved metadata is stored in Cloud Storage as custom metadata key:value pairs.

  * Numeric GID is stored as `goog-reserved-posix-gid`.
  * Numeric UID is stored as `goog-reserved-posix-uid`.
  * Numeric MODE is stored as `goog-reserved-posix-mode`.



For symbolic links, Storage Transfer Service preserves the target link as an object in Cloud Storage with the following qualities:

  * Object key is composed of the destination prefix plus the path to the symlink, relative to the `root_directory`.
  * Object metadata: 
    * Any symlink metadata is preserved as Cloud Storage object metadata.
    * A custom metadata entry is made: `goog-reserved-file-is-symlink:true`.
  * The object content is the target of the symlink. For example, for a symlink `sym-> dir1/target`, the object's content is "dir1/target".



Storage Transfer Service does not validate the link or copy the target file.

#### Cloud Storage to POSIX

If metadata is preserved when files are transferred to Cloud Storage, that metadata can be written back to the files when they are [transferred back to a POSIX file system](https://docs.cloud.google.com/storage-transfer/docs/download-from-cloud-storage).

If a metadata option is set to preserve, Storage Transfer Service takes the following actions:

  * Symbolic links: Storage Transfer Service creates a symlink file pointing to the target link. If the target file does not exist, the symlink will be broken.
  * GID, UID, and MODE: the values stored in Cloud Storage metadata are written back to the file.



#### POSIX to POSIX

Transfers between file systems can optionally preserve GID, UID, and MODE for files and folders.

Last modified time is saved for files, but not for folders. `mtime` is set to the create time of the folder on the destination file system.

Storage Transfer Service saves folder metadata by creating 0-byte folder objects in the intermediate bucket, then copying that metadata back to the folder on the destination file system. For this reason, the number of objects created in the intermediate bucket may be greater than the number of files being transferred.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
