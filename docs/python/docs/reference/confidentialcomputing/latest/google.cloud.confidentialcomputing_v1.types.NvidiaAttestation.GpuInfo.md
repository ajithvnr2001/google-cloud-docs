---
url: https://docs.cloud.google.com/python/docs/reference/confidentialcomputing/latest/google.cloud.confidentialcomputing_v1.types.NvidiaAttestation.GpuInfo
title: Class GpuInfo (0.11.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:03.441452+00:00
---

# Class GpuInfo (0.11.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/confidentialcomputing/latest/google.cloud.confidentialcomputing_v1.types.NvidiaAttestation.GpuInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GpuInfo (0.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.2 (latest)  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.18  0.3.0  0.2.0  0.1.1 
    
    
    GpuInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

GpuInfo contains the attestation evidence for a GPU device.

## Attributes  
  
---  
**Name** | **Description**  
`uuid` |  `str`   
Optional. The UUID of the GPU device.   
`driver_version` |  `str`   
Optional. The driver version of the GPU.   
`vbios_version` |  `str`   
Optional. The vBIOS version of the GPU.   
`gpu_architecture_type` |  `[google.cloud.confidentialcomputing_v1.types.NvidiaAttestation.GpuArchitectureType](https://docs.cloud.google.com/python/docs/reference/confidentialcomputing/latest/google.cloud.confidentialcomputing_v1.types.NvidiaAttestation.GpuArchitectureType)`   
Optional. The GPU architecture type.   
`attestation_certificate_chain` |  `bytes`   
Optional. The raw attestation certificate chain for the GPU device.   
`attestation_report` |  `bytes`   
Optional. The raw attestation report for the GPU device. This field contains SPDM request/response defined in https://www.dmtf.org/sites/default/files/standards/documents/DSP0274_1.1.0.pdf   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
