---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails/
title: TargetVMDetails \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:52.718504+00:00
---

# TargetVMDetails  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  TargetVMDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DiskType
  * LicenseType
  * BootOption



This item is deprecated!

TargetVMDetails is a collection of details for creating a VM in a target Compute Engine project.

JSON representation  
---  
      
    
    {
      "name": string,
      "project": string,
      "targetProject": string,
      "zone": string,
      "machineTypeSeries": string,
      "machineType": string,
      "network": string,
      "subnetwork": string,
      "internalIp": string,
      "externalIp": string,
      "networkTags": [
        string
      ],
      "serviceAccount": string,
      "diskType": enum ([DiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#DiskType)),
      "labels": {
        string: string,
        ...
      },
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#LicenseType)),
      "appliedLicense": {
        object ([AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense))
      },
      "computeScheduling": {
        object ([ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling))
      },
      "networkInterfaces": [
        {
          object ([NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface))
        }
      ],
      "secureBoot": boolean,
      "bootOption": enum ([BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#BootOption)),
      "metadata": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the VM to create.  
`project  
**(deprecated)**` |  `string` This item is deprecated!Output only. The project in which to create the VM.  
`targetProject` |  `string` The full path of the resource of type TargetProject which represents the Compute Engine project in which to create this VM.  
`zone` |  `string` The zone in which to create the VM.  
`machineTypeSeries` |  `string` The machine type series to create the VM with.  
`machineType` |  `string` The machine type to create the VM with.  
`network` |  `string` The network to connect the VM to.  
`subnetwork` |  `string` The subnetwork to connect the VM to.  
`internalIp` |  `string` The internal IP to define in the VM. The formats accepted are: `ephemeral` \ ipv4 address \ a named address resource full path.  
`externalIp` |  `string` The external IP to define in the VM.  
`networkTags[]` |  `string` A list of network tags to associate with the VM.  
`serviceAccount` |  `string` The service account to associate the VM with.  
`diskType` |  `enum (`[DiskType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#DiskType)`)` The disk type to use in the VM.  
`labels` |  `map (key: string, value: string)` A map of labels to associate with the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#LicenseType)`)` The license type to use in OS adaptation.  
`appliedLicense` |  `object (`[AppliedLicense](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/AppliedLicense)`)` Output only. The OS license returned from the adaptation module report.  
`computeScheduling` |  `object (`[ComputeScheduling](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/ComputeScheduling)`)` Compute instance scheduling information (if empty default is used).  
`networkInterfaces[]` |  `object (`[NetworkInterface](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/NetworkInterface)`)` List of NICs connected to this VM.  
`secureBoot` |  `boolean` Defines whether the instance has Secure Boot enabled. This can be set to true only if the vm boot option is EFI.  
`bootOption` |  `enum (`[BootOption](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/TargetVMDetails#BootOption)`)` Output only. The VM Boot Option, as set in the source VM.  
`metadata` |  `map (key: string, value: string)` The metadata key/value pairs to assign to the VM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## DiskType

Types of disks supported for the VM.

Enums  
---  
`DISK_TYPE_UNSPECIFIED` | An unspecified disk type. Will be used as STANDARD.  
`STANDARD` | A Standard disk type.  
`BALANCED` | An alternative to SSD persistent disks that balance performance and cost.  
`SSD` | SSD hard disk type.  
`HYPERDISK_BALANCED` | Hyperdisk balanced disk type.  
  
## LicenseType

Types of licenses used in OS adaptation.

Enums  
---  
`DEFAULT` | The license type is the default for the OS.  
`PAYG` | The license type is Pay As You Go license type.  
`BYOL` | The license type is Bring Your Own License type.  
  
## BootOption

Possible values for vm boot option.

Enums  
---  
`BOOT_OPTION_UNSPECIFIED` | The boot option is unknown.  
`EFI` | The boot option is EFI.  
`BIOS` | The boot option is BIOS.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
