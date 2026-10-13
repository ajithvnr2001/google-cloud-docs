---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/imageViews/list/
title: Method: imageViews.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:52.613267+00:00
---

# Method: imageViews.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/imageViews/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: imageViews.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns a list of global ImageView resources, with a regional context.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/imageViews?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Required. Project ID for this request.  
`region` |  `string` Required. Name of the region for this request.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
  
### Request body

The request body must be empty.

### Response body

Response message for ImageViewsService.List

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "image": {
            "kind": string,
            "id": string,
            "creationTimestamp": string,
            "name": string,
            "description": string,
            "sourceType": enum,
            "rawDisk": {
              "source": string,
              "sha1Checksum": string,
              "containerType": enum
            },
            "deprecated": {
              "state": enum,
              "replacement": string,
              "deprecated": string,
              "obsolete": string,
              "deleted": string
            },
            "status": enum,
            "archiveSizeBytes": string,
            "diskSizeGb": string,
            "sourceDisk": string,
            "sourceDiskId": string,
            "licenses": [
              string
            ],
            "family": string,
            "imageEncryptionKey": {
              "rawKey": string,
              "rsaEncryptedKey": string,
              "kmsKeyName": string,
              "sha256": string,
              "kmsKeyServiceAccount": string
            },
            "sourceDiskEncryptionKey": {
              "rawKey": string,
              "rsaEncryptedKey": string,
              "kmsKeyName": string,
              "sha256": string,
              "kmsKeyServiceAccount": string
            },
            "selfLink": string,
            "labels": {
              string: string,
              ...
            },
            "labelFingerprint": string,
            "guestOsFeatures": [
              {
                "type": enum
              }
            ],
            "licenseCodes": [
              string
            ],
            "sourceImage": string,
            "sourceImageId": string,
            "sourceImageEncryptionKey": {
              "rawKey": string,
              "rsaEncryptedKey": string,
              "kmsKeyName": string,
              "sha256": string,
              "kmsKeyServiceAccount": string
            },
            "sourceSnapshot": string,
            "sourceSnapshotId": string,
            "sourceSnapshotEncryptionKey": {
              "rawKey": string,
              "rsaEncryptedKey": string,
              "kmsKeyName": string,
              "sha256": string,
              "kmsKeyServiceAccount": string
            },
            "storageLocations": [
              string
            ],
            "shieldedInstanceInitialState": {
              "pk": {
                "content": string,
                "fileType": enum
              },
              "keks": [
                {
                  "content": string,
                  "fileType": enum
                }
              ],
              "dbs": [
                {
                  "content": string,
                  "fileType": enum
                }
              ],
              "dbxs": [
                {
                  "content": string,
                  "fileType": enum
                }
              ]
            },
            "satisfiesPzs": boolean,
            "architecture": enum,
            "enableConfidentialCompute": boolean,
            "satisfiesPzi": boolean,
            "params": {
              "resourceManagerTags": {
                string: string,
                ...
              }
            }
          }
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      },
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string`  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Image resources.  
`items[].image` |  `object` The Image resource.  
`items[].image.kind` |  `string` Output only. Type of the resource. Always `compute#image` for images.  
`items[].image.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].image.creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].image.name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].image.description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].image.sourceType` |  `enum` The type of the image used to create this disk. The default and only valid value is `RAW`.  
`items[].image.rawDisk` |  `object` The parameters of the raw disk image.  
`items[].image.rawDisk.source` |  `string` The full Google Cloud Storage URL or Artifact Registry path where the raw disk image archive is stored. The following are valid formats: 

  * `<https://storage.googleapis.com/>bucketName/image_archive_name`
  * `<https://storage.googleapis.com/>bucketName/folder_name/image_archive_name`
  * `projects/project/locations/location/repositories/repo/packages/package/versions/version_id`
  * `projects/project/locations/location/repositories/repo/packages/package/versions/version_id@dirsum_sha256:hex_value`

In order to create an image, you must provide the full or partial URL of one of the following: 

  * The `rawDisk.source` URL 
  * The `sourceDisk` URL 
  * The `sourceImage` URL 
  * The `sourceSnapshot` URL 

  
`items[].image.rawDisk.sha1Checksum  
**(deprecated)**` |  `string` [Deprecated] This field is deprecated. An optional SHA1 checksum of the disk image before unpackaging provided by the client when the disk image is created.  
`items[].image.rawDisk.containerType` |  `enum` The format used to encode and transmit the block device, which should be `TAR`. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created.  
`items[].image.deprecated` |  `object` Output only. The deprecation status associated with this image.  
`items[].image.deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`items[].image.deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`items[].image.deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].image.deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].image.deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].image.status` |  `enum` Output only. The status of the image. An image can be used to create other resources, such as instances, only after the image has been successfully created and the `status` is set to `READY`. Possible values are `FAILED`, `PENDING`, or `READY`.  
`items[].image.archiveSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the image `tar.gz` archive stored in Google Cloud Storage (in bytes).  
`items[].image.diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the image when restored onto a persistent disk (in GB).  
`items[].image.sourceDisk` |  `string` URL of the source disk used to create this image. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone/disks/disk`
  * `projects/project/zones/zone/disks/disk`
  * `zones/zone/disks/disk`

In order to create an image, you must provide the full or partial URL of one of the following: 

  * The `rawDisk.source` URL 
  * The `sourceDisk` URL 
  * The `sourceImage` URL 
  * The `sourceSnapshot` URL 

  
`items[].image.sourceDiskId` |  `string` Output only. The ID value of the disk used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given disk name.  
`items[].image.licenses[]` |  `string` Any applicable license URI.  
`items[].image.family` |  `string` The name of the image family to which this image belongs. The image family name can be from a publicly managed image family provided by Compute Engine, or from a custom image family you create. For example, `centos-stream-9` is a publicly available image family. For more information, see [Image family best practices](https://cloud.google.com/compute/docs/images/image-families-best-practices).When creating disks, you can specify an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`items[].image.imageEncryptionKey` |  `object` Encrypts the image using a [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption).After you encrypt an image with a customer-supplied key, you must provide the same key if you use the image later (e.g. to create a disk from the image).Customer-supplied encryption keys do not protect access to metadata of the disk.If you do not provide an encryption key when creating the image, then the disk will be encrypted using an automatically generated key and you do not need to provide a key to use the image later.  
`items[].image.imageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`items[].image.imageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`items[].image.imageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`items[].image.imageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`items[].image.imageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`items[].image.sourceDiskEncryptionKey` |  `object` The [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) of the source disk. Required if the source disk is protected by a customer-supplied encryption key.  
`items[].image.sourceDiskEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`items[].image.sourceDiskEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`items[].image.sourceDiskEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`items[].image.sourceDiskEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`items[].image.sourceDiskEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`items[].image.selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].image.labels` |  `map (key: string, value: string)` Labels to apply to this image. These can be later modified by the `setLabels` method.  
`items[].image.labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this image, which is essentially a hash of the labels used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an image.A base64-encoded string.  
`items[].image.guestOsFeatures[]` |  `object` A list of features to enable on the guest operating system. Applicable only for bootable images. To see a list of available options, see the `guestOSfeatures[].type` parameter.  
`items[].image.guestOsFeatures[].type` |  `enum` The ID of a supported feature. To add multiple values, use commas to separate values. Set to one or more of the following values: 

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
`items[].image.licenseCodes[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Integer license codes indicating which licenses are attached to this image.  
`items[].image.sourceImage` |  `string` URL of the source image used to create this image. The following are valid formats for the URL: 

  * `<https://www.googleapis.com/compute/v1/projects/>projectId/global/ images/image_name`
  * `projects/projectId/global/images/image_name`

In order to create an image, you must provide the full or partial URL of one of the following: 

  * The `rawDisk.source` URL 
  * The `sourceDisk` URL 
  * The `sourceImage` URL 
  * The `sourceSnapshot` URL 

  
`items[].image.sourceImageId` |  `string` Output only. The ID value of the image used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given image name.  
`items[].image.sourceImageEncryptionKey` |  `object` The customer-supplied encryption key of the source image. Required if the source image is protected by a customer-supplied encryption key.  
`items[].image.sourceImageEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`items[].image.sourceImageEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`items[].image.sourceImageEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`items[].image.sourceImageEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`items[].image.sourceImageEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`items[].image.sourceSnapshot` |  `string` URL of the source snapshot used to create this image. The following are valid formats for the URL: 

  * `<https://www.googleapis.com/compute/v1/projects/>projectId/global/ snapshots/snapshotName`
  * `projects/projectId/global/snapshots/snapshotName`

In order to create an image, you must provide the full or partial URL of one of the following: 

  * The `rawDisk.source` URL 
  * The `sourceDisk` URL 
  * The `sourceImage` URL 
  * The `sourceSnapshot` URL 

  
`items[].image.sourceSnapshotId` |  `string` Output only. The ID value of the snapshot used to create this image. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given snapshot name.  
`items[].image.sourceSnapshotEncryptionKey` |  `object` The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by a customer-supplied encryption key.  
`items[].image.sourceSnapshotEncryptionKey.rawKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies a 256-bit [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="   
  
`items[].image.sourceSnapshotEncryptionKey.rsaEncryptedKey  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit [ customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) to either encrypt or decrypt this resource. You can provide either the `rawKey` or the `rsaEncryptedKey`. For example: 
    
    
    "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFH z0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoD D6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oe==" 

The key must meet the following requirements before you can provide it to Compute Engine: 

  1. The key is wrapped using a RSA public key certificate provided by Google.
  2. After being wrapped, the key must be encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoding.

Gets the RSA public key certificate provided by Google at: 
    
    
     <https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem>  
  
`items[].image.sourceSnapshotEncryptionKey.kmsKeyName` |  `string` The name of the encryption key that is stored in Google Cloud KMS. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key 

The fully-qualifed key name may be returned for resource GET requests. For example: 
    
    
    "kmsKeyName": "projects/ kms_project_id/locations/ region/keyRings/ key_region/cryptoKeys/key /cryptoKeyVersions/1  
  
`items[].image.sourceSnapshotEncryptionKey.sha256  
**(deprecated)**` |  `string` [DEPRECATED] CSEK is no longer supported. Use CMEK instead. Output only. The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the [customer-supplied encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) that protects this resource.  
`items[].image.sourceSnapshotEncryptionKey.kmsKeyServiceAccount` |  `string` The service account being used for the encryption request for the given KMS key. If absent, the Compute Engine default service account is used. For example: 
    
    
    "kmsKeyServiceAccount": "name@ projectId.iam.gserviceaccount.com/   
  
`items[].image.storageLocations[]` |  `string` Cloud Storage bucket storage location of the image (regional or multi-regional).  
`items[].image.shieldedInstanceInitialState` |  `object` Set the secure boot keys of shielded instance.  
`items[].image.shieldedInstanceInitialState.pk` |  `object` The Platform Key (PK).  
`items[].image.shieldedInstanceInitialState.pk.content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`items[].image.shieldedInstanceInitialState.pk.fileType` |  `enum` The file type of source file.  
`items[].image.shieldedInstanceInitialState.keks[]` |  `object` The Key Exchange Key (KEK).  
`items[].image.shieldedInstanceInitialState.keks[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`items[].image.shieldedInstanceInitialState.keks[].fileType` |  `enum` The file type of source file.  
`items[].image.shieldedInstanceInitialState.dbs[]` |  `object` The Key Database (db).  
`items[].image.shieldedInstanceInitialState.dbs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`items[].image.shieldedInstanceInitialState.dbs[].fileType` |  `enum` The file type of source file.  
`items[].image.shieldedInstanceInitialState.dbxs[]` |  `object` The forbidden key database (dbx).  
`items[].image.shieldedInstanceInitialState.dbxs[].content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content in the secure keys file.A base64-encoded string.  
`items[].image.shieldedInstanceInitialState.dbxs[].fileType` |  `enum` The file type of source file.  
`items[].image.satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`items[].image.architecture` |  `enum` The architecture of the image. Valid values are ARM64 or X86_64.  
`items[].image.enableConfidentialCompute` |  `boolean` Output only. Whether this image is created from a confidential compute mode disk. Output only.: This field is not set by user, but from source disk.  
`items[].image.satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
`items[].image.params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`items[].image.params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the image. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`nextPageToken` |  `string`  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`etag` |  `string` Etag of the resource.  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.images.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
