---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DdlStatementActionInfo/
title: DdlStatementActionInfo \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:17.602171+00:00
---

# DdlStatementActionInfo  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DdlStatementActionInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  DdlStatementActionInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Action information extracted from a DDL statement. This proto is used to display the brief info of the DDL statement for the operation `[databases.updateDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/updateDdl#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)`.

JSON representation  
---  
      
    
    {
      "action": string,
      "entityType": string,
      "entityNames": [
        string
      ]
    }  
  
Fields  
---  
`action` |  `string` The action for the DDL statement, for example, CREATE, ALTER, DROP, GRANT, etc. This field is a non-empty string.  
`entityType` |  `string` The entity type for the DDL statement, for example, TABLE, INDEX, VIEW, etc. This field can be empty string for some DDL statement, for example, for statement "ANALYZE", `entityType` = "".  
`entityNames[]` |  `string` The entity names being operated on the DDL statement. For example, 1. For statement "CREATE TABLE t1(...)", `entityNames` = ["t1"]. 2. For statement "GRANT ROLE r1, r2 ...", `entityNames` = ["r1", "r2"]. 3. For statement "ANALYZE", `entityNames` = [].  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
