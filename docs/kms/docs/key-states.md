---
url: https://docs.cloud.google.com/kms/docs/key-states/
title: Key version states \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:35.638642+00:00
---

# Key version states  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/key-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key version states Stay organized with collections  Save and categorize content based on your preferences. 

A key version has a [state](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState):

  * _Pending generation_ (`PENDING_GENERATION`): (Applies to asymmetric keys only.) This key version is still being generated. It may not be used, enabled, disabled, or destroyed yet. Cloud Key Management Service will automatically change the state to enabled as soon as the version is ready.

  * _Pending import_ (`PENDING_IMPORT`): (Applies to imported keys only.) This key version is still being imported. It may not be used, enabled, disabled, or destroyed yet. Cloud Key Management Service will automatically change the state to enabled as soon as the version is ready.

  * _Enabled_ (`ENABLED`): The key version is ready for use.

  * _Disabled_ (`DISABLED`): This key version may not be used, but the key material is still available, and the version can be [re-enabled](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version).

  * _Scheduled for destruction_ (`DESTROY_SCHEDULED`): This key version is scheduled for destruction and will be destroyed soon. While a key version is in this state, it can't be used for cryptographic operations, and requests to use the key fail. The key version can be [restored into the disabled state](https://docs.cloud.google.com/kms/docs/destroy-restore#restore) within the scheduled destruction period. This state corresponds with [Stage 2 - Soft Deletion](https://docs.cloud.google.com/security/deletion#stage_2_-_soft_deletion) in the data deletion pipeline.

  * _Destroyed_ (`DESTROYED`): This key version is destroyed, and the key material is no longer stored in Cloud KMS. If the key version was used for asymmetric or symmetric encryption, any ciphertext encrypted with this version is not recoverable. If the key version was used for digital signing, new signatures cannot be created. Additionally, for all asymmetric key versions, the public key is no longer available for download. A key version may not leave the destroyed state once entered, except [when re-imported](https://docs.cloud.google.com/kms/docs/importing-a-key#re-import_a_previously_destroyed_key). This state corresponds with [Stage 3 - Logical Deletion from Active Systems](https://docs.cloud.google.com/security/deletion#stage_3_-_logical_deletion_from_active_systems) in the data deletion pipeline, meaning key material is deleted from all active Cloud KMS systems. It takes 45 days from destruction time for key material to be deleted from all Google active and backup systems. See [Cloud KMS's deletion timeline](https://docs.cloud.google.com/kms/docs/destroy-restore#timeline) for more information.

  * _Import failed_ (`IMPORT_FAILED`): This key version could not be imported. See [Troubleshooting failed imports](https://docs.cloud.google.com/kms/docs/troubleshooting-failed-imports) for additional information about the conditions that cause import failures.


**Note:** Keys do not have states, only key versions have states.

## Changing states of a key version

The following describes how a key version can change states:

  * When a key version for an asymmetric key is created, it starts with a state of pending generation. When Cloud KMS finishes generating the key version, its state automatically changes to enabled.

  * When a key version for a symmetric key is created, it starts with a state of enabled.

  * A key version can move from enabled to disabled and from disabled to enabled using [`UpdateCryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch) and interfaces to this method. For examples, see [Enabling and disabling key versions](https://docs.cloud.google.com/kms/docs/enable-disable).

  * A key version which is enabled or disabled can move to scheduled for destruction using [`DestroyCryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/destroy) and interfaces to this method. For examples, see [Schedule a key version for destruction](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version).

  * A key version which is scheduled for destruction can be reverted to disabled using [`RestoreCryptoKeyVersion`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/restore) and interfaces to this method. For examples, see [Restore a key version](https://docs.cloud.google.com/kms/docs/destroy-restore#restore_a_key_version).




The following diagram shows the allowable states for a key version.

![Key version states](https://docs.cloud.google.com/static/kms/images/key_states.png)

Note that only key versions for asymmetric keys start in the pending generation state. Key versions for symmetric keys start in the enabled state.

## Impact of key version state on cryptographic operations

The impact of key version state on cryptographic operations depends on whether the key is used for:

  * Symmetric encryption
  * Asymmetric encryption or digital signing



### Symmetric encryption

Each symmetric encryption key has a designated _primary version_ which is used at that point in time to encrypt data. **In order for a key to be available for use to encrypt data, it needs to have a primary key version which is enabled.**

When a key is used to encrypt plaintext, its primary key version is used to encrypt that data. The information as to which version was used to encrypt data is stored in the ciphertext of the data. Only one version of a key can be primary at any given point in time.

If the primary key version is disabled, that key version cannot be used to encrypt data. Note that an enabled primary key version can be disabled, scheduled for destruction or destroyed, and a version which is not enabled can be made the primary version.

Which key version is primary does not impact the ability to decrypt data. A key version can be used to decrypt data as long as it is enabled.

### Asymmetric encryption or digital signing

Each time an asymmetric key is used for encryption or digital signing, a key version must be specified. **In order for the key version to be available for asymmetric encryption or digital signing, the key version must be enabled.** You can retrieve a key version's public key only if the key version is enabled.

## Variable duration of the _scheduled for destruction_ state

By default, keys in Cloud KMS spend 30 days in the _Scheduled for destruction_ ([soft deleted](https://docs.cloud.google.com/security/deletion#stage_2_-_soft_deletion)) state before the key material is [logically deleted](https://docs.cloud.google.com/security/deletion#stage_3_-_logical_deletion_from_active_systems) from the system. This duration may be configured, with the following caveats:

  * The duration is only configurable during key creation.
  * Once specified, the duration for the key cannot be changed.
  * The duration applies to all versions of the key created in the future.
  * The minimum duration is 24 hours for all keys, except for import-only keys which have a minimum duration of 0.
  * The maximum duration is 120 days.



The value is configured using the `destroy_scheduled_duration` field of the [CryptoKey](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#resource:-cryptokey) in the `CreateCryptoKeyRequest`.

We recommend that you use the default duration of 30 days for all keys unless you have specific application or regulatory requirements that require a different value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
