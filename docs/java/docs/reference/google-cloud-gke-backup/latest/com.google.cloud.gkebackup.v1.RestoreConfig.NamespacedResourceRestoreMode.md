---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreConfig.NamespacedResourceRestoreMode
title: Enum RestoreConfig.NamespacedResourceRestoreMode (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:34.707407+00:00
---

# Enum RestoreConfig.NamespacedResourceRestoreMode (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreConfig.NamespacedResourceRestoreMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum RestoreConfig.NamespacedResourceRestoreMode (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.0 
    
    
    public enum RestoreConfig.NamespacedResourceRestoreMode extends Enum<RestoreConfig.NamespacedResourceRestoreMode> implements ProtocolMessageEnum

Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster.

Protobuf enum `google.cloud.gkebackup.v1.RestoreConfig.NamespacedResourceRestoreMode`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`DELETE_AND_RESTORE` |  When conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered, this will first trigger a delete of the conflicting resource AND ALL OF ITS REFERENCED RESOURCES (e.g., all resources in the Namespace or all resources referenced by the ProtectedApplication) before restoring the resources from the Backup. This mode should only be used when you are intending to revert some portion of a cluster to an earlier state. `DELETE_AND_RESTORE = 1;`  
`DELETE_AND_RESTORE_VALUE` |  When conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered, this will first trigger a delete of the conflicting resource AND ALL OF ITS REFERENCED RESOURCES (e.g., all resources in the Namespace or all resources referenced by the ProtectedApplication) before restoring the resources from the Backup. This mode should only be used when you are intending to revert some portion of a cluster to an earlier state. `DELETE_AND_RESTORE = 1;`  
`FAIL_ON_CONFLICT` |  If conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered at the beginning of a restore process, the Restore will fail. If a conflict occurs during the restore process itself (e.g., because an out of band process creates conflicting resources), a conflict will be reported. `FAIL_ON_CONFLICT = 2;`  
`FAIL_ON_CONFLICT_VALUE` |  If conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered at the beginning of a restore process, the Restore will fail. If a conflict occurs during the restore process itself (e.g., because an out of band process creates conflicting resources), a conflict will be reported. `FAIL_ON_CONFLICT = 2;`  
`MERGE_REPLACE_ON_CONFLICT` |  This mode merges the backup and the target cluster and replaces the conflicting resources with the ones in the backup. If a single resource to restore exists in the cluster before restoration, the resource will be replaced with the one from the backup. To replace an existing resource, the first attempt is to update the resource to match the one from the backup; if the update fails, the second attempt is to delete the resource and restore it from the backup. Note that this mode could cause data loss as it replaces the existing resources in the target cluster, and the original PV can be retained or deleted depending on its reclaim policy. `MERGE_REPLACE_ON_CONFLICT = 5;`  
`MERGE_REPLACE_ON_CONFLICT_VALUE` |  This mode merges the backup and the target cluster and replaces the conflicting resources with the ones in the backup. If a single resource to restore exists in the cluster before restoration, the resource will be replaced with the one from the backup. To replace an existing resource, the first attempt is to update the resource to match the one from the backup; if the update fails, the second attempt is to delete the resource and restore it from the backup. Note that this mode could cause data loss as it replaces the existing resources in the target cluster, and the original PV can be retained or deleted depending on its reclaim policy. `MERGE_REPLACE_ON_CONFLICT = 5;`  
`MERGE_REPLACE_VOLUME_ON_CONFLICT` |  This mode merges the backup and the target cluster and skips the conflicting resources except volume data. If a PVC to restore already exists, this mode will restore/reconnect the volume without overwriting the PVC. It is similar to MERGE_SKIP_ON_CONFLICT except that it will apply the volume data policy for the conflicting PVCs:

  * RESTORE_VOLUME_DATA_FROM_BACKUP: restore data only and respect the reclaim policy of the original PV;
  * REUSE_VOLUME_HANDLE_FROM_BACKUP: reconnect and respect the reclaim policy of the original PV;
  * NO_VOLUME_DATA_RESTORATION: new provision and respect the reclaim policy of the original PV. Note that this mode could cause data loss as the original PV can be retained or deleted depending on its reclaim policy.

`MERGE_REPLACE_VOLUME_ON_CONFLICT = 4;`  
`MERGE_REPLACE_VOLUME_ON_CONFLICT_VALUE` |  This mode merges the backup and the target cluster and skips the conflicting resources except volume data. If a PVC to restore already exists, this mode will restore/reconnect the volume without overwriting the PVC. It is similar to MERGE_SKIP_ON_CONFLICT except that it will apply the volume data policy for the conflicting PVCs:

  * RESTORE_VOLUME_DATA_FROM_BACKUP: restore data only and respect the reclaim policy of the original PV;
  * REUSE_VOLUME_HANDLE_FROM_BACKUP: reconnect and respect the reclaim policy of the original PV;
  * NO_VOLUME_DATA_RESTORATION: new provision and respect the reclaim policy of the original PV. Note that this mode could cause data loss as the original PV can be retained or deleted depending on its reclaim policy.

`MERGE_REPLACE_VOLUME_ON_CONFLICT = 4;`  
`MERGE_SKIP_ON_CONFLICT` |  This mode merges the backup and the target cluster and skips the conflicting resources. If a single resource to restore exists in the cluster before restoration, the resource will be skipped, otherwise it will be restored. `MERGE_SKIP_ON_CONFLICT = 3;`  
`MERGE_SKIP_ON_CONFLICT_VALUE` |  This mode merges the backup and the target cluster and skips the conflicting resources. If a single resource to restore exists in the cluster before restoration, the resource will be skipped, otherwise it will be restored. `MERGE_SKIP_ON_CONFLICT = 3;`  
`NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED` |  Unspecified (invalid). `NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED = 0;`  
`NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED_VALUE` |  Unspecified (invalid). `NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreConfig.NamespacedResourceRestoreMode#com_google_cloud_gkebackup_v1_RestoreConfig_NamespacedResourceRestoreMode_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
