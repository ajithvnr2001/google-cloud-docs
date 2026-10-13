---
url: https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.ListVolumeBackupsRequest
title: Class ListVolumeBackupsRequest (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:30.283389+00:00
---

# Class ListVolumeBackupsRequest (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkebackup/latest/google.cloud.gke_backup_v1.types.ListVolumeBackupsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListVolumeBackupsRequest (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.19  0.4.4  0.3.0  0.2.2  0.1.1 
    
    
    ListVolumeBackupsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for ListVolumeBackups.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The Backup that contains the VolumeBackups to list. Format: `projects/*/locations/*/backupPlans/*/backups/*`  
`page_size` |  `int`   
Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's next_page_token to determine if there are more instances left to be queried.   
`page_token` |  `str`   
Optional. The value of next_page_token received from a previous `ListVolumeBackups` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListVolumeBackups` must match the call that provided the page token.   
`filter` |  `str`   
Optional. Field match expression used to filter the results.   
`order_by` |  `str`   
Optional. Field by which to sort the results.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
