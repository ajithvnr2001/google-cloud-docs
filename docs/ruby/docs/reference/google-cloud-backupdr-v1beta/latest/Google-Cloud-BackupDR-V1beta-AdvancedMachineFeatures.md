---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AdvancedMachineFeatures/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::AdvancedMachineFeatures (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:14.467671+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::AdvancedMachineFeatures (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AdvancedMachineFeatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::AdvancedMachineFeatures (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::AdvancedMachineFeatures.

Specifies options for controlling advanced machine features.

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

  * (::Boolean) — Optional. Whether to enable nested virtualization or not (default is false). 



### #enable_nested_virtualization=
    
    
    def enable_nested_virtualization=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to enable nested virtualization or not (default is false). 



**Returns**

  * (::Boolean) — Optional. Whether to enable nested virtualization or not (default is false). 



### #enable_uefi_networking
    
    
    def enable_uefi_networking() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to enable UEFI networking for instance creation. 



### #enable_uefi_networking=
    
    
    def enable_uefi_networking=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to enable UEFI networking for instance creation. 



**Returns**

  * (::Boolean) — Optional. Whether to enable UEFI networking for instance creation. 



### #threads_per_core
    
    
    def threads_per_core() -> ::Integer

**Returns**

  * (::Integer) — Optional. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



### #threads_per_core=
    
    
    def threads_per_core=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



**Returns**

  * (::Integer) — Optional. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed. 



### #visible_core_count
    
    
    def visible_core_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



### #visible_core_count=
    
    
    def visible_core_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



**Returns**

  * (::Integer) — Optional. The number of physical cores to expose to an instance. Multiply by the number of threads per core to compute the total number of virtual CPUs to expose to the instance. If unset, the number of cores is inferred from the instance's nominal CPU count and the underlying platform's SMT width. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
