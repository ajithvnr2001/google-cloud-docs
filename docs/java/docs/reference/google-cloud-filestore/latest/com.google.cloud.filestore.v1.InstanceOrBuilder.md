---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.InstanceOrBuilder
title: Interface InstanceOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:58.566323+00:00
---

# Interface InstanceOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.InstanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InstanceOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.2.0 
    
    
    public interface InstanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Resource labels to represent user provided metadata.

`map<string, string> labels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsTags(String key)
    
    
    public abstract boolean containsTags(String key)

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



` map<string, string> tags = 20 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the instance was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the instance was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCustomPerformanceSupported()
    
    
    public abstract boolean getCustomPerformanceSupported()

Output only. Indicates whether this instance supports configuring its performance. If true, the user can configure the instance's performance by using the 'performance_config' field.

`bool custom_performance_supported = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The customPerformanceSupported.  
  
### getDeletionProtectionEnabled()
    
    
    public abstract boolean getDeletionProtectionEnabled()

Optional. Indicates whether the instance is protected against deletion.

`bool deletion_protection_enabled = 26 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deletionProtectionEnabled.  
  
### getDeletionProtectionReason()
    
    
    public abstract String getDeletionProtectionReason()

Optional. The reason for enabling deletion protection.

`string deletion_protection_reason = 27 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deletionProtectionReason.  
  
### getDeletionProtectionReasonBytes()
    
    
    public abstract ByteString getDeletionProtectionReasonBytes()

Optional. The reason for enabling deletion protection.

`string deletion_protection_reason = 27 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for deletionProtectionReason.  
  
### getDescription()
    
    
    public abstract String getDescription()

The description of the instance (2048 characters or less).

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

The description of the instance (2048 characters or less).

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEtag()
    
    
    public abstract String getEtag()

Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.

`string etag = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.

`string etag = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getFileShares(int index)
    
    
    public abstract FileShareConfig getFileShares(int index)

File system shares on the instance. For this version, only a single file share is supported.

`repeated .google.cloud.filestore.v1.FileShareConfig file_shares = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FileShareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.FileShareConfig)` |   
  
### getFileSharesCount()
    
    
    public abstract int getFileSharesCount()

File system shares on the instance. For this version, only a single file share is supported.

`repeated .google.cloud.filestore.v1.FileShareConfig file_shares = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFileSharesList()
    
    
    public abstract List<FileShareConfig> getFileSharesList()

File system shares on the instance. For this version, only a single file share is supported.

`repeated .google.cloud.filestore.v1.FileShareConfig file_shares = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FileShareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.FileShareConfig)>` |   
  
### getFileSharesOrBuilder(int index)
    
    
    public abstract FileShareConfigOrBuilder getFileSharesOrBuilder(int index)

File system shares on the instance. For this version, only a single file share is supported.

`repeated .google.cloud.filestore.v1.FileShareConfig file_shares = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FileShareConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.FileShareConfigOrBuilder)` |   
  
### getFileSharesOrBuilderList()
    
    
    public abstract List<? extends FileShareConfigOrBuilder> getFileSharesOrBuilderList()

File system shares on the instance. For this version, only a single file share is supported.

`repeated .google.cloud.filestore.v1.FileShareConfig file_shares = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.filestore.v1.FileShareConfigOrBuilder>` |   
  
### getKmsKeyName()
    
    
    public abstract String getKmsKeyName()

KMS key name used for data encryption.

`string kms_key_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyName.  
  
### getKmsKeyNameBytes()
    
    
    public abstract ByteString getKmsKeyNameBytes()

KMS key name used for data encryption.

`string kms_key_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyName.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.InstanceOrBuilder#com_google_cloud_filestore_v1_InstanceOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Resource labels to represent user provided metadata.

`map<string, string> labels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Resource labels to represent user provided metadata.

`map<string, string> labels = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Resource labels to represent user provided metadata.

`map<string, string> labels = 9;`

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

Resource labels to represent user provided metadata.

`map<string, string> labels = 9;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The resource name of the instance, in the format `projects/{project}/locations/{location}/instances/{instance}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The resource name of the instance, in the format `projects/{project}/locations/{location}/instances/{instance}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetworks(int index)
    
    
    public abstract NetworkConfig getNetworks(int index)

VPC networks to which the instance is connected. For this version, only a single network is supported.

`repeated .google.cloud.filestore.v1.NetworkConfig networks = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.NetworkConfig)` |   
  
### getNetworksCount()
    
    
    public abstract int getNetworksCount()

VPC networks to which the instance is connected. For this version, only a single network is supported.

`repeated .google.cloud.filestore.v1.NetworkConfig networks = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNetworksList()
    
    
    public abstract List<NetworkConfig> getNetworksList()

VPC networks to which the instance is connected. For this version, only a single network is supported.

`repeated .google.cloud.filestore.v1.NetworkConfig networks = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.NetworkConfig)>` |   
  
### getNetworksOrBuilder(int index)
    
    
    public abstract NetworkConfigOrBuilder getNetworksOrBuilder(int index)

VPC networks to which the instance is connected. For this version, only a single network is supported.

`repeated .google.cloud.filestore.v1.NetworkConfig networks = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.NetworkConfigOrBuilder)` |   
  
### getNetworksOrBuilderList()
    
    
    public abstract List<? extends NetworkConfigOrBuilder> getNetworksOrBuilderList()

VPC networks to which the instance is connected. For this version, only a single network is supported.

`repeated .google.cloud.filestore.v1.NetworkConfig networks = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.filestore.v1.NetworkConfigOrBuilder>` |   
  
### getPerformanceConfig()
    
    
    public abstract Instance.PerformanceConfig getPerformanceConfig()

Optional. Used to configure performance.

` .google.cloud.filestore.v1.Instance.PerformanceConfig performance_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.PerformanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceConfig)` | The performanceConfig.  
  
### getPerformanceConfigOrBuilder()
    
    
    public abstract Instance.PerformanceConfigOrBuilder getPerformanceConfigOrBuilder()

Optional. Used to configure performance.

` .google.cloud.filestore.v1.Instance.PerformanceConfig performance_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.PerformanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceConfigOrBuilder)` |   
  
### getPerformanceLimits()
    
    
    public abstract Instance.PerformanceLimits getPerformanceLimits()

Output only. Used for getting performance limits.

` .google.cloud.filestore.v1.Instance.PerformanceLimits performance_limits = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.PerformanceLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceLimits)` | The performanceLimits.  
  
### getPerformanceLimitsOrBuilder()
    
    
    public abstract Instance.PerformanceLimitsOrBuilder getPerformanceLimitsOrBuilder()

Output only. Used for getting performance limits.

` .google.cloud.filestore.v1.Instance.PerformanceLimits performance_limits = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.PerformanceLimitsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceLimitsOrBuilder)` |   
  
### getProtocol()
    
    
    public abstract Instance.FileProtocol getProtocol()

Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: `NFS_V3`.

` .google.cloud.filestore.v1.Instance.FileProtocol protocol = 21 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.FileProtocol](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.FileProtocol)` | The protocol.  
  
### getProtocolValue()
    
    
    public abstract int getProtocolValue()

Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: `NFS_V3`.

` .google.cloud.filestore.v1.Instance.FileProtocol protocol = 21 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for protocol.  
  
### getReplication()
    
    
    public abstract Replication getReplication()

Optional. Replication configuration.

` .google.cloud.filestore.v1.Replication replication = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Replication)` | The replication.  
  
### getReplicationOrBuilder()
    
    
    public abstract ReplicationOrBuilder getReplicationOrBuilder()

Optional. Replication configuration.

` .google.cloud.filestore.v1.Replication replication = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReplicationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.ReplicationOrBuilder)` |   
  
### getSatisfiesPzi()
    
    
    public abstract boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 18 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public abstract BoolValue getSatisfiesPzs()

Output only. Reserved for future use.

` .google.protobuf.BoolValue satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The satisfiesPzs.  
  
### getSatisfiesPzsOrBuilder()
    
    
    public abstract BoolValueOrBuilder getSatisfiesPzsOrBuilder()

Output only. Reserved for future use.

` .google.protobuf.BoolValue satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getState()
    
    
    public abstract Instance.State getState()

Output only. The instance state.

` .google.cloud.filestore.v1.Instance.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Instance.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The instance state.

` .google.cloud.filestore.v1.Instance.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStatusMessage()
    
    
    public abstract String getStatusMessage()

Output only. Additional information about the instance state, if available.

`string status_message = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The statusMessage.  
  
### getStatusMessageBytes()
    
    
    public abstract ByteString getStatusMessageBytes()

Output only. Additional information about the instance state, if available.

`string status_message = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for statusMessage.  
  
### getSuspensionReasons(int index)
    
    
    public abstract Instance.SuspensionReason getSuspensionReasons(int index)

Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.

` repeated .google.cloud.filestore.v1.Instance.SuspensionReason suspension_reasons = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Instance.SuspensionReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.SuspensionReason)` | The suspensionReasons at the given index.  
  
### getSuspensionReasonsCount()
    
    
    public abstract int getSuspensionReasonsCount()

Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.

` repeated .google.cloud.filestore.v1.Instance.SuspensionReason suspension_reasons = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of suspensionReasons.  
  
### getSuspensionReasonsList()
    
    
    public abstract List<Instance.SuspensionReason> getSuspensionReasonsList()

Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.

` repeated .google.cloud.filestore.v1.Instance.SuspensionReason suspension_reasons = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SuspensionReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.SuspensionReason)>` | A list containing the suspensionReasons.  
  
### getSuspensionReasonsValue(int index)
    
    
    public abstract int getSuspensionReasonsValue(int index)

Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.

` repeated .google.cloud.filestore.v1.Instance.SuspensionReason suspension_reasons = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of suspensionReasons at the given index.  
  
### getSuspensionReasonsValueList()
    
    
    public abstract List<Integer> getSuspensionReasonsValueList()

Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.

` repeated .google.cloud.filestore.v1.Instance.SuspensionReason suspension_reasons = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for suspensionReasons.  
  
### getTags() (deprecated)
    
    
    public abstract Map<String,String> getTags()

Use [#getTagsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.InstanceOrBuilder#com_google_cloud_filestore_v1_InstanceOrBuilder_getTagsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



` map<string, string> tags = 20 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTagsMap()
    
    
    public abstract Map<String,String> getTagsMap()

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



` map<string, string> tags = 20 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsOrDefault(String key, String defaultValue)
    
    
    public abstract String getTagsOrDefault(String key, String defaultValue)

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



` map<string, string> tags = 20 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTagsOrThrow(String key)
    
    
    public abstract String getTagsOrThrow(String key)

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



` map<string, string> tags = 20 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTier()
    
    
    public abstract Instance.Tier getTier()

The service tier of the instance.

`.google.cloud.filestore.v1.Instance.Tier tier = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Instance.Tier](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.Tier)` | The tier.  
  
### getTierValue()
    
    
    public abstract int getTierValue()

The service tier of the instance.

`.google.cloud.filestore.v1.Instance.Tier tier = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for tier.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the instance was created.

`.google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasPerformanceConfig()
    
    
    public abstract boolean hasPerformanceConfig()

Optional. Used to configure performance.

` .google.cloud.filestore.v1.Instance.PerformanceConfig performance_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the performanceConfig field is set.  
  
### hasPerformanceLimits()
    
    
    public abstract boolean hasPerformanceLimits()

Output only. Used for getting performance limits.

` .google.cloud.filestore.v1.Instance.PerformanceLimits performance_limits = 25 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the performanceLimits field is set.  
  
### hasReplication()
    
    
    public abstract boolean hasReplication()

Optional. Replication configuration.

` .google.cloud.filestore.v1.Replication replication = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the replication field is set.  
  
### hasSatisfiesPzs()
    
    
    public abstract boolean hasSatisfiesPzs()

Output only. Reserved for future use.

` .google.protobuf.BoolValue satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzs field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
