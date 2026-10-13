---
url: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/Database/
title: Database \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:54.435802+00:00
---

# Database  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/Database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)



Send feedback 

#  Database Stay organized with collections  Save and categorize content based on your preferences. 

Message describing Database object.

JSON representation  
---  
      
    
    {
      "name": string,
      "charset": string,
      "collation": string,
      "characterType": string,
      "isTemplate": boolean,
      "databaseTemplate": string,
      "isTemplateDatabase": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource in the form of `projects/{project}/locations/{location}/clusters/{cluster}/databases/{database}`.  
`charset` |  `string` Optional. Immutable. Charset for the database. This field can contain any PostgreSQL supported charset name. Example values include "UTF8", "SQL_ASCII", etc.  
`collation` |  `string` Optional. Immutable. lc_collate for the database. String sort order. Example values include "C", "POSIX", etc.  
`characterType` |  `string` Optional. Immutable. lc_ctype for the database. Character classification (What is a letter? The upper-case equivalent?). Example values include "C", "POSIX", etc.  
`isTemplate  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Whether the database is a template database. Deprecated in favor of isTemplateDatabase.  
`databaseTemplate` |  `string` Input only. Immutable. Template of the database to be used for creating a new database.  
`isTemplateDatabase` |  `boolean` Optional. Whether the database is a template database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-05 UTC."],[],[]] 
