---
url: https://docs.cloud.google.com/python/docs/reference/baremetalsolution/latest/google.cloud.bare_metal_solution_v2.types.VRF.VlanAttachment
title: Class VlanAttachment (1.15.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:38.101655+00:00
---

# Class VlanAttachment (1.15.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/baremetalsolution/latest/google.cloud.bare_metal_solution_v2.types.VRF.VlanAttachment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VlanAttachment (1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.3  1.9.0  1.8.1  1.7.5  1.6.0  1.5.1  1.4.2  1.3.1  1.2.1  1.1.3  1.0.1  0.1.1 
    
    
    VlanAttachment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

VLAN attachment details.

## Attributes  
  
---  
**Name** | **Description**  
`peer_vlan_id` |  `int`   
The peer vlan ID of the attachment.   
`peer_ip` |  `str`   
The peer IP of the attachment.   
`router_ip` |  `str`   
The router IP of the attachment.   
`pairing_key` |  `str`   
Input only. Pairing key.   
`qos_policy` |  `[google.cloud.bare_metal_solution_v2.types.VRF.QosPolicy](https://docs.cloud.google.com/python/docs/reference/baremetalsolution/latest/google.cloud.bare_metal_solution_v2.types.VRF.QosPolicy)`   
The QOS policy applied to this VLAN attachment. This value should be preferred to using qos at vrf level.   
`id` |  `str`   
Immutable. The identifier of the attachment within vrf.   
`interconnect_attachment` |  `str`   
Optional. The name of the vlan attachment within vrf. This is of the form projects/{project_number}/regions/{region}/interconnectAttachments/{interconnect_attachment}   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
