---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo
title: Class HardwareInstallationInfo (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:45.779701+00:00
---

# Class HardwareInstallationInfo (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HardwareInstallationInfo (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    HardwareInstallationInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information for installation of a Hardware.

## Attributes  
  
---  
**Name** | **Description**  
`rack_location` |  `str`   
Required. Location of the rack in the site e.g. Floor 2, Room 201, Row 7, Rack 3.   
`power_distance_meters` |  `int`   
Required. Distance from the power outlet in meters.   
`switch_distance_meters` |  `int`   
Required. Distance from the network switch in meters.   
`rack_unit_dimensions` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Dimensions](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Dimensions)`   
Required. Dimensions of the rack unit.   
`rack_space` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.RackSpace](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RackSpace)`   
Required. Rack space allocated for the hardware.   
`rack_type` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo.RackType](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo.RackType)`   
Required. Type of the rack.   
  
## Classes 

### RackType
    
    
    RackType(value)

Valid rack types.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
