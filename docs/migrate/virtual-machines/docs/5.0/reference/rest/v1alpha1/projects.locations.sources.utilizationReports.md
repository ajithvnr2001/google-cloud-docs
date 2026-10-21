---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports
title: REST Resource: projects.locations.sources.utilizationReports \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:49.206431+00:00
---

# REST Resource: projects.locations.sources.utilizationReports  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.utilizationReports Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UtilizationReport
    * JSON representation
  * State
  * TimeFrame
  * VmUtilizationInfo
    * JSON representation
  * VmwareVmDetails
    * JSON representation
  * PowerState
  * BootOption
  * VmUtilizationMetrics
    * JSON representation
  * Methods



## Resource: UtilizationReport

Utilization report details the utilization (CPU, memory, etc.) of selected source VMs.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#State)),
      "stateTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status))
      },
      "createTime": string,
      "timeFrame": enum ([TimeFrame](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#TimeFrame)),
      "frameEndTime": string,
      "vmsCount": integer,
      "vmCount": integer,
      "vms": [
        {
          object ([VmUtilizationInfo](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmUtilizationInfo))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The report unique name.  
`displayName` |  `string` The report display name, as assigned by the user.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#State)`)` Output only. Current state of the report.  
`stateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the state was last set.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/Status)`)` Output only. Provides details on the state of the report in case of an error.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the report was created (this refers to the time of the request, not the time the report creation completed).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`timeFrame` |  `enum (`[TimeFrame](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#TimeFrame)`)` Time frame of the report.  
`frameEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The point in time when the time frame ends. Notice that the time frame is counted backwards. For instance if the "frameEndTime" value is 2021/01/20 and the time frame is WEEK then the report covers the week between 2021/01/20 and 2021/01/14.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`vmsCount  
**(deprecated)**` |  `integer` This item is deprecated!Output only. Total number of VMs included in the report.  
`vmCount` |  `integer` Output only. Total number of VMs included in the report.  
`vms[]` |  `object (`[VmUtilizationInfo](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmUtilizationInfo)`)` List of utilization information per VM. When sent as part of the request, the "vmId" field is used in order to specify which VMs to include in the report. In that case all other fields are ignored.  
  
## State

Utilization report state.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This value is not in use.  
`CREATING` | The report is in the making.  
`SUCCEEDED` | Report creation completed successfully.  
`FAILED` | Report creation failed.  
  
## TimeFrame

Report time frame options.

Enums  
---  
`TIME_FRAME_UNSPECIFIED` | The time frame was not specified and will default to WEEK.  
`WEEK` | One week.  
`MONTH` | One month.  
`YEAR` | One year.  
  
## VmUtilizationInfo

Utilization information of a single VM.

JSON representation  
---  
      
    
    {
      "vmId": string,
      "utilization": {
        object ([VmUtilizationMetrics](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmUtilizationMetrics))
      },
    
      // Union field VmDetails can be only one of the following:
      "vmwareVmDetails": {
        object ([VmwareVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmwareVmDetails))
      }
      // End of list of possible types for union field VmDetails.
    }  
  
Fields  
---  
`vmId` |  `string` The VM's ID in the source.  
`utilization` |  `object (`[VmUtilizationMetrics](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmUtilizationMetrics)`)` Utilization metrics for this VM.  
Union field `VmDetails`.`VmDetails` can be only one of the following:  
`vmwareVmDetails` |  `object (`[VmwareVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#VmwareVmDetails)`)` The description of the VM in a Source of type Vmware.  
  
## VmwareVmDetails

VmwareVmDetails describes a VM in vCenter.

JSON representation  
---  
      
    
    {
      "vmId": string,
      "datacenterId": string,
      "datacenterDescription": string,
      "uuid": string,
      "displayName": string,
      "powerState": enum ([PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#PowerState)),
      "cpuCount": integer,
      "memoryMb": integer,
      "diskCount": integer,
      "committedStorage": string,
      "committedStorageMb": string,
      "guestDescription": string,
      "bootOption": enum ([BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#BootOption))
    }  
  
Fields  
---  
`vmId` |  `string` The VM's id in the source (note that this is not the MigratingVm's id). This is the moref id of the VM.  
`datacenterId` |  `string` The id of the vCenter's datacenter this VM is contained in.  
`datacenterDescription` |  `string` The descriptive name of the vCenter's datacenter this VM is contained in.  
`uuid` |  `string` The unique identifier of the VM in vCenter.  
`displayName` |  `string` The display name of the VM. Note that this is not necessarily unique.  
`powerState` |  `enum (`[PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#PowerState)`)` The power state of the VM at the moment list was taken.  
`cpuCount` |  `integer` The number of cpus in the VM.  
`memoryMb` |  `integer` The size of the memory of the VM in MB.  
`diskCount` |  `integer` The number of disks the VM has.  
`committedStorage  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The total size of the storage allocated to the VM in MB.  
`committedStorageMb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total size of the storage allocated to the VM in MB.  
`guestDescription` |  `string` The VM's OS. See for example <https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html> for types of strings this might hold.  
`bootOption` |  `enum (`[BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports#BootOption)`)` Output only. The VM Boot Option.  
  
## PowerState

Possible values for the power state of the VM.

Enums  
---  
`POWER_STATE_UNSPECIFIED` | Power state is not specified.  
`ON` | The VM is turned ON.  
`OFF` | The VM is turned OFF.  
`SUSPENDED` | The VM is suspended. This is similar to hibernation or sleep mode.  
  
## BootOption

Possible values for vm boot option.

Enums  
---  
`BOOT_OPTION_UNSPECIFIED` | The boot option is unknown.  
`EFI` | The boot option is EFI.  
`BIOS` | The boot option is BIOS.  
  
## VmUtilizationMetrics

Utilization metrics values for a single VM.

JSON representation  
---  
      
    
    {
      "cpuMax": integer,
      "cpuMaxPercent": integer,
      "cpuAverage": integer,
      "cpuAveragePercent": integer,
      "memoryMax": integer,
      "memoryMaxPercent": integer,
      "memoryAverage": integer,
      "memoryAveragePercent": integer,
      "diskIoRateMax": string,
      "diskIoRateMaxKbps": string,
      "diskIoRateAverage": string,
      "diskIoRateAverageKbps": string,
      "networkThroughputMax": string,
      "networkThroughputMaxKbps": string,
      "networkThroughputAverage": string,
      "networkThroughputAverageKbps": string
    }  
  
Fields  
---  
`cpuMax  
**(deprecated)**` |  `integer` This item is deprecated!Max CPU usage, percent.  
`cpuMaxPercent` |  `integer` Max CPU usage, percent.  
`cpuAverage  
**(deprecated)**` |  `integer` This item is deprecated!Average CPU usage, percent.  
`cpuAveragePercent` |  `integer` Average CPU usage, percent.  
`memoryMax  
**(deprecated)**` |  `integer` This item is deprecated!Max memory usage, percent.  
`memoryMaxPercent` |  `integer` Max memory usage, percent.  
`memoryAverage  
**(deprecated)**` |  `integer` This item is deprecated!Average memory usage, percent.  
`memoryAveragePercent` |  `integer` Average memory usage, percent.  
`diskIoRateMax  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Max disk IO rate, in kilobytes per second.  
`diskIoRateMaxKbps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Max disk IO rate, in kilobytes per second.  
`diskIoRateAverage  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Average disk IO rate, in kilobytes per second.  
`diskIoRateAverageKbps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Average disk IO rate, in kilobytes per second.  
`networkThroughputMax  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Max network throughput (combined transmit-rates and receive-rates), in kilobytes per second.  
`networkThroughputMaxKbps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Max network throughput (combined transmit-rates and receive-rates), in kilobytes per second.  
`networkThroughputAverage  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Average network throughput (combined transmit-rates and receive-rates), in kilobytes per second.  
`networkThroughputAverageKbps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Average network throughput (combined transmit-rates and receive-rates), in kilobytes per second.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/create)`

|  Creates a new UtilizationReport.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/delete)`

|  Deletes a single Utilization Report.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/get)`

|  Gets a single Utilization Report.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/list)`

|  Lists Utilization Reports of the given Source.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
