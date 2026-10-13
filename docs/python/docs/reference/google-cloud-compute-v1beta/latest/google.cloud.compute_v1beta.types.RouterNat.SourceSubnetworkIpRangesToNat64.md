---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RouterNat.SourceSubnetworkIpRangesToNat64
title: Class SourceSubnetworkIpRangesToNat64 (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:45.735408+00:00
---

# Class SourceSubnetworkIpRangesToNat64 (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RouterNat.SourceSubnetworkIpRangesToNat64

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SourceSubnetworkIpRangesToNat64 (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    SourceSubnetworkIpRangesToNat64(value)

Specify the Nat option for NAT64, which can take one of the following values:

::

  * ALL_IPV6_SUBNETWORKS: All of the IP ranges in every Subnetwork are allowed to Nat.
  * LIST_OF_IPV6_SUBNETWORKS: A list of Subnetworks are allowed to Nat (specified in the field nat64_subnetwork below)



The default is NAT64_OPTION_UNSPECIFIED. Note that if this field contains NAT64_ALL_V6_SUBNETWORKS no other Router.Nat section in this region can also enable NAT64 for any Subnetworks in this network. Other Router.Nat sections can still be present to enable NAT44 only.

## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_SOURCE_SUBNETWORK_IP_RANGES_TO_NAT64` | A value indicating that the enum field is not set.  
`ALL_IPV6_SUBNETWORKS` | NAT64 is enabled for all the IPv6 subnet ranges. In dual stack subnets, NAT64 will only be enabled for IPv6-only VMs.  
`LIST_OF_IPV6_SUBNETWORKS` | NAT64 is enabled for a list of IPv6 subnet ranges. In dual stack subnets, NAT64 will only be enabled for IPv6-only VMs. If this option is used, the nat64_subnetworks field must be specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
