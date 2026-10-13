---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo
title: Class HardwarePhysicalInfo (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:11.201431+00:00
---

# Class HardwarePhysicalInfo (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HardwarePhysicalInfo (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    HardwarePhysicalInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Physical properties of a hardware.

## Attributes  
  
---  
**Name** | **Description**  
`power_receptacle` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.PowerReceptacleType](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.PowerReceptacleType)`   
Required. The power receptacle type.   
`network_uplink` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.NetworkUplinkType](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.NetworkUplinkType)`   
Required. Type of the uplink network connection.   
`voltage` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Voltage](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Voltage)`   
Required. Voltage of the power supply.   
`amperes` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Amperes](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Amperes)`   
Required. Amperes of the power supply.   
  
## Classes 

### Amperes
    
    
    Amperes(value)

Valid amperes values.

### NetworkUplinkType
    
    
    NetworkUplinkType(value)

Valid network uplink types.

### PowerReceptacleType
    
    
    PowerReceptacleType(value)

Valid power receptacle types.

### Voltage
    
    
    Voltage(value)

Valid voltage values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
