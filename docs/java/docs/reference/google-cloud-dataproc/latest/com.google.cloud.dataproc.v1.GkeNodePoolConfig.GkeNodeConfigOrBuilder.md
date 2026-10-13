---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodeConfigOrBuilder
title: Interface GkeNodePoolConfig.GkeNodeConfigOrBuilder (4.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:39.999056+00:00
---

# Interface GkeNodePoolConfig.GkeNodeConfigOrBuilder (4.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodeConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GkeNodePoolConfig.GkeNodeConfigOrBuilder (4.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.96.0 (latest)  4.92.0  4.91.1  4.90.0  4.88.0  4.85.0  4.84.0  4.82.0  4.80.0  4.79.0  4.78.0  4.77.0  4.75.0  4.73.0  4.72.0  4.71.0  4.70.0  4.69.0  4.67.0  4.65.0  4.64.0  4.61.0  4.60.0  4.59.0  4.57.0  4.56.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.46.0  4.45.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.34.0  4.33.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.8  3.1.2  3.0.3  2.3.1 
    
    
    public static interface GkeNodePoolConfig.GkeNodeConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccelerators(int index)
    
    
    public abstract GkeNodePoolConfig.GkeNodePoolAcceleratorConfig getAccelerators(int index)

Optional. A list of [hardware accelerators](https://cloud.google.com/compute/docs/gpus) to attach to each node.

` repeated .google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig accelerators = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GkeNodePoolConfig.GkeNodePoolAcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig)` |   
  
### getAcceleratorsCount()
    
    
    public abstract int getAcceleratorsCount()

Optional. A list of [hardware accelerators](https://cloud.google.com/compute/docs/gpus) to attach to each node.

` repeated .google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig accelerators = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAcceleratorsList()
    
    
    public abstract List<GkeNodePoolConfig.GkeNodePoolAcceleratorConfig> getAcceleratorsList()

Optional. A list of [hardware accelerators](https://cloud.google.com/compute/docs/gpus) to attach to each node.

` repeated .google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig accelerators = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GkeNodePoolAcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig)>` |   
  
### getAcceleratorsOrBuilder(int index)
    
    
    public abstract GkeNodePoolConfig.GkeNodePoolAcceleratorConfigOrBuilder getAcceleratorsOrBuilder(int index)

Optional. A list of [hardware accelerators](https://cloud.google.com/compute/docs/gpus) to attach to each node.

` repeated .google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig accelerators = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GkeNodePoolConfig.GkeNodePoolAcceleratorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfigOrBuilder)` |   
  
### getAcceleratorsOrBuilderList()
    
    
    public abstract List<? extends GkeNodePoolConfig.GkeNodePoolAcceleratorConfigOrBuilder> getAcceleratorsOrBuilderList()

Optional. A list of [hardware accelerators](https://cloud.google.com/compute/docs/gpus) to attach to each node.

` repeated .google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfig accelerators = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dataproc.v1.GkeNodePoolConfig.GkeNodePoolAcceleratorConfigOrBuilder>` |   
  
### getBootDiskKmsKey()
    
    
    public abstract String getBootDiskKmsKey()

Optional. The [Customer Managed Encryption Key (CMEK)](https://cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) used to encrypt the boot disk attached to each node in the node pool. Specify the key using the following format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`

` string boot_disk_kms_key = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bootDiskKmsKey.  
  
### getBootDiskKmsKeyBytes()
    
    
    public abstract ByteString getBootDiskKmsKeyBytes()

Optional. The [Customer Managed Encryption Key (CMEK)](https://cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) used to encrypt the boot disk attached to each node in the node pool. Specify the key using the following format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`

` string boot_disk_kms_key = 23 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bootDiskKmsKey.  
  
### getLocalSsdCount()
    
    
    public abstract int getLocalSsdCount()

Optional. The number of local SSD disks to attach to the node, which is limited by the maximum number of disks allowable per zone (see [Adding Local SSDs](https://cloud.google.com/compute/docs/disks/local-ssd)).

`int32 local_ssd_count = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The localSsdCount.  
  
### getMachineType()
    
    
    public abstract String getMachineType()

Optional. The name of a Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-types).

`string machine_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

Optional. The name of a Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-types).

`string machine_type = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMinCpuPlatform()
    
    
    public abstract String getMinCpuPlatform()

Optional. [Minimum CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform) to be used by this instance. The instance may be scheduled on the specified or a newer CPU platform. Specify the friendly names of CPU platforms, such as "Intel Haswell"` or Intel Sandy Bridge".

`string min_cpu_platform = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minCpuPlatform.  
  
### getMinCpuPlatformBytes()
    
    
    public abstract ByteString getMinCpuPlatformBytes()

Optional. [Minimum CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform) to be used by this instance. The instance may be scheduled on the specified or a newer CPU platform. Specify the friendly names of CPU platforms, such as "Intel Haswell"` or Intel Sandy Bridge".

`string min_cpu_platform = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minCpuPlatform.  
  
### getPreemptible()
    
    
    public abstract boolean getPreemptible()

Optional. Whether the nodes are created as legacy [preemptible VM instances](https://cloud.google.com/compute/docs/instances/preemptible). Also see Spot VMs, preemptible VM instances without a maximum lifetime. Legacy and Spot preemptible nodes cannot be used in a node pool with the `CONTROLLER` [role](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters#role) or in the DEFAULT node pool if the CONTROLLER role is not assigned (the DEFAULT node pool will assume the CONTROLLER role).

`bool preemptible = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preemptible.  
  
### getSpot()
    
    
    public abstract boolean getSpot()

Optional. Whether the nodes are created as [Spot VM instances](https://cloud.google.com/compute/docs/instances/spot). Spot VMs are the latest update to legacy preemptible VMs. Spot VMs do not have a maximum lifetime. Legacy and Spot preemptible nodes cannot be used in a node pool with the `CONTROLLER` [role](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters#role) or in the DEFAULT node pool if the CONTROLLER role is not assigned (the DEFAULT node pool will assume the CONTROLLER role).

`bool spot = 32 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The spot.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
