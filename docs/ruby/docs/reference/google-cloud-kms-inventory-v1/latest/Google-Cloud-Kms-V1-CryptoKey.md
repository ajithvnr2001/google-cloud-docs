---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey/
title: KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKey (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:03.554153+00:00
---

# KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKey (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKey (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.2  0.15.1  0.14.1  0.13.0  0.12.2  0.11.3  0.10.0  0.9.1  0.8.3  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the KMS Inventory V1 API class Google::Cloud::Kms::V1::CryptoKey.

A [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") represents a logical key that can be used for cryptographic operations.

A [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") is made up of zero or more [versions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"), which represent the actual key material used in cryptographic operations.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") was created. 



### #crypto_key_backend
    
    
    def crypto_key_backend() -> ::String

**Returns**

  * (::String) — Immutable. The resource name of the backend environment where the key material for all [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") associated with this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") reside and where all related cryptographic operations are performed. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)"), with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"), with the resource name in the format `projects/*/locations/*/singleTenantHsmInstances/*`. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. 



### #crypto_key_backend=
    
    
    def crypto_key_backend=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The resource name of the backend environment where the key material for all [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") associated with this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") reside and where all related cryptographic operations are performed. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)"), with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"), with the resource name in the format `projects/*/locations/*/singleTenantHsmInstances/*`. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. 



**Returns**

  * (::String) — Immutable. The resource name of the backend environment where the key material for all [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") associated with this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") reside and where all related cryptographic operations are performed. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)"), with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Only applicable if [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") have a [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") of [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"), with the resource name in the format `projects/*/locations/*/singleTenantHsmInstances/*`. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. 



### #destroy_scheduled_duration
    
    
    def destroy_scheduled_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — Immutable. The period of time that versions of this key spend in the [DESTROY_SCHEDULED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROY_SCHEDULED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROY_SCHEDULED \(constant\)") state before transitioning to [DESTROYED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROYED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROYED \(constant\)"). If not specified at creation time, the default duration is 30 days. 



### #destroy_scheduled_duration=
    
    
    def destroy_scheduled_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — Immutable. The period of time that versions of this key spend in the [DESTROY_SCHEDULED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROY_SCHEDULED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROY_SCHEDULED \(constant\)") state before transitioning to [DESTROYED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROYED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROYED \(constant\)"). If not specified at creation time, the default duration is 30 days. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — Immutable. The period of time that versions of this key spend in the [DESTROY_SCHEDULED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROY_SCHEDULED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROY_SCHEDULED \(constant\)") state before transitioning to [DESTROYED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROYED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROYED \(constant\)"). If not specified at creation time, the default duration is 30 days. 



### #import_only
    
    
    def import_only() -> ::Boolean

**Returns**

  * (::Boolean) — Immutable. Whether this key may contain imported versions only. 



### #import_only=
    
    
    def import_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Immutable. Whether this key may contain imported versions only. 



**Returns**

  * (::Boolean) — Immutable. Whether this key may contain imported versions only. 



### #key_access_justifications_policy
    
    
    def key_access_justifications_policy() -> ::Google::Cloud::Kms::V1::KeyAccessJustificationsPolicy

**Returns**

  * ([::Google::Cloud::Kms::V1::KeyAccessJustificationsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-KeyAccessJustificationsPolicy)) — Optional. The policy used for Key Access Justifications Policy Enforcement. If this field is present and this key is enrolled in Key Access Justifications Policy Enforcement, the policy will be evaluated in encrypt, decrypt, and sign operations, and the operation will fail if rejected by the policy. The policy is defined by specifying zero or more allowed justification codes. https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes By default, this field is absent, and all justification codes are allowed. If the `key_access_justifications_policy.allowed_access_reasons` is empty (zero allowed justification code), all encrypt, decrypt, and sign operations will fail. 



### #key_access_justifications_policy=
    
    
    def key_access_justifications_policy=(value) -> ::Google::Cloud::Kms::V1::KeyAccessJustificationsPolicy

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::KeyAccessJustificationsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-KeyAccessJustificationsPolicy)) — Optional. The policy used for Key Access Justifications Policy Enforcement. If this field is present and this key is enrolled in Key Access Justifications Policy Enforcement, the policy will be evaluated in encrypt, decrypt, and sign operations, and the operation will fail if rejected by the policy. The policy is defined by specifying zero or more allowed justification codes. https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes By default, this field is absent, and all justification codes are allowed. If the `key_access_justifications_policy.allowed_access_reasons` is empty (zero allowed justification code), all encrypt, decrypt, and sign operations will fail. 



**Returns**

  * ([::Google::Cloud::Kms::V1::KeyAccessJustificationsPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-KeyAccessJustificationsPolicy)) — Optional. The policy used for Key Access Justifications Policy Enforcement. If this field is present and this key is enrolled in Key Access Justifications Policy Enforcement, the policy will be evaluated in encrypt, decrypt, and sign operations, and the operation will fail if rejected by the policy. The policy is defined by specifying zero or more allowed justification codes. https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes By default, this field is absent, and all justification codes are allowed. If the `key_access_justifications_policy.allowed_access_reasons` is empty (zero allowed justification code), all encrypt, decrypt, and sign operations will fail. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name for this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`. 



### #next_rotation_time
    
    
    def next_rotation_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — At [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)"), the Key Management Service will automatically:

    1. Create a new version of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)").
    2. Mark the new version as primary.

Key rotations performed manually via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] and [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion] do not affect [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)").

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




### #next_rotation_time=
    
    
    def next_rotation_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — At [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)"), the Key Management Service will automatically:

    1. Create a new version of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)").
    2. Mark the new version as primary.

Key rotations performed manually via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] and [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion] do not affect [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)").

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — At [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)"), the Key Management Service will automatically:

    1. Create a new version of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)").
    2. Mark the new version as primary.

Key rotations performed manually via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] and [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion] do not affect [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)").

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




### #primary
    
    
    def primary() -> ::Google::Cloud::Kms::V1::CryptoKeyVersion

**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion)) — Output only. A copy of the "primary" [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") that will be used by [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt] when this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") is given in [EncryptRequest.name][google.cloud.kms.v1.EncryptRequest.name].

The [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)")'s primary version can be updated via [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") may have a primary. For other keys, this field will be omitted. 




### #purpose
    
    
    def purpose() -> ::Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose

**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose)) — Immutable. The immutable purpose of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)"). 



### #purpose=
    
    
    def purpose=(value) -> ::Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose)) — Immutable. The immutable purpose of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)"). 



**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose)) — Immutable. The immutable purpose of this [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)"). 



### #rotation_period
    
    
    def rotation_period() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_rotation_period_instance_ "Google::Cloud::Kms::V1::CryptoKey#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") must also be set.

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




### #rotation_period=
    
    
    def rotation_period=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_rotation_period_instance_ "Google::Cloud::Kms::V1::CryptoKey#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") must also be set.

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Duration)) — [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.

If [rotation_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_rotation_period_instance_ "Google::Cloud::Kms::V1::CryptoKey#rotation_period \(method\)") is set, [next_rotation_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_next_rotation_time_instance_ "Google::Cloud::Kms::V1::CryptoKey#next_rotation_time \(method\)") must also be set.

Keys with [purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)") support automatic rotation. For other keys, this field must be omitted. 




### #version_template
    
    
    def version_template() -> ::Google::Cloud::Kms::V1::CryptoKeyVersionTemplate

**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate)) — A template describing settings for new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances. The properties of new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances created by either [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or auto-rotation are controlled by this template. 



### #version_template=
    
    
    def version_template=(value) -> ::Google::Cloud::Kms::V1::CryptoKeyVersionTemplate

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::CryptoKeyVersionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate)) — A template describing settings for new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances. The properties of new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances created by either [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or auto-rotation are controlled by this template. 



**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate)) — A template describing settings for new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances. The properties of new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") instances created by either [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or auto-rotation are controlled by this template. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
