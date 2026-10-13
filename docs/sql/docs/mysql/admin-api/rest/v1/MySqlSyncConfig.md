---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/MySqlSyncConfig/
title: MySqlSyncConfig \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:01.376919+00:00
---

# MySqlSyncConfig  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/MySqlSyncConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  MySqlSyncConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SyncFlags
    * JSON representation



MySQL-specific external server sync settings.

JSON representation  
---  
      
    
    {
      "initialSyncFlags": [
        {
          object ([SyncFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/MySqlSyncConfig#SyncFlags))
        }
      ]
    }  
  
Fields  
---  
`initialSyncFlags[]` |  `object (`[SyncFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/MySqlSyncConfig#SyncFlags)`)` Flags to use for the initial dump.  
  
## SyncFlags

Initial sync flags for certain Cloud SQL APIs. Currently used for the MySQL external server initial dump.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` The name of the flag.  
`value` |  `string` The value of the flag. This field must be omitted if the flag doesn't take a value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
