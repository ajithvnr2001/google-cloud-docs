---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster
title: Class Cluster (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:52.775971+00:00
---

# Class Cluster (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Cluster (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.14 
    
    
    Cluster(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A cluster instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`gcs_source` |  `[google.cloud.redis_cluster_v1.types.Cluster.GcsBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.GcsBackupSource)`   
Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects. This field is a member of `oneof`_ `import_sources`.   
`managed_backup_source` |  `[google.cloud.redis_cluster_v1.types.Cluster.ManagedBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.ManagedBackupSource)`   
Optional. Backups generated and managed by memorystore service. This field is a member of `oneof`_ `import_sources`.   
`name` |  `str`   
Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp associated with the cluster creation request.   
`state` |  `[google.cloud.redis_cluster_v1.types.Cluster.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.State)`   
Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED   
`uid` |  `str`   
Output only. System assigned, unique identifier for the cluster.   
`replica_count` |  `int`   
Optional. The number of replica nodes per shard. This field is a member of `oneof`_ `_replica_count`.   
`authorization_mode` |  `[google.cloud.redis_cluster_v1.types.AuthorizationMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AuthorizationMode)`   
Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.   
`transit_encryption_mode` |  `[google.cloud.redis_cluster_v1.types.TransitEncryptionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.TransitEncryptionMode)`   
Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.   
`size_gb` |  `int`   
Output only. Redis memory size in GB for the entire cluster rounded up to the next integer. This field is a member of `oneof`_ `_size_gb`.   
`shard_count` |  `int`   
Optional. Number of shards for the Redis cluster. This field is a member of `oneof`_ `_shard_count`.   
`psc_configs` |  `MutableSequence[[google.cloud.redis_cluster_v1.types.PscConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscConfig)]`   
Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.   
`discovery_endpoints` |  `MutableSequence[[google.cloud.redis_cluster_v1.types.DiscoveryEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.DiscoveryEndpoint)]`   
Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.   
`psc_connections` |  `MutableSequence[[google.cloud.redis_cluster_v1.types.PscConnection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscConnection)]`   
Output only. The list of PSC connections that are auto-created through service connectivity automation.   
`state_info` |  `[google.cloud.redis_cluster_v1.types.Cluster.StateInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.StateInfo)`   
Output only. Additional information about the current state of the cluster.   
`node_type` |  `[google.cloud.redis_cluster_v1.types.NodeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.NodeType)`   
Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.   
`persistence_config` |  `[google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig)`   
Optional. Persistence config (RDB, AOF) for the cluster.   
`redis_configs` |  `MutableMapping[str, str]`   
Optional. Key/Value pairs of customer overrides for mutable Redis Configs   
`precise_size_gb` |  `float`   
Output only. Precise value of redis memory size in GB for the entire cluster. This field is a member of `oneof`_ `_precise_size_gb`.   
`zone_distribution_config` |  `[google.cloud.redis_cluster_v1.types.ZoneDistributionConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ZoneDistributionConfig)`   
Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.   
`cross_cluster_replication_config` |  `[google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig)`   
Optional. Cross cluster replication config.   
`deletion_protection_enabled` |  `bool`   
Optional. The delete operation will fail when the value is set to true. This field is a member of `oneof`_ `_deletion_protection_enabled`.   
`maintenance_policy` |  `[google.cloud.redis_cluster_v1.types.ClusterMaintenancePolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterMaintenancePolicy)`   
Optional. ClusterMaintenancePolicy determines when to allow or deny updates. This field is a member of `oneof`_ `_maintenance_policy`.   
`maintenance_schedule` |  `[google.cloud.redis_cluster_v1.types.ClusterMaintenanceSchedule](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterMaintenanceSchedule)`   
Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule. This field is a member of `oneof`_ `_maintenance_schedule`.   
`psc_service_attachments` |  `MutableSequence[[google.cloud.redis_cluster_v1.types.PscServiceAttachment](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscServiceAttachment)]`   
Output only. Service attachment details to configure Psc connections   
`cluster_endpoints` |  `MutableSequence[[google.cloud.redis_cluster_v1.types.ClusterEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterEndpoint)]`   
Optional. A list of cluster enpoints.   
`backup_collection` |  `str`   
Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection} This field is a member of `oneof`_ `_backup_collection`.   
`kms_key` |  `str`   
Optional. The KMS key used to encrypt the at-rest data of the cluster. This field is a member of `oneof`_ `_kms_key`.   
`automated_backup_config` |  `[google.cloud.redis_cluster_v1.types.AutomatedBackupConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AutomatedBackupConfig)`   
Optional. The automated backup config for the cluster.   
`encryption_info` |  `[google.cloud.redis_cluster_v1.types.EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.EncryptionInfo)`   
Output only. Encryption information of the data at rest of the cluster.   
`async_cluster_endpoints_deletion_enabled` |  `bool`   
Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted. This field is a member of `oneof`_ `_async_cluster_endpoints_deletion_enabled`.   
`server_ca_mode` |  `[google.cloud.redis_cluster_v1.types.ServerCaMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ServerCaMode)`   
Optional. Server CA mode for the cluster. This field is a member of `oneof`_ `_server_ca_mode`.   
`server_ca_pool` |  `str`   
Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}". This field is a member of `oneof`_ `_server_ca_pool`.   
`rotate_server_certificate` |  `bool`   
Optional. Input only. Rotate the server certificates. This field is a member of `oneof`_ `_rotate_server_certificate`.   
  
## Classes 

### GcsBackupSource
    
    
    GcsBackupSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters.

### ManagedBackupSource
    
    
    ManagedBackupSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Backups that generated and managed by memorystore.

### RedisConfigsEntry
    
    
    RedisConfigsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### State
    
    
    State(value)

Represents the different states of a Redis cluster.

### StateInfo
    
    
    StateInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents additional information about the state of the cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
