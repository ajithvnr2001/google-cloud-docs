---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets
title: REST Resource: projects.locations.autonomousDatabaseCharacterSets \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:36.907496+00:00
---

# REST Resource: projects.locations.autonomousDatabaseCharacterSets  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.autonomousDatabaseCharacterSets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AutonomousDatabaseCharacterSet
    * JSON representation
  * CharacterSetType
  * Methods



## Resource: AutonomousDatabaseCharacterSet

Details of the Autonomous Database character set resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/>

JSON representation  
---  
      
    
    {
      "name": string,
      "characterSetType": enum ([CharacterSetType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets#CharacterSetType)),
      "characterSet": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Autonomous Database Character Set resource in the following format: projects/{project}/locations/{region}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}  
`characterSetType` |  `enum (`[CharacterSetType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets#CharacterSetType)`)` Output only. The character set type for the Autonomous Database.  
`characterSet` |  `string` Output only. The character set name for the Autonomous Database which is the ID in the resource name.  
  
## CharacterSetType

The type of character set an Autonomous Database can have.

Enums  
---  
`CHARACTER_SET_TYPE_UNSPECIFIED` | Character set type is not specified.  
`DATABASE` | Character set type is set to database.  
`NATIONAL` | Character set type is set to national.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets/list)`

|  Lists Autonomous Database Character Sets in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
