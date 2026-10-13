---
url: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.CompilationResultAction.Relation.IncrementalTableConfig
title: Class IncrementalTableConfig (0.11.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:27.578872+00:00
---

# Class IncrementalTableConfig (0.11.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.CompilationResultAction.Relation.IncrementalTableConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IncrementalTableConfig (0.11.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.4 (latest)  0.11.3  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.16  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    IncrementalTableConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains settings for relations of type `INCREMENTAL_TABLE`.

## Attributes  
  
---  
**Name** | **Description**  
`incremental_select_query` |  `str`   
The SELECT query which returns rows which should be inserted into the relation if it already exists and is not being refreshed.   
`refresh_disabled` |  `bool`   
Whether this table should be protected from being refreshed.   
`unique_key_parts` |  `MutableSequence[str]`   
A set of columns or SQL expressions used to define row uniqueness. If any duplicates are discovered (as defined by `unique_key_parts`), only the newly selected rows (as defined by `incremental_select_query`) will be included in the relation.   
`update_partition_filter` |  `str`   
A SQL expression conditional used to limit the set of existing rows considered for a merge operation (see `unique_key_parts` for more information).   
`incremental_pre_operations` |  `MutableSequence[str]`   
SQL statements to be executed before inserting new rows into the relation.   
`incremental_post_operations` |  `MutableSequence[str]`   
SQL statements to be executed after inserting new rows into the relation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
