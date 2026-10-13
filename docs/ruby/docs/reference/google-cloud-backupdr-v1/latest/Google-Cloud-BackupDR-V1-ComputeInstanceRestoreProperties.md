---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:40.230904+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties.

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advanced_machine_features
    
    
    def advanced_machine_features() -> ::Google::Cloud::BackupDR::V1::AdvancedMachineFeatures

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AdvancedMachineFeatures)) — Optional. Controls for advanced machine-related behavior features. 



### #advanced_machine_features=
    
    
    def advanced_machine_features=(value) -> ::Google::Cloud::BackupDR::V1::AdvancedMachineFeatures

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AdvancedMachineFeatures)) — Optional. Controls for advanced machine-related behavior features. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AdvancedMachineFeatures](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AdvancedMachineFeatures)) — Optional. Controls for advanced machine-related behavior features. 



### #allocation_affinity
    
    
    def allocation_affinity() -> ::Google::Cloud::BackupDR::V1::AllocationAffinity

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AllocationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AllocationAffinity)) — Optional. Specifies the reservations that this instance can consume from. 



### #allocation_affinity=
    
    
    def allocation_affinity=(value) -> ::Google::Cloud::BackupDR::V1::AllocationAffinity

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AllocationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AllocationAffinity)) — Optional. Specifies the reservations that this instance can consume from. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AllocationAffinity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AllocationAffinity)) — Optional. Specifies the reservations that this instance can consume from. 



### #can_ip_forward
    
    
    def can_ip_forward() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Allows this instance to send and receive packets with non-matching destination or source IPs. 



### #can_ip_forward=
    
    
    def can_ip_forward=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Allows this instance to send and receive packets with non-matching destination or source IPs. 



**Returns**

  * (::Boolean) — Optional. Allows this instance to send and receive packets with non-matching destination or source IPs. 



### #confidential_instance_config
    
    
    def confidential_instance_config() -> ::Google::Cloud::BackupDR::V1::ConfidentialInstanceConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ConfidentialInstanceConfig)) — Optional. Controls Confidential compute options on the instance 



### #confidential_instance_config=
    
    
    def confidential_instance_config=(value) -> ::Google::Cloud::BackupDR::V1::ConfidentialInstanceConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ConfidentialInstanceConfig)) — Optional. Controls Confidential compute options on the instance 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ConfidentialInstanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ConfidentialInstanceConfig)) — Optional. Controls Confidential compute options on the instance 



### #deletion_protection
    
    
    def deletion_protection() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the resource should be protected against deletion. 



### #deletion_protection=
    
    
    def deletion_protection=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the resource should be protected against deletion. 



**Returns**

  * (::Boolean) — Optional. Whether the resource should be protected against deletion. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



**Returns**

  * (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



### #disks
    
    
    def disks() -> ::Array<::Google::Cloud::BackupDR::V1::AttachedDisk>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — Optional. Array of disks associated with this instance. Persistent disks must be created before you can assign them. Source regional persistent disks will be restored with default replica zones if not specified. 



### #disks=
    
    
    def disks=(value) -> ::Array<::Google::Cloud::BackupDR::V1::AttachedDisk>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — Optional. Array of disks associated with this instance. Persistent disks must be created before you can assign them. Source regional persistent disks will be restored with default replica zones if not specified. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AttachedDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk)>) — Optional. Array of disks associated with this instance. Persistent disks must be created before you can assign them. Source regional persistent disks will be restored with default replica zones if not specified. 



### #display_device
    
    
    def display_device() -> ::Google::Cloud::BackupDR::V1::DisplayDevice

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DisplayDevice)) — Optional. Enables display device for the instance. 



### #display_device=
    
    
    def display_device=(value) -> ::Google::Cloud::BackupDR::V1::DisplayDevice

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DisplayDevice)) — Optional. Enables display device for the instance. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DisplayDevice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DisplayDevice)) — Optional. Enables display device for the instance. 



### #guest_accelerators
    
    
    def guest_accelerators() -> ::Array<::Google::Cloud::BackupDR::V1::AcceleratorConfig>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — Optional. A list of the type and count of accelerator cards attached to the instance. 



### #guest_accelerators=
    
    
    def guest_accelerators=(value) -> ::Array<::Google::Cloud::BackupDR::V1::AcceleratorConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — Optional. A list of the type and count of accelerator cards attached to the instance. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::AcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AcceleratorConfig)>) — Optional. A list of the type and count of accelerator cards attached to the instance. 



### #hostname
    
    
    def hostname() -> ::String

**Returns**

  * (::String) — Optional. Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



### #hostname=
    
    
    def hostname=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



**Returns**

  * (::String) — Optional. Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. 



### #instance_encryption_key
    
    
    def instance_encryption_key() -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts suspended data for an instance with a customer-managed encryption key. 



### #instance_encryption_key=
    
    
    def instance_encryption_key=(value) -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts suspended data for an instance with a customer-managed encryption key. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts suspended data for an instance with a customer-managed encryption key. 



### #key_revocation_action_type
    
    
    def key_revocation_action_type() -> ::Google::Cloud::BackupDR::V1::KeyRevocationActionType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — Optional. KeyRevocationActionType of the instance. 



### #key_revocation_action_type=
    
    
    def key_revocation_action_type=(value) -> ::Google::Cloud::BackupDR::V1::KeyRevocationActionType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — Optional. KeyRevocationActionType of the instance. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::KeyRevocationActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-KeyRevocationActionType)) — Optional. KeyRevocationActionType of the instance. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this instance. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this instance. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this instance. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — Optional. Full or partial URL of the machine type resource to use for this instance. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Full or partial URL of the machine type resource to use for this instance. 



**Returns**

  * (::String) — Optional. Full or partial URL of the machine type resource to use for this instance. 



### #metadata
    
    
    def metadata() -> ::Google::Cloud::BackupDR::V1::Metadata

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — Optional. This includes custom metadata and predefined keys. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Cloud::BackupDR::V1::Metadata

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — Optional. This includes custom metadata and predefined keys. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Metadata)) — Optional. This includes custom metadata and predefined keys. 



### #min_cpu_platform
    
    
    def min_cpu_platform() -> ::String

**Returns**

  * (::String) — Optional. Minimum CPU platform to use for this instance. 



### #min_cpu_platform=
    
    
    def min_cpu_platform=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Minimum CPU platform to use for this instance. 



**Returns**

  * (::String) — Optional. Minimum CPU platform to use for this instance. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the compute instance. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the compute instance. 



**Returns**

  * (::String) — Required. Name of the compute instance. 



### #network_interfaces
    
    
    def network_interfaces() -> ::Array<::Google::Cloud::BackupDR::V1::NetworkInterface>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — Optional. An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. Required to restore in different project or region. 



### #network_interfaces=
    
    
    def network_interfaces=(value) -> ::Array<::Google::Cloud::BackupDR::V1::NetworkInterface>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — Optional. An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. Required to restore in different project or region. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::NetworkInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkInterface)>) — Optional. An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. Required to restore in different project or region. 



### #network_performance_config
    
    
    def network_performance_config() -> ::Google::Cloud::BackupDR::V1::NetworkPerformanceConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkPerformanceConfig)) — Optional. Configure network performance such as egress bandwidth tier. 



### #network_performance_config=
    
    
    def network_performance_config=(value) -> ::Google::Cloud::BackupDR::V1::NetworkPerformanceConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkPerformanceConfig)) — Optional. Configure network performance such as egress bandwidth tier. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::NetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-NetworkPerformanceConfig)) — Optional. Configure network performance such as egress bandwidth tier. 



### #params
    
    
    def params() -> ::Google::Cloud::BackupDR::V1::InstanceParams

**Returns**

  * ([::Google::Cloud::BackupDR::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InstanceParams)) — Input only. Additional params passed with the request, but not persisted as part of resource payload. 



### #params=
    
    
    def params=(value) -> ::Google::Cloud::BackupDR::V1::InstanceParams

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InstanceParams)) — Input only. Additional params passed with the request, but not persisted as part of resource payload. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::InstanceParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InstanceParams)) — Input only. Additional params passed with the request, but not persisted as part of resource payload. 



### #private_ipv6_google_access
    
    
    def private_ipv6_google_access() -> ::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess

**Returns**

  * ([::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties-InstancePrivateIpv6GoogleAccess)) — Optional. The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. 



### #private_ipv6_google_access=
    
    
    def private_ipv6_google_access=(value) -> ::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties-InstancePrivateIpv6GoogleAccess)) — Optional. The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties-InstancePrivateIpv6GoogleAccess)) — Optional. The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. 



### #resource_policies
    
    
    def resource_policies() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Resource policies applied to this instance. By default, no resource policies will be applied. 



### #resource_policies=
    
    
    def resource_policies=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Resource policies applied to this instance. By default, no resource policies will be applied. 



**Returns**

  * (::Array<::String>) — Optional. Resource policies applied to this instance. By default, no resource policies will be applied. 



### #scheduling
    
    
    def scheduling() -> ::Google::Cloud::BackupDR::V1::Scheduling

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Optional. Sets the scheduling options for this instance. 



### #scheduling=
    
    
    def scheduling=(value) -> ::Google::Cloud::BackupDR::V1::Scheduling

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Optional. Sets the scheduling options for this instance. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Scheduling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Scheduling)) — Optional. Sets the scheduling options for this instance. 



### #service_accounts
    
    
    def service_accounts() -> ::Array<::Google::Cloud::BackupDR::V1::ServiceAccount>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — Optional. A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported. 



### #service_accounts=
    
    
    def service_accounts=(value) -> ::Array<::Google::Cloud::BackupDR::V1::ServiceAccount>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — Optional. A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::ServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ServiceAccount)>) — Optional. A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported. 



### #tags
    
    
    def tags() -> ::Google::Cloud::BackupDR::V1::Tags

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — Optional. Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. 



### #tags=
    
    
    def tags=(value) -> ::Google::Cloud::BackupDR::V1::Tags

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — Optional. Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Tags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Tags)) — Optional. Tags to apply to this instance. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during instance creation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
