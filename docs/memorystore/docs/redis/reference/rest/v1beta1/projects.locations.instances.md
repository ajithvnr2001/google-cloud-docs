---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:49.776062+00:00
---

# REST Resource: projects.locations.instances  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * State
  * Tier
  * ConnectMode
  * TlsCertificate
    * JSON representation
  * TransitEncryptionMode
  * MaintenancePolicy
    * JSON representation
  * WeeklyMaintenanceWindow
    * JSON representation
  * MaintenanceSchedule
    * JSON representation
  * NodeInfo
    * JSON representation
  * ReadReplicasMode
  * PersistenceConfig
    * JSON representation
  * PersistenceMode
  * SnapshotPeriod
  * SuspensionReason
  * Methods



## Resource: Instance

A Memorystore for Redis instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "locationId": string,
      "alternativeLocationId": string,
      "redisVersion": string,
      "reservedIpRange": string,
      "secondaryIpRange": string,
      "host": string,
      "port": integer,
      "currentLocationId": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#State)),
      "statusMessage": string,
      "redisConfigs": {
        string: string,
        ...
      },
      "tier": enum ([Tier](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Tier)),
      "memorySizeGb": integer,
      "authorizedNetwork": string,
      "persistenceIamIdentity": string,
      "connectMode": enum ([ConnectMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#ConnectMode)),
      "authEnabled": boolean,
      "serverCaCerts": [
        {
          object ([TlsCertificate](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#TlsCertificate))
        }
      ],
      "transitEncryptionMode": enum ([TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#TransitEncryptionMode)),
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#MaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#MaintenanceSchedule))
      },
      "replicaCount": integer,
      "nodes": [
        {
          object ([NodeInfo](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#NodeInfo))
        }
      ],
      "readEndpoint": string,
      "readEndpointPort": integer,
      "readReplicasMode": enum ([ReadReplicasMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#ReadReplicasMode)),
      "customerManagedKey": string,
      "persistenceConfig": {
        object ([PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#PersistenceConfig))
      },
      "suspensionReasons": [
        enum ([SuspensionReason](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#SuspensionReason))
      ],
      "maintenanceVersion": string,
      "availableMaintenanceVersions": [
        string
      ],
      "tags": {
        string: string,
        ...
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. Unique name of the resource in this scope including project and location using the form: `projects/{projectId}/locations/{locationId}/instances/{instanceId}`Note: Redis instances are managed and addressed at regional level so locationId here refers to a GCP region; however, users may choose which specific zone (or collection of zones for cross-zone instances) an instance should be provisioned in. Refer to `[locationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance.FIELDS.location_id)` and `[alternativeLocationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance.FIELDS.alternative_location_id)` fields for more details.  
`displayName` |  `string` An arbitrary and optional user-provided name for the instance.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadataAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`locationId` |  `string` Optional. The zone where the instance will be provisioned. If not provided, the service will choose a zone from the specified region for the instance. For standard tier, additional nodes will be added across multiple zones for protection against zonal failures. If specified, at least one node will be provisioned in this zone.  
`alternativeLocationId` |  `string` Optional. If specified, at least one node will be provisioned in this zone in addition to the zone specified in locationId. Only applicable to standard tier. If provided, it must be a different zone from the one provided in [locationId]. Additional nodes beyond the first 2 will be placed in zones selected by the service.  
`redisVersion` |  `string` Optional. The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values are:

  * `REDIS_3_2` for Redis 3.2 compatibility
  * `REDIS_4_0` for Redis 4.0 compatibility (default)
  * `REDIS_5_0` for Redis 5.0 compatibility
  * `REDIS_6_X` for Redis 6.x compatibility
  * `REDIS_7_0` for Redis 7.0 compatibility

  
`reservedIpRange` |  `string` Optional. For DIRECT_PEERING mode, the CIDR range of internal addresses that are reserved for this instance. Range must be unique and non-overlapping with existing subnets in an authorized network. For PRIVATE_SERVICE_ACCESS mode, the name of one allocated IP address ranges associated with this private service access connection. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. For READ_REPLICAS_ENABLED the default block size is /28.  
`secondaryIpRange` |  `string` Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto".  
`host` |  `string` Output only. Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.  
`port` |  `integer` Output only. The port number of the exposed Redis endpoint.  
`currentLocationId` |  `string` Output only. The current zone where the Redis primary node is located. In basic tier, this will always be the same as [locationId]. In standard tier, this can be the zone of any node in the instance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#State)`)` Output only. The current state of this instance.  
`statusMessage` |  `string` Output only. Additional information about the current status of this instance, if available.  
`redisConfigs` |  `map (key: string, value: string)` Optional. Redis configuration parameters, according to <http://redis.io/topics/config>. Currently, the only supported parameters are:Redis version 3.2 and newer:

  * maxmemory-policy
  * notify-keyspace-events

Redis version 4.0 and newer:

  * activedefrag
  * lfu-decay-time
  * lfu-log-factor
  * maxmemory-gb

Redis version 5.0 and newer:

  * stream-node-max-bytes
  * stream-node-max-entries

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tier` |  `enum (`[Tier](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Tier)`)` Required. The service tier of the instance.  
`memorySizeGb` |  `integer` Required. Redis memory size in GiB.  
`authorizedNetwork` |  `string` Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. If left unspecified, the `default` network will be used.  
`persistenceIamIdentity` |  `string` Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is "serviceAccount:". The value may change over time for a given instance so should be checked before each import/export operation.  
`connectMode` |  `enum (`[ConnectMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#ConnectMode)`)` Optional. The network connect mode of the Redis instance. If not provided, the connect mode defaults to DIRECT_PEERING.  
`authEnabled` |  `boolean` Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled.  
`serverCaCerts[]` |  `object (`[TlsCertificate](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#TlsCertificate)`)` Output only. List of server CA certificates for the instance.  
`transitEncryptionMode` |  `enum (`[TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#TransitEncryptionMode)`)` Optional. The TLS mode of the Redis instance. If not provided, TLS is disabled for the instance.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#MaintenancePolicy)`)` Optional. The maintenance policy for the instance. If not provided, maintenance events can be performed at any time.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#MaintenanceSchedule)`)` Output only. Date and time of upcoming maintenance events which have been scheduled.  
`replicaCount` |  `integer` Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0.  
`nodes[]` |  `object (`[NodeInfo](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#NodeInfo)`)` Output only. Info per node.  
`readEndpoint` |  `string` Output only. Hostname or IP address of the exposed readonly Redis endpoint. Standard tier only. Targets all healthy replica nodes in instance. Replication is asynchronous and replica nodes will exhibit some lag behind the primary. Write requests must target 'host'.  
`readEndpointPort` |  `integer` Output only. The port number of the exposed readonly redis endpoint. Standard tier only. Write requests should target 'port'.  
`readReplicasMode` |  `enum (`[ReadReplicasMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#ReadReplicasMode)`)` Optional. Read replicas mode for the instance. Defaults to READ_REPLICAS_DISABLED.  
`customerManagedKey` |  `string` Optional. The KMS key reference that the customer provides when trying to create the instance.  
`persistenceConfig` |  `object (`[PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#PersistenceConfig)`)` Optional. Persistence configuration parameters  
`suspensionReasons[]` |  `enum (`[SuspensionReason](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#SuspensionReason)`)` Optional. reasons that causes instance in "SUSPENDED" state.  
`maintenanceVersion` |  `string` Optional. The self service update maintenance version. The version is date based such as "20210712_00_00".  
`availableMaintenanceVersions[]` |  `string` Optional. The available maintenance versions that an instance could update to.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
  
## State

Represents the different states of a Redis instance.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | Redis instance is being created.  
`READY` | Redis instance has been created and is fully usable.  
`UPDATING` | Redis instance configuration is being updated. Certain kinds of updates may cause the instance to become unusable while the update is in progress.  
`DELETING` | Redis instance is being deleted.  
`REPAIRING` | Redis instance is being repaired and may be unusable.  
`MAINTENANCE` | Maintenance is being performed on this Redis instance.  
`IMPORTING` | Redis instance is importing data (availability may be affected).  
`FAILING_OVER` | Redis instance is failing over (availability may be affected).  
  
## Tier

Available service tiers to choose from

Enums  
---  
`TIER_UNSPECIFIED` | Not set.  
`BASIC` | BASIC tier: standalone instance  
`STANDARD_HA` | STANDARD_HA tier: highly available primary/replica instances  
  
## ConnectMode

Available connection modes.

Enums  
---  
`CONNECT_MODE_UNSPECIFIED` | Not set.  
`DIRECT_PEERING` | Connect via direct peering to the Memorystore for Redis hosted service.  
`PRIVATE_SERVICE_ACCESS` | Connect your Memorystore for Redis instance using Private Service Access. Private services access provides an IP address range for multiple Google Cloud services, including Memorystore.  
  
## TlsCertificate

TlsCertificate Resource

JSON representation  
---  
      
    
    {
      "serialNumber": string,
      "cert": string,
      "createTime": string,
      "expireTime": string,
      "sha1Fingerprint": string
    }  
  
Fields  
---  
`serialNumber` |  `string` Serial number, as extracted from the certificate.  
`cert` |  `string` PEM representation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2020-05-18T00:00:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2020-05-18T00:00:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sha1Fingerprint` |  `string` Sha1 Fingerprint of the certificate.  
  
## TransitEncryptionMode

Available TLS modes.

Enums  
---  
`TRANSIT_ENCRYPTION_MODE_UNSPECIFIED` | Not set.  
`SERVER_AUTHENTICATION` | Client to Server traffic encryption enabled with server authentication.  
`DISABLED` | TLS is disabled for the instance.  
  
## MaintenancePolicy

Maintenance policy for an instance.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "description": string,
      "weeklyMaintenanceWindow": [
        {
          object ([WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#WeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512.  
`weeklyMaintenanceWindow[]` |  `object (`[WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#WeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one.  
  
## WeeklyMaintenanceWindow

Time window in which disruptive maintenance updates occur. Non-disruptive updates can occur inside or outside this window.

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/TimeOfDay))
      },
      "duration": string
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/DayOfWeek)`)` Required. The day of week that maintenance updates occur.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/TimeOfDay)`)` Required. Start time of the window in UTC time.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Duration of the maintenance window. The current window is fixed at 1 hour.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## MaintenanceSchedule

Upcoming maintenance schedule. If no maintenance is scheduled, fields are not populated.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "canReschedule": boolean,
      "scheduleDeadlineTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`canReschedule  
**(deprecated)**` |  `boolean` This item is deprecated!If the scheduled maintenance can be rescheduled, default is true.  
`scheduleDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The deadline that the maintenance schedule start time can not go beyond, including reschedule.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## NodeInfo

Node specific properties.

JSON representation  
---  
      
    
    {
      "id": string,
      "zone": string
    }  
  
Fields  
---  
`id` |  `string` Output only. Node identifying string. e.g. 'node-0', 'node-1'  
`zone` |  `string` Output only. Location of the node.  
  
## ReadReplicasMode

Read replicas mode.

Enums  
---  
`READ_REPLICAS_MODE_UNSPECIFIED` | If not set, Memorystore Redis backend will default to READ_REPLICAS_DISABLED.  
`READ_REPLICAS_DISABLED` | If disabled, read endpoint will not be provided and the instance cannot scale up or down the number of replicas.  
`READ_REPLICAS_ENABLED` | If enabled, read endpoint will be provided and the instance can scale up and down the number of replicas. Not valid for basic tier.  
  
## PersistenceConfig

Configuration of the persistence functionality.

JSON representation  
---  
      
    
    {
      "persistenceMode": enum ([PersistenceMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#PersistenceMode)),
      "rdbSnapshotPeriod": enum ([SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#SnapshotPeriod)),
      "rdbNextSnapshotTime": string,
      "rdbSnapshotStartTime": string
    }  
  
Fields  
---  
`persistenceMode` |  `enum (`[PersistenceMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#PersistenceMode)`)` Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used.  
`rdbSnapshotPeriod` |  `enum (`[SnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#SnapshotPeriod)`)` Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default.  
`rdbNextSnapshotTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The next time that a snapshot attempt is scheduled to occur.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## PersistenceMode

Available Persistence modes.

Enums  
---  
`PERSISTENCE_MODE_UNSPECIFIED` | Not set.  
`DISABLED` | Persistence is disabled for the instance, and any existing snapshots are deleted.  
`RDB` | RDB based Persistence is enabled.  
  
## SnapshotPeriod

Available snapshot periods for scheduling.

Enums  
---  
`SNAPSHOT_PERIOD_UNSPECIFIED` | Not set.  
`ONE_HOUR` | Snapshot every 1 hour.  
`SIX_HOURS` | Snapshot every 6 hours.  
`TWELVE_HOURS` | Snapshot every 12 hours.  
`TWENTY_FOUR_HOURS` | Snapshot every 24 hours.  
  
## SuspensionReason

Possible reasons for the instance to be in a "SUSPENDED" state.

Enums  
---  
`SUSPENSION_REASON_UNSPECIFIED` | Not set.  
`CUSTOMER_MANAGED_KEY_ISSUE` | Something wrong with the CMEK key provided by customer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/create)`

|  Creates a Redis instance based on the specified tier and memory size.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/delete)`

|  Deletes a specific Redis instance.  
  
### `[export](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/export)`

|  Export Redis instance data into a Redis RDB format file in Cloud Storage.  
  
### `[failover](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover)`

|  Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/get)`

|  Gets the details of a specific Redis instance.  
  
### `[getAuthString](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/getAuthString)`

|  Gets the AUTH string for a Redis instance.  
  
### `[import](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/import)`

|  Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/list)`

|  Lists all Redis instances owned by a project in either the specified location (region) or all locations.  
  
### `[patch](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/patch)`

|  Updates the metadata and configuration of a specific Redis instance.  
  
### `[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/rescheduleMaintenance)`

|  Reschedule maintenance for a given instance in a given project and location.  
  
### `[upgrade](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/upgrade)`

|  Upgrades Redis instance to the newer Redis version specified in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
