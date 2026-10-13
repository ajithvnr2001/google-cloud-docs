---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation.Type
title: Enum Operation.Type (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:47.965249+00:00
---

# Enum Operation.Type (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Operation.Type (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public enum Operation.Type extends Enum<Operation.Type> implements ProtocolMessageEnum

Operation type categorizes the operation.

Protobuf enum `google.container.v1beta1.Operation.Type`

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
`AUTO_REPAIR_NODES` |  A problem has been detected with nodes and [they are being repaired](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair). This operation type is initiated by GKE, typically automatically. This operation may be concurrent with other operations and there may be multiple repairs occurring on the same node pool. `AUTO_REPAIR_NODES = 10;`  
`AUTO_REPAIR_NODES_VALUE` |  A problem has been detected with nodes and [they are being repaired](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair). This operation type is initiated by GKE, typically automatically. This operation may be concurrent with other operations and there may be multiple repairs occurring on the same node pool. `AUTO_REPAIR_NODES = 10;`  
`AUTO_UPGRADE_NODES` |  Unused. Automatic node upgrade uses UPGRADE_NODES. `AUTO_UPGRADE_NODES = 11 [deprecated = true];`  
`AUTO_UPGRADE_NODES_VALUE` |  Unused. Automatic node upgrade uses UPGRADE_NODES. `AUTO_UPGRADE_NODES = 11 [deprecated = true];`  
`CREATE_CLUSTER` |  The cluster is being created. The cluster should be assumed to be unusable until the operation finishes. In the event of the operation failing, the cluster will enter the ERROR state and eventually be deleted. `CREATE_CLUSTER = 1;`  
`CREATE_CLUSTER_VALUE` |  The cluster is being created. The cluster should be assumed to be unusable until the operation finishes. In the event of the operation failing, the cluster will enter the ERROR state and eventually be deleted. `CREATE_CLUSTER = 1;`  
`CREATE_NODE_POOL` |  A node pool is being created. The node pool should be assumed to be unusable until this operation finishes. In the event of an error, the node pool may be partially created. If enabled, [node autoprovisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) may have automatically initiated such operations. `CREATE_NODE_POOL = 7;`  
`CREATE_NODE_POOL_VALUE` |  A node pool is being created. The node pool should be assumed to be unusable until this operation finishes. In the event of an error, the node pool may be partially created. If enabled, [node autoprovisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) may have automatically initiated such operations. `CREATE_NODE_POOL = 7;`  
`DELETE_CLUSTER` |  The cluster is being deleted. The cluster should be assumed to be unusable as soon as this operation starts. In the event of the operation failing, the cluster will enter the ERROR state and the deletion will be automatically retried until completed. `DELETE_CLUSTER = 2;`  
`DELETE_CLUSTER_VALUE` |  The cluster is being deleted. The cluster should be assumed to be unusable as soon as this operation starts. In the event of the operation failing, the cluster will enter the ERROR state and the deletion will be automatically retried until completed. `DELETE_CLUSTER = 2;`  
`DELETE_NODE_POOL` |  The node pool is being deleted. The node pool should be assumed to be unusable as soon as this operation starts. `DELETE_NODE_POOL = 8;`  
`DELETE_NODE_POOL_VALUE` |  The node pool is being deleted. The node pool should be assumed to be unusable as soon as this operation starts. `DELETE_NODE_POOL = 8;`  
`FLEET_FEATURE_UPGRADE` |  Fleet features of GKE Enterprise are being upgraded. The cluster should be assumed to be blocked for other upgrades until the operation finishes. `FLEET_FEATURE_UPGRADE = 19;`  
`FLEET_FEATURE_UPGRADE_VALUE` |  Fleet features of GKE Enterprise are being upgraded. The cluster should be assumed to be blocked for other upgrades until the operation finishes. `FLEET_FEATURE_UPGRADE = 19;`  
`REPAIR_CLUSTER` |  A problem has been detected with the control plane and is being repaired. This operation type is initiated by GKE. For more details, see [documentation on repairs](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs). `REPAIR_CLUSTER = 5;`  
`REPAIR_CLUSTER_VALUE` |  A problem has been detected with the control plane and is being repaired. This operation type is initiated by GKE. For more details, see [documentation on repairs](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs). `REPAIR_CLUSTER = 5;`  
`RESIZE_CLUSTER` |  The control plane is being resized. This operation type is initiated by GKE. These operations are often performed preemptively to ensure that the control plane has sufficient resources and is not typically an indication of issues. For more details, see [documentation on resizes](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs). `RESIZE_CLUSTER = 18;`  
`RESIZE_CLUSTER_VALUE` |  The control plane is being resized. This operation type is initiated by GKE. These operations are often performed preemptively to ensure that the control plane has sufficient resources and is not typically an indication of issues. For more details, see [documentation on resizes](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs). `RESIZE_CLUSTER = 18;`  
`SET_LABELS` |  Unused. Updating labels uses UPDATE_CLUSTER. `SET_LABELS = 12 [deprecated = true];`  
`SET_LABELS_VALUE` |  Unused. Updating labels uses UPDATE_CLUSTER. `SET_LABELS = 12 [deprecated = true];`  
`SET_MAINTENANCE_POLICY` |  Unused. Updating maintenance policy uses UPDATE_CLUSTER. `SET_MAINTENANCE_POLICY = 16 [deprecated = true];`  
`SET_MAINTENANCE_POLICY_VALUE` |  Unused. Updating maintenance policy uses UPDATE_CLUSTER. `SET_MAINTENANCE_POLICY = 16 [deprecated = true];`  
`SET_MASTER_AUTH` |  Unused. Updating master auth uses UPDATE_CLUSTER. `SET_MASTER_AUTH = 13 [deprecated = true];`  
`SET_MASTER_AUTH_VALUE` |  Unused. Updating master auth uses UPDATE_CLUSTER. `SET_MASTER_AUTH = 13 [deprecated = true];`  
`SET_NETWORK_POLICY` |  Unused. Updating network policy uses UPDATE_CLUSTER. `SET_NETWORK_POLICY = 15 [deprecated = true];`  
`SET_NETWORK_POLICY_VALUE` |  Unused. Updating network policy uses UPDATE_CLUSTER. `SET_NETWORK_POLICY = 15 [deprecated = true];`  
`SET_NODE_POOL_MANAGEMENT` |  The node pool's manamagent field is being updated. These operations only update metadata and may be concurrent with most other operations. `SET_NODE_POOL_MANAGEMENT = 9;`  
`SET_NODE_POOL_MANAGEMENT_VALUE` |  The node pool's manamagent field is being updated. These operations only update metadata and may be concurrent with most other operations. `SET_NODE_POOL_MANAGEMENT = 9;`  
`SET_NODE_POOL_SIZE` |  The node pool is being resized. With the exception of resizing to or from size zero, the node pool is generally usable during this operation. `SET_NODE_POOL_SIZE = 14;`  
`SET_NODE_POOL_SIZE_VALUE` |  The node pool is being resized. With the exception of resizing to or from size zero, the node pool is generally usable during this operation. `SET_NODE_POOL_SIZE = 14;`  
`TYPE_UNSPECIFIED` |  Not set. `TYPE_UNSPECIFIED = 0;`  
`TYPE_UNSPECIFIED_VALUE` |  Not set. `TYPE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`UPDATE_CLUSTER` |  The cluster is being updated. This is a broad category of operations and includes operations that only change metadata as well as those that must recreate the entire cluster. If the control plane must be recreated, this will cause temporary downtime for zonal clusters. Some features require recreating the nodes as well. Those will be recreated as separate operations and the update may not be completely functional until the node pools recreations finish. Node recreations will generally follow [maintenance policies](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). Some GKE-initiated operations use this type. This includes certain types of auto-upgrades and incident mitigations. `UPDATE_CLUSTER = 6;`  
`UPDATE_CLUSTER_VALUE` |  The cluster is being updated. This is a broad category of operations and includes operations that only change metadata as well as those that must recreate the entire cluster. If the control plane must be recreated, this will cause temporary downtime for zonal clusters. Some features require recreating the nodes as well. Those will be recreated as separate operations and the update may not be completely functional until the node pools recreations finish. Node recreations will generally follow [maintenance policies](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). Some GKE-initiated operations use this type. This includes certain types of auto-upgrades and incident mitigations. `UPDATE_CLUSTER = 6;`  
`UPGRADE_MASTER` |  The cluster version is being updated. Note that this includes "upgrades" to the same version, which are simply a recreation. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically). For more details, see [documentation on cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#cluster_upgrades). `UPGRADE_MASTER = 3;`  
`UPGRADE_MASTER_VALUE` |  The cluster version is being updated. Note that this includes "upgrades" to the same version, which are simply a recreation. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically). For more details, see [documentation on cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#cluster_upgrades). `UPGRADE_MASTER = 3;`  
`UPGRADE_NODES` |  A node pool is being updated. Despite calling this an "upgrade", this includes most forms of updates to node pools. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades). This operation sets the progress field and may be canceled. The upgrade strategy depends on [node pool configuration](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). The nodes are generally still usable during this operation. `UPGRADE_NODES = 4;`  
`UPGRADE_NODES_VALUE` |  A node pool is being updated. Despite calling this an "upgrade", this includes most forms of updates to node pools. This also includes [auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades). This operation sets the progress field and may be canceled. The upgrade strategy depends on [node pool configuration](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). The nodes are generally still usable during this operation. `UPGRADE_NODES = 4;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation.Type#com_google_container_v1beta1_Operation_Type_forNumber_int_) instead._  
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
