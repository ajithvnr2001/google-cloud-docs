---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault
title: Class BackupVault (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:14.241084+00:00
---

# Class BackupVault (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupVault (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    BackupVault(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A NetApp BackupVault.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the backup vault. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}`.   
`state` |  `[google.cloud.netapp_v1.types.BackupVault.State](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.State)`   
Output only. The backup vault state.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time of the backup vault.   
`description` |  `str`   
Description of the backup vault.   
`labels` |  `MutableMapping[str, str]`   
Resource labels to represent user provided metadata.   
`backup_vault_type` |  `[google.cloud.netapp_v1.types.BackupVault.BackupVaultType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.BackupVaultType)`   
Optional. Type of backup vault to be created. Default is IN_REGION.   
`source_region` |  `str`   
Output only. Region in which the backup vault is created. Format: `projects/{project_id}/locations/{location}`  
`backup_region` |  `str`   
Optional. Region where the backups are stored. Format: `projects/{project_id}/locations/{location}`  
`source_backup_vault` |  `str`   
Output only. Name of the Backup vault created in source region. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}`  
`destination_backup_vault` |  `str`   
Output only. Name of the Backup vault created in backup region. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}`  
`backup_retention_policy` |  `[google.cloud.netapp_v1.types.BackupVault.BackupRetentionPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.BackupRetentionPolicy)`   
Optional. Backup retention policy defining the retention of backups.   
`kms_config` |  `str`   
Optional. Specifies the Key Management System (KMS) configuration to be used for backup encryption. Format: `projects/{project}/locations/{location}/kmsConfigs/{kms_config}`  
`encryption_state` |  `[google.cloud.netapp_v1.types.BackupVault.EncryptionState](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.EncryptionState)`   
Output only. Field indicating encryption state of CMEK backups.   
`backups_crypto_key_version` |  `str`   
Output only. The crypto key version used to encrypt the backup vault. Format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`  
  
## Classes 

### BackupRetentionPolicy
    
    
    BackupRetentionPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Retention policy for backups in the backup vault

### BackupVaultType
    
    
    BackupVaultType(value)

Backup Vault Type.

### EncryptionState
    
    
    EncryptionState(value)

Encryption state of customer-managed encryption keys (CMEK) backups.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### State
    
    
    State(value)

The Backup Vault States

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
