---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDbVersions
title: REST Resource: projects.locations.autonomousDbVersions \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:41.342502+00:00
---

# REST Resource: projects.locations.autonomousDbVersions  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDbVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.autonomousDbVersions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AutonomousDbVersion
    * JSON representation
  * Methods



## Resource: AutonomousDbVersion

Details of the Autonomous Database version. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDbVersionSummary/>

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "dbWorkload": enum ([DBWorkload](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DBWorkload)),
      "workloadUri": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Autonomous Database Version resource with the format: projects/{project}/locations/{region}/autonomousDbVersions/{autonomous_db_version}  
`version` |  `string` Output only. An Oracle Database version for Autonomous Database.  
`dbWorkload` |  `enum (`[DBWorkload](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DBWorkload)`)` Output only. The Autonomous Database workload type.  
`workloadUri` |  `string` Output only. A URL that points to a detailed description of the Autonomous Database version.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDbVersions/list)`

|  Lists all the available Autonomous Database versions for a project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
