---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AccessConfig/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AccessConfig (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:57.070992+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AccessConfig (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AccessConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AccessConfig (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AccessConfig.

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #external_ipv6
    
    
    def external_ipv6() -> ::String

**Returns**

  * (::String) — Applies to ipv6AccessConfigs only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored inexternalIpv6PrefixLength in ipv6AccessConfig. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork. 



### #external_ipv6=
    
    
    def external_ipv6=(value) -> ::String

**Parameter**

  * **value** (::String) — Applies to ipv6AccessConfigs only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored inexternalIpv6PrefixLength in ipv6AccessConfig. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork. 



**Returns**

  * (::String) — Applies to ipv6AccessConfigs only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored inexternalIpv6PrefixLength in ipv6AccessConfig. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork. 



### #external_ipv6_prefix_length
    
    
    def external_ipv6_prefix_length() -> ::Integer

**Returns**

  * (::Integer) — Applies to ipv6AccessConfigs only. The prefix length of the external IPv6 range. 



### #external_ipv6_prefix_length=
    
    
    def external_ipv6_prefix_length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Applies to ipv6AccessConfigs only. The prefix length of the external IPv6 range. 



**Returns**

  * (::Integer) — Applies to ipv6AccessConfigs only. The prefix length of the external IPv6 range. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#accessConfig for access configs. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#accessConfig for access configs. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#accessConfig for access configs. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of this access configuration. In accessConfigs (IPv4), the default and recommended name is External NAT, but you can use any arbitrary string, such as My external IP orNetwork Access. In ipv6AccessConfigs, the recommend name is External IPv6. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of this access configuration. In accessConfigs (IPv4), the default and recommended name is External NAT, but you can use any arbitrary string, such as My external IP orNetwork Access. In ipv6AccessConfigs, the recommend name is External IPv6. 



**Returns**

  * (::String) — The name of this access configuration. In accessConfigs (IPv4), the default and recommended name is External NAT, but you can use any arbitrary string, such as My external IP orNetwork Access. In ipv6AccessConfigs, the recommend name is External IPv6. 



### #nat_i_p
    
    
    def nat_i_p() -> ::String

**Returns**

  * (::String) — Applies to accessConfigs (IPv4) only. Anexternal IP address associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance. 



### #nat_i_p=
    
    
    def nat_i_p=(value) -> ::String

**Parameter**

  * **value** (::String) — Applies to accessConfigs (IPv4) only. Anexternal IP address associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance. 



**Returns**

  * (::String) — Applies to accessConfigs (IPv4) only. Anexternal IP address associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance. 



### #network_tier
    
    
    def network_tier() -> ::String

**Returns**

  * (::String) — This signifies the networking tier used for configuring this access configuration and can only take the following values: PREMIUM,STANDARD.

If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.

If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP. Check the NetworkTier enum for the list of possible values. 




### #network_tier=
    
    
    def network_tier=(value) -> ::String

**Parameter**

  * **value** (::String) — This signifies the networking tier used for configuring this access configuration and can only take the following values: PREMIUM,STANDARD.

If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.

If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP. Check the NetworkTier enum for the list of possible values. 




**Returns**

  * (::String) — This signifies the networking tier used for configuring this access configuration and can only take the following values: PREMIUM,STANDARD.

If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.

If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP. Check the NetworkTier enum for the list of possible values. 




### #public_ptr_domain_name
    
    
    def public_ptr_domain_name() -> ::String

**Returns**

  * (::String) — The DNS domain name for the public PTR record.

You can set this field only if the `setPublicPtr` field is enabled inaccessConfig. If this field is unspecified inipv6AccessConfig, a default PTR record will be created for first IP in associated external IPv6 range. 




### #public_ptr_domain_name=
    
    
    def public_ptr_domain_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The DNS domain name for the public PTR record.

You can set this field only if the `setPublicPtr` field is enabled inaccessConfig. If this field is unspecified inipv6AccessConfig, a default PTR record will be created for first IP in associated external IPv6 range. 




**Returns**

  * (::String) — The DNS domain name for the public PTR record.

You can set this field only if the `setPublicPtr` field is enabled inaccessConfig. If this field is unspecified inipv6AccessConfig, a default PTR record will be created for first IP in associated external IPv6 range. 




### #security_policy
    
    
    def security_policy() -> ::String

**Returns**

  * (::String) — The resource URL for the security policy associated with this access config. 



### #security_policy=
    
    
    def security_policy=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource URL for the security policy associated with this access config. 



**Returns**

  * (::String) — The resource URL for the security policy associated with this access config. 



### #set_public_ptr
    
    
    def set_public_ptr() -> ::Boolean

**Returns**

  * (::Boolean) — Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

This field is not used in ipv6AccessConfig. A default PTR record will be created if the VM has external IPv6 range associated. 




### #set_public_ptr=
    
    
    def set_public_ptr=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

This field is not used in ipv6AccessConfig. A default PTR record will be created if the VM has external IPv6 range associated. 




**Returns**

  * (::Boolean) — Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

This field is not used in ipv6AccessConfig. A default PTR record will be created if the VM has external IPv6 range associated. 




### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of configuration. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. Inipv6AccessConfigs, the default and only option isDIRECT_IPV6. Check the Type enum for the list of possible values. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of configuration. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. Inipv6AccessConfigs, the default and only option isDIRECT_IPV6. Check the Type enum for the list of possible values. 



**Returns**

  * (::String) — The type of configuration. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. Inipv6AccessConfigs, the default and only option isDIRECT_IPV6. Check the Type enum for the list of possible values. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
