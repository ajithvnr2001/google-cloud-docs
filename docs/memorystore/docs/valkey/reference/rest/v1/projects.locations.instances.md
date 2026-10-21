---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:28.597987+00:00
---

# REST Resource: projects.locations.instances  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * GcsBackupSource
    * JSON representation
  * ManagedBackupSource
    * JSON representation
  * State
  * StateInfo
    * JSON representation
  * UpdateInfo
    * JSON representation
  * AuthorizationMode
  * TransitEncryptionMode
  * DiscoveryEndpoint
    * JSON representation
  * PersistenceConfig
    * JSON representation
  * PersistenceMode
  * RDBConfig
    * JSON representation
  * SnapshotPeriod
  * AOFConfig
    * JSON representation
  * AppendFsync
  * NodeConfig
    * JSON representation
  * ZoneDistributionConfig
    * JSON representation
  * ZoneDistributionMode
  * PscAutoConnection
    * JSON representation
  * PscConnectionStatus
  * ConnectionType
  * PscAttachmentDetail
    * JSON representation
  * InstanceEndpoint
    * JSON representation
  * ConnectionDetail
    * JSON representation
  * PscConnection
    * JSON representation
  * Mode
  * MaintenancePolicy
    * JSON representation
  * WeeklyMaintenanceWindow
    * JSON representation
  * MaintenanceSchedule
    * JSON representation
  * CrossInstanceReplicationConfig
    * JSON representation
  * InstanceRole
  * RemoteInstance
    * JSON representation
  * Membership
    * JSON representation
  * AutomatedBackupConfig
    * JSON representation
  * FixedFrequencySchedule
    * JSON representation
  * AutomatedBackupMode
  * ServerCaMode
  * MigrationConfig
    * JSON representation
  * SelfManagedSource
    * JSON representation
  * State
  * AclPolicyInfo
    * JSON representation
  * Methods



## Resource: Instance

A Memorystore instance.

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
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#State)),
      "stateInfo": {
        object ([StateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#StateInfo))
      },
      "uid": string,
      "authorizationMode": enum ([AuthorizationMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AuthorizationMode)),
      "transitEncryptionMode": enum ([TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#TransitEncryptionMode)),
      "shardCount": integer,
      "discoveryEndpoints": [
        {
          object ([DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#DiscoveryEndpoint))
        }
      ],
      "nodeType": enum ([NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/NodeType)),
      "persistenceConfig": {
        object ([PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceConfig))
      },
      "engineVersion": string,
      "engineConfigs": {
        string: string,
        ...
      },
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#NodeConfig))
      },
      "zoneDistributionConfig": {
        object ([ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionConfig))
      },
      "pscAutoConnections": [
        {
          object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAutoConnection))
        }
      ],
      "pscAttachmentDetails": [
        {
          object ([PscAttachmentDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAttachmentDetail))
        }
      ],
      "endpoints": [
        {
          object ([InstanceEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#InstanceEndpoint))
        }
      ],
      "mode": enum ([Mode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Mode)),
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MaintenanceSchedule))
      },
      "crossInstanceReplicationConfig": {
        object ([CrossInstanceReplicationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#CrossInstanceReplicationConfig))
      },
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/EncryptionInfo))
      },
      "automatedBackupConfig": {
        object ([AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AutomatedBackupConfig))
      },
      "availableMaintenanceVersions": [
        string
      ],
      "allowFewerZonesDeployment": boolean,
      "migrationConfig": {
        object ([MigrationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MigrationConfig))
      },
      "aclPolicyInfo": {
        object ([AclPolicyInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AclPolicyInfo))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#GcsBackupSource))
      },
      "managedBackupSource": {
        object ([ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ManagedBackupSource))
      }
      // End of mutually exclusive fields.
      "replicaCount": integer,
      "deletionProtectionEnabled": boolean,
      "simulateMaintenanceEvent": boolean,
      "ondemandMaintenance": boolean,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
      "asyncInstanceEndpointsDeletionEnabled": boolean,
      "kmsKey": string,
      "backupCollection": string,
      "maintenanceVersion": string,
      "effectiveMaintenanceVersion": string,
      "serverCaMode": enum ([ServerCaMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ServerCaMode)),
      "serverCaPool": string,
      "rotateServerCertificate": boolean,
      "aclPolicy": string,
      "aclPolicyInSync": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the instance. Format: projects/{project}/locations/{location}/instances/{instance}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation timestamp of the instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Latest update timestamp of the instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#State)`)` Output only. Current state of the instance.  
`stateInfo` |  `object (`[StateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#StateInfo)`)` Output only. Additional information about the state of the instance.  
`uid` |  `string` Output only. System assigned, unique identifier for the instance.  
`authorizationMode` |  `enum (`[AuthorizationMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AuthorizationMode)`)` Optional. Authorization mode of the instance.  
`transitEncryptionMode` |  `enum (`[TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#TransitEncryptionMode)`)` Optional. Immutable. In-transit encryption mode of the instance.  
`shardCount` |  `integer` Optional. Number of shards for the instance.  
`discoveryEndpoints[]  
**(deprecated)**` |  `object (`[DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#DiscoveryEndpoint)`)` This item is deprecated!Output only. Deprecated: The discoveryEndpoints parameter is deprecated. As a result, it will not be populated if the connections are created using endpoints parameter. Instead of this parameter, for discovery, use endpoints.connections.pscConnection and endpoints.connections.pscAutoConnection with connectionType CONNECTION_TYPE_DISCOVERY.  
`nodeType` |  `enum (`[NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/NodeType)`)` Optional. Machine type for individual nodes of the instance.  
`persistenceConfig` |  `object (`[PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceConfig)`)` Optional. Persistence configuration of the instance.  
`engineVersion` |  `string` Optional. Engine version of the instance.  
`engineConfigs` |  `map (key: string, value: string)` Optional. User-provided engine configurations for the instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#NodeConfig)`)` Output only. Configuration of individual nodes of the instance.  
`zoneDistributionConfig` |  `object (`[ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionConfig)`)` Optional. Immutable. Zone distribution configuration of the instance for node allocation.  
`pscAutoConnections[]  
**(deprecated)**` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAutoConnection)`)` This item is deprecated!Optional. Immutable. Deprecated: Use the endpoints.connections.psc_auto_connection value instead.  
`pscAttachmentDetails[]` |  `object (`[PscAttachmentDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAttachmentDetail)`)` Output only. Service attachment details to configure PSC connections.  
`endpoints[]` |  `object (`[InstanceEndpoint](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#InstanceEndpoint)`)` Optional. Endpoints for the instance.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Mode)`)` Optional. Immutable. The mode config for the instance.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MaintenancePolicy)`)` Optional. The maintenance policy for the instance. If not provided, the maintenance event will be performed based on Memorystore internal rollout schedule.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MaintenanceSchedule)`)` Output only. Published maintenance schedule.  
`crossInstanceReplicationConfig` |  `object (`[CrossInstanceReplicationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#CrossInstanceReplicationConfig)`)` Optional. The config for cross instance replication.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/EncryptionInfo)`)` Output only. Encryption information of the data at rest of the cluster.  
`automatedBackupConfig` |  `object (`[AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AutomatedBackupConfig)`)` Optional. The automated backup config for the instance.  
`availableMaintenanceVersions[]` |  `string` Output only. This field is used to determine the available maintenance versions for the self service update.  
`allowFewerZonesDeployment  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. Deprecated, do not use.  
`migrationConfig` |  `object (`[MigrationConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#MigrationConfig)`)` Output only. Migration config for the instance.  
`aclPolicyInfo` |  `object (`[AclPolicyInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AclPolicyInfo)`)` Output only. Details of the applied ACL policy.  
The source to import from. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#GcsBackupSource)`)` Optional. Immutable. Backups that stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the instances. Read permission is required to import from the provided Cloud Storage Objects.  
`managedBackupSource` |  `object (`[ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ManagedBackupSource)`)` Optional. Immutable. Backups that generated and managed by memorystore service.  
End of mutually exclusive fields.  
`replicaCount` |  `integer` Optional. Number of replica nodes per shard. If omitted the default is 0 replicas.  
`deletionProtectionEnabled` |  `boolean` Optional. If set to true deletion of the instance will fail.  
`simulateMaintenanceEvent` |  `boolean` Optional. Input only. Simulate a maintenance event.  
`ondemandMaintenance  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Input only. Ondemand maintenance for the instance.  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
`asyncInstanceEndpointsDeletionEnabled` |  `boolean` Optional. If true, instance endpoints that are created and registered by customers can be deleted asynchronously. That is, such an instance endpoint can be de-registered before the forwarding rules in the instance endpoint are deleted.  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the at-rest data of the cluster.  
`backupCollection` |  `string` Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}  
`maintenanceVersion` |  `string` Optional. This field can be used to trigger self service update to indicate the desired maintenance version. The input to this field can be determined by the availableMaintenanceVersions field.  
`effectiveMaintenanceVersion` |  `string` Output only. This field represents the actual maintenance version of the instance.  
`serverCaMode` |  `enum (`[ServerCaMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ServerCaMode)`)` Optional. Immutable. The Server CA mode for the instance.  
`serverCaPool` |  `string` Optional. Immutable. The customer-managed CA pool for the instance. Only applicable if the Server CA mode is CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".  
`rotateServerCertificate` |  `boolean` Optional. Input only. Rotate the server certificates.  
`aclPolicy` |  `string` Optional. The ACL policy for the instance. Format: projects/{project}/locations/{location}/aclPolicies/{aclPolicy}  
`aclPolicyInSync  
**(deprecated)**` |  `boolean` This item is deprecated!Output only. Deprecated: Whether the ACL rules applied to the instance are in sync.  
  
## GcsBackupSource

Backups that stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the instances.

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
  
## ManagedBackupSource

Backups that generated and managed by memorystore.

JSON representation  
---  
      
    
    {
      "backup": string
    }  
  
Fields  
---  
`backup` |  `string` Optional. Example: //memorystore.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup} A shorter version (without the prefix) of the backup name is also supported, like projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backupId} In this case, it assumes the backup is under memorystore.googleapis.com.  
  
## State

Possible states of the instance.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | Instance is being created.  
`ACTIVE` | Instance has been created and is usable.  
`UPDATING` | Instance is being updated.  
`DELETING` | Instance is being deleted.  
`MIGRATING` | Instance is being migrated.  
  
## StateInfo

Additional information about the state of the instance.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#UpdateInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#UpdateInfo)`)` Output only. Describes ongoing update when instance state is UPDATING.  
End of mutually exclusive fields.  
  
## UpdateInfo

Represents information about instance with state UPDATING.

JSON representation  
---  
      
    
    {
      "targetShardCount": integer,
      "targetReplicaCount": integer,
      "targetEngineVersion": string,
      "targetNodeType": enum ([NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/NodeType))
    }  
  
Fields  
---  
`targetShardCount` |  `integer` Output only. Target number of shards for the instance.  
`targetReplicaCount` |  `integer` Output only. Target number of replica nodes per shard for the instance.  
`targetEngineVersion` |  `string` Output only. Target engine version for the instance.  
`targetNodeType` |  `enum (`[NodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/NodeType)`)` Output only. Target node type for the instance.  
  
## AuthorizationMode

Possible authorization modes of the instance.

Enums  
---  
`AUTHORIZATION_MODE_UNSPECIFIED` | Not set.  
`AUTH_DISABLED` | Authorization disabled.  
`IAM_AUTH` | IAM basic authorization.  
`TOKEN_AUTH` | Token based authorization.  
  
## TransitEncryptionMode

Possible in-transit encryption modes of the instance.

Enums  
---  
`TRANSIT_ENCRYPTION_MODE_UNSPECIFIED` | Not set.  
`TRANSIT_ENCRYPTION_DISABLED` | In-transit encryption is disabled.  
`SERVER_AUTHENTICATION` | Server-managed encryption is used for in-transit encryption.  
  
## DiscoveryEndpoint

Represents an endpoint for clients to connect to the instance.

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
`network` |  `string` Output only. The network where the IP address of the discovery endpoint will be reserved, in the form of projects/{networkProject}/global/networks/{network_name}.  
  
## PersistenceConfig

Represents persistence configuration for a instance.

JSON representation  
---  
      
    
    {
      "mode": enum ([PersistenceMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceMode)),
      "rdbConfig": {
        object ([RDBConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RDBConfig))
      },
      "aofConfig": {
        object ([AOFConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AOFConfig))
      }
    }  
  
Fields  
---  
`mode` |  `enum (`[PersistenceMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceMode)`)` Optional. Current persistence mode.  
`rdbConfig` |  `object (`[RDBConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RDBConfig)`)` Optional. RDB configuration. This field will be ignored if mode is not RDB.  
`aofConfig` |  `object (`[AOFConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AOFConfig)`)` Optional. AOF configuration. This field will be ignored if mode is not AOF.  
  
## PersistenceMode

Possible persistence modes.

Enums  
---  
`PERSISTENCE_MODE_UNSPECIFIED` | Not set.  
`DISABLED` | Persistence is disabled, and any snapshot data is deleted.  
`RDB` | RDB based persistence is enabled.  
`AOF` | AOF based persistence is enabled.  
  
## RDBConfig

Configuration for RDB based persistence.

JSON representation  
---  
      
    
    {
      "rdbSnapshotPeriod": enum ([SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#SnapshotPeriod)),
      "rdbSnapshotStartTime": string
    }  
  
Fields  
---  
`rdbSnapshotPeriod` |  `enum (`[SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#SnapshotPeriod)`)` Optional. Period between RDB snapshots.  
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SnapshotPeriod

Possible snapshot periods.

Enums  
---  
`SNAPSHOT_PERIOD_UNSPECIFIED` | Not set.  
`ONE_HOUR` | One hour.  
`SIX_HOURS` | Six hours.  
`TWELVE_HOURS` | Twelve hours.  
`TWENTY_FOUR_HOURS` | Twenty four hours.  
  
## AOFConfig

Configuration for AOF based persistence.

JSON representation  
---  
      
    
    {
      "appendFsync": enum ([AppendFsync](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AppendFsync))
    }  
  
Fields  
---  
`appendFsync` |  `enum (`[AppendFsync](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AppendFsync)`)` Optional. The fsync mode.  
  
## AppendFsync

Possible fsync modes.

Enums  
---  
`APPEND_FSYNC_UNSPECIFIED` | Not set. Default: EVERY_SEC  
`NEVER` | Never fsync. Normally Linux will flush data every 30 seconds with this configuration, but it's up to the kernel's exact tuning.  
`EVERY_SEC` | Fsync every second. You may lose 1 second of data if there is a disaster.  
`ALWAYS` | Fsync every time new write commands are appended to the AOF. The best data loss protection at the cost of performance.  
  
## NodeConfig

Represents configuration for nodes of the instance.

JSON representation  
---  
      
    
    {
      "sizeGb": number
    }  
  
Fields  
---  
`sizeGb` |  `number` Output only. Memory size in GB of the node.  
  
## ZoneDistributionConfig

Zone distribution configuration for allocation of instance resources.

JSON representation  
---  
      
    
    {
      "zone": string,
      "zones": [
        string
      ],
      "mode": enum ([ZoneDistributionMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionMode))
    }  
  
Fields  
---  
`zone` |  `string` Optional. Defines zone where all resources will be allocated with SINGLE_ZONE mode. Ignored for MULTI_ZONE mode.  
`zones[]` |  `string` Optional. Specify the zones of a multi-zone instance where Memorystore instance allocates resources. This flag isn't applicable for single-zone instances.  
`mode` |  `enum (`[ZoneDistributionMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionMode)`)` Optional. Current zone distribution mode. Defaults to MULTI_ZONE.  
  
## ZoneDistributionMode

Possible zone distribution modes.

Enums  
---  
`ZONE_DISTRIBUTION_MODE_UNSPECIFIED` | Not Set. Default: MULTI_ZONE  
`MULTI_ZONE` | Distribute resources across 3 zones picked at random within the region.  
`SINGLE_ZONE` | Provision resources in a single zone. Zone field must be specified.  
  
## PscAutoConnection

Details of consumer resources in a PSC connection.

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "ipAddress": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum ([PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnectionStatus)),
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "port": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Output only. The PSC connection id of the forwarding rule connected to the service attachment.  
`ipAddress` |  `string` Output only. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Output only. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwardingRule}  
`projectId` |  `string` Required. The consumer projectId where PSC connections are established. This should be the same projectId that the instance is being created in.  
`network` |  `string` Required. The network where the PSC endpoints are created, in the form of projects/{projectId}/global/networks/{network_name}.  
`serviceAttachment` |  `string` Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`[PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnectionStatus)`)` Output only. The status of the PSC connection: whether a connection exists and ACTIVE or it no longer exists. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType)`)` Output only. Type of the PSC connection.  
Ports of the exposed endpoint. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`port` |  `integer` Optional. port will only be set for Primary/Reader or Discovery endpoint.  
End of mutually exclusive fields.  
  
## PscConnectionStatus

Status of the PSC connection.

Enums  
---  
`PSC_CONNECTION_STATUS_UNSPECIFIED` | PSC connection status is not specified.  
`ACTIVE` | The connection is active  
`NOT_FOUND` | Connection not found  
  
## ConnectionType

Type of a PSC connection

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | Connection Type is not set  
`CONNECTION_TYPE_DISCOVERY` | Connection that will be used for topology discovery.  
`CONNECTION_TYPE_PRIMARY` | Connection that will be used as primary endpoint to access primary.  
`CONNECTION_TYPE_READER` | Connection that will be used as reader endpoint to access replicas.  
  
## PscAttachmentDetail

Configuration of a service attachment of the cluster, for creating PSC connections.

JSON representation  
---  
      
    
    {
      "serviceAttachment": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType))
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Output only. Service attachment URI which your self-created PscConnection should use as target.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType)`)` Output only. Type of Psc endpoint.  
  
## InstanceEndpoint

InstanceEndpoint consists of PSC connections that are created as a group in each VPC network for accessing the instance. In each group, there shall be one connection for each service attachment in the cluster.

JSON representation  
---  
      
    
    {
      "connections": [
        {
          object ([ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionDetail))
        }
      ]
    }  
  
Fields  
---  
`connections[]` |  `object (`[ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionDetail)`)` Optional. A group of PSC connections. They are created in the same VPC network, one for each service attachment in the cluster.  
  
## ConnectionDetail

Information of each PSC connection.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "pscAutoConnection": {
        object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAutoConnection))
      },
      "pscConnection": {
        object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnection))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A PSC connection to an instance could either be created through Service Connectivity Automation (auto connection) during the cluster creation, or it could be created by customer themeslves (user-created connection). The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`pscAutoConnection` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscAutoConnection)`)` Immutable. Detailed information of a PSC connection that is created through service connectivity automation.  
`pscConnection` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnection)`)` Detailed information of a PSC connection that is created by the user.  
End of mutually exclusive fields.  
  
## PscConnection

User created Psc connection configuration.

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "ipAddress": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum ([PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnectionStatus)),
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "port": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Required. The PSC connection id of the forwarding rule connected to the service attachment.  
`ipAddress` |  `string` Required. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Required. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwardingRule}  
`projectId` |  `string` Output only. The consumer projectId where the forwarding rule is created from.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{projectId}/global/networks/{network_name}.  
`serviceAttachment` |  `string` Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`[PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConnectionStatus)`)` Output only. The status of the PSC connection: whether a connection exists and ACTIVE or it no longer exists. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ConnectionType)`)` Output only. Type of the PSC connection.  
Ports of the exposed endpoint. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`port` |  `integer` Optional. port will only be set for Primary/Reader or Discovery endpoint.  
End of mutually exclusive fields.  
  
## Mode

The mode config, which is used to enable/disable cluster mode.

Enums  
---  
`MODE_UNSPECIFIED` | Mode is not specified.  
`STANDALONE` | Deprecated: Use CLUSTER_DISABLED instead.This item is deprecated!  
`CLUSTER` | Instance is in cluster mode.  
`CLUSTER_DISABLED` | Cluster mode is disabled for the instance.  
  
## MaintenancePolicy

Maintenance policy per instance.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "weeklyMaintenanceWindow": [
        {
          object ([WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`weeklyMaintenanceWindow[]` |  `object (`[WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one.  
  
## WeeklyMaintenanceWindow

Time window specified for weekly operations.

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay))
      }
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/DayOfWeek)`)` Optional. Allows to define schedule that runs specified day of the week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay)`)` Optional. Start time of the window in UTC.  
  
## MaintenanceSchedule

Upcoming maintenance schedule.

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
  
## CrossInstanceReplicationConfig

Cross instance replication config.

JSON representation  
---  
      
    
    {
      "instanceRole": enum ([InstanceRole](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#InstanceRole)),
      "primaryInstance": {
        object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance))
      },
      "secondaryInstances": [
        {
          object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance))
        }
      ],
      "updateTime": string,
      "membership": {
        object ([Membership](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Membership))
      }
    }  
  
Fields  
---  
`instanceRole` |  `enum (`[InstanceRole](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#InstanceRole)`)` Required. The role of the instance in cross instance replication.  
`primaryInstance` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance)`)` Optional. Details of the primary instance that is used as the replication source for this secondary instance.This field is only set for a secondary instance.  
`secondaryInstances[]` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance)`)` Optional. List of secondary instances that are replicating from this primary instance.This field is only set for a primary instance.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time cross instance replication config was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Membership)`)` Output only. An output only view of all the member instances participating in the cross instance replication. This view will be provided by every member instance irrespective of its instance role(primary or secondary).A primary instance can provide information about all the secondary instances replicating from it. However, a secondary instance only knows about the primary instance from which it is replicating. However, for scenarios, where the primary instance is unavailable(e.g. regional outage), a Getinstance request can be sent to any other member instance and this field will list all the member instances participating in cross instance replication.  
  
## InstanceRole

The role of the instance in cross instance replication.

Enums  
---  
`INSTANCE_ROLE_UNSPECIFIED` | instance role is not set. The behavior is equivalent to NONE.  
`NONE` | This instance does not participate in cross instance replication. It is an independent instance and does not replicate to or from any other instances.  
`PRIMARY` | A instance that allows both reads and writes. Any data written to this instance is also replicated to the attached secondary instances.  
`SECONDARY` | A instance that allows only reads and replicates data from a primary instance.  
  
## RemoteInstance

Details of the remote instance associated with this instance in a cross instance replication setup.

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
  
## Membership

An output only view of all the member instances participating in the cross instance replication.

JSON representation  
---  
      
    
    {
      "primaryInstance": {
        object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance))
      },
      "secondaryInstances": [
        {
          object ([RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance))
        }
      ]
    }  
  
Fields  
---  
`primaryInstance` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance)`)` Output only. The primary instance that acts as the source of replication for the secondary instances.  
`secondaryInstances[]` |  `object (`[RemoteInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RemoteInstance)`)` Output only. The list of secondary instances replicating from the primary instance.  
  
## AutomatedBackupConfig

The automated backup config for an instance.

JSON representation  
---  
      
    
    {
      "automatedBackupMode": enum ([AutomatedBackupMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AutomatedBackupMode)),
      "retention": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "fixedFrequencySchedule": {
        object ([FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#FixedFrequencySchedule))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`automatedBackupMode` |  `enum (`[AutomatedBackupMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#AutomatedBackupMode)`)` Optional. The automated backup mode. If the mode is disabled, the other fields will be ignored.  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to keep automated backups before the backups are deleted. The value should be between 1 day and 365 days. If not specified, the default value is 35 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
The schedule of automated backups. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`fixedFrequencySchedule` |  `object (`[FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#FixedFrequencySchedule)`)` Optional. Trigger automated backups at a fixed frequency.  
End of mutually exclusive fields.  
  
## FixedFrequencySchedule

This schedule allows the backup to be triggered at a fixed frequency (currently only daily is supported).

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay))
      }
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay)`)` Required. The start time of every automated backup in UTC. It must be set to the start of an hour. This field is required.  
  
## AutomatedBackupMode

The automated backup mode.

Enums  
---  
`AUTOMATED_BACKUP_MODE_UNSPECIFIED` | Default value. Automated backup config is not specified.  
`DISABLED` | Automated backup config disabled.  
`ENABLED` | Automated backup config enabled.  
  
## ServerCaMode

The Server CA mode for the instance.

Enums  
---  
`SERVER_CA_MODE_UNSPECIFIED` | Server CA mode not specified.  
`GOOGLE_MANAGED_PER_INSTANCE_CA` | Each instance has its own Google-managed CA.  
`GOOGLE_MANAGED_SHARED_CA` | The instance uses a Google-managed shared CA for the instance's region.  
`CUSTOMER_MANAGED_CAS_CA` | The instance uses a customer-managed CA from CAS.  
`SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA` | Deprecated: Use GOOGLE_MANAGED_PER_INSTANCE_CA instead.This item is deprecated!  
`SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA` | Deprecated: Use GOOGLE_MANAGED_SHARED_CA instead.This item is deprecated!  
`SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA` | Deprecated: Use CUSTOMER_MANAGED_CAS_CA instead.This item is deprecated!  
  
## MigrationConfig

Configuration for the migration of an instance.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#State_1)),
      "forceFinishMigration": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "selfManagedSource": {
        object ([SelfManagedSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#SelfManagedSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#State_1)`)` Output only. Migration state of the instance.  
`forceFinishMigration` |  `boolean` Output only. Represents a boolean flag to force migration finalization without offset catch up validation between source and target before stopping replication.  
Details about the migration source. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`selfManagedSource` |  `object (`[SelfManagedSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#SelfManagedSource)`)` Output only. Configuration for migrating from a self-managed Valkey/Redis instance  
End of mutually exclusive fields.  
  
## SelfManagedSource

Details of the self-managed source instance.

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
`networkAttachment` |  `string` Required. The resource name of the Private Service Connect Network Attachment used to establish connectivity to the source instance. This network attachment has the following requirements: 1. It must be in the same project as the Memorystore instance. 2. It must be in the same region as the Memorystore instance. 3. The subnet attached to the network attachment must be in the same VPC network as the source instance nodes.Format: projects/{project}/regions/{region}/networkAttachments/{networkAttachment}  
  
## State

Migration state of the instance. New values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | Instance has no migration related activity. This is the initial state.  
`ROLLED_BACK` | Instance is not currently migrating. The instance underwent a migration attempt that failed, and the subsequent rollback was successful. The instance is now ready for a new migration attempt if desired.  
`ROLLING_BACK` | Indicates a previous migration attempt failed. The high-level instance state will be `MIGRATING`. The instance is not ready for a new migration attempt. Rollback is in progress to restore the instance to its original state. The instance will remain in this state until rollback is successful.  
`REPLICATION_ESTABLISHED` | Instance is in the process of migration. Instance has established successful replication and is ready for cutover.  
`MIGRATED` | Instance is successfully migrated.  
  
## AclPolicyInfo

Details of the applied ACL policy.

JSON representation  
---  
      
    
    {
      "appliedAclPolicy": string,
      "appliedAclPolicyRevision": string,
      "appliedAclPolicyRevisionNumber": string,
      "aclPolicyRevisionStatuses": [
        {
          object ([AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus))
        }
      ]
    }  
  
Fields  
---  
`appliedAclPolicy` |  `string` Output only. The resource name of the applied ACL policy. Format: "projects/{project}/locations/{location}/aclPolicies/{aclPolicy}"  
`appliedAclPolicyRevision` |  `string` Output only. The resource name of the applied ACL policy revision. Format: "projects/{project}/locations/{location}/aclPolicies/{aclPolicy}/revisions/{revision}"  
`appliedAclPolicyRevisionNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The revision number of the applied ACL policy revision.  
`aclPolicyRevisionStatuses[]` |  `object (`[AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/AclPolicyRevisionStatus)`)` Output only. A list of status for various revisions of this ACL policy on the instance.  
  
## Methods  
  
---  
  
### `[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/addTokenAuthUser)`

|  Adds a token auth user for a token based auth enabled instance.  
  
### `[backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/backup)`

|  Backup Instance.  
  
### `[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/create)`

|  Creates a new Instance in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/delete)`

|  Deletes a single Instance.  
  
### `[finishMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/finishMigration)`

|  Finalizes the migration process.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/get)`

|  Gets details of a single Instance.  
  
### `[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority)`

|  Gets details about the certificate authority for an Instance.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/list)`

|  Lists Instances in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/patch)`

|  Updates the parameters of a single Instance.  
  
### `[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/rescheduleMaintenance)`

|  Reschedules upcoming maintenance event.  
  
### `[startMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/startMigration)`

|  Initiates the migration of a source instance to the target Memorystore instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
