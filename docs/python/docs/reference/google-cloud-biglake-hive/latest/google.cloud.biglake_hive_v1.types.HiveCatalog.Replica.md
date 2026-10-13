---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1.types.HiveCatalog.Replica
title: Class Replica (0.3.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:29.295628+00:00
---

# Class Replica (0.3.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1.types.HiveCatalog.Replica

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Replica (0.3.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.5 (latest)  0.3.4  0.2.0  0.1.0 
    
    
    Replica(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The replica of the Catalog.

## Attributes  
  
---  
**Name** | **Description**  
`region` |  `str`   
Output only. The region of the replica. For example `us-east1`.   
`state` |  `[google.cloud.biglake_hive_v1.types.HiveCatalog.Replica.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1.types.HiveCatalog.Replica.State)`   
Output only. The current state of the replica.   
  
## Classes 

### State
    
    
    State(value)

If the catalog is replicated to multiple regions, this enum describes the current state of the replica.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
