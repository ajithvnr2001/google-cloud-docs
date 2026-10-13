---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.CloudSQLBackupRunSource
title: Class CloudSQLBackupRunSource (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:29.660397+00:00
---

# Class CloudSQLBackupRunSource (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.CloudSQLBackupRunSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudSQLBackupRunSource (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    CloudSQLBackupRunSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The source CloudSQL backup resource.

## Attributes  
  
---  
**Name** | **Description**  
`project` |  `str`   
The project ID of the source CloudSQL instance. This should be the same as the AlloyDB cluster's project.   
`instance_id` |  `str`   
Required. The CloudSQL instance ID.   
`backup_run_id` |  `int`   
Required. The CloudSQL backup run ID.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
