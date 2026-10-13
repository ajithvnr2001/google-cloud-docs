---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/summary_class/
title: Package Classes (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:53.566322+00:00
---

# Package Classes (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.14 

Summary of entries of Classes for google-cloud-redis-cluster.

## Classes 

### [CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient)

Configures and manages Cloud Memorystore for Redis clusters

Google Cloud Memorystore for Redis Cluster

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



### [CloudRedisClusterClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.CloudRedisClusterClient)

Configures and manages Cloud Memorystore for Redis clusters

Google Cloud Memorystore for Redis Cluster

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



### [ListBackupCollectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager)

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupCollectionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListBackupCollectionsPager)

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsResponse) object, and provides an `__iter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__iter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListBackupsPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersResponse) object, and provides an `__aiter__` method to iterate through its `clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers.ListClustersPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersResponse) object, and provides an `__iter__` method to iterate through its `clusters` field.

If there are more pages, the `__iter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AuthorizationMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AuthorizationMode)

Available authorization mode of a Redis cluster.

### [AutomatedBackupConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AutomatedBackupConfig)

The automated backup config for a cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutomatedBackupMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AutomatedBackupConfig.AutomatedBackupMode)

The automated backup mode.

### [FixedFrequencySchedule](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.AutomatedBackupConfig.FixedFrequencySchedule)

This schedule allows the backup to be triggered at a fixed frequency (currently only daily is supported).

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Backup)

Backup of a cluster.

### [BackupType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Backup.BackupType)

Type of the backup.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Backup.State)

State of the backup.

### [BackupClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.BackupClusterRequest)

Request for [BackupCluster].

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupCollection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.BackupCollection)

BackupCollection of a cluster.

### [BackupFile](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.BackupFile)

Backup is consisted of multiple backup files.

### [CertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CertificateAuthority)

Redis cluster certificate authority

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ManagedCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CertificateAuthority.ManagedCertificateAuthority)

### [CertChain](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CertificateAuthority.ManagedCertificateAuthority.CertChain)

### [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster)

A cluster instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.GcsBackupSource)

Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters.

### [ManagedBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.ManagedBackupSource)

Backups that generated and managed by memorystore.

### [RedisConfigsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.RedisConfigsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.State)

Represents the different states of a Redis cluster.

### [StateInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.StateInfo)

Represents additional information about the state of the cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.Cluster.StateInfo.UpdateInfo)

Represents information about an updating cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ClusterEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterEndpoint)

ClusterEndpoint consists of PSC connections that are created as a group in each VPC network for accessing the cluster. In each group, there shall be one connection for each service attachment in the cluster.

### [ClusterMaintenancePolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterMaintenancePolicy)

Maintenance policy per cluster.

### [ClusterMaintenanceSchedule](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterMaintenanceSchedule)

Upcoming maitenance schedule.

### [ClusterPersistenceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig)

Configuration of the persistence functionality.

### [AOFConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig.AOFConfig)

Configuration of the AOF based persistence.

### [AppendFsync](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig.AOFConfig.AppendFsync)

Available fsync modes.

### [PersistenceMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig.PersistenceMode)

Available persistence modes.

### [RDBConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig.RDBConfig)

Configuration of the RDB based persistence.

### [SnapshotPeriod](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterPersistenceConfig.RDBConfig.SnapshotPeriod)

Available snapshot periods.

### [ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ClusterWeeklyMaintenanceWindow)

Time window specified for weekly operations.

### [ConnectionDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ConnectionDetail)

Detailed information of each PSC connection.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConnectionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ConnectionType)

Type of a PSC connection, for cluster access purpose.

### [CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CreateClusterRequest)

Request for `CreateCluster][CloudRedis.CreateCluster]`.

### [CrossClusterReplicationConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig)

Cross cluster replication config.

### [ClusterRole](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig.ClusterRole)

The role of the cluster in cross cluster replication.

### [Membership](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig.Membership)

An output only view of all the member clusters participating in the cross cluster replication.

### [RemoteCluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.CrossClusterReplicationConfig.RemoteCluster)

Details of the remote cluster associated with this cluster in a cross cluster replication setup.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.DeleteBackupRequest)

Request for [DeleteBackup].

### [DeleteClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.DeleteClusterRequest)

Request for `DeleteCluster][CloudRedis.DeleteCluster]`.

### [DiscoveryEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.DiscoveryEndpoint)

Endpoints on each network, for Redis clients to connect to the cluster.

### [EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.EncryptionInfo)

EncryptionInfo describes the encryption information of a cluster or a backup.

### [KmsKeyState](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.EncryptionInfo.KmsKeyState)

The state of the KMS key perceived by the system. Refer to the public documentation for the impact of each state.

### [Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.EncryptionInfo.Type)

Possible encryption types.

### [ExportBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ExportBackupRequest)

Request for [ExportBackup].

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetBackupCollectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.GetBackupCollectionRequest)

Request for [GetBackupCollection].

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.GetBackupRequest)

Request for [GetBackup].

### [GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.GetClusterCertificateAuthorityRequest)

Request for `GetClusterCertificateAuthorityRequest][CloudRedis.GetClusterCertificateAuthorityRequest]`.

### [GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.GetClusterRequest)

Request for `GetCluster][CloudRedis.GetCluster]`.

### [GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.GetSharedRegionalCertificateAuthorityRequest)

Request for `GetSharedRegionalCertificateAuthority][CloudRedis.GetSharedRegionalCertificateAuthority]`.

### [ListBackupCollectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsRequest)

Request for [ListBackupCollections]

### [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupCollectionsResponse)

Response for [ListBackupCollections].

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsRequest)

Request for [ListBackups].

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListBackupsResponse)

Response for [ListBackups].

### [ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersRequest)

Request for `ListClusters][CloudRedis.ListClusters]`.

### [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ListClustersResponse)

Response for `ListClusters][CloudRedis.ListClusters]`.

### [NodeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.NodeType)

NodeType of a redis cluster node,

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.OperationMetadata)

Pre-defined metadata fields.

### [PscAutoConnection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscAutoConnection)

Details of consumer resources in a PSC connection that is created through Service Connectivity Automation.

### [PscConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscConfig)

### [PscConnection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscConnection)

Details of consumer resources in a PSC connection.

### [PscConnectionStatus](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscConnectionStatus)

Status of the PSC connection.

### [PscServiceAttachment](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.PscServiceAttachment)

Configuration of a service attachment of the cluster, for creating PSC connections.

### [RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.RescheduleClusterMaintenanceRequest)

Request for rescheduling a cluster maintenance.

### [RescheduleType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.RescheduleClusterMaintenanceRequest.RescheduleType)

Reschedule options.

### [ServerCaMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ServerCaMode)

Server CA mode for the cluster.

### [SharedRegionalCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.SharedRegionalCertificateAuthority)

Shared regional certificate authority

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RegionalManagedCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority)

CA certificate chains for redis managed server authentication.

### [RegionalCertChain](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain)

The certificates that form the CA chain, from leaf to root order.

### [TransitEncryptionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.TransitEncryptionMode)

Available mode of in-transit encryption.

### [UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.UpdateClusterRequest)

Request for `UpdateCluster][CloudRedis.UpdateCluster]`.

### [ZoneDistributionConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ZoneDistributionConfig)

Zone distribution config for allocation of cluster resources.

### [ZoneDistributionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.types.ZoneDistributionConfig.ZoneDistributionMode)

Defines various modes of zone distribution.

### [CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient)

Configures and manages Cloud Memorystore for Redis clusters

Google Cloud Memorystore for Redis Cluster

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



### [CloudRedisClusterClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterClient)

Configures and manages Cloud Memorystore for Redis clusters

Google Cloud Memorystore for Redis Cluster

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



### [ListBackupCollectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager)

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupCollectionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsPager)

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) object, and provides an `__iter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__iter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) object, and provides an `__aiter__` method to iterate through its `clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersPager)

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) object, and provides an `__iter__` method to iterate through its `clusters` field.

If there are more pages, the `__iter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AuthorizationMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.AuthorizationMode)

Available authorization mode of a Redis cluster.

### [AutomatedBackupConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig)

The automated backup config for a cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutomatedBackupMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig.AutomatedBackupMode)

The automated backup mode.

### [FixedFrequencySchedule](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.AutomatedBackupConfig.FixedFrequencySchedule)

This schedule allows the backup to be triggered at a fixed frequency (currently only daily is supported).

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Backup)

Backup of a cluster.

### [BackupType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Backup.BackupType)

Type of the backup.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Backup.State)

State of the backup.

### [BackupClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupClusterRequest)

Request for [BackupCluster].

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupCollection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupCollection)

BackupCollection of a cluster.

### [BackupFile](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupFile)

Backup is consisted of multiple backup files.

### [CertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CertificateAuthority)

Redis cluster certificate authority

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ManagedCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CertificateAuthority.ManagedCertificateAuthority)

### [CertChain](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CertificateAuthority.ManagedCertificateAuthority.CertChain)

### [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster)

A cluster instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.GcsBackupSource)

Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters.

### [ManagedBackupSource](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.ManagedBackupSource)

Backups that generated and managed by memorystore.

### [RedisConfigsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.RedisConfigsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.State)

Represents the different states of a Redis cluster.

### [StateInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.StateInfo)

Represents additional information about the state of the cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.StateInfo.UpdateInfo)

Represents information about an updating cluster.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ClusterEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterEndpoint)

ClusterEndpoint consists of PSC connections that are created as a group in each VPC network for accessing the cluster. In each group, there shall be one connection for each service attachment in the cluster.

### [ClusterMaintenancePolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterMaintenancePolicy)

Maintenance policy per cluster.

### [ClusterMaintenanceSchedule](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterMaintenanceSchedule)

Upcoming maitenance schedule.

### [ClusterPersistenceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig)

Configuration of the persistence functionality.

### [AOFConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.AOFConfig)

Configuration of the AOF based persistence.

### [AppendFsync](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.AOFConfig.AppendFsync)

Available fsync modes.

### [PersistenceMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.PersistenceMode)

Available persistence modes.

### [RDBConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.RDBConfig)

Configuration of the RDB based persistence.

### [SnapshotPeriod](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterPersistenceConfig.RDBConfig.SnapshotPeriod)

Available snapshot periods.

### [ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ClusterWeeklyMaintenanceWindow)

Time window specified for weekly operations.

### [ConnectionDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ConnectionDetail)

Detailed information of each PSC connection.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConnectionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ConnectionType)

Type of a PSC connection, for cluster access purpose.

### [CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CreateClusterRequest)

Request for `CreateCluster][CloudRedis.CreateCluster]`.

### [CrossClusterReplicationConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig)

Cross cluster replication config.

### [ClusterRole](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.ClusterRole)

The role of the cluster in cross cluster replication.

### [Membership](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.Membership)

An output only view of all the member clusters participating in the cross cluster replication.

### [RemoteCluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CrossClusterReplicationConfig.RemoteCluster)

Details of the remote cluster associated with this cluster in a cross cluster replication setup.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteBackupRequest)

Request for [DeleteBackup].

### [DeleteClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteClusterRequest)

Request for `DeleteCluster][CloudRedis.DeleteCluster]`.

### [DiscoveryEndpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DiscoveryEndpoint)

Endpoints on each network, for Redis clients to connect to the cluster.

### [EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.EncryptionInfo)

EncryptionInfo describes the encryption information of a cluster or a backup.

### [KmsKeyState](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.EncryptionInfo.KmsKeyState)

The state of the KMS key perceived by the system. Refer to the public documentation for the impact of each state.

### [Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.EncryptionInfo.Type)

Possible encryption types.

### [ExportBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ExportBackupRequest)

Request for [ExportBackup].

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetBackupCollectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupCollectionRequest)

Request for [GetBackupCollection].

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupRequest)

Request for [GetBackup].

### [GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterCertificateAuthorityRequest)

Request for `GetClusterCertificateAuthorityRequest][CloudRedis.GetClusterCertificateAuthorityRequest]`.

### [GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterRequest)

Request for `GetCluster][CloudRedis.GetCluster]`.

### [GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetSharedRegionalCertificateAuthorityRequest)

Request for `GetSharedRegionalCertificateAuthority][CloudRedis.GetSharedRegionalCertificateAuthority]`.

### [ListBackupCollectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest)

Request for [ListBackupCollections]

### [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse)

Response for [ListBackupCollections].

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest)

Request for [ListBackups].

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse)

Response for [ListBackups].

### [ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersRequest)

Request for `ListClusters][CloudRedis.ListClusters]`.

### [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse)

Response for `ListClusters][CloudRedis.ListClusters]`.

### [NodeType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.NodeType)

NodeType of a redis cluster node,

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.OperationMetadata)

Pre-defined metadata fields.

### [PscAutoConnection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.PscAutoConnection)

Details of consumer resources in a PSC connection that is created through Service Connectivity Automation.

### [PscConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.PscConfig)

### [PscConnection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.PscConnection)

Details of consumer resources in a PSC connection.

### [PscConnectionStatus](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.PscConnectionStatus)

Status of the PSC connection.

### [PscServiceAttachment](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.PscServiceAttachment)

Configuration of a service attachment of the cluster, for creating PSC connections.

### [RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest)

Request for rescheduling a cluster maintenance.

### [RescheduleType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest.RescheduleType)

Reschedule options.

### [ServerCaMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ServerCaMode)

Server CA mode for the cluster.

### [SharedRegionalCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority)

Shared regional certificate authority

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RegionalManagedCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority)

CA certificate chains for redis managed server authentication.

### [RegionalCertChain](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain)

The certificates that form the CA chain, from leaf to root order.

### [TransitEncryptionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.TransitEncryptionMode)

Available mode of in-transit encryption.

### [UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.UpdateClusterRequest)

Request for `UpdateCluster][CloudRedis.UpdateCluster]`.

### [ZoneDistributionConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig)

Zone distribution config for allocation of cluster resources.

### [ZoneDistributionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ZoneDistributionConfig.ZoneDistributionMode)

Defines various modes of zone distribution.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1.services.cloud_redis_cluster.pagers)

API documentation for `redis_cluster_v1.services.cloud_redis_cluster.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers)

API documentation for `redis_cluster_v1beta1.services.cloud_redis_cluster.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
