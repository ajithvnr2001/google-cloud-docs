---
url: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/CreateDatabaseRequest/
title: CreateDatabaseRequest \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:38.442856+00:00
---

# CreateDatabaseRequest  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/CreateDatabaseRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)



Send feedback 

#  CreateDatabaseRequest Stay organized with collections  Save and categorize content based on your preferences. 

Message for CreateDatabase request.

JSON representation  
---  
      
    
    {
      "parent": string,
      "databaseId": string,
      "database": {
        object ([Database](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/Database))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. Value for parent.  
`databaseId` |  `string` Required. ID of the requesting object.  
`database` |  `object (`[Database](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/Database)`)` Required. The resource being created.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-05 UTC."],[],[]] 
