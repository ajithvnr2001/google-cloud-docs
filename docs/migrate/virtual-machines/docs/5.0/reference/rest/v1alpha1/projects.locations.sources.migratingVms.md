---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms
title: REST Resource: projects.locations.sources.migratingVms \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:46.134555+00:00
---

# REST Resource: projects.locations.sources.migratingVms  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.migratingVms Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MigratingVm
    * JSON representation
  * ComputeEngineTargetDefaults
    * JSON representation
  * ComputeEngineDisksTargetDefaults
    * JSON representation
  * DisksMigrationDisksTargetDefaults
  * DisksMigrationVmTargetDefaults
    * JSON representation
  * BootDiskDefaults
    * JSON representation
  * DiskImageDefaults
    * JSON representation
  * PersistentDiskDefaults
    * JSON representation
  * VmAttachmentDetails
    * JSON representation
  * VmwareSourceVmDetails
    * JSON representation
  * Firmware
  * VmwareDiskDetails
    * JSON representation
  * VmCapabilities
    * JSON representation
  * OsCapability
  * AwsSourceVmDetails
    * JSON representation
  * Firmware
  * AwsDiskDetails
    * JSON representation
  * AzureSourceVmDetails
    * JSON representation
  * Firmware
  * AzureDiskDetails
    * JSON representation
  * SchedulePolicy
    * JSON representation
  * ReplicationSync
    * JSON representation
  * State
  * CutoverForecast
    * JSON representation
  * Methods



## Resource: MigratingVm

MigratingVm describes the VM that will be migrated from a Source environment and its replication state.

JSON representation  
---  
      
    
    {
      "name": string,
      "sourceVmId": string,
      "displayName": string,
      "description": string,
      "targetDefaults": {
        object ([TargetVMDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails))
      },
      "policy": {
        object ([SchedulePolicy](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#SchedulePolicy))
      },
      "createTime": string,
      "updateTime": string,
      "lastSync": {
        object ([ReplicationSync](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ReplicationSync))
      },
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#State)),
      "stateTime": string,
      "currentSyncInfo": {
        object ([ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle))
      },
      "lastReplicationCycle": {
        object ([ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle))
      },
      "group": string,
      "labels": {
        string: string,
        ...
      },
      "recentCloneJobs": [
        {
          object ([CloneJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs#CloneJob))
        }
      ],
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status))
      },
      "recentCutoverJobs": [
        {
          object ([CutoverJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob))
        }
      ],
      "cutoverForecast": {
        object ([CutoverForecast](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#CutoverForecast))
      },
    
      // Union field target can be only one of the following:
      "computeEngineVmDefaults": {
        object ([TargetVMDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails))
      }
      // End of list of possible types for union field target.
    
      // Union field target_vm_defaults can be only one of the following:
      "computeEngineTargetDefaults": {
        object ([ComputeEngineTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ComputeEngineTargetDefaults))
      },
      "computeEngineDisksTargetDefaults": {
        object ([ComputeEngineDisksTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ComputeEngineDisksTargetDefaults))
      }
      // End of list of possible types for union field target_vm_defaults.
    
      // Union field source_vm_details can be only one of the following:
      "vmwareSourceVmDetails": {
        object ([VmwareSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmwareSourceVmDetails))
      },
      "awsSourceVmDetails": {
        object ([AwsSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AwsSourceVmDetails))
      },
      "azureSourceVmDetails": {
        object ([AzureSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AzureSourceVmDetails))
      }
      // End of list of possible types for union field source_vm_details.
    }  
  
Fields  
---  
`name` |  `string` Output only. The identifier of the MigratingVm.  
`sourceVmId` |  `string` The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-.  
`displayName` |  `string` The display name attached to the MigratingVm by the user.  
`description` |  `string` The description attached to the migrating VM by the user.  
`targetDefaults  
**(deprecated)**` |  `object (`[TargetVMDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails)`)` This item is deprecated!The default configuration of the target VM that will be created in Google Cloud as a result of the migration. Deprecated: Use computeEngineTargetDefaults instead.  
`policy` |  `object (`[SchedulePolicy](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#SchedulePolicy)`)` The replication schedule policy.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time the migrating VM resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`lastSync` |  `object (`[ReplicationSync](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ReplicationSync)`)` Output only. The most updated snapshot created time in the source that finished replication.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#State)`)` Output only. State of the MigratingVm.  
`stateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time the migrating VM state was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`currentSyncInfo` |  `object (`[ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle)`)` Output only. Details of the current running replication cycle.  
`lastReplicationCycle` |  `object (`[ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle)`)` Output only. Details of the last replication cycle. This will be updated whenever a replication cycle is finished and is not to be confused with lastSync which is only updated on successful replication cycles.  
`group` |  `string` Output only. The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate `[Group](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups#Group)` resource.  
`labels` |  `map (key: string, value: string)` The labels of the migrating VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`recentCloneJobs[]` |  `object (`[CloneJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs#CloneJob)`)` Output only. The recent `[clone jobs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs#CloneJob)` performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status)`)` Output only. Provides details on the state of the Migrating VM in case of an error in replication.  
`recentCutoverJobs[]` |  `object (`[CutoverJob](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob)`)` Output only. The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request.  
`cutoverForecast` |  `object (`[CutoverForecast](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#CutoverForecast)`)` Output only. Provides details of future CutoverJobs of a MigratingVm. Set to empty when cutover forecast is unavailable.  
Union field `target`. The default configuration of the target VM that will be created in Google Cloud as a result of the migration. `target` can be only one of the following:  
`computeEngineVmDefaults  
**(deprecated)**` |  `object (`[TargetVMDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails)`)` This item is deprecated!Details of the VM in Compute Engine. Deprecated: Use computeEngineTargetDefaults instead.  
Union field `target_vm_defaults`. The default configuration of the target VM that will be created in Google Cloud as a result of the migration. `target_vm_defaults` can be only one of the following:  
`computeEngineTargetDefaults` |  `object (`[ComputeEngineTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ComputeEngineTargetDefaults)`)` Details of the target VM in Compute Engine.  
`computeEngineDisksTargetDefaults` |  `object (`[ComputeEngineDisksTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#ComputeEngineDisksTargetDefaults)`)` Details of the target Persistent Disks in Compute Engine.  
Union field `source_vm_details`. Details about the source VM. `source_vm_details` can be only one of the following:  
`vmwareSourceVmDetails` |  `object (`[VmwareSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmwareSourceVmDetails)`)` Output only. Details of the VM from a Vmware source.  
`awsSourceVmDetails` |  `object (`[AwsSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AwsSourceVmDetails)`)` Output only. Details of the VM from an AWS source.  
`azureSourceVmDetails` |  `object (`[AzureSourceVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AzureSourceVmDetails)`)` Output only. Details of the VM from an Azure source.  
  
## ComputeEngineTargetDefaults

ComputeEngineTargetDefaults is a collection of details for creating a VM in a target Compute Engine project.

JSON representation  
---  
      
    
    {
      "vmName": string,
      "targetProject": string,
      "zone": string,
      "machineTypeSeries": string,
      "machineType": string,
      "networkTags": [
        string
      ],
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface))
        }
      ],
      "serviceAccount": string,
      "diskType": enum ([ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)),
      "labels": {
        string: string,
        ...
      },
      "licenseType": enum ([ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineLicenseType)),
      "appliedLicense": {
        object ([AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense))
      },
      "computeScheduling": {
        object ([ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling))
      },
      "secureBoot": boolean,
      "enableVtpm": boolean,
      "enableIntegrityMonitoring": boolean,
      "bootOption": enum ([ComputeEngineBootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineBootOption)),
      "metadata": {
        string: string,
        ...
      },
      "additionalLicenses": [
        string
      ],
      "hostname": string,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
      "bootConversion": enum ([BootConversion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/BootConversion))
    }  
  
Fields  
---  
`vmName` |  `string` The name of the VM to create.  
`targetProject` |  `string` The full path of the resource of type TargetProject which represents the Compute Engine project in which to create this VM.  
`zone` |  `string` The zone in which to create the VM.  
`machineTypeSeries` |  `string` The machine type series to create the VM with.  
`machineType` |  `string` The machine type to create the VM with.  
`networkTags[]` |  `string` A list of network tags to associate with the VM.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface)`)` List of NICs connected to this VM.  
`serviceAccount` |  `string` The service account to associate the VM with.  
`diskType` |  `enum (`[ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)`)` The disk type to use in the VM.  
`labels` |  `map (key: string, value: string)` A map of labels to associate with the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`licenseType` |  `enum (`[ComputeEngineLicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineLicenseType)`)` The license type to use in OS adaptation.  
`appliedLicense` |  `object (`[AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense)`)` Output only. The OS license returned from the adaptation module report.  
`computeScheduling` |  `object (`[ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling)`)` Compute instance scheduling information (if empty default is used).  
`secureBoot` |  `boolean` Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.  
`enableVtpm` |  `boolean` Optional. Defines whether the instance has vTPM enabled. This can be set to true only if the VM boot option is EFI.  
`enableIntegrityMonitoring` |  `boolean` Optional. Defines whether the instance has integrity monitoring enabled. This can be set to true only if the VM boot option is EFI, and vTPM is enabled.  
`bootOption` |  `enum (`[ComputeEngineBootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineBootOption)`)` Output only. The VM Boot Option, as set in the source VM.  
`metadata` |  `map (key: string, value: string)` The metadata key/value pairs to assign to the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`additionalLicenses[]` |  `string` Additional licenses to assign to the VM.  
`hostname` |  `string` The hostname to assign to the VM.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. Immutable. The encryption to apply to the VM disks.  
`bootConversion` |  `enum (`[BootConversion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/BootConversion)`)` Optional. By default the virtual machine will keep its existing boot option. Setting this property will trigger an internal process which will convert the virtual machine from using the existing boot option to another.  
  
## ComputeEngineDisksTargetDefaults

ComputeEngineDisksTargetDefaults is a collection of details for creating Persistent Disks in a target Compute Engine project.

JSON representation  
---  
      
    
    {
      "targetProject": string,
      "disks": [
        {
          object ([PersistentDiskDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#PersistentDiskDefaults))
        }
      ],
    
      // Union field location can be only one of the following:
      "zone": string
      // End of list of possible types for union field location.
    
      // Union field vm_target can be only one of the following:
      "disksTargetDefaults": {
        object ([DisksMigrationDisksTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DisksMigrationDisksTargetDefaults))
      },
      "vmTargetDefaults": {
        object ([DisksMigrationVmTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DisksMigrationVmTargetDefaults))
      }
      // End of list of possible types for union field vm_target.
    }  
  
Fields  
---  
`targetProject` |  `string` The full path of the resource of type TargetProject which represents the Compute Engine project in which to create the Persistent Disks.  
`disks[]` |  `object (`[PersistentDiskDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#PersistentDiskDefaults)`)` The details of each Persistent Disk to create.  
Union field `location`.`location` can be only one of the following:  
`zone` |  `string` The zone in which to create the Persistent Disks.  
Union field `vm_target`. Details of the VM to attach the disks to as the target of this migration. `vm_target` can be only one of the following:  
`disksTargetDefaults` |  `object (`[DisksMigrationDisksTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DisksMigrationDisksTargetDefaults)`)` Details of the disk only migration target.  
`vmTargetDefaults` |  `object (`[DisksMigrationVmTargetDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DisksMigrationVmTargetDefaults)`)` Details of the VM migration target.  
  
## DisksMigrationDisksTargetDefaults

This type has no fields.

Details for a disk only migration.

## DisksMigrationVmTargetDefaults

Details for creation of a VM that migrated data disks will be attached to.

JSON representation  
---  
      
    
    {
      "vmName": string,
      "machineTypeSeries": string,
      "machineType": string,
      "networkTags": [
        string
      ],
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface))
        }
      ],
      "serviceAccount": string,
      "computeScheduling": {
        object ([ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling))
      },
      "secureBoot": boolean,
      "enableVtpm": boolean,
      "enableIntegrityMonitoring": boolean,
      "metadata": {
        string: string,
        ...
      },
      "additionalLicenses": [
        string
      ],
      "hostname": string,
      "labels": {
        string: string,
        ...
      },
      "bootDiskDefaults": {
        object ([BootDiskDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#BootDiskDefaults))
      },
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      }
    }  
  
Fields  
---  
`vmName` |  `string` Required. The name of the VM to create.  
`machineTypeSeries` |  `string` Optional. The machine type series to create the VM with. For presentation only.  
`machineType` |  `string` Required. The machine type to create the VM with.  
`networkTags[]` |  `string` Optional. A list of network tags to associate with the VM.  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface)`)` Optional. NICs to attach to the VM.  
`serviceAccount` |  `string` Optional. The service account to associate the VM with.  
`computeScheduling` |  `object (`[ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling)`)` Optional. Compute instance scheduling information (if empty default is used).  
`secureBoot` |  `boolean` Optional. Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.  
`enableVtpm` |  `boolean` Optional. Defines whether the instance has vTPM enabled.  
`enableIntegrityMonitoring` |  `boolean` Optional. Defines whether the instance has integrity monitoring enabled.  
`metadata` |  `map (key: string, value: string)` Optional. The metadata key/value pairs to assign to the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`additionalLicenses[]` |  `string` Optional. Additional licenses to assign to the VM.  
`hostname` |  `string` Optional. The hostname to assign to the VM.  
`labels` |  `map (key: string, value: string)` Optional. A map of labels to associate with the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`bootDiskDefaults` |  `object (`[BootDiskDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#BootDiskDefaults)`)` Optional. Details of the boot disk of the VM.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. The encryption to apply to the VM.  
  
## BootDiskDefaults

BootDiskDefaults hold information about the boot disk of a VM.

JSON representation  
---  
      
    
    {
      "diskName": string,
      "diskType": enum ([ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)),
      "deviceName": string,
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
    
      // Union field source can be only one of the following:
      "image": {
        object ([DiskImageDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DiskImageDefaults))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`diskName` |  `string` Optional. The name of the disk.  
`diskType` |  `enum (`[ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)`)` Optional. The type of disk provisioning to use for the VM.  
`deviceName` |  `string` Optional. Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-* tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. The encryption to apply to the boot disk.  
Union field `source`.`source` can be only one of the following:  
`image` |  `object (`[DiskImageDefaults](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#DiskImageDefaults)`)` The image to use when creating the disk.  
  
## DiskImageDefaults

Contains details about the image source used to create the disk.

JSON representation  
---  
      
    
    {
      "sourceImage": string
    }  
  
Fields  
---  
`sourceImage` |  `string` Required. The Image resource used when creating the disk.  
  
## PersistentDiskDefaults

Details for creation of a Persistent Disk.

JSON representation  
---  
      
    
    {
      "sourceDiskNumber": integer,
      "diskName": string,
      "diskType": enum ([ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)),
      "additionalLabels": {
        string: string,
        ...
      },
      "encryption": {
        object ([Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption))
      },
      "vmAttachmentDetails": {
        object ([VmAttachmentDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmAttachmentDetails))
      }
    }  
  
Fields  
---  
`sourceDiskNumber` |  `integer` Required. The ordinal number of the source VM disk.  
`diskName` |  `string` Optional. The name of the Persistent Disk to create.  
`diskType` |  `enum (`[ComputeEngineDiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeEngineDiskType)`)` The disk type to use.  
`additionalLabels` |  `map (key: string, value: string)` A map of labels to associate with the Persistent Disk.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`encryption` |  `object (`[Encryption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Encryption)`)` Optional. The encryption to apply to the disk.  
`vmAttachmentDetails` |  `object (`[VmAttachmentDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmAttachmentDetails)`)` Optional. Details for attachment of the disk to a VM. Used when the disk is set to be attached to a target VM.  
  
## VmAttachmentDetails

Details for attachment of the disk to a VM.

JSON representation  
---  
      
    
    {
      "deviceName": string
    }  
  
Fields  
---  
`deviceName` |  `string` Optional. Specifies a unique device name of your choice that is reflected into the /dev/disk/by-id/google-* tree of a Linux operating system running within the instance. If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks.  
  
## VmwareSourceVmDetails

Represent the source Vmware VM details.

JSON representation  
---  
      
    
    {
      "firmware": enum ([Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware)),
      "committedStorageBytes": string,
      "disks": [
        {
          object ([VmwareDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmwareDiskDetails))
        }
      ],
      "vmCapabilitiesInfo": {
        object ([VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities))
      }
    }  
  
Fields  
---  
`firmware` |  `enum (`[Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware)`)` Output only. The firmware type of the source VM.  
`committedStorageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total size of the disks being migrated in bytes.  
`disks[]` |  `object (`[VmwareDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmwareDiskDetails)`)` Output only. The disks attached to the source VM.  
`vmCapabilitiesInfo` |  `object (`[VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities)`)` Output only. Information about VM capabilities needed for some Compute Engine features.  
  
## Firmware

Possible values for Vmware VM firmware.

Enums  
---  
`FIRMWARE_UNSPECIFIED` | The firmware is unknown.  
`EFI` | The firmware is EFI.  
`BIOS` | The firmware is BIOS.  
  
## VmwareDiskDetails

The details of a Vmware VM disk.

JSON representation  
---  
      
    
    {
      "diskNumber": integer,
      "sizeGb": string,
      "label": string
    }  
  
Fields  
---  
`diskNumber` |  `integer` Output only. The ordinal number of the disk.  
`sizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size in GB.  
`label` |  `string` Output only. The disk label.  
  
## VmCapabilities

Migrating VM source information about the VM capabilities needed for some Compute Engine features.

JSON representation  
---  
      
    
    {
      "osCapabilities": [
        enum ([OsCapability](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#OsCapability))
      ],
      "lastOsCapabilitiesUpdateTime": string
    }  
  
Fields  
---  
`osCapabilities[]` |  `enum (`[OsCapability](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#OsCapability)`)` Output only. Unordered list. List of certain VM OS capabilities needed for some Compute Engine features.  
`lastOsCapabilitiesUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time OS capabilities list was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## OsCapability

VM operating system (OS) capabilities needed for determining compatibility with Compute Engine features supported by the migration.

Enums  
---  
`OS_CAPABILITY_UNSPECIFIED` | This is for API compatibility only and is not in use.  
`OS_CAPABILITY_NVME_STORAGE_ACCESS` | NVMe driver installed and the VM can use NVMe PD or local SSD.  
`OS_CAPABILITY_GVNIC_NETWORK_INTERFACE` | gVNIC virtual NIC driver supported.  
  
## AwsSourceVmDetails

Represent the source AWS VM details.

JSON representation  
---  
      
    
    {
      "firmware": enum ([Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware_1)),
      "committedStorageBytes": string,
      "disks": [
        {
          object ([AwsDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AwsDiskDetails))
        }
      ],
      "vmCapabilitiesInfo": {
        object ([VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities))
      }
    }  
  
Fields  
---  
`firmware` |  `enum (`[Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware_1)`)` Output only. The firmware type of the source VM.  
`committedStorageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total size of the disks being migrated in bytes.  
`disks[]` |  `object (`[AwsDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AwsDiskDetails)`)` Output only. The disks attached to the source VM.  
`vmCapabilitiesInfo` |  `object (`[VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities)`)` Output only. Information about VM capabilities needed for some Compute Engine features.  
  
## Firmware

Possible values for AWS VM firmware.

Enums  
---  
`FIRMWARE_UNSPECIFIED` | The firmware is unknown.  
`EFI` | The firmware is EFI.  
`BIOS` | The firmware is BIOS.  
  
## AwsDiskDetails

The details of an AWS instance disk.

JSON representation  
---  
      
    
    {
      "diskNumber": integer,
      "volumeId": string,
      "sizeGb": string
    }  
  
Fields  
---  
`diskNumber` |  `integer` Output only. The ordinal number of the disk.  
`volumeId` |  `string` Output only. AWS volume ID.  
`sizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size in GB.  
  
## AzureSourceVmDetails

Represent the source Azure VM details.

JSON representation  
---  
      
    
    {
      "firmware": enum ([Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware_2)),
      "committedStorageBytes": string,
      "disks": [
        {
          object ([AzureDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AzureDiskDetails))
        }
      ],
      "vmCapabilitiesInfo": {
        object ([VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities))
      }
    }  
  
Fields  
---  
`firmware` |  `enum (`[Firmware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#Firmware_2)`)` Output only. The firmware type of the source VM.  
`committedStorageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total size of the disks being migrated in bytes.  
`disks[]` |  `object (`[AzureDiskDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#AzureDiskDetails)`)` Output only. The disks attached to the source VM.  
`vmCapabilitiesInfo` |  `object (`[VmCapabilities](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms#VmCapabilities)`)` Output only. Information about VM capabilities needed for some Compute Engine features.  
  
## Firmware

Possible values for Azure VM firmware.

Enums  
---  
`FIRMWARE_UNSPECIFIED` | The firmware is unknown.  
`EFI` | The firmware is EFI.  
`BIOS` | The firmware is BIOS.  
  
## AzureDiskDetails

The details of an Azure VM disk.

JSON representation  
---  
      
    
    {
      "diskNumber": integer,
      "diskId": string,
      "sizeGb": string
    }  
  
Fields  
---  
`diskNumber` |  `integer` Output only. The ordinal number of the disk.  
`diskId` |  `string` Output only. Azure disk ID.  
`sizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size in GB.  
  
## SchedulePolicy

A policy for scheduling replications.

JSON representation  
---  
      
    
    {
      "idleDuration": string,
      "skipOsAdaptation": boolean
    }  
  
Fields  
---  
`idleDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The idle duration between replication stages.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`skipOsAdaptation` |  `boolean` A flag to indicate whether to skip OS adaptation during the replication sync. OS adaptation is a process where the VM's operating system undergoes changes and adaptations to fully function on Compute Engine.  
  
## ReplicationSync

ReplicationSync contain information about the last replica sync to the cloud.

JSON representation  
---  
      
    
    {
      "lastSyncTime": string
    }  
  
Fields  
---  
`lastSyncTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The most updated snapshot created time in the source that finished replication.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## State

The possible values of the state/health of source VM.

Enums  
---  
`STATE_UNSPECIFIED` | The state was not sampled by the health checks yet.  
`PENDING` | The VM in the source is being verified.  
`READY` | The source VM was verified, and it's ready to start replication.  
`FIRST_SYNC` | Migration is going through the first sync cycle.  
`ACTIVE` | The replication is active, and it's running or scheduled to run.  
`CUTTING_OVER` | The source VM is being turned off, and a final replication is currently running.  
`CUTOVER` | The source VM was stopped and replicated. The replication is currently paused.  
`FINAL_SYNC` | A cutover job is active and replication cycle is running the final sync.  
`PAUSED` | The replication was paused by the user and no cycles are scheduled to run.  
`FINALIZING` | The migrating VM is being finalized and migration resources are being removed.  
`FINALIZED` | The replication process is done. The migrating VM is finalized and no longer consumes billable resources.  
`ERROR` | The replication process encountered an unrecoverable error and was aborted.  
  
## CutoverForecast

CutoverForecast holds information about future CutoverJobs of a MigratingVm.

JSON representation  
---  
      
    
    {
      "estimatedCutoverJobDuration": string
    }  
  
Fields  
---  
`estimatedCutoverJobDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Estimation of the CutoverJob duration.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/create)`

|  Creates a new MigratingVm in a given Source.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/delete)`

|  Deletes a single MigratingVm.  
  
### `[finalizeMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/finalizeMigration)`

|  Marks a migration as completed, deleting migration resources that are no longer being used.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/get)`

|  Gets details of a single MigratingVm.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/list)`

|  Lists MigratingVms in a given Source.  
  
### `[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/patch)`

|  Updates the parameters of a single MigratingVm.  
  
### `[pauseMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/pauseMigration)`

|  Pauses a migration for a VM.  
  
### `[resumeMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/resumeMigration)`

|  Resumes a migration for a VM.  
  
### `[startMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/startMigration)`

|  Starts migration for a VM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
