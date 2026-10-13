---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container/
title: Container \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:42.972550+00:00
---

# Container  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Container Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a container that may contain DLP findings. Examples of a container include a file, table, or database record.

JSON representation  
---  
      
    
    {
      "type": string,
      "projectId": string,
      "fullPath": string,
      "rootPath": string,
      "relativePath": string,
      "updateTime": string,
      "version": string
    }  
  
Fields  
---  
`type` |  `string` Container type, for example BigQuery or Cloud Storage.  
`projectId` |  `string` Project where the finding was found. Can be different from the project that owns the finding.  
`fullPath` |  `string` A string representation of the full container name. Examples: - BigQuery: 'Project:DataSetId.TableId' - Cloud Storage: 'gs://Bucket/folders/filename.txt'  
`rootPath` |  `string` The root of the container. Examples:

  * For BigQuery table `projectId:datasetId.table_id`, the root is `datasetId`
  * For Cloud Storage file `gs://bucket/folder/filename.txt`, the root is `gs://bucket`

  
`relativePath` |  `string` The rest of the path after the root. Examples:

  * For BigQuery table `projectId:datasetId.table_id`, the relative path is `tableId`
  * For Cloud Storage file `gs://bucket/folder/filename.txt`, the relative path is `folder/filename.txt`

  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Findings container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the lastModifiedTime property. For Datastore, this field isn't populated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`version` |  `string` Findings container version, if available ("generation" for Cloud Storage).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-09 UTC."],[],[]] 
