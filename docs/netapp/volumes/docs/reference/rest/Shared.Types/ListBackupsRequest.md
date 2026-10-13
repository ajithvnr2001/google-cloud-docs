---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/Shared.Types/ListBackupsRequest/
title: ListBackupsRequest \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:19.107759+00:00
---

# ListBackupsRequest  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/Shared.Types/ListBackupsRequest/




#  ListBackupsRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



ListBackupsRequest lists backups.

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "orderBy": string,
      "filter": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The backupVault for which to retrieve backup information, in the format `projects/{projectId}/locations/{location}/backupVaults/{backupVaultId}`. To retrieve backup information for all locations, use "-" for the `{location}` value. To retrieve backup information for all backupVaults, use "-" for the `{backupVaultId}` value. To retrieve backup information for a volume, use "-" for the `{backupVaultId}` value and specify volume full name with the filter.  
`pageSize` |  `integer` The maximum number of items to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` The nextPageToken value to use if there are additional results to retrieve for this list request.  
`orderBy` |  `string` Sort results. Supported values are "name", "name desc" or "" (unsorted).  
`filter` |  `string` The standard list filter. If specified, backups will be returned based on the attribute name that matches the filter expression. If empty, then no backups are filtered out. See <https://google.aip.dev/160>  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-23 UTC."],[],[]] 
