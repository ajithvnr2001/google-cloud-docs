---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileClusterSummary
title: Class FileClusterSummary (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:05.237011+00:00
---

# Class FileClusterSummary (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileClusterSummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FileClusterSummary (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    FileClusterSummary(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The file cluster summary.

## Attributes  
  
---  
**Name** | **Description**  
`file_cluster_type` |  `[google.cloud.dlp_v2.types.FileClusterType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileClusterType)`   
The file cluster type.   
`file_store_info_type_summaries` |  `MutableSequence[[google.cloud.dlp_v2.types.FileStoreInfoTypeSummary](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileStoreInfoTypeSummary)]`   
InfoTypes detected in this cluster.   
`sensitivity_score` |  `[google.cloud.dlp_v2.types.SensitivityScore](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.SensitivityScore)`   
The sensitivity score of this cluster. The score will be SENSITIVITY_LOW if nothing has been scanned.   
`data_risk_level` |  `[google.cloud.dlp_v2.types.DataRiskLevel](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataRiskLevel)`   
The data risk level of this cluster. RISK_LOW if nothing has been scanned.   
`errors` |  `MutableSequence[[google.cloud.dlp_v2.types.Error](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Error)]`   
A list of errors detected while scanning this cluster. The list is truncated to 10 per cluster.   
`file_extensions_scanned` |  `MutableSequence[[google.cloud.dlp_v2.types.FileExtensionInfo](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileExtensionInfo)]`   
A sample of file types scanned in this cluster. Empty if no files were scanned. File extensions can be derived from the file name or the file content.   
`file_extensions_seen` |  `MutableSequence[[google.cloud.dlp_v2.types.FileExtensionInfo](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileExtensionInfo)]`   
A sample of file types seen in this cluster. Empty if no files were seen. File extensions can be derived from the file name or the file content.   
`no_files_exist` |  `bool`   
True if no files exist in this cluster. If the file store had more files than could be listed, this will be false even if no files for this cluster were seen and file_extensions_seen is empty.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
