---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/get_instance/
title: MCP Tools Reference: redis.googleapis.com \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:53.013145+00:00
---

# MCP Tools Reference: redis.googleapis.com  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/get_instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  MCP Tools Reference: redis.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_instance`

Get detailed information about a Memorystore for Redis instance.

The following sample demonstrate how to use `curl` to invoke the `get_instance` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://redis.googleapis.com/mcp' \
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

Request for `GetInstance`.

### GetInstanceRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
  
## Output Schema

A Memorystore for Redis instance.

### Instance

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
      "state": enum (State),
      "statusMessage": string,
      "redisConfigs": {
        string: string,
        ...
      },
      "tier": enum (Tier),
      "memorySizeGb": integer,
      "authorizedNetwork": string,
      "persistenceIamIdentity": string,
      "connectMode": enum (ConnectMode),
      "authEnabled": boolean,
      "serverCaCerts": [
        {
          object ([TlsCertificate](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.TlsCertificate))
        }
      ],
      "transitEncryptionMode": enum (TransitEncryptionMode),
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.MaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.MaintenanceSchedule))
      },
      "replicaCount": integer,
      "nodes": [
        {
          object ([NodeInfo](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.NodeInfo))
        }
      ],
      "readEndpoint": string,
      "readEndpointPort": integer,
      "readReplicasMode": enum (ReadReplicasMode),
      "customerManagedKey": string,
      "persistenceConfig": {
        object ([PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.PersistenceConfig))
      },
      "suspensionReasons": [
        enum (SuspensionReason)
      ],
      "maintenanceVersion": string,
      "availableMaintenanceVersions": [
        string
      ],
      "tags": {
        string: string,
        ...
      },
    
      // Union field _satisfies_pzs can be only one of the following:
      "satisfiesPzs": boolean
      // End of list of possible types for union field _satisfies_pzs.
    
      // Union field _satisfies_pzi can be only one of the following:
      "satisfiesPzi": boolean
      // End of list of possible types for union field _satisfies_pzi.
    }  
  
Fields  
---  
`name` |  `string` Required. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}`Note: Redis instances are managed and addressed at regional level so location_id here refers to a GCP region; however, users may choose which specific zone (or collection of zones for cross-zone instances) an instance should be provisioned in. Refer to `location_id` and `alternative_location_id` fields for more details.  
`displayName` |  `string` An arbitrary and optional user-provided name for the instance.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadataAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`locationId` |  `string` Optional. The zone where the instance will be provisioned. If not provided, the service will choose a zone from the specified region for the instance. For standard tier, additional nodes will be added across multiple zones for protection against zonal failures. If specified, at least one node will be provisioned in this zone.  
`alternativeLocationId` |  `string` Optional. If specified, at least one node will be provisioned in this zone in addition to the zone specified in location_id. Only applicable to standard tier. If provided, it must be a different zone from the one provided in [location_id]. Additional nodes beyond the first 2 will be placed in zones selected by the service.  
`redisVersion` |  `string` Optional. The version of Redis software. If not provided, the default version will be used. Currently, the supported values are:

  * `REDIS_3_2` for Redis 3.2 compatibility
  * `REDIS_4_0` for Redis 4.0 compatibility
  * `REDIS_5_0` for Redis 5.0 compatibility
  * `REDIS_6_X` for Redis 6.x compatibility
  * `REDIS_7_0` for Redis 7.0 compatibility (default)
  * `REDIS_7_2` for Redis 7.2 compatibility

  
`reservedIpRange` |  `string` Optional. For DIRECT_PEERING mode, the CIDR range of internal addresses that are reserved for this instance. Range must be unique and non-overlapping with existing subnets in an authorized network. For PRIVATE_SERVICE_ACCESS mode, the name of one allocated IP address ranges associated with this private service access connection. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. For READ_REPLICAS_ENABLED the default block size is /28.  
`secondaryIpRange` |  `string` Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto".  
`host` |  `string` Output only. Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.  
`port` |  `integer` Output only. The port number of the exposed Redis endpoint.  
`currentLocationId` |  `string` Output only. The current zone where the Redis primary node is located. In basic tier, this will always be the same as [location_id]. In standard tier, this can be the zone of any node in the instance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`State`)` Output only. The current state of this instance.  
`statusMessage` |  `string` Output only. Additional information about the current status of this instance, if available.  
`redisConfigs` |  `map (key: string, value: string)` Optional. Redis configuration parameters, according to [Redis configuration](https://redis.io/docs/latest/operate/oss_and_stack/management/config/). Currently, the only supported parameters are:Redis version 3.2 and newer:

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
`tier` |  `enum (`Tier`)` Required. The service tier of the instance.  
`memorySizeGb` |  `integer` Required. Redis memory size in GiB.  
`authorizedNetwork` |  `string` Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. If left unspecified, the `default` network will be used.  
`persistenceIamIdentity` |  `string` Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is "serviceAccount:". The value may change over time for a given instance so should be checked before each import/export operation.  
`connectMode` |  `enum (`ConnectMode`)` Optional. The network connect mode of the Redis instance. If not provided, the connect mode defaults to DIRECT_PEERING.  
`authEnabled` |  `boolean` Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled.  
`serverCaCerts[]` |  `object (`[TlsCertificate](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.TlsCertificate)`)` Output only. List of server CA certificates for the instance.  
`transitEncryptionMode` |  `enum (`TransitEncryptionMode`)` Optional. The TLS mode of the Redis instance. If not provided, TLS is disabled for the instance.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.MaintenancePolicy)`)` Optional. The maintenance policy for the instance. If not provided, maintenance events can be performed at any time.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.MaintenanceSchedule)`)` Output only. Date and time of upcoming maintenance events which have been scheduled.  
`replicaCount` |  `integer` Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0.  
`nodes[]` |  `object (`[NodeInfo](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.NodeInfo)`)` Output only. Info per node.  
`readEndpoint` |  `string` Output only. Hostname or IP address of the exposed readonly Redis endpoint. Standard tier only. Targets all healthy replica nodes in instance. Replication is asynchronous and replica nodes will exhibit some lag behind the primary. Write requests must target 'host'.  
`readEndpointPort` |  `integer` Output only. The port number of the exposed readonly redis endpoint. Standard tier only. Write requests should target 'port'.  
`readReplicasMode` |  `enum (`ReadReplicasMode`)` Optional. Read replicas mode for the instance. Defaults to READ_REPLICAS_DISABLED.  
`customerManagedKey` |  `string` Optional. The KMS key reference that the customer provides when trying to create the instance.  
`persistenceConfig` |  `object (`[PersistenceConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.PersistenceConfig)`)` Optional. Persistence configuration parameters  
`suspensionReasons[]` |  `enum (`SuspensionReason`)` Optional. reasons that causes instance in "SUSPENDED" state.  
`maintenanceVersion` |  `string` Optional. The self service update maintenance version. The version is date based such as "20210712_00_00".  
`availableMaintenanceVersions[]` |  `string` Optional. The available maintenance versions that an instance could update to.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `_satisfies_pzs`.`_satisfies_pzs` can be only one of the following:  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
Union field `_satisfies_pzi`.`_satisfies_pzi` can be only one of the following:  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
  
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
  
### TlsCertificate

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
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2020-05-18T00:00:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2020-05-18T00:00:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sha1Fingerprint` |  `string` Sha1 Fingerprint of the certificate.  
  
### MaintenancePolicy

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "description": string,
      "weeklyMaintenanceWindow": [
        {
          object ([WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.WeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512.  
`weeklyMaintenanceWindow[]` |  `object (`[WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.WeeklyMaintenanceWindow)`)` Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one.  
  
### WeeklyMaintenanceWindow

JSON representation  
---  
      
    
    {
      "day": enum (google.type.DayOfWeek),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay))
      },
      "duration": string
    }  
  
Fields  
---  
`day` |  `enum (`google.type.DayOfWeek`)` Required. The day of week that maintenance updates occur.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/redis/reference/mcp/tools_list/list_instances#Output.Schema.TimeOfDay)`)` Required. Start time of the window in UTC time.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Duration of the maintenance window. The current window is fixed at 1 hour.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
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
  
### MaintenanceSchedule

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
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`canReschedule  
**(deprecated)**` |  `boolean` This item is deprecated!If the scheduled maintenance can be rescheduled, default is true.  
`scheduleDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The deadline that the maintenance schedule start time can not go beyond, including reschedule.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### NodeInfo

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
  
### PersistenceConfig

JSON representation  
---  
      
    
    {
      "persistenceMode": enum (PersistenceMode),
      "rdbSnapshotPeriod": enum (SnapshotPeriod),
      "rdbNextSnapshotTime": string,
      "rdbSnapshotStartTime": string
    }  
  
Fields  
---  
`persistenceMode` |  `enum (`PersistenceMode`)` Optional. Controls whether Persistence features are enabled. If not provided, the existing value will be used.  
`rdbSnapshotPeriod` |  `enum (`SnapshotPeriod`)` Optional. Period between RDB snapshots. Snapshots will be attempted every period starting from the provided snapshot start time. For example, a start time of 01/01/2033 06:45 and SIX_HOURS snapshot period will do nothing until 01/01/2033, and then trigger snapshots every day at 06:45, 12:45, 18:45, and 00:45 the next day, and so on. If not provided, TWENTY_FOUR_HOURS will be used as default.  
`rdbNextSnapshotTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The next time that a snapshot attempt is scheduled to occur.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rdbSnapshotStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Date and time that the first snapshot was/will be attempted, and to which future snapshots will be aligned. If not provided, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### TagsEntry

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
