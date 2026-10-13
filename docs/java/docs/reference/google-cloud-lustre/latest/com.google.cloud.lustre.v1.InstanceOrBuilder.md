---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.InstanceOrBuilder
title: Interface InstanceOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:04.960892+00:00
---

# Interface InstanceOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.InstanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InstanceOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface InstanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels as key value pairs.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessRulesOptions()
    
    
    public abstract AccessRulesOptions getAccessRulesOptions()

Optional. The access rules options for the instance.

` .google.cloud.lustre.v1.AccessRulesOptions access_rules_options = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessRulesOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptions)` | The accessRulesOptions.  
  
### getAccessRulesOptionsOrBuilder()
    
    
    public abstract AccessRulesOptionsOrBuilder getAccessRulesOptionsOrBuilder()

Optional. The access rules options for the instance.

` .google.cloud.lustre.v1.AccessRulesOptions access_rules_options = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessRulesOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptionsOrBuilder)` |   
  
### getAvailableVersion()
    
    
    public abstract String getAvailableVersion()

Output only. The available version that this instance can be upgraded to. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string available_version = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The availableVersion.  
  
### getAvailableVersionBytes()
    
    
    public abstract ByteString getAvailableVersionBytes()

Output only. The available version that this instance can be upgraded to. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string available_version = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for availableVersion.  
  
### getCapacityGib()
    
    
    public abstract long getCapacityGib()

Required. The storage capacity of the instance in gibibytes (GiB). Allowed values depend on the `perUnitStorageThroughput`. See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for specific minimums, maximums, and step sizes for each performance tier.

`int64 capacity_gib = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The capacityGib.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Timestamp when the instance was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when the instance was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A user-readable description of the instance.

`string description = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A user-readable description of the instance.

`string description = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDynamicTierOptions()
    
    
    public abstract DynamicTierOptions getDynamicTierOptions()

Optional. Immutable. Specifies whether the instance is on the Dynamic tier. See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for more information.

` .google.cloud.lustre.v1.DynamicTierOptions dynamic_tier_options = 24 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DynamicTierOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DynamicTierOptions)` | The dynamicTierOptions.  
  
### getDynamicTierOptionsOrBuilder()
    
    
    public abstract DynamicTierOptionsOrBuilder getDynamicTierOptionsOrBuilder()

Optional. Immutable. Specifies whether the instance is on the Dynamic tier. See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for more information.

` .google.cloud.lustre.v1.DynamicTierOptions dynamic_tier_options = 24 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DynamicTierOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DynamicTierOptionsOrBuilder)` |   
  
### getEffectiveVersion()
    
    
    public abstract String getEffectiveVersion()

Output only. The effective version of the instance. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string effective_version = 35 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The effectiveVersion.  
  
### getEffectiveVersionBytes()
    
    
    public abstract ByteString getEffectiveVersionBytes()

Output only. The effective version of the instance. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string effective_version = 35 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for effectiveVersion.  
  
### getFilesystem()
    
    
    public abstract String getFilesystem()

Required. Immutable. The filesystem name for this instance. This name is used by client-side tools, including when mounting the instance. Must be eight characters or less and can only contain letters and numbers.

` string filesystem = 10 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filesystem.  
  
### getFilesystemBytes()
    
    
    public abstract ByteString getFilesystemBytes()

Required. Immutable. The filesystem name for this instance. This name is used by client-side tools, including when mounting the instance. Must be eight characters or less and can only contain letters and numbers.

` string filesystem = 10 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filesystem.  
  
### getGkeSupportEnabled() (deprecated)
    
    
    public abstract boolean getGkeSupportEnabled()

**Deprecated.** _google.cloud.lustre.v1.Instance.gke_support_enabled is deprecated. See google/cloud/lustre/v1/instance.proto;l=133_

Optional. Deprecated: No longer required for GKE instance creation. Indicates whether you want to enable support for GKE clients. By default, GKE clients are not supported.

` bool gke_support_enabled = 12 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The gkeSupportEnabled.  
  
### getKmsKey()
    
    
    public abstract String getKmsKey()

Optional. Immutable. The Cloud KMS key name to use for data encryption. If not set, the instance will use Google-managed encryption keys. If set, the instance will use customer-managed encryption keys. The key must be in the same region as the instance. The key format is: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}

` string kms_key = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKey.  
  
### getKmsKeyBytes()
    
    
    public abstract ByteString getKmsKeyBytes()

Optional. Immutable. The Cloud KMS key name to use for data encryption. If not set, the instance will use Google-managed encryption keys. If set, the instance will use customer-managed encryption keys. The key must be in the same region as the instance. The key format is: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}

` string kms_key = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKey.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.InstanceOrBuilder#com_google_cloud_lustre_v1_InstanceOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels as key value pairs.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels as key value pairs.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels as key value pairs.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Labels as key value pairs.

`map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaintenancePolicy()
    
    
    public abstract MaintenancePolicy getMaintenancePolicy()

Optional. The maintenance policy for the instance to determine when to allow or exclude the instance from maintenance updates.

` .google.cloud.lustre.v1.MaintenancePolicy maintenance_policy = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.MaintenancePolicy)` | The maintenancePolicy.  
  
### getMaintenancePolicyOrBuilder()
    
    
    public abstract MaintenancePolicyOrBuilder getMaintenancePolicyOrBuilder()

Optional. The maintenance policy for the instance to determine when to allow or exclude the instance from maintenance updates.

` .google.cloud.lustre.v1.MaintenancePolicy maintenance_policy = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.MaintenancePolicyOrBuilder)` |   
  
### getMountPoint()
    
    
    public abstract String getMountPoint()

Output only. Mount point of the instance in the format `IP_ADDRESS@tcp:/FILESYSTEM`.

`string mount_point = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mountPoint.  
  
### getMountPointBytes()
    
    
    public abstract ByteString getMountPointBytes()

Output only. Mount point of the instance in the format `IP_ADDRESS@tcp:/FILESYSTEM`.

`string mount_point = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mountPoint.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the instance.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the instance.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Required. Immutable. The full name of the VPC network to which the instance is connected. Must be in the format `projects/{project_id}/global/networks/{network_name}`.

` string network = 3 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Required. Immutable. The full name of the VPC network to which the instance is connected. Must be in the format `projects/{project_id}/global/networks/{network_name}`.

` string network = 3 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getPerUnitStorageThroughput()
    
    
    public abstract long getPerUnitStorageThroughput()

Optional. The throughput of the instance in MBps per TiB. Valid values are 0, 125, 250, 500, 1000. See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for more information.

If the instance is using the Dynamic tier, this field must not be set or must be set to zero.

`int64 per_unit_storage_throughput = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The perUnitStorageThroughput.  
  
### getPlacementPolicy()
    
    
    public abstract String getPlacementPolicy()

Optional. The placement policy name for the instance in the format of projects/{project}/locations/{location}/resourcePolicies/{resource_policy}

` string placement_policy = 17 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The placementPolicy.  
  
### getPlacementPolicyBytes()
    
    
    public abstract ByteString getPlacementPolicyBytes()

Optional. The placement policy name for the instance in the format of projects/{project}/locations/{location}/resourcePolicies/{resource_policy}

` string placement_policy = 17 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for placementPolicy.  
  
### getState()
    
    
    public abstract Instance.State getState()

Output only. The state of the instance.

` .google.cloud.lustre.v1.Instance.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.Instance.State)` | The state.  
  
### getStateReason()
    
    
    public abstract String getStateReason()

Output only. The reason why the instance is in a certain state (e.g. SUSPENDED).

`string state_reason = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateReason.  
  
### getStateReasonBytes()
    
    
    public abstract ByteString getStateReasonBytes()

Output only. The reason why the instance is in a certain state (e.g. SUSPENDED).

`string state_reason = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateReason.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The state of the instance.

` .google.cloud.lustre.v1.Instance.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTargetVersion()
    
    
    public abstract String getTargetVersion()

Optional. The target version of the instance. Setting this field triggers a self-service update to the specified version. Format: `Lustre_YYYYMMDD.NN_pXX` or `latest`

`optional string target_version = 34 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetVersion.  
  
### getTargetVersionBytes()
    
    
    public abstract ByteString getTargetVersionBytes()

Optional. The target version of the instance. Setting this field triggers a self-service update to the specified version. Format: `Lustre_YYYYMMDD.NN_pXX` or `latest`

`optional string target_version = 34 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetVersion.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. Unique ID of the resource. This is unrelated to the access rules which allow specifying the root squash uid.

` string uid = 19 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. Unique ID of the resource. This is unrelated to the access rules which allow specifying the root squash uid.

` string uid = 19 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpcomingMaintenanceSchedule()
    
    
    public abstract MaintenanceSchedule getUpcomingMaintenanceSchedule()

Output only. Date and time of upcoming maintenance for the instance, if a maintenance policy is set.

` .google.cloud.lustre.v1.MaintenanceSchedule upcoming_maintenance_schedule = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.MaintenanceSchedule)` | The upcomingMaintenanceSchedule.  
  
### getUpcomingMaintenanceScheduleOrBuilder()
    
    
    public abstract MaintenanceScheduleOrBuilder getUpcomingMaintenanceScheduleOrBuilder()

Output only. Date and time of upcoming maintenance for the instance, if a maintenance policy is set.

` .google.cloud.lustre.v1.MaintenanceSchedule upcoming_maintenance_schedule = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.MaintenanceScheduleOrBuilder)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Timestamp when the instance was last updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp when the instance was last updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAccessRulesOptions()
    
    
    public abstract boolean hasAccessRulesOptions()

Optional. The access rules options for the instance.

` .google.cloud.lustre.v1.AccessRulesOptions access_rules_options = 18 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessRulesOptions field is set.  
  
### hasAvailableVersion()
    
    
    public abstract boolean hasAvailableVersion()

Output only. The available version that this instance can be upgraded to. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string available_version = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availableVersion field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Timestamp when the instance was created.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDynamicTierOptions()
    
    
    public abstract boolean hasDynamicTierOptions()

Optional. Immutable. Specifies whether the instance is on the Dynamic tier. See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for more information.

` .google.cloud.lustre.v1.DynamicTierOptions dynamic_tier_options = 24 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dynamicTierOptions field is set.  
  
### hasEffectiveVersion()
    
    
    public abstract boolean hasEffectiveVersion()

Output only. The effective version of the instance. Format: `Lustre_YYYYMMDD.NN_pXX`

`optional string effective_version = 35 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the effectiveVersion field is set.  
  
### hasMaintenancePolicy()
    
    
    public abstract boolean hasMaintenancePolicy()

Optional. The maintenance policy for the instance to determine when to allow or exclude the instance from maintenance updates.

` .google.cloud.lustre.v1.MaintenancePolicy maintenance_policy = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenancePolicy field is set.  
  
### hasTargetVersion()
    
    
    public abstract boolean hasTargetVersion()

Optional. The target version of the instance. Setting this field triggers a self-service update to the specified version. Format: `Lustre_YYYYMMDD.NN_pXX` or `latest`

`optional string target_version = 34 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetVersion field is set.  
  
### hasUpcomingMaintenanceSchedule()
    
    
    public abstract boolean hasUpcomingMaintenanceSchedule()

Output only. Date and time of upcoming maintenance for the instance, if a maintenance policy is set.

` .google.cloud.lustre.v1.MaintenanceSchedule upcoming_maintenance_schedule = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the upcomingMaintenanceSchedule field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Timestamp when the instance was last updated.

`.google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
