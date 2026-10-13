---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.PrivacyMetric.DeltaPresenceEstimationConfig
title: Class DeltaPresenceEstimationConfig (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:23.233988+00:00
---

# Class DeltaPresenceEstimationConfig (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.PrivacyMetric.DeltaPresenceEstimationConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeltaPresenceEstimationConfig (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    DeltaPresenceEstimationConfig(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

δ-presence metric, used to estimate how likely it is for an attacker to figure out that one given individual appears in a de-identified dataset. Similarly to the k-map metric, we cannot compute δ-presence exactly without knowing the attack dataset, so we use a statistical model instead.

## Attributes  
  
---  
**Name** | **Description**  
`quasi_ids` |  `MutableSequence[[google.cloud.dlp_v2.types.QuasiId](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.QuasiId)]`   
Required. Fields considered to be quasi-identifiers. No two fields can have the same tag.   
`region_code` |  `str`   
ISO 3166-1 alpha-2 region code to use in the statistical modeling. Set if no column is tagged with a region-specific InfoType (like US_ZIP_5) or a region code.   
`auxiliary_tables` |  `MutableSequence[[google.cloud.dlp_v2.types.StatisticalTable](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.StatisticalTable)]`   
Several auxiliary tables can be used in the analysis. Each custom_tag used to tag a quasi-identifiers field must appear in exactly one field of one auxiliary table.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
