---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig/
title: DatabaseManagementConfig \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:54.125513+00:00
---

# DatabaseManagementConfig  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  DatabaseManagementConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ManagementState
  * ManagementType



The configuration of the Database Management service.

JSON representation  
---  
      
    
    {
      "managementState": enum ([ManagementState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig#ManagementState)),
      "managementType": enum ([ManagementType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig#ManagementType))
    }  
  
Fields  
---  
`managementState` |  `enum (`[ManagementState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig#ManagementState)`)` Output only. The status of the Database Management service.  
`managementType` |  `enum (`[ManagementType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig#ManagementType)`)` Output only. The Database Management type.  
  
## ManagementState

The status of the Database Management service.

Enums  
---  
`MANAGEMENT_STATE_UNSPECIFIED` | The status is not specified.  
`ENABLING` | The Database Management service is enabling.  
`ENABLED` | The Database Management service is enabled.  
`DISABLING` | The Database Management service is disabling.  
`DISABLED` | The Database Management service is disabled.  
`UPDATING` | The Database Management service is updating.  
`FAILED_ENABLING` | The Database Management service failed to enable.  
`FAILED_DISABLING` | The Database Management service failed to disable.  
`FAILED_UPDATING` | The Database Management service failed to update.  
  
## ManagementType

The Database Management type.

Enums  
---  
`MANAGEMENT_TYPE_UNSPECIFIED` | The type is not specified.  
`BASIC` | Basic Database Management.  
`ADVANCED` | Advanced Database Management.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
