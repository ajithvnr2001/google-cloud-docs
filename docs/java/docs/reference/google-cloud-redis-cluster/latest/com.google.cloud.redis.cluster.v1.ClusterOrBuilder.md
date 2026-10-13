---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterOrBuilder
title: Interface ClusterOrBuilder (0.71.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:57.419863+00:00
---

# Interface ClusterOrBuilder (0.71.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterOrBuilder (0.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.71.0 (latest)  0.67.0  0.66.0  0.65.0  0.63.0  0.60.0  0.59.0  0.57.0  0.55.0  0.54.0  0.52.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ClusterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsRedisConfigs(String key)
    
    
    public abstract boolean containsRedisConfigs(String key)

Optional. Key/Value pairs of customer overrides for mutable Redis Configs

`map<string, string> redis_configs = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAsyncClusterEndpointsDeletionEnabled()
    
    
    public abstract boolean getAsyncClusterEndpointsDeletionEnabled()

Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted.

` optional bool async_cluster_endpoints_deletion_enabled = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The asyncClusterEndpointsDeletionEnabled.  
  
### getAuthorizationMode()
    
    
    public abstract AuthorizationMode getAuthorizationMode()

Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.

` .google.cloud.redis.cluster.v1.AuthorizationMode authorization_mode = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AuthorizationMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.AuthorizationMode)` | The authorizationMode.  
  
### getAuthorizationModeValue()
    
    
    public abstract int getAuthorizationModeValue()

Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.

` .google.cloud.redis.cluster.v1.AuthorizationMode authorization_mode = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authorizationMode.  
  
### getAutomatedBackupConfig()
    
    
    public abstract AutomatedBackupConfig getAutomatedBackupConfig()

Optional. The automated backup config for the cluster.

` .google.cloud.redis.cluster.v1.AutomatedBackupConfig automated_backup_config = 42 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.AutomatedBackupConfig)` | The automatedBackupConfig.  
  
### getAutomatedBackupConfigOrBuilder()
    
    
    public abstract AutomatedBackupConfigOrBuilder getAutomatedBackupConfigOrBuilder()

Optional. The automated backup config for the cluster.

` .google.cloud.redis.cluster.v1.AutomatedBackupConfig automated_backup_config = 42 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.AutomatedBackupConfigOrBuilder)` |   
  
### getBackupCollection()
    
    
    public abstract String getBackupCollection()

Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}

` optional string backup_collection = 39 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backupCollection.  
  
### getBackupCollectionBytes()
    
    
    public abstract ByteString getBackupCollectionBytes()

Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}

` optional string backup_collection = 39 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backupCollection.  
  
### getClusterEndpoints(int index)
    
    
    public abstract ClusterEndpoint getClusterEndpoints(int index)

Optional. A list of cluster enpoints.

` repeated .google.cloud.redis.cluster.v1.ClusterEndpoint cluster_endpoints = 36 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterEndpoint)` |   
  
### getClusterEndpointsCount()
    
    
    public abstract int getClusterEndpointsCount()

Optional. A list of cluster enpoints.

` repeated .google.cloud.redis.cluster.v1.ClusterEndpoint cluster_endpoints = 36 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getClusterEndpointsList()
    
    
    public abstract List<ClusterEndpoint> getClusterEndpointsList()

Optional. A list of cluster enpoints.

` repeated .google.cloud.redis.cluster.v1.ClusterEndpoint cluster_endpoints = 36 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ClusterEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterEndpoint)>` |   
  
### getClusterEndpointsOrBuilder(int index)
    
    
    public abstract ClusterEndpointOrBuilder getClusterEndpointsOrBuilder(int index)

Optional. A list of cluster enpoints.

` repeated .google.cloud.redis.cluster.v1.ClusterEndpoint cluster_endpoints = 36 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterEndpointOrBuilder)` |   
  
### getClusterEndpointsOrBuilderList()
    
    
    public abstract List<? extends ClusterEndpointOrBuilder> getClusterEndpointsOrBuilderList()

Optional. A list of cluster enpoints.

` repeated .google.cloud.redis.cluster.v1.ClusterEndpoint cluster_endpoints = 36 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.redis.cluster.v1.ClusterEndpointOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp associated with the cluster creation request.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp associated with the cluster creation request.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCrossClusterReplicationConfig()
    
    
    public abstract CrossClusterReplicationConfig getCrossClusterReplicationConfig()

Optional. Cross cluster replication config.

` .google.cloud.redis.cluster.v1.CrossClusterReplicationConfig cross_cluster_replication_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.CrossClusterReplicationConfig)` | The crossClusterReplicationConfig.  
  
### getCrossClusterReplicationConfigOrBuilder()
    
    
    public abstract CrossClusterReplicationConfigOrBuilder getCrossClusterReplicationConfigOrBuilder()

Optional. Cross cluster replication config.

` .google.cloud.redis.cluster.v1.CrossClusterReplicationConfig cross_cluster_replication_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.CrossClusterReplicationConfigOrBuilder)` |   
  
### getDeletionProtectionEnabled()
    
    
    public abstract boolean getDeletionProtectionEnabled()

Optional. The delete operation will fail when the value is set to true.

`optional bool deletion_protection_enabled = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deletionProtectionEnabled.  
  
### getDiscoveryEndpoints(int index)
    
    
    public abstract DiscoveryEndpoint getDiscoveryEndpoints(int index)

Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.

` repeated .google.cloud.redis.cluster.v1.DiscoveryEndpoint discovery_endpoints = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.DiscoveryEndpoint)` |   
  
### getDiscoveryEndpointsCount()
    
    
    public abstract int getDiscoveryEndpointsCount()

Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.

` repeated .google.cloud.redis.cluster.v1.DiscoveryEndpoint discovery_endpoints = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDiscoveryEndpointsList()
    
    
    public abstract List<DiscoveryEndpoint> getDiscoveryEndpointsList()

Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.

` repeated .google.cloud.redis.cluster.v1.DiscoveryEndpoint discovery_endpoints = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DiscoveryEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.DiscoveryEndpoint)>` |   
  
### getDiscoveryEndpointsOrBuilder(int index)
    
    
    public abstract DiscoveryEndpointOrBuilder getDiscoveryEndpointsOrBuilder(int index)

Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.

` repeated .google.cloud.redis.cluster.v1.DiscoveryEndpoint discovery_endpoints = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveryEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.DiscoveryEndpointOrBuilder)` |   
  
### getDiscoveryEndpointsOrBuilderList()
    
    
    public abstract List<? extends DiscoveryEndpointOrBuilder> getDiscoveryEndpointsOrBuilderList()

Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.

` repeated .google.cloud.redis.cluster.v1.DiscoveryEndpoint discovery_endpoints = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.redis.cluster.v1.DiscoveryEndpointOrBuilder>` |   
  
### getEncryptionInfo()
    
    
    public abstract EncryptionInfo getEncryptionInfo()

Output only. Encryption information of the data at rest of the cluster.

` .google.cloud.redis.cluster.v1.EncryptionInfo encryption_info = 43 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.EncryptionInfo)` | The encryptionInfo.  
  
### getEncryptionInfoOrBuilder()
    
    
    public abstract EncryptionInfoOrBuilder getEncryptionInfoOrBuilder()

Output only. Encryption information of the data at rest of the cluster.

` .google.cloud.redis.cluster.v1.EncryptionInfo encryption_info = 43 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.EncryptionInfoOrBuilder)` |   
  
### getGcsSource()
    
    
    public abstract Cluster.GcsBackupSource getGcsSource()

Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.

` .google.cloud.redis.cluster.v1.Cluster.GcsBackupSource gcs_source = 34 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.GcsBackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.GcsBackupSource)` | The gcsSource.  
  
### getGcsSourceOrBuilder()
    
    
    public abstract Cluster.GcsBackupSourceOrBuilder getGcsSourceOrBuilder()

Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.

` .google.cloud.redis.cluster.v1.Cluster.GcsBackupSource gcs_source = 34 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.GcsBackupSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.GcsBackupSourceOrBuilder)` |   
  
### getImportSourcesCase()
    
    
    public abstract Cluster.ImportSourcesCase getImportSourcesCase()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.ImportSourcesCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.ImportSourcesCase)` |   
  
### getKmsKey()
    
    
    public abstract String getKmsKey()

Optional. The KMS key used to encrypt the at-rest data of the cluster.

` optional string kms_key = 40 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKey.  
  
### getKmsKeyBytes()
    
    
    public abstract ByteString getKmsKeyBytes()

Optional. The KMS key used to encrypt the at-rest data of the cluster.

` optional string kms_key = 40 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKey.  
  
### getMaintenancePolicy()
    
    
    public abstract ClusterMaintenancePolicy getMaintenancePolicy()

Optional. ClusterMaintenancePolicy determines when to allow or deny updates.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenancePolicy maintenance_policy = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterMaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterMaintenancePolicy)` | The maintenancePolicy.  
  
### getMaintenancePolicyOrBuilder()
    
    
    public abstract ClusterMaintenancePolicyOrBuilder getMaintenancePolicyOrBuilder()

Optional. ClusterMaintenancePolicy determines when to allow or deny updates.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenancePolicy maintenance_policy = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterMaintenancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterMaintenancePolicyOrBuilder)` |   
  
### getMaintenanceSchedule()
    
    
    public abstract ClusterMaintenanceSchedule getMaintenanceSchedule()

Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenanceSchedule maintenance_schedule = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterMaintenanceSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterMaintenanceSchedule)` | The maintenanceSchedule.  
  
### getMaintenanceScheduleOrBuilder()
    
    
    public abstract ClusterMaintenanceScheduleOrBuilder getMaintenanceScheduleOrBuilder()

Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenanceSchedule maintenance_schedule = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterMaintenanceScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterMaintenanceScheduleOrBuilder)` |   
  
### getManagedBackupSource()
    
    
    public abstract Cluster.ManagedBackupSource getManagedBackupSource()

Optional. Backups generated and managed by memorystore service.

` .google.cloud.redis.cluster.v1.Cluster.ManagedBackupSource managed_backup_source = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.ManagedBackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.ManagedBackupSource)` | The managedBackupSource.  
  
### getManagedBackupSourceOrBuilder()
    
    
    public abstract Cluster.ManagedBackupSourceOrBuilder getManagedBackupSourceOrBuilder()

Optional. Backups generated and managed by memorystore service.

` .google.cloud.redis.cluster.v1.Cluster.ManagedBackupSource managed_backup_source = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.ManagedBackupSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.ManagedBackupSourceOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNodeType()
    
    
    public abstract NodeType getNodeType()

Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.

` .google.cloud.redis.cluster.v1.NodeType node_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.NodeType)` | The nodeType.  
  
### getNodeTypeValue()
    
    
    public abstract int getNodeTypeValue()

Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.

` .google.cloud.redis.cluster.v1.NodeType node_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for nodeType.  
  
### getPersistenceConfig()
    
    
    public abstract ClusterPersistenceConfig getPersistenceConfig()

Optional. Persistence config (RDB, AOF) for the cluster.

` .google.cloud.redis.cluster.v1.ClusterPersistenceConfig persistence_config = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPersistenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterPersistenceConfig)` | The persistenceConfig.  
  
### getPersistenceConfigOrBuilder()
    
    
    public abstract ClusterPersistenceConfigOrBuilder getPersistenceConfigOrBuilder()

Optional. Persistence config (RDB, AOF) for the cluster.

` .google.cloud.redis.cluster.v1.ClusterPersistenceConfig persistence_config = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPersistenceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterPersistenceConfigOrBuilder)` |   
  
### getPreciseSizeGb()
    
    
    public abstract double getPreciseSizeGb()

Output only. Precise value of redis memory size in GB for the entire cluster.

`optional double precise_size_gb = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preciseSizeGb.  
  
### getPscConfigs(int index)
    
    
    public abstract PscConfig getPscConfigs(int index)

Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.

` repeated .google.cloud.redis.cluster.v1.PscConfig psc_configs = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConfig)` |   
  
### getPscConfigsCount()
    
    
    public abstract int getPscConfigsCount()

Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.

` repeated .google.cloud.redis.cluster.v1.PscConfig psc_configs = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPscConfigsList()
    
    
    public abstract List<PscConfig> getPscConfigsList()

Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.

` repeated .google.cloud.redis.cluster.v1.PscConfig psc_configs = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PscConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConfig)>` |   
  
### getPscConfigsOrBuilder(int index)
    
    
    public abstract PscConfigOrBuilder getPscConfigsOrBuilder(int index)

Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.

` repeated .google.cloud.redis.cluster.v1.PscConfig psc_configs = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConfigOrBuilder)` |   
  
### getPscConfigsOrBuilderList()
    
    
    public abstract List<? extends PscConfigOrBuilder> getPscConfigsOrBuilderList()

Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.

` repeated .google.cloud.redis.cluster.v1.PscConfig psc_configs = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.redis.cluster.v1.PscConfigOrBuilder>` |   
  
### getPscConnections(int index)
    
    
    public abstract PscConnection getPscConnections(int index)

Output only. The list of PSC connections that are auto-created through service connectivity automation.

` repeated .google.cloud.redis.cluster.v1.PscConnection psc_connections = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConnection)` |   
  
### getPscConnectionsCount()
    
    
    public abstract int getPscConnectionsCount()

Output only. The list of PSC connections that are auto-created through service connectivity automation.

` repeated .google.cloud.redis.cluster.v1.PscConnection psc_connections = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPscConnectionsList()
    
    
    public abstract List<PscConnection> getPscConnectionsList()

Output only. The list of PSC connections that are auto-created through service connectivity automation.

` repeated .google.cloud.redis.cluster.v1.PscConnection psc_connections = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PscConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConnection)>` |   
  
### getPscConnectionsOrBuilder(int index)
    
    
    public abstract PscConnectionOrBuilder getPscConnectionsOrBuilder(int index)

Output only. The list of PSC connections that are auto-created through service connectivity automation.

` repeated .google.cloud.redis.cluster.v1.PscConnection psc_connections = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscConnectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscConnectionOrBuilder)` |   
  
### getPscConnectionsOrBuilderList()
    
    
    public abstract List<? extends PscConnectionOrBuilder> getPscConnectionsOrBuilderList()

Output only. The list of PSC connections that are auto-created through service connectivity automation.

` repeated .google.cloud.redis.cluster.v1.PscConnection psc_connections = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.redis.cluster.v1.PscConnectionOrBuilder>` |   
  
### getPscServiceAttachments(int index)
    
    
    public abstract PscServiceAttachment getPscServiceAttachments(int index)

Output only. Service attachment details to configure Psc connections

` repeated .google.cloud.redis.cluster.v1.PscServiceAttachment psc_service_attachments = 30 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscServiceAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscServiceAttachment)` |   
  
### getPscServiceAttachmentsCount()
    
    
    public abstract int getPscServiceAttachmentsCount()

Output only. Service attachment details to configure Psc connections

` repeated .google.cloud.redis.cluster.v1.PscServiceAttachment psc_service_attachments = 30 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPscServiceAttachmentsList()
    
    
    public abstract List<PscServiceAttachment> getPscServiceAttachmentsList()

Output only. Service attachment details to configure Psc connections

` repeated .google.cloud.redis.cluster.v1.PscServiceAttachment psc_service_attachments = 30 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PscServiceAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscServiceAttachment)>` |   
  
### getPscServiceAttachmentsOrBuilder(int index)
    
    
    public abstract PscServiceAttachmentOrBuilder getPscServiceAttachmentsOrBuilder(int index)

Output only. Service attachment details to configure Psc connections

` repeated .google.cloud.redis.cluster.v1.PscServiceAttachment psc_service_attachments = 30 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PscServiceAttachmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.PscServiceAttachmentOrBuilder)` |   
  
### getPscServiceAttachmentsOrBuilderList()
    
    
    public abstract List<? extends PscServiceAttachmentOrBuilder> getPscServiceAttachmentsOrBuilderList()

Output only. Service attachment details to configure Psc connections

` repeated .google.cloud.redis.cluster.v1.PscServiceAttachment psc_service_attachments = 30 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.redis.cluster.v1.PscServiceAttachmentOrBuilder>` |   
  
### getRedisConfigs() (deprecated)
    
    
    public abstract Map<String,String> getRedisConfigs()

Use [#getRedisConfigsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ClusterOrBuilder#com_google_cloud_redis_cluster_v1_ClusterOrBuilder_getRedisConfigsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getRedisConfigsCount()
    
    
    public abstract int getRedisConfigsCount()

Optional. Key/Value pairs of customer overrides for mutable Redis Configs

`map<string, string> redis_configs = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRedisConfigsMap()
    
    
    public abstract Map<String,String> getRedisConfigsMap()

Optional. Key/Value pairs of customer overrides for mutable Redis Configs

`map<string, string> redis_configs = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getRedisConfigsOrDefault(String key, String defaultValue)
    
    
    public abstract String getRedisConfigsOrDefault(String key, String defaultValue)

Optional. Key/Value pairs of customer overrides for mutable Redis Configs

`map<string, string> redis_configs = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRedisConfigsOrThrow(String key)
    
    
    public abstract String getRedisConfigsOrThrow(String key)

Optional. Key/Value pairs of customer overrides for mutable Redis Configs

`map<string, string> redis_configs = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getReplicaCount()
    
    
    public abstract int getReplicaCount()

Optional. The number of replica nodes per shard.

`optional int32 replica_count = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The replicaCount.  
  
### getRotateServerCertificate()
    
    
    public abstract boolean getRotateServerCertificate()

Optional. Input only. Rotate the server certificates.

` optional bool rotate_server_certificate = 55 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rotateServerCertificate.  
  
### getServerCaMode()
    
    
    public abstract ServerCaMode getServerCaMode()

Optional. Server CA mode for the cluster.

` optional .google.cloud.redis.cluster.v1.ServerCaMode server_ca_mode = 53 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ServerCaMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ServerCaMode)` | The serverCaMode.  
  
### getServerCaModeValue()
    
    
    public abstract int getServerCaModeValue()

Optional. Server CA mode for the cluster.

` optional .google.cloud.redis.cluster.v1.ServerCaMode server_ca_mode = 53 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for serverCaMode.  
  
### getServerCaPool()
    
    
    public abstract String getServerCaPool()

Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".

` optional string server_ca_pool = 54 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serverCaPool.  
  
### getServerCaPoolBytes()
    
    
    public abstract ByteString getServerCaPoolBytes()

Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".

` optional string server_ca_pool = 54 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serverCaPool.  
  
### getShardCount()
    
    
    public abstract int getShardCount()

Optional. Number of shards for the Redis cluster.

`optional int32 shard_count = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The shardCount.  
  
### getSizeGb()
    
    
    public abstract int getSizeGb()

Output only. Redis memory size in GB for the entire cluster rounded up to the next integer.

`optional int32 size_gb = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sizeGb.  
  
### getState()
    
    
    public abstract Cluster.State getState()

Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED

` .google.cloud.redis.cluster.v1.Cluster.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.State)` | The state.  
  
### getStateInfo()
    
    
    public abstract Cluster.StateInfo getStateInfo()

Output only. Additional information about the current state of the cluster.

` .google.cloud.redis.cluster.v1.Cluster.StateInfo state_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.StateInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.StateInfo)` | The stateInfo.  
  
### getStateInfoOrBuilder()
    
    
    public abstract Cluster.StateInfoOrBuilder getStateInfoOrBuilder()

Output only. Additional information about the current state of the cluster.

` .google.cloud.redis.cluster.v1.Cluster.StateInfo state_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.StateInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.Cluster.StateInfoOrBuilder)` |   
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED

` .google.cloud.redis.cluster.v1.Cluster.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getTransitEncryptionMode()
    
    
    public abstract TransitEncryptionMode getTransitEncryptionMode()

Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.

` .google.cloud.redis.cluster.v1.TransitEncryptionMode transit_encryption_mode = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TransitEncryptionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.TransitEncryptionMode)` | The transitEncryptionMode.  
  
### getTransitEncryptionModeValue()
    
    
    public abstract int getTransitEncryptionModeValue()

Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.

` .google.cloud.redis.cluster.v1.TransitEncryptionMode transit_encryption_mode = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for transitEncryptionMode.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. System assigned, unique identifier for the cluster.

`string uid = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. System assigned, unique identifier for the cluster.

`string uid = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getZoneDistributionConfig()
    
    
    public abstract ZoneDistributionConfig getZoneDistributionConfig()

Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.

` .google.cloud.redis.cluster.v1.ZoneDistributionConfig zone_distribution_config = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ZoneDistributionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ZoneDistributionConfig)` | The zoneDistributionConfig.  
  
### getZoneDistributionConfigOrBuilder()
    
    
    public abstract ZoneDistributionConfigOrBuilder getZoneDistributionConfigOrBuilder()

Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.

` .google.cloud.redis.cluster.v1.ZoneDistributionConfig zone_distribution_config = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ZoneDistributionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1.ZoneDistributionConfigOrBuilder)` |   
  
### hasAsyncClusterEndpointsDeletionEnabled()
    
    
    public abstract boolean hasAsyncClusterEndpointsDeletionEnabled()

Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted.

` optional bool async_cluster_endpoints_deletion_enabled = 44 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the asyncClusterEndpointsDeletionEnabled field is set.  
  
### hasAutomatedBackupConfig()
    
    
    public abstract boolean hasAutomatedBackupConfig()

Optional. The automated backup config for the cluster.

` .google.cloud.redis.cluster.v1.AutomatedBackupConfig automated_backup_config = 42 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automatedBackupConfig field is set.  
  
### hasBackupCollection()
    
    
    public abstract boolean hasBackupCollection()

Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}

` optional string backup_collection = 39 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupCollection field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp associated with the cluster creation request.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCrossClusterReplicationConfig()
    
    
    public abstract boolean hasCrossClusterReplicationConfig()

Optional. Cross cluster replication config.

` .google.cloud.redis.cluster.v1.CrossClusterReplicationConfig cross_cluster_replication_config = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the crossClusterReplicationConfig field is set.  
  
### hasDeletionProtectionEnabled()
    
    
    public abstract boolean hasDeletionProtectionEnabled()

Optional. The delete operation will fail when the value is set to true.

`optional bool deletion_protection_enabled = 25 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deletionProtectionEnabled field is set.  
  
### hasEncryptionInfo()
    
    
    public abstract boolean hasEncryptionInfo()

Output only. Encryption information of the data at rest of the cluster.

` .google.cloud.redis.cluster.v1.EncryptionInfo encryption_info = 43 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionInfo field is set.  
  
### hasGcsSource()
    
    
    public abstract boolean hasGcsSource()

Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.

` .google.cloud.redis.cluster.v1.Cluster.GcsBackupSource gcs_source = 34 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsSource field is set.  
  
### hasKmsKey()
    
    
    public abstract boolean hasKmsKey()

Optional. The KMS key used to encrypt the at-rest data of the cluster.

` optional string kms_key = 40 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kmsKey field is set.  
  
### hasMaintenancePolicy()
    
    
    public abstract boolean hasMaintenancePolicy()

Optional. ClusterMaintenancePolicy determines when to allow or deny updates.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenancePolicy maintenance_policy = 26 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenancePolicy field is set.  
  
### hasMaintenanceSchedule()
    
    
    public abstract boolean hasMaintenanceSchedule()

Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.

` optional .google.cloud.redis.cluster.v1.ClusterMaintenanceSchedule maintenance_schedule = 27 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceSchedule field is set.  
  
### hasManagedBackupSource()
    
    
    public abstract boolean hasManagedBackupSource()

Optional. Backups generated and managed by memorystore service.

` .google.cloud.redis.cluster.v1.Cluster.ManagedBackupSource managed_backup_source = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the managedBackupSource field is set.  
  
### hasPersistenceConfig()
    
    
    public abstract boolean hasPersistenceConfig()

Optional. Persistence config (RDB, AOF) for the cluster.

` .google.cloud.redis.cluster.v1.ClusterPersistenceConfig persistence_config = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the persistenceConfig field is set.  
  
### hasPreciseSizeGb()
    
    
    public abstract boolean hasPreciseSizeGb()

Output only. Precise value of redis memory size in GB for the entire cluster.

`optional double precise_size_gb = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the preciseSizeGb field is set.  
  
### hasReplicaCount()
    
    
    public abstract boolean hasReplicaCount()

Optional. The number of replica nodes per shard.

`optional int32 replica_count = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the replicaCount field is set.  
  
### hasRotateServerCertificate()
    
    
    public abstract boolean hasRotateServerCertificate()

Optional. Input only. Rotate the server certificates.

` optional bool rotate_server_certificate = 55 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rotateServerCertificate field is set.  
  
### hasServerCaMode()
    
    
    public abstract boolean hasServerCaMode()

Optional. Server CA mode for the cluster.

` optional .google.cloud.redis.cluster.v1.ServerCaMode server_ca_mode = 53 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serverCaMode field is set.  
  
### hasServerCaPool()
    
    
    public abstract boolean hasServerCaPool()

Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".

` optional string server_ca_pool = 54 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serverCaPool field is set.  
  
### hasShardCount()
    
    
    public abstract boolean hasShardCount()

Optional. Number of shards for the Redis cluster.

`optional int32 shard_count = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shardCount field is set.  
  
### hasSizeGb()
    
    
    public abstract boolean hasSizeGb()

Output only. Redis memory size in GB for the entire cluster rounded up to the next integer.

`optional int32 size_gb = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sizeGb field is set.  
  
### hasStateInfo()
    
    
    public abstract boolean hasStateInfo()

Output only. Additional information about the current state of the cluster.

` .google.cloud.redis.cluster.v1.Cluster.StateInfo state_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stateInfo field is set.  
  
### hasZoneDistributionConfig()
    
    
    public abstract boolean hasZoneDistributionConfig()

Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.

` .google.cloud.redis.cluster.v1.ZoneDistributionConfig zone_distribution_config = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zoneDistributionConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
