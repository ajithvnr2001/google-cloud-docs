---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryptionOrBuilder
title: Interface DatabaseEncryptionOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:15.748217+00:00
---

# Interface DatabaseEncryptionOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryptionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DatabaseEncryptionOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface DatabaseEncryptionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCurrentState()
    
    
    public abstract DatabaseEncryption.CurrentState getCurrentState()

Output only. The current state of etcd encryption.

` optional .google.container.v1.DatabaseEncryption.CurrentState current_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption.CurrentState](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption.CurrentState)` | The currentState.  
  
### getCurrentStateValue()
    
    
    public abstract int getCurrentStateValue()

Output only. The current state of etcd encryption.

` optional .google.container.v1.DatabaseEncryption.CurrentState current_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for currentState.  
  
### getDecryptionKeys(int index)
    
    
    public abstract String getDecryptionKeys(int index)

Output only. Keys in use by the cluster for decrypting existing objects, in addition to the key in `key_name`.

Each item is a CloudKMS key resource.

`repeated string decryption_keys = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The decryptionKeys at the given index.  
  
### getDecryptionKeysBytes(int index)
    
    
    public abstract ByteString getDecryptionKeysBytes(int index)

Output only. Keys in use by the cluster for decrypting existing objects, in addition to the key in `key_name`.

Each item is a CloudKMS key resource.

`repeated string decryption_keys = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the decryptionKeys at the given index.  
  
### getDecryptionKeysCount()
    
    
    public abstract int getDecryptionKeysCount()

Output only. Keys in use by the cluster for decrypting existing objects, in addition to the key in `key_name`.

Each item is a CloudKMS key resource.

`repeated string decryption_keys = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of decryptionKeys.  
  
### getDecryptionKeysList()
    
    
    public abstract List<String> getDecryptionKeysList()

Output only. Keys in use by the cluster for decrypting existing objects, in addition to the key in `key_name`.

Each item is a CloudKMS key resource.

`repeated string decryption_keys = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the decryptionKeys.  
  
### getKeyName()
    
    
    public abstract String getKeyName()

Name of CloudKMS key to use for the encryption of secrets in etcd. Ex. projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key

`string key_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The keyName.  
  
### getKeyNameBytes()
    
    
    public abstract ByteString getKeyNameBytes()

Name of CloudKMS key to use for the encryption of secrets in etcd. Ex. projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key

`string key_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for keyName.  
  
### getLastOperationErrors(int index)
    
    
    public abstract DatabaseEncryption.OperationError getLastOperationErrors(int index)

Output only. Records errors seen during DatabaseEncryption update operations.

` repeated .google.container.v1.DatabaseEncryption.OperationError last_operation_errors = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption.OperationError](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption.OperationError)` |   
  
### getLastOperationErrorsCount()
    
    
    public abstract int getLastOperationErrorsCount()

Output only. Records errors seen during DatabaseEncryption update operations.

` repeated .google.container.v1.DatabaseEncryption.OperationError last_operation_errors = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLastOperationErrorsList()
    
    
    public abstract List<DatabaseEncryption.OperationError> getLastOperationErrorsList()

Output only. Records errors seen during DatabaseEncryption update operations.

` repeated .google.container.v1.DatabaseEncryption.OperationError last_operation_errors = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[OperationError](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption.OperationError)>` |   
  
### getLastOperationErrorsOrBuilder(int index)
    
    
    public abstract DatabaseEncryption.OperationErrorOrBuilder getLastOperationErrorsOrBuilder(int index)

Output only. Records errors seen during DatabaseEncryption update operations.

` repeated .google.container.v1.DatabaseEncryption.OperationError last_operation_errors = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption.OperationErrorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption.OperationErrorOrBuilder)` |   
  
### getLastOperationErrorsOrBuilderList()
    
    
    public abstract List<? extends DatabaseEncryption.OperationErrorOrBuilder> getLastOperationErrorsOrBuilderList()

Output only. Records errors seen during DatabaseEncryption update operations.

` repeated .google.container.v1.DatabaseEncryption.OperationError last_operation_errors = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.DatabaseEncryption.OperationErrorOrBuilder>` |   
  
### getState()
    
    
    public abstract DatabaseEncryption.State getState()

The desired state of etcd encryption.

`.google.container.v1.DatabaseEncryption.State state = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DatabaseEncryption.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

The desired state of etcd encryption.

`.google.container.v1.DatabaseEncryption.State state = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasCurrentState()
    
    
    public abstract boolean hasCurrentState()

Output only. The current state of etcd encryption.

` optional .google.container.v1.DatabaseEncryption.CurrentState current_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the currentState field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
