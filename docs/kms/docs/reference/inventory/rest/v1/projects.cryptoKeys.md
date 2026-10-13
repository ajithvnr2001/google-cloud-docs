---
url: https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys
title: REST Resource: projects.cryptoKeys \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:44.938967+00:00
---

# REST Resource: projects.cryptoKeys  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  REST Resource: projects.cryptoKeys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CryptoKey
    * JSON representation
  * Methods



## Resource: CryptoKey

A [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) represents a logical key that can be used for cryptographic operations.

A [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) is made up of zero or more [versions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion), which represent the actual key material used in cryptographic operations.

JSON representation  
---  
      
    
    {
      "name": string,
      "primary": {
        object ([CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion))
      },
      "purpose": enum ([CryptoKeyPurpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)),
      "createTime": string,
      "nextRotationTime": string,
      "versionTemplate": {
        object ([CryptoKeyVersionTemplate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyVersionTemplate))
      },
      "labels": {
        string: string,
        ...
      },
      "importOnly": boolean,
      "destroyScheduledDuration": string,
      "cryptoKeyBackend": string,
      "keyAccessJustificationsPolicy": {
        object ([KeyAccessJustificationsPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#KeyAccessJustificationsPolicy))
      },
    
      // Union field rotation_schedule can be only one of the following:
      "rotationPeriod": string
      // End of list of possible types for union field rotation_schedule.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name for this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.  
`primary` |  `object ([CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion))` Output only. A copy of the "primary" [CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) that will be used by [Encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt#google.cloud.kms.v1.KeyManagementService.Encrypt) when this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) is given in [EncryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt#body.PATH_PARAMETERS.name).The [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)'s primary version can be updated via [UpdateCryptoKeyPrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion).Keys with [purpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose) [ENCRYPT_DECRYPT](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose.ENUM_VALUES.ENCRYPT_DECRYPT) may have a primary. For other keys, this field will be omitted.  
`purpose` |  `enum ([CryptoKeyPurpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose))` Immutable. The immutable purpose of this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey).  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextRotationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` At [nextRotationTime](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time), the Key Management Service will automatically:

  1. Create a new version of this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey).
  2. Mark the new version as primary.

Key rotations performed manually via [CreateCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create#google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion) and [UpdateCryptoKeyPrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion) do not affect [nextRotationTime](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time).Keys with [purpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose) [ENCRYPT_DECRYPT](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose.ENUM_VALUES.ENCRYPT_DECRYPT) support automatic rotation. For other keys, this field must be omitted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`versionTemplate` |  `object ([CryptoKeyVersionTemplate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyVersionTemplate))` A template describing settings for new [CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) instances. The properties of new [CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) instances created by either [CreateCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create#google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion) or auto-rotation are controlled by this template.  
`labels` |  `map (key: string, value: string)` Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).  
`importOnly` |  `boolean` Immutable. Whether this key may contain imported versions only.  
`destroyScheduledDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Immutable. The period of time that versions of this key spend in the [DESTROY_SCHEDULED](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.DESTROY_SCHEDULED) state before transitioning to [DESTROYED](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.DESTROYED). If not specified at creation time, the default duration is 30 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`cryptoKeyBackend` |  `string` Immutable. The resource name of the backend environment where the key material for all [CryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) associated with this [CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) reside and where all related cryptographic operations are performed. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) have a [ProtectionLevel](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel) of [EXTERNAL_VPC](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel#ENUM_VALUES.EXTERNAL_VPC), with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion) have a [ProtectionLevel](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel) of [HSM_SINGLE_TENANT](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel#ENUM_VALUES.HSM_SINGLE_TENANT), with the resource name in the format `projects/*/locations/*/singleTenantHsmInstances/*`. Note, this list is non-exhaustive.  
`keyAccessJustificationsPolicy` |  `object ([KeyAccessJustificationsPolicy](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#KeyAccessJustificationsPolicy))` Optional. The policy used for Key Access Justifications Policy Enforcement. If this field is present and this key is enrolled in Key Access Justifications Policy Enforcement, the policy will be evaluated in encrypt, decrypt, and sign operations, and the operation will fail if rejected by the policy. The policy is defined by specifying zero or more allowed justification codes. <https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes> By default, this field is absent, and all justification codes are allowed. If the `keyAccessJustificationsPolicy.allowed_access_reasons` is empty (zero allowed justification code), all encrypt, decrypt, and sign operations will fail.  
Union field `rotation_schedule`. Controls the rate of automatic rotation. `rotation_schedule` can be only one of the following:  
`rotationPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` [nextRotationTime](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time) will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.If [rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period) is set, [nextRotationTime](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time) must also be set.Keys with [purpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.purpose) [ENCRYPT_DECRYPT](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose.ENUM_VALUES.ENCRYPT_DECRYPT) support automatic rotation. For other keys, this field must be omitted.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/kms/docs/reference/inventory/rest/v1/projects.cryptoKeys/list)`

|  Returns cryptographic keys managed by Cloud KMS in a given Cloud project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
