---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.NodePool.LocalDiskEncryptionOrBuilder
title: Interface NodePool.LocalDiskEncryptionOrBuilder (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:39.592896+00:00
---

# Interface NodePool.LocalDiskEncryptionOrBuilder (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.NodePool.LocalDiskEncryptionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodePool.LocalDiskEncryptionOrBuilder (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface NodePool.LocalDiskEncryptionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getKmsKey()
    
    
    public abstract String getKmsKey()

Optional. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting node local disks. If not specified, a Google-managed key will be used instead.

` string kms_key = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKey.  
  
### getKmsKeyActiveVersion()
    
    
    public abstract String getKmsKeyActiveVersion()

Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting node local disks. Only applicable if kms_key is set.

` string kms_key_active_version = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyActiveVersion.  
  
### getKmsKeyActiveVersionBytes()
    
    
    public abstract ByteString getKmsKeyActiveVersionBytes()

Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting node local disks. Only applicable if kms_key is set.

` string kms_key_active_version = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyActiveVersion.  
  
### getKmsKeyBytes()
    
    
    public abstract ByteString getKmsKeyBytes()

Optional. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting node local disks. If not specified, a Google-managed key will be used instead.

` string kms_key = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKey.  
  
### getKmsKeyState()
    
    
    public abstract KmsKeyState getKmsKeyState()

Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.

` .google.cloud.edgecontainer.v1.KmsKeyState kms_key_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[KmsKeyState](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.KmsKeyState)` | The kmsKeyState.  
  
### getKmsKeyStateValue()
    
    
    public abstract int getKmsKeyStateValue()

Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.

` .google.cloud.edgecontainer.v1.KmsKeyState kms_key_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for kmsKeyState.  
  
### getKmsStatus()
    
    
    public abstract Status getKmsStatus()

Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kms_key_state` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.

`.google.rpc.Status kms_status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The kmsStatus.  
  
### getKmsStatusOrBuilder()
    
    
    public abstract StatusOrBuilder getKmsStatusOrBuilder()

Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kms_key_state` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.

`.google.rpc.Status kms_status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getResourceState()
    
    
    public abstract ResourceState getResourceState()

Output only. The current resource state associated with the cmek.

` .google.cloud.edgecontainer.v1.ResourceState resource_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceState](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ResourceState)` | The resourceState.  
  
### getResourceStateValue()
    
    
    public abstract int getResourceStateValue()

Output only. The current resource state associated with the cmek.

` .google.cloud.edgecontainer.v1.ResourceState resource_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for resourceState.  
  
### hasKmsStatus()
    
    
    public abstract boolean hasKmsStatus()

Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kms_key_state` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.

`.google.rpc.Status kms_status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kmsStatus field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
