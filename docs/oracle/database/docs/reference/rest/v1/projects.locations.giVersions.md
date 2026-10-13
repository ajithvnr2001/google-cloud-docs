---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions
title: REST Resource: projects.locations.giVersions \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:47.351323+00:00
---

# REST Resource: projects.locations.giVersions  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.giVersions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GiVersion
    * JSON representation
  * Methods



## Resource: GiVersion

Details of the Oracle Grid Infrastructure (GI) version resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/GiVersionSummary/>

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Oracle Grid Infrastructure (GI) version resource with the format: projects/{project}/locations/{region}/giVersions/{giVersions}  
`version` |  `string` Optional. version  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions/list)`

|  Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
