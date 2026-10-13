---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Disk/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Disk (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:05.788759+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Disk (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Disk (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::Disk.

Represents a Persistent Disk resource.

Google Compute Engine has two Disk resources:

  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks)



Persistent disks are required for running your VM instances. Create both boot and non-boot (data) persistent disks. For more information, read Persistent Disks. For more storage options, read Storage options.

The disks resource represents a zonal persistent disk. For more information, readZonal persistent disks.

The regionDisks resource represents a regional persistent disk. For more information, read Regional resources.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_mode
    
    
    def access_mode() -> ::String

**Returns**

  * (::String) — The access mode of the disk.
        
        - READ_WRITE_SINGLE: The default AccessMode, means the
         disk can be attached to single instance in RW mode.
         - READ_WRITE_MANY: The AccessMode means the disk can be
         attached to multiple instances in RW mode.
         - READ_ONLY_MANY: The AccessMode means the disk can be
         attached to multiple instances in RO mode.
        

The AccessMode is only valid for Hyperdisk disk types. Check the AccessMode enum for the list of possible values. 




### #access_mode=
    
    
    def access_mode=(value) -> ::String

**Parameter**

  * **value** (::String) — The access mode of the disk.
        
        - READ_WRITE_SINGLE: The default AccessMode, means the
         disk can be attached to single instance in RW mode.
         - READ_WRITE_MANY: The AccessMode means the disk can be
         attached to multiple instances in RW mode.
         - READ_ONLY_MANY: The AccessMode means the disk can be
         attached to multiple instances in RO mode.
        

The AccessMode is only valid for Hyperdisk disk types. Check the AccessMode enum for the list of possible values. 




**Returns**

  * (::String) — The access mode of the disk.
        
        - READ_WRITE_SINGLE: The default AccessMode, means the
         disk can be attached to single instance in RW mode.
         - READ_WRITE_MANY: The AccessMode means the disk can be
         attached to multiple instances in RW mode.
         - READ_ONLY_MANY: The AccessMode means the disk can be
         attached to multiple instances in RO mode.
        

The AccessMode is only valid for Hyperdisk disk types. Check the AccessMode enum for the list of possible values. 




### #architecture
    
    
    def architecture() -> ::String

**Returns**

  * (::String) — The architecture of the disk. Valid values are ARM64 or X86_64. Check the Architecture enum for the list of possible values. 



### #architecture=
    
    
    def architecture=(value) -> ::String

**Parameter**

  * **value** (::String) — The architecture of the disk. Valid values are ARM64 or X86_64. Check the Architecture enum for the list of possible values. 



**Returns**

  * (::String) — The architecture of the disk. Valid values are ARM64 or X86_64. Check the Architecture enum for the list of possible values. 



### #async_primary_disk
    
    
    def async_primary_disk() -> ::Google::Cloud::Compute::V1::DiskAsyncReplication

**Returns**

  * ([::Google::Cloud::Compute::V1::DiskAsyncReplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskAsyncReplication)) — Disk asynchronously replicated into this disk. 



### #async_primary_disk=
    
    
    def async_primary_disk=(value) -> ::Google::Cloud::Compute::V1::DiskAsyncReplication

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::DiskAsyncReplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskAsyncReplication)) — Disk asynchronously replicated into this disk. 



**Returns**

  * ([::Google::Cloud::Compute::V1::DiskAsyncReplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskAsyncReplication)) — Disk asynchronously replicated into this disk. 



### #async_secondary_disks
    
    
    def async_secondary_disks() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::DiskAsyncReplicationList}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::DiskAsyncReplicationList}) — Output only. [Output Only] A list of disks this disk is asynchronously replicated to. 



### #async_secondary_disks=
    
    
    def async_secondary_disks=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::DiskAsyncReplicationList}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::DiskAsyncReplicationList}) — Output only. [Output Only] A list of disks this disk is asynchronously replicated to. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::DiskAsyncReplicationList}) — Output only. [Output Only] A list of disks this disk is asynchronously replicated to. 



### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional description of this resource. Provide this property when you create the resource. 



**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #disk_encryption_key
    
    
    def disk_encryption_key() -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key.

Encryption keys do not protect access to metadata of the disk.

After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later. For example, to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine.

After you encrypt a disk with a customer-managed key, thediskEncryptionKey.kmsKeyName is set to a key _version_ name once the disk is created. The disk is encrypted with this version of the key. In the response, diskEncryptionKey.kmsKeyName appears in the following format:

"diskEncryptionKey.kmsKeyName": "projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version

If you do not provide an encryption key when creating the disk, then the disk is encrypted using an automatically generated key and you don't need to provide a key to use the disk later. 




### #disk_encryption_key=
    
    
    def disk_encryption_key=(value) -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key.

Encryption keys do not protect access to metadata of the disk.

After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later. For example, to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine.

After you encrypt a disk with a customer-managed key, thediskEncryptionKey.kmsKeyName is set to a key _version_ name once the disk is created. The disk is encrypted with this version of the key. In the response, diskEncryptionKey.kmsKeyName appears in the following format:

"diskEncryptionKey.kmsKeyName": "projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version

If you do not provide an encryption key when creating the disk, then the disk is encrypted using an automatically generated key and you don't need to provide a key to use the disk later. 




**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key.

Encryption keys do not protect access to metadata of the disk.

After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later. For example, to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine.

After you encrypt a disk with a customer-managed key, thediskEncryptionKey.kmsKeyName is set to a key _version_ name once the disk is created. The disk is encrypted with this version of the key. In the response, diskEncryptionKey.kmsKeyName appears in the following format:

"diskEncryptionKey.kmsKeyName": "projects/kms_project_id/locations/region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version

If you do not provide an encryption key when creating the disk, then the disk is encrypted using an automatically generated key and you don't need to provide a key to use the disk later. 




### #enable_confidential_compute
    
    
    def enable_confidential_compute() -> ::Boolean

**Returns**

  * (::Boolean) — Whether this disk is using confidential compute mode. 



### #enable_confidential_compute=
    
    
    def enable_confidential_compute=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether this disk is using confidential compute mode. 



**Returns**

  * (::Boolean) — Whether this disk is using confidential compute mode. 



### #guest_os_features
    
    
    def guest_os_features() -> ::Array<::Google::Cloud::Compute::V1::GuestOsFeature>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GuestOsFeature)>) — A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options. 



### #guest_os_features=
    
    
    def guest_os_features=(value) -> ::Array<::Google::Cloud::Compute::V1::GuestOsFeature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GuestOsFeature)>) — A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GuestOsFeature)>) — A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#disk for disks. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Always compute#disk for disks. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#disk for disks. 



### #label_fingerprint
    
    
    def label_fingerprint() -> ::String

**Returns**

  * (::String) — A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve a disk. 




### #label_fingerprint=
    
    
    def label_fingerprint=(value) -> ::String

**Parameter**

  * **value** (::String) — A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve a disk. 




**Returns**

  * (::String) — A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve a disk. 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this disk. These can be later modified by the setLabels method. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this disk. These can be later modified by the setLabels method. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to this disk. These can be later modified by the setLabels method. 



### #last_attach_timestamp
    
    
    def last_attach_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Last attach timestamp inRFC3339 text format. 



### #last_attach_timestamp=
    
    
    def last_attach_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Last attach timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Last attach timestamp inRFC3339 text format. 



### #last_detach_timestamp
    
    
    def last_detach_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Last detach timestamp inRFC3339 text format. 



### #last_detach_timestamp=
    
    
    def last_detach_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Last detach timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Last detach timestamp inRFC3339 text format. 



### #license_codes
    
    
    def license_codes() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — Integer license codes indicating which licenses are attached to this disk. 



### #license_codes=
    
    
    def license_codes=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — Integer license codes indicating which licenses are attached to this disk. 



**Returns**

  * (::Array<::Integer>) — Integer license codes indicating which licenses are attached to this disk. 



### #licenses
    
    
    def licenses() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of publicly visible licenses. Reserved for Google's use. 



### #licenses=
    
    
    def licenses=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of publicly visible licenses. Reserved for Google's use. 



**Returns**

  * (::Array<::String>) — A list of publicly visible licenses. Reserved for Google's use. 



### #location_hint
    
    
    def location_hint() -> ::String

**Returns**

  * (::String) — An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. 



### #location_hint=
    
    
    def location_hint=(value) -> ::String

**Parameter**

  * **value** (::String) — An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. 



**Returns**

  * (::String) — An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



**Returns**

  * (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #options
    
    
    def options() -> ::String

**Returns**

  * (::String) — Internal use only. 



### #options=
    
    
    def options=(value) -> ::String

**Parameter**

  * **value** (::String) — Internal use only. 



**Returns**

  * (::String) — Internal use only. 



### #params
    
    
    def params() -> ::Google::Cloud::Compute::V1::DiskParams

**Returns**

  * ([::Google::Cloud::Compute::V1::DiskParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



### #params=
    
    
    def params=(value) -> ::Google::Cloud::Compute::V1::DiskParams

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::DiskParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



**Returns**

  * ([::Google::Cloud::Compute::V1::DiskParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskParams)) — Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. 



### #physical_block_size_bytes
    
    
    def physical_block_size_bytes() -> ::Integer

**Returns**

  * (::Integer) — Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. 



### #physical_block_size_bytes=
    
    
    def physical_block_size_bytes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. 



**Returns**

  * (::Integer) — Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. 



### #provisioned_iops
    
    
    def provisioned_iops() -> ::Integer

**Returns**

  * (::Integer) — Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see theExtreme persistent disk documentation. 



### #provisioned_iops=
    
    
    def provisioned_iops=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see theExtreme persistent disk documentation. 



**Returns**

  * (::Integer) — Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see theExtreme persistent disk documentation. 



### #provisioned_throughput
    
    
    def provisioned_throughput() -> ::Integer

**Returns**

  * (::Integer) — Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. 



### #provisioned_throughput=
    
    
    def provisioned_throughput=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. 



**Returns**

  * (::Integer) — Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



**Returns**

  * (::String) — Output only. [Output Only] URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



### #replica_zones
    
    
    def replica_zones() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — URLs of the zones where the disk should be replicated to. Only applicable for regional resources. 



### #replica_zones=
    
    
    def replica_zones=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — URLs of the zones where the disk should be replicated to. Only applicable for regional resources. 



**Returns**

  * (::Array<::String>) — URLs of the zones where the disk should be replicated to. Only applicable for regional resources. 



### #resource_policies
    
    
    def resource_policies() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Resource policies applied to this disk for automatic snapshot creations. 



### #resource_policies=
    
    
    def resource_policies=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Resource policies applied to this disk for automatic snapshot creations. 



**Returns**

  * (::Array<::String>) — Resource policies applied to this disk for automatic snapshot creations. 



### #resource_status
    
    
    def resource_status() -> ::Google::Cloud::Compute::V1::DiskResourceStatus

**Returns**

  * ([::Google::Cloud::Compute::V1::DiskResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskResourceStatus)) — Output only. [Output Only] Status information for the disk resource. 



### #resource_status=
    
    
    def resource_status=(value) -> ::Google::Cloud::Compute::V1::DiskResourceStatus

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::DiskResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskResourceStatus)) — Output only. [Output Only] Status information for the disk resource. 



**Returns**

  * ([::Google::Cloud::Compute::V1::DiskResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskResourceStatus)) — Output only. [Output Only] Status information for the disk resource. 



### #satisfies_pzi
    
    
    def satisfies_pzi() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Reserved for future use. 



### #satisfies_pzi=
    
    
    def satisfies_pzi=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. Reserved for future use. 



**Returns**

  * (::Boolean) — Output only. Reserved for future use. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #satisfies_pzs=
    
    
    def satisfies_pzs=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. [Output Only] Reserved for future use. 



**Returns**

  * (::Boolean) — Output only. [Output Only] Reserved for future use. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #size_gb
    
    
    def size_gb() -> ::Integer

**Returns**

  * (::Integer) — Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using thesourceImage, sourceSnapshot, orsourceDisk parameter, or specify it alone to create an empty persistent disk.

If you specify this field along with a source, the value ofsizeGb must not be less than the size of the source. Acceptable values are greater than 0. 




### #size_gb=
    
    
    def size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using thesourceImage, sourceSnapshot, orsourceDisk parameter, or specify it alone to create an empty persistent disk.

If you specify this field along with a source, the value ofsizeGb must not be less than the size of the source. Acceptable values are greater than 0. 




**Returns**

  * (::Integer) — Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using thesourceImage, sourceSnapshot, orsourceDisk parameter, or specify it alone to create an empty persistent disk.

If you specify this field along with a source, the value ofsizeGb must not be less than the size of the source. Acceptable values are greater than 0. 




### #source_consistency_group_policy
    
    
    def source_consistency_group_policy() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] URL of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



### #source_consistency_group_policy=
    
    
    def source_consistency_group_policy=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] URL of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



**Returns**

  * (::String) — Output only. [Output Only] URL of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



### #source_consistency_group_policy_id
    
    
    def source_consistency_group_policy_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] ID of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



### #source_consistency_group_policy_id=
    
    
    def source_consistency_group_policy_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] ID of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



**Returns**

  * (::String) — Output only. [Output Only] ID of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group. 



### #source_disk
    
    
    def source_disk() -> ::String

**Returns**

  * (::String) — 

The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        -
           https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk
        
         -
           https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk
        
         -
           projects/project/zones/zone/disks/disk
        
         -
           projects/project/regions/region/disks/disk
        
         -
           zones/zone/disks/disk
        
         -
           regions/region/disks/disk
        




### #source_disk=
    
    
    def source_disk=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        -
           https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk
        
         -
           https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk
        
         -
           projects/project/zones/zone/disks/disk
        
         -
           projects/project/regions/region/disks/disk
        
         -
           zones/zone/disks/disk
        
         -
           regions/region/disks/disk
        




**Returns**

  * (::String) — 

The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        -
           https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk
        
         -
           https://www.googleapis.com/compute/v1/projects/project/regions/region/disks/disk
        
         -
           projects/project/zones/zone/disks/disk
        
         -
           projects/project/regions/region/disks/disk
        
         -
           zones/zone/disks/disk
        
         -
           regions/region/disks/disk
        




### #source_disk_id
    
    
    def source_disk_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used. 



### #source_disk_id=
    
    
    def source_disk_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used. 



**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used. 



### #source_image
    
    
    def source_image() -> ::String

**Returns**

  * (::String) — The source image used to create this disk. If the source image is deleted, this field will not be set.

To create a disk with one of the public operating system images, specify the image by its family name. For example, specifyfamily/debian-9 to use the latest Debian 9 image:

projects/debian-cloud/global/images/family/debian-9

Alternatively, use a specific version of a public operating system image:

projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD

To create a disk with a custom image that you created, specify the image name in the following format:

global/images/my-custom-image

You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name:

global/images/family/my-image-family 




### #source_image=
    
    
    def source_image=(value) -> ::String

**Parameter**

  * **value** (::String) — The source image used to create this disk. If the source image is deleted, this field will not be set.

To create a disk with one of the public operating system images, specify the image by its family name. For example, specifyfamily/debian-9 to use the latest Debian 9 image:

projects/debian-cloud/global/images/family/debian-9

Alternatively, use a specific version of a public operating system image:

projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD

To create a disk with a custom image that you created, specify the image name in the following format:

global/images/my-custom-image

You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name:

global/images/family/my-image-family 




**Returns**

  * (::String) — The source image used to create this disk. If the source image is deleted, this field will not be set.

To create a disk with one of the public operating system images, specify the image by its family name. For example, specifyfamily/debian-9 to use the latest Debian 9 image:

projects/debian-cloud/global/images/family/debian-9

Alternatively, use a specific version of a public operating system image:

projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD

To create a disk with a custom image that you created, specify the image name in the following format:

global/images/my-custom-image

You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name:

global/images/family/my-image-family 




### #source_image_encryption_key
    
    
    def source_image_encryption_key() -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. 



### #source_image_encryption_key=
    
    
    def source_image_encryption_key=(value) -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. 



**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key. 



### #source_image_id
    
    
    def source_image_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used. 



### #source_image_id=
    
    
    def source_image_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used. 



**Returns**

  * (::String) — Output only. [Output Only] The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used. 



### #source_instant_snapshot
    
    
    def source_instant_snapshot() -> ::String

**Returns**

  * (::String) — 

The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instantSnapshots/instantSnapshot
         - projects/project/zones/zone/instantSnapshots/instantSnapshot
        

    * zones/zone/instantSnapshots/instantSnapshot



### #source_instant_snapshot=
    
    
    def source_instant_snapshot=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instantSnapshots/instantSnapshot
         - projects/project/zones/zone/instantSnapshots/instantSnapshot
        

    * zones/zone/instantSnapshots/instantSnapshot



**Returns**

  * (::String) — 

The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instantSnapshots/instantSnapshot
         - projects/project/zones/zone/instantSnapshots/instantSnapshot
        

    * zones/zone/instantSnapshots/instantSnapshot



### #source_instant_snapshot_id
    
    
    def source_instant_snapshot_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used. 



### #source_instant_snapshot_id=
    
    
    def source_instant_snapshot_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used. 



**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used. 



### #source_snapshot
    
    
    def source_snapshot() -> ::String

**Returns**

  * (::String) — 

The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot
        

    * projects/project/global/snapshots/snapshot 
      * global/snapshots/snapshot



### #source_snapshot=
    
    
    def source_snapshot=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot
        

    * projects/project/global/snapshots/snapshot 
      * global/snapshots/snapshot



**Returns**

  * (::String) — 

The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot
        

    * projects/project/global/snapshots/snapshot 
      * global/snapshots/snapshot



### #source_snapshot_encryption_key
    
    
    def source_snapshot_encryption_key() -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. 



### #source_snapshot_encryption_key=
    
    
    def source_snapshot_encryption_key=(value) -> ::Google::Cloud::Compute::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. 



**Returns**

  * ([::Google::Cloud::Compute::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CustomerEncryptionKey)) — Thecustomer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key. 



### #source_snapshot_id
    
    
    def source_snapshot_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used. 



### #source_snapshot_id=
    
    
    def source_snapshot_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used. 



**Returns**

  * (::String) — Output only. [Output Only] The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used. 



### #source_storage_object
    
    
    def source_storage_object() -> ::String

**Returns**

  * (::String) — The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead. 



### #source_storage_object=
    
    
    def source_storage_object=(value) -> ::String

**Parameter**

  * **value** (::String) — The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead. 



**Returns**

  * (::String) — The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead. 



### #status
    
    
    def status() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The status of disk creation.
        
        - CREATING: Disk is provisioning.
         - RESTORING: Source data is being copied into the
         disk.
         - FAILED: Disk creation failed.
         - READY: Disk is ready for use.
         - DELETING: Disk is deleting.
        

Check the Status enum for the list of possible values. 




### #status=
    
    
    def status=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The status of disk creation.
        
        - CREATING: Disk is provisioning.
         - RESTORING: Source data is being copied into the
         disk.
         - FAILED: Disk creation failed.
         - READY: Disk is ready for use.
         - DELETING: Disk is deleting.
        

Check the Status enum for the list of possible values. 




**Returns**

  * (::String) — Output only. [Output Only] The status of disk creation.
        
        - CREATING: Disk is provisioning.
         - RESTORING: Source data is being copied into the
         disk.
         - FAILED: Disk creation failed.
         - READY: Disk is ready for use.
         - DELETING: Disk is deleting.
        

Check the Status enum for the list of possible values. 




### #storage_pool
    
    
    def storage_pool() -> ::String

**Returns**

  * (::String) — 

The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/storagePools/storagePool
         - projects/project/zones/zone/storagePools/storagePool
        

    * zones/zone/storagePools/storagePool



### #storage_pool=
    
    
    def storage_pool=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/storagePools/storagePool
         - projects/project/zones/zone/storagePools/storagePool
        

    * zones/zone/storagePools/storagePool



**Returns**

  * (::String) — 

The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/zones/zone/storagePools/storagePool
         - projects/project/zones/zone/storagePools/storagePool
        

    * zones/zone/storagePools/storagePool



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example:projects/project/zones/zone/diskTypes/pd-ssd. See Persistent disk types. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example:projects/project/zones/zone/diskTypes/pd-ssd. See Persistent disk types. 



**Returns**

  * (::String) — URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example:projects/project/zones/zone/diskTypes/pd-ssd. See Persistent disk types. 



### #users
    
    
    def users() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. [Output Only] Links to the users of the disk (attached instances) in form:projects/project/zones/zone/instances/instance 



### #users=
    
    
    def users=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. [Output Only] Links to the users of the disk (attached instances) in form:projects/project/zones/zone/instances/instance 



**Returns**

  * (::Array<::String>) — Output only. [Output Only] Links to the users of the disk (attached instances) in form:projects/project/zones/zone/instances/instance 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



**Returns**

  * (::String) — Output only. [Output Only] URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
