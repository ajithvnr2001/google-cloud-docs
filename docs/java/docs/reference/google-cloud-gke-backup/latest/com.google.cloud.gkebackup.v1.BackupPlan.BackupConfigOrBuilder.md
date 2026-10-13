---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan.BackupConfigOrBuilder
title: Interface BackupPlan.BackupConfigOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:59.764494+00:00
---

# Interface BackupPlan.BackupConfigOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan.BackupConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackupPlan.BackupConfigOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.0 
    
    
    public static interface BackupPlan.BackupConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllNamespaces()
    
    
    public abstract boolean getAllNamespaces()

If True, include all namespaced resources

`bool all_namespaces = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allNamespaces.  
  
### getBackupScopeCase()
    
    
    public abstract BackupPlan.BackupConfig.BackupScopeCase getBackupScopeCase()

**Returns**  
---  
**Type** | **Description**  
`[BackupPlan.BackupConfig.BackupScopeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan.BackupConfig.BackupScopeCase)` |   
  
### getEncryptionKey()
    
    
    public abstract EncryptionKey getEncryptionKey()

Optional. This defines a customer managed encryption key that will be used to encrypt the "config" portion (the Kubernetes resources) of Backups created via this plan.

Default (empty): Config backup artifacts will not be encrypted.

` .google.cloud.gkebackup.v1.EncryptionKey encryption_key = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.EncryptionKey)` | The encryptionKey.  
  
### getEncryptionKeyOrBuilder()
    
    
    public abstract EncryptionKeyOrBuilder getEncryptionKeyOrBuilder()

Optional. This defines a customer managed encryption key that will be used to encrypt the "config" portion (the Kubernetes resources) of Backups created via this plan.

Default (empty): Config backup artifacts will not be encrypted.

` .google.cloud.gkebackup.v1.EncryptionKey encryption_key = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.EncryptionKeyOrBuilder)` |   
  
### getIncludeSecrets()
    
    
    public abstract boolean getIncludeSecrets()

Optional. This flag specifies whether Kubernetes Secret resources should be included when they fall into the scope of Backups.

Default: False

`bool include_secrets = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The includeSecrets.  
  
### getIncludeVolumeData()
    
    
    public abstract boolean getIncludeVolumeData()

Optional. This flag specifies whether volume data should be backed up when PVCs are included in the scope of a Backup.

Default: False

`bool include_volume_data = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The includeVolumeData.  
  
### getPermissiveMode()
    
    
    public abstract boolean getPermissiveMode()

Optional. If false, Backups will fail when Backup for GKE detects Kubernetes configuration that is non-standard or requires additional setup to restore.

Default: False

`bool permissive_mode = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The permissiveMode.  
  
### getSelectedApplications()
    
    
    public abstract NamespacedNames getSelectedApplications()

If set, include just the resources referenced by the listed ProtectedApplications.

`.google.cloud.gkebackup.v1.NamespacedNames selected_applications = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacedNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.NamespacedNames)` | The selectedApplications.  
  
### getSelectedApplicationsOrBuilder()
    
    
    public abstract NamespacedNamesOrBuilder getSelectedApplicationsOrBuilder()

If set, include just the resources referenced by the listed ProtectedApplications.

`.google.cloud.gkebackup.v1.NamespacedNames selected_applications = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacedNamesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.NamespacedNamesOrBuilder)` |   
  
### getSelectedNamespaces()
    
    
    public abstract Namespaces getSelectedNamespaces()

If set, include just the resources in the listed namespaces.

`.google.cloud.gkebackup.v1.Namespaces selected_namespaces = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Namespaces](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Namespaces)` | The selectedNamespaces.  
  
### getSelectedNamespacesOrBuilder()
    
    
    public abstract NamespacesOrBuilder getSelectedNamespacesOrBuilder()

If set, include just the resources in the listed namespaces.

`.google.cloud.gkebackup.v1.Namespaces selected_namespaces = 2;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.NamespacesOrBuilder)` |   
  
### hasAllNamespaces()
    
    
    public abstract boolean hasAllNamespaces()

If True, include all namespaced resources

`bool all_namespaces = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allNamespaces field is set.  
  
### hasEncryptionKey()
    
    
    public abstract boolean hasEncryptionKey()

Optional. This defines a customer managed encryption key that will be used to encrypt the "config" portion (the Kubernetes resources) of Backups created via this plan.

Default (empty): Config backup artifacts will not be encrypted.

` .google.cloud.gkebackup.v1.EncryptionKey encryption_key = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionKey field is set.  
  
### hasSelectedApplications()
    
    
    public abstract boolean hasSelectedApplications()

If set, include just the resources referenced by the listed ProtectedApplications.

`.google.cloud.gkebackup.v1.NamespacedNames selected_applications = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selectedApplications field is set.  
  
### hasSelectedNamespaces()
    
    
    public abstract boolean hasSelectedNamespaces()

If set, include just the resources in the listed namespaces.

`.google.cloud.gkebackup.v1.Namespaces selected_namespaces = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selectedNamespaces field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
