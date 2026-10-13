---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.SlurmLoginNodesOrBuilder
title: Interface SlurmLoginNodesOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:46.556146+00:00
---

# Interface SlurmLoginNodesOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.SlurmLoginNodesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SlurmLoginNodesOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface SlurmLoginNodesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each login node instance.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBootDisk()
    
    
    public abstract BootDisk getBootDisk()

Optional. Boot disk for the login node.

` .google.cloud.hypercomputecluster.v1beta.BootDisk boot_disk = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BootDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.BootDisk)` | The bootDisk.  
  
### getBootDiskOrBuilder()
    
    
    public abstract BootDiskOrBuilder getBootDiskOrBuilder()

Optional. Boot disk for the login node.

` .google.cloud.hypercomputecluster.v1beta.BootDisk boot_disk = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BootDiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.BootDiskOrBuilder)` |   
  
### getCount()
    
    
    public abstract long getCount()

Required. Number of login node instances to create.

`int64 count = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count.  
  
### getEnableOsLogin()
    
    
    public abstract boolean getEnableOsLogin()

Optional. Whether [OS Login](https://cloud.google.com/compute/docs/oslogin) should be enabled on login node instances.

`bool enable_os_login = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableOsLogin.  
  
### getEnablePublicIps()
    
    
    public abstract boolean getEnablePublicIps()

Optional. Whether login node instances should be assigned [external IP addresses](https://cloud.google.com/compute/docs/ip-addresses#externaladdresses).

`bool enable_public_ips = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePublicIps.  
  
### getInstances(int index)
    
    
    public abstract ComputeInstance getInstances(int index)

Output only. Information about the login node instances that were created in Compute Engine.

` repeated .google.cloud.hypercomputecluster.v1beta.ComputeInstance instances = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComputeInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ComputeInstance)` |   
  
### getInstancesCount()
    
    
    public abstract int getInstancesCount()

Output only. Information about the login node instances that were created in Compute Engine.

` repeated .google.cloud.hypercomputecluster.v1beta.ComputeInstance instances = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInstancesList()
    
    
    public abstract List<ComputeInstance> getInstancesList()

Output only. Information about the login node instances that were created in Compute Engine.

` repeated .google.cloud.hypercomputecluster.v1beta.ComputeInstance instances = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ComputeInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ComputeInstance)>` |   
  
### getInstancesOrBuilder(int index)
    
    
    public abstract ComputeInstanceOrBuilder getInstancesOrBuilder(int index)

Output only. Information about the login node instances that were created in Compute Engine.

` repeated .google.cloud.hypercomputecluster.v1beta.ComputeInstance instances = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ComputeInstanceOrBuilder)` |   
  
### getInstancesOrBuilderList()
    
    
    public abstract List<? extends ComputeInstanceOrBuilder> getInstancesOrBuilderList()

Output only. Information about the login node instances that were created in Compute Engine.

` repeated .google.cloud.hypercomputecluster.v1beta.ComputeInstance instances = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.hypercomputecluster.v1beta.ComputeInstanceOrBuilder>` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.SlurmLoginNodesOrBuilder#com_google_cloud_hypercomputecluster_v1beta_SlurmLoginNodesOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each login node instance.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each login node instance.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each login node instance.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. [Labels](https://cloud.google.com/compute/docs/labeling-resources) that should be applied to each login node instance.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMachineType()
    
    
    public abstract String getMachineType()

Required. Name of the Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-resource) to use for login nodes, e.g. `n2-standard-2`.

`string machine_type = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

Required. Name of the Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-resource) to use for login nodes, e.g. `n2-standard-2`.

`string machine_type = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getStartupScript()
    
    
    public abstract String getStartupScript()

Optional. [Startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) to be run on each login node instance. Max 256KB.

`string startup_script = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The startupScript.  
  
### getStartupScriptBytes()
    
    
    public abstract ByteString getStartupScriptBytes()

Optional. [Startup script](https://cloud.google.com/compute/docs/instances/startup-scripts/linux) to be run on each login node instance. Max 256KB.

`string startup_script = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for startupScript.  
  
### getStorageConfigs(int index)
    
    
    public abstract StorageConfig getStorageConfigs(int index)

Optional. How storage resources should be mounted on each login node.

` repeated .google.cloud.hypercomputecluster.v1beta.StorageConfig storage_configs = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageConfig)` |   
  
### getStorageConfigsCount()
    
    
    public abstract int getStorageConfigsCount()

Optional. How storage resources should be mounted on each login node.

` repeated .google.cloud.hypercomputecluster.v1beta.StorageConfig storage_configs = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStorageConfigsList()
    
    
    public abstract List<StorageConfig> getStorageConfigsList()

Optional. How storage resources should be mounted on each login node.

` repeated .google.cloud.hypercomputecluster.v1beta.StorageConfig storage_configs = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageConfig)>` |   
  
### getStorageConfigsOrBuilder(int index)
    
    
    public abstract StorageConfigOrBuilder getStorageConfigsOrBuilder(int index)

Optional. How storage resources should be mounted on each login node.

` repeated .google.cloud.hypercomputecluster.v1beta.StorageConfig storage_configs = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageConfigOrBuilder)` |   
  
### getStorageConfigsOrBuilderList()
    
    
    public abstract List<? extends StorageConfigOrBuilder> getStorageConfigsOrBuilderList()

Optional. How storage resources should be mounted on each login node.

` repeated .google.cloud.hypercomputecluster.v1beta.StorageConfig storage_configs = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.hypercomputecluster.v1beta.StorageConfigOrBuilder>` |   
  
### getZone()
    
    
    public abstract String getZone()

Required. Name of the zone in which login nodes should run, e.g., `us-central1-a`. Must be in the same region as the cluster, and must match the zone of any other resources specified in the cluster.

`string zone = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

Required. Name of the zone in which login nodes should run, e.g., `us-central1-a`. Must be in the same region as the cluster, and must match the zone of any other resources specified in the cluster.

`string zone = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasBootDisk()
    
    
    public abstract boolean hasBootDisk()

Optional. Boot disk for the login node.

` .google.cloud.hypercomputecluster.v1beta.BootDisk boot_disk = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bootDisk field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
