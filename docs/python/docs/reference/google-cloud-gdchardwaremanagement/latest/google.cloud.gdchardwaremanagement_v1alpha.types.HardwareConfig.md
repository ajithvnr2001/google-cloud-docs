---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig
title: Class HardwareConfig (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:45.243664+00:00
---

# Class HardwareConfig (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HardwareConfig (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    HardwareConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for GDC hardware.

## Attributes  
  
---  
**Name** | **Description**  
`sku` |  `str`   
Required. Reference to the SKU for this hardware. This can point to a specific SKU revision in the form of `resource_name@revision_id` as defined in `AIP-162 `__. If no revision_id is specified, it refers to the latest revision.   
`power_supply` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.PowerSupply](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.PowerSupply)`   
Required. Power supply type for this hardware.   
`subscription_duration_months` |  `int`   
Optional. Subscription duration for the hardware in months.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
