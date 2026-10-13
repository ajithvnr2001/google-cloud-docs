---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfigOrBuilder
title: Interface NodeConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:39.207776+00:00
---

# Interface NodeConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodeConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface NodeConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

The Kubernetes labels (key/value pairs) to apply to each node. The values in this field are added to the set of default labels Kubernetes applies to nodes.

This field has the following restrictions:

  * Labels must use a valid Kubernetes syntax and character set, as defined in <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set>.
  * This field supports up to 1,024 total characters in a single request.

Depending on the Kubernetes version, keys in this field might conflict with the keys of the default labels, which might change which of your labels are applied to the nodes. Assume that the behavior is unpredictable and avoid label key conflicts. For more information about the default labels, see: <https://kubernetes.io/docs/reference/labels-annotations-taints/>




`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsMetadata(String key)
    
    
    public abstract boolean containsMetadata(String key)

The metadata key/value pairs assigned to instances in the cluster.

Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys:

  * "cluster-location"
  * "cluster-name"
  * "cluster-uid"
  * "configure-sh"
  * "containerd-configure-sh"
  * "enable-oslogin"
  * "gci-ensure-gke-docker"
  * "gci-metrics-enabled"
  * "gci-update-strategy"
  * "instance-template"
  * "kube-env"
  * "startup-script"
  * "user-data"
  * "disable-address-manager"
  * "windows-startup-script-ps1"
  * "common-psm1"
  * "k8s-node-setup-psm1"
  * "install-ssh-psm1"
  * "user-profile-psm1"

Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB.

The total size of all keys and values must be less than 512 KB.




`map<string, string> metadata = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsResourceLabels(String key)
    
    
    public abstract boolean containsResourceLabels(String key)

The resource labels for the node pool to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 37;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccelerators(int index)
    
    
    public abstract AcceleratorConfig getAccelerators(int index)

A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.

`repeated .google.container.v1beta1.AcceleratorConfig accelerators = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AcceleratorConfig)` |   
  
### getAcceleratorsCount()
    
    
    public abstract int getAcceleratorsCount()

A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.

`repeated .google.container.v1beta1.AcceleratorConfig accelerators = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAcceleratorsList()
    
    
    public abstract List<AcceleratorConfig> getAcceleratorsList()

A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.

`repeated .google.container.v1beta1.AcceleratorConfig accelerators = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AcceleratorConfig)>` |   
  
### getAcceleratorsOrBuilder(int index)
    
    
    public abstract AcceleratorConfigOrBuilder getAcceleratorsOrBuilder(int index)

A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.

`repeated .google.container.v1beta1.AcceleratorConfig accelerators = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AcceleratorConfigOrBuilder)` |   
  
### getAcceleratorsOrBuilderList()
    
    
    public abstract List<? extends AcceleratorConfigOrBuilder> getAcceleratorsOrBuilderList()

A list of hardware accelerators to be attached to each node. See <https://cloud.google.com/compute/docs/gpus> for more information about support for GPUs.

`repeated .google.container.v1beta1.AcceleratorConfig accelerators = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1beta1.AcceleratorConfigOrBuilder>` |   
  
### getAdvancedMachineFeatures()
    
    
    public abstract AdvancedMachineFeatures getAdvancedMachineFeatures()

Advanced features for the Compute Engine VM.

`.google.container.v1beta1.AdvancedMachineFeatures advanced_machine_features = 26;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedMachineFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdvancedMachineFeatures)` | The advancedMachineFeatures.  
  
### getAdvancedMachineFeaturesOrBuilder()
    
    
    public abstract AdvancedMachineFeaturesOrBuilder getAdvancedMachineFeaturesOrBuilder()

Advanced features for the Compute Engine VM.

`.google.container.v1beta1.AdvancedMachineFeatures advanced_machine_features = 26;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedMachineFeaturesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdvancedMachineFeaturesOrBuilder)` |   
  
### getBootDisk()
    
    
    public abstract BootDisk getBootDisk()

Boot disk configuration for the node pool.

`.google.container.v1beta1.BootDisk boot_disk = 57;`

**Returns**  
---  
**Type** | **Description**  
`[BootDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BootDisk)` | The bootDisk.  
  
### getBootDiskKmsKey()
    
    
    public abstract String getBootDiskKmsKey()

The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <https://cloud.google.com/compute/docs/disks/customer-managed-encryption>

`string boot_disk_kms_key = 23;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bootDiskKmsKey.  
  
### getBootDiskKmsKeyBytes()
    
    
    public abstract ByteString getBootDiskKmsKeyBytes()

The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <https://cloud.google.com/compute/docs/disks/customer-managed-encryption>

`string boot_disk_kms_key = 23;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bootDiskKmsKey.  
  
### getBootDiskOrBuilder()
    
    
    public abstract BootDiskOrBuilder getBootDiskOrBuilder()

Boot disk configuration for the node pool.

`.google.container.v1beta1.BootDisk boot_disk = 57;`

**Returns**  
---  
**Type** | **Description**  
`[BootDiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BootDiskOrBuilder)` |   
  
### getConfidentialNodes()
    
    
    public abstract ConfidentialNodes getConfidentialNodes()

Confidential nodes config. All the nodes in the node pool will be Confidential VM once enabled.

`.google.container.v1beta1.ConfidentialNodes confidential_nodes = 35;`

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ConfidentialNodes)` | The confidentialNodes.  
  
### getConfidentialNodesOrBuilder()
    
    
    public abstract ConfidentialNodesOrBuilder getConfidentialNodesOrBuilder()

Confidential nodes config. All the nodes in the node pool will be Confidential VM once enabled.

`.google.container.v1beta1.ConfidentialNodes confidential_nodes = 35;`

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialNodesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ConfidentialNodesOrBuilder)` |   
  
### getConsolidationDelay()
    
    
    public abstract Duration getConsolidationDelay()

Consolidation delay defines duration after which the Cluster Autoscaler can scale down underutilized nodes. If not set, nodes are scaled down by default behavior, i.e. according to the chosen autoscaling profile.

`.google.protobuf.Duration consolidation_delay = 60;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The consolidationDelay.  
  
### getConsolidationDelayOrBuilder()
    
    
    public abstract DurationOrBuilder getConsolidationDelayOrBuilder()

Consolidation delay defines duration after which the Cluster Autoscaler can scale down underutilized nodes. If not set, nodes are scaled down by default behavior, i.e. according to the chosen autoscaling profile.

`.google.protobuf.Duration consolidation_delay = 60;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getContainerdConfig()
    
    
    public abstract ContainerdConfig getContainerdConfig()

Parameters for containerd customization.

`.google.container.v1beta1.ContainerdConfig containerd_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig)` | The containerdConfig.  
  
### getContainerdConfigOrBuilder()
    
    
    public abstract ContainerdConfigOrBuilder getContainerdConfigOrBuilder()

Parameters for containerd customization.

`.google.container.v1beta1.ContainerdConfig containerd_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfigOrBuilder)` |   
  
### getDiskSizeGb()
    
    
    public abstract int getDiskSizeGb()

Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.

If unspecified, the default disk size is 100GB.

`int32 disk_size_gb = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskSizeGb.  
  
### getDiskType()
    
    
    public abstract String getDiskType()

Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced')

If unspecified, the default disk type is 'pd-standard'

`string disk_type = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskType.  
  
### getDiskTypeBytes()
    
    
    public abstract ByteString getDiskTypeBytes()

Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced')

If unspecified, the default disk type is 'pd-standard'

`string disk_type = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskType.  
  
### getEffectiveCgroupMode()
    
    
    public abstract NodeConfig.EffectiveCgroupMode getEffectiveCgroupMode()

Output only. effective_cgroup_mode is the cgroup mode actually used by the node pool. It is determined by the cgroup mode specified in the LinuxNodeConfig or the default cgroup mode based on the cluster creation version.

` .google.container.v1beta1.NodeConfig.EffectiveCgroupMode effective_cgroup_mode = 55 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeConfig.EffectiveCgroupMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfig.EffectiveCgroupMode)` | The effectiveCgroupMode.  
  
### getEffectiveCgroupModeValue()
    
    
    public abstract int getEffectiveCgroupModeValue()

Output only. effective_cgroup_mode is the cgroup mode actually used by the node pool. It is determined by the cgroup mode specified in the LinuxNodeConfig or the default cgroup mode based on the cluster creation version.

` .google.container.v1beta1.NodeConfig.EffectiveCgroupMode effective_cgroup_mode = 55 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for effectiveCgroupMode.  
  
### getEnableConfidentialStorage()
    
    
    public abstract boolean getEnableConfidentialStorage()

Optional. Reserved for future use.

`bool enable_confidential_storage = 46 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableConfidentialStorage.  
  
### getEphemeralStorageConfig()
    
    
    public abstract EphemeralStorageConfig getEphemeralStorageConfig()

Parameters for the ephemeral storage filesystem. If unspecified, ephemeral storage is backed by the boot disk.

`.google.container.v1beta1.EphemeralStorageConfig ephemeral_storage_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[EphemeralStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.EphemeralStorageConfig)` | The ephemeralStorageConfig.  
  
### getEphemeralStorageConfigOrBuilder()
    
    
    public abstract EphemeralStorageConfigOrBuilder getEphemeralStorageConfigOrBuilder()

Parameters for the ephemeral storage filesystem. If unspecified, ephemeral storage is backed by the boot disk.

`.google.container.v1beta1.EphemeralStorageConfig ephemeral_storage_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[EphemeralStorageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.EphemeralStorageConfigOrBuilder)` |   
  
### getEphemeralStorageLocalSsdConfig()
    
    
    public abstract EphemeralStorageLocalSsdConfig getEphemeralStorageLocalSsdConfig()

Parameters for the node ephemeral storage using Local SSDs. If unspecified, ephemeral storage is backed by the boot disk. This field is functionally equivalent to the ephemeral_storage_config

` .google.container.v1beta1.EphemeralStorageLocalSsdConfig ephemeral_storage_local_ssd_config = 41; `

**Returns**  
---  
**Type** | **Description**  
`[EphemeralStorageLocalSsdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.EphemeralStorageLocalSsdConfig)` | The ephemeralStorageLocalSsdConfig.  
  
### getEphemeralStorageLocalSsdConfigOrBuilder()
    
    
    public abstract EphemeralStorageLocalSsdConfigOrBuilder getEphemeralStorageLocalSsdConfigOrBuilder()

Parameters for the node ephemeral storage using Local SSDs. If unspecified, ephemeral storage is backed by the boot disk. This field is functionally equivalent to the ephemeral_storage_config

` .google.container.v1beta1.EphemeralStorageLocalSsdConfig ephemeral_storage_local_ssd_config = 41; `

**Returns**  
---  
**Type** | **Description**  
`[EphemeralStorageLocalSsdConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.EphemeralStorageLocalSsdConfigOrBuilder)` |   
  
### getFastSocket()
    
    
    public abstract FastSocket getFastSocket()

Enable or disable NCCL fast socket for the node pool.

`optional .google.container.v1beta1.FastSocket fast_socket = 36;`

**Returns**  
---  
**Type** | **Description**  
`[FastSocket](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.FastSocket)` | The fastSocket.  
  
### getFastSocketOrBuilder()
    
    
    public abstract FastSocketOrBuilder getFastSocketOrBuilder()

Enable or disable NCCL fast socket for the node pool.

`optional .google.container.v1beta1.FastSocket fast_socket = 36;`

**Returns**  
---  
**Type** | **Description**  
`[FastSocketOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.FastSocketOrBuilder)` |   
  
### getFlexStart()
    
    
    public abstract boolean getFlexStart()

Flex Start flag for enabling Flex Start VM.

`optional bool flex_start = 56;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The flexStart.  
  
### getGcfsConfig()
    
    
    public abstract GcfsConfig getGcfsConfig()

GCFS (Google Container File System) configs.

`.google.container.v1beta1.GcfsConfig gcfs_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig)` | The gcfsConfig.  
  
### getGcfsConfigOrBuilder()
    
    
    public abstract GcfsConfigOrBuilder getGcfsConfigOrBuilder()

GCFS (Google Container File System) configs.

`.google.container.v1beta1.GcfsConfig gcfs_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfigOrBuilder)` |   
  
### getGpuDirectConfig()
    
    
    public abstract GPUDirectConfig getGpuDirectConfig()

The configuration for GPU Direct

`optional .google.container.v1beta1.GPUDirectConfig gpu_direct_config = 51;`

**Returns**  
---  
**Type** | **Description**  
`[GPUDirectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUDirectConfig)` | The gpuDirectConfig.  
  
### getGpuDirectConfigOrBuilder()
    
    
    public abstract GPUDirectConfigOrBuilder getGpuDirectConfigOrBuilder()

The configuration for GPU Direct

`optional .google.container.v1beta1.GPUDirectConfig gpu_direct_config = 51;`

**Returns**  
---  
**Type** | **Description**  
`[GPUDirectConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GPUDirectConfigOrBuilder)` |   
  
### getGvnic()
    
    
    public abstract VirtualNIC getGvnic()

Enable or disable gvnic on the node pool.

`.google.container.v1beta1.VirtualNIC gvnic = 29;`

**Returns**  
---  
**Type** | **Description**  
`[VirtualNIC](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VirtualNIC)` | The gvnic.  
  
### getGvnicOrBuilder()
    
    
    public abstract VirtualNICOrBuilder getGvnicOrBuilder()

Enable or disable gvnic on the node pool.

`.google.container.v1beta1.VirtualNIC gvnic = 29;`

**Returns**  
---  
**Type** | **Description**  
`[VirtualNICOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VirtualNICOrBuilder)` |   
  
### getHostMaintenancePolicy()
    
    
    public abstract HostMaintenancePolicy getHostMaintenancePolicy()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy host_maintenance_policy = 44;`

**Returns**  
---  
**Type** | **Description**  
`[HostMaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy)` | The hostMaintenancePolicy.  
  
### getHostMaintenancePolicyOrBuilder()
    
    
    public abstract HostMaintenancePolicyOrBuilder getHostMaintenancePolicyOrBuilder()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy host_maintenance_policy = 44;`

**Returns**  
---  
**Type** | **Description**  
`[HostMaintenancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicyOrBuilder)` |   
  
### getImageType()
    
    
    public abstract String getImageType()

The image type to use for this node. Note that for a given image type, the latest version of it will be used. Please see <https://cloud.google.com/kubernetes-engine/docs/concepts/node-images> for available image types.

`string image_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imageType.  
  
### getImageTypeBytes()
    
    
    public abstract ByteString getImageTypeBytes()

The image type to use for this node. Note that for a given image type, the latest version of it will be used. Please see <https://cloud.google.com/kubernetes-engine/docs/concepts/node-images> for available image types.

`string image_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imageType.  
  
### getKubeletConfig()
    
    
    public abstract NodeKubeletConfig getKubeletConfig()

Node kubelet configs.

`.google.container.v1beta1.NodeKubeletConfig kubelet_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)` | The kubeletConfig.  
  
### getKubeletConfigOrBuilder()
    
    
    public abstract NodeKubeletConfigOrBuilder getKubeletConfigOrBuilder()

Node kubelet configs.

`.google.container.v1beta1.NodeKubeletConfig kubelet_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfigOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfigOrBuilder#com_google_container_v1beta1_NodeConfigOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

The Kubernetes labels (key/value pairs) to apply to each node. The values in this field are added to the set of default labels Kubernetes applies to nodes.

This field has the following restrictions:

  * Labels must use a valid Kubernetes syntax and character set, as defined in <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set>.
  * This field supports up to 1,024 total characters in a single request.

Depending on the Kubernetes version, keys in this field might conflict with the keys of the default labels, which might change which of your labels are applied to the nodes. Assume that the behavior is unpredictable and avoid label key conflicts. For more information about the default labels, see: <https://kubernetes.io/docs/reference/labels-annotations-taints/>




`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

The Kubernetes labels (key/value pairs) to apply to each node. The values in this field are added to the set of default labels Kubernetes applies to nodes.

This field has the following restrictions:

  * Labels must use a valid Kubernetes syntax and character set, as defined in <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set>.
  * This field supports up to 1,024 total characters in a single request.

Depending on the Kubernetes version, keys in this field might conflict with the keys of the default labels, which might change which of your labels are applied to the nodes. Assume that the behavior is unpredictable and avoid label key conflicts. For more information about the default labels, see: <https://kubernetes.io/docs/reference/labels-annotations-taints/>




`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

The Kubernetes labels (key/value pairs) to apply to each node. The values in this field are added to the set of default labels Kubernetes applies to nodes.

This field has the following restrictions:

  * Labels must use a valid Kubernetes syntax and character set, as defined in <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set>.
  * This field supports up to 1,024 total characters in a single request.

Depending on the Kubernetes version, keys in this field might conflict with the keys of the default labels, which might change which of your labels are applied to the nodes. Assume that the behavior is unpredictable and avoid label key conflicts. For more information about the default labels, see: <https://kubernetes.io/docs/reference/labels-annotations-taints/>




`map<string, string> labels = 6;`

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

The Kubernetes labels (key/value pairs) to apply to each node. The values in this field are added to the set of default labels Kubernetes applies to nodes.

This field has the following restrictions:

  * Labels must use a valid Kubernetes syntax and character set, as defined in <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set>.
  * This field supports up to 1,024 total characters in a single request.

Depending on the Kubernetes version, keys in this field might conflict with the keys of the default labels, which might change which of your labels are applied to the nodes. Assume that the behavior is unpredictable and avoid label key conflicts. For more information about the default labels, see: <https://kubernetes.io/docs/reference/labels-annotations-taints/>




`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLinuxNodeConfig()
    
    
    public abstract LinuxNodeConfig getLinuxNodeConfig()

Parameters that can be configured on Linux nodes.

`.google.container.v1beta1.LinuxNodeConfig linux_node_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig)` | The linuxNodeConfig.  
  
### getLinuxNodeConfigOrBuilder()
    
    
    public abstract LinuxNodeConfigOrBuilder getLinuxNodeConfigOrBuilder()

Parameters that can be configured on Linux nodes.

`.google.container.v1beta1.LinuxNodeConfig linux_node_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfigOrBuilder)` |   
  
### getLocalNvmeSsdBlockConfig()
    
    
    public abstract LocalNvmeSsdBlockConfig getLocalNvmeSsdBlockConfig()

Parameters for using raw-block Local NVMe SSDs.

`.google.container.v1beta1.LocalNvmeSsdBlockConfig local_nvme_ssd_block_config = 40; `

**Returns**  
---  
**Type** | **Description**  
`[LocalNvmeSsdBlockConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LocalNvmeSsdBlockConfig)` | The localNvmeSsdBlockConfig.  
  
### getLocalNvmeSsdBlockConfigOrBuilder()
    
    
    public abstract LocalNvmeSsdBlockConfigOrBuilder getLocalNvmeSsdBlockConfigOrBuilder()

Parameters for using raw-block Local NVMe SSDs.

`.google.container.v1beta1.LocalNvmeSsdBlockConfig local_nvme_ssd_block_config = 40; `

**Returns**  
---  
**Type** | **Description**  
`[LocalNvmeSsdBlockConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LocalNvmeSsdBlockConfigOrBuilder)` |   
  
### getLocalSsdCount()
    
    
    public abstract int getLocalSsdCount()

The number of local SSD disks to be attached to the node.

The limit for this value is dependent upon the maximum number of disks available on a machine per zone. See: <https://cloud.google.com/compute/docs/disks/local-ssd> for more information.

`int32 local_ssd_count = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The localSsdCount.  
  
### getLocalSsdEncryptionMode()
    
    
    public abstract NodeConfig.LocalSsdEncryptionMode getLocalSsdEncryptionMode()

Specifies which method should be used for encrypting the Local SSDs attached to the node.

` optional .google.container.v1beta1.NodeConfig.LocalSsdEncryptionMode local_ssd_encryption_mode = 54; `

**Returns**  
---  
**Type** | **Description**  
`[NodeConfig.LocalSsdEncryptionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfig.LocalSsdEncryptionMode)` | The localSsdEncryptionMode.  
  
### getLocalSsdEncryptionModeValue()
    
    
    public abstract int getLocalSsdEncryptionModeValue()

Specifies which method should be used for encrypting the Local SSDs attached to the node.

` optional .google.container.v1beta1.NodeConfig.LocalSsdEncryptionMode local_ssd_encryption_mode = 54; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for localSsdEncryptionMode.  
  
### getLoggingConfig()
    
    
    public abstract NodePoolLoggingConfig getLoggingConfig()

Logging configuration.

`.google.container.v1beta1.NodePoolLoggingConfig logging_config = 38;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig)` | The loggingConfig.  
  
### getLoggingConfigOrBuilder()
    
    
    public abstract NodePoolLoggingConfigOrBuilder getLoggingConfigOrBuilder()

Logging configuration.

`.google.container.v1beta1.NodePoolLoggingConfig logging_config = 38;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfigOrBuilder)` |   
  
### getMachineType()
    
    
    public abstract String getMachineType()

The name of a Google Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-types).

If unspecified, the default machine type is `e2-medium`.

`string machine_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

The name of a Google Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-types).

If unspecified, the default machine type is `e2-medium`.

`string machine_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMaxRunDuration()
    
    
    public abstract Duration getMaxRunDuration()

The maximum duration for the nodes to exist. If unspecified, the nodes can exist indefinitely.

`.google.protobuf.Duration max_run_duration = 53;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maxRunDuration.  
  
### getMaxRunDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getMaxRunDurationOrBuilder()

The maximum duration for the nodes to exist. If unspecified, the nodes can exist indefinitely.

`.google.protobuf.Duration max_run_duration = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMetadata() (deprecated)
    
    
    public abstract Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfigOrBuilder#com_google_container_v1beta1_NodeConfigOrBuilder_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public abstract int getMetadataCount()

The metadata key/value pairs assigned to instances in the cluster.

Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys:

  * "cluster-location"
  * "cluster-name"
  * "cluster-uid"
  * "configure-sh"
  * "containerd-configure-sh"
  * "enable-oslogin"
  * "gci-ensure-gke-docker"
  * "gci-metrics-enabled"
  * "gci-update-strategy"
  * "instance-template"
  * "kube-env"
  * "startup-script"
  * "user-data"
  * "disable-address-manager"
  * "windows-startup-script-ps1"
  * "common-psm1"
  * "k8s-node-setup-psm1"
  * "install-ssh-psm1"
  * "user-profile-psm1"

Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB.

The total size of all keys and values must be less than 512 KB.




`map<string, string> metadata = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public abstract Map<String,String> getMetadataMap()

The metadata key/value pairs assigned to instances in the cluster.

Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys:

  * "cluster-location"
  * "cluster-name"
  * "cluster-uid"
  * "configure-sh"
  * "containerd-configure-sh"
  * "enable-oslogin"
  * "gci-ensure-gke-docker"
  * "gci-metrics-enabled"
  * "gci-update-strategy"
  * "instance-template"
  * "kube-env"
  * "startup-script"
  * "user-data"
  * "disable-address-manager"
  * "windows-startup-script-ps1"
  * "common-psm1"
  * "k8s-node-setup-psm1"
  * "install-ssh-psm1"
  * "user-profile-psm1"

Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB.

The total size of all keys and values must be less than 512 KB.




`map<string, string> metadata = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public abstract String getMetadataOrDefault(String key, String defaultValue)

The metadata key/value pairs assigned to instances in the cluster.

Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys:

  * "cluster-location"
  * "cluster-name"
  * "cluster-uid"
  * "configure-sh"
  * "containerd-configure-sh"
  * "enable-oslogin"
  * "gci-ensure-gke-docker"
  * "gci-metrics-enabled"
  * "gci-update-strategy"
  * "instance-template"
  * "kube-env"
  * "startup-script"
  * "user-data"
  * "disable-address-manager"
  * "windows-startup-script-ps1"
  * "common-psm1"
  * "k8s-node-setup-psm1"
  * "install-ssh-psm1"
  * "user-profile-psm1"

Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB.

The total size of all keys and values must be less than 512 KB.




`map<string, string> metadata = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadataOrThrow(String key)
    
    
    public abstract String getMetadataOrThrow(String key)

The metadata key/value pairs assigned to instances in the cluster.

Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys:

  * "cluster-location"
  * "cluster-name"
  * "cluster-uid"
  * "configure-sh"
  * "containerd-configure-sh"
  * "enable-oslogin"
  * "gci-ensure-gke-docker"
  * "gci-metrics-enabled"
  * "gci-update-strategy"
  * "instance-template"
  * "kube-env"
  * "startup-script"
  * "user-data"
  * "disable-address-manager"
  * "windows-startup-script-ps1"
  * "common-psm1"
  * "k8s-node-setup-psm1"
  * "install-ssh-psm1"
  * "user-profile-psm1"

Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB.

The total size of all keys and values must be less than 512 KB.




`map<string, string> metadata = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMinCpuPlatform()
    
    
    public abstract String getMinCpuPlatform()

Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: "Intel Haswell"` or `minCpuPlatform: "Intel Sandy Bridge"`. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

`string min_cpu_platform = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minCpuPlatform.  
  
### getMinCpuPlatformBytes()
    
    
    public abstract ByteString getMinCpuPlatformBytes()

Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: "Intel Haswell"` or `minCpuPlatform: "Intel Sandy Bridge"`. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

`string min_cpu_platform = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minCpuPlatform.  
  
### getNodeGroup()
    
    
    public abstract String getNodeGroup()

Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on [sole tenant nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

`string node_group = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodeGroup.  
  
### getNodeGroupBytes()
    
    
    public abstract ByteString getNodeGroupBytes()

Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on [sole tenant nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

`string node_group = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodeGroup.  
  
### getNodeImageConfig()
    
    
    public abstract CustomImageConfig getNodeImageConfig()

The node image configuration to use for this node pool. Note that this is only applicable for node pools using image_type=CUSTOM.

`.google.container.v1beta1.CustomImageConfig node_image_config = 90;`

**Returns**  
---  
**Type** | **Description**  
`[CustomImageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CustomImageConfig)` | The nodeImageConfig.  
  
### getNodeImageConfigOrBuilder()
    
    
    public abstract CustomImageConfigOrBuilder getNodeImageConfigOrBuilder()

The node image configuration to use for this node pool. Note that this is only applicable for node pools using image_type=CUSTOM.

`.google.container.v1beta1.CustomImageConfig node_image_config = 90;`

**Returns**  
---  
**Type** | **Description**  
`[CustomImageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CustomImageConfigOrBuilder)` |   
  
### getOauthScopes(int index)
    
    
    public abstract String getOauthScopes(int index)

The set of Google API scopes to be made available on all of the node VMs under the "default" service account.

The following scopes are recommended, but not required, and by default are not included:

  * `<https://www.googleapis.com/auth/compute>` is required for mounting persistent storage on your nodes.
  * `<https://www.googleapis.com/auth/devstorage.read_only>` is required for communicating with **gcr.io** (the [Artifact Registry](https://cloud.google.com/artifact-registry/)).

If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.




`repeated string oauth_scopes = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The oauthScopes at the given index.  
  
### getOauthScopesBytes(int index)
    
    
    public abstract ByteString getOauthScopesBytes(int index)

The set of Google API scopes to be made available on all of the node VMs under the "default" service account.

The following scopes are recommended, but not required, and by default are not included:

  * `<https://www.googleapis.com/auth/compute>` is required for mounting persistent storage on your nodes.
  * `<https://www.googleapis.com/auth/devstorage.read_only>` is required for communicating with **gcr.io** (the [Artifact Registry](https://cloud.google.com/artifact-registry/)).

If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.




`repeated string oauth_scopes = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the oauthScopes at the given index.  
  
### getOauthScopesCount()
    
    
    public abstract int getOauthScopesCount()

The set of Google API scopes to be made available on all of the node VMs under the "default" service account.

The following scopes are recommended, but not required, and by default are not included:

  * `<https://www.googleapis.com/auth/compute>` is required for mounting persistent storage on your nodes.
  * `<https://www.googleapis.com/auth/devstorage.read_only>` is required for communicating with **gcr.io** (the [Artifact Registry](https://cloud.google.com/artifact-registry/)).

If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.




`repeated string oauth_scopes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of oauthScopes.  
  
### getOauthScopesList()
    
    
    public abstract List<String> getOauthScopesList()

The set of Google API scopes to be made available on all of the node VMs under the "default" service account.

The following scopes are recommended, but not required, and by default are not included:

  * `<https://www.googleapis.com/auth/compute>` is required for mounting persistent storage on your nodes.
  * `<https://www.googleapis.com/auth/devstorage.read_only>` is required for communicating with **gcr.io** (the [Artifact Registry](https://cloud.google.com/artifact-registry/)).

If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.




`repeated string oauth_scopes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the oauthScopes.  
  
### getPreemptible()
    
    
    public abstract boolean getPreemptible()

Whether the nodes are created as preemptible VM instances. See: <https://cloud.google.com/compute/docs/instances/preemptible> for more information about preemptible VM instances.

`bool preemptible = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preemptible.  
  
### getReservationAffinity()
    
    
    public abstract ReservationAffinity getReservationAffinity()

The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this node pool.

`.google.container.v1beta1.ReservationAffinity reservation_affinity = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ReservationAffinity](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReservationAffinity)` | The reservationAffinity.  
  
### getReservationAffinityOrBuilder()
    
    
    public abstract ReservationAffinityOrBuilder getReservationAffinityOrBuilder()

The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this node pool.

`.google.container.v1beta1.ReservationAffinity reservation_affinity = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ReservationAffinityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReservationAffinityOrBuilder)` |   
  
### getResourceLabels() (deprecated)
    
    
    public abstract Map<String,String> getResourceLabels()

Use [#getResourceLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeConfigOrBuilder#com_google_container_v1beta1_NodeConfigOrBuilder_getResourceLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsCount()
    
    
    public abstract int getResourceLabelsCount()

The resource labels for the node pool to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 37;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceLabelsMap()
    
    
    public abstract Map<String,String> getResourceLabelsMap()

The resource labels for the node pool to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 37;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getResourceLabelsOrDefault(String key, String defaultValue)

The resource labels for the node pool to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 37;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceLabelsOrThrow(String key)
    
    
    public abstract String getResourceLabelsOrThrow(String key)

The resource labels for the node pool to use to annotate any related Google Compute Engine resources.

`map<string, string> resource_labels = 37;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceManagerTags()
    
    
    public abstract ResourceManagerTags getResourceManagerTags()

A map of resource manager tag keys and values to be attached to the nodes.

`.google.container.v1beta1.ResourceManagerTags resource_manager_tags = 45;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags)` | The resourceManagerTags.  
  
### getResourceManagerTagsOrBuilder()
    
    
    public abstract ResourceManagerTagsOrBuilder getResourceManagerTagsOrBuilder()

A map of resource manager tag keys and values to be attached to the nodes.

`.google.container.v1beta1.ResourceManagerTags resource_manager_tags = 45;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTagsOrBuilder)` |   
  
### getSandboxConfig()
    
    
    public abstract SandboxConfig getSandboxConfig()

Sandbox configuration for this node.

`.google.container.v1beta1.SandboxConfig sandbox_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[SandboxConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SandboxConfig)` | The sandboxConfig.  
  
### getSandboxConfigOrBuilder()
    
    
    public abstract SandboxConfigOrBuilder getSandboxConfigOrBuilder()

Sandbox configuration for this node.

`.google.container.v1beta1.SandboxConfig sandbox_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[SandboxConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SandboxConfigOrBuilder)` |   
  
### getSecondaryBootDiskUpdateStrategy()
    
    
    public abstract SecondaryBootDiskUpdateStrategy getSecondaryBootDiskUpdateStrategy()

Secondary boot disk update strategy.

` optional .google.container.v1beta1.SecondaryBootDiskUpdateStrategy secondary_boot_disk_update_strategy = 50; `

**Returns**  
---  
**Type** | **Description**  
`[SecondaryBootDiskUpdateStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecondaryBootDiskUpdateStrategy)` | The secondaryBootDiskUpdateStrategy.  
  
### getSecondaryBootDiskUpdateStrategyOrBuilder()
    
    
    public abstract SecondaryBootDiskUpdateStrategyOrBuilder getSecondaryBootDiskUpdateStrategyOrBuilder()

Secondary boot disk update strategy.

` optional .google.container.v1beta1.SecondaryBootDiskUpdateStrategy secondary_boot_disk_update_strategy = 50; `

**Returns**  
---  
**Type** | **Description**  
`[SecondaryBootDiskUpdateStrategyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecondaryBootDiskUpdateStrategyOrBuilder)` |   
  
### getSecondaryBootDisks(int index)
    
    
    public abstract SecondaryBootDisk getSecondaryBootDisks(int index)

List of secondary boot disks attached to the nodes.

`repeated .google.container.v1beta1.SecondaryBootDisk secondary_boot_disks = 48;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecondaryBootDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecondaryBootDisk)` |   
  
### getSecondaryBootDisksCount()
    
    
    public abstract int getSecondaryBootDisksCount()

List of secondary boot disks attached to the nodes.

`repeated .google.container.v1beta1.SecondaryBootDisk secondary_boot_disks = 48;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSecondaryBootDisksList()
    
    
    public abstract List<SecondaryBootDisk> getSecondaryBootDisksList()

List of secondary boot disks attached to the nodes.

`repeated .google.container.v1beta1.SecondaryBootDisk secondary_boot_disks = 48;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SecondaryBootDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecondaryBootDisk)>` |   
  
### getSecondaryBootDisksOrBuilder(int index)
    
    
    public abstract SecondaryBootDiskOrBuilder getSecondaryBootDisksOrBuilder(int index)

List of secondary boot disks attached to the nodes.

`repeated .google.container.v1beta1.SecondaryBootDisk secondary_boot_disks = 48;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecondaryBootDiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecondaryBootDiskOrBuilder)` |   
  
### getSecondaryBootDisksOrBuilderList()
    
    
    public abstract List<? extends SecondaryBootDiskOrBuilder> getSecondaryBootDisksOrBuilderList()

List of secondary boot disks attached to the nodes.

`repeated .google.container.v1beta1.SecondaryBootDisk secondary_boot_disks = 48;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1beta1.SecondaryBootDiskOrBuilder>` |   
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

The Google Cloud Platform Service Account to be used by the node VMs. Specify the email address of the Service Account; otherwise, if no Service Account is specified, the "default" service account is used.

`string service_account = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

The Google Cloud Platform Service Account to be used by the node VMs. Specify the email address of the Service Account; otherwise, if no Service Account is specified, the "default" service account is used.

`string service_account = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getShieldedInstanceConfig()
    
    
    public abstract ShieldedInstanceConfig getShieldedInstanceConfig()

Shielded Instance options.

`.google.container.v1beta1.ShieldedInstanceConfig shielded_instance_config = 20;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedInstanceConfig)` | The shieldedInstanceConfig.  
  
### getShieldedInstanceConfigOrBuilder()
    
    
    public abstract ShieldedInstanceConfigOrBuilder getShieldedInstanceConfigOrBuilder()

Shielded Instance options.

`.google.container.v1beta1.ShieldedInstanceConfig shielded_instance_config = 20;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedInstanceConfigOrBuilder)` |   
  
### getSoleTenantConfig()
    
    
    public abstract SoleTenantConfig getSoleTenantConfig()

Parameters for node pools to be backed by shared sole tenant node groups.

`.google.container.v1beta1.SoleTenantConfig sole_tenant_config = 42;`

**Returns**  
---  
**Type** | **Description**  
`[SoleTenantConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SoleTenantConfig)` | The soleTenantConfig.  
  
### getSoleTenantConfigOrBuilder()
    
    
    public abstract SoleTenantConfigOrBuilder getSoleTenantConfigOrBuilder()

Parameters for node pools to be backed by shared sole tenant node groups.

`.google.container.v1beta1.SoleTenantConfig sole_tenant_config = 42;`

**Returns**  
---  
**Type** | **Description**  
`[SoleTenantConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SoleTenantConfigOrBuilder)` |   
  
### getSpot()
    
    
    public abstract boolean getSpot()

Spot flag for enabling Spot VM, which is a rebrand of the existing preemptible flag.

`bool spot = 32;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The spot.  
  
### getStoragePools(int index)
    
    
    public abstract String getStoragePools(int index)

List of Storage Pools where boot disks are provisioned.

`repeated string storage_pools = 49;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The storagePools at the given index.  
  
### getStoragePoolsBytes(int index)
    
    
    public abstract ByteString getStoragePoolsBytes(int index)

List of Storage Pools where boot disks are provisioned.

`repeated string storage_pools = 49;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the storagePools at the given index.  
  
### getStoragePoolsCount()
    
    
    public abstract int getStoragePoolsCount()

List of Storage Pools where boot disks are provisioned.

`repeated string storage_pools = 49;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of storagePools.  
  
### getStoragePoolsList()
    
    
    public abstract List<String> getStoragePoolsList()

List of Storage Pools where boot disks are provisioned.

`repeated string storage_pools = 49;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the storagePools.  
  
### getTags(int index)
    
    
    public abstract String getTags(int index)

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.

`repeated string tags = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public abstract ByteString getTagsBytes(int index)

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.

`repeated string tags = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.

`repeated string tags = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public abstract List<String> getTagsList()

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.

`repeated string tags = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tags.  
  
### getTaintConfig()
    
    
    public abstract TaintConfig getTaintConfig()

Optional. The taint configuration for the node pool.

` optional .google.container.v1beta1.TaintConfig taint_config = 62 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TaintConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TaintConfig)` | The taintConfig.  
  
### getTaintConfigOrBuilder()
    
    
    public abstract TaintConfigOrBuilder getTaintConfigOrBuilder()

Optional. The taint configuration for the node pool.

` optional .google.container.v1beta1.TaintConfig taint_config = 62 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TaintConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TaintConfigOrBuilder)` |   
  
### getTaints(int index)
    
    
    public abstract NodeTaint getTaints(int index)

List of kubernetes taints to be applied to each node.

For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

`repeated .google.container.v1beta1.NodeTaint taints = 15;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodeTaint](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeTaint)` |   
  
### getTaintsCount()
    
    
    public abstract int getTaintsCount()

List of kubernetes taints to be applied to each node.

For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

`repeated .google.container.v1beta1.NodeTaint taints = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTaintsList()
    
    
    public abstract List<NodeTaint> getTaintsList()

List of kubernetes taints to be applied to each node.

For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

`repeated .google.container.v1beta1.NodeTaint taints = 15;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NodeTaint](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeTaint)>` |   
  
### getTaintsOrBuilder(int index)
    
    
    public abstract NodeTaintOrBuilder getTaintsOrBuilder(int index)

List of kubernetes taints to be applied to each node.

For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

`repeated .google.container.v1beta1.NodeTaint taints = 15;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodeTaintOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeTaintOrBuilder)` |   
  
### getTaintsOrBuilderList()
    
    
    public abstract List<? extends NodeTaintOrBuilder> getTaintsOrBuilderList()

List of kubernetes taints to be applied to each node.

For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/>

`repeated .google.container.v1beta1.NodeTaint taints = 15;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1beta1.NodeTaintOrBuilder>` |   
  
### getWindowsNodeConfig()
    
    
    public abstract WindowsNodeConfig getWindowsNodeConfig()

Parameters that can be configured on Windows nodes.

`.google.container.v1beta1.WindowsNodeConfig windows_node_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WindowsNodeConfig)` | The windowsNodeConfig.  
  
### getWindowsNodeConfigOrBuilder()
    
    
    public abstract WindowsNodeConfigOrBuilder getWindowsNodeConfigOrBuilder()

Parameters that can be configured on Windows nodes.

`.google.container.v1beta1.WindowsNodeConfig windows_node_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsNodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WindowsNodeConfigOrBuilder)` |   
  
### getWorkloadMetadataConfig()
    
    
    public abstract WorkloadMetadataConfig getWorkloadMetadataConfig()

The workload metadata configuration for this node.

`.google.container.v1beta1.WorkloadMetadataConfig workload_metadata_config = 14;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadMetadataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadMetadataConfig)` | The workloadMetadataConfig.  
  
### getWorkloadMetadataConfigOrBuilder()
    
    
    public abstract WorkloadMetadataConfigOrBuilder getWorkloadMetadataConfigOrBuilder()

The workload metadata configuration for this node.

`.google.container.v1beta1.WorkloadMetadataConfig workload_metadata_config = 14;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadMetadataConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadMetadataConfigOrBuilder)` |   
  
### hasAdvancedMachineFeatures()
    
    
    public abstract boolean hasAdvancedMachineFeatures()

Advanced features for the Compute Engine VM.

`.google.container.v1beta1.AdvancedMachineFeatures advanced_machine_features = 26;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the advancedMachineFeatures field is set.  
  
### hasBootDisk()
    
    
    public abstract boolean hasBootDisk()

Boot disk configuration for the node pool.

`.google.container.v1beta1.BootDisk boot_disk = 57;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bootDisk field is set.  
  
### hasConfidentialNodes()
    
    
    public abstract boolean hasConfidentialNodes()

Confidential nodes config. All the nodes in the node pool will be Confidential VM once enabled.

`.google.container.v1beta1.ConfidentialNodes confidential_nodes = 35;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the confidentialNodes field is set.  
  
### hasConsolidationDelay()
    
    
    public abstract boolean hasConsolidationDelay()

Consolidation delay defines duration after which the Cluster Autoscaler can scale down underutilized nodes. If not set, nodes are scaled down by default behavior, i.e. according to the chosen autoscaling profile.

`.google.protobuf.Duration consolidation_delay = 60;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the consolidationDelay field is set.  
  
### hasContainerdConfig()
    
    
    public abstract boolean hasContainerdConfig()

Parameters for containerd customization.

`.google.container.v1beta1.ContainerdConfig containerd_config = 43;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the containerdConfig field is set.  
  
### hasEphemeralStorageConfig()
    
    
    public abstract boolean hasEphemeralStorageConfig()

Parameters for the ephemeral storage filesystem. If unspecified, ephemeral storage is backed by the boot disk.

`.google.container.v1beta1.EphemeralStorageConfig ephemeral_storage_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ephemeralStorageConfig field is set.  
  
### hasEphemeralStorageLocalSsdConfig()
    
    
    public abstract boolean hasEphemeralStorageLocalSsdConfig()

Parameters for the node ephemeral storage using Local SSDs. If unspecified, ephemeral storage is backed by the boot disk. This field is functionally equivalent to the ephemeral_storage_config

` .google.container.v1beta1.EphemeralStorageLocalSsdConfig ephemeral_storage_local_ssd_config = 41; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ephemeralStorageLocalSsdConfig field is set.  
  
### hasFastSocket()
    
    
    public abstract boolean hasFastSocket()

Enable or disable NCCL fast socket for the node pool.

`optional .google.container.v1beta1.FastSocket fast_socket = 36;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fastSocket field is set.  
  
### hasFlexStart()
    
    
    public abstract boolean hasFlexStart()

Flex Start flag for enabling Flex Start VM.

`optional bool flex_start = 56;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flexStart field is set.  
  
### hasGcfsConfig()
    
    
    public abstract boolean hasGcfsConfig()

GCFS (Google Container File System) configs.

`.google.container.v1beta1.GcfsConfig gcfs_config = 25;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcfsConfig field is set.  
  
### hasGpuDirectConfig()
    
    
    public abstract boolean hasGpuDirectConfig()

The configuration for GPU Direct

`optional .google.container.v1beta1.GPUDirectConfig gpu_direct_config = 51;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gpuDirectConfig field is set.  
  
### hasGvnic()
    
    
    public abstract boolean hasGvnic()

Enable or disable gvnic on the node pool.

`.google.container.v1beta1.VirtualNIC gvnic = 29;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gvnic field is set.  
  
### hasHostMaintenancePolicy()
    
    
    public abstract boolean hasHostMaintenancePolicy()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy host_maintenance_policy = 44;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hostMaintenancePolicy field is set.  
  
### hasKubeletConfig()
    
    
    public abstract boolean hasKubeletConfig()

Node kubelet configs.

`.google.container.v1beta1.NodeKubeletConfig kubelet_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kubeletConfig field is set.  
  
### hasLinuxNodeConfig()
    
    
    public abstract boolean hasLinuxNodeConfig()

Parameters that can be configured on Linux nodes.

`.google.container.v1beta1.LinuxNodeConfig linux_node_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the linuxNodeConfig field is set.  
  
### hasLocalNvmeSsdBlockConfig()
    
    
    public abstract boolean hasLocalNvmeSsdBlockConfig()

Parameters for using raw-block Local NVMe SSDs.

`.google.container.v1beta1.LocalNvmeSsdBlockConfig local_nvme_ssd_block_config = 40; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localNvmeSsdBlockConfig field is set.  
  
### hasLocalSsdEncryptionMode()
    
    
    public abstract boolean hasLocalSsdEncryptionMode()

Specifies which method should be used for encrypting the Local SSDs attached to the node.

` optional .google.container.v1beta1.NodeConfig.LocalSsdEncryptionMode local_ssd_encryption_mode = 54; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the localSsdEncryptionMode field is set.  
  
### hasLoggingConfig()
    
    
    public abstract boolean hasLoggingConfig()

Logging configuration.

`.google.container.v1beta1.NodePoolLoggingConfig logging_config = 38;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loggingConfig field is set.  
  
### hasMaxRunDuration()
    
    
    public abstract boolean hasMaxRunDuration()

The maximum duration for the nodes to exist. If unspecified, the nodes can exist indefinitely.

`.google.protobuf.Duration max_run_duration = 53;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxRunDuration field is set.  
  
### hasNodeImageConfig()
    
    
    public abstract boolean hasNodeImageConfig()

The node image configuration to use for this node pool. Note that this is only applicable for node pools using image_type=CUSTOM.

`.google.container.v1beta1.CustomImageConfig node_image_config = 90;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeImageConfig field is set.  
  
### hasReservationAffinity()
    
    
    public abstract boolean hasReservationAffinity()

The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this node pool.

`.google.container.v1beta1.ReservationAffinity reservation_affinity = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reservationAffinity field is set.  
  
### hasResourceManagerTags()
    
    
    public abstract boolean hasResourceManagerTags()

A map of resource manager tag keys and values to be attached to the nodes.

`.google.container.v1beta1.ResourceManagerTags resource_manager_tags = 45;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resourceManagerTags field is set.  
  
### hasSandboxConfig()
    
    
    public abstract boolean hasSandboxConfig()

Sandbox configuration for this node.

`.google.container.v1beta1.SandboxConfig sandbox_config = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sandboxConfig field is set.  
  
### hasSecondaryBootDiskUpdateStrategy()
    
    
    public abstract boolean hasSecondaryBootDiskUpdateStrategy()

Secondary boot disk update strategy.

` optional .google.container.v1beta1.SecondaryBootDiskUpdateStrategy secondary_boot_disk_update_strategy = 50; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the secondaryBootDiskUpdateStrategy field is set.  
  
### hasShieldedInstanceConfig()
    
    
    public abstract boolean hasShieldedInstanceConfig()

Shielded Instance options.

`.google.container.v1beta1.ShieldedInstanceConfig shielded_instance_config = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shieldedInstanceConfig field is set.  
  
### hasSoleTenantConfig()
    
    
    public abstract boolean hasSoleTenantConfig()

Parameters for node pools to be backed by shared sole tenant node groups.

`.google.container.v1beta1.SoleTenantConfig sole_tenant_config = 42;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the soleTenantConfig field is set.  
  
### hasTaintConfig()
    
    
    public abstract boolean hasTaintConfig()

Optional. The taint configuration for the node pool.

` optional .google.container.v1beta1.TaintConfig taint_config = 62 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the taintConfig field is set.  
  
### hasWindowsNodeConfig()
    
    
    public abstract boolean hasWindowsNodeConfig()

Parameters that can be configured on Windows nodes.

`.google.container.v1beta1.WindowsNodeConfig windows_node_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowsNodeConfig field is set.  
  
### hasWorkloadMetadataConfig()
    
    
    public abstract boolean hasWorkloadMetadataConfig()

The workload metadata configuration for this node.

`.google.container.v1beta1.WorkloadMetadataConfig workload_metadata_config = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the workloadMetadataConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
