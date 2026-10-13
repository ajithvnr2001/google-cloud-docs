---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::NetworkInterface (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:59.849337+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::NetworkInterface (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::NetworkInterface (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::NetworkInterface.

A network interface resource attached to an instance. s

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_configs
    
    
    def access_configs() -> ::Array<::Google::Cloud::BackupDR::V1beta::AccessConfig>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of configurations for this interface. Currently, only one access config,ONE_TO_ONE_NAT is supported. If there are no accessConfigs specified, then this instance will have no external internet access. 



### #access_configs=
    
    
    def access_configs=(value) -> ::Array<::Google::Cloud::BackupDR::V1beta::AccessConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of configurations for this interface. Currently, only one access config,ONE_TO_ONE_NAT is supported. If there are no accessConfigs specified, then this instance will have no external internet access. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of configurations for this interface. Currently, only one access config,ONE_TO_ONE_NAT is supported. If there are no accessConfigs specified, then this instance will have no external internet access. 



### #alias_ip_ranges
    
    
    def alias_ip_ranges() -> ::Array<::Google::Cloud::BackupDR::V1beta::AliasIpRange>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AliasIpRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AliasIpRange)>) — Optional. An array of alias IP ranges for this network interface. You can only specify this field for network interfaces in VPC networks. 



### #alias_ip_ranges=
    
    
    def alias_ip_ranges=(value) -> ::Array<::Google::Cloud::BackupDR::V1beta::AliasIpRange>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1beta::AliasIpRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AliasIpRange)>) — Optional. An array of alias IP ranges for this network interface. You can only specify this field for network interfaces in VPC networks. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AliasIpRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AliasIpRange)>) — Optional. An array of alias IP ranges for this network interface. You can only specify this field for network interfaces in VPC networks. 



### #internal_ipv6_prefix_length
    
    
    def internal_ipv6_prefix_length() -> ::Integer

**Returns**

  * (::Integer) — Optional. The prefix length of the primary internal IPv6 range. 



### #internal_ipv6_prefix_length=
    
    
    def internal_ipv6_prefix_length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The prefix length of the primary internal IPv6 range. 



**Returns**

  * (::Integer) — Optional. The prefix length of the primary internal IPv6 range. 



### #ip_address
    
    
    def ip_address() -> ::String

**Returns**

  * (::String) — Optional. An IPv4 internal IP address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system. 



### #ip_address=
    
    
    def ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An IPv4 internal IP address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system. 



**Returns**

  * (::String) — Optional. An IPv4 internal IP address to assign to the instance for this network interface. If not specified by the user, an unused internal IP is assigned by the system. 



### #ipv6_access_configs
    
    
    def ipv6_access_configs() -> ::Array<::Google::Cloud::BackupDR::V1beta::AccessConfig>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of IPv6 access configurations for this interface. Currently, only one IPv6 access config, DIRECT_IPV6, is supported. If there is no ipv6AccessConfig specified, then this instance will have no external IPv6 Internet access. 



### #ipv6_access_configs=
    
    
    def ipv6_access_configs=(value) -> ::Array<::Google::Cloud::BackupDR::V1beta::AccessConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of IPv6 access configurations for this interface. Currently, only one IPv6 access config, DIRECT_IPV6, is supported. If there is no ipv6AccessConfig specified, then this instance will have no external IPv6 Internet access. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::AccessConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AccessConfig)>) — Optional. An array of IPv6 access configurations for this interface. Currently, only one IPv6 access config, DIRECT_IPV6, is supported. If there is no ipv6AccessConfig specified, then this instance will have no external IPv6 Internet access. 



### #ipv6_access_type
    
    
    def ipv6_access_type() -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::Ipv6AccessType

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::Ipv6AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-Ipv6AccessType)) — Optional. [Output Only] One of EXTERNAL, INTERNAL to indicate whether the IP can be accessed from the Internet. This field is always inherited from its subnetwork. 



### #ipv6_access_type=
    
    
    def ipv6_access_type=(value) -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::Ipv6AccessType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::Ipv6AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-Ipv6AccessType)) — Optional. [Output Only] One of EXTERNAL, INTERNAL to indicate whether the IP can be accessed from the Internet. This field is always inherited from its subnetwork. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::Ipv6AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-Ipv6AccessType)) — Optional. [Output Only] One of EXTERNAL, INTERNAL to indicate whether the IP can be accessed from the Internet. This field is always inherited from its subnetwork. 



### #ipv6_address
    
    
    def ipv6_address() -> ::String

**Returns**

  * (::String) — Optional. An IPv6 internal network address for this network interface. To use a static internal IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an internal IPv6 address from the instance's subnetwork. 



### #ipv6_address=
    
    
    def ipv6_address=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An IPv6 internal network address for this network interface. To use a static internal IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an internal IPv6 address from the instance's subnetwork. 



**Returns**

  * (::String) — Optional. An IPv6 internal network address for this network interface. To use a static internal IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an internal IPv6 address from the instance's subnetwork. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The name of the network interface, which is generated by the server. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Optional. URL of the VPC network resource for this instance. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. URL of the VPC network resource for this instance. 



**Returns**

  * (::String) — Optional. URL of the VPC network resource for this instance. 



### #network_attachment
    
    
    def network_attachment() -> ::String

**Returns**

  * (::String) — Optional. The URL of the network attachment that this interface should connect to in the following format: projects/{project_number}/regions/{region_name}/networkAttachments/{network_attachment_name}. 



### #network_attachment=
    
    
    def network_attachment=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The URL of the network attachment that this interface should connect to in the following format: projects/{project_number}/regions/{region_name}/networkAttachments/{network_attachment_name}. 



**Returns**

  * (::String) — Optional. The URL of the network attachment that this interface should connect to in the following format: projects/{project_number}/regions/{region_name}/networkAttachments/{network_attachment_name}. 



### #nic_type
    
    
    def nic_type() -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::NicType

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #nic_type=
    
    
    def nic_type=(value) -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::NicType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::NicType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-NicType)) — Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. 



### #queue_count
    
    
    def queue_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It'll be empty if not specified by the users. 



### #queue_count=
    
    
    def queue_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It'll be empty if not specified by the users. 



**Returns**

  * (::Integer) — Optional. The networking queue count that's specified by users for the network interface. Both Rx and Tx queues will be set to this number. It'll be empty if not specified by the users. 



### #stack_type
    
    
    def stack_type() -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::StackType

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-StackType)) — The stack type for this network interface. 



### #stack_type=
    
    
    def stack_type=(value) -> ::Google::Cloud::BackupDR::V1beta::NetworkInterface::StackType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-StackType)) — The stack type for this network interface. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::NetworkInterface::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-NetworkInterface-StackType)) — The stack type for this network interface. 



### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — Optional. The URL of the Subnetwork resource for this instance. 



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The URL of the Subnetwork resource for this instance. 



**Returns**

  * (::String) — Optional. The URL of the Subnetwork resource for this instance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
