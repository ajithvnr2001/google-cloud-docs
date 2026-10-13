---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.FutureReservation.ProtectionTier
title: Class ProtectionTier (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:53.419370+00:00
---

# Class ProtectionTier (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.FutureReservation.ProtectionTier

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ProtectionTier (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    ProtectionTier(value)

Protection tier for the workload.

## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_PROTECTION_TIER` | A value indicating that the enum field is not set.  
`CAPACITY_OPTIMIZED` | CAPACITY_OPTIMIZED capacity leverages redundancies (e.g. power, cooling) at the data center during normal operating conditions. In the event of infrastructure failures at data center (e.g. power and/or cooling failures), this workload may be disrupted. As a consequence, it has a weaker availability SLO than STANDARD.  
`PROTECTION_TIER_UNSPECIFIED` | Unspecified protection tier.  
`STANDARD` | STANDARD protection for workload that should be protected by redundancies (e.g. power, cooling) at the data center level. In the event of infrastructure failures at data center (e.g. power and/or cooling failures), this workload is expected to continue as normal using the redundancies.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
