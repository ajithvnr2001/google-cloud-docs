---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AccessConfig
title: Google Cloud Backup Dr V1beta Client - Class AccessConfig (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:01.778804+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AccessConfig (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AccessConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AccessConfig (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AccessConfig.

An access configuration attached to an instance's network interface.

Only one access config per instance is supported.

Generated from protobuf message `google.cloud.backupdr.v1beta.AccessConfig`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ type` |  `int`   
Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6.  
`↳ name` |  `string`   
Optional. The name of this access configuration.  
`↳ external_ip` |  `string`   
Optional. The external IP address of this access configuration.  
`↳ external_ipv6` |  `string`   
Optional. The external IPv6 address of this access configuration.  
`↳ external_ipv6_prefix_length` |  `int`   
Optional. The prefix length of the external IPv6 range.  
`↳ set_public_ptr` |  `bool`   
Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.  
`↳ public_ptr_domain_name` |  `string`   
Optional. The DNS domain name for the public PTR record.  
`↳ network_tier` |  `int`   
Optional. This signifies the networking tier used for configuring this access  
  
### getType

Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasType

### clearType

### setType

Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Optional. The name of this access configuration.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasName

### clearName

### setName

Optional. The name of this access configuration.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExternalIp

Optional. The external IP address of this access configuration.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasExternalIp

### clearExternalIp

### setExternalIp

Optional. The external IP address of this access configuration.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExternalIpv6

Optional. The external IPv6 address of this access configuration.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasExternalIpv6

### clearExternalIpv6

### setExternalIpv6

Optional. The external IPv6 address of this access configuration.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExternalIpv6PrefixLength

Optional. The prefix length of the external IPv6 range.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasExternalIpv6PrefixLength

### clearExternalIpv6PrefixLength

### setExternalIpv6PrefixLength

Optional. The prefix length of the external IPv6 range.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSetPublicPtr

Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasSetPublicPtr

### clearSetPublicPtr

### setSetPublicPtr

Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPublicPtrDomainName

Optional. The DNS domain name for the public PTR record.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasPublicPtrDomainName

### clearPublicPtrDomainName

### setPublicPtrDomainName

Optional. The DNS domain name for the public PTR record.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNetworkTier

Optional. This signifies the networking tier used for configuring this access

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasNetworkTier

### clearNetworkTier

### setNetworkTier

Optional. This signifies the networking tier used for configuring this access

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
