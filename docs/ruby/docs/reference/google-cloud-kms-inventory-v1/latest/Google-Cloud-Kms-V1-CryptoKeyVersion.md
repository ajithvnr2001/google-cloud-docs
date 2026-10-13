---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion/
title: KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKeyVersion (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:08.369927+00:00
---

# KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKeyVersion (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  KMS Inventory V1 API - Class Google::Cloud::Kms::V1::CryptoKeyVersion (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.2  0.15.1  0.14.1  0.13.0  0.12.2  0.11.3  0.10.0  0.9.1  0.8.3  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the KMS Inventory V1 API class Google::Cloud::Kms::V1::CryptoKeyVersion.

A [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") represents an individual cryptographic key, and the associated key material.

An [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__ENABLED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::ENABLED \(constant\)") version can be used for cryptographic operations.

For security reasons, the raw cryptographic key material represented by a [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #algorithm
    
    
    def algorithm() -> ::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm

**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm)) — Output only. The [CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm \(module\)") that this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") supports. 



### #attestation
    
    
    def attestation() -> ::Google::Cloud::Kms::V1::KeyOperationAttestation

**Returns**

  * ([::Google::Cloud::Kms::V1::KeyOperationAttestation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-KeyOperationAttestation)) — Output only. Statement that was generated and signed by the HSM at key creation time. Use this statement to verify attributes of the key as stored on the HSM, independently of Google. Only provided for key versions with [protection_level](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_protection_level_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#protection_level \(method\)") [HSM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM "Google::Cloud::Kms::V1::ProtectionLevel::HSM \(constant\)"). 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") was created. 



### #destroy_event_time
    
    
    def destroy_event_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this CryptoKeyVersion's key material was destroyed. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_state_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#state \(method\)") is [DESTROYED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROYED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROYED \(constant\)"). 



### #destroy_time
    
    
    def destroy_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)")'s key material is scheduled for destruction. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_state_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#state \(method\)") is [DESTROY_SCHEDULED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__DESTROY_SCHEDULED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::DESTROY_SCHEDULED \(constant\)"). 



### #external_destruction_failure_reason
    
    
    def external_destruction_failure_reason() -> ::String

**Returns**

  * (::String) — Output only. The root cause of the most recent external destruction failure. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_state_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#state \(method\)") is [EXTERNAL_DESTRUCTION_FAILED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__EXTERNAL_DESTRUCTION_FAILED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::EXTERNAL_DESTRUCTION_FAILED \(constant\)"). 



### #external_protection_level_options
    
    
    def external_protection_level_options() -> ::Google::Cloud::Kms::V1::ExternalProtectionLevelOptions

**Returns**

  * ([::Google::Cloud::Kms::V1::ExternalProtectionLevelOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ExternalProtectionLevelOptions)) — ExternalProtectionLevelOptions stores a group of additional fields for configuring a [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") that are specific to the [EXTERNAL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL \(constant\)") protection level and [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)") protection levels. 



### #external_protection_level_options=
    
    
    def external_protection_level_options=(value) -> ::Google::Cloud::Kms::V1::ExternalProtectionLevelOptions

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::ExternalProtectionLevelOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ExternalProtectionLevelOptions)) — ExternalProtectionLevelOptions stores a group of additional fields for configuring a [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") that are specific to the [EXTERNAL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL \(constant\)") protection level and [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)") protection levels. 



**Returns**

  * ([::Google::Cloud::Kms::V1::ExternalProtectionLevelOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ExternalProtectionLevelOptions)) — ExternalProtectionLevelOptions stores a group of additional fields for configuring a [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") that are specific to the [EXTERNAL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL \(constant\)") protection level and [EXTERNAL_VPC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__EXTERNAL_VPC "Google::Cloud::Kms::V1::ProtectionLevel::EXTERNAL_VPC \(constant\)") protection levels. 



### #generate_time
    
    
    def generate_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)")'s key material was generated. 



### #generation_failure_reason
    
    
    def generation_failure_reason() -> ::String

**Returns**

  * (::String) — Output only. The root cause of the most recent generation failure. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_state_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#state \(method\)") is [GENERATION_FAILED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__GENERATION_FAILED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::GENERATION_FAILED \(constant\)"). 



### #hsm_trusted
    
    
    def hsm_trusted() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Field indicating that the key wrapping key is trusted. This field is only valid for key purpose [AES_256_WRAPPING][CryptoKey.CryptoKeyPurpose.AES_256_WRAPPING], and protection level [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"). 



### #import_failure_reason
    
    
    def import_failure_reason() -> ::String

**Returns**

  * (::String) — Output only. The root cause of the most recent import failure. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion#Google__Cloud__Kms__V1__CryptoKeyVersion_state_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersion#state \(method\)") is [IMPORT_FAILED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionState__IMPORT_FAILED "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState::IMPORT_FAILED \(constant\)"). 



### #import_job
    
    
    def import_job() -> ::String

**Returns**

  * (::String) — Output only. The name of the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") used in the most recent import of this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"). Only present if the underlying key material was imported. 



### #import_time
    
    
    def import_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)")'s key material was most recently imported. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name for this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`. 



### #protection_level
    
    
    def protection_level() -> ::Google::Cloud::Kms::V1::ProtectionLevel

**Returns**

  * ([::Google::Cloud::Kms::V1::ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel)) — Output only. The [ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") describing how crypto operations are performed with this [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"). 



### #reimport_eligible
    
    
    def reimport_eligible() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether or not this key version is eligible for reimport, by being specified as a target in [ImportCryptoKeyVersionRequest.crypto_key_version][google.cloud.kms.v1.ImportCryptoKeyVersionRequest.crypto_key_version]. 



### #state
    
    
    def state() -> ::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState

**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState)) — The current state of the [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"). 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState)) — The current state of the [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"). 



**Returns**

  * ([::Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionState)) — The current state of the [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"). 



### #trusted_wrapping_enabled
    
    
    def trusted_wrapping_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Immutable. Field indicating that the key may be wrapped by a trusted key. This field can be set for all key purposes except [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)"), and is only valid for keys with protection level [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"). This field can only be set at creation or import time via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion], or [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]. 



### #trusted_wrapping_enabled=
    
    
    def trusted_wrapping_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Immutable. Field indicating that the key may be wrapped by a trusted key. This field can be set for all key purposes except [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)"), and is only valid for keys with protection level [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"). This field can only be set at creation or import time via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion], or [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]. 



**Returns**

  * (::Boolean) — Immutable. Field indicating that the key may be wrapped by a trusted key. This field can be set for all key purposes except [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)"), and is only valid for keys with protection level [HSM_SINGLE_TENANT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM_SINGLE_TENANT "Google::Cloud::Kms::V1::ProtectionLevel::HSM_SINGLE_TENANT \(constant\)"). This field can only be set at creation or import time via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion], or [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
