---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-financialservices/latest/google.cloud.financialservices_v1.types.EngineConfig.HyperparameterSource
title: Class HyperparameterSource (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:47.045694+00:00
---

# Class HyperparameterSource (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-financialservices/latest/google.cloud.financialservices_v1.types.EngineConfig.HyperparameterSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HyperparameterSource (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.3 
    
    
    HyperparameterSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Parameters for bootstrapping an Engine Config with the results of another one.

## Attributes  
  
---  
**Name** | **Description**  
`source_engine_config` |  `str`   
Required. The resource name of the source EngineConfig whose outputs are used. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}`  
`source_engine_version` |  `str`   
Output only. The resource name of the EngineVersion that was used in the tuning run. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
