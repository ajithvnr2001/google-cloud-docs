---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoprovisioningNodePoolDefaultsOrBuilder
title: Interface AutoprovisioningNodePoolDefaultsOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:58.900626+00:00
---

# Interface AutoprovisioningNodePoolDefaultsOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AutoprovisioningNodePoolDefaultsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AutoprovisioningNodePoolDefaultsOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface AutoprovisioningNodePoolDefaultsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBootDiskKmsKey()
    
    
    public abstract String getBootDiskKmsKey()

The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <https://cloud.google.com/compute/docs/disks/customer-managed-encryption>

`string boot_disk_kms_key = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bootDiskKmsKey.  
  
### getBootDiskKmsKeyBytes()
    
    
    public abstract ByteString getBootDiskKmsKeyBytes()

The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <https://cloud.google.com/compute/docs/disks/customer-managed-encryption>

`string boot_disk_kms_key = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bootDiskKmsKey.  
  
### getDiskSizeGb()
    
    
    public abstract int getDiskSizeGb()

Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.

If unspecified, the default disk size is 100GB.

`int32 disk_size_gb = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskSizeGb.  
  
### getDiskType()
    
    
    public abstract String getDiskType()

Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced')

If unspecified, the default disk type is 'pd-standard'

`string disk_type = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskType.  
  
### getDiskTypeBytes()
    
    
    public abstract ByteString getDiskTypeBytes()

Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced')

If unspecified, the default disk type is 'pd-standard'

`string disk_type = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskType.  
  
### getImageType()
    
    
    public abstract String getImageType()

The image type to use for NAP created node. Please see <https://cloud.google.com/kubernetes-engine/docs/concepts/node-images> for available image types.

`string image_type = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imageType.  
  
### getImageTypeBytes()
    
    
    public abstract ByteString getImageTypeBytes()

The image type to use for NAP created node. Please see <https://cloud.google.com/kubernetes-engine/docs/concepts/node-images> for available image types.

`string image_type = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imageType.  
  
### getInsecureKubeletReadonlyPortEnabled()
    
    
    public abstract boolean getInsecureKubeletReadonlyPortEnabled()

DEPRECATED. Use NodePoolAutoConfig.NodeKubeletConfig instead.

`optional bool insecure_kubelet_readonly_port_enabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The insecureKubeletReadonlyPortEnabled.  
  
### getManagement()
    
    
    public abstract NodeManagement getManagement()

Specifies the node management options for NAP created node-pools.

`.google.container.v1.NodeManagement management = 4;`

**Returns**  
---  
**Type** | **Description**  
`[NodeManagement](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeManagement)` | The management.  
  
### getManagementOrBuilder()
    
    
    public abstract NodeManagementOrBuilder getManagementOrBuilder()

Specifies the node management options for NAP created node-pools.

`.google.container.v1.NodeManagement management = 4;`

**Returns**  
---  
**Type** | **Description**  
`[NodeManagementOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeManagementOrBuilder)` |   
  
### getMinCpuPlatform() (deprecated)
    
    
    public abstract String getMinCpuPlatform()

**Deprecated.** _google.container.v1.AutoprovisioningNodePoolDefaults.min_cpu_platform is deprecated. See google/container/v1/cluster_service.proto;l=5937_

Deprecated. Minimum CPU platform to be used for NAP created node pools. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: Intel Haswell or minCpuPlatform: Intel Sandy Bridge. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform). This field is deprecated, min_cpu_platform should be specified using `cloud.google.com/requested-min-cpu-platform` label selector on the pod. To unset the min cpu platform field pass "automatic" as field value.

`string min_cpu_platform = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minCpuPlatform.  
  
### getMinCpuPlatformBytes() (deprecated)
    
    
    public abstract ByteString getMinCpuPlatformBytes()

**Deprecated.** _google.container.v1.AutoprovisioningNodePoolDefaults.min_cpu_platform is deprecated. See google/container/v1/cluster_service.proto;l=5937_

Deprecated. Minimum CPU platform to be used for NAP created node pools. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: Intel Haswell or minCpuPlatform: Intel Sandy Bridge. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform). This field is deprecated, min_cpu_platform should be specified using `cloud.google.com/requested-min-cpu-platform` label selector on the pod. To unset the min cpu platform field pass "automatic" as field value.

`string min_cpu_platform = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minCpuPlatform.  
  
### getOauthScopes(int index)
    
    
    public abstract String getOauthScopes(int index)

Scopes that are used by NAP when creating node pools.

`repeated string oauth_scopes = 1;`

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

Scopes that are used by NAP when creating node pools.

`repeated string oauth_scopes = 1;`

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

Scopes that are used by NAP when creating node pools.

`repeated string oauth_scopes = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of oauthScopes.  
  
### getOauthScopesList()
    
    
    public abstract List<String> getOauthScopesList()

Scopes that are used by NAP when creating node pools.

`repeated string oauth_scopes = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the oauthScopes.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

The Google Cloud Platform Service Account to be used by the node VMs.

`string service_account = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

The Google Cloud Platform Service Account to be used by the node VMs.

`string service_account = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getShieldedInstanceConfig()
    
    
    public abstract ShieldedInstanceConfig getShieldedInstanceConfig()

Shielded Instance options.

`.google.container.v1.ShieldedInstanceConfig shielded_instance_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedInstanceConfig)` | The shieldedInstanceConfig.  
  
### getShieldedInstanceConfigOrBuilder()
    
    
    public abstract ShieldedInstanceConfigOrBuilder getShieldedInstanceConfigOrBuilder()

Shielded Instance options.

`.google.container.v1.ShieldedInstanceConfig shielded_instance_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ShieldedInstanceConfigOrBuilder)` |   
  
### getUpgradeSettings()
    
    
    public abstract NodePool.UpgradeSettings getUpgradeSettings()

Specifies the upgrade settings for NAP created node pools

`.google.container.v1.NodePool.UpgradeSettings upgrade_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NodePool.UpgradeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool.UpgradeSettings)` | The upgradeSettings.  
  
### getUpgradeSettingsOrBuilder()
    
    
    public abstract NodePool.UpgradeSettingsOrBuilder getUpgradeSettingsOrBuilder()

Specifies the upgrade settings for NAP created node pools

`.google.container.v1.NodePool.UpgradeSettings upgrade_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NodePool.UpgradeSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool.UpgradeSettingsOrBuilder)` |   
  
### hasInsecureKubeletReadonlyPortEnabled()
    
    
    public abstract boolean hasInsecureKubeletReadonlyPortEnabled()

DEPRECATED. Use NodePoolAutoConfig.NodeKubeletConfig instead.

`optional bool insecure_kubelet_readonly_port_enabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the insecureKubeletReadonlyPortEnabled field is set.  
  
### hasManagement()
    
    
    public abstract boolean hasManagement()

Specifies the node management options for NAP created node-pools.

`.google.container.v1.NodeManagement management = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the management field is set.  
  
### hasShieldedInstanceConfig()
    
    
    public abstract boolean hasShieldedInstanceConfig()

Shielded Instance options.

`.google.container.v1.ShieldedInstanceConfig shielded_instance_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shieldedInstanceConfig field is set.  
  
### hasUpgradeSettings()
    
    
    public abstract boolean hasUpgradeSettings()

Specifies the upgrade settings for NAP created node pools

`.google.container.v1.NodePool.UpgradeSettings upgrade_settings = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the upgradeSettings field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
