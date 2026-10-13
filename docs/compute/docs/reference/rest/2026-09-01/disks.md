---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/
title: REST Resource: disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:02:49.444348+00:00
---

# REST Resource: disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: disks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Disk
    * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: Disk

Represents a Persistent Disk resource.

Google Compute Engine has two Disk resources:

  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks)



Persistent disks are required for running your VM instances. Create both boot and non-boot (data) persistent disks. For more information, read [Persistent Disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs). For more storage options, read [Storage options](https://docs.cloud.google.com/compute/docs/disks).

The `disks` resource represents a zonal persistent disk. For more information, read [Zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs).

The `regionDisks` resource represents a regional persistent disk. For more information, read [ Regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "sizeGb": string,
      "zone": string,
      "status": enum,
      "sourceSnapshot": string,
      "sourceSnapshotId": string,
      "sourceStorageObject": string,
      "options": string,
      "selfLink": string,
      "sourceImage": string,
      "sourceImageId": string,
      "type": string,
      "licenses": [
        string
      ],
      "guestOsFeatures": [
        {
          "type": enum
        }
      ],
      "lastAttachTimestamp": string,
      "lastDetachTimestamp": string,
      "users": [
        string
      ],
      "diskEncryptionKey": {
        "rawKey": string,
        "rsaEncryptedKey": string,
        "kmsKeyName": string,
        "sha256": string,
        "kmsKeyServiceAccount": string
      },
      "sourceImageEncryptionKey": {
        "rawKey": string,
        "rsaEncryptedKey": string,
        "kmsKeyName": string,
        "sha256": string,
        "kmsKeyServiceAccount": string
      },
      "sourceSnapshotEncryptionKey": {
        "rawKey": string,
        "rsaEncryptedKey": string,
        "kmsKeyName": string,
        "sha256": string,
        "kmsKeyServiceAccount": string
      },
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "region": string,
      "replicaZones": [
        string
      ],
      "licenseCodes": [
        string
      ],
      "physicalBlockSizeBytes": string,
      "resourcePolicies": [
        string
      ],
      "sourceDisk": string,
      "sourceDiskId": string,
      "provisionedIops": string,
      "provisionedThroughput": string,
      "enableConfidentialCompute": boolean,
      "sourceInstantSnapshot": string,
      "sourceInstantSnapshotId": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
      "locationHint": string,
      "storagePool": string,
      "accessMode": enum,
      "asyncPrimaryDisk": {
        "disk": string,
        "diskId": string,
        "consistencyGroupPolicy": string,
        "consistencyGroupPolicyId": string
      },
      "asyncSecondaryDisks": {
        string: {
          "asyncReplicationDisk": {
            "disk": string,
            "diskId": string,
            "consistencyGroupPolicy": string,
            "consistencyGroupPolicyId": string
          }
        },
        ...
      },
      "resourceStatus": {
        "asyncPrimaryDisk": {
          "state": enum
        },
        "asyncSecondaryDisks": {
          string: {
            "state": enum
          },
          ...
        }
      },
      "sourceConsistencyGroupPolicy": string,
      "sourceConsistencyGroupPolicyId": string,
      "architecture": enum,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#disk` for disks.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`sizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using the `sourceImage`, `sourceSnapshot`, or `sourceDisk` parameter, or specify it alone to create an empty persistent disk.If you specify this field along with a source, the value of `sizeGb` must not be less than the size of the source. Acceptable values are greater than `0`.  
`zone` |  `string` Output only. URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`status` |  `enum` Output only. The status of disk creation. 

  * `CREATING`: Disk is provisioning.
  * `RESTORING`: Source data is being copied into the disk.
  * `FAILED`: Disk creation failed.
  * `READY`: Disk is ready for use.
  * `DELETING`: Disk is deleting.

  
`sourceSnapshot` |  `string` The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/snapshots/snapshot`
  * `projects/project/global/snapshots/snapshot`
  * `global/snapshots/snapshot`

  
`sourceSnapshotId` |  `string` Output only. The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used.  
`sourceStorageObject` |  `string` The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or <https://storage.googleapis.com/>. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use `[gcloud compute images import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import)` instead.  
`options` |  `string` Internal use only.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`sourceImage` |  `string` The source image used to create this disk. If the source image is deleted, this field will not be set.To create a disk with one of the public operating system images, specify the image by its family name. For example, specify `family/debian-9` to use the latest Debian 9 image: `projects/debian-cloud/global/images/family/debian-9`Alternatively, use a specific version of a public operating system image: `projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD`To create a disk with a custom image that you created, specify the image name in the following format: `global/images/my-custom-image`You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with `family/family-name`: `global/images/family/my-image-family`  
`sourceImageId` |  `string` Output only. The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used.  
`type` |  `string` URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example: `projects/project/zones/zone/diskTypes/pd-ssd `. See [Persistent disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types).  
`licenses[]` |  `string` A list of publicly visible licenses. Reserved for Google's use.  
`guestOsFeatures[]` |  `object` A list of features to enable on the guest operating system. Applicable only for bootable images. Read [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to see a list of available options.  
`guestOsFeatures[].type` |  `enum` The ID of a supported feature. To add multiple values, use commas to separate values. Set to one or more of the following values: 

  * `VIRTIO_SCSI_MULTIQUEUE`
  * `WINDOWS`
  * `MULTI_IP_SUBNET`
  * `UEFI_COMPATIBLE`
  * `GVNIC`
  * `SEV_CAPABLE`
  * `SUSPEND_RESUME_COMPATIBLE`
  * `SEV_LIVE_MIGRATABLE_V2`
  * `SEV_SNP_CAPABLE`
  * `TDX_CAPABLE`
  * `IDPF`
  * `SNP_SVSM_CAPABLE`
  * `CCA_CAPABLE`
  * `SUSPEND_SAFE_FPR`

For more information, see [ Enabling guest operating system features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).   
`lastAttachTimestamp` |  `string` Output only. Last attach timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`lastDetachTimestamp` |  `string` Output only. Last detach timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`users[]` |  `string` Output only. Links to the users of the disk (attached instances) in form: `projects/project/zones/zone/instances/instance`  
`diskEncryptionKey` |  `object` Encrypts the disk using a [ customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption) or a [ customer-managed encryption key](https://cloud.google.com/compute/docs/disks/customer-managed-encryption).Encryption keys do not protect access to metadata of the disk.After you encrypt a disk with a customer-supplied key, you must provide the same key if you use the disk later. For example, to create a disk snapshot, to create a disk image, to create a machine image, or to attach the disk to a virtual machine.After you encrypt a disk with a customer-managed key, the `diskEncryptionKey.kmsKeyName` is set to a key _version_ name once the disk is created. The disk is encrypted with this version of the key. In the response, `diskEncryptionKey.kmsKeyName` appears in the following format: 
    
    
    "diskEncryptionKey.kmsKeyName": "projects/kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeysVersions/version 

If you do not provide an encryption key when creating the disk, then the disk is encrypted using an automatically generated key and you don't need to provide a key to use the disk later.   
`diskEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`diskEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`diskEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`diskEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`diskEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`sourceImageEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source image. Required if the source image is protected by a customer-supplied encryption key.  
`sourceImageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`sourceImageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`sourceImageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`sourceImageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`sourceImageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`sourceSnapshotEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  
`sourceSnapshotEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`sourceSnapshotEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`sourceSnapshotEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`sourceSnapshotEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`sourceSnapshotEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`labels` |  `map (key: string, value: string)` Labels to apply to this disk. These can be later modified by the `setLabels` method.  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a disk.A base64-encoded string.  
`region` |  `string` Output only. URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. Available from version 2026-09-01.  
`replicaZones[]` |  `string` URLs of the zones where the disk should be replicated to. Only applicable for regional resources. Available from version 2026-09-01.  
`licenseCodes[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Integer license codes indicating which licenses are attached to this disk.  
`physicalBlockSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project.  
`resourcePolicies[]` |  `string` Resource policies applied to this disk for automatic snapshot creations.  
`sourceDisk` |  `string` The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/disks/disk`
  * `<https://www.googleapis.com/compute/v1/projects/>project/regions/region/disks/disk`
  * `projects/project/zones/zone/disks/disk`
  * `projects/project/regions/region/disks/disk`
  * `zones/zone/disks/disk`
  * `regions/region/disks/disk`

  
`sourceDiskId` |  `string` Output only. The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used.  
`provisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the [Extreme persistent disk documentation](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk). Available from version 2026-09-01.  
`provisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. Available from version 2026-09-01.  
`enableConfidentialCompute` |  `boolean` Whether this disk is using confidential compute mode. Available from version 2026-09-01.  
`sourceInstantSnapshot` |  `string` The source instant snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/instantSnapshots/instantSnapshot`
  * `projects/project/zones/zone/instantSnapshots/instantSnapshot`
  * `zones/zone/instantSnapshots/instantSnapshot`

  
`sourceInstantSnapshotId` |  `string` Output only. The unique ID of the instant snapshot used to create this disk. This value identifies the exact instant snapshot that was used to create this persistent disk. For example, if you created the persistent disk from an instant snapshot that was later deleted and recreated under the same name, the source instant snapshot ID would identify the exact version of the instant snapshot that was used.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use. Available from version 2026-09-01.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use. Available from version 2026-09-01.  
`locationHint` |  `string` An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. Available from version 2026-09-01.  
`storagePool` |  `string` The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/storagePools/storagePool`
  * `projects/project/zones/zone/storagePools/storagePool`
  * `zones/zone/storagePools/storagePool`

  
`accessMode` |  `enum` The access mode of the disk. 

  * `READ_WRITE_SINGLE`: The default AccessMode, means the disk can be attached to single instance in RW mode.
  * `READ_WRITE_MANY`: The AccessMode means the disk can be attached to multiple instances in RW mode.
  * `READ_ONLY_MANY`: The AccessMode means the disk can be attached to multiple instances in RO mode.

The AccessMode is only valid for Hyperdisk disk types.   
`asyncPrimaryDisk` |  `object` Disk asynchronously replicated into this disk.  
`asyncPrimaryDisk.disk` |  `string` The other disk asynchronously replicated to or from the current disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/disks/disk`
  * `projects/project/zones/zone/disks/disk`
  * `zones/zone/disks/disk`

  
`asyncPrimaryDisk.diskId` |  `string` Output only. The unique ID of the other disk asynchronously replicated to or from the current disk. This value identifies the exact disk that was used to create this replication. For example, if you started replicating the persistent disk from a disk that was later deleted and recreated under the same name, the disk ID would identify the exact version of the disk that was used.  
`asyncPrimaryDisk.consistencyGroupPolicy` |  `string` Output only. URL of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.  
`asyncPrimaryDisk.consistencyGroupPolicyId` |  `string` Output only. ID of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.  
`asyncSecondaryDisks` |  `map (key: string, value: object)` Output only. A list of disks this disk is asynchronously replicated to.  
`asyncSecondaryDisks.asyncReplicationDisk` |  `object`  
`asyncSecondaryDisks.asyncReplicationDisk.disk` |  `string` The other disk asynchronously replicated to or from the current disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/disks/disk`
  * `projects/project/zones/zone/disks/disk`
  * `zones/zone/disks/disk`

  
`asyncSecondaryDisks.asyncReplicationDisk.diskId` |  `string` Output only. The unique ID of the other disk asynchronously replicated to or from the current disk. This value identifies the exact disk that was used to create this replication. For example, if you started replicating the persistent disk from a disk that was later deleted and recreated under the same name, the disk ID would identify the exact version of the disk that was used.  
`asyncSecondaryDisks.asyncReplicationDisk.consistencyGroupPolicy` |  `string` Output only. URL of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.  
`asyncSecondaryDisks.asyncReplicationDisk.consistencyGroupPolicyId` |  `string` Output only. ID of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.  
`resourceStatus` |  `object` Output only. Status information for the disk resource.  
`resourceStatus.asyncPrimaryDisk` |  `object`  
`resourceStatus.asyncPrimaryDisk.state` |  `enum`  
`resourceStatus.asyncSecondaryDisks[]` |  `map (key: string, value: object)` Key: disk, value: AsyncReplicationStatus message  
`resourceStatus.asyncSecondaryDisks[].state` |  `enum`  
`sourceConsistencyGroupPolicy` |  `string` Output only. URL of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group.  
`sourceConsistencyGroupPolicyId` |  `string` Output only. ID of the DiskConsistencyGroupPolicy for a secondary disk that was created using a consistency group.  
`architecture` |  `enum` The architecture of the disk. Valid values are ARM64 or X86_64. Available from version 2026-09-01.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload. Available from version 2026-09-01.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the disk. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
  
## Methods  
  
---  
  
### `[addResourcePolicies](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/addResourcePolicies)`

|  Adds existing resource policies to a disk.  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/aggregatedList)`

|  Retrieves an aggregated list of persistent disks.  
  
### `[bulkInsert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/bulkInsert)`

|  Bulk create a set of disks.  
  
### `[bulkSetLabels](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/bulkSetLabels)`

|  Sets the labels on many disks at once.  
  
### `[createSnapshot](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/createSnapshot)`

|  Creates a snapshot of a specified persistent disk.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/delete)`

|  Deletes the specified persistent disk.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/get)`

|  Returns the specified persistent disk.  
  
### `[getIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/insert)`

|  Creates a persistent disk in the specified project using the data in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/list)`

|  Retrieves a list of persistent disks contained within the specified zone.  
  
### `[removeResourcePolicies](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/removeResourcePolicies)`

|  Removes resource policies from a disk.  
  
### `[resize](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/resize)`

|  Resizes the specified persistent disk.  
  
### `[setIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[setLabels](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/setLabels)`

|  Sets the labels on a disk.  
  
### `[startAsyncReplication](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/startAsyncReplication)`

|  Starts asynchronous replication.  
  
### `[stopAsyncReplication](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/stopAsyncReplication)`

|  Stops asynchronous replication.  
  
### `[stopGroupAsyncReplication](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/stopGroupAsyncReplication)`

|  Stops asynchronous replication for a consistency group of disks.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/update)`

|  Updates the specified disk with the data included in the request.  
  
### `[updateKmsKey](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/disks/updateKmsKey)`

|  Rotates the [customer-managed encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) to the latest version for the specified persistent disk.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
