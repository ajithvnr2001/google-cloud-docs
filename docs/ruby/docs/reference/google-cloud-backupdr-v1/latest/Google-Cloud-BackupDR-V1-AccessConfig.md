---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AccessConfig (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:23.972068+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AccessConfig (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AccessConfig (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::AccessConfig.

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #external_ip
    
    
    def external_ip() -> ::String

**Returns**

  * (::String) — Optional. The external IP address of this access configuration. 



### #external_ip=
    
    
    def external_ip=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The external IP address of this access configuration. 



**Returns**

  * (::String) — Optional. The external IP address of this access configuration. 



### #external_ipv6
    
    
    def external_ipv6() -> ::String

**Returns**

  * (::String) — Optional. The external IPv6 address of this access configuration. 



### #external_ipv6=
    
    
    def external_ipv6=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The external IPv6 address of this access configuration. 



**Returns**

  * (::String) — Optional. The external IPv6 address of this access configuration. 



### #external_ipv6_prefix_length
    
    
    def external_ipv6_prefix_length() -> ::Integer

**Returns**

  * (::Integer) — Optional. The prefix length of the external IPv6 range. 



### #external_ipv6_prefix_length=
    
    
    def external_ipv6_prefix_length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The prefix length of the external IPv6 range. 



**Returns**

  * (::Integer) — Optional. The prefix length of the external IPv6 range. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Optional. The name of this access configuration. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name of this access configuration. 



**Returns**

  * (::String) — Optional. The name of this access configuration. 



### #network_tier
    
    
    def network_tier() -> ::Google::Cloud::BackupDR::V1::AccessConfig::NetworkTier

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AccessConfig::NetworkTier](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-NetworkTier)) — Optional. This signifies the networking tier used for configuring this access 



### #network_tier=
    
    
    def network_tier=(value) -> ::Google::Cloud::BackupDR::V1::AccessConfig::NetworkTier

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AccessConfig::NetworkTier](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-NetworkTier)) — Optional. This signifies the networking tier used for configuring this access 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AccessConfig::NetworkTier](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-NetworkTier)) — Optional. This signifies the networking tier used for configuring this access 



### #public_ptr_domain_name
    
    
    def public_ptr_domain_name() -> ::String

**Returns**

  * (::String) — Optional. The DNS domain name for the public PTR record. 



### #public_ptr_domain_name=
    
    
    def public_ptr_domain_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The DNS domain name for the public PTR record. 



**Returns**

  * (::String) — Optional. The DNS domain name for the public PTR record. 



### #set_public_ptr
    
    
    def set_public_ptr() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name. 



### #set_public_ptr=
    
    
    def set_public_ptr=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name. 



**Returns**

  * (::Boolean) — Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name. 



### #type
    
    
    def type() -> ::Google::Cloud::BackupDR::V1::AccessConfig::AccessType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AccessConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-AccessType)) — Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::BackupDR::V1::AccessConfig::AccessType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AccessConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-AccessType)) — Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AccessConfig::AccessType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AccessConfig-AccessType)) — Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
