---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupPropertiesOrBuilder
title: Interface AutonomousDatabaseBackupPropertiesOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:40.795955+00:00
---

# Interface AutonomousDatabaseBackupPropertiesOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupPropertiesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AutonomousDatabaseBackupPropertiesOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AutonomousDatabaseBackupPropertiesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAvailableTillTime()
    
    
    public abstract Timestamp getAvailableTillTime()

Output only. Timestamp until when the backup will be available.

` .google.protobuf.Timestamp available_till_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The availableTillTime.  
  
### getAvailableTillTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getAvailableTillTimeOrBuilder()

Output only. Timestamp until when the backup will be available.

` .google.protobuf.Timestamp available_till_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCompartmentId()
    
    
    public abstract String getCompartmentId()

Output only. The OCID of the compartment.

`string compartment_id = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The compartmentId.  
  
### getCompartmentIdBytes()
    
    
    public abstract ByteString getCompartmentIdBytes()

Output only. The OCID of the compartment.

`string compartment_id = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for compartmentId.  
  
### getDatabaseSizeTb()
    
    
    public abstract float getDatabaseSizeTb()

Output only. The quantity of data in the database, in terabytes.

`float database_size_tb = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The databaseSizeTb.  
  
### getDbVersion()
    
    
    public abstract String getDbVersion()

Output only. A valid Oracle Database version for Autonomous Database.

`string db_version = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dbVersion.  
  
### getDbVersionBytes()
    
    
    public abstract ByteString getDbVersionBytes()

Output only. A valid Oracle Database version for Autonomous Database.

`string db_version = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dbVersion.  
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. The date and time the backup completed.

`.google.protobuf.Timestamp end_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. The date and time the backup completed.

`.google.protobuf.Timestamp end_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getIsAutomaticBackup()
    
    
    public abstract boolean getIsAutomaticBackup()

Output only. Indicates if the backup is automatic or user initiated.

`bool is_automatic_backup = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isAutomaticBackup.  
  
### getIsLongTermBackup()
    
    
    public abstract boolean getIsLongTermBackup()

Output only. Indicates if the backup is long term backup.

`bool is_long_term_backup = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isLongTermBackup.  
  
### getIsRestorable()
    
    
    public abstract boolean getIsRestorable()

Output only. Indicates if the backup can be used to restore the Autonomous Database.

`bool is_restorable = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isRestorable.  
  
### getKeyStoreId()
    
    
    public abstract String getKeyStoreId()

Optional. The OCID of the key store of Oracle Vault.

`string key_store_id = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The keyStoreId.  
  
### getKeyStoreIdBytes()
    
    
    public abstract ByteString getKeyStoreIdBytes()

Optional. The OCID of the key store of Oracle Vault.

`string key_store_id = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for keyStoreId.  
  
### getKeyStoreWallet()
    
    
    public abstract String getKeyStoreWallet()

Optional. The wallet name for Oracle Key Vault.

`string key_store_wallet = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The keyStoreWallet.  
  
### getKeyStoreWalletBytes()
    
    
    public abstract ByteString getKeyStoreWalletBytes()

Optional. The wallet name for Oracle Key Vault.

`string key_store_wallet = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for keyStoreWallet.  
  
### getKmsKeyId()
    
    
    public abstract String getKmsKeyId()

Optional. The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`string kms_key_id = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyId.  
  
### getKmsKeyIdBytes()
    
    
    public abstract ByteString getKmsKeyIdBytes()

Optional. The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

`string kms_key_id = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyId.  
  
### getKmsKeyVersionId()
    
    
    public abstract String getKmsKeyVersionId()

Optional. The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation. Autonomous Database Serverless does not use key versions, hence is not applicable for Autonomous Database Serverless instances.

`string kms_key_version_id = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyVersionId.  
  
### getKmsKeyVersionIdBytes()
    
    
    public abstract ByteString getKmsKeyVersionIdBytes()

Optional. The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation. Autonomous Database Serverless does not use key versions, hence is not applicable for Autonomous Database Serverless instances.

`string kms_key_version_id = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyVersionId.  
  
### getLifecycleDetails()
    
    
    public abstract String getLifecycleDetails()

Output only. Additional information about the current lifecycle state.

`string lifecycle_details = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The lifecycleDetails.  
  
### getLifecycleDetailsBytes()
    
    
    public abstract ByteString getLifecycleDetailsBytes()

Output only. Additional information about the current lifecycle state.

`string lifecycle_details = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for lifecycleDetails.  
  
### getLifecycleState()
    
    
    public abstract AutonomousDatabaseBackupProperties.State getLifecycleState()

Output only. The lifecycle state of the backup.

` .google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.State lifecycle_state = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupProperties.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.State)` | The lifecycleState.  
  
### getLifecycleStateValue()
    
    
    public abstract int getLifecycleStateValue()

Output only. The lifecycle state of the backup.

` .google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.State lifecycle_state = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for lifecycleState.  
  
### getOcid()
    
    
    public abstract String getOcid()

Output only. OCID of the Autonomous Database backup. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>

`string ocid = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ocid.  
  
### getOcidBytes()
    
    
    public abstract ByteString getOcidBytes()

Output only. OCID of the Autonomous Database backup. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>

`string ocid = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ocid.  
  
### getRetentionPeriodDays()
    
    
    public abstract int getRetentionPeriodDays()

Optional. Retention period in days for the backup.

`int32 retention_period_days = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The retentionPeriodDays.  
  
### getSizeTb()
    
    
    public abstract float getSizeTb()

Output only. The backup size in terabytes.

`float size_tb = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sizeTb.  
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. The date and time the backup started.

`.google.protobuf.Timestamp start_time = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. The date and time the backup started.

`.google.protobuf.Timestamp start_time = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getType()
    
    
    public abstract AutonomousDatabaseBackupProperties.Type getType()

Output only. The type of the backup.

` .google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.Type type = 19 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseBackupProperties.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Output only. The type of the backup.

` .google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.Type type = 19 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getVaultId()
    
    
    public abstract String getVaultId()

Optional. The OCID of the vault.

`string vault_id = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vaultId.  
  
### getVaultIdBytes()
    
    
    public abstract ByteString getVaultIdBytes()

Optional. The OCID of the vault.

`string vault_id = 20 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vaultId.  
  
### hasAvailableTillTime()
    
    
    public abstract boolean hasAvailableTillTime()

Output only. Timestamp until when the backup will be available.

` .google.protobuf.Timestamp available_till_time = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availableTillTime field is set.  
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. The date and time the backup completed.

`.google.protobuf.Timestamp end_time = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. The date and time the backup started.

`.google.protobuf.Timestamp start_time = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
