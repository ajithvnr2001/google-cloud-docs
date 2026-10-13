---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk
title: Class Disk (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:11.427650+00:00
---

# Class Disk (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Disk (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    Disk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Persistent Disk resource.

Google Compute Engine has two Disk resources:

  * `Zonal </compute/docs/reference/rest/v1/disks>`__
  * `Regional </compute/docs/reference/rest/v1/regionDisks>`__



Persistent disks are required for running your VM instances. Create both boot and non-boot (data) persistent disks. For more information, read Persistent Disks. For more storage options, read Storage options.

The disks resource represents a zonal persistent disk. For more information, readZonal persistent disks.

The regionDisks resource represents a regional persistent disk. For more information, read Regional resources.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`access_mode` |  `str`   
The access mode of the disk. :: \- READ_WRITE_SINGLE: The default AccessMode, means the disk can be attached to single instance in RW mode. \- READ_WRITE_MANY: The AccessMode means the disk can be attached to multiple instances in RW mode. \- READ_ONLY_MANY: The AccessMode means the disk can be attached to multiple instances in RO mode. The AccessMode is only valid for Hyperdisk disk types. Check the AccessMode enum for the list of possible values. This field is a member of `oneof`_ `_access_mode`.   
`architecture` |  `str`   
The architecture of the disk. Valid values are ARM64 or X86_64. Check the Architecture enum for the list of possible values. This field is a member of `oneof`_ `_architecture`.   
`async_primary_disk` |  `[google.cloud.compute_v1.types.DiskAsyncReplication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskAsyncReplication)`   
Disk asynchronously replicated into this disk. This field is a member of `oneof`_ `_async_primary_disk`.   
`async_secondary_disks` |  `MutableMapping[str, [google.cloud.compute_v1.types.DiskAsyncReplicationList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskAsyncReplicationList)]`   
Output only. [Output Only] A list of disks this disk is asynchronously replicated to.   
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`disk_encryption_key` |  `[google.cloud.compute_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey)`   
Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key. Encryption keys do not protect access to metadata of the disk. After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later. For example, to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine. After you encrypt a disk with a customer-managed key, thediskEncryptionKey.kmsKeyName is set to a key *version* name once the disk is created. The disk is encrypted with this version of the key. In the response, diskEncryptionKey.kmsKeyName appears in the following format: "diskEncryptionKey.kmsKeyName": "projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version If you do not provide an encryption key when creating the disk, then the disk is encrypted using an automatically generated key and you don't need to provide a key to use the disk later. This field is a member of `oneof`_ `_disk_encryption_key`.   
`enable_confidential_compute` |  `bool`   
Whether this disk is using confidential compute mode. This field is a member of `oneof`_ `_enable_confidential_compute`.   
`guest_os_features` |  `MutableSequence[[google.cloud.compute_v1.types.GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GuestOsFeature)]`   
A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. Always compute#disk for disks. This field is a member of `oneof`_ `_kind`.   
`label_fingerprint` |  `str`   
A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a disk. This field is a member of `oneof`_ `_label_fingerprint`.   
`labels` |  `MutableMapping[str, str]`   
Labels to apply to this disk. These can be later modified by the setLabels method.   
`last_attach_timestamp` |  `str`   
Output only. [Output Only] Last attach timestamp inRFC3339 text format. This field is a member of `oneof`_ `_last_attach_timestamp`.   
`last_detach_timestamp` |  `str`   
Output only. [Output Only] Last detach timestamp inRFC3339 text format. This field is a member of `oneof`_ `_last_detach_timestamp`.   
`license_codes` |  `MutableSequence[int]`   
Integer license codes indicating which licenses are attached to this disk.   
`licenses` |  `MutableSequence[str]`   
A list of publicly visible licenses. Reserved for Google's use.   
`location_hint` |  `str`   
An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. This field is a member of `oneof`_ `_location_hint`.   
`name` |  `str`   
Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`options` |  `str`   
Internal use only. This field is a member of `oneof`_ `_options`.   
`params` |  `[google.cloud.compute_v1.types.DiskParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskParams)`   
Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. This field is a member of `oneof`_ `_params`.   
`physical_block_size_bytes` |  `int`   
Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. This field is a member of `oneof`_ `_physical_block_size_bytes`.   
`provisioned_iops` |  `int`   
Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see theExtreme persistent disk documentation. This field is a member of `oneof`_ `_provisioned_iops`.   
`provisioned_throughput` |  `int`   
Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. This field is a member of `oneof`_ `_provisioned_throughput`.   
`region` |  `str`   
Output only. [Output Only] URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. This field is a member of `oneof`_ `_region`.   
`replica_zones` |  `MutableSequence[str]`   
URLs of the zones where the disk should be replicated to. Only applicable for regional resources.   
`resource_policies` |  `MutableSequence[str]`   
Resource policies applied to this disk for automatic snapshot creations.   
`resource_status` |  `[google.cloud.compute_v1.types.DiskResourceStatus](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskResourceStatus)`   
Output only. [Output Only] Status information for the disk resource. This field is a member of `oneof`_ `_resource_status`.   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzi`.   
`satisfies_pzs` |  `bool`   
Output only. [Output Only] Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzs`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined fully-qualified URL for this resource. This field is a member of `oneof`_ `_self_link`.   
`size_gb` |  `int`   
Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using thesourceImage, sourceSnapshot, orsourceDisk parameter, or specify it alone to create an empty persistent disk. If you specify this field along with a source, the value ofsizeGb must not be less than the size of the source. Acceptable values are greater than 0. This field is a member of `oneof`_ `_size_gb`.   
`source_consistency_group_policy` |  `str`   
Output only. [Output Only] URL of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. This field is a member of `oneof`_ `_source_consistency_group_policy`.   
`source_consistency_group_policy_id` |  `str`   
Output only. [Output Only] ID of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. This field is a member of `oneof`_ `_source_consistency_group_policy_id`.   
`source_disk` |  `str`   
The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: \- https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk \- https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk \- projects/project/zones/zone/disks/disk \- projects/project/regions/region/disks/disk \- zones/zone/disks/disk \- regions/region/disks/disk This field is a member of `oneof`_ `_source_disk`.   
`source_disk_id` |  `str`   
Output only. [Output Only] The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used. This field is a member of `oneof`_ `_source_disk_id`.   
`source_image` |  `str`   
The source image used to create this disk. If the source image is deleted, this field will not be set. To create a disk with one of the public operating system images, specify the image by its family name. For example, specifyfamily/debian-9 to use the latest Debian 9 image: projects/debian-cloud/global/images/family/debian-9 Alternatively, use a specific version of a public operating system image: projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD To create a disk with a custom image that you created, specify the image name in the following format: global/images/my-custom-image You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name: global/images/family/my-image-family This field is a member of `oneof`_ `_source_image`.   
`source_image_encryption_key` |  `[google.cloud.compute_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey)`   
Thecustomer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. This field is a member of `oneof`_ `_source_image_encryption_key`.   
`source_image_id` |  `str`   
Output only. [Output Only] The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used. This field is a member of `oneof`_ `_source_image_id`.   
`source_instant_snapshot` |  `str`   
The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: \- https://www.googleapis.com/compute/v1/projects/project/zones/zone/instantSnapshots/instantSnapshot \- projects/project/zones/zone/instantSnapshots/instantSnapshot \- zones/zone/instantSnapshots/instantSnapshot This field is a member of `oneof`_ `_source_instant_snapshot`.   
`source_instant_snapshot_id` |  `str`   
Output only. [Output Only] The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used. This field is a member of `oneof`_ `_source_instant_snapshot_id`.   
`source_snapshot` |  `str`   
The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: \- https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot \- projects/project/global/snapshots/snapshot \- global/snapshots/snapshot This field is a member of `oneof`_ `_source_snapshot`.   
`source_snapshot_encryption_key` |  `[google.cloud.compute_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey)`   
Thecustomer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. This field is a member of `oneof`_ `_source_snapshot_encryption_key`.   
`source_snapshot_id` |  `str`   
Output only. [Output Only] The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used. This field is a member of `oneof`_ `_source_snapshot_id`.   
`source_storage_object` |  `str`   
The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead. This field is a member of `oneof`_ `_source_storage_object`.   
`status` |  `str`   
Output only. [Output Only] The status of disk creation. :: \- CREATING: Disk is provisioning. \- RESTORING: Source data is being copied into the disk. \- FAILED: Disk creation failed. \- READY: Disk is ready for use. \- DELETING: Disk is deleting. Check the Status enum for the list of possible values. This field is a member of `oneof`_ `_status`.   
`storage_pool` |  `str`   
The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: \- https://www.googleapis.com/compute/v1/projects/project/zones/zone/storagePools/storagePool \- projects/project/zones/zone/storagePools/storagePool \- zones/zone/storagePools/storagePool This field is a member of `oneof`_ `_storage_pool`.   
`type_` |  `str`   
URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example:projects/project/zones/zone/diskTypes/pd-ssd. See Persistent disk types. This field is a member of `oneof`_ `_type`.   
`users` |  `MutableSequence[str]`   
Output only. [Output Only] Links to the users of the disk (attached instances) in form:projects/project/zones/zone/instances/instance   
`zone` |  `str`   
Output only. [Output Only] URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. This field is a member of `oneof`_ `_zone`.   
  
## Classes 

### AccessMode
    
    
    AccessMode(value)

The access mode of the disk.

::
    
    
     - READ_WRITE_SINGLE: The default AccessMode, means the
     disk can be attached to single instance in RW mode.
     - READ_WRITE_MANY: The AccessMode means the disk can be
     attached to multiple instances in RW mode.
     - READ_ONLY_MANY: The AccessMode means the disk can be
     attached to multiple instances in RO mode.
    

The AccessMode is only valid for Hyperdisk disk types.

### Architecture
    
    
    Architecture(value)

The architecture of the disk. Valid values are ARM64 or X86_64.

### AsyncSecondaryDisksEntry
    
    
    AsyncSecondaryDisksEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### Status
    
    
    Status(value)

Output only. [Output Only] The status of disk creation.

::
    
    
     - CREATING: Disk is provisioning.
     - RESTORING: Source data is being copied into the
     disk.
     - FAILED: Disk creation failed.
     - READY: Disk is ready for use.
     - DELETING: Disk is deleting.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
