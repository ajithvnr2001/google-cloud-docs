---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AdvancedMachineFeatures/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AdvancedMachineFeatures (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:25.097583+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AdvancedMachineFeatures (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AdvancedMachineFeatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AdvancedMachineFeatures (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AdvancedMachineFeatures.

Specifies options for controlling advanced machine features. Options that would traditionally be configured in a BIOS belong here. Features that require operating system support may have corresponding entries in the GuestOsFeatures of anImage (e.g., whether or not the OS in theImage supports nested virtualization being enabled or disabled).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enable_nested_virtualization
    
    
    def enable_nested_virtualization() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to enable nested virtualization or not (default is false). 



### #enable_nested_virtualization=
    
    
    def enable_nested_virtualization=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to enable nested virtualization or not (default is false). 



**Returns**

  * (::Boolean) — Whether to enable nested virtualization or not (default is false). 



### #enable_uefi_networking
    
    
    def enable_uefi_networking() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to enable UEFI networking for instance creation. 



### #enable_uefi_networking=
    
    
    def enable_uefi_networking=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to enable UEFI networking for instance creation. 



**Returns**

  * (::Boolean) — Whether to enable UEFI networking for instance creation. 



### #performance_monitoring_unit
    
    
    def performance_monitoring_unit() -> ::String

**Returns**

  * (::String) — Type of Performance Monitoring Unit requested on instance. Check the PerformanceMonitoringUnit enum for the list of possible values. 



### #performance_monitoring_unit=
    
    
    def performance_monitoring_unit=(value) -> ::String

**Parameter**

  * **value** (::String) — Type of Performance Monitoring Unit requested on instance. Check the PerformanceMonitoringUnit enum for the list of possible values. 



**Returns**

  * (::String) — Type of Performance Monitoring Unit requested on instance. Check the PerformanceMonitoringUnit enum for the list of possible values. 



### #threads_per_core
    
    
    def threads_per_core() -> ::Integer

**Returns**

  * (::Integer) — The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



### #threads_per_core=
    
    
    def threads_per_core=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



**Returns**

  * (::Integer) — The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



### #turbo_mode
    
    
    def turbo_mode() -> ::String

**Returns**

  * (::String) — Turbo frequency mode to use for the instance. Supported modes include:

    * ALL_CORE_MAX

Using empty string or not setting this field will use the platform-specific default turbo mode. 




### #turbo_mode=
    
    
    def turbo_mode=(value) -> ::String

**Parameter**

  * **value** (::String) — Turbo frequency mode to use for the instance. Supported modes include:

    * ALL_CORE_MAX

Using empty string or not setting this field will use the platform-specific default turbo mode. 




**Returns**

  * (::String) — Turbo frequency mode to use for the instance. Supported modes include:

    * ALL_CORE_MAX

Using empty string or not setting this field will use the platform-specific default turbo mode. 




### #visible_core_count
    
    
    def visible_core_count() -> ::Integer

**Returns**

  * (::Integer) — The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



### #visible_core_count=
    
    
    def visible_core_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



**Returns**

  * (::Integer) — The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
