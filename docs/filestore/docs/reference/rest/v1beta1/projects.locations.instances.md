---
url: https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances
title: REST Resource: projects.locations.instances \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:49.021100+00:00
---

# REST Resource: projects.locations.instances  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Reference ](https://docs.cloud.google.com/filestore/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Instance
    * JSON representation
  * State
  * FileShareConfig
    * JSON representation
  * NetworkConfig
    * JSON representation
  * AddressMode
  * ConnectMode
  * PscConfig
    * JSON representation
  * SuspensionReason
  * DirectoryServicesConfig
    * JSON representation
  * ManagedActiveDirectoryConfig
    * JSON representation
  * LdapConfig
    * JSON representation
  * Replication
    * JSON representation
  * Role
  * ReplicaConfig
    * JSON representation
  * State
  * StateReason
  * PerformanceConfig
    * JSON representation
  * IOPSPerTB
    * JSON representation
  * FixedIOPS
    * JSON representation
  * PerformanceLimits
    * JSON representation
  * BackendType
  * Methods



## Resource: Instance

A Filestore instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#State)),
      "statusMessage": string,
      "createTime": string,
      "tier": enum ([Tier](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/Tier)),
      "labels": {
        string: string,
        ...
      },
      "fileShares": [
        {
          object ([FileShareConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#FileShareConfig))
        }
      ],
      "networks": [
        {
          object ([NetworkConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#NetworkConfig))
        }
      ],
      "etag": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
      "kmsKeyName": string,
      "suspensionReasons": [
        enum ([SuspensionReason](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#SuspensionReason))
      ],
      "minCapacityGb": string,
      "maxCapacityGb": string,
      "capacityStepSizeGb": string,
      "maxShareCount": string,
      "capacityGb": string,
      "multiShareEnabled": boolean,
      "protocol": enum ([FileProtocol](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/FileProtocol)),
      "directoryServices": {
        object ([DirectoryServicesConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#DirectoryServicesConfig))
      },
      "replication": {
        object ([Replication](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#Replication))
      },
      "tags": {
        string: string,
        ...
      },
      "customPerformanceSupported": boolean,
      "performanceConfig": {
        object ([PerformanceConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PerformanceConfig))
      },
      "performanceLimits": {
        object ([PerformanceLimits](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PerformanceLimits))
      },
      "deletionProtectionEnabled": boolean,
      "deletionProtectionReason": string,
      "backendType": enum ([BackendType](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#BackendType))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the instance, in the format `projects/{projectId}/locations/{locationId}/instances/{instanceId}`.  
`description` |  `string` The description of the instance (2048 characters or less).  
`state` |  `enum (`[State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#State)`)` Output only. The instance state.  
`statusMessage` |  `string` Output only. Additional information about the instance state, if available.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tier` |  `enum (`[Tier](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/Tier)`)` The service tier of the instance.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fileShares[]` |  `object (`[FileShareConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#FileShareConfig)`)` File system shares on the instance. For this version, only a single file share is supported.  
`networks[]` |  `object (`[NetworkConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#NetworkConfig)`)` VPC networks to which the instance is connected. For this version, only a single network is supported.  
`etag` |  `string` Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
`kmsKeyName` |  `string` KMS key name used for data encryption.  
`suspensionReasons[]` |  `enum (`[SuspensionReason](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#SuspensionReason)`)` Output only. Field indicates all the reasons the instance is in "SUSPENDED" state.  
`maxCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum capacity of the instance.  
`capacityStepSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The incremental increase or decrease in capacity, designated in some number of GB.  
`maxShareCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of shares allowed.  
`capacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The storage capacity of the instance in gigabytes (GB = 1024^3 bytes). This capacity can be increased up to `maxCapacityGb` GB in multipliers of `capacityStepSizeGb` GB.  
`multiShareEnabled` |  `boolean` Indicates whether this instance uses a multi-share configuration with which it can have more than one file-share or none at all. File-shares are added, updated and removed through the separate file-share APIs.  
`protocol` |  `enum (`[FileProtocol](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/FileProtocol)`)` Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: `NFS_V3`.  
`directoryServices` |  `object (`[DirectoryServicesConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#DirectoryServicesConfig)`)` Optional. Directory Services configuration. Should only be set if protocol is "NFS_V4_1".  
`replication` |  `object (`[Replication](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#Replication)`)` Optional. Replication configuration.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information: - Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key> \- Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`customPerformanceSupported` |  `boolean` Output only. Indicates whether this instance supports configuring its performance. If true, the user can configure the instance's performance by using the 'performanceConfig' field.  
`performanceConfig` |  `object (`[PerformanceConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PerformanceConfig)`)` Optional. Used to configure performance.  
`performanceLimits` |  `object (`[PerformanceLimits](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PerformanceLimits)`)` Output only. Used for getting performance limits.  
`deletionProtectionEnabled` |  `boolean` Optional. Indicates whether the instance is protected against deletion.  
`deletionProtectionReason` |  `string` Optional. The reason for enabling deletion protection.  
`backendType` |  `enum (`[BackendType](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#BackendType)`)` Optional. Immutable. Designates the backend type of this instance. Intended to be used by internal tests and allowed customers.  
  
## State

The instance state.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | The instance is being created.  
`READY` | The instance is available for use.  
`REPAIRING` | Work is being done on the instance. You can get further details from the `statusMessage` field of the `Instance` resource.  
`DELETING` | The instance is shutting down.  
`ERROR` | The instance is experiencing an issue and might be unusable. You can get further details from the `statusMessage` field of the `Instance` resource.  
`RESTORING` | The instance is restoring a snapshot or backup to an existing file share and may be unusable during this time.  
`SUSPENDED` | The instance is suspended. You can get further details from the `suspensionReasons` field of the `Instance` resource.  
`REVERTING` | The instance is reverting to a snapshot.  
`SUSPENDING` | The instance is in the process of becoming suspended.  
`RESUMING` | The instance is in the process of becoming active.  
`PROMOTING` | The replica instance is being promoted.  
  
## FileShareConfig

File share configuration for the instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "capacityGb": string,
      "nfsExportOptions": [
        {
          object ([NfsExportOptions](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/NfsExportOptions))
        }
      ],
    
      // Union field source can be only one of the following:
      "sourceBackup": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the file share. Must use 1-16 characters for the basic service tier and 1-63 characters for all other service tiers. Must use lowercase letters, numbers, or underscores `[a-z0-9_]`. Must start with a letter. Immutable.  
`capacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` File share capacity in gigabytes (GB). Filestore defines 1 GB as 1024^3 bytes.  
`nfsExportOptions[]` |  `object (`[NfsExportOptions](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/NfsExportOptions)`)` Nfs Export Options. There is a limit of 10 export options per file share.  
Union field `source`. The source that this file share has been restored from. Empty if the file share is created from scratch. `source` can be only one of the following:  
`sourceBackup` |  `string` The resource name of the backup, in the format `projects/{projectId}/locations/{locationId}/backups/{backupId}`, that this file share has been restored from.  
  
## NetworkConfig

Network configuration for the instance.

JSON representation  
---  
      
    
    {
      "network": string,
      "modes": [
        enum ([AddressMode](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#AddressMode))
      ],
      "reservedIpRange": string,
      "ipAddresses": [
        string
      ],
      "connectMode": enum ([ConnectMode](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ConnectMode)),
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PscConfig))
      }
    }  
  
Fields  
---  
`network` |  `string` The name of the Google Compute Engine [VPC network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected.  
`modes[]` |  `enum (`[AddressMode](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#AddressMode)`)` Internet protocol versions for which the instance has IP addresses assigned. For this version, only MODE_IPV4 is supported.  
`reservedIpRange` |  `string` Optional, reservedIpRange can have one of the following two types of values.

  * CIDR range value when using DIRECT_PEERING connect mode.
  * [Allocated IP address range](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address) when using PRIVATE_SERVICE_ACCESS connect mode.

When the name of an allocated IP address range is specified, it must be one of the ranges associated with the private service access connection. When specified as a direct CIDR value, it must be a /29 CIDR block for Basic tier, a /24 CIDR block for High Scale tier, or a /26 CIDR block for Enterprise tier in one of the [internal IP address ranges](https://www.arin.net/reference/research/statistics/address_filters/) that identifies the range of IP addresses reserved for this instance. For example, 10.0.0.0/29, 192.168.0.0/24, or 192.168.0.0/26, respectively. The range you specify can't overlap with either existing subnets or assigned IP address ranges for other Filestore instances in the selected VPC network.  
`ipAddresses[]` |  `string` Output only. IPv4 addresses in the format `{octet1}.{octet2}.{octet3}.{octet4}` or IPv6 addresses in the format `{block1}:{block2}:{block3}:{block4}:{block5}:{block6}:{block7}:{block8}`.  
`connectMode` |  `enum (`[ConnectMode](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ConnectMode)`)` The network connect mode of the Filestore instance. If not provided, the connect mode defaults to DIRECT_PEERING.  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#PscConfig)`)` Optional. Private Service Connect configuration. Should only be set when connectMode is PRIVATE_SERVICE_CONNECT.  
  
## AddressMode

Internet protocol versions supported by Filestore.

Enums  
---  
`ADDRESS_MODE_UNSPECIFIED` | Internet protocol not set.  
`MODE_IPV4` | Use the IPv4 internet protocol.  
  
## ConnectMode

Available connection modes.

Enums  
---  
`CONNECT_MODE_UNSPECIFIED` | ConnectMode not set.  
`DIRECT_PEERING` | Connect via direct peering to the Filestore service.  
`PRIVATE_SERVICE_ACCESS` | Connect to your Filestore instance using Private Service Access. Private services access provides an IP address range for multiple Google Cloud services, including Filestore.  
`PRIVATE_SERVICE_CONNECT` | Connect to your Filestore instance using Private Service Connect. A connection policy must exist in the region for the VPC network and the google-cloud-filestore service class.  
  
## PscConfig

Private Service Connect configuration.

JSON representation  
---  
      
    
    {
      "endpointProject": string
    }  
  
Fields  
---  
`endpointProject` |  `string` Consumer service project in which the Private Service Connect endpoint would be set up. This is optional, and only relevant in case the network is a shared VPC. If this is not specified, the endpoint would be setup in the VPC host project.  
  
## SuspensionReason

SuspensionReason contains the possible reasons for a suspension.

Enums  
---  
`SUSPENSION_REASON_UNSPECIFIED` | Not set.  
`KMS_KEY_ISSUE` | The KMS key used by the instance is either revoked or denied access to.  
  
## DirectoryServicesConfig

Directory Services configuration.

JSON representation  
---  
      
    
    {
    
      // Union field config can be only one of the following:
      "managedActiveDirectory": {
        object ([ManagedActiveDirectoryConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ManagedActiveDirectoryConfig))
      },
      "ldap": {
        object ([LdapConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#LdapConfig))
      }
      // End of list of possible types for union field config.
    }  
  
Fields  
---  
Union field `config`.`config` can be only one of the following:  
`managedActiveDirectory` |  `object (`[ManagedActiveDirectoryConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ManagedActiveDirectoryConfig)`)` Configuration for Managed Service for Microsoft Active Directory.  
`ldap` |  `object (`[LdapConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#LdapConfig)`)` Configuration for LDAP servers.  
  
## ManagedActiveDirectoryConfig

ManagedActiveDirectoryConfig contains all the parameters for connecting to Managed Service for Microsoft Active Directory (Managed Microsoft AD).

JSON representation  
---  
      
    
    {
      "domain": string,
      "computer": string
    }  
  
Fields  
---  
`domain` |  `string` Required. The domain resource name, in the format `projects/{projectId}/locations/global/domains/{domain}`.  
`computer` |  `string` Required. The computer name is used as a prefix in the command to mount the remote target. For example: if the computer is `my-computer`, the mount command will look like: `$mount -o vers=4.1,sec=krb5 my-computer.filestore.<domain>:<share> <mount point>`.  
  
## LdapConfig

LdapConfig contains all the parameters for connecting to LDAP servers.

JSON representation  
---  
      
    
    {
      "domain": string,
      "servers": [
        string
      ],
      "usersOu": string,
      "groupsOu": string
    }  
  
Fields  
---  
`domain` |  `string` Required. The LDAP domain name in the format of `my-domain.com`.  
`servers[]` |  `string` Required. The servers names are used for specifying the LDAP servers names. The LDAP servers names can come with two formats: 1. DNS name, for example: `ldap.example1.com`, `ldap.example2.com`. 2. IP address, for example: `10.0.0.1`, `10.0.0.2`, `10.0.0.3`. All servers names must be in the same format: either all DNS names or all IP addresses.  
`usersOu` |  `string` Optional. The users Organizational Unit (OU) is optional. This parameter is a hint to allow faster lookup in the LDAP namespace. In case that this parameter is not provided, Filestore instance will query the whole LDAP namespace.  
`groupsOu` |  `string` Optional. The groups Organizational Unit (OU) is optional. This parameter is a hint to allow faster lookup in the LDAP namespace. In case that this parameter is not provided, Filestore instance will query the whole LDAP namespace.  
  
## Replication

Optional. The configuration used to replicate an instance.

JSON representation  
---  
      
    
    {
      "role": enum ([Role](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#Role)),
      "replicas": [
        {
          object ([ReplicaConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ReplicaConfig))
        }
      ]
    }  
  
Fields  
---  
`role` |  `enum (`[Role](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#Role)`)` Output only. The replication role. When creating a new replica, this field must be set to `STANDBY`.  
`replicas[]` |  `object (`[ReplicaConfig](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#ReplicaConfig)`)` Replication configuration for the replica instance associated with this instance. Only a single replica is supported.  
  
## Role

Replication role.

Enums  
---  
`ROLE_UNSPECIFIED` | Role not set.  
`ACTIVE` | The instance is the `ACTIVE` replication member, functions as the replication source instance.  
`STANDBY` | The instance is the `STANDBY` replication member, functions as the replication destination instance.  
  
## ReplicaConfig

Replica configuration for the instance.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#State_1)),
      "stateUpdateTime": string,
      "stateReasons": [
        enum ([StateReason](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#StateReason))
      ],
      "peerInstance": string,
      "lastActiveSyncTime": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#State_1)`)` Output only. The replica state.  
`stateUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the replica state was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stateReasons[]` |  `enum (`[StateReason](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#StateReason)`)` Output only. Additional information about the replication state, if available.  
`peerInstance` |  `string` The name of the source instance for the replica, in the format `projects/{project}/locations/{location}/instances/{instance}`. This field is required when creating a replica.  
`lastActiveSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of the latest replication snapshot taken on the active instance and is already replicated safely.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The replica state.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | The replica is being created.  
`READY` | The replica is ready.  
`REMOVING` | The replica is being removed.  
`FAILED` | The replica is experiencing an issue and might be unusable. You can get further details from the `stateReasons` field of the `ReplicaConfig` object.  
`PROMOTING` | The replica is being promoted.  
`PAUSING` | The replica is being paused.  
`PAUSED` | The replica is paused.  
`RESUMING` | The replica is being resumed.  
  
## StateReason

Enums  
---  
`STATE_REASON_UNSPECIFIED` | Reason not specified.  
`PEER_INSTANCE_UNREACHABLE` | The peer instance is unreachable.  
`REMOVE_FAILED` | The remove replica peer instance operation failed.  
`PAUSE_FAILED` | The pause replica operation failed.  
`RESUME_FAILED` | The resume replica operation failed.  
  
## PerformanceConfig

Used for setting the performance configuration. If the user doesn't specify PerformanceConfig, automatically provision the default performance settings as described in <https://cloud.google.com/filestore/docs/performance>. Larger instances will be linearly set to more IOPS. If the instance's capacity is increased or decreased, its performance will be automatically adjusted upwards or downwards accordingly (respectively).

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "iopsPerTb": {
        object ([IOPSPerTB](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#IOPSPerTB))
      },
      "fixedIops": {
        object ([FixedIOPS](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#FixedIOPS))
      }
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`.`mode` can be only one of the following:  
`iopsPerTb` |  `object (`[IOPSPerTB](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#IOPSPerTB)`)` Provision IOPS dynamically based on the capacity of the instance. Provisioned IOPS will be calculated by multiplying the capacity of the instance in TiB by the `iopsPerTb` value. For example, for a 2 TiB instance with an `iopsPerTb` value of 17000 the provisioned IOPS will be 34000.If the calculated value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.  
`fixedIops` |  `object (`[FixedIOPS](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances#FixedIOPS)`)` Choose a fixed provisioned IOPS value for the instance, which will remain constant regardless of instance capacity. Value must be a multiple of 1000.If the chosen value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.  
  
## IOPSPerTB

IOPS per TB. Filestore defines TB as 1024^4 bytes (TiB).

JSON representation  
---  
      
    
    {
      "maxIopsPerTb": string
    }  
  
Fields  
---  
`maxIopsPerTb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Maximum IOPS per TiB.  
  
## FixedIOPS

Fixed IOPS (input/output operations per second) parameters.

JSON representation  
---  
      
    
    {
      "maxIops": string
    }  
  
Fields  
---  
`maxIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Maximum IOPS.  
  
## PerformanceLimits

The enforced performance limits, calculated from the instance's performance configuration.

JSON representation  
---  
      
    
    {
      "maxIops": string,
      "maxReadIops": string,
      "maxWriteIops": string,
      "maxReadThroughputBps": string,
      "maxWriteThroughputBps": string
    }  
  
Fields  
---  
`maxIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum IOPS.  
`maxReadIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum read IOPS.  
`maxWriteIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum write IOPS.  
`maxReadThroughputBps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum read throughput in bytes per second.  
`maxWriteThroughputBps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximumwrite throughput in bytes per second.  
  
## BackendType

BackendType contains the possible backend types for an instance.

Enums  
---  
`BACKEND_TYPE_UNSPECIFIED` | Backend type not set.  
`COMPUTE_BASED_BACKEND` | Instance is backed by Compute.  
`FILESTORE_BACKEND` | Instance is backed by Filestore.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create)`

|  Creates an instance.  
  
### `[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/delete)`

|  Deletes an instance.  
  
### `[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/get)`

|  Gets the details of a specific instance.  
  
### `[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/list)`

|  Lists all instances in a project for either a specified location or for all locations.  
  
### `[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/patch)`

|  Updates the settings of a specific instance.  
  
### `[pauseReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/pauseReplica)`

|  Pause the standby instance (replica).  
  
### `[promoteReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/promoteReplica)`

|  Promote the standby instance (replica).  
  
### `[restore](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/restore)`

|  Restores an existing instance's file share from a backup.  
  
### `[resumeReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/resumeReplica)`

|  Resume the standby instance (replica).  
  
### `[revert](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/revert)`

|  Revert an existing instance's file system to a specified snapshot.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-21 UTC."],[],[]] 
