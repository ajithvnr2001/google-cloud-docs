---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.PromoteClusterStatus
title: Class PromoteClusterStatus (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:43.698490+00:00
---

# Class PromoteClusterStatus (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.PromoteClusterStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PromoteClusterStatus (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    PromoteClusterStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for current status of the database during Promote Cluster operation.

## Attribute  
  
---  
**Name** | **Description**  
`state` |  `[google.cloud.alloydb_v1alpha.types.PromoteClusterStatus.State](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.PromoteClusterStatus.State)`   
Output only. The current state of the promoted secondary's database. Once the operation is complete, the final state of the database in the LRO can be one of: 1\. PROMOTE_CLUSTER_AVAILABLE_FOR_READ, indicating that the promote operation has failed mid-way, the database is still only available for read. 2\. PROMOTE_CLUSTER_COMPLETED, indicating that a promote operation completed successfully. The database is available for both read and write requests   
  
## Classes 

### State
    
    
    State(value)

State contains all valid states of the database during promote cluster operation. This is used for status reporting through the LRO metadata.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
