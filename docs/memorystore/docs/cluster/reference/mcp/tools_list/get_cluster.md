---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_cluster/
title: MCP Tools Reference: redis.googleapis.com \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:54.502552+00:00
---

# MCP Tools Reference: redis.googleapis.com  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  MCP Tools Reference: redis.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_cluster`

Get detailed information about a cluster in Memorystore for Redis Cluster.

The following sample demonstrate how to use `curl` to invoke the `get_cluster` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://redis.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_cluster",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for `GetCluster`.

### GetClusterRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Redis cluster resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}` where `location_id` refers to a Google Cloud region.  
  
## Output Schema

A cluster instance.

### Cluster

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "state": enum (State),
      "uid": string,
      "authorizationMode": enum (AuthorizationMode),
      "transitEncryptionMode": enum (TransitEncryptionMode),
      "pscConfigs": [
        {
          object ([PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConfig))
        }
      ],
      "discoveryEndpoints": [
        {
          object ([DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.DiscoveryEndpoint))
        }
      ],
      "pscConnections": [
        {
          object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConnection))
        }
      ],
      "stateInfo": {
        object ([StateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.StateInfo))
      },
      "nodeType": enum (NodeType),
      "persistenceConfig": {
        object ([ClusterPersistenceConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterPersistenceConfig))
      },
      "redisConfigs": {
        string: string,
        ...
      },
      "zoneDistributionConfig": {
        object ([ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ZoneDistributionConfig))
      },
      "crossClusterReplicationConfig": {
        object ([CrossClusterReplicationConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.CrossClusterReplicationConfig))
      },
      "pscServiceAttachments": [
        {
          object ([PscServiceAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscServiceAttachment))
        }
      ],
      "clusterEndpoints": [
        {
          object ([ClusterEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterEndpoint))
        }
      ],
      "automatedBackupConfig": {
        object ([AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.AutomatedBackupConfig))
      },
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.EncryptionInfo))
      },
      "availableMaintenanceVersions": [
        string
      ],
      "allowFewerZonesDeployment": boolean,
      "labels": {
        string: string,
        ...
      },
      "aclPolicy": string,
    
      // Union field import_sources can be only one of the following:
      "gcsSource": {
        object ([GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.GcsBackupSource))
      },
      "managedBackupSource": {
        object ([ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ManagedBackupSource))
      }
      // End of list of possible types for union field import_sources.
    
      // Union field _replica_count can be only one of the following:
      "replicaCount": integer
      // End of list of possible types for union field _replica_count.
    
      // Union field _size_gb can be only one of the following:
      "sizeGb": integer
      // End of list of possible types for union field _size_gb.
    
      // Union field _shard_count can be only one of the following:
      "shardCount": integer
      // End of list of possible types for union field _shard_count.
    
      // Union field _precise_size_gb can be only one of the following:
      "preciseSizeGb": number
      // End of list of possible types for union field _precise_size_gb.
    
      // Union field _deletion_protection_enabled can be only one of the following:
      "deletionProtectionEnabled": boolean
      // End of list of possible types for union field _deletion_protection_enabled.
    
      // Union field _maintenance_policy can be only one of the following:
      "maintenancePolicy": {
        object ([ClusterMaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterMaintenancePolicy))
      }
      // End of list of possible types for union field _maintenance_policy.
    
      // Union field _maintenance_schedule can be only one of the following:
      "maintenanceSchedule": {
        object ([ClusterMaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterMaintenanceSchedule))
      }
      // End of list of possible types for union field _maintenance_schedule.
    
      // Union field _satisfies_pzs can be only one of the following:
      "satisfiesPzs": boolean
      // End of list of possible types for union field _satisfies_pzs.
    
      // Union field _satisfies_pzi can be only one of the following:
      "satisfiesPzi": boolean
      // End of list of possible types for union field _satisfies_pzi.
    
      // Union field _simulate_maintenance_event can be only one of the following:
      "simulateMaintenanceEvent": boolean
      // End of list of possible types for union field _simulate_maintenance_event.
    
      // Union field _backup_collection can be only one of the following:
      "backupCollection": string
      // End of list of possible types for union field _backup_collection.
    
      // Union field _kms_key can be only one of the following:
      "kmsKey": string
      // End of list of possible types for union field _kms_key.
    
      // Union field _ondemand_maintenance can be only one of the following:
      "ondemandMaintenance": boolean
      // End of list of possible types for union field _ondemand_maintenance.
    
      // Union field _async_cluster_endpoints_deletion_enabled can be only one of the
      // following:
      "asyncClusterEndpointsDeletionEnabled": boolean
      // End of list of possible types for union field
      // _async_cluster_endpoints_deletion_enabled.
    
      // Union field _maintenance_version can be only one of the following:
      "maintenanceVersion": string
      // End of list of possible types for union field _maintenance_version.
    
      // Union field _effective_maintenance_version can be only one of the following:
      "effectiveMaintenanceVersion": string
      // End of list of possible types for union field
      // _effective_maintenance_version.
    
      // Union field _server_ca_mode can be only one of the following:
      "serverCaMode": enum (ServerCaMode)
      // End of list of possible types for union field _server_ca_mode.
    
      // Union field _server_ca_pool can be only one of the following:
      "serverCaPool": string
      // End of list of possible types for union field _server_ca_pool.
    
      // Union field _rotate_server_certificate can be only one of the following:
      "rotateServerCertificate": boolean
      // End of list of possible types for union field _rotate_server_certificate.
    
      // Union field _acl_policy_in_sync can be only one of the following:
      "aclPolicyInSync": boolean
      // End of list of possible types for union field _acl_policy_in_sync.
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp associated with the cluster creation request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`State`)` Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED  
`uid` |  `string` Output only. System assigned, unique identifier for the cluster.  
`authorizationMode` |  `enum (`AuthorizationMode`)` Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.  
`transitEncryptionMode` |  `enum (`TransitEncryptionMode`)` Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.  
`pscConfigs[]` |  `object (`[PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConfig)`)` Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.  
`discoveryEndpoints[]` |  `object (`[DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.DiscoveryEndpoint)`)` Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.  
`pscConnections[]` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConnection)`)` Output only. The list of PSC connections that are auto-created through service connectivity automation.  
`stateInfo` |  `object (`[StateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.StateInfo)`)` Output only. Additional information about the current state of the cluster.  
`nodeType` |  `enum (`NodeType`)` Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.  
`persistenceConfig` |  `object (`[ClusterPersistenceConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterPersistenceConfig)`)` Optional. Persistence config (RDB, AOF) for the cluster.  
`redisConfigs` |  `map (key: string, value: string)` Optional. Key/Value pairs of customer overrides for mutable Redis ConfigsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`zoneDistributionConfig` |  `object (`[ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ZoneDistributionConfig)`)` Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.  
`crossClusterReplicationConfig` |  `object (`[CrossClusterReplicationConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.CrossClusterReplicationConfig)`)` Optional. Cross cluster replication config.  
`pscServiceAttachments[]` |  `object (`[PscServiceAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscServiceAttachment)`)` Output only. Service attachment details to configure Psc connections  
`clusterEndpoints[]` |  `object (`[ClusterEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterEndpoint)`)` Optional. A list of cluster endpoints.  
`automatedBackupConfig` |  `object (`[AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.AutomatedBackupConfig)`)` Optional. The automated backup config for the cluster.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.EncryptionInfo)`)` Output only. Encryption information of the data at rest of the cluster.  
`availableMaintenanceVersions[]` |  `string` Output only. This field is used to determine the available maintenance versions for the self service update.  
`allowFewerZonesDeployment  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. Deprecated, do not use.  
`labels` |  `map (key: string, value: string)` Optional. Labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`aclPolicy` |  `string` Optional. The ACL policy to be applied to the cluster.  
Union field `import_sources`. The source to import from. `import_sources` can be only one of the following:  
`gcsSource` |  `object (`[GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.GcsBackupSource)`)` Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.  
`managedBackupSource` |  `object (`[ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ManagedBackupSource)`)` Optional. Backups generated and managed by memorystore service.  
Union field `_replica_count`.`_replica_count` can be only one of the following:  
`replicaCount` |  `integer` Optional. The number of replica nodes per shard.  
Union field `_size_gb`.`_size_gb` can be only one of the following:  
`sizeGb` |  `integer` Output only. Redis memory size in GB for the entire cluster rounded up to the next integer.  
Union field `_shard_count`.`_shard_count` can be only one of the following:  
`shardCount` |  `integer` Optional. Number of shards for the Redis cluster.  
Union field `_precise_size_gb`.`_precise_size_gb` can be only one of the following:  
`preciseSizeGb` |  `number` Output only. Precise value of redis memory size in GB for the entire cluster.  
Union field `_deletion_protection_enabled`.`_deletion_protection_enabled` can be only one of the following:  
`deletionProtectionEnabled` |  `boolean` Optional. The delete operation will fail when the value is set to true.  
Union field `_maintenance_policy`.`_maintenance_policy` can be only one of the following:  
`maintenancePolicy` |  `object (`[ClusterMaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterMaintenancePolicy)`)` Optional. ClusterMaintenancePolicy determines when to allow or deny updates.  
Union field `_maintenance_schedule`.`_maintenance_schedule` can be only one of the following:  
`maintenanceSchedule` |  `object (`[ClusterMaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterMaintenanceSchedule)`)` Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.  
Union field `_satisfies_pzs`.`_satisfies_pzs` can be only one of the following:  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
Union field `_satisfies_pzi`.`_satisfies_pzi` can be only one of the following:  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
Union field `_simulate_maintenance_event`.`_simulate_maintenance_event` can be only one of the following:  
`simulateMaintenanceEvent` |  `boolean` Optional. Input only. Simulate a maintenance event.  
Union field `_backup_collection`.`_backup_collection` can be only one of the following:  
`backupCollection` |  `string` Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}  
Union field `_kms_key`.`_kms_key` can be only one of the following:  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the at-rest data of the cluster.  
Union field `_ondemand_maintenance`.`_ondemand_maintenance` can be only one of the following:  
`ondemandMaintenance  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Input only. Ondemand maintenance for the cluster. This field can be used to trigger ondemand critical update on the cluster.  
Union field `_async_cluster_endpoints_deletion_enabled`.`_async_cluster_endpoints_deletion_enabled` can be only one of the following:  
`asyncClusterEndpointsDeletionEnabled` |  `boolean` Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted.  
Union field `_maintenance_version`.`_maintenance_version` can be only one of the following:  
`maintenanceVersion` |  `string` Optional. This field can be used to trigger self service update to indicate the desired maintenance version. The input to this field can be determined by the available_maintenance_versions field.  
Union field `_effective_maintenance_version`.`_effective_maintenance_version` can be only one of the following:  
`effectiveMaintenanceVersion` |  `string` Output only. This field represents the actual maintenance version of the cluster.  
Union field `_server_ca_mode`.`_server_ca_mode` can be only one of the following:  
`serverCaMode` |  `enum (`ServerCaMode`)` Optional. Server CA mode for the cluster.  
Union field `_server_ca_pool`.`_server_ca_pool` can be only one of the following:  
`serverCaPool` |  `string` Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if server_ca_mode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".  
Union field `_rotate_server_certificate`.`_rotate_server_certificate` can be only one of the following:  
`rotateServerCertificate` |  `boolean` Optional. Input only. Rotate the server certificates.  
Union field `_acl_policy_in_sync`.`_acl_policy_in_sync` can be only one of the following:  
`aclPolicyInSync` |  `boolean` Optional. Output only. Indicates whether the ACL rules applied to the cluster are in sync with the latest ACL policy rules. This field is only applicable if the ACL policy is set for the cluster.  
  
### GcsBackupSource

JSON representation  
---  
      
    
    {
      "uris": [
        string
      ]
    }  
  
Fields  
---  
`uris[]` |  `string` Optional. URIs of the Cloud Storage objects to import. Example: gs://bucket1/object1, gs://bucket2/folder2/object2  
  
### ManagedBackupSource

JSON representation  
---  
      
    
    {
      "backup": string
    }  
  
Fields  
---  
`backup` |  `string` Optional. Example: //redis.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup} A shorter version (without the prefix) of the backup name is also supported, like projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup_id} In this case, it assumes the backup is under redis.googleapis.com.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### PscConfig

JSON representation  
---  
      
    
    {
      "network": string
    }  
  
Fields  
---  
`network` |  `string` Required. The network where the IP address of the discovery endpoint will be reserved, in the form of projects/{network_project}/global/networks/{network_id}.  
  
### DiscoveryEndpoint

JSON representation  
---  
      
    
    {
      "address": string,
      "port": integer,
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConfig))
      }
    }  
  
Fields  
---  
`address` |  `string` Output only. Address of the exposed Redis endpoint used by clients to connect to the service. The address could be either IP or hostname.  
`port` |  `integer` Output only. The port number of the exposed Redis endpoint.  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConfig)`)` Output only. Customer configuration for where the endpoint is created and accessed from.  
  
### PscConnection

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "address": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum (PscConnectionStatus),
      "connectionType": enum (ConnectionType),
    
      // Union field ports can be only one of the following:
      "port": integer
      // End of list of possible types for union field ports.
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Required. The PSC connection id of the forwarding rule connected to the service attachment.  
`address` |  `string` Required. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Required. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.  
`projectId` |  `string` Optional. Project ID of the consumer project where the forwarding rule is created in.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`PscConnectionStatus`)` Output only. The status of the PSC connection. Please note that this value is updated periodically. To get the latest status of a PSC connection, follow <https://cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details>.  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of the PSC connection.  
Union field `ports`. The port number of the exposed discovery endpoint. `ports` can be only one of the following:  
`port` |  `integer` Output only. port will only be set for Primary/Reader or Discovery endpoint.  
  
### StateInfo

JSON representation  
---  
      
    
    {
    
      // Union field info can be only one of the following:
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.UpdateInfo))
      }
      // End of list of possible types for union field info.
    }  
  
Fields  
---  
Union field `info`.`info` can be only one of the following:  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.UpdateInfo)`)` Describes ongoing update on the cluster when cluster state is UPDATING.  
  
### UpdateInfo

JSON representation  
---  
      
    
    {
    
      // Union field _target_shard_count can be only one of the following:
      "targetShardCount": integer
      // End of list of possible types for union field _target_shard_count.
    
      // Union field _target_replica_count can be only one of the following:
      "targetReplicaCount": integer
      // End of list of possible types for union field _target_replica_count.
    
      // Union field _target_node_type can be only one of the following:
      "targetNodeType": enum (NodeType)
      // End of list of possible types for union field _target_node_type.
    }  
  
Fields  
---  
Union field `_target_shard_count`.`_target_shard_count` can be only one of the following:  
`targetShardCount` |  `integer` Target number of shards for redis cluster  
Union field `_target_replica_count`.`_target_replica_count` can be only one of the following:  
`targetReplicaCount` |  `integer` Target number of replica nodes per shard.  
Union field `_target_node_type`.`_target_node_type` can be only one of the following:  
`targetNodeType` |  `enum (`NodeType`)` Target node type for redis cluster.  
  
### ClusterPersistenceConfig

JSON representation  
---  
      
    
    {
      "mode": enum (PersistenceMode),
      "rdbConfig": {
        object ([RDBConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RDBConfig))
      },
      "aofConfig": {
        object ([AOFConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.AOFConfig))
      }
    }  
  
Fields  
---  
`mode` |  `enum (`PersistenceMode`)` Optional. The mode of persistence.  
`rdbConfig` |  `object (`[RDBConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RDBConfig)`)` Optional. RDB configuration. This field will be ignored if mode is not RDB.  
`aofConfig` |  `object (`[AOFConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.AOFConfig)`)` Optional. AOF configuration. This field will be ignored if mode is not AOF.  
  
### RDBConfig

JSON representation  
---  
      
    
    {
      "rdbSnapshotPeriod": enum (SnapshotPeriod),
      "rdbSnapshotStartTime": string
    }  
  
Fields  
---  
`rdbSnapshotPeriod` |  `enum (`SnapshotPeriod`)` Optional. Period between RDB snapshots.  
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### AOFConfig

JSON representation  
---  
      
    
    {
      "appendFsync": enum (AppendFsync)
    }  
  
Fields  
---  
`appendFsync` |  `enum (`AppendFsync`)` Optional. fsync configuration.  
  
### RedisConfigsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### ZoneDistributionConfig

JSON representation  
---  
      
    
    {
      "mode": enum (ZoneDistributionMode),
      "zone": string
    }  
  
Fields  
---  
`mode` |  `enum (`ZoneDistributionMode`)` Optional. The mode of zone distribution. Defaults to MULTI_ZONE, when not specified.  
`zone` |  `string` Optional. When SINGLE ZONE distribution is selected, zone field would be used to allocate all resources in that zone. This is not applicable to MULTI_ZONE, and would be ignored for MULTI_ZONE clusters.  
  
### CrossClusterReplicationConfig

JSON representation  
---  
      
    
    {
      "clusterRole": enum (ClusterRole),
      "primaryCluster": {
        object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster))
      },
      "secondaryClusters": [
        {
          object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster))
        }
      ],
      "updateTime": string,
      "membership": {
        object ([Membership](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.Membership))
      }
    }  
  
Fields  
---  
`clusterRole` |  `enum (`ClusterRole`)` Output only. The role of the cluster in cross cluster replication.  
`primaryCluster` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster)`)` Details of the primary cluster that is used as the replication source for this secondary cluster.This field is only set for a secondary cluster.  
`secondaryClusters[]` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster)`)` List of secondary clusters that are replicating from this primary cluster.This field is only set for a primary cluster.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time cross cluster replication config was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.Membership)`)` Output only. An output only view of all the member clusters participating in the cross cluster replication. This view will be provided by every member cluster irrespective of its cluster role(primary or secondary).A primary cluster can provide information about all the secondary clusters replicating from it. However, a secondary cluster only knows about the primary cluster from which it is replicating. However, for scenarios, where the primary cluster is unavailable(e.g. regional outage), a GetCluster request can be sent to any other member cluster and this field will list all the member clusters participating in cross cluster replication.  
  
### RemoteCluster

JSON representation  
---  
      
    
    {
      "cluster": string,
      "uid": string
    }  
  
Fields  
---  
`cluster` |  `string` Output only. The full resource path of the remote cluster in the format: projects//locations//clusters/  
`uid` |  `string` Output only. The unique identifier of the remote cluster.  
  
### Membership

JSON representation  
---  
      
    
    {
      "primaryCluster": {
        object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster))
      },
      "secondaryClusters": [
        {
          object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster))
        }
      ]
    }  
  
Fields  
---  
`primaryCluster` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster)`)` Output only. The primary cluster that acts as the source of replication for the secondary clusters.  
`secondaryClusters[]` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.RemoteCluster)`)` Output only. The list of secondary clusters replicating from the primary cluster.  
  
### ClusterMaintenancePolicy

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "weeklyMaintenanceWindow": [
        {
          object ([ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterWeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created i.e. Maintenance Window or Deny Period was assigned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was updated i.e. Maintenance Window or Deny Period was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`weeklyMaintenanceWindow[]` |  `object (`[ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ClusterWeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_maintenance_window is expected to be one.  
  
### ClusterWeeklyMaintenanceWindow

JSON representation  
---  
      
    
    {
      "day": enum (google.type.DayOfWeek),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`day` |  `enum (`google.type.DayOfWeek`)` Optional. Allows to define schedule that runs specified day of the week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.TimeOfDay)`)` Optional. Start time of the window in UTC.  
  
### TimeOfDay

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
### ClusterMaintenanceSchedule

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### PscServiceAttachment

JSON representation  
---  
      
    
    {
      "serviceAttachment": string,
      "connectionType": enum (ConnectionType)
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Output only. Service attachment URI which your self-created PscConnection should use as target  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of a PSC connection targeting this service attachment.  
  
### ClusterEndpoint

JSON representation  
---  
      
    
    {
      "connections": [
        {
          object ([ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ConnectionDetail))
        }
      ]
    }  
  
Fields  
---  
`connections[]` |  `object (`[ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.ConnectionDetail)`)` Required. A group of PSC connections. They are created in the same VPC network, one for each service attachment in the cluster.  
  
### ConnectionDetail

JSON representation  
---  
      
    
    {
    
      // Union field connection can be only one of the following:
      "pscAutoConnection": {
        object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscAutoConnection))
      },
      "pscConnection": {
        object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConnection))
      }
      // End of list of possible types for union field connection.
    }  
  
Fields  
---  
Union field `connection`. A PSC connection to a cluster could either be created through Service Connectivity Automation (auto-registered connection) during the cluster creation, or it could be created by customer themselves (user-registered connection). `connection` can be only one of the following:  
`pscAutoConnection` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscAutoConnection)`)` Detailed information of a PSC connection that is created through service connectivity automation.  
`pscConnection` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.PscConnection)`)` Detailed information of a PSC connection that is created by the customer who owns the cluster.  
  
### PscAutoConnection

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "address": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum (PscConnectionStatus),
      "connectionType": enum (ConnectionType)
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Output only. The PSC connection id of the forwarding rule connected to the service attachment.  
`address` |  `string` Output only. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Output only. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.  
`projectId` |  `string` Required. The consumer project_id where the forwarding rule is created from.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`PscConnectionStatus`)` Output only. The status of the PSC connection. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of the PSC connection.  
  
### AutomatedBackupConfig

JSON representation  
---  
      
    
    {
      "automatedBackupMode": enum (AutomatedBackupMode),
    
      // Union field schedule can be only one of the following:
      "fixedFrequencySchedule": {
        object ([FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.FixedFrequencySchedule))
      }
      // End of list of possible types for union field schedule.
    
      // Union field _retention can be only one of the following:
      "retention": string
      // End of list of possible types for union field _retention.
    }  
  
Fields  
---  
`automatedBackupMode` |  `enum (`AutomatedBackupMode`)` Optional. The automated backup mode. If the mode is disabled, the other fields will be ignored.  
Union field `schedule`. The schedule of automated backups. `schedule` can be only one of the following:  
`fixedFrequencySchedule` |  `object (`[FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.FixedFrequencySchedule)`)` Optional. Trigger automated backups at a fixed frequency.  
Union field `_retention`.`_retention` can be only one of the following:  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to keep automated backups before the backups are deleted. The value should be between 1 day and 365 days. If not specified, the default value is 35 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### FixedFrequencySchedule

JSON representation  
---  
      
    
    {
    
      // Union field _start_time can be only one of the following:
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.TimeOfDay))
      }
      // End of list of possible types for union field _start_time.
    }  
  
Fields  
---  
Union field `_start_time`.`_start_time` can be only one of the following:  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters#Output.Schema.TimeOfDay)`)` Required. The start time of every automated backup in UTC. It must be set to the start of an hour. This field is required.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### EncryptionInfo

JSON representation  
---  
      
    
    {
      "encryptionType": enum (Type),
      "kmsKeyVersions": [
        string
      ],
      "kmsKeyPrimaryState": enum (KmsKeyState),
      "lastUpdateTime": string
    }  
  
Fields  
---  
`encryptionType` |  `enum (`Type`)` Output only. Type of encryption.  
`kmsKeyVersions[]` |  `string` Output only. KMS key versions that are being used to protect the data at-rest.  
`kmsKeyPrimaryState` |  `enum (`KmsKeyState`)` Output only. The state of the primary version of the KMS key perceived by the system. This field is not populated in backups.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time when the encryption info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
