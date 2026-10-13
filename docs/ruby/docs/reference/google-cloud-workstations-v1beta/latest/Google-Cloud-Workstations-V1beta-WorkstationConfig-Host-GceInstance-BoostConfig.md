---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-BoostConfig/
title: Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig (v0.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:31.184963+00:00
---

# Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig (v0.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-BoostConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Workstations V1BETA API - Class Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig (v0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.1  0.7.1  0.6.0  0.5.1  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Cloud Workstations V1BETA API class Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig.

A boost configuration is a set of resources that a workstation can use to increase its performance. If you specify a boost configuration, upon startup, workstation users can choose to use a VM provisioned under the boost config by passing the boost config ID in the start request. If the workstation user does not provide a boost config ID in the start request, the system will choose a VM from the pool provisioned under the default config.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerators
    
    
    def accelerators() -> ::Array<::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::Accelerator>

**Returns**

  * (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::Accelerator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-Accelerator)>) — Optional. A list of the type and count of accelerator cards attached to the boost instance. Defaults to `none`. 



### #accelerators=
    
    
    def accelerators=(value) -> ::Array<::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::Accelerator>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::Accelerator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-Accelerator)>) — Optional. A list of the type and count of accelerator cards attached to the boost instance. Defaults to `none`. 



**Returns**

  * (::Array<[::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::Accelerator](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-Accelerator)>) — Optional. A list of the type and count of accelerator cards attached to the boost instance. Defaults to `none`. 



### #boot_disk_size_gb
    
    
    def boot_disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. The size of the boot disk for the VM in gigabytes (GB). The minimum boot disk size is `30` GB. Defaults to `50` GB. 



### #boot_disk_size_gb=
    
    
    def boot_disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The size of the boot disk for the VM in gigabytes (GB). The minimum boot disk size is `30` GB. Defaults to `50` GB. 



**Returns**

  * (::Integer) — Optional. The size of the boot disk for the VM in gigabytes (GB). The minimum boot disk size is `30` GB. Defaults to `50` GB. 



### #enable_nested_virtualization
    
    
    def enable_nested_virtualization() -> ::Boolean

**Returns**

  * (::Boolean) — 

Optional. Whether to enable nested virtualization on boosted Cloud Workstations VMs running using this boost configuration.

Defaults to false.

Nested virtualization lets you run virtual machine (VM) instances inside your workstation. Before enabling nested virtualization, consider the following important considerations. Cloud Workstations instances are subject to the [same restrictions as Compute Engine instances](https://cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions):

    * **Organization policy** : projects, folders, or organizations may be restricted from creating nested VMs if the **Disable VM nested virtualization** constraint is enforced in the organization policy. For more information, see the Compute Engine section, [Checking whether nested virtualization is allowed](https://cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#checking_whether_nested_virtualization_is_allowed).
    * **Performance** : nested VMs might experience a 10% or greater decrease in performance for workloads that are CPU-bound and possibly greater than a 10% decrease for workloads that are input/output bound.
    * **Machine Type** : nested virtualization can only be enabled on boost configurations that specify a [machine_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-BoostConfig#Google__Cloud__Workstations__V1beta__WorkstationConfig__Host__GceInstance__BoostConfig_machine_type_instance_ "Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig#machine_type \(method\)") in the N1 or N2 machine series.



### #enable_nested_virtualization=
    
    
    def enable_nested_virtualization=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

Optional. Whether to enable nested virtualization on boosted Cloud Workstations VMs running using this boost configuration.

Defaults to false.

Nested virtualization lets you run virtual machine (VM) instances inside your workstation. Before enabling nested virtualization, consider the following important considerations. Cloud Workstations instances are subject to the [same restrictions as Compute Engine instances](https://cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions):

    * **Organization policy** : projects, folders, or organizations may be restricted from creating nested VMs if the **Disable VM nested virtualization** constraint is enforced in the organization policy. For more information, see the Compute Engine section, [Checking whether nested virtualization is allowed](https://cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#checking_whether_nested_virtualization_is_allowed).
    * **Performance** : nested VMs might experience a 10% or greater decrease in performance for workloads that are CPU-bound and possibly greater than a 10% decrease for workloads that are input/output bound.
    * **Machine Type** : nested virtualization can only be enabled on boost configurations that specify a [machine_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-BoostConfig#Google__Cloud__Workstations__V1beta__WorkstationConfig__Host__GceInstance__BoostConfig_machine_type_instance_ "Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig#machine_type \(method\)") in the N1 or N2 machine series.



**Returns**

  * (::Boolean) — 

Optional. Whether to enable nested virtualization on boosted Cloud Workstations VMs running using this boost configuration.

Defaults to false.

Nested virtualization lets you run virtual machine (VM) instances inside your workstation. Before enabling nested virtualization, consider the following important considerations. Cloud Workstations instances are subject to the [same restrictions as Compute Engine instances](https://cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions):

    * **Organization policy** : projects, folders, or organizations may be restricted from creating nested VMs if the **Disable VM nested virtualization** constraint is enforced in the organization policy. For more information, see the Compute Engine section, [Checking whether nested virtualization is allowed](https://cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#checking_whether_nested_virtualization_is_allowed).
    * **Performance** : nested VMs might experience a 10% or greater decrease in performance for workloads that are CPU-bound and possibly greater than a 10% decrease for workloads that are input/output bound.
    * **Machine Type** : nested virtualization can only be enabled on boost configurations that specify a [machine_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-BoostConfig#Google__Cloud__Workstations__V1beta__WorkstationConfig__Host__GceInstance__BoostConfig_machine_type_instance_ "Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::BoostConfig#machine_type \(method\)") in the N1 or N2 machine series.



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Required. The ID to be used for the boost configuration. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to be used for the boost configuration. 



**Returns**

  * (::String) — Required. The ID to be used for the boost configuration. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — Optional. The type of machine that boosted VM instances will use—for example, `e2-standard-4`. For more information about machine types that Cloud Workstations supports, see the list of [available machine types](https://cloud.google.com/workstations/docs/available-machine-types). Defaults to `e2-standard-4`. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The type of machine that boosted VM instances will use—for example, `e2-standard-4`. For more information about machine types that Cloud Workstations supports, see the list of [available machine types](https://cloud.google.com/workstations/docs/available-machine-types). Defaults to `e2-standard-4`. 



**Returns**

  * (::String) — Optional. The type of machine that boosted VM instances will use—for example, `e2-standard-4`. For more information about machine types that Cloud Workstations supports, see the list of [available machine types](https://cloud.google.com/workstations/docs/available-machine-types). Defaults to `e2-standard-4`. 



### #pool_size
    
    
    def pool_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The number of boost VMs that the system should keep idle so that workstations can be boosted quickly. Defaults to `0`. 



### #pool_size=
    
    
    def pool_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The number of boost VMs that the system should keep idle so that workstations can be boosted quickly. Defaults to `0`. 



**Returns**

  * (::Integer) — Optional. The number of boost VMs that the system should keep idle so that workstations can be boosted quickly. Defaults to `0`. 



### #reservation_affinity
    
    
    def reservation_affinity() -> ::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::ReservationAffinity

**Returns**

  * ([::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-ReservationAffinity)) — 

Optional. [ReservationAffinity](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) specifies a reservation that can be consumed to create boost VM instances. If SPECIFIC_RESERVATION is specified, Cloud Workstations will only create VMs in the zone where the reservation is located. This would affect availability since the service will no longer be resilient to zonal outages. If ANY_RESERVATION is specified, creating reservations in both zones that the config creates VMs in will ensure higher availability. **Important Considerations for Reservation Affinity:**

    * This feature is intended for advanced users and requires familiarity with Google Compute Engine reservations.
    * Using reservations incurs charges, regardless of utilization.
    * The resources in the pool will consume the specified reservation. Take this into account when setting the pool size.



### #reservation_affinity=
    
    
    def reservation_affinity=(value) -> ::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::ReservationAffinity

**Parameter**

  * **value** ([::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-ReservationAffinity)) — 

Optional. [ReservationAffinity](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) specifies a reservation that can be consumed to create boost VM instances. If SPECIFIC_RESERVATION is specified, Cloud Workstations will only create VMs in the zone where the reservation is located. This would affect availability since the service will no longer be resilient to zonal outages. If ANY_RESERVATION is specified, creating reservations in both zones that the config creates VMs in will ensure higher availability. **Important Considerations for Reservation Affinity:**

    * This feature is intended for advanced users and requires familiarity with Google Compute Engine reservations.
    * Using reservations incurs charges, regardless of utilization.
    * The resources in the pool will consume the specified reservation. Take this into account when setting the pool size.



**Returns**

  * ([::Google::Cloud::Workstations::V1beta::WorkstationConfig::Host::GceInstance::ReservationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-WorkstationConfig-Host-GceInstance-ReservationAffinity)) — 

Optional. [ReservationAffinity](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) specifies a reservation that can be consumed to create boost VM instances. If SPECIFIC_RESERVATION is specified, Cloud Workstations will only create VMs in the zone where the reservation is located. This would affect availability since the service will no longer be resilient to zonal outages. If ANY_RESERVATION is specified, creating reservations in both zones that the config creates VMs in will ensure higher availability. **Important Considerations for Reservation Affinity:**

    * This feature is intended for advanced users and requires familiarity with Google Compute Engine reservations.
    * Using reservations incurs charges, regardless of utilization.
    * The resources in the pool will consume the specified reservation. Take this into account when setting the pool size.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
