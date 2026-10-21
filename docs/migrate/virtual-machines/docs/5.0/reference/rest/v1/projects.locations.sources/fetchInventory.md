---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory/
title: Method: projects.locations.sources.fetchInventory \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:32.962857+00:00
---

# Method: projects.locations.sources.fetchInventory  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  Method: projects.locations.sources.fetchInventory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * VmwareVmsDetails
    * JSON representation
  * AwsVmsDetails
    * JSON representation
  * AwsVmDetails
    * JSON representation
  * PowerState
  * BootOption
  * AwsSecurityGroup
    * JSON representation
  * VmVirtualizationType
  * VmArchitecture
  * AzureVmsDetails
    * JSON representation
  * AzureVmDetails
    * JSON representation
  * PowerState
  * OSDisk
    * JSON representation
  * Disk
    * JSON representation
  * OSDescription
    * JSON representation
  * BootOption



List remote source's inventory of VMs. The remote source is the onprem vCenter (remote in the sense it's not in Compute Engine). The inventory describes the list of existing VMs in that source. Note that this operation lists the VMs on the remote source, as opposed to listing the MigratingVms resources in the vmmigration service.

### HTTP request

`GET https://vmmigration.googleapis.com/v1/{source=projects/*/locations/*/sources/*}:fetchInventory`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`source` |  `string` Required. The name of the Source. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `source`:

  * `vmmigration.sources.get`

  
  
### Query parameters

Parameters  
---  
`forceRefresh` |  `boolean` If this flag is set to true, the source will be queried instead of using cached results. Using this flag will make the call slower.  
`pageSize` |  `integer` The maximum number of VMs to return. The service may return fewer than this value. For AWS source: If unspecified, at most 500 VMs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. For VMWare source: If unspecified, all VMs will be returned. There is no limit for maximum value.  
`pageToken` |  `string` A page token, received from a previous `sources.fetchInventory` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `sources.fetchInventory` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[fetchInventory](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#google.cloud.vmmigration.v1.VmMigration.FetchInventory)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "updateTime": string,
      "nextPageToken": string,
    
      // Union field SourceVms can be only one of the following:
      "vmwareVms": {
        object ([VmwareVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmwareVmsDetails))
      },
      "awsVms": {
        object ([AwsVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsVmsDetails))
      },
      "azureVms": {
        object ([AzureVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AzureVmsDetails))
      }
      // End of list of possible types for union field SourceVms.
    }  
  
Fields  
---  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the source was last queried (if the result is from the cache).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`nextPageToken` |  `string` Output only. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
Union field `SourceVms`.`SourceVms` can be only one of the following:  
`vmwareVms` |  `object (`[VmwareVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmwareVmsDetails)`)` The description of the VMs in a Source of type Vmware.  
`awsVms` |  `object (`[AwsVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsVmsDetails)`)` The description of the VMs in a Source of type AWS.  
`azureVms` |  `object (`[AzureVmsDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AzureVmsDetails)`)` The description of the VMs in a Source of type Azure.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## VmwareVmsDetails

VmwareVmsDetails describes VMs in vCenter.

JSON representation  
---  
      
    
    {
      "details": [
        {
          object ([VmwareVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.utilizationReports#VmwareVmDetails))
        }
      ]
    }  
  
Fields  
---  
`details[]` |  `object (`[VmwareVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.utilizationReports#VmwareVmDetails)`)` The details of the vmware VMs.  
  
## AwsVmsDetails

AWSVmsDetails describes VMs in AWS.

JSON representation  
---  
      
    
    {
      "details": [
        {
          object ([AwsVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsVmDetails))
        }
      ]
    }  
  
Fields  
---  
`details[]` |  `object (`[AwsVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsVmDetails)`)` The details of the AWS VMs.  
  
## AwsVmDetails

AwsVmDetails describes a VM in AWS.

JSON representation  
---  
      
    
    {
      "vmId": string,
      "displayName": string,
      "sourceId": string,
      "sourceDescription": string,
      "powerState": enum ([PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#PowerState)),
      "cpuCount": integer,
      "memoryMb": integer,
      "diskCount": integer,
      "committedStorageMb": string,
      "osDescription": string,
      "bootOption": enum ([BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#BootOption)),
      "instanceType": string,
      "vpcId": string,
      "securityGroups": [
        {
          object ([AwsSecurityGroup](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsSecurityGroup))
        }
      ],
      "tags": {
        string: string,
        ...
      },
      "zone": string,
      "virtualizationType": enum ([VmVirtualizationType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmVirtualizationType)),
      "architecture": enum ([VmArchitecture](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmArchitecture))
    }  
  
Fields  
---  
`vmId` |  `string` The VM ID in AWS.  
`displayName` |  `string` The display name of the VM. Note that this value is not necessarily unique.  
`sourceId` |  `string` The id of the AWS's source this VM is connected to.  
`sourceDescription` |  `string` The descriptive name of the AWS's source this VM is connected to.  
`powerState` |  `enum (`[PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#PowerState)`)` Output only. The power state of the VM at the moment list was taken.  
`cpuCount` |  `integer` The number of cpus the VM has.  
`memoryMb` |  `integer` The memory size of the VM in MB.  
`diskCount` |  `integer` The number of disks the VM has.  
`committedStorageMb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total size of the storage allocated to the VM in MB.  
`osDescription` |  `string` The VM's OS.  
`bootOption` |  `enum (`[BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#BootOption)`)` The VM Boot Option.  
`instanceType` |  `string` The instance type of the VM.  
`vpcId` |  `string` The VPC ID the VM belongs to.  
`securityGroups[]` |  `object (`[AwsSecurityGroup](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AwsSecurityGroup)`)` The security groups the VM belongs to.  
`tags` |  `map (key: string, value: string)` The tags of the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`zone` |  `string` The AWS zone of the VM.  
`virtualizationType` |  `enum (`[VmVirtualizationType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmVirtualizationType)`)` The virtualization type.  
`architecture` |  `enum (`[VmArchitecture](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#VmArchitecture)`)` The CPU architecture.  
  
## PowerState

Possible values for the power state of the VM.

Enums  
---  
`POWER_STATE_UNSPECIFIED` | Power state is not specified.  
`ON` | The VM is turned on.  
`OFF` | The VM is turned off.  
`SUSPENDED` | The VM is suspended. This is similar to hibernation or sleep mode.  
`PENDING` | The VM is starting.  
  
## BootOption

The possible values for the vm boot option.

Enums  
---  
`BOOT_OPTION_UNSPECIFIED` | The boot option is unknown.  
`EFI` | The boot option is UEFI.  
`BIOS` | The boot option is LEGACY-BIOS.  
  
## AwsSecurityGroup

AwsSecurityGroup describes a security group of an AWS VM.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string
    }  
  
Fields  
---  
`id` |  `string` The AWS security group id.  
`name` |  `string` The AWS security group name.  
  
## VmVirtualizationType

Possible values for the virtualization types of the VM.

Enums  
---  
`VM_VIRTUALIZATION_TYPE_UNSPECIFIED` | The virtualization type is unknown.  
`HVM` | The virtualziation type is HVM.  
`PARAVIRTUAL` | The virtualziation type is PARAVIRTUAL.  
  
## VmArchitecture

Possible values for the architectures of the VM.

Enums  
---  
`VM_ARCHITECTURE_UNSPECIFIED` | The architecture is unknown.  
`I386` | The architecture is I386.  
`X86_64` | The architecture is X86_64.  
`ARM64` | The architecture is ARM64.  
`X86_64_MAC` | The architecture is X86_64_MAC.  
  
## AzureVmsDetails

AzureVmsDetails describes VMs in Azure.

JSON representation  
---  
      
    
    {
      "details": [
        {
          object ([AzureVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AzureVmDetails))
        }
      ]
    }  
  
Fields  
---  
`details[]` |  `object (`[AzureVmDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#AzureVmDetails)`)` The details of the Azure VMs.  
  
## AzureVmDetails

AzureVmDetails describes a VM in Azure.

JSON representation  
---  
      
    
    {
      "vmId": string,
      "powerState": enum ([PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#PowerState_1)),
      "vmSize": string,
      "cpuCount": integer,
      "memoryMb": integer,
      "diskCount": integer,
      "committedStorageMb": string,
      "osDisk": {
        object ([OSDisk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#OSDisk))
      },
      "disks": [
        {
          object ([Disk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#Disk))
        }
      ],
      "osDescription": {
        object ([OSDescription](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#OSDescription))
      },
      "bootOption": enum ([BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#BootOption_1)),
      "tags": {
        string: string,
        ...
      },
      "computerName": string
    }  
  
Fields  
---  
`vmId` |  `string` The VM full path in Azure.  
`powerState` |  `enum (`[PowerState](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#PowerState_1)`)` The power state of the VM at the moment list was taken.  
`vmSize` |  `string` VM size as configured in Azure. Determines the VM's hardware spec.  
`cpuCount` |  `integer` The number of cpus the VM has.  
`memoryMb` |  `integer` The memory size of the VM in MB.  
`diskCount` |  `integer` The number of disks the VM has, including OS disk.  
`committedStorageMb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total size of the storage allocated to the VM in MB.  
`osDisk` |  `object (`[OSDisk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#OSDisk)`)` Description of the OS disk.  
`disks[]` |  `object (`[Disk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#Disk)`)` Description of the data disks.  
`osDescription` |  `object (`[OSDescription](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#OSDescription)`)` Description of the OS.  
`bootOption` |  `enum (`[BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources/fetchInventory#BootOption_1)`)` The VM Boot Option.  
`tags` |  `map (key: string, value: string)` The tags of the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`computerName` |  `string` The VM's ComputerName.  
  
## PowerState

Possible values for the power state of the VM.

Enums  
---  
`POWER_STATE_UNSPECIFIED` | Power state is not specified.  
`STARTING` | The VM is starting.  
`RUNNING` | The VM is running.  
`STOPPING` | The VM is stopping.  
`STOPPED` | The VM is stopped.  
`DEALLOCATING` | The VM is deallocating.  
`DEALLOCATED` | The VM is deallocated.  
`UNKNOWN` | The VM's power state is unknown.  
  
## OSDisk

A message describing the OS disk.

JSON representation  
---  
      
    
    {
      "type": string,
      "name": string,
      "sizeGb": integer
    }  
  
Fields  
---  
`type` |  `string` The disk's type.  
`name` |  `string` The disk's full name.  
`sizeGb` |  `integer` The disk's size in GB.  
  
## Disk

A message describing a data disk.

JSON representation  
---  
      
    
    {
      "name": string,
      "sizeGb": integer,
      "lun": integer
    }  
  
Fields  
---  
`name` |  `string` The disk name.  
`sizeGb` |  `integer` The disk size in GB.  
`lun` |  `integer` The disk's Logical Unit Number (LUN).  
  
## OSDescription

A message describing the VM's OS. Including OS, Publisher, Offer and Plan if applicable.

JSON representation  
---  
      
    
    {
      "type": string,
      "publisher": string,
      "offer": string,
      "plan": string
    }  
  
Fields  
---  
`type` |  `string` OS type.  
`publisher` |  `string` OS publisher.  
`offer` |  `string` OS offer.  
`plan` |  `string` OS plan.  
  
## BootOption

The possible values for the vm boot option.

Enums  
---  
`BOOT_OPTION_UNSPECIFIED` | The boot option is unknown.  
`EFI` | The boot option is UEFI.  
`BIOS` | The boot option is BIOS.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
