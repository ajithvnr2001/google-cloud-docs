---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ZoneNetworkConfig
title: Class ZoneNetworkConfig (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:55.354678+00:00
---

# Class ZoneNetworkConfig (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ZoneNetworkConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ZoneNetworkConfig (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    ZoneNetworkConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Networking configuration for a zone.

## Attributes  
  
---  
**Name** | **Description**  
`machine_mgmt_ipv4_range` |  `str`   
Required. An IPv4 address block for machine management. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per machine in the Zone. Should be in `management_ipv4_subnet`, and disjoint with other address ranges.   
`kubernetes_node_ipv4_range` |  `str`   
Required. An IPv4 address block for kubernetes nodes. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per machine in the Zone. Should be in `kubernetes_ipv4_subnet`, and disjoint with other address ranges.   
`kubernetes_control_plane_ipv4_range` |  `str`   
Required. An IPv4 address block for kubernetes control plane. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per cluster in the Zone. Should be in `kubernetes_ipv4_subnet`, and disjoint with other address ranges.   
`management_ipv4_subnet` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Subnet](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Subnet)`   
Required. An IPv4 subnet for the management network.   
`kubernetes_ipv4_subnet` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Subnet](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Subnet)`   
Optional. An IPv4 subnet for the kubernetes network. If unspecified, the kubernetes subnet will be the same as the management subnet.   
`dns_ipv4_addresses` |  `MutableSequence[str]`   
Optional. DNS nameservers. The GDC Infrastructure will resolve DNS queries via these IPs. If unspecified, Google DNS is used.   
`kubernetes_primary_vlan_id` |  `int`   
Optional. Kubernetes VLAN ID. By default, the kubernetes node, including the primary kubernetes network, are in the same VLAN as the machine management network. For network segmentation purposes, these can optionally be separated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
