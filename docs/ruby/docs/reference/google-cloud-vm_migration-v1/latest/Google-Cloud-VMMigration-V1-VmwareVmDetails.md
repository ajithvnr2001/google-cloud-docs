---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VmwareVmDetails (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:57.897461+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VmwareVmDetails (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VmwareVmDetails (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::VmwareVmDetails.

VmwareVmDetails describes a VM in vCenter.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #architecture
    
    
    def architecture() -> ::Google::Cloud::VMMigration::V1::VmwareVmDetails::VmArchitecture

**Returns**

  * ([::Google::Cloud::VMMigration::V1::VmwareVmDetails::VmArchitecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails-VmArchitecture)) — Output only. The CPU architecture. 



### #boot_option
    
    
    def boot_option() -> ::Google::Cloud::VMMigration::V1::VmwareVmDetails::BootOption

**Returns**

  * ([::Google::Cloud::VMMigration::V1::VmwareVmDetails::BootOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails-BootOption)) — Output only. The VM Boot Option. 



### #committed_storage_mb
    
    
    def committed_storage_mb() -> ::Integer

**Returns**

  * (::Integer) — The total size of the storage allocated to the VM in MB. 



### #committed_storage_mb=
    
    
    def committed_storage_mb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The total size of the storage allocated to the VM in MB. 



**Returns**

  * (::Integer) — The total size of the storage allocated to the VM in MB. 



### #cpu_count
    
    
    def cpu_count() -> ::Integer

**Returns**

  * (::Integer) — The number of cpus in the VM. 



### #cpu_count=
    
    
    def cpu_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of cpus in the VM. 



**Returns**

  * (::Integer) — The number of cpus in the VM. 



### #datacenter_description
    
    
    def datacenter_description() -> ::String

**Returns**

  * (::String) — The descriptive name of the vCenter's datacenter this VM is contained in. 



### #datacenter_description=
    
    
    def datacenter_description=(value) -> ::String

**Parameter**

  * **value** (::String) — The descriptive name of the vCenter's datacenter this VM is contained in. 



**Returns**

  * (::String) — The descriptive name of the vCenter's datacenter this VM is contained in. 



### #datacenter_id
    
    
    def datacenter_id() -> ::String

**Returns**

  * (::String) — The id of the vCenter's datacenter this VM is contained in. 



### #datacenter_id=
    
    
    def datacenter_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The id of the vCenter's datacenter this VM is contained in. 



**Returns**

  * (::String) — The id of the vCenter's datacenter this VM is contained in. 



### #disk_count
    
    
    def disk_count() -> ::Integer

**Returns**

  * (::Integer) — The number of disks the VM has. 



### #disk_count=
    
    
    def disk_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of disks the VM has. 



**Returns**

  * (::Integer) — The number of disks the VM has. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The display name of the VM. Note that this is not necessarily unique. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The display name of the VM. Note that this is not necessarily unique. 



**Returns**

  * (::String) — The display name of the VM. Note that this is not necessarily unique. 



### #guest_description
    
    
    def guest_description() -> ::String

**Returns**

  * (::String) — The VM's OS. See for example https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html for types of strings this might hold. 



### #guest_description=
    
    
    def guest_description=(value) -> ::String

**Parameter**

  * **value** (::String) — The VM's OS. See for example https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html for types of strings this might hold. 



**Returns**

  * (::String) — The VM's OS. See for example https://vdc-repo.vmware.com/vmwb-repository/dcr-public/da47f910-60ac-438b-8b9b-6122f4d14524/16b7274a-bf8b-4b4c-a05e-746f2aa93c8c/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html for types of strings this might hold. 



### #memory_mb
    
    
    def memory_mb() -> ::Integer

**Returns**

  * (::Integer) — The size of the memory of the VM in MB. 



### #memory_mb=
    
    
    def memory_mb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The size of the memory of the VM in MB. 



**Returns**

  * (::Integer) — The size of the memory of the VM in MB. 



### #power_state
    
    
    def power_state() -> ::Google::Cloud::VMMigration::V1::VmwareVmDetails::PowerState

**Returns**

  * ([::Google::Cloud::VMMigration::V1::VmwareVmDetails::PowerState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails-PowerState)) — The power state of the VM at the moment list was taken. 



### #power_state=
    
    
    def power_state=(value) -> ::Google::Cloud::VMMigration::V1::VmwareVmDetails::PowerState

**Parameter**

  * **value** ([::Google::Cloud::VMMigration::V1::VmwareVmDetails::PowerState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails-PowerState)) — The power state of the VM at the moment list was taken. 



**Returns**

  * ([::Google::Cloud::VMMigration::V1::VmwareVmDetails::PowerState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VmwareVmDetails-PowerState)) — The power state of the VM at the moment list was taken. 



### #uuid
    
    
    def uuid() -> ::String

**Returns**

  * (::String) — The unique identifier of the VM in vCenter. 



### #uuid=
    
    
    def uuid=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique identifier of the VM in vCenter. 



**Returns**

  * (::String) — The unique identifier of the VM in vCenter. 



### #vm_id
    
    
    def vm_id() -> ::String

**Returns**

  * (::String) — The VM's id in the source (note that this is not the MigratingVm's id). This is the moref id of the VM. 



### #vm_id=
    
    
    def vm_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The VM's id in the source (note that this is not the MigratingVm's id). This is the moref id of the VM. 



**Returns**

  * (::String) — The VM's id in the source (note that this is not the MigratingVm's id). This is the moref id of the VM. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
