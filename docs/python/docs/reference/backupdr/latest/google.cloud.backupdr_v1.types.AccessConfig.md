---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig
title: Class AccessConfig (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:44.525645+00:00
---

# Class AccessConfig (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AccessConfig (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    AccessConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`type_` |  `[google.cloud.backupdr_v1.types.AccessConfig.AccessType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig.AccessType)`   
Optional. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. In ipv6AccessConfigs, the default and only option is DIRECT_IPV6. This field is a member of `oneof`_ `_type`.   
`name` |  `str`   
Optional. The name of this access configuration. This field is a member of `oneof`_ `_name`.   
`external_ip` |  `str`   
Optional. The external IP address of this access configuration. This field is a member of `oneof`_ `_external_ip`.   
`external_ipv6` |  `str`   
Optional. The external IPv6 address of this access configuration. This field is a member of `oneof`_ `_external_ipv6`.   
`external_ipv6_prefix_length` |  `int`   
Optional. The prefix length of the external IPv6 range. This field is a member of `oneof`_ `_external_ipv6_prefix_length`.   
`set_public_ptr` |  `bool`   
Optional. Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name. This field is a member of `oneof`_ `_set_public_ptr`.   
`public_ptr_domain_name` |  `str`   
Optional. The DNS domain name for the public PTR record. This field is a member of `oneof`_ `_public_ptr_domain_name`.   
`network_tier` |  `[google.cloud.backupdr_v1.types.AccessConfig.NetworkTier](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig.NetworkTier)`   
Optional. This signifies the networking tier used for configuring this access This field is a member of `oneof`_ `_network_tier`.   
  
## Classes 

### AccessType
    
    
    AccessType(value)

The type of configuration.

### NetworkTier
    
    
    NetworkTier(value)

Network tier property used by addresses, instances and forwarding rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
