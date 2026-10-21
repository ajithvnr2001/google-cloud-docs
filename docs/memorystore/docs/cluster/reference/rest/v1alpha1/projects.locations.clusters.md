---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters
title: REST Resource: projects.locations.clusters \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:49.865337+00:00
---

# REST Resource: projects.locations.clusters  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.clusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Cluster
    * JSON representation
  * GcsBackupSource
    * JSON representation
  * ManagedBackupSource
    * JSON representation
  * State
  * AuthorizationMode
  * TransitEncryptionMode
  * PscConfig
    * JSON representation
  * DiscoveryEndpoint
    * JSON representation
  * PscConnection
    * JSON representation
  * PscConnectionStatus
  * ConnectionType
  * StateInfo
    * JSON representation
  * UpdateInfo
    * JSON representation
  * ClusterPersistenceConfig
    * JSON representation
  * PersistenceMode
  * RDBConfig
    * JSON representation
  * SnapshotPeriod
  * AOFConfig
    * JSON representation
  * AppendFsync
  * ZoneDistributionConfig
    * JSON representation
  * ZoneDistributionMode
  * CrossClusterReplicationConfig
    * JSON representation
  * ClusterRole
  * RemoteCluster
    * JSON representation
  * Membership
    * JSON representation
  * ClusterMaintenancePolicy
    * JSON representation
  * ClusterWeeklyMaintenanceWindow
    * JSON representation
  * ClusterMaintenanceSchedule
    * JSON representation
  * PscServiceAttachment
    * JSON representation
  * ClusterEndpoint
    * JSON representation
  * ConnectionDetail
    * JSON representation
  * PscAutoConnection
    * JSON representation
  * AutomatedBackupConfig
    * JSON representation
  * FixedFrequencySchedule
    * JSON representation
  * AutomatedBackupMode
  * ServerCaMode
  * AclPolicyInfo
    * JSON representation
  * Methods



## Resource: Cluster

A cluster instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#State)),
      "uid": string,
      "authorizationMode": enum ([AuthorizationMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AuthorizationMode)),
      "transitEncryptionMode": enum ([TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#TransitEncryptionMode)),
      "pscConfigs": [
        {
          object ([PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConfig))
        }
      ],
      "discoveryEndpoints": [
        {
          object ([DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#DiscoveryEndpoint))
        }
      ],
      "pscConnections": [
        {
          object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnection))
        }
      ],
      "stateInfo": {
        object ([StateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#StateInfo))
      },
      "nodeType": enum ([NodeType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/NodeType)),
      "persistenceConfig": {
        object ([ClusterPersistenceConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterPersistenceConfig))
      },
      "redisConfigs": {
        string: string,
        ...
      },
      "zoneDistributionConfig": {
        object ([ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ZoneDistributionConfig))
      },
      "crossClusterReplicationConfig": {
        object ([CrossClusterReplicationConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#CrossClusterReplicationConfig))
      },
      "pscServiceAttachments": [
        {
          object ([PscServiceAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscServiceAttachment))
        }
      ],
      "clusterEndpoints": [
        {
          object ([ClusterEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterEndpoint))
        }
      ],
      "automatedBackupConfig": {
        object ([AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AutomatedBackupConfig))
      },
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/EncryptionInfo))
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
      "aclPolicyInfo": {
        object ([AclPolicyInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AclPolicyInfo))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#GcsBackupSource))
      },
      "managedBackupSource": {
        object ([ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ManagedBackupSource))
      }
      // End of mutually exclusive fields.
      "replicaCount": integer,
      "sizeGb": integer,
      "shardCount": integer,
      "preciseSizeGb": number,
      "deletionProtectionEnabled": boolean,
      "maintenancePolicy": {
        object ([ClusterMaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterMaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([ClusterMaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterMaintenanceSchedule))
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
      "simulateMaintenanceEvent": boolean,
      "backupCollection": string,
      "kmsKey": string,
      "ondemandMaintenance": boolean,
      "asyncClusterEndpointsDeletionEnabled": boolean,
      "maintenanceVersion": string,
      "effectiveMaintenanceVersion": string,
      "serverCaMode": enum ([ServerCaMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ServerCaMode)),
      "serverCaPool": string,
      "rotateServerCertificate": boolean,
      "aclPolicyInSync": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{projectId}/locations/{locationId}/clusters/{clusterId}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp associated with the cluster creation request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#State)`)` Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED  
`uid` |  `string` Output only. System assigned, unique identifier for the cluster.  
`authorizationMode` |  `enum (`[AuthorizationMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AuthorizationMode)`)` Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster.  
`transitEncryptionMode` |  `enum (`[TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#TransitEncryptionMode)`)` Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster.  
`pscConfigs[]` |  `object (`[PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConfig)`)` Optional. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported.  
`discoveryEndpoints[]` |  `object (`[DiscoveryEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#DiscoveryEndpoint)`)` Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported.  
`pscConnections[]` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnection)`)` Output only. The list of PSC connections that are auto-created through service connectivity automation.  
`stateInfo` |  `object (`[StateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#StateInfo)`)` Output only. Additional information about the current state of the cluster.  
`nodeType` |  `enum (`[NodeType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/NodeType)`)` Optional. The type of a redis node in the cluster. NodeType determines the underlying machine-type of a redis node.  
`persistenceConfig` |  `object (`[ClusterPersistenceConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterPersistenceConfig)`)` Optional. Persistence config (RDB, AOF) for the cluster.  
`redisConfigs` |  `map (key: string, value: string)` Optional. Key/Value pairs of customer overrides for mutable Redis ConfigsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`zoneDistributionConfig` |  `object (`[ZoneDistributionConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ZoneDistributionConfig)`)` Optional. This config will be used to determine how the customer wants us to distribute cluster resources within the region.  
`crossClusterReplicationConfig` |  `object (`[CrossClusterReplicationConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#CrossClusterReplicationConfig)`)` Optional. Cross cluster replication config.  
`pscServiceAttachments[]` |  `object (`[PscServiceAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscServiceAttachment)`)` Output only. Service attachment details to configure Psc connections  
`clusterEndpoints[]` |  `object (`[ClusterEndpoint](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterEndpoint)`)` Optional. A list of cluster endpoints.  
`automatedBackupConfig` |  `object (`[AutomatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AutomatedBackupConfig)`)` Optional. The automated backup config for the cluster.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/EncryptionInfo)`)` Output only. Encryption information of the data at rest of the cluster.  
`availableMaintenanceVersions[]` |  `string` Output only. This field is used to determine the available maintenance versions for the self service update.  
`allowFewerZonesDeployment  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. Deprecated, do not use.  
`labels` |  `map (key: string, value: string)` Optional. Labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`aclPolicy` |  `string` Optional. The ACL policy to be applied to the cluster.  
`aclPolicyInfo` |  `object (`[AclPolicyInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AclPolicyInfo)`)` Output only. Details of the applied ACL policy.  
The source to import from. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#GcsBackupSource)`)` Optional. Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters. Read permission is required to import from the provided Cloud Storage objects.  
`managedBackupSource` |  `object (`[ManagedBackupSource](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ManagedBackupSource)`)` Optional. Backups generated and managed by memorystore service.  
End of mutually exclusive fields.  
`replicaCount` |  `integer` Optional. The number of replica nodes per shard.  
`sizeGb` |  `integer` Output only. Redis memory size in GB for the entire cluster rounded up to the next integer.  
`shardCount` |  `integer` Optional. Number of shards for the Redis cluster.  
`preciseSizeGb` |  `number` Output only. Precise value of redis memory size in GB for the entire cluster.  
`deletionProtectionEnabled` |  `boolean` Optional. The delete operation will fail when the value is set to true.  
`maintenancePolicy` |  `object (`[ClusterMaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterMaintenancePolicy)`)` Optional. ClusterMaintenancePolicy determines when to allow or deny updates.  
`maintenanceSchedule` |  `object (`[ClusterMaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterMaintenanceSchedule)`)` Output only. ClusterMaintenanceSchedule Output only Published maintenance schedule.  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
`simulateMaintenanceEvent` |  `boolean` Optional. Input only. Simulate a maintenance event.  
`backupCollection` |  `string` Optional. Output only. The backup collection full resource name. Example: projects/{project}/locations/{location}/backupCollections/{collection}  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the at-rest data of the cluster.  
`ondemandMaintenance  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Input only. Ondemand maintenance for the cluster. This field can be used to trigger ondemand critical update on the cluster.  
`asyncClusterEndpointsDeletionEnabled` |  `boolean` Optional. If true, cluster endpoints that are created and registered by customers can be deleted asynchronously. That is, such a cluster endpoint can be de-registered before the forwarding rules in the cluster endpoint are deleted.  
`maintenanceVersion` |  `string` Optional. This field can be used to trigger self service update to indicate the desired maintenance version. The input to this field can be determined by the availableMaintenanceVersions field.  
`effectiveMaintenanceVersion` |  `string` Output only. This field represents the actual maintenance version of the cluster.  
`serverCaMode` |  `enum (`[ServerCaMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ServerCaMode)`)` Optional. Server CA mode for the cluster.  
`serverCaPool` |  `string` Optional. Customer-managed CA pool for the cluster. Only applicable for BYOCA i.e. if serverCaMode is SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA. Format: "projects/{project}/locations/{region}/caPools/{ca_pool}".  
`rotateServerCertificate` |  `boolean` Optional. Input only. Rotate the server certificates.  
`aclPolicyInSync  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Output only. Deprecated: Indicates whether the ACL rules applied to the cluster are in sync.  
  
## GcsBackupSource

Backups stored in Cloud Storage buckets. The Cloud Storage buckets need to be the same region as the clusters.

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
  
## ManagedBackupSource

Backups that generated and managed by memorystore.

JSON representation  
---  
      
    
    {
      "backup": string
    }  
  
Fields  
---  
`backup` |  `string` Optional. Example: //redis.googleapis.com/projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backup} A shorter version (without the prefix) of the backup name is also supported, like projects/{project}/locations/{location}/backupCollections/{collection}/backups/{backupId} In this case, it assumes the backup is under redis.googleapis.com.  
  
## State

Represents the different states of a Redis cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | Redis cluster is being created.  
`ACTIVE` | Redis cluster has been created and is fully usable.  
`UPDATING` | Redis cluster configuration is being updated.  
`DELETING` | Redis cluster is being deleted.  
  
## AuthorizationMode

Available authorization mode of a Redis cluster.

Enums  
---  
`AUTH_MODE_UNSPECIFIED` | Not set.  
`AUTH_MODE_IAM_AUTH` | IAM basic authorization mode  
`AUTH_MODE_DISABLED` | Authorization disabled mode  
`AUTH_MODE_TOKEN_AUTH` | Token based authorization mode  
  
## TransitEncryptionMode

Available mode of in-transit encryption.

Enums  
---  
`TRANSIT_ENCRYPTION_MODE_UNSPECIFIED` | In-transit encryption not set.  
`TRANSIT_ENCRYPTION_MODE_DISABLED` | In-transit encryption disabled.  
`TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION` | Use server managed encryption for in-transit encryption.  
  
## PscConfig

JSON representation  
---  
      
    
    {
      "network": string
    }  
  
Fields  
---  
`network` |  `string` Required. The network where the IP address of the discovery endpoint will be reserved, in the form of projects/{networkProject}/global/networks/{network_id}.  
  
## DiscoveryEndpoint

Endpoints on each network, for Redis clients to connect to the cluster.

JSON representation  
---  
      
    
    {
      "address": string,
      "port": integer,
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConfig))
      }
    }  
  
Fields  
---  
`address` |  `string` Output only. Address of the exposed Redis endpoint used by clients to connect to the service. The address could be either IP or hostname.  
`port` |  `integer` Output only. The port number of the exposed Redis endpoint.  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConfig)`)` Output only. Customer configuration for where the endpoint is created and accessed from.  
  
## PscConnection

Details of consumer resources in a PSC connection.

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "address": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum ([PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnectionStatus)),
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "port": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Required. The PSC connection id of the forwarding rule connected to the service attachment.  
`address` |  `string` Required. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Required. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.  
`projectId` |  `string` Optional. Project ID of the consumer project where the forwarding rule is created in.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{projectId}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`[PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnectionStatus)`)` Output only. The status of the PSC connection. Please note that this value is updated periodically. To get the latest status of a PSC connection, follow <https://cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details>.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType)`)` Output only. Type of the PSC connection.  
The port number of the exposed discovery endpoint. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`port` |  `integer` Output only. port will only be set for Primary/Reader or Discovery endpoint.  
End of mutually exclusive fields.  
  
## PscConnectionStatus

Status of the PSC connection.

Enums  
---  
`PSC_CONNECTION_STATUS_UNSPECIFIED` | PSC connection status is not specified.  
`PSC_CONNECTION_STATUS_ACTIVE` | The connection is active  
`PSC_CONNECTION_STATUS_NOT_FOUND` | Connection not found  
  
## ConnectionType

Type of a PSC connection, for cluster access purpose.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | Cluster endpoint Type is not set  
`CONNECTION_TYPE_DISCOVERY` | Cluster endpoint that will be used as for cluster topology discovery.  
`CONNECTION_TYPE_PRIMARY` | Cluster endpoint that will be used as primary endpoint to access primary.  
`CONNECTION_TYPE_READER` | Cluster endpoint that will be used as reader endpoint to access replicas.  
  
## StateInfo

Represents additional information about the state of the cluster.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "updateInfo": {
        object ([UpdateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#UpdateInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`updateInfo` |  `object (`[UpdateInfo](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#UpdateInfo)`)` Describes ongoing update on the cluster when cluster state is UPDATING.  
End of mutually exclusive fields.  
  
## UpdateInfo

Represents information about an updating cluster.

JSON representation  
---  
      
    
    {
      "targetShardCount": integer,
      "targetReplicaCount": integer,
      "targetNodeType": enum ([NodeType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/NodeType))
    }  
  
Fields  
---  
`targetShardCount` |  `integer` Target number of shards for redis cluster  
`targetReplicaCount` |  `integer` Target number of replica nodes per shard.  
`targetNodeType` |  `enum (`[NodeType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/NodeType)`)` Target node type for redis cluster.  
  
## ClusterPersistenceConfig

Configuration of the persistence functionality.

JSON representation  
---  
      
    
    {
      "mode": enum ([PersistenceMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PersistenceMode)),
      "rdbConfig": {
        object ([RDBConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RDBConfig))
      },
      "aofConfig": {
        object ([AOFConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AOFConfig))
      }
    }  
  
Fields  
---  
`mode` |  `enum (`[PersistenceMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PersistenceMode)`)` Optional. The mode of persistence.  
`rdbConfig` |  `object (`[RDBConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RDBConfig)`)` Optional. RDB configuration. This field will be ignored if mode is not RDB.  
`aofConfig` |  `object (`[AOFConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AOFConfig)`)` Optional. AOF configuration. This field will be ignored if mode is not AOF.  
  
## PersistenceMode

Available persistence modes.

Enums  
---  
`PERSISTENCE_MODE_UNSPECIFIED` | Not set.  
`DISABLED` | Persistence is disabled, and any snapshot data is deleted.  
`RDB` | RDB based persistence is enabled.  
`AOF` | AOF based persistence is enabled.  
  
## RDBConfig

Configuration of the RDB based persistence.

JSON representation  
---  
      
    
    {
      "rdbSnapshotPeriod": enum ([SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#SnapshotPeriod)),
      "rdbSnapshotStartTime": string
    }  
  
Fields  
---  
`rdbSnapshotPeriod` |  `enum (`[SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#SnapshotPeriod)`)` Optional. Period between RDB snapshots.  
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SnapshotPeriod

Available snapshot periods.

Enums  
---  
`SNAPSHOT_PERIOD_UNSPECIFIED` | Not set.  
`ONE_HOUR` | One hour.  
`SIX_HOURS` | Six hours.  
`TWELVE_HOURS` | Twelve hours.  
`TWENTY_FOUR_HOURS` | Twenty four hours.  
  
## AOFConfig

Configuration of the AOF based persistence.

JSON representation  
---  
      
    
    {
      "appendFsync": enum ([AppendFsync](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AppendFsync))
    }  
  
Fields  
---  
`appendFsync` |  `enum (`[AppendFsync](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AppendFsync)`)` Optional. fsync configuration.  
  
## AppendFsync

Available fsync modes.

Enums  
---  
`APPEND_FSYNC_UNSPECIFIED` | Not set. Default: EVERYSEC  
`NO` | Never fsync. Normally Linux will flush data every 30 seconds with this configuration, but it's up to the kernel's exact tuning.  
`EVERYSEC` | fsync every second. Fast enough, and you may lose 1 second of data if there is a disaster  
`ALWAYS` | fsync every time new write commands are appended to the AOF. It has the best data loss protection at the cost of performance  
  
## ZoneDistributionConfig

Zone distribution config for allocation of cluster resources.

JSON representation  
---  
      
    
    {
      "mode": enum ([ZoneDistributionMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ZoneDistributionMode)),
      "zone": string,
      "zones": [
        string
      ]
    }  
  
Fields  
---  
`mode` |  `enum (`[ZoneDistributionMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ZoneDistributionMode)`)` Optional. The mode of zone distribution. Defaults to MULTI_ZONE, when not specified.  
`zone` |  `string` Optional. When SINGLE ZONE distribution is selected, zone field would be used to allocate all resources in that zone. This is not applicable to MULTI_ZONE, and would be ignored for MULTI_ZONE clusters.  
`zones[]` |  `string` Optional. Specify the zones of a multi-zone cluster where Redis Cluster allocates resources. This flag isn't applicable for single-zone clusters.  
  
## ZoneDistributionMode

Defines various modes of zone distribution.

Enums  
---  
`ZONE_DISTRIBUTION_MODE_UNSPECIFIED` | Not Set. Default: MULTI_ZONE  
`MULTI_ZONE` | Distribute all resources across 3 zones picked at random, within the region.  
`SINGLE_ZONE` | Distribute all resources in a single zone. The zone field must be specified, when this mode is selected.  
  
## CrossClusterReplicationConfig

Cross cluster replication config.

JSON representation  
---  
      
    
    {
      "clusterRole": enum ([ClusterRole](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterRole)),
      "primaryCluster": {
        object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster))
      },
      "secondaryClusters": [
        {
          object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster))
        }
      ],
      "updateTime": string,
      "membership": {
        object ([Membership](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#Membership))
      }
    }  
  
Fields  
---  
`clusterRole` |  `enum (`[ClusterRole](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterRole)`)` Output only. The role of the cluster in cross cluster replication.  
`primaryCluster` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster)`)` Details of the primary cluster that is used as the replication source for this secondary cluster.This field is only set for a secondary cluster.  
`secondaryClusters[]` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster)`)` List of secondary clusters that are replicating from this primary cluster.This field is only set for a primary cluster.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time cross cluster replication config was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`membership` |  `object (`[Membership](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#Membership)`)` Output only. An output only view of all the member clusters participating in the cross cluster replication. This view will be provided by every member cluster irrespective of its cluster role(primary or secondary).A primary cluster can provide information about all the secondary clusters replicating from it. However, a secondary cluster only knows about the primary cluster from which it is replicating. However, for scenarios, where the primary cluster is unavailable(e.g. regional outage), a clusters.get request can be sent to any other member cluster and this field will list all the member clusters participating in cross cluster replication.  
  
## ClusterRole

The role of the cluster in cross cluster replication.

Enums  
---  
`CLUSTER_ROLE_UNSPECIFIED` | Cluster role is not set. The behavior is equivalent to NONE.  
`NONE` | This cluster does not participate in cross cluster replication. It is an independent cluster and does not replicate to or from any other clusters.  
`PRIMARY` | A cluster that allows both reads and writes. Any data written to this cluster is also replicated to the attached secondary clusters.  
`SECONDARY` | A cluster that allows only reads and replicates data from a primary cluster.  
  
## RemoteCluster

Details of the remote cluster associated with this cluster in a cross cluster replication setup.

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
  
## Membership

An output only view of all the member clusters participating in the cross cluster replication.

JSON representation  
---  
      
    
    {
      "primaryCluster": {
        object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster))
      },
      "secondaryClusters": [
        {
          object ([RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster))
        }
      ]
    }  
  
Fields  
---  
`primaryCluster` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster)`)` Output only. The primary cluster that acts as the source of replication for the secondary clusters.  
`secondaryClusters[]` |  `object (`[RemoteCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#RemoteCluster)`)` Output only. The list of secondary clusters replicating from the primary cluster.  
  
## ClusterMaintenancePolicy

Maintenance policy per cluster.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "weeklyMaintenanceWindow": [
        {
          object ([ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterWeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created i.e. Maintenance Window or Deny Period was assigned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was updated i.e. Maintenance Window or Deny Period was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`weeklyMaintenanceWindow[]` |  `object (`[ClusterWeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ClusterWeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weeklyMaintenanceWindow is expected to be one.  
  
## ClusterWeeklyMaintenanceWindow

Time window specified for weekly operations.

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay))
      }
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/DayOfWeek)`)` Optional. Allows to define schedule that runs specified day of the week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay)`)` Optional. Start time of the window in UTC.  
  
## ClusterMaintenanceSchedule

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
  
## PscServiceAttachment

Configuration of a service attachment of the cluster, for creating PSC connections.

JSON representation  
---  
      
    
    {
      "serviceAttachment": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType))
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Output only. Service attachment URI which your self-created PscConnection should use as target  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType)`)` Output only. Type of a PSC connection targeting this service attachment.  
  
## ClusterEndpoint

ClusterEndpoint consists of PSC connections that are created as a group in each VPC network for accessing the cluster. In each group, there shall be one connection for each service attachment in the cluster.

JSON representation  
---  
      
    
    {
      "connections": [
        {
          object ([ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionDetail))
        }
      ]
    }  
  
Fields  
---  
`connections[]` |  `object (`[ConnectionDetail](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionDetail)`)` Required. A group of PSC connections. They are created in the same VPC network, one for each service attachment in the cluster.  
  
## ConnectionDetail

Detailed information of each PSC connection.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "pscAutoConnection": {
        object ([PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscAutoConnection))
      },
      "pscConnection": {
        object ([PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnection))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A PSC connection to a cluster could either be created through Service Connectivity Automation (auto-registered connection) during the cluster creation, or it could be created by customer themselves (user-registered connection). The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`pscAutoConnection` |  `object (`[PscAutoConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscAutoConnection)`)` Detailed information of a PSC connection that is created through service connectivity automation.  
`pscConnection` |  `object (`[PscConnection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnection)`)` Detailed information of a PSC connection that is created by the customer who owns the cluster.  
End of mutually exclusive fields.  
  
## PscAutoConnection

Details of consumer resources in a PSC connection that is created through Service Connectivity Automation.

JSON representation  
---  
      
    
    {
      "pscConnectionId": string,
      "address": string,
      "forwardingRule": string,
      "projectId": string,
      "network": string,
      "serviceAttachment": string,
      "pscConnectionStatus": enum ([PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnectionStatus)),
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType))
    }  
  
Fields  
---  
`pscConnectionId` |  `string` Output only. The PSC connection id of the forwarding rule connected to the service attachment.  
`address` |  `string` Output only. The IP allocated on the consumer network for the PSC forwarding rule.  
`forwardingRule` |  `string` Output only. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.  
`projectId` |  `string` Required. The consumer projectId where the forwarding rule is created from.  
`network` |  `string` Required. The consumer network where the IP address resides, in the form of projects/{projectId}/global/networks/{network_id}.  
`serviceAttachment` |  `string` Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.  
`pscConnectionStatus` |  `enum (`[PscConnectionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#PscConnectionStatus)`)` Output only. The status of the PSC connection. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#ConnectionType)`)` Output only. Type of the PSC connection.  
  
## AutomatedBackupConfig

The automated backup config for a cluster.

JSON representation  
---  
      
    
    {
      "automatedBackupMode": enum ([AutomatedBackupMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AutomatedBackupMode)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "fixedFrequencySchedule": {
        object ([FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#FixedFrequencySchedule))
      }
      // End of mutually exclusive fields.
      "retention": string
    }  
  
Fields  
---  
`automatedBackupMode` |  `enum (`[AutomatedBackupMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#AutomatedBackupMode)`)` Optional. The automated backup mode. If the mode is disabled, the other fields will be ignored.  
The schedule of automated backups. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`fixedFrequencySchedule` |  `object (`[FixedFrequencySchedule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters#FixedFrequencySchedule)`)` Optional. Trigger automated backups at a fixed frequency.  
End of mutually exclusive fields.  
`retention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How long to keep automated backups before the backups are deleted. The value should be between 1 day and 365 days. If not specified, the default value is 35 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## FixedFrequencySchedule

This schedule allows the backup to be triggered at a fixed frequency (currently only daily is supported).

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay))
      }
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay)`)` Required. The start time of every automated backup in UTC. It must be set to the start of an hour. This field is required.  
  
## AutomatedBackupMode

The automated backup mode.

Enums  
---  
`AUTOMATED_BACKUP_MODE_UNSPECIFIED` | Default value. Automated backup config is not specified.  
`DISABLED` | Automated backup config disabled.  
`ENABLED` | Automated backup config enabled.  
  
## ServerCaMode

Server CA mode for the cluster.

Enums  
---  
`SERVER_CA_MODE_UNSPECIFIED` | Server CA mode not specified.  
`SERVER_CA_MODE_GOOGLE_MANAGED_PER_INSTANCE_CA` | Each cluster has its own Google managed CA.  
`SERVER_CA_MODE_GOOGLE_MANAGED_SHARED_CA` | The cluster uses Google managed shared CA in the region.  
`SERVER_CA_MODE_CUSTOMER_MANAGED_CAS_CA` | The cluster uses customer managed CA from CAS.  
  
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
          object ([AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/AclPolicyRevisionStatus))
        }
      ]
    }  
  
Fields  
---  
`appliedAclPolicy` |  `string` Output only. The resource name of the applied ACL policy. Format: "projects/{project}/locations/{location}/aclPolicies/{aclPolicy}"  
`appliedAclPolicyRevision` |  `string` Output only. The resource name of the applied ACL policy revision. Format: "projects/{project}/locations/{location}/aclPolicies/{aclPolicy}/revisions/{revision}"  
`appliedAclPolicyRevisionNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The revision number of the applied ACL policy revision.  
`aclPolicyRevisionStatuses[]` |  `object (`[AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/AclPolicyRevisionStatus)`)` Output only. A list of status for various revisions of this ACL policy on the cluster.  
  
## Methods  
  
---  
  
### `[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/addTokenAuthUser)`

|  Adds a token auth user for a token based auth enabled cluster.  
  
### `[backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/backup)`

|  Backup Redis Cluster.  
  
### `[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/create)`

|  Creates a Redis cluster based on the specified properties.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/delete)`

|  Deletes a specific Redis cluster.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/get)`

|  Gets the details of a specific Redis cluster.  
  
### `[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/getCertificateAuthority)`

|  Gets the details of certificate authority information for Redis cluster.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/list)`

|  Lists all Redis clusters owned by a project in either the specified location (region) or all locations.  
  
### `[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/patch)`

|  Updates the metadata and configuration of a specific Redis cluster.  
  
### `[rescheduleClusterMaintenance](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/rescheduleClusterMaintenance)`

|  Reschedules upcoming maintenance event.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
