---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions
title: REST Resource: projects.locations.dbVersions \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:44.249923+00:00
---

# REST Resource: projects.locations.dbVersions  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dbVersions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbVersion
    * JSON representation
  * DbVersionProperties
    * JSON representation
  * Methods



## Resource: DbVersion

A valid Oracle Database version.

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([DbVersionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions#DbVersionProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the DbVersion resource in the following format: projects/{project}/locations/{region}/dbVersions/{dbVersion}  
`properties` |  `object (`[DbVersionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions#DbVersionProperties)`)` Output only. The properties of the DbVersion.  
  
## DbVersionProperties

The properties of a DbVersion.

JSON representation  
---  
      
    
    {
      "version": string,
      "isLatestForMajorVersion": boolean,
      "supportsPdb": boolean,
      "isPreviewDbVersion": boolean,
      "isUpgradeSupported": boolean
    }  
  
Fields  
---  
`version` |  `string` Output only. A valid Oracle Database version.  
`isLatestForMajorVersion` |  `boolean` Output only. True if this version of the Oracle Database software is the latest version for a release.  
`supportsPdb` |  `boolean` Output only. True if this version of the Oracle Database software supports pluggable databases.  
`isPreviewDbVersion` |  `boolean` Output only. True if this version of the Oracle Database software is the preview version.  
`isUpgradeSupported` |  `boolean` Output only. True if this version of the Oracle Database software is supported for Upgrade.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions/list)`

|  List DbVersions for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
