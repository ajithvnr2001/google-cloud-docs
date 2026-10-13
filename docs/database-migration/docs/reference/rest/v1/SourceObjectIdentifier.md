---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier/
title: SourceObjectIdentifier \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:43.242843+00:00
---

# SourceObjectIdentifier  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  SourceObjectIdentifier Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * MigrationJobObjectType



An identifier for the Migration Job Object.

JSON representation  
---  
      
    
    {
      "database": string,
      "schema": string,
      "table": string,
      "type": enum ([MigrationJobObjectType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier#MigrationJobObjectType))
    }  
  
Fields  
---  
`database` |  `string` Optional. The database name. This will be required only if the object uses a database name as part of its unique identifier.  
`schema` |  `string` Optional. The schema name. This will be required only if the object uses a schema name as part of its unique identifier.  
`table` |  `string` Optional. The table name. This will be required only if the object is a level below database or schema.  
`type` |  `enum (`[MigrationJobObjectType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier#MigrationJobObjectType)`)` Required. The type of the migration job object.  
  
## MigrationJobObjectType

The type of the migration job object.

Enums  
---  
`MIGRATION_JOB_OBJECT_TYPE_UNSPECIFIED` | The type of the migration job object is unknown.  
`DATABASE` | The migration job object is a database.  
`SCHEMA` | The migration job object is a schema.  
`TABLE` | The migration job object is a table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
