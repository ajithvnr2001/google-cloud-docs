---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/object-v1/
title: KRM API object.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:43.027558+00:00
---

# KRM API object.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/object-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API object.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## object.gdc.goog/v1

Contains API schema definitions for the Object Storage `v1` API group.

### Bucket

Defines the schema for the Buckets API.

_Appears in:_ \- BucketList

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `Bucket`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketSpec_ |   
`status` _BucketStatus_ |   
  
### BucketInfo

Defines the schema for the BucketInfo API.

_Appears in:_ \- BucketInfoList

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `BucketInfo`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BucketInfoSpec_ |   
`status` _BucketInfoStatus_ |   
  
### BucketInfoList

Contains a list of BucketInfos.

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `BucketInfoList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BucketInfo array_ |   
  
### BucketInfoSpec

BucketInfoSpec defines the desired state of the BucketInfo Resource.

_Appears in:_ \- BucketInfo

Field | Description  
---|---  
`description` _string_ | The description of bucket contents.  
`storageClass` _ObjectStorageClass_ | Defines how frequently data needs to be accessed. The available options include `Standard` and `Nearline`. `Standard` is appropriate for hot data that is accessed frequently, such as websites, streaming videos, and mobile apps. It is used for data that can be stored for at least 30 days. `Nearline` is appropriate for data that can be stored for at least 60 days, including data backup and long-tail multimedia content.  
`bucketPolicy` _GlobalBucketPolicy_ | Defines policies of the bucket resource. If unspecified, default policies are applied.  
`location` _string_ | Defines the physical place where object data in the bucket resides. If unspecified, defaults to the location in which the bucket is being created.  
`bucketName` _string_ | The non-namespaced name of the provisioned bucket. This is used to refer to the bucket when using local tools and libraries.  
`zonalEndpoints` _string array_ | Zonal DNS endpoints at which the bucket is reachable. Use these endpoints if customized failover is required.  
`globalEndpoint` _string_ | Global endpoint which will dynamically route traffic to any zone which contains data for this bucket. Use this endpoint if automatic failover is required.  
`region` _string_ | The region where the bucket is stored.  
`encryption` _EncryptionStatus_ | The status of the encryption on the bucket.  
`allowDegradedWrites` _boolean_ | Only used for synchronous buckets. Determines if S3 operations should revert to asynchronous replication due to one of the replication zones being unavailable. This prevents synchronous buckets from becoming read-only in the event that one of the replication zones is down. If empty, defaults to false.  
  
### BucketInfoStatus

Defines the observed state of the BucketInfo.

_Appears in:_ \- BucketInfo

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### BucketList

Contains a list of Buckets.

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `BucketList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Bucket array_ |   
  
### BucketPolicy

Defines policies of the Bucket.

_Appears in:_ \- BucketSpec

Field | Description  
---|---  
`lockingPolicy` _LockingPolicy_ | Policy for object locking. When set, object versioning is enabled and all objects stored in the bucket will be subject to this policy. A locked object cannot be deleted until the lock expires. Can only be enabled when creating the bucket and cannot be disabled afterwards. When not enabled, object locking and versioning are disabled and cannot be enabled.  
`corsPolicy` _CorsPolicy_ | Policy for custom CORS policy user set on the bucket. CorsPolicy has to be enabled when additional CORS policy is needed on the buckets. Otherwise, the bucket will only have the default UI console CORS policy. CorsPolicy can always be added or modified later after the bucket is created.  
`lifecyclePolicy` _LifecyclePolicy_ | Policy for custom lifecycle policy user set on the bucket. LifecyclePolicy can always be added, modified, removed later after the bucket is created.  
  
### BucketSpec

BucketSpec defines the desired state of the Bucket Resource.

_Appears in:_ \- Bucket

Field | Description  
---|---  
`description` _string_ | Description of bucket contents.  
`storageClass` _ObjectStorageClass_ | Defines how frequently data needs to be accessed. The available options include `Standard` and `Nearline`. `Standard` is appropriate for hot data that is accessed frequently, such as websites, streaming videos, and mobile apps. It is used for data that can be stored for at least 30 days. `Nearline` is appropriate for data that can be stored for at least 60 days, including data backup and long-tail multimedia content.  
`bucketPolicy` _BucketPolicy_ | Defines policies of the bucket resource. If unspecified, default policies are applied.  
`location` _string_ | Defines the physical place where object data in the bucket resides. If unspecified, defaults to the location in which the bucket is being created.  
  
### BucketStatus

Defines the observed state of the Bucket.

_Appears in:_ \- Bucket

Field | Description  
---|---  
`fullyQualifiedName` _string_ | The name of the provisioned bucket. This name is used to refer to the bucket when using external tools and libraries.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Specifies the status of the bucket. Supported conditions include `BucketReady`. If BucketReady is `True`, it indicates the bucket has been provisioned and is ready for use.  
`endpoint` _string_ | The DNS endpoint at which the bucket is reachable.  
`region` _string_ | The region where the bucket is stored.  
`encryption` _EncryptionStatus_ | The status of the encryption on the bucket.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with the observed times included.  
  
### CorsPolicy

Defines the strategy for setting up custom CORS policy on the bucket.

_Appears in:_ \- BucketPolicy \- GlobalBucketPolicy

Field | Description  
---|---  
`enableCorsPolicy` _boolean_ | Defines whether the user wants the custom policy to take effect on the bucket. If yes, the custom policy defined in CorsDetail will be read. Otherwise, CorsDetail would not be used even if it has custom policy set up.  
`corsDetail` _CorsRule array_ | Detail of the custom CORS policy being set.  
  
### CorsRule

Defines the information related with CORS rule.

_Appears in:_ \- CorsPolicy

Field | Description  
---|---  
`allowedHeaders` _string array_ | Headers that are specified in the Access-Control-Request-Headers header.  
`allowedMethods` _string array_ | HTTP methods that are permitted to be executed by an allowed origin.  
`allowedOrigins` _string array_ | Origins that can access the bucket.  
`exposeHeaders` _string array_ | Headers in the response that can be accessed.  
`id` _string_ | Unique identifier for the rule. The value can not be longer than 255 characters.  
  
### EncryptionStatus

EncryptionStatus defines the status of the encryption on the bucket.

_Appears in:_ \- BucketInfoSpec \- BucketStatus

Field | Description  
---|---  
`type` _EncryptionType_ | Defines the type of encryption to be used for the bucket. Available options are: - CMEK - Customer Managed Encryption Key which creates a KMS backed key rooted in the HSM which the customer is billed for. The customer can access these keys and manage them through KMS.  
`keyRef` _[ObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectreference-v1-core)_ | KeyRef references the key which is used as the default key to encrypt objects in the bucket.  
  
### GlobalBucketPolicy

Defines policies of the Bucket.

_Appears in:_ \- BucketInfoSpec

Field | Description  
---|---  
`lockingPolicy` _LockingPolicy_ | Policy for object locking. When set, object versioning is enabled and all objects stored in the bucket will be subject to this policy. A locked object cannot be deleted until the lock expires. Can only be enabled when creating the bucket and cannot be disabled afterwards.  
`corsPolicy` _CorsPolicy_ | Policy for custom CORS policy user set on the bucket. CorsPolicy has to be enabled when additional CORS policy is needed on the buckets. Otherwise, the bucket will only have the default UI console CORS policy. CorsPolicy can always be added or modified later after the bucket is created.  
`lifecyclePolicy` _LifecyclePolicy_ | Policy for custom lifecycle policy user set on the bucket. LifecyclePolicy can always be added, modified, removed later after the bucket is created.  
  
### LifecycleExpiration

_Appears in:_ \- LifecycleRule

Field | Description  
---|---  
`date` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Specific date when the objects should be deleted.  
`days` _integer_ | Number of days this object is subject to the rule.  
  
### LifecycleNoncurrentExpiration

_Appears in:_ \- LifecycleRule

Field | Description  
---|---  
`noncurrentDays` _integer_ | Number of days an object is noncurrent before lifecycle rules takes the action.  
  
### LifecyclePolicy

_Appears in:_ \- BucketPolicy \- GlobalBucketPolicy

Field | Description  
---|---  
`enable` _boolean_ | Defines whether the user wants to enable custom lifecycle policy on the bucket.  
`lifecycleRules` _LifecycleRule array_ | Consists of one or more lifecycle configuration rules that can take expiration action on objects in the bucket.  
  
### LifecycleRule

_Appears in:_ \- LifecyclePolicy

Field | Description  
---|---  
`id` _string_ | Unique identifier for the rule. The value cannot be longer than 255 characters.  
`status` _LifecycleRuleStatus_ | Status of the lifecycle rule. Indicate whether this rule takes action. The status can always be changed, and only Enabled rule would take effect.  
`expiration` _LifecycleExpiration_ | Expiration behavior for objects in current version. Either Expiration or NoncurrentExpiration, or both should be provided. Rule without expiration behavior would be ignored.  
`noncurrentExpiration` _LifecycleNoncurrentExpiration_ | Expiration behavior for objects noncurrent.  
`filter` _LifecycleRuleFilter_ | Filter for the rule. Empty filer means the rule apply to all objects in the bucket.  
  
### LifecycleRuleFilter

Defines the filter that can be set on lifecycle rule.

_Appears in:_ \- LifecycleRule

Field | Description  
---|---  
`prefixFilter` _string_ | Match objects with provided prefix. Empty string of prefix means apply to all objects in the bucket.  
`tagFilters` _Tag array_ | Match objects with provided tags. The tag on object must match both the key and value exactly.  
  
### LifecycleRuleStatus

_Underlying type:_ `string`

_Appears in:_ \- LifecycleRule

### LockingPolicy

Defines the strategy for locking the objects of the Bucket.

_Appears in:_ \- BucketPolicy \- GlobalBucketPolicy

Field | Description  
---|---  
`defaultObjectRetentionDays` _integer_ | Specifies the minimum number of days that each version of every object will be retained. An object cannot be deleted during the retention period. If a bucket contains any object, it cannot be deleted either. When unspecified, no default object retention period is set. Can be modified after creation, however the change will only take effect for new objects and versions. Existing objects and versions will still use the previous value.  
  
### S3CredentialRotationRequest

S3CredentialRotationRequest is the Schema for the S3CredentialRotationRequests API

_Appears in:_ \- S3CredentialRotationRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `S3CredentialRotationRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _S3CredentialRotationRequestSpec_ |   
`status` _S3CredentialRotationRequestStatus_ |   
  
### S3CredentialRotationRequestList

S3CredentialRotationRequestList contains a list of S3CredentialRotationRequest

Field | Description  
---|---  
`apiVersion` _string_ | `object.gdc.goog/v1`  
`kind` _string_ | `S3CredentialRotationRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _S3CredentialRotationRequest array_ |   
  
### S3CredentialRotationRequestSpec

S3CredentialRotationRequestSpec defines the desired state of a S3CredentialRotationRequest. This spec is used to initiate the rotation of S3 credentials stored in a Kubernetes Secret.

_Appears in:_ \- S3CredentialRotationRequest

Field | Description  
---|---  
`secretName` _string_ | SecretName is the name of the Kubernetes Secret containing the S3 credentials that need to be rotated. The Secret must exist in the same namespace as this S3CredentialRotationRequest.  
`expirationDelay` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | ExpirationDelay specifies the duration for which the old, rotated S3 key will remain valid after the new key has been created. This allows for a graceful transition period for clients and applications to switch to the new credentials. If not specified, this value is defaulted by a defaulting webhook to 72 hours. A value of "0s" indicates that the old key should be revoked immediately after the new key is activated. The format is a duration string that is parsable by Go's time.ParseDuration function. For example, "72h", "90m", "30s". Note that units such as "d" for days are not supported. See https://pkg.go.dev/time#ParseDuration for more details on the format.  
`requestTTL` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | RequestTTL defines the time-to-live (TTL) for this S3CredentialRotationRequest object itself. The TTL timer begins after the credential rotation is complete (i.e., when the `RotationCompleted` status condition becomes `True`). After this duration, the request object will be automatically garbage collected by the system. This mechanism preserves the request as an audit record for a configurable period. If not specified, this value is defaulted by a defaulting webhook to 90 days. The format is a duration string that is parsable by Go's time.ParseDuration function. For example, "2160h" (for 90 days), "72h", "30m". Note that units such as "d" for days are not supported. See https://pkg.go.dev/time#ParseDuration for more details on the format.  
  
### S3CredentialRotationRequestStatus

S3CredentialRotationRequestStatus defines the observed state of a S3CredentialRotationRequest. It provides feedback on the progress and outcome of the credential rotation process.

_Appears in:_ \- S3CredentialRotationRequest

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the rotation request's state. It provides a detailed breakdown of the rotation process, including its current phase and any errors that may have occurred.  
`oldKeyRevocationTimestamp` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | OldKeyRevocationTimestamp is the timestamp when the old, rotated S3 key is scheduled to be permanently revoked from the backend storage system. This time is calculated by adding the ExpirationDelay to the LastTransitionTime of the RotationCompleted condition.  
  
### Tag

Defines the tags on object that can be used by lifecycle filter.

_Appears in:_ \- LifecycleRuleFilter

Field | Description  
---|---  
`key` _string_ |   
`value` _string_ |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
