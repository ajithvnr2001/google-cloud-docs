---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig
title: Class ResourceBackupConfig (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:42.574792+00:00
---

# Class ResourceBackupConfig (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceBackupConfig (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    ResourceBackupConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ResourceBackupConfig represents a resource along with its backup configurations.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the ResourceBackupConfig. Format: projects/{project}/locations/{location}/resourceBackupConfigs/{uid}   
`uid` |  `str`   
Output only. The unique identifier of the resource backup config.   
`target_resource` |  `str`   
Output only. The `full resource name   
`target_resource_display_name` |  `str`   
Output only. The human friendly name of the target resource.   
`target_resource_type` |  `[google.cloud.backupdr_v1.types.ResourceBackupConfig.ResourceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig.ResourceType)`   
Output only. The type of the target resource.   
`target_resource_labels` |  `MutableMapping[str, str]`   
Labels associated with the target resource.   
`backup_configs_details` |  `MutableSequence[[google.cloud.backupdr_v1.types.BackupConfigDetails](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails)]`   
Backup configurations applying to the target resource, including those targeting its related/child resources. For example, backup configuration applicable to Compute Engine disks will be populated in this field for a Compute Engine VM which has the disk associated.   
`backup_configured` |  `bool`   
Output only. Whether the target resource is configured for backup. This is true if the backup_configs_details is not empty.   
`vaulted` |  `bool`   
Output only. Whether the target resource is protected by a backup vault. This is true if the backup_configs_details is not empty and any of the ResourceBackupConfig.backup_configs_details has a backup configuration with BackupConfigDetails.backup_vault set. set.   
  
## Classes 

### ResourceType
    
    
    ResourceType(value)

The type of the cloud resource.

### TargetResourceLabelsEntry
    
    
    TargetResourceLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
