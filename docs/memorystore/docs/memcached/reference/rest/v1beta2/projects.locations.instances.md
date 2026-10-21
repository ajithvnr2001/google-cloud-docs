---
url: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:10:51.919550+00:00
---

# REST Resource: projects.locations.instances  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/memcached/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * NodeConfig
    * JSON representation
  * MemcacheVersion
  * MemcacheParameters
    * JSON representation
  * Node
    * JSON representation
  * State
  * State
  * InstanceMessage
    * JSON representation
  * Code
  * MaintenancePolicy
    * JSON representation
  * WeeklyMaintenanceWindow
    * JSON representation
  * MaintenanceSchedule
    * JSON representation
  * Methods



## Resource: Instance

A Memorystore for Memcached instance

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "authorizedNetwork": string,
      "zones": [
        string
      ],
      "nodeCount": integer,
      "nodeConfig": {
        object ([NodeConfig](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#NodeConfig))
      },
      "memcacheVersion": enum ([MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion)),
      "parameters": {
        object ([MemcacheParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheParameters))
      },
      "memcacheNodes": [
        {
          object ([Node](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Node))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#State_1)),
      "memcacheFullVersion": string,
      "instanceMessages": [
        {
          object ([InstanceMessage](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#InstanceMessage))
        }
      ],
      "discoveryEndpoint": string,
      "updateAvailable": boolean,
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MaintenancePolicy))
      },
      "maintenanceSchedule": {
        object ([MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MaintenanceSchedule))
      },
      "reservedIpRangeId": [
        string
      ],
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. Unique name of the resource in this scope including project and location using the form: `projects/{projectId}/locations/{locationId}/instances/{instanceId}`Note: Memcached instances are managed and addressed at the regional level so `locationId` here refers to a Google Cloud region; however, users may choose which zones Memcached nodes should be provisioned in within an instance. Refer to `[zones](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Instance.FIELDS.zones)` field for more details.  
`displayName` |  `string` User provided name for the instance, which is only used for display purposes. Cannot be more than 80 characters.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. <https://cloud.google.com/compute/docs/labeling-resources>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`authorizedNetwork` |  `string` The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. If left unspecified, the `default` network will be used.  
`zones[]` |  `string` Zones in which Memcached nodes should be provisioned. Memcached nodes will be equally distributed across these zones. If not provided, the service will by default create nodes in all zones in the region for the instance.  
`nodeCount` |  `integer` Required. Number of nodes in the Memcached instance.  
`nodeConfig` |  `object (`[NodeConfig](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#NodeConfig)`)` Required. Configuration for Memcached nodes.  
`memcacheVersion` |  `enum (`[MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion)`)` The major version of Memcached software. If not provided, latest supported version will be used. Currently the latest supported major version is `MEMCACHE_1_5`. The minor version will be automatically determined by our system based on the latest supported minor version.  
`parameters` |  `object (`[MemcacheParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheParameters)`)` User defined parameters to apply to the memcached process on each node.  
`memcacheNodes[]` |  `object (`[Node](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Node)`)` Output only. List of Memcached nodes. Refer to `[Node](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Node)` message for more details.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the instance was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#State_1)`)` Output only. The state of this Memcached instance.  
`memcacheFullVersion` |  `string` Output only. The full version of memcached server running on this instance. System automatically determines the full memcached version for an instance based on the input MemcacheVersion. The full version format will be "memcached-1.5.16".  
`instanceMessages[]` |  `object (`[InstanceMessage](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#InstanceMessage)`)` List of messages that describe the current state of the Memcached instance.  
`discoveryEndpoint` |  `string` Output only. Endpoint for the Discovery API.  
`updateAvailable` |  `boolean` Output only. Returns true if there is an update waiting to be applied  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MaintenancePolicy)`)` The maintenance policy for the instance. If not provided, the maintenance event will be performed based on Memorystore internal rollout schedule.  
`maintenanceSchedule` |  `object (`[MaintenanceSchedule](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MaintenanceSchedule)`)` Output only. Published maintenance schedule.  
`reservedIpRangeId[]` |  `string` Optional. Contains the id of allocated IP address ranges associated with the private service access connection for example, "test-default" associated with IP range 10.0.0.0/29.  
`satisfiesPzs` |  `boolean` Optional. Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Optional. Output only. Reserved for future use.  
  
## NodeConfig

Configuration for a Memcached Node.

JSON representation  
---  
      
    
    {
      "cpuCount": integer,
      "memorySizeMb": integer
    }  
  
Fields  
---  
`cpuCount` |  `integer` Required. Number of cpus per Memcached node.  
`memorySizeMb` |  `integer` Required. Memory size in MiB for each Memcached node.  
  
## MemcacheVersion

Memcached versions supported by our service.

Enums  
---  
`MEMCACHE_VERSION_UNSPECIFIED` | Memcache version is not specified by customer  
`MEMCACHE_1_5` | Memcached 1.5 version.  
`MEMCACHE_1_6_15` | Memcached 1.6.15 version.  
  
## MemcacheParameters

JSON representation  
---  
      
    
    {
      "id": string,
      "params": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique ID associated with this set of parameters. Users can use this id to determine if the parameters associated with the instance differ from the parameters associated with the nodes. A discrepancy between parameter ids can inform users that they may need to take action to apply parameters on nodes.  
`params` |  `map (key: string, value: string)` User defined set of parameters to use in the memcached process.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Node

JSON representation  
---  
      
    
    {
      "nodeId": string,
      "zone": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#State)),
      "host": string,
      "port": integer,
      "parameters": {
        object ([MemcacheParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheParameters))
      },
      "updateAvailable": boolean,
      "memcacheVersion": enum ([MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion)),
      "memcacheFullVersion": string
    }  
  
Fields  
---  
`nodeId` |  `string` Output only. Identifier of the Memcached node. The node id does not include project or location like the Memcached instance name.  
`zone` |  `string` Output only. Location (GCP Zone) for the Memcached node.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#State)`)` Output only. Current state of the Memcached node.  
`host` |  `string` Output only. Hostname or IP address of the Memcached node used by the clients to connect to the Memcached server on this node.  
`port` |  `integer` Output only. The port number of the Memcached server on this node.  
`parameters` |  `object (`[MemcacheParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheParameters)`)` User defined parameters currently applied to the node.  
`updateAvailable` |  `boolean` Output only. Returns true if there is an update waiting to be applied  
`memcacheVersion` |  `enum (`[MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion)`)` Output only. Major version of memcached server running on this node, e.g. MEMCACHE_1_5  
`memcacheFullVersion` |  `string` Output only. The full version of memcached server running on this node. e.g. - memcached-1.5.16  
  
## State

Different states of a Memcached node.

Enums  
---  
`STATE_UNSPECIFIED` | Node state is not set.  
`CREATING` | Node is being created.  
`READY` | Node has been created and ready to be used.  
`DELETING` | Node is being deleted.  
`UPDATING` | Node is being updated.  
  
## State

Different states of a Memcached instance.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | Memcached instance is being created.  
`READY` | Memcached instance has been created and ready to be used.  
`UPDATING` | Memcached instance is updating configuration such as maintenance policy and schedule.  
`DELETING` | Memcached instance is being deleted.  
`PERFORMING_MAINTENANCE` | Memcached instance is going through maintenance, e.g. data plane rollout.  
`MEMCACHE_VERSION_UPGRADING` | Memcached instance is undergoing memcached engine version upgrade.  
  
## InstanceMessage

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Code)),
      "message": string
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#Code)`)` A code that correspond to one type of user-facing message.  
`message` |  `string` Message on memcached instance which will be exposed to users.  
  
## Code

Enums  
---  
`CODE_UNSPECIFIED` | Message Code not set.  
`ZONE_DISTRIBUTION_UNBALANCED` | Memcached nodes are distributed unevenly.  
  
## MaintenancePolicy

Maintenance policy per instance.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "description": string,
      "weeklyMaintenanceWindow": [
        {
          object ([WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#WeeklyMaintenanceWindow))
        }
      ]
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the policy was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512.  
`weeklyMaintenanceWindow[]` |  `object (`[WeeklyMaintenanceWindow](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#WeeklyMaintenanceWindow)`)` Required. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_maintenance_windows is expected to be one.  
  
## WeeklyMaintenanceWindow

Time window specified for weekly operations.

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/Shared.Types/DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/Shared.Types/TimeOfDay))
      },
      "duration": string
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/Shared.Types/DayOfWeek)`)` Required. Allows to define schedule that runs specified day of the week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/Shared.Types/TimeOfDay)`)` Required. Start time of the window in UTC.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. Duration of the time window.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## MaintenanceSchedule

Upcoming maintenance schedule.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "scheduleDeadlineTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scheduleDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The deadline that the maintenance schedule start time can not go beyond, including reschedule.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[applyParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/applyParameters)`

|  `ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.  
  
### `[applySoftwareUpdate](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/applySoftwareUpdate)`

|  Updates software on the selected nodes of the Instance.  
  
### `[create](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/create)`

|  Creates a new Instance in a given location.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/delete)`

|  Deletes a single Instance.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/get)`

|  Gets details of a single Instance.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/list)`

|  Lists Instances in a given location.  
  
### `[patch](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/patch)`

|  Updates an existing Instance in a given project and location.  
  
### `[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/rescheduleMaintenance)`

|  Performs the apply phase of the RescheduleMaintenance verb.  
  
### `[updateParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/updateParameters)`

|  Updates the defined Memcached parameters for an existing instance.  
  
### `[upgrade](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/upgrade)`

|  Upgrades the Memcache instance to a newer memcached engine version specified in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
