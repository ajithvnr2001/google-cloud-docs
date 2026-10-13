---
url: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets
title: REST Resource: billingAccounts.locations.buckets \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:22.647536+00:00
---

# REST Resource: billingAccounts.locations.buckets  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  REST Resource: billingAccounts.locations.buckets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LogBucket
    * JSON representation
    * IndexConfig
      * JSON representation
    * IndexType
    * CmekSettings
      * JSON representation
  * Methods



## Resource: LogBucket

Describes a repository in which log entries are stored.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "retentionDays": integer,
      "locked": boolean,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LifecycleState)),
      "analyticsEnabled": boolean,
      "restrictedFields": [
        string
      ],
      "indexConfigs": [
        {
          object ([IndexConfig](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig))
        }
      ],
      "cmekSettings": {
        object ([CmekSettings](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.CmekSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the bucket.For example:`projects/my-project/locations/global/buckets/my-bucket`For a list of supported locations, see [Supported Regions](https://docs.cloud.google.com/logging/docs/region-support)For the location of `global` it is unspecified where log entries are actually stored.After a bucket has been created, the location cannot be changed.  
`description` |  `string` Optional. Describes this bucket.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of the bucket. This is not set for any of the default buckets.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of the bucket.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`retentionDays` |  `integer` Optional. Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.  
`locked` |  `boolean` Optional. Whether the bucket is locked.The retention period on a locked bucket cannot be changed. Locked buckets may only be deleted if they are empty.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LifecycleState)`)` Output only. The bucket lifecycle state.  
`analyticsEnabled` |  `boolean` Optional. Whether log analytics is enabled for this bucket.Once enabled, log analytics features cannot be disabled.  
`restrictedFields[]` |  `string` Optional. Log entry field paths that are denied access in this bucket.The following fields and their children are eligible: `textPayload`, `jsonPayload`, `protoPayload`, `httpRequest`, `labels`, `sourceLocation`.Restricting a repeated field will restrict all values. Adding a parent will block all child fields. (e.g. `foo.bar` will block `foo.bar.baz`)  
`indexConfigs[]` |  `object (`[IndexConfig](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexConfig)`)` Optional. A list of indexed fields and related configuration data.  
`cmekSettings` |  `object (`[CmekSettings](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.CmekSettings)`)` Optional. The CMEK settings of the log bucket. If present, new log entries written to this log bucket are encrypted using the CMEK key provided in this configuration. If a log bucket has CMEK settings, the CMEK settings cannot be disabled later by updating the log bucket. Changing the KMS key is allowed.  
  
### IndexConfig

Configuration for an indexed field.

JSON representation  
---  
      
    
    {
      "fieldPath": string,
      "type": enum ([IndexType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexType)),
      "createTime": string
    }  
  
Fields  
---  
`fieldPath` |  `string` Required. The LogEntry field path to index.Note that some paths are automatically indexed, and other paths are not eligible for indexing. See [indexing documentation]( <https://docs.cloud.google.com/logging/docs/analyze/custom-index>) for details.For example: `jsonPayload.request.status`  
`type` |  `enum (`[IndexType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets#LogBucket.IndexType)`)` Required. The type of data in this index.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the index was last modified.This is used to return the timestamp, and will be ignored if supplied during update.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### IndexType

IndexType is used for custom indexing. It describes the type of an indexed field.

Enums  
---  
`INDEX_TYPE_UNSPECIFIED` | The index's type is unspecified.  
`INDEX_TYPE_STRING` | The index is a string-type index.  
`INDEX_TYPE_INTEGER` | The index is a integer-type index.  
  
### CmekSettings

Describes the customer-managed encryption key (CMEK) settings associated with a project, folder, organization, billing account, or flexible resource.

Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

See [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) for more information.

JSON representation  
---  
      
    
    {
      "name": string,
      "kmsKeyName": string,
      "kmsKeyVersionName": string,
      "serviceAccountId": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the CMEK settings.  
`kmsKeyName` |  `string` Optional. The resource name for the configured Cloud KMS key.KMS key name format:
    
    
    "projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]"
    

For example:`"projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key"`To enable CMEK for the Log Router, set this field to a valid `kmsKeyName` for which the associated service account has the needed cloudkms.cryptoKeyEncrypterDecrypter roles assigned for the key.The Cloud KMS key used by the Log Router can be updated by changing the `kmsKeyName` to a new valid key name or disabled by setting the key name to an empty string. Encryption operations that are in progress will be completed with the key that was in use when they started. Decryption operations will be completed using the key that was used at the time of encryption unless access to that key has been revoked.To disable CMEK for the Log Router, set this field to an empty string.See [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) for more information.  
`kmsKeyVersionName` |  `string` Output only. The CryptoKeyVersion resource name for the configured Cloud KMS key.KMS key name format:
    
    
    "projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]/cryptoKeyVersions/[VERSION]"
    

For example:`"projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key/cryptoKeyVersions/1"`This is a read-only field used to convey the specific configured CryptoKeyVersion of `kms_key` that has been configured. It will be populated in cases where the CMEK settings are bound to a single key version.If this field is populated, the `kms_key` is tied to a specific CryptoKeyVersion.  
`serviceAccountId` |  `string` Output only. The service account that will be used by the Log Router to access your Cloud KMS key.Before enabling CMEK for Log Router, you must first assign the cloudkms.cryptoKeyEncrypterDecrypter role to the service account that the Log Router will use to access your Cloud KMS key. Use `[v2.getCmekSettings](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getCmekSettings#google.logging.v2.ConfigServiceV2.GetCmekSettings)` to obtain the service account ID.See [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) for more information.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/create)`

|  Creates a log bucket that can be used to store log entries.  
  
### `[createAsync](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/createAsync)`

|  Creates a log bucket asynchronously that can be used to store log entries.  
  
### `[delete](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/delete)`

|  Deletes a log bucket.  
  
### `[get](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/get)`

|  Gets a log bucket.  
  
### `[list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/list)`

|  Lists log buckets.  
  
### `[patch](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/patch)`

|  Updates a log bucket.  
  
### `[undelete](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/undelete)`

|  Undeletes a log bucket.  
  
### `[updateAsync](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets/updateAsync)`

|  Updates a log bucket asynchronously.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-27 UTC."],[],[]] 
