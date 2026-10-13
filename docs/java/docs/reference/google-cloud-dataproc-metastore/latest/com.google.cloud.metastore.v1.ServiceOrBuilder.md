---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ServiceOrBuilder
title: Interface ServiceOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:47.594837+00:00
---

# Interface ServiceOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ServiceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServiceOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.4  2.3.0  2.2.0  2.1.9 
    
    
    public interface ServiceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

User-defined labels for the metastore service.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getArtifactGcsUri()
    
    
    public abstract String getArtifactGcsUri()

Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.

`string artifact_gcs_uri = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The artifactGcsUri.  
  
### getArtifactGcsUriBytes()
    
    
    public abstract ByteString getArtifactGcsUriBytes()

Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.

`string artifact_gcs_uri = 12 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for artifactGcsUri.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the metastore service was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the metastore service was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDatabaseType()
    
    
    public abstract Service.DatabaseType getDatabaseType()

Immutable. The database type that the Metastore service stores its data.

` .google.cloud.metastore.v1.Service.DatabaseType database_type = 22 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Service.DatabaseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service.DatabaseType)` | The databaseType.  
  
### getDatabaseTypeValue()
    
    
    public abstract int getDatabaseTypeValue()

Immutable. The database type that the Metastore service stores its data.

` .google.cloud.metastore.v1.Service.DatabaseType database_type = 22 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for databaseType.  
  
### getEncryptionConfig()
    
    
    public abstract EncryptionConfig getEncryptionConfig()

Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.

` .google.cloud.metastore.v1.EncryptionConfig encryption_config = 20 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.EncryptionConfig)` | The encryptionConfig.  
  
### getEncryptionConfigOrBuilder()
    
    
    public abstract EncryptionConfigOrBuilder getEncryptionConfigOrBuilder()

Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.

` .google.cloud.metastore.v1.EncryptionConfig encryption_config = 20 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.EncryptionConfigOrBuilder)` |   
  
### getEndpointUri()
    
    
    public abstract String getEndpointUri()

Output only. The URI of the endpoint used to access the metastore service.

`string endpoint_uri = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpointUri.  
  
### getEndpointUriBytes()
    
    
    public abstract ByteString getEndpointUriBytes()

Output only. The URI of the endpoint used to access the metastore service.

`string endpoint_uri = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpointUri.  
  
### getHiveMetastoreConfig()
    
    
    public abstract HiveMetastoreConfig getHiveMetastoreConfig()

Configuration information specific to running Hive metastore software as the metastore service.

`.google.cloud.metastore.v1.HiveMetastoreConfig hive_metastore_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.HiveMetastoreConfig)` | The hiveMetastoreConfig.  
  
### getHiveMetastoreConfigOrBuilder()
    
    
    public abstract HiveMetastoreConfigOrBuilder getHiveMetastoreConfigOrBuilder()

Configuration information specific to running Hive metastore software as the metastore service.

`.google.cloud.metastore.v1.HiveMetastoreConfig hive_metastore_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.HiveMetastoreConfigOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ServiceOrBuilder#com_google_cloud_metastore_v1_ServiceOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

User-defined labels for the metastore service.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

User-defined labels for the metastore service.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

User-defined labels for the metastore service.

`map<string, string> labels = 4;`

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

User-defined labels for the metastore service.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaintenanceWindow()
    
    
    public abstract MaintenanceWindow getMaintenanceWindow()

The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.

`.google.cloud.metastore.v1.MaintenanceWindow maintenance_window = 15;`

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MaintenanceWindow)` | The maintenanceWindow.  
  
### getMaintenanceWindowOrBuilder()
    
    
    public abstract MaintenanceWindowOrBuilder getMaintenanceWindowOrBuilder()

The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.

`.google.cloud.metastore.v1.MaintenanceWindow maintenance_window = 15;`

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MaintenanceWindowOrBuilder)` |   
  
### getMetadataManagementActivity()
    
    
    public abstract MetadataManagementActivity getMetadataManagementActivity()

Output only. The metadata management activities of the metastore service.

` .google.cloud.metastore.v1.MetadataManagementActivity metadata_management_activity = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MetadataManagementActivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataManagementActivity)` | The metadataManagementActivity.  
  
### getMetadataManagementActivityOrBuilder()
    
    
    public abstract MetadataManagementActivityOrBuilder getMetadataManagementActivityOrBuilder()

Output only. The metadata management activities of the metastore service.

` .google.cloud.metastore.v1.MetadataManagementActivity metadata_management_activity = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MetadataManagementActivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataManagementActivityOrBuilder)` |   
  
### getMetastoreConfigCase()
    
    
    public abstract Service.MetastoreConfigCase getMetastoreConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[Service.MetastoreConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service.MetastoreConfigCase)` |   
  
### getName()
    
    
    public abstract String getName()

Immutable. The relative resource name of the metastore service, in the following format:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. The relative resource name of the metastore service, in the following format:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:

`projects/{project_number}/global/networks/{network_id}`.

` string network = 7 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:

`projects/{project_number}/global/networks/{network_id}`.

` string network = 7 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkConfig()
    
    
    public abstract NetworkConfig getNetworkConfig()

The configuration specifying the network settings for the Dataproc Metastore service.

`.google.cloud.metastore.v1.NetworkConfig network_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.NetworkConfig)` | The networkConfig.  
  
### getNetworkConfigOrBuilder()
    
    
    public abstract NetworkConfigOrBuilder getNetworkConfigOrBuilder()

The configuration specifying the network settings for the Dataproc Metastore service.

`.google.cloud.metastore.v1.NetworkConfig network_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.NetworkConfigOrBuilder)` |   
  
### getPort()
    
    
    public abstract int getPort()

The TCP port at which the metastore service is reached. Default: 9083.

`int32 port = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The port.  
  
### getReleaseChannel()
    
    
    public abstract Service.ReleaseChannel getReleaseChannel()

Immutable. The release channel of the service. If unspecified, defaults to `STABLE`.

` .google.cloud.metastore.v1.Service.ReleaseChannel release_channel = 19 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[Service.ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service.ReleaseChannel)` | The releaseChannel.  
  
### getReleaseChannelValue()
    
    
    public abstract int getReleaseChannelValue()

Immutable. The release channel of the service. If unspecified, defaults to `STABLE`.

` .google.cloud.metastore.v1.Service.ReleaseChannel release_channel = 19 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for releaseChannel.  
  
### getScalingConfig()
    
    
    public abstract ScalingConfig getScalingConfig()

Scaling configuration of the metastore service.

`.google.cloud.metastore.v1.ScalingConfig scaling_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[ScalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ScalingConfig)` | The scalingConfig.  
  
### getScalingConfigOrBuilder()
    
    
    public abstract ScalingConfigOrBuilder getScalingConfigOrBuilder()

Scaling configuration of the metastore service.

`.google.cloud.metastore.v1.ScalingConfig scaling_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[ScalingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ScalingConfigOrBuilder)` |   
  
### getState()
    
    
    public abstract Service.State getState()

Output only. The current state of the metastore service.

` .google.cloud.metastore.v1.Service.State state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Service.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service.State)` | The state.  
  
### getStateMessage()
    
    
    public abstract String getStateMessage()

Output only. Additional information about the current state of the metastore service, if available.

`string state_message = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateMessage.  
  
### getStateMessageBytes()
    
    
    public abstract ByteString getStateMessageBytes()

Output only. Additional information about the current state of the metastore service, if available.

`string state_message = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateMessage.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of the metastore service.

` .google.cloud.metastore.v1.Service.State state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTelemetryConfig()
    
    
    public abstract TelemetryConfig getTelemetryConfig()

The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.

`.google.cloud.metastore.v1.TelemetryConfig telemetry_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[TelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.TelemetryConfig)` | The telemetryConfig.  
  
### getTelemetryConfigOrBuilder()
    
    
    public abstract TelemetryConfigOrBuilder getTelemetryConfigOrBuilder()

The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.

`.google.cloud.metastore.v1.TelemetryConfig telemetry_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[TelemetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.TelemetryConfigOrBuilder)` |   
  
### getTier()
    
    
    public abstract Service.Tier getTier()

The tier of the service.

`.google.cloud.metastore.v1.Service.Tier tier = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Service.Tier](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service.Tier)` | The tier.  
  
### getTierValue()
    
    
    public abstract int getTierValue()

The tier of the service.

`.google.cloud.metastore.v1.Service.Tier tier = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for tier.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. The globally unique resource identifier of the metastore service.

`string uid = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. The globally unique resource identifier of the metastore service.

`string uid = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time when the metastore service was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time when the metastore service was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the metastore service was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionConfig()
    
    
    public abstract boolean hasEncryptionConfig()

Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.

` .google.cloud.metastore.v1.EncryptionConfig encryption_config = 20 [(.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionConfig field is set.  
  
### hasHiveMetastoreConfig()
    
    
    public abstract boolean hasHiveMetastoreConfig()

Configuration information specific to running Hive metastore software as the metastore service.

`.google.cloud.metastore.v1.HiveMetastoreConfig hive_metastore_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hiveMetastoreConfig field is set.  
  
### hasMaintenanceWindow()
    
    
    public abstract boolean hasMaintenanceWindow()

The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.

`.google.cloud.metastore.v1.MaintenanceWindow maintenance_window = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceWindow field is set.  
  
### hasMetadataManagementActivity()
    
    
    public abstract boolean hasMetadataManagementActivity()

Output only. The metadata management activities of the metastore service.

` .google.cloud.metastore.v1.MetadataManagementActivity metadata_management_activity = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadataManagementActivity field is set.  
  
### hasNetworkConfig()
    
    
    public abstract boolean hasNetworkConfig()

The configuration specifying the network settings for the Dataproc Metastore service.

`.google.cloud.metastore.v1.NetworkConfig network_config = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkConfig field is set.  
  
### hasScalingConfig()
    
    
    public abstract boolean hasScalingConfig()

Scaling configuration of the metastore service.

`.google.cloud.metastore.v1.ScalingConfig scaling_config = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scalingConfig field is set.  
  
### hasTelemetryConfig()
    
    
    public abstract boolean hasTelemetryConfig()

The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.

`.google.cloud.metastore.v1.TelemetryConfig telemetry_config = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the telemetryConfig field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time when the metastore service was last updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
