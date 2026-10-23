---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/
title: Buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:08.239340+00:00
---

# Buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets Stay organized with collections  Save and categorize content based on your preferences. 

The Buckets resource represents a [bucket](https://docs.cloud.google.com/storage/docs/buckets) in Cloud Storage. There is a single global namespace shared by all buckets. For more information, see [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

Buckets contain [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects) which can be accessed by their own methods. In addition to the `acl` property, buckets contain [bucketAccessControls](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls), for use in fine-grained manipulation of an existing bucket's access controls.

A bucket is always owned by the associated project's `projectOwner` [convenience value](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values).

To try out the methods for this resource, such as creating a new bucket, see Methods.

## Resource representations
    
    
    {
      "kind": "storage#bucket",
      "selfLink": string,
      "id": string,
      "name": string,
      "projectNumber": "unsigned long",
      "generation": "long",
      "metageneration": "long",
      "location": string,
      "storageClass": string,
      "etag": string,
      "defaultEventBasedHold": boolean,
      "timeCreated": "datetime",
      "updated": "datetime",
      "softDeleteTime": "datetime",
      "hardDeleteTime": "datetime",
      "hierarchicalNamespace": {
        "enabled": boolean
      },
      "encryption": {
        "defaultKmsKeyName": string,
        "googleManagedEncryptionEnforcementConfig": {
          "restrictionMode": string,
          "effectiveTime": datetime
        },
        "customerManagedEncryptionEnforcementConfig": {
          "restrictionMode": string,
          "effectiveTime": datetime
        },
        "customerSuppliedEncryptionEnforcementConfig": {
          "restrictionMode": string,
          "effectiveTime": datetime
        },
      },
      "acl": [
        [bucketAccessControls Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls#resource)
      ],
      "defaultObjectAcl": [
        [defaultObjectAccessControls Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls#resource)
      ],
      "website": {
        "mainPageSuffix": string,
        "notFoundPage": string
      },
      "owner": {
        "entity": string,
        "entityId": string
      },
      "logging": {
        "logBucket": string,
        "logObjectPrefix": string
      },
      "cors": [
        {
          "origin": [
            string
          ],
          "method": [
            string
          ],
          "responseHeader": [
            string
          ],
          "maxAgeSeconds": integer
        }
      ],
      "versioning": {
        "enabled": boolean
      },
      "lifecycle": {
        "rule": [
          {
            "action": {
              "storageClass": string,
              "type": string
            },
            "condition": {
              "age": integer,
              "createdBefore": "date",
              "isLive": boolean,
              "numNewerVersions": integer,
              "matchesStorageClass": [
                string
              ],
              "daysSinceCustomTime": integer,
              "customTimeBefore": "date",
              "daysSinceNoncurrentTime": integer,
              "noncurrentTimeBefore": "date",
              "matchesPrefix": [
                string
              ],
              "matchesSuffix": [
                string
              ],
              "sizeAboveBytes": integer,
              "sizeBelowBytes": integer
            }
          }
        ]
      },
      "autoclass": {
        "enabled": boolean,
        "toggleTime": "datetime",
        "terminalStorageClass": string,
        "terminalStorageClassUpdateTime": "datetime"
      },
      "labels": {
        (key): string
      },
      "retentionPolicy": {
        "retentionPeriod": "unsigned long",
        "effectiveTime": "datetime",
        "isLocked": boolean
      },
      "objectRetention": {
        "mode": string
      },
      "billing": {
        "requesterPays": boolean
      },
      "iamConfiguration": {
        "publicAccessPrevention": string,
        "uniformBucketLevelAccess": {
          "enabled": boolean,
          "lockedTime":"datetime"
        },
      },
      "ipFilter": {
        "allowAllServiceAgentAccess": boolean,
        "allowCrossOrgVpcs": boolean,
        "mode": string,
        "publicNetworkSource": {
          "allowedIpCidrRanges": [
            string,
            ]
        },
        "vpcNetworkSources": [
          {
            "network": string,
            "allowedIpCidrRanges": [
              string,
              ]
          },
        ]
      }
      "locationType": string,
      "customPlacementConfig": {
        "dataLocations": [
          string,
          string
        ]
      },
      "softDeletePolicy": {
        "retentionDurationSeconds": long,
        "effectiveTime": datetime
      },
      "rpo": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`acl[]` | `list` | Access controls on the bucket, containing one or more [bucketAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls). If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field is omitted in responses, and requests that specify this field fail with a `400 Bad Request` response. |  writable   
`autoclass` | `object` | The bucket's [Autoclass configuration](https://docs.cloud.google.com/storage/docs/autoclass), which, when enabled, controls the storage class of objects based on how and when the objects are accessed. |  writable   
`autoclass.enabled` | `boolean` | Whether or not Autoclass is enabled. By default, this boolean is not set, and Autoclass is disabled. | writable  
`autoclass.terminalStorageClass` | `string` | The coldest storage class that an object in an Autoclass-enabled bucket transitions to if it is not accessed. Valid values are `NEARLINE` and `ARCHIVE`. The default value is `NEARLINE`. | writable  
`autoclass.terminalStorageClassUpdateTime` | `datetime`1 | The time at which the terminal storage class was last updated for this bucket, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`autoclass.toggleTime` | `datetime`1 | The time at which Autoclass was last enabled or disabled for this bucket, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`billing` | `object` | The bucket's billing configuration. |  writable   
`billing.requesterPays` | `boolean` | When set to true, [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) is enabled for this bucket. |  writable   
`cors[]` | `list` | The bucket's [Cross-Origin Resource Sharing](https://www.w3.org/TR/cors/) (CORS) configuration. |  writable   
`cors[].maxAgeSeconds` | `integer` | The value, in seconds, to return in the [Access-Control-Max-Age header](https://www.w3.org/TR/cors/#access-control-max-age-response-header) used in preflight responses. |  writable   
`cors[].method[]` | `list` | The list of HTTP methods on which to include CORS response headers in, such as `"GET"`, `"OPTIONS"`, and `"POST"`. **Note:** `"*"` is permitted in the list of methods, and means "any method". |  writable   
`cors[].origin[]` | `list` | The list of [Origins](https://datatracker.ietf.org/doc/html/rfc6454) eligible to receive CORS response headers. **Note:** `"*"` is permitted in the list of origins, and means "any Origin". |  writable   
`cors[].responseHeader[]` | `list` | The list of HTTP headers other than the [simple response headers](https://www.w3.org/TR/cors/#simple-response-header) to give permission for the user-agent to share across domains. |  writable   
`customPlacementConfig` | `object` | Applicable only if a bucket is located in a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr). The bucket's custom location configuration. |  writable for [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) requests   
`customPlacementConfig.dataLocations[]` | `list` | The list of individual regions that comprise a configurable dual-region bucket. See [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations#location-dr) for a list of acceptable regions. |  writable for [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) requests   
`defaultEventBasedHold` | `boolean` | Whether or not to automatically apply an [`eventBasedHold`](https://docs.cloud.google.com/storage/docs/object-holds#hold-types) to new objects added to the bucket. |  writable   
`defaultObjectAcl[]` | `list` | Default access controls to apply to new objects when no ACL is provided. This list contains one or more [defaultObjectAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls). If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field is omitted in responses, and requests that specify this field fail. |  writable   
`encryption` | `object` | Encryption settings for a bucket. |  writable   
`encryption.defaultKmsKeyName` | `string` | A [Cloud KMS key](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) that is used to encrypt objects written to this bucket if no encryption method is specified as part of the object write request. | writable  
`encryption.googleManagedEncryptionEnforcementConfig` | `object` |  Controls the use of [standard encryption (Google default encryption)](https://docs.cloud.google.com/storage/docs/encryption) to encrypt objects in this bucket. If omitted, then creating new objects with standard encryption is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. | writable  
`encryption.googleManagedEncryptionEnforcementConfig.restrictionMode` | `string` |  Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 

  * `NotRestricted`: new objects can use standard encryption.
  * `FullyRestricted`: new objects can't use standard encryption.

| writable  
`encryption.googleManagedEncryptionEnforcementConfig.effectiveTime` | `datetime`1 |  The time from which the encryption enforcement configuration for standard encryption (Google default encryption) was set to fully restricted, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  |   
`encryption.customerManagedEncryptionEnforcementConfig` | `object` |  Controls the use of [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to encrypt objects in this bucket. If omitted, then creating new objects with CMEKs is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. | writable  
`encryption.customerManagedEncryptionEnforcementConfig.restrictionMode` | `string` |  Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 

  * `NotRestricted`: new objects can use CMEKs.
  * `FullyRestricted`: new objects can't use CMEKs.

| writable  
`encryption.customerManagedEncryptionEnforcementConfig.effectiveTime` | `datetime`1 |  The time from which the encryption enforcement configuration for CMEKs was set to fully restricted, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  |   
`encryption.customerSuppliedEncryptionEnforcementConfig` | `object` |  Controls the use of [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) to encrypt objects in this bucket. If omitted, then creating new objects with customer-supplied encryption keys is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. | writable  
`encryption.customerSuppliedEncryptionEnforcementConfig.restrictionMode` | `string` |  Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 

  * `NotRestricted`: new objects can use customer-supplied encryption keys.
  * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

| writable  
`encryption.customerSuppliedEncryptionEnforcementConfig.effectiveTime` | `datetime`1 |  The time from which the encryption enforcement configuration for customer-supplied encryption keys was set to fully restricted, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  |   
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the bucket. |   
`hierarchicalNamespace.enabled` | `boolean` | Whether or not [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) is enabled for this bucket. |  writable for [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) requests   
`iamConfiguration` | `object` | The IAM configuration for a bucket. |  writable   
`iamConfiguration.publicAccessPrevention` | `string` | The bucket's [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) status, which is either `"inherited"` or `"enforced"`. If `"inherited"`, the bucket uses public access prevention only if the bucket is subject to the [public access prevention organization policy constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention). Defaults to `"inherited"`. |  writable   
`iamConfiguration.uniformBucketLevelAccess` | `object` | The bucket's [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) configuration. **Note:** `iamConfiguration` also includes the `bucketPolicyOnly` field, which uses a legacy name but has the same functionality as the `uniformBucketLevelAccess` field. We recommend only using `uniformBucketLevelAccess`, as specifying both fields might result in unreliable behavior. |  writable   
`iamConfiguration.uniformBucketLevelAccess.enabled` | `boolean` | Whether or not the bucket uses uniform bucket-level access. If set, access checks only use bucket-level IAM policies or above. |  writable   
`iamConfiguration.uniformBucketLevelAccess.lockedTime` | `datetime`1 | The deadline time for changing `iamConfiguration.uniformBucketLevelAccess.enabled` from `true` to `false`, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. `iamConfiguration.uniformBucketLevelAccess.enabled` might be changed from `true` to `false` until the locked time, after which the field is immutable. |   
`id` | `string` | The ID of the bucket. For buckets, the `id` and `name` properties are the same. |   
`ipFilter` | `object` | The [bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) configuration. Specifies the network sources that can access the bucket, as well as its underlying objects. |  writable   
`ipFilter.allowAllServiceAgentAccess` | `boolean` | Whether to allow [service agent](https://docs.cloud.google.com/iam/docs/service-agents) access to the bucket, regardless of the IP filter configuration. If the value is `true`, other Google Cloud services can use service agents to access the bucket without IP-based validation. |  writable   
`ipFilter.allowCrossOrgVpcs` | `boolean` | Whether to allow VPC networks that are defined in `vpcNetworkSources` to originate from a different organization. If set to `true`, the request allows cross-organizational VPC networks. If set to `false`, the request restricts the VPC networks to the same organization as the bucket. If not specified, the default value is `false`. |  writable   
`ipFilter.mode` | `string` | The state of the IP filter configuration. Valid values are `Enabled` and `Disabled`. When set to `Enabled`, IP filtering rules are applied to a bucket and all incoming requests to the bucket are evaluated against these rules. When set to `Disabled`, IP filtering rules are not applied to a bucket. |  writable   
`ipFilter.publicNetworkSource` | `object` | The public network IP address ranges that can access the bucket and its data. |  writable   
`ipFilter.publicNetworkSource.allowedIpCidrRanges[]` | `list of strings` | The list of public IPv4 and IPv6 CIDR ranges that can access the bucket and its data. In the CIDR IP address block, the specified IP address must be properly truncated, meaning all the host bits must be zero or else the input is considered malformed. For example, `192.0.2.0/24` is accepted but `192.0.2.1/24` is not. Similarly, for IPv6, `2001:db8::/32` is accepted whereas `2001:db8::1/32` is not. |  writable   
`ipFilter.vpcNetworkSources[]` | `list` | The list of [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) that can access the bucket. |  writable   
`ipFilter.vpcNetworkSources.network` | `string` | Name of the network.  
Format: `projects/PROJECT_ID/global/networks/NETWORK_NAME` |  writable   
`ipFilter.vpcNetworkSources.allowedIpCidrRanges[]` | `list of strings` | The list of public or private IPv4 and IPv6 CIDR ranges that can access the bucket. In the CIDR IP address block, the specified IP address must be properly truncated, meaning all the host bits must be zero or else the input is considered malformed. For example, `192.0.2.0/24` is accepted but `192.0.2.1/24` is not. Similarly, for IPv6, `2001:db8::/32` is accepted whereas `2001:db8::1/32` is not. |  writable   
`kind` | `string` | The kind of resource being described. For buckets, this is always `"storage#bucket"`. |   
`labels` | `object` | User-provided [bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), in key-value pairs. |  writable   
`labels.(key)` | `string` | An individual label entry. |  writable   
`lifecycle` | `object` | The bucket's lifecycle configuration. See [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) for more information. |  writable   
`lifecycle.rule[]` | `list` | A lifecycle management rule, which is made of an action to take and the conditions under which the action is taken. | writable  
`lifecycle.rule[].action` | `object` | The lifecycle action to take. | writable  
`lifecycle.rule[].action.storageClass` | `string` | The new storage class when `action.type` is `"SetStorageClass"`. See [lifecycle actions](https://docs.cloud.google.com/storage/docs/lifecycle#actions) for a table of supported storage class transitions. | writable  
`lifecycle.rule[].action.type` | `string` | The type of action. Supported values are `"Delete"`, `"SetStorageClass"`, and `"AbortIncompleteMultipartUpload"`. | writable  
`lifecycle.rule[].condition` | `object` | The conditions under which the action is taken. | writable  
`lifecycle.rule[].condition.age` | `integer` | Age of an object (in days). This condition is satisfied when an object reaches the specified age. | writable  
`lifecycle.rule[].condition.createdBefore` | `date`1 | A date in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format `YYYY-MM-DD`. This condition is satisfied when an object is created before midnight of the specified date in UTC. | writable  
`lifecycle.rule[].condition.customTimeBefore` | `date`1 | A date in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format `YYYY-MM-DD`. This condition is satisfied when the `customTime` metadata for the object is set to an earlier date than the date used in this lifecycle condition. | writable  
`lifecycle.rule[].condition.daysSinceCustomTime` | `integer` | Days since the date set in the `customTime` metadata for the object. This condition is satisfied when the current date and time is at least the specified number of days after the `customTime`. | writable  
`lifecycle.rule[].condition.daysSinceNoncurrentTime` | `integer` | Relevant only for versioned objects. This condition is satisfied when an object has been noncurrent for more than the specified number of days. | writable  
`lifecycle.rule[].condition.isLive` | `boolean` | Relevant only for versioned objects. If the value is `true`, this condition matches the live version of objects; if the value is `false`, it matches noncurrent versions of objects. | writable  
`lifecycle.rule[].condition.matchesPrefix[]` | `list of strings` | The prefix of an object. This condition is satisfied when the beginning of an object's name is an exact case-sensitive match with the prefix. The prefix must meet [object naming requirements](https://docs.cloud.google.com/storage/docs/objects#naming). You can specify one or multiple strings as a list. | writable  
`lifecycle.rule[].condition.matchesStorageClass[]` | `list` | Objects having any of the storage classes specified by this condition will be matched. Values include `"STANDARD"`, `"NEARLINE"`, `"COLDLINE"`, `"ARCHIVE"`, `"MULTI_REGIONAL"`, `"REGIONAL"`, and `"DURABLE_REDUCED_AVAILABILITY"`. | writable  
`lifecycle.rule[].condition.matchesSuffix[]` | `list of strings` | The suffix of an object. This condition is satisfied when the end of an object's name is an exact case-sensitive match with the suffix. The suffix must meet [object naming requirements](https://docs.cloud.google.com/storage/docs/objects#naming). You can specify one or multiple strings as a list. | writable  
`lifecycle.rule[].condition.noncurrentTimeBefore` | `date`1 | Relevant only for versioned objects. A date in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format `YYYY-MM-DD`. This condition is satisfied for objects that became noncurrent on a date prior to the one specified in this condition. | writable  
`lifecycle.rule[].condition.numNewerVersions` | `integer` | Relevant only for versioned objects. If the value is `N`, this condition is satisfied when there are at least `N` versions (including the live version) newer than this version of the object. | writable  
`lifecycle.rule[].condition.sizeAboveBytes` | `integer` |  The size of an object, excluding its metadata, in bytes. This condition is satisfied when an object's size is larger than the specified value. Use this condition to define a minimum size threshold for lifecycle actions.  | writable  
`lifecycle.rule[].condition.sizeBelowBytes` | `integer` |  The size of an object, excluding its metadata, in bytes. This condition is satisfied when an object's size is smaller than the specified value. Use this condition to define a maximum size threshold for lifecycle actions.  | writable  
`location` | `string` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this location. Defaults to `"US"`. See [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations) for the authoritative list. |  writable for [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) requests   
`locationType` | `string` | The type of location that the bucket resides in. Possible values include `region`, `dual-region`, and `multi-region`. |   
`logging` | `object` | The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's [usage logs and storage logs](https://docs.cloud.google.com/storage/docs/access-logs). |  writable   
`logging.logBucket` | `string` | The destination bucket where the current bucket's logs should be placed. |  writable   
`logging.logObjectPrefix` | `string` | A prefix for log object names. The default prefix is the bucket name. |  writable   
`generation` | `long`1 | The version of the bucket. |   
`metageneration` | `long`1 | The metadata generation of this bucket. |   
`name` | `string` | The name of the bucket. | writable for [insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) requests  
`objectRetention` | `object` | The bucket's [object retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). |   
`objectRetention.mode` | `string` | When set to `Enabled`, retention configurations can be set on objects in the bucket. |   
`owner` | `object` | The owner of the bucket. This is always the project team's owner group. |   
`owner.entity` | `string` | The entity, in the form `"project-owner-projectId"`. |   
`owner.entityId` | `string` | The ID for the entity. |   
`projectNumber` | `unsigned long`1 | The project number of the project the bucket belongs to. |   
`selfLink` | `string` | The URI of this bucket. |   
`retentionPolicy` | `object` | The bucket's [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy), which defines the minimum age an object in the bucket must reach before it can be deleted or replaced. |  writable   
`retentionPolicy.effectiveTime` | `datetime`1 | The time from which the retentionPolicy was effective, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`retentionPolicy.isLocked` | `boolean` | Whether or not the retentionPolicy is locked. If true, the retentionPolicy cannot be removed and the retention period cannot be reduced. |   
`retentionPolicy.retentionPeriod` | `unsigned integer`1 | The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, replaced, or made noncurrent. The value must be greater than 0 seconds and less than 3,155,760,000 seconds. |  writable   
`rpo` | `string` | The recovery point objective for cross-region replication of the bucket. Applicable only for dual- and multi-region buckets. `"DEFAULT"` uses default replication. `"ASYNC_TURBO"` enables turbo replication, valid for dual-region buckets only. If `rpo` is not specified when the bucket is created, it defaults to `"DEFAULT"`. For more information, see [redundancy across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy). |  writable   
`softDeletePolicy` | `object` |  The bucket's [soft delete policy](https://docs.cloud.google.com/storage/docs/soft-delete), which defines the period of time during which objects in the bucket are retained in a soft-deleted state after being deleted. Objects in a soft-deleted state cannot be permanently deleted, and are restorable until their `hardDeleteTime`.  | writable  
`softDeletePolicy.effectiveTime` | `datetime` |  The datetime at which the soft delete policy becomes effective, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. `softDeletePolicy.effectiveTime` is updated whenever `softDeletePolicy.retentionDurationSeconds` is increased. |   
`softDeletePolicy.retentionDurationSeconds` | `long` |  The period of time during which a soft-deleted object is retained and cannot be permanently deleted, in seconds. The value must be greater than or equal to 7 days and less than 90 days. The value can also be set to `0`, which disables the soft delete policy.  | writable  
`storageClass` | `string` | The bucket's default storage class, used whenever no `storageClass` is specified for a newly-created object. If `storageClass` is not specified when the bucket is created, it defaults to `"STANDARD"`. For available storage classes, see [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes). |  writable   
`timeCreated` | `datetime`1 | The creation time of the bucket in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`updated` | `datetime`1 | The time at which the bucket's metadata or IAM policy was last updated, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`softDeleteTime` | `datetime`1 | The time at which the bucket was [soft-deleted](https://docs.cloud.google.com/storage/docs/soft-delete). |   
`hardDeleteTime` | `datetime`1 | The time when a soft-deleted bucket is permanently deleted and can no longer be restored. This time is always equal to or later than the latest `hardDeleteTime` of any soft-deleted object within the bucket. |   
`versioning` | `object` | The bucket's versioning configuration. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). |  writable   
`versioning.enabled` | `boolean` | While set to true, versioning is fully enabled for this bucket. |  writable   
`website` | `object` | The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the [Static Website Examples](https://docs.cloud.google.com/storage/docs/static-website) for more information. |  writable   
`website.mainPageSuffix` | `string` | If the requested object path is missing, the service ensures the path has a trailing '/', appends the suffix, and attempts to retrieve the resulting object. This allows the creation of `index.html` objects to represent directory pages. |  writable   
`website.notFoundPage` | `string` | If the requested object path is missing, and any `mainPageSuffix` object is missing, if applicable, the service returns the named object from this bucket as the content for a [`404 Not Found`](https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.4) result. |  writable   
1 This property is a string formatted as the specified value type. 

## Methods

Available methods for Buckets resources are as follows:

[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/delete)
    Deletes a bucket.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get)
    Returns metadata for the specified bucket.
[getIamPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy)
    Returns an IAM policy for the specified bucket.
[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert)
    Creates a new bucket.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list)
    Retrieves a list of buckets for a given project.
[lockRetentionPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/lockRetentionPolicy)
    Irreversibly sets the retention policy on a bucket.
[patch](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch)
    Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. This method supports [patch](https://docs.cloud.google.com/storage/docs/json_api#patch) semantics.
[relocate](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate)
    Relocates a bucket to a different geographic location.
[restore](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/restore)
    Restores a soft-deleted bucket.
[setIamPolicy](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy)
    Updates an IAM policy for the specified bucket.
[testIamPermissions](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions)
    Tests a set of permissions on the given bucket to see which, if any, are held by the caller.
[update](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/update)
    Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. This method sets the complete metadata of a bucket. If you want to change some of a bucket's metadata while leaving other parts unaffected, use the [PATCH](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) method instead.

For information about status and error codes returned by these APIs, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
