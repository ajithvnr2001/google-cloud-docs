---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob/
title: KMS Inventory V1 API - Class Google::Cloud::Kms::V1::ImportJob (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:04.656020+00:00
---

# KMS Inventory V1 API - Class Google::Cloud::Kms::V1::ImportJob (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  KMS Inventory V1 API - Class Google::Cloud::Kms::V1::ImportJob (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.2  0.15.1  0.14.1  0.13.0  0.12.2  0.11.3  0.10.0  0.9.1  0.8.3  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the KMS Inventory V1 API class Google::Cloud::Kms::V1::ImportJob.

An [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") can be used to create [CryptoKeys](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") and [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") using pre-existing key material, generated outside of Cloud KMS.

When an [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") is created, Cloud KMS will generate a "wrapping key", which is a public/private key pair. You use the wrapping key to encrypt (also known as wrap) the pre-existing key material to protect it during the import process. The nature of the wrapping key depends on the choice of [import_method](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob#Google__Cloud__Kms__V1__ImportJob_import_method_instance_ "Google::Cloud::Kms::V1::ImportJob#import_method \(method\)"). When the wrapping key generation is complete, the [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob#Google__Cloud__Kms__V1__ImportJob_state_instance_ "Google::Cloud::Kms::V1::ImportJob#state \(method\)") will be set to [ACTIVE](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportJobState#Google__Cloud__Kms__V1__ImportJob__ImportJobState__ACTIVE "Google::Cloud::Kms::V1::ImportJob::ImportJobState::ACTIVE \(constant\)") and the [public_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob#Google__Cloud__Kms__V1__ImportJob_public_key_instance_ "Google::Cloud::Kms::V1::ImportJob#public_key \(method\)") can be fetched. The fetched public key can then be used to wrap your pre-existing key material.

Once the key material is wrapped, it can be imported into a new [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") in an existing [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") by calling [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]. Multiple [CryptoKeyVersions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)") can be imported with a single [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). Cloud KMS uses the private key portion of the wrapping key to unwrap the key material. Only Cloud KMS has access to the private key.

An [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") expires 3 days after it is created. Once expired, Cloud KMS will no longer be able to import or unwrap any key material that was wrapped with the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)")'s public key.

For more information, see [Importing a key](https://cloud.google.com/kms/docs/importing-a-key).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attestation
    
    
    def attestation() -> ::Google::Cloud::Kms::V1::KeyOperationAttestation

**Returns**

  * ([::Google::Cloud::Kms::V1::KeyOperationAttestation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-KeyOperationAttestation)) — Output only. Statement that was generated and signed by the key creator (for example, an HSM) at key creation time. Use this statement to verify attributes of the key as stored on the HSM, independently of Google. Only present if the chosen [ImportMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportMethod "Google::Cloud::Kms::V1::ImportJob::ImportMethod \(module\)") is one with a protection level of [HSM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel#Google__Cloud__Kms__V1__ProtectionLevel__HSM "Google::Cloud::Kms::V1::ProtectionLevel::HSM \(constant\)"). 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which this [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") was created. 



### #crypto_key_backend
    
    
    def crypto_key_backend() -> ::String

**Returns**

  * (::String) — 

Immutable. The resource name of the backend environment where the key material for the wrapping key resides and where all related cryptographic operations are performed. Currently, this field is only populated for keys stored in HSM_SINGLE_TENANT. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. Supported resources:

    * `"projects/*/locations/*/singleTenantHsmInstances/*"`



### #crypto_key_backend=
    
    
    def crypto_key_backend=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Immutable. The resource name of the backend environment where the key material for the wrapping key resides and where all related cryptographic operations are performed. Currently, this field is only populated for keys stored in HSM_SINGLE_TENANT. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. Supported resources:

    * `"projects/*/locations/*/singleTenantHsmInstances/*"`



**Returns**

  * (::String) — 

Immutable. The resource name of the backend environment where the key material for the wrapping key resides and where all related cryptographic operations are performed. Currently, this field is only populated for keys stored in HSM_SINGLE_TENANT. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel "Google::Cloud::Kms::V1::ProtectionLevel \(module\)") in the future. Supported resources:

    * `"projects/*/locations/*/singleTenantHsmInstances/*"`



### #expire_event_time
    
    
    def expire_event_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") expired. Only present if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob#Google__Cloud__Kms__V1__ImportJob_state_instance_ "Google::Cloud::Kms::V1::ImportJob#state \(method\)") is [EXPIRED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportJobState#Google__Cloud__Kms__V1__ImportJob__ImportJobState__EXPIRED "Google::Cloud::Kms::V1::ImportJob::ImportJobState::EXPIRED \(constant\)"). 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time at which this [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") is scheduled for expiration and can no longer be used to import key material. 



### #generate_time
    
    
    def generate_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)")'s key material was generated. 



### #import_method
    
    
    def import_method() -> ::Google::Cloud::Kms::V1::ImportJob::ImportMethod

**Returns**

  * ([::Google::Cloud::Kms::V1::ImportJob::ImportMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportMethod)) — Required. Immutable. The wrapping method to be used for incoming key material. 



### #import_method=
    
    
    def import_method=(value) -> ::Google::Cloud::Kms::V1::ImportJob::ImportMethod

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::ImportJob::ImportMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportMethod)) — Required. Immutable. The wrapping method to be used for incoming key material. 



**Returns**

  * ([::Google::Cloud::Kms::V1::ImportJob::ImportMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportMethod)) — Required. Immutable. The wrapping method to be used for incoming key material. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name for this [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)") in the format `projects/*/locations/*/keyRings/*/importJobs/*`. 



### #protection_level
    
    
    def protection_level() -> ::Google::Cloud::Kms::V1::ProtectionLevel

**Returns**

  * ([::Google::Cloud::Kms::V1::ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel)) — Required. Immutable. The protection level of the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). This must match the [protection_level](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate#Google__Cloud__Kms__V1__CryptoKeyVersionTemplate_protection_level_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersionTemplate#protection_level \(method\)") of the [version_template](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_version_template_instance_ "Google::Cloud::Kms::V1::CryptoKey#version_template \(method\)") on the [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") you attempt to import into. 



### #protection_level=
    
    
    def protection_level=(value) -> ::Google::Cloud::Kms::V1::ProtectionLevel

**Parameter**

  * **value** ([::Google::Cloud::Kms::V1::ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel)) — Required. Immutable. The protection level of the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). This must match the [protection_level](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate#Google__Cloud__Kms__V1__CryptoKeyVersionTemplate_protection_level_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersionTemplate#protection_level \(method\)") of the [version_template](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_version_template_instance_ "Google::Cloud::Kms::V1::CryptoKey#version_template \(method\)") on the [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") you attempt to import into. 



**Returns**

  * ([::Google::Cloud::Kms::V1::ProtectionLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ProtectionLevel)) — Required. Immutable. The protection level of the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"). This must match the [protection_level](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersionTemplate#Google__Cloud__Kms__V1__CryptoKeyVersionTemplate_protection_level_instance_ "Google::Cloud::Kms::V1::CryptoKeyVersionTemplate#protection_level \(method\)") of the [version_template](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_version_template_instance_ "Google::Cloud::Kms::V1::CryptoKey#version_template \(method\)") on the [CryptoKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-CryptoKey "Google::Cloud::Kms::V1::CryptoKey \(class\)") you attempt to import into. 



### #public_key
    
    
    def public_key() -> ::Google::Cloud::Kms::V1::ImportJob::WrappingPublicKey

**Returns**

  * ([::Google::Cloud::Kms::V1::ImportJob::WrappingPublicKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-WrappingPublicKey)) — Output only. The public key with which to wrap key material prior to import. Only returned if [state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob#Google__Cloud__Kms__V1__ImportJob_state_instance_ "Google::Cloud::Kms::V1::ImportJob#state \(method\)") is [ACTIVE](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportJobState#Google__Cloud__Kms__V1__ImportJob__ImportJobState__ACTIVE "Google::Cloud::Kms::V1::ImportJob::ImportJobState::ACTIVE \(constant\)"). 



### #public_key_format
    
    
    def public_key_format() -> ::Google::Cloud::Kms::V1::PublicKey::PublicKeyFormat

**Returns**

  * ([::Google::Cloud::Kms::V1::PublicKey::PublicKeyFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-PublicKey-PublicKeyFormat)) — Output only. Specifies the [WrappingPublicKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-WrappingPublicKey "Google::Cloud::Kms::V1::ImportJob::WrappingPublicKey \(class\)") format provided by the customer in the [KeyManagementService.GetImportJob][google.cloud.kms.v1.KeyManagementService.GetImportJob] request. 



### #state
    
    
    def state() -> ::Google::Cloud::Kms::V1::ImportJob::ImportJobState

**Returns**

  * ([::Google::Cloud::Kms::V1::ImportJob::ImportJobState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob-ImportJobState)) — Output only. The current state of the [ImportJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-V1-ImportJob "Google::Cloud::Kms::V1::ImportJob \(class\)"), indicating if it can be used. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
