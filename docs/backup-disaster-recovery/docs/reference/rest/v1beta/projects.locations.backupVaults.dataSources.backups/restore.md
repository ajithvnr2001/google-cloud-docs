---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore/
title: Method: projects.locations.backupVaults.dataSources.backups.restore \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:46.434034+00:00
---

# Method: projects.locations.backupVaults.dataSources.backups.restore  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Method: projects.locations.backupVaults.dataSources.backups.restore Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * ComputeInstanceTargetEnvironment
    * JSON representation
  * DiskTargetEnvironment
    * JSON representation
  * RegionDiskTargetEnvironment
    * JSON representation
  * ComputeInstanceRestoreProperties
    * JSON representation
  * AdvancedMachineFeatures
    * JSON representation
  * ConfidentialInstanceConfig
    * JSON representation
  * DisplayDevice
    * JSON representation
  * NetworkPerformanceConfig
    * JSON representation
  * Tier
  * InstanceParams
    * JSON representation
  * InstancePrivateIpv6GoogleAccess
  * AllocationAffinity
    * JSON representation
  * Type
  * DiskRestoreProperties
    * JSON representation
  * RestoreDiskFromInstanceOptions
    * JSON representation
  * AccessMode
  * Architecture
  * Try it!



Restore from a Backup

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west10europe-west12me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8useu

  
`POST https://backupdr.googleapis.com/v1beta/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}:restore`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requestId": string,
    
      // Union field target_environment can be only one of the following:
      "computeInstanceTargetEnvironment": {
        object ([ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ComputeInstanceTargetEnvironment))
      },
      "diskTargetEnvironment": {
        object ([DiskTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DiskTargetEnvironment))
      },
      "regionDiskTargetEnvironment": {
        object ([RegionDiskTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#RegionDiskTargetEnvironment))
      }
      // End of list of possible types for union field target_environment.
    
      // Union field instance_properties can be only one of the following:
      "computeInstanceRestoreProperties": {
        object ([ComputeInstanceRestoreProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ComputeInstanceRestoreProperties))
      },
      "diskRestoreProperties": {
        object ([DiskRestoreProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DiskRestoreProperties))
      }
      // End of list of possible types for union field instance_properties.
      "clearOverridesFieldMask": string
    }  
  
Fields  
---  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
Union field `target_environment`. The target environment for the restore operation. `target_environment` can be only one of the following:  
`computeInstanceTargetEnvironment` |  `object (`[ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ComputeInstanceTargetEnvironment)`)` Compute Engine target environment to be used during restore.  
`diskTargetEnvironment` |  `object (`[DiskTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DiskTargetEnvironment)`)` Disk target environment to be used during restore.  
`regionDiskTargetEnvironment` |  `object (`[RegionDiskTargetEnvironment](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#RegionDiskTargetEnvironment)`)` Region disk target environment to be used during restore.  
Union field `instance_properties`. The property overrides for the instance being restored. `instance_properties` can be only one of the following:  
`computeInstanceRestoreProperties` |  `object (`[ComputeInstanceRestoreProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ComputeInstanceRestoreProperties)`)` Compute Engine instance properties to be overridden during restore.  
`diskRestoreProperties` |  `object (`[DiskRestoreProperties](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DiskRestoreProperties)`)` Disk properties to be overridden during restore.  
`clearOverridesFieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.The most common current use case is clearing default encryption keys.Examples of field mask paths: - Compute Instance Disks: `computeInstanceRestoreProperties.disks.*.disk_encryption_key` \- Single Disk: `diskRestoreProperties.disk_encryption_key`This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-backupdr`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `backupdr.bvbackups.restore`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ComputeInstanceTargetEnvironment

ComputeInstanceTargetEnvironment represents Compute Engine target environment to be used during restore.

JSON representation  
---  
      
    
    {
      "project": string,
      "zone": string,
      "useProjectServiceAccount": boolean
    }  
  
Fields  
---  
`project` |  `string` Required. Target project for the Compute Engine instance.  
`zone` |  `string` Required. The zone of the Compute Engine instance.  
`useProjectServiceAccount` |  `boolean` Optional. Whether to use the project service account for the Compute Engine instance restore.  
  
## DiskTargetEnvironment

DiskTargetEnvironment represents the target environment for the disk.

JSON representation  
---  
      
    
    {
      "project": string,
      "zone": string,
      "useProjectServiceAccount": boolean
    }  
  
Fields  
---  
`project` |  `string` Required. Target project for the disk.  
`zone` |  `string` Required. Target zone for the disk.  
`useProjectServiceAccount` |  `boolean` Optional. Whether to use the project service account for the disk restore.  
  
## RegionDiskTargetEnvironment

RegionDiskTargetEnvironment represents the target environment for the disk.

JSON representation  
---  
      
    
    {
      "project": string,
      "region": string,
      "replicaZones": [
        string
      ],
      "useProjectServiceAccount": boolean
    }  
  
Fields  
---  
`project` |  `string` Required. Target project for the disk.  
`region` |  `string` Required. Target region for the disk.  
`replicaZones[]` |  `string` Required. Target URLs of the replica zones for the disk.  
`useProjectServiceAccount` |  `boolean` Optional. Whether to use the project service account for the disk restore.  
  
## ComputeInstanceRestoreProperties

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

JSON representation  
---  
      
    
    {
      "disks": [
        {
          object ([AttachedDisk](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#AttachedDisk))
        }
      ],
      "guestAccelerators": [
        {
          object ([AcceleratorConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#AcceleratorConfig))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#NetworkInterface))
        }
      ],
      "resourcePolicies": [
        string
      ],
      "serviceAccounts": [
        {
          object ([ServiceAccount](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#ServiceAccount))
        }
      ],
      "name": string,
      "advancedMachineFeatures": {
        object ([AdvancedMachineFeatures](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AdvancedMachineFeatures))
      },
      "canIpForward": boolean,
      "confidentialInstanceConfig": {
        object ([ConfidentialInstanceConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ConfidentialInstanceConfig))
      },
      "deletionProtection": boolean,
      "description": string,
      "displayDevice": {
        object ([DisplayDevice](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DisplayDevice))
      },
      "hostname": string,
      "instanceEncryptionKey": {
        object ([CustomerEncryptionKey](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#CustomerEncryptionKey))
      },
      "keyRevocationActionType": enum ([KeyRevocationActionType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#KeyRevocationActionType)),
      "machineType": string,
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Metadata))
      },
      "minCpuPlatform": string,
      "networkPerformanceConfig": {
        object ([NetworkPerformanceConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#NetworkPerformanceConfig))
      },
      "params": {
        object ([InstanceParams](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#InstanceParams))
      },
      "privateIpv6GoogleAccess": enum ([InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#InstancePrivateIpv6GoogleAccess)),
      "reservationAffinity": {
        object ([AllocationAffinity](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AllocationAffinity))
      },
      "scheduling": {
        object ([Scheduling](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Scheduling))
      },
      "tags": {
        object ([Tags](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Tags))
      }
    }  
  
Fields  
---  
`disks[]` |  `object (`[AttachedDisk](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#AttachedDisk)`)` Optional. Array of disks associated with this instance. Persistent disks must be created before you can assign them. Source regional persistent disks will be restored with default replica zones if not specified.  
`guestAccelerators[]` |  `object (`[AcceleratorConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#AcceleratorConfig)`)` Optional. A list of the type and count of accelerator cards attached to the instance.  
`labels` |  `map (key: string, value: string)` Optional. Labels to apply to this instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#NetworkInterface)`)` Optional. An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. Required to restore in different project or region.  
`resourcePolicies[]` |  `string` Optional. Resource policies applied to this instance. By default, no resource policies will be applied.  
`serviceAccounts[]` |  `object (`[ServiceAccount](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#ServiceAccount)`)` Optional. A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported.  
`name` |  `string` Required. Name of the compute instance.  
`advancedMachineFeatures` |  `object (`[AdvancedMachineFeatures](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AdvancedMachineFeatures)`)` Optional. Controls for advanced machine-related behavior features.  
`canIpForward` |  `boolean` Optional. Allows this instance to send and receive packets with non-matching destination or source IPs.  
`confidentialInstanceConfig` |  `object (`[ConfidentialInstanceConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#ConfidentialInstanceConfig)`)` Optional. Controls Confidential compute options on the instance  
`deletionProtection` |  `boolean` Optional. Whether the resource should be protected against deletion.  
`description` |  `string` Optional. An optional description of this resource. Provide this property when you create the resource.  
`displayDevice` |  `object (`[DisplayDevice](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#DisplayDevice)`)` Optional. Enables display device for the instance.  
`hostname` |  `string` Optional. Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS.  
`instanceEncryptionKey` |  `object (`[CustomerEncryptionKey](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#CustomerEncryptionKey)`)` Optional. Encrypts suspended data for an instance with a customer-managed encryption key.  
`keyRevocationActionType` |  `enum (`[KeyRevocationActionType](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#KeyRevocationActionType)`)` Optional. KeyRevocationActionType of the instance.  
`machineType` |  `string` Optional. Full or partial URL of the machine type resource to use for this instance.  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Metadata)`)` Optional. This includes custom metadata and predefined keys.  
`minCpuPlatform` |  `string` Optional. Minimum CPU platform to use for this instance.  
`networkPerformanceConfig` |  `object (`[NetworkPerformanceConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#NetworkPerformanceConfig)`)` Optional. Configure network performance such as egress bandwidth tier.  
`params` |  `object (`[InstanceParams](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#InstanceParams)`)` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`privateIpv6GoogleAccess` |  `enum (`[InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#InstancePrivateIpv6GoogleAccess)`)` Optional. The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default.  
`reservationAffinity` |  `object (`[AllocationAffinity](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AllocationAffinity)`)` Optional. Specifies the reservations that this instance can consume from.  
`scheduling` |  `object (`[Scheduling](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Scheduling)`)` Optional. Sets the scheduling options for this instance.  
`tags` |  `object (`[Tags](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#Tags)`)` Optional. Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation.  
  
## AdvancedMachineFeatures

Specifies options for controlling advanced machine features.

JSON representation  
---  
      
    
    {
      "enableNestedVirtualization": boolean,
      "threadsPerCore": integer,
      "visibleCoreCount": integer,
      "enableUefiNetworking": boolean
    }  
  
Fields  
---  
`enableNestedVirtualization` |  `boolean` Optional. Whether to enable nested virtualization or not (default is false).  
`threadsPerCore` |  `integer` Optional. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.  
`visibleCoreCount` |  `integer` Optional. The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width.  
`enableUefiNetworking` |  `boolean` Optional. Whether to enable UEFI networking for instance creation.  
  
## ConfidentialInstanceConfig

A set of Confidential Instance options.

JSON representation  
---  
      
    
    {
      "enableConfidentialCompute": boolean
    }  
  
Fields  
---  
`enableConfidentialCompute` |  `boolean` Optional. Defines whether the instance should have confidential compute enabled.  
  
## DisplayDevice

A set of Display Device options

JSON representation  
---  
      
    
    {
      "enableDisplay": boolean
    }  
  
Fields  
---  
`enableDisplay` |  `boolean` Optional. Enables display for the Compute Engine VM  
  
## NetworkPerformanceConfig

Network performance configuration.

JSON representation  
---  
      
    
    {
      "totalEgressBandwidthTier": enum ([Tier](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Tier))
    }  
  
Fields  
---  
`totalEgressBandwidthTier` |  `enum (`[Tier](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Tier)`)` Optional. The tier of the total egress bandwidth.  
  
## Tier

Network performance tier.

Enums  
---  
`TIER_UNSPECIFIED` | This value is unused.  
`DEFAULT` | Default network performance config.  
`TIER_1` | Tier 1 network performance config.  
  
## InstanceParams

Additional instance params.

JSON representation  
---  
      
    
    {
      "resourceManagerTags": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`resourceManagerTags` |  `map (key: string, value: string)` Optional. Resource manager tags to be bound to the instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## InstancePrivateIpv6GoogleAccess

The private IPv6 google access type for the VMs.

Enums  
---  
`INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED` | Default value. This value is unused.  
`INHERIT_FROM_SUBNETWORK` | Each network interface inherits PrivateIpv6GoogleAccess from its subnetwork.  
`ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE` | Outbound private IPv6 access from VMs in this subnet to Google services. If specified, the subnetwork who is attached to the instance's default network interface will be assigned an internal IPv6 prefix if it doesn't have before.  
`ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE` | Bidirectional private IPv6 access to/from Google services. If specified, the subnetwork who is attached to the instance's default network interface will be assigned an internal IPv6 prefix if it doesn't have before.  
  
## AllocationAffinity

Specifies the reservations that this instance can consume from.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ],
      "consumeReservationType": enum ([Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Type)),
      "key": string
    }  
  
Fields  
---  
`values[]` |  `string` Optional. Corresponds to the label values of a reservation resource.  
`consumeReservationType` |  `enum (`[Type](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Type)`)` Optional. Specifies the type of reservation from which this instance can consume  
`key` |  `string` Optional. Corresponds to the label key of a reservation resource.  
  
## Type

Indicates whether to consume from a reservation or not.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`NO_RESERVATION` | Do not consume from any allocated capacity.  
`ANY_RESERVATION` | Consume any allocation available.  
`SPECIFIC_RESERVATION` | Must consume from a specific reservation. Must specify key value fields for specifying the reservations.  
  
## DiskRestoreProperties

DiskRestoreProperties represents the properties of a Disk restore.

JSON representation  
---  
      
    
    {
      "licenses": [
        string
      ],
      "guestOsFeature": [
        {
          object ([GuestOsFeature](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#GuestOsFeature))
        }
      ],
      "resourcePolicy": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "resourceManagerTags": {
        string: string,
        ...
      },
    
      // Union field source_options can be only one of the following:
      "instanceBackupSource": {
        object ([RestoreDiskFromInstanceOptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#RestoreDiskFromInstanceOptions))
      }
      // End of list of possible types for union field source_options.
      "name": string,
      "description": string,
      "sizeGb": string,
      "diskEncryptionKey": {
        object ([CustomerEncryptionKey](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#CustomerEncryptionKey))
      },
      "physicalBlockSizeBytes": string,
      "provisionedIops": string,
      "provisionedThroughput": string,
      "enableConfidentialCompute": boolean,
      "storagePool": string,
      "accessMode": enum ([AccessMode](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AccessMode)),
      "architecture": enum ([Architecture](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Architecture)),
      "type": string
    }  
  
Fields  
---  
`licenses[]` |  `string` Optional. A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image  
`guestOsFeature[]` |  `object (`[GuestOsFeature](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#GuestOsFeature)`)` Optional. A list of features to enable in the guest operating system. This is applicable only for bootable images.  
`resourcePolicy[]` |  `string` Optional. Resource policies applied to this disk.  
`labels` |  `map (key: string, value: string)` Optional. Labels to apply to this disk. These can be modified later using `setLabels` method. Label values can be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`resourceManagerTags` |  `map (key: string, value: string)` Optional. Resource manager tags to be bound to the disk.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `source_options`. Specifies the source of the restore. This is required for selective or cross-workload restores. `source_options` can be only one of the following:  
`instanceBackupSource` |  `object (`[RestoreDiskFromInstanceOptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#RestoreDiskFromInstanceOptions)`)` Options for creating a disk from a source Compute Instance backup.  
`name` |  `string` Required. Name of the disk.  
`description` |  `string` Optional. An optional description of this resource. Provide this property when you create the resource.  
`sizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The size of the disk in GB.  
`diskEncryptionKey` |  `object (`[CustomerEncryptionKey](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups#CustomerEncryptionKey)`)` Optional. Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key.  
`physicalBlockSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently, the supported size is 4096.  
`provisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle.  
`provisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput MB per second that the disk can handle.  
`enableConfidentialCompute` |  `boolean` Optional. Indicates whether this disk is using confidential compute mode. Encryption with a Cloud KMS key is required to enable this option.  
`storagePool` |  `string` Optional. The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource.  
`accessMode` |  `enum (`[AccessMode](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#AccessMode)`)` Optional. The access mode of the disk.  
`architecture` |  `enum (`[Architecture](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupVaults.dataSources.backups/restore#Architecture)`)` Optional. The architecture of the source disk. Valid values are ARM64 or X86_64.  
`type` |  `string` Required. URL of the disk type resource describing which disk type to use to create the disk.  
  
## RestoreDiskFromInstanceOptions

Options for creating a disk from a source Compute Instance backup.

JSON representation  
---  
      
    
    {
    
      // Union field source_disk can be only one of the following:
      "sourceDeviceName": string,
      "bootDisk": boolean
      // End of list of possible types for union field source_disk.
    }  
  
Fields  
---  
Union field `source_disk`. Required: The disk to be restored from the instance backup. `source_disk` can be only one of the following:  
`sourceDeviceName` |  `string` The device name of the disk to restore from the VM backup.  
`bootDisk` |  `boolean` Set to true to restore the boot disk from the instance backup. This field should only be set to true if selected.  
  
## AccessMode

The supported access modes of the disk.

Enums  
---  
`READ_WRITE_SINGLE` | The default AccessMode, means the disk can be attached to single instance in RW mode.  
`READ_WRITE_MANY` | The AccessMode means the disk can be attached to multiple instances in RW mode.  
`READ_ONLY_MANY` | The AccessMode means the disk can be attached to multiple instances in RO mode.  
  
## Architecture

Architecture of the source disk.

Enums  
---  
`ARCHITECTURE_UNSPECIFIED` | Default value. This value is unused.  
`X86_64` | Disks with architecture X86_64  
`ARM64` | Disks with architecture ARM64  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
