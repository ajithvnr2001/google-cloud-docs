---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceBackupProperties/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:40.646458+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceBackupProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties.

ComputeInstanceBackupProperties represents Compute Engine instance backup properties.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #can_ip_forward
    
    
    def can_ip_forward() -> ::Boolean

**Returns**

  * (::Boolean) — Enables instances created based on these properties to send packets with source IP addresses other than their own and receive packets with destination IP addresses other than their own. If these instances will be used as an IP gateway or it will be set as the next-hop in a Route resource, specify `true`. If unsure, leave this set to `false`. See the https://cloud.google.com/vpc/docs/using-routes#canipforward documentation for more information. 



### #can_ip_forward=
    
    
    def can_ip_forward=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enables instances created based on these properties to send packets with source IP addresses other than their own and receive packets with destination IP addresses other than their own. If these instances will be used as an IP gateway or it will be set as the next-hop in a Route resource, specify `true`. If unsure, leave this set to `false`. See the https://cloud.google.com/vpc/docs/using-routes#canipforward documentation for more information. 



**Returns**

  * (::Boolean) — Enables instances created based on these properties to send packets with source IP addresses other than their own and receive packets with destination IP addresses other than their own. If these instances will be used as an IP gateway or it will be set as the next-hop in a Route resource, specify `true`. If unsure, leave this set to `false`. See the https://cloud.google.com/vpc/docs/using-routes#canipforward documentation for more information. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional text description for the instances that are created from these properties. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional text description for the instances that are created from these properties. 



**Returns**

  * (::String) — An optional text description for the instances that are created from these properties. 



### #disk
    
    
    def disk() -> ::Array<::Google::Cloud::BackupDR::V1::AttachedDisk>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — An array of disks that are associated with the instances that are created from these properties. 



### #disk=
    
    
    def disk=(value) -> ::Array<::Google::Cloud::BackupDR::V1::AttachedDisk>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — An array of disks that are associated with the instances that are created from these properties. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — An array of disks that are associated with the instances that are created from these properties. 



### #guest_accelerator
    
    
    def guest_accelerator() -> ::Array<::Google::Cloud::BackupDR::V1::AcceleratorConfig>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — A list of guest accelerator cards' type and count to use for instances created from these properties. 



### #guest_accelerator=
    
    
    def guest_accelerator=(value) -> ::Array<::Google::Cloud::BackupDR::V1::AcceleratorConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — A list of guest accelerator cards' type and count to use for instances created from these properties. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — A list of guest accelerator cards' type and count to use for instances created from these properties. 



### #key_revocation_action_type
    
    
    def key_revocation_action_type() -> ::Google::Cloud::BackupDR::V1::KeyRevocationActionType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. 



### #key_revocation_action_type=
    
    
    def key_revocation_action_type=(value) -> ::Google::Cloud::BackupDR::V1::KeyRevocationActionType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to instances that are created from these properties. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to instances that are created from these properties. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to instances that are created from these properties. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — The machine type to use for instances that are created from these properties. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The machine type to use for instances that are created from these properties. 



**Returns**

  * (::String) — The machine type to use for instances that are created from these properties. 



### #metadata
    
    
    def metadata() -> ::Google::Cloud::BackupDR::V1::Metadata

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — The metadata key/value pairs to assign to instances that are created from these properties. These pairs can consist of custom metadata or predefined keys. See https://cloud.google.com/compute/docs/metadata/overview for more information. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Cloud::BackupDR::V1::Metadata

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — The metadata key/value pairs to assign to instances that are created from these properties. These pairs can consist of custom metadata or predefined keys. See https://cloud.google.com/compute/docs/metadata/overview for more information. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — The metadata key/value pairs to assign to instances that are created from these properties. These pairs can consist of custom metadata or predefined keys. See https://cloud.google.com/compute/docs/metadata/overview for more information. 



### #min_cpu_platform
    
    
    def min_cpu_platform() -> ::String

**Returns**

  * (::String) — Minimum cpu/platform to be used by instances. The instance may be scheduled on the specified or newer cpu/platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: Intel Haswell` or `minCpuPlatform: Intel Sandy Bridge`. For more information, read https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform. 



### #min_cpu_platform=
    
    
    def min_cpu_platform=(value) -> ::String

**Parameter**

  * **value** (::String) — Minimum cpu/platform to be used by instances. The instance may be scheduled on the specified or newer cpu/platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: Intel Haswell` or `minCpuPlatform: Intel Sandy Bridge`. For more information, read https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform. 



**Returns**

  * (::String) — Minimum cpu/platform to be used by instances. The instance may be scheduled on the specified or newer cpu/platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: Intel Haswell` or `minCpuPlatform: Intel Sandy Bridge`. For more information, read https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform. 



### #network_interface
    
    
    def network_interface() -> ::Array<::Google::Cloud::BackupDR::V1::NetworkInterface>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — An array of network access configurations for this interface. 



### #network_interface=
    
    
    def network_interface=(value) -> ::Array<::Google::Cloud::BackupDR::V1::NetworkInterface>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — An array of network access configurations for this interface. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — An array of network access configurations for this interface. 



### #scheduling
    
    
    def scheduling() -> ::Google::Cloud::BackupDR::V1::Scheduling

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Specifies the scheduling options for the instances that are created from these properties. 



### #scheduling=
    
    
    def scheduling=(value) -> ::Google::Cloud::BackupDR::V1::Scheduling

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Specifies the scheduling options for the instances that are created from these properties. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Specifies the scheduling options for the instances that are created from these properties. 



### #service_account
    
    
    def service_account() -> ::Array<::Google::Cloud::BackupDR::V1::ServiceAccount>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — A list of service accounts with specified scopes. Access tokens for these service accounts are available to the instances that are created from these properties. Use metadata queries to obtain the access tokens for these instances. 



### #service_account=
    
    
    def service_account=(value) -> ::Array<::Google::Cloud::BackupDR::V1::ServiceAccount>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — A list of service accounts with specified scopes. Access tokens for these service accounts are available to the instances that are created from these properties. Use metadata queries to obtain the access tokens for these instances. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — A list of service accounts with specified scopes. Access tokens for these service accounts are available to the instances that are created from these properties. Use metadata queries to obtain the access tokens for these instances. 



### #source_instance
    
    
    def source_instance() -> ::String

**Returns**

  * (::String) — The source instance used to create this backup. This can be a partial or full URL to the resource. For example, the following are valid values: -https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance -projects/project/zones/zone/instances/instance 



### #source_instance=
    
    
    def source_instance=(value) -> ::String

**Parameter**

  * **value** (::String) — The source instance used to create this backup. This can be a partial or full URL to the resource. For example, the following are valid values: -https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance -projects/project/zones/zone/instances/instance 



**Returns**

  * (::String) — The source instance used to create this backup. This can be a partial or full URL to the resource. For example, the following are valid values: -https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance -projects/project/zones/zone/instances/instance 



### #tags
    
    
    def tags() -> ::Google::Cloud::BackupDR::V1::Tags

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — A list of tags to apply to the instances that are created from these properties. The tags identify valid sources or targets for network firewalls. The setTags method can modify this list of tags. Each tag within the list must comply with RFC1035 (https://www.ietf.org/rfc/rfc1035.txt). 



### #tags=
    
    
    def tags=(value) -> ::Google::Cloud::BackupDR::V1::Tags

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — A list of tags to apply to the instances that are created from these properties. The tags identify valid sources or targets for network firewalls. The setTags method can modify this list of tags. Each tag within the list must comply with RFC1035 (https://www.ietf.org/rfc/rfc1035.txt). 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — A list of tags to apply to the instances that are created from these properties. The tags identify valid sources or targets for network firewalls. The setTags method can modify this list of tags. Each tag within the list must comply with RFC1035 (https://www.ietf.org/rfc/rfc1035.txt). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
