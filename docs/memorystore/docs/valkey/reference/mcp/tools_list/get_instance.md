---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_instance/
title: MCP Tools Reference: memorystore.googleapis.com \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:48.469512+00:00
---

# MCP Tools Reference: memorystore.googleapis.com  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/get_instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  MCP Tools Reference: memorystore.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_instance`

Get detailed information about a Memorystore for Valkey instance.

The following sample demonstrate how to use `curl` to invoke the `get_instance` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://memorystore.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_instance",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for `GetInstance`.

### GetInstanceRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the instance to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}  
  
## Output Schema

A Memorystore instance.

### Instance

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum (State),
      "stateInfo": {
        object ([StateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.StateInfo))
      },
      "uid": string,
      "authorizationMode": enum (AuthorizationMode),
      "transitEncryptionMode": enum (TransitEncryptionMode),
      "shardCount": integer,
      "discoveryEndpoints": [
        {
          object ([DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.DiscoveryEndpoint))
        }
      ],
      "nodeType": enum (NodeType),
      "persistenceConfig": {
        object ([PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PersistenceConfig))
      },
      "engineVersion": string,
      "engineConfigs": {
        string: string,
        ...
      },
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.NodeConfig))
      },
      "zoneDistributionConfig": {
        object ([ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ZoneDistributionConfig))
      },
      "pscAutoConnections": [
        {
          object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAutoConnection))
        }
      ],
      "pscAttachmentDetails": [
        {
          object ([PscAttachmentDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAttachmentDetail))
        }
      ],
      "endpoints": [
        {
          object ([InstanceEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.InstanceEndpoint))
        }
      ],
      "mode": enum (Mode),
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MaintenanceSchedule))
      },
      "crossInstanceReplicationConfig": {
        object ([CrossInstanceReplicationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.CrossInstanceReplicationConfig))
      },
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.EncryptionInfo))
      },
      "automatedBackupConfig": {
        object ([AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.AutomatedBackupConfig))
      },
      "availableMaintenanceVersions": [
        string
      ],
      "allowFewerZonesDeployment": boolean,
      "migrationConfig": {
        object ([MigrationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MigrationConfig))
      },
    
      // Union field import_sources can be only one of the following:
      "gcsSource": {
        object ([GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.GcsBackupSource))
      },
      "managedBackupSource": {
        object ([ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ManagedBackupSource))
      }
      // End of list of possible types for union field import_sources.
    
      // Union field _replica_count can be only one of the following:
      "replicaCount": integer
      // End of list of possible types for union field _replica_count.
    
      // Union field _deletion_protection_enabled can be only one of the following:
      "deletionProtectionEnabled": boolean
      // End of list of possible types for union field _deletion_protection_enabled.
    
      // Union field _simulate_maintenance_event can be only one of the following:
      "simulateMaintenanceEvent": boolean
      // End of list of possible types for union field _simulate_maintenance_event.
    
      // Union field _ondemand_maintenance can be only one of the following:
      "ondemandMaintenance": boolean
      // End of list of possible types for union field _ondemand_maintenance.
    
      // Union field _satisfies_pzs can be only one of the following:
      "satisfiesPzs": boolean
      // End of list of possible types for union field _satisfies_pzs.
    
      // Union field _satisfies_pzi can be only one of the following:
      "satisfiesPzi": boolean
      // End of list of possible types for union field _satisfies_pzi.
    
      // Union field _async_instance_endpoints_deletion_enabled can be only one of
      // the following:
      "asyncInstanceEndpointsDeletionEnabled": boolean
      // End of list of possible types for union field
      // _async_instance_endpoints_deletion_enabled.
    
      // Union field _kms_key can be only one of the following:
      "kmsKey": string
      // End of list of possible types for union field _kms_key.
    
      // Union field _backup_collection can be only one of the following:
      "backupCollection": string
      // End of list of possible types for union field _backup_collection.
    
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
    
      // Union field _acl_policy can be only one of the following:
      "aclPolicy": string
      // End of list of possible types for union field _acl_policy.
    
      // Union field _acl_policy_in_sync can be only one of the following:
      "aclPolicyInSync": boolean
      // End of list of possible types for union field _acl_policy_in_sync.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the instance. Format: projects/{project}/locations/{location}/instances/{instance}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation timestamp of the instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Latest update timestamp of the instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`State`)` Output only. Current state of the instance.  
`stateInfo` |  `object (`[StateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.StateInfo)`)` Output only. Additional information about the state of the instance.  
`uid` |  `string` Output only. System assigned, unique identifier for the instance.  
`authorizationMode` |  `enum (`AuthorizationMode`)` Optional. Immutable. Authorization mode of the instance.  
`transitEncryptionMode` |  `enum (`TransitEncryptionMode`)` Optional. Immutable. In-transit encryption mode of the instance.  
`shardCount` |  `integer` Optional. Number of shards for the instance.  
`discoveryEndpoints[]  
**(deprecated)**` |  `object (`[DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.DiscoveryEndpoint)`)` This item is deprecated!Output only. Deprecated: The discovery_endpoints parameter is deprecated. As a result, it will not be populated if the connections are created using endpoints parameter. Instead of this parameter, for discovery, use endpoints.connections.pscConnection and endpoints.connections.pscAutoConnection with connectionType CONNECTION_TYPE_DISCOVERY.  
`nodeType` |  `enum (`NodeType`)` Optional. Machine type for individual nodes of the instance.  
`persistenceConfig` |  `object (`[PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PersistenceConfig)`)` Optional. Persistence configuration of the instance.  
`engineVersion` |  `string` Optional. Engine version of the instance.  
`engineConfigs` |  `map (key: string, value: string)` Optional. User-provided engine configurations for the instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.NodeConfig)`)` Output only. Configuration of individual nodes of the instance.  
`zoneDistributionConfig` |  `object (`[ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ZoneDistributionConfig)`)` Optional. Immutable. Zone distribution configuration of the instance for node allocation.  
`pscAutoConnections[]  
**(deprecated)**` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAutoConnection)`)` This item is deprecated!Optional. Immutable. Deprecated: Use the endpoints.connections.psc_auto_connection value instead.  
`pscAttachmentDetails[]` |  `object (`[PscAttachmentDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAttachmentDetail)`)` Output only. Service attachment details to configure PSC connections.  
`endpoints[]` |  `object (`[InstanceEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.InstanceEndpoint)`)` Optional. Endpoints for the instance.  
`mode` |  `enum (`Mode`)` Optional. The mode config for the instance.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MaintenancePolicy)`)` Optional. The maintenance policy for the instance. If not provided, the maintenance event will be performed based on Memorystore internal rollout schedule.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MaintenanceSchedule)`)` Output only. Published maintenance schedule.  
`crossInstanceReplicationConfig` |  `object (`[CrossInstanceReplicationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.CrossInstanceReplicationConfig)`)` Optional. The config for cross instance replication.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.EncryptionInfo)`)` Output only. Encryption information of the data at rest of the cluster.  
`automatedBackupConfig` |  `object (`[AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.AutomatedBackupConfig)`)` Optional. The automated backup config for the instance.  
`availableMaintenanceVersions[]` |  `string` Output only. This field is used to determine the available maintenance versions for the self service update.  
`allowFewerZonesDeployment  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. Deprecated, do not use.  
`migrationConfig` |  `object (`[MigrationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.MigrationConfig)`)` Output only. Migration config for the instance.  
Union field `import_sources`. The source to import from. `import_sources` can be only one of the following:  
`gcsSource` |  `object (`[GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.GcsBackupSource)`)` Optional. Immutable. Backups that stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the instances. Read permission is required to import from the provided Cloud Storage Objects.  
`managedBackupSource` |  `object (`[ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ManagedBackupSource)`)` Optional. Immutable. Backups that generated and managed by memorystore service.  
Union field `_replica_count`.`_replica_count` can be only one of the following:  
`replicaCount` |  `integer` Optional. Number of replica nodes per shard. If omitted the default is 0 replicas.  
Union field `_deletion_protection_enabled`.`_deletion_protection_enabled` can be only one of the following:  
`deletionProtectionEnabled` |  `boolean` Optional. If set to true deletion of the instance will fail.  
Union field `_simulate_maintenance_event`.`_simulate_maintenance_event` can be only one of the following:  
`simulateMaintenanceEvent` |  `boolean` Optional. Input only. Simulate a maintenance event.  
Union field `_ondemand_maintenance`.`_ondemand_maintenance` can be only one of the following:  
`ondemandMaintenance  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Input only. Ondemand maintenance for the instance.  
Union field `_satisfies_pzs`.`_satisfies_pzs` can be only one of the following:  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
Union field `_satisfies_pzi`.`_satisfies_pzi` can be only one of the following:  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
Union field `_async_instance_endpoints_deletion_enabled`.`_async_instance_endpoints_deletion_enabled` can be only one of the following:  
`asyncInstanceEndpointsDeletionEnabled` |  `boolean` Optional. If true, instance endpoints that are created and registered by customers can be deleted asynchronously. That is, such an instance endpoint can be de-registered before the forwarding rules in the instance endpoint are deleted.  
Union field `_kms_key`.`_kms_key` can be only one of the following:  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the at-rest data of the cluster.  
Union field `_backup_collection`.`_backup_collection` can be only one of the following:  
`backupCollection` |  `string` Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}  
Union field `_maintenance_version`.`_maintenance_version` can be only one of the following:  
`maintenanceVersion` |  `string` Optional. This field can be used to trigger self service update to indicate the desired maintenance version. The input to this field can be determined by the available_maintenance_versions field.  
Union field `_effective_maintenance_version`.`_effective_maintenance_version` can be only one of the following:  
`effectiveMaintenanceVersion` |  `string` Output only. This field represents the actual maintenance version of the instance.  
Union field `_server_ca_mode`.`_server_ca_mode` can be only one of the following:  
`serverCaMode` |  `enum (`ServerCaMode`)` Optional. Immutable. The Server CA mode for the instance.  
Union field `_server_ca_pool`.`_server_ca_pool` can be only one of the following:  
`serverCaPool` |  `string` Optional. Immutable. The customer-managed CA pool for the instance. Only applicable if the Server CA mode is CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".  
Union field `_rotate_server_certificate`.`_rotate_server_certificate` can be only one of the following:  
`rotateServerCertificate` |  `boolean` Optional. Input only. Rotate the server certificates.  
Union field `_acl_policy`.`_acl_policy` can be only one of the following:  
`aclPolicy` |  `string` Optional. The ACL policy for the instance. Format: projects/{project}/locations/{location}/aclPolicies/{acl_policy}  
Union field `_acl_policy_in_sync`.`_acl_policy_in_sync` can be only one of the following:  
`aclPolicyInSync` |  `boolean` Output only. Whether the ACL rules applied to the instance are in sync with the latest ACL policy rules. This field is only applicable if the ACL policy is set for the instance.  
  
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
`uris[]` |  `string` Optional. Example: gs://bucket1/object1, gs://bucket2/folder2/object2  
  
### ManagedBackupSource

JSON representation  
---  
      
    
    {
      "backup": string
    }  
  
Fields  
---  
`backup` |  `string` Optional. Example: //memorystore.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup} A shorter version (without the prefix) of the backup name is also supported, like projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup_id} In this case, it assumes the backup is under memorystore.googleapis.com.  
  
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
  
### StateInfo

JSON representation  
---  
      
    
    {
    
      // Union field info can be only one of the following:
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.UpdateInfo))
      }
      // End of list of possible types for union field info.
    }  
  
Fields  
---  
Union field `info`.`info` can be only one of the following:  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.UpdateInfo)`)` Output only. Describes ongoing update when instance state is UPDATING.  
  
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
    
      // Union field _target_engine_version can be only one of the following:
      "targetEngineVersion": string
      // End of list of possible types for union field _target_engine_version.
    
      // Union field _target_node_type can be only one of the following:
      "targetNodeType": enum (NodeType)
      // End of list of possible types for union field _target_node_type.
    }  
  
Fields  
---  
Union field `_target_shard_count`.`_target_shard_count` can be only one of the following:  
`targetShardCount` |  `integer` Output only. Target number of shards for the instance.  
Union field `_target_replica_count`.`_target_replica_count` can be only one of the following:  
`targetReplicaCount` |  `integer` Output only. Target number of replica nodes per shard for the instance.  
Union field `_target_engine_version`.`_target_engine_version` can be only one of the following:  
`targetEngineVersion` |  `string` Output only. Target engine version for the instance.  
Union field `_target_node_type`.`_target_node_type` can be only one of the following:  
`targetNodeType` |  `enum (`NodeType`)` Output only. Target node type for the instance.  
  
### DiscoveryEndpoint

JSON representation  
---  
      
    
    {
      "address": string,
      "port": integer,
      "network": string
    }  
  
Fields  
---  
`address` |  `string` Output only. IP address of the exposed endpoint clients connect to.  
`port` |  `integer` Output only. The port number of the exposed endpoint.  
`network` |  `string` Output only. The network where the IP address of the discovery endpoint will be reserved, in the form of projects/{network_project}/global/networks/{network_id}.  
  
### PersistenceConfig

JSON representation  
---  
      
    
    {
      "mode": enum (PersistenceMode),
      "rdbConfig": {
        object ([RDBConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RDBConfig))
      },
      "aofConfig": {
        object ([AOFConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.AOFConfig))
      }
    }  
  
Fields  
---  
`mode` |  `enum (`PersistenceMode`)` Optional. Current persistence mode.  
`rdbConfig` |  `object (`[RDBConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RDBConfig)`)` Optional. RDB configuration. This field will be ignored if mode is not RDB.  
`aofConfig` |  `object (`[AOFConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.AOFConfig)`)` Optional. AOF configuration. This field will be ignored if mode is not AOF.  
  
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
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### AOFConfig

JSON representation  
---  
      
    
    {
      "appendFsync": enum (AppendFsync)
    }  
  
Fields  
---  
`appendFsync` |  `enum (`AppendFsync`)` Optional. The fsync mode.  
  
### EngineConfigsEntry

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
  
### NodeConfig

JSON representation  
---  
      
    
    {
      "sizeGb": number
    }  
  
Fields  
---  
`sizeGb` |  `number` Output only. Memory size in GB of the node.  
  
### ZoneDistributionConfig

JSON representation  
---  
      
    
    {
      "zone": string,
      "mode": enum (ZoneDistributionMode)
    }  
  
Fields  
---  
`zone` |  `string` Optional. Defines zone where all resources will be allocated with SINGLE_ZONE mode. Ignored for MULTI_ZONE mode.  
`mode` |  `enum (`ZoneDistributionMode`)` Optional. Current zone distribution mode. Defaults to MULTI_ZONE.  
  
### PscAutoConnection

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "ipAddress": string,
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
`pscConnectionId` |  `string` Output only. The PSC connection id of the forwarding rule connected to the service attachment.  
`ipAddress` |  `string` Output only. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Output only. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}  
`projectId` |  `string` Required. The consumer project_id where PSC connections are established. This should be the same project_id that the instance is being created in.  
`network` |  `string` Required. The network where the PSC endpoints are created, in the form of projects/{project_id}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`PscConnectionStatus`)` Output only. The status of the PSC connection: whether a connection exists and ACTIVE or it no longer exists. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of the PSC connection.  
Union field `ports`. Ports of the exposed endpoint. `ports` can be only one of the following:  
`port` |  `integer` Optional. port will only be set for Primary/Reader or Discovery endpoint.  
  
### PscAttachmentDetail

JSON representation  
---  
      
    
    {
      "serviceAttachment": string,
      "connectionType": enum (ConnectionType)
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Output only. Service attachment URI which your self-created PscConnection should use as target.  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of Psc endpoint.  
  
### InstanceEndpoint

JSON representation  
---  
      
    
    {
      "connections": [
        {
          object ([ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ConnectionDetail))
        }
      ]
    }  
  
Fields  
---  
`connections[]` |  `object (`[ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.ConnectionDetail)`)` Optional. A group of PSC connections. They are created in the same VPC network, one for each service attachment in the cluster.  
  
### ConnectionDetail

JSON representation  
---  
      
    
    {
    
      // Union field connection can be only one of the following:
      "pscAutoConnection": {
        object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAutoConnection))
      },
      "pscConnection": {
        object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscConnection))
      }
      // End of list of possible types for union field connection.
    }  
  
Fields  
---  
Union field `connection`. A PSC connection to an instance could either be created through Service Connectivity Automation (auto connection) during the cluster creation, or it could be created by customer themeslves (user-created connection). `connection` can be only one of the following:  
`pscAutoConnection` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscAutoConnection)`)` Immutable. Detailed information of a PSC connection that is created through service connectivity automation.  
`pscConnection` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.PscConnection)`)` Detailed information of a PSC connection that is created by the user.  
  
### PscConnection

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "ipAddress": string,
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
`ipAddress` |  `string` Required. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Required. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}  
`projectId` |  `string` Output only. The consumer project_id where the forwarding rule is created from.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`PscConnectionStatus`)` Output only. The status of the PSC connection: whether a connection exists and ACTIVE or it no longer exists. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`ConnectionType`)` Output only. Type of the PSC connection.  
Union field `ports`. Ports of the exposed endpoint. `ports` can be only one of the following:  
`port` |  `integer` Optional. port will only be set for Primary/Reader or Discovery endpoint.  
  
### MaintenancePolicy

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "weeklyMaintenanceWindow": [
        {
          object ([WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.WeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`weeklyMaintenanceWindow[]` |  `object (`[WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.WeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one.  
  
### WeeklyMaintenanceWindow

JSON representation  
---  
      
    
    {
      "day": enum (google.type.DayOfWeek),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`day` |  `enum (`google.type.DayOfWeek`)` Optional. Allows to define schedule that runs specified day of the week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay)`)` Optional. Start time of the window in UTC.  
  
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
  
### MaintenanceSchedule

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
  
### CrossInstanceReplicationConfig

JSON representation  
---  
      
    
    {
      "instanceRole": enum (InstanceRole),
      "primaryInstance": {
        object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance))
      },
      "secondaryInstances": [
        {
          object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance))
        }
      ],
      "updateTime": string,
      "membership": {
        object ([Membership](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.Membership))
      }
    }  
  
Fields  
---  
`instanceRole` |  `enum (`InstanceRole`)` Required. The role of the instance in cross instance replication.  
`primaryInstance` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance)`)` Optional. Details of the primary instance that is used as the replication source for this secondary instance.This field is only set for a secondary instance.  
`secondaryInstances[]` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance)`)` Optional. List of secondary instances that are replicating from this primary instance.This field is only set for a primary instance.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time cross instance replication config was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.Membership)`)` Output only. An output only view of all the member instances participating in the cross instance replication. This view will be provided by every member instance irrespective of its instance role(primary or secondary).A primary instance can provide information about all the secondary instances replicating from it. However, a secondary instance only knows about the primary instance from which it is replicating. However, for scenarios, where the primary instance is unavailable(e.g. regional outage), a Getinstance request can be sent to any other member instance and this field will list all the member instances participating in cross instance replication.  
  
### RemoteInstance

JSON representation  
---  
      
    
    {
      "instance": string,
      "uid": string
    }  
  
Fields  
---  
`instance` |  `string` Optional. The full resource path of the remote instance in the format: projects//locations//instances/  
`uid` |  `string` Output only. The unique identifier of the remote instance.  
  
### Membership

JSON representation  
---  
      
    
    {
      "primaryInstance": {
        object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance))
      },
      "secondaryInstances": [
        {
          object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance))
        }
      ]
    }  
  
Fields  
---  
`primaryInstance` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance)`)` Output only. The primary instance that acts as the source of replication for the secondary instances.  
`secondaryInstances[]` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.RemoteInstance)`)` Output only. The list of secondary instances replicating from the primary instance.  
  
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
  
### AutomatedBackupConfig

JSON representation  
---  
      
    
    {
      "automatedBackupMode": enum (AutomatedBackupMode),
      "retention": string,
    
      // Union field schedule can be only one of the following:
      "fixedFrequencySchedule": {
        object ([FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.FixedFrequencySchedule))
      }
      // End of list of possible types for union field schedule.
    }  
  
Fields  
---  
`automatedBackupMode` |  `enum (`AutomatedBackupMode`)` Optional. The automated backup mode. If the mode is disabled, the other fields will be ignored.  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to keep automated backups before the backups are deleted. The value should be between 1 day and 365 days. If not specified, the default value is 35 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
Union field `schedule`. The schedule of automated backups. `schedule` can be only one of the following:  
`fixedFrequencySchedule` |  `object (`[FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.FixedFrequencySchedule)`)` Optional. Trigger automated backups at a fixed frequency.  
  
### FixedFrequencySchedule

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay)`)` Required. The start time of every automated backup in UTC. It must be set to the start of an hour. This field is required.  
  
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
  
### MigrationConfig

JSON representation  
---  
      
    
    {
      "state": enum (State),
      "forceFinishMigration": boolean,
    
      // Union field source can be only one of the following:
      "selfManagedSource": {
        object ([SelfManagedSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.SelfManagedSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`state` |  `enum (`State`)` Output only. Migration state of the instance.  
`forceFinishMigration` |  `boolean` Output only. Represents a boolean flag to force migration finalization without offset catch up validation between source and target before stopping replication.  
Union field `source`. Details about the migration source. `source` can be only one of the following:  
`selfManagedSource` |  `object (`[SelfManagedSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/mcp/tools_list/list_instances#Output.Schema.SelfManagedSource)`)` Output only. Configuration for migrating from a self-managed Valkey/Redis instance  
  
### SelfManagedSource

JSON representation  
---  
      
    
    {
      "ipAddress": string,
      "port": integer,
      "networkAttachment": string
    }  
  
Fields  
---  
`ipAddress` |  `string` Required. The IP address of the source instance. This IP address should be a stable IP address that can be accessed by the Memorystore instance throughout the migration process.  
`port` |  `integer` Required. The port of the source instance. This port should be a stable port that can be accessed by the Memorystore instance throughout the migration process.  
`networkAttachment` |  `string` Required. The resource name of the Private Service Connect Network Attachment used to establish connectivity to the source instance. This network attachment has the following requirements: 1. It must be in the same project as the Memorystore instance. 2. It must be in the same region as the Memorystore instance. 3. The subnet attached to the network attachment must be in the same VPC network as the source instance nodes.Format: projects/{project}/regions/{region}/networkAttachments/{network_attachment}  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
