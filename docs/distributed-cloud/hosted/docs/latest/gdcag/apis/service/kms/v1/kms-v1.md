---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/kms-v1/
title: KRM API kms.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:06.915921+00:00
---

# KRM API kms.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/v1/kms-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API kms.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## kms.gdc.goog/v1

### AEADKey

Represents a cryptographic key to use for Authenticated Encryption with Associated Data (AEAD) operations.

_Appears in:_ \- AEADKeyList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `AEADKey`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _AEADKeySpec_ |   
`status` _AEADKeyStatus_ |   
  
### AEADKeyList

Represents a collection of AEADKeys.

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `AEADKeyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _AEADKey array_ |   
  
### AEADKeySpec

Provides the specification for an AEADKey.

_Appears in:_ \- AEADKey

Field | Description  
---|---  
`algorithm` _AEADAlgorithm_ |   
  
### AEADKeyStatus

Provides the status for an AEADKey.

_Appears in:_ \- AEADKey

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A report that indicates when an AEADKey creation is complete and ready for use.  
`encryptedKeyMaterial` _integer array_ | Key material encrypted by the KMS root key.  
`rootKeyID` _string_ | Identifier to the root key that wrapped the key material. Follows the format `root-key-namespace/root-key-type/root-key-name/version` Example - `kms-system/ctm/org1-root-key/1` or `kms-system/local/org-1-root-key/1`  
  
### KeyExport

Represents a request to export a key.

_Appears in:_ \- KeyExportList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `KeyExport`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _KeyExportSpec_ |   
`status` _KeyExportStatus_ |   
  
### KeyExportList

Represents a collection of KeyExport resources.

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `KeyExportList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _KeyExport array_ |   
  
### KeyExportSpec

Provides the specification for a KeyExport resource.

_Appears in:_ \- KeyExport

Field | Description  
---|---  
`context` _KeySharingContext_ | The information necessary to wrap the key to export.  
`keyToExport` _[TypedLocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#typedlocalobjectreference-v1-core)_ | A reference to the key for export.  
  
### KeyExportStatus

Provides the status for a KeyExport resource.

_Appears in:_ \- KeyExport

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The status on the KeyExport resource as successful or failed, and provides a reason for the failure.  
`exportedKey` _WrappedKey_ | The exported key material.  
  
### KeyImport

Represents a request to import a key.

_Appears in:_ \- KeyImportList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `KeyImport`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _KeyImportSpec_ |   
`status` _KeyImportStatus_ |   
  
### KeyImportList

Represents a collection of key imports.

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `KeyImportList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _KeyImport array_ |   
  
### KeyImportSpec

Provides the specification for a KeyImport resource.

_Appears in:_ \- KeyImport

Field | Description  
---|---  
`context` _KeySharingContext_ | The information from the sender to unwrap the key material to import.  
`keyToImport` _WrappedKey_ | The wrapped key material to import.  
  
### KeyImportStatus

Provides the status for a KeyImport resource.

_Appears in:_ \- KeyImport

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The status of the KeyImport resource as awaiting, successful, or failed and a reason for the failure.  
`peerContext` _PeerSharingContext_ | The information required to wrap the key to import.  
`importedKeyRef` _[TypedLocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#typedlocalobjectreference-v1-core)_ | A reference to the imported key.  
  
### KeyMetadata

Represents the attributes required to create or re-create the customer key.

_Appears in:_ \- WrappedKey

Field | Description  
---|---  
`algorithm` _string_ | The algorithm to use with the key.  
  
### KeySharingContext

Contains information by the party that initiates intent for key import and export operations.

_Appears in:_ \- KeyExportSpec \- KeyImportSpec

Field | Description  
---|---  
`mechanism` _KeySharingMechanism_ | The algorithms to use to wrap keys.  
`publicKey` _integer array_ |   
  
### PeerSharingContext

Contains information by the party that responds to the intent for key import operations.

_Appears in:_ \- KeyImportStatus

Field | Description  
---|---  
`publicKey` _integer array_ |   
`privateKey` _integer array_ |   
`rootKeyID` _string_ | Identifier to the root key that wrapped the key material. Follows the format `root-key-namespace/root-key-type/root-key-name/version` Example - `kms-system/ctm/org1-root-key/1` or `kms-system/local/org-1-root-key/1`  
  
### ProtectionLevel

ProtectionLevel bundles the cryptographic execution mode and its targeted routing backend.

_Appears in:_ \- SigningKeySpec

Field | Description  
---|---  
`mode` _ProtectionMode_ | Mode dictates the boundary and mechanism of cryptographic operations for the key.  
`cryptoBackendRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | CryptoBackendRef explicitly points to the CryptoBackend CR within this namespace. This field must be omitted when Mode is WRAPPED_BY_ROOTKEY. For all other modes, if this field is omitted, the KMS will default to routing to a backend named "default".  
  
### RotationJob

Represents a cluster level resource that runs root key rotation, and re-encryption of all KMS keys in the cluster.

_Appears in:_ \- RotationJobList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `RotationJob`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RotationJobSpec_ |   
`status` _RotationJobStatus_ |   
  
### RotationJobList

Represents a collection of RotationJob resources.

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `RotationJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _RotationJob array_ |   
  
### RotationJobSpec

Provides the specification for a RotationJob resource.

_Appears in:_ \- RotationJob

Field | Description  
---|---  
`rootKeyResourceName` _string_ | The root key name specified in the form namespaces//secrets/  
`ttlSecondsAfterCompletion` _integer_ | TTLSecondsAfterCompletion specifies how long a RotationJob should persist after it's completed. If this field is not set, it will default to 24h (86400s)  
  
### RotationJobStatus

Provides the status for a RotationJob resource.

_Appears in:_ \- RotationJob

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The status of the RotationJob resource as successful or failed, and provides a reason for the failure.  
  
### SigningKey

Represents a cryptographic key to use for creating digital signatures.

_Appears in:_ \- SigningKeyList

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `SigningKey`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _SigningKeySpec_ |   
`status` _SigningKeyStatus_ |   
  
### SigningKeyList

Represents a collection of SigningKey resources.

Field | Description  
---|---  
`apiVersion` _string_ | `kms.gdc.goog/v1`  
`kind` _string_ | `SigningKeyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _SigningKey array_ |   
  
### SigningKeySpec

Provides the specification for a SigningKey resource.

_Appears in:_ \- SigningKey

Field | Description  
---|---  
`algorithm` _SigningAlgorithm_ |   
`protectionLevel` _ProtectionLevel_ | ProtectionLevel configures how and where the key material is managed and routed. If this entire block is omitted, the KMS defaults to WRAPPED_BY_ROOTKEY ProtectionMode. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.  
`existingKeyID` _string_ | ExistingKeyID specifies the identifier of a pre-existing HSM key to onboard. The KMS uses this value to verify the key's existence during initial creation, which supports use cases like Multi-Zone. To bind to an existing key from another zone, populate this field using the KeyIdentifier found in the Status of the original SigningKey. If left empty, the KMS will generate a new key. This field is immutable and cannot be changed in spec after the SigningKey is created. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.  
  
### SigningKeyStatus

Provides the status for a SigningKey resource.

_Appears in:_ \- SigningKey

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A report that indicates when a SigningKey creation is complete and ready for use.  
`encryptedKeyMaterial` _integer array_ | Key material encrypted by the KMS root key.  
`publicKey` _integer array_ | The public key of the asymmetric signing key pair.  
`rootKeyID` _string_ | Identifier to the root key that wrapped the private key material. Follows the format `root-key-namespace/root-key-type/root-key-name/version` Example - `kms-system/ctm/org1-root-key/1` or `kms-system/local/org-1-root-key/1`  
`keyIdentifier` _string_ | KeyIdentifier is the primary identifier for private and public key objects. This is the serialized goog.gdc.kms.v1.KeyIdentifier protobuf message schema. The field is immutable once set and cannot be removed. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.  
  
### WrappedKey

Contains the customer key wrapped for import or export operations.

_Appears in:_ \- KeyExportStatus \- KeyImportSpec

Field | Description  
---|---  
`metadata` _KeyMetadata_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`keyMaterial` _integer array_ | The wrapped key material.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
