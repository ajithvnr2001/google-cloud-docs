---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DestinationVolumeParameters
title: Class DestinationVolumeParameters (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:17.917330+00:00
---

# Class DestinationVolumeParameters (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DestinationVolumeParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DestinationVolumeParameters (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    DestinationVolumeParameters(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DestinationVolumeParameters specify input parameters used for creating destination volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`storage_pool` |  `str`   
Required. Existing destination StoragePool name.   
`volume_id` |  `str`   
Desired destination volume resource id. If not specified, source volume's resource id will be used. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.   
`share_name` |  `str`   
Destination volume's share name. If not specified, source volume's share name will be used.   
`description` |  `str`   
Description for the destination volume. This field is a member of `oneof`_ `_description`.   
`tiering_policy` |  `[google.cloud.netapp_v1.types.TieringPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.TieringPolicy)`   
Optional. Tiering policy for the volume. This field is a member of `oneof`_ `_tiering_policy`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
