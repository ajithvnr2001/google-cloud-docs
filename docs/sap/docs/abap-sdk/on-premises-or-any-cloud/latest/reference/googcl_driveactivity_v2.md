---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_driveactivity_v2/
title: Class /GOOG/CL_DRIVEACTIVITY_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:24.454329+00:00
---

# Class /GOOG/CL_DRIVEACTIVITY_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_driveactivity_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DRIVEACTIVITY_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_driveactivity_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_driveactivity_v2)



## Class
    
    
    /GOOG/CL_DRIVEACTIVITY_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Drive Activity API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Action` | PUBLIC  
`TY_002` | `ActionDetail` | PUBLIC  
`TY_003` | `Actor` | PUBLIC  
`TY_007` | `ApplicationReference` | PUBLIC  
`TY_008` | `AppliedLabelChange` | PUBLIC  
`TY_009` | `AppliedLabelChangeDetail` | PUBLIC  
`TY_010` | `Assignment` | PUBLIC  
`TY_011` | `Comment` | PUBLIC  
`TY_012` | `ConsolidationStrategy` | PUBLIC  
`TY_013` | `Copy` | PUBLIC  
`TY_014` | `Create` | PUBLIC  
`TY_015` | `DataLeakPreventionChange` | PUBLIC  
`TY_016` | `Date` | PUBLIC  
`TY_017` | `Delete` | PUBLIC  
`TY_019` | `Domain` | PUBLIC  
`TY_020` | `Drive` | PUBLIC  
`TY_021` | `DriveActivity` | PUBLIC  
`TY_023` | `DriveFolder` | PUBLIC  
`TY_024` | `DriveItem` | PUBLIC  
`TY_025` | `DriveItemReference` | PUBLIC  
`TY_026` | `DriveReference` | PUBLIC  
`TY_028` | `FieldValue` | PUBLIC  
`TY_029` | `FieldValueChange` | PUBLIC  
`TY_031` | `FileComment` | PUBLIC  
`TY_032` | `Folder` | PUBLIC  
`TY_033` | `Group` | PUBLIC  
`TY_034` | `Impersonation` | PUBLIC  
`TY_035` | `Integer` | PUBLIC  
`TY_036` | `KnownUser` | PUBLIC  
`TY_038` | `Move` | PUBLIC  
`TY_041` | `Owner` | PUBLIC  
`TY_042` | `Permission` | PUBLIC  
`TY_043` | `PermissionChange` | PUBLIC  
`TY_044` | `Post` | PUBLIC  
`TY_045` | `QueryDriveActivityRequest` | PUBLIC  
`TY_046` | `QueryDriveActivityResponse` | PUBLIC  
`TY_047` | `Rename` | PUBLIC  
`TY_048` | `Restore` | PUBLIC  
`TY_049` | `RestrictionChange` | PUBLIC  
`TY_050` | `Selection` | PUBLIC  
`TY_051` | `SelectionList` | PUBLIC  
`TY_052` | `SettingsChange` | PUBLIC  
`TY_053` | `SingleUser` | PUBLIC  
`TY_054` | `Suggestion` | PUBLIC  
`TY_055` | `SystemEvent` | PUBLIC  
`TY_056` | `Target` | PUBLIC  
`TY_057` | `TargetReference` | PUBLIC  
`TY_058` | `TeamDrive` | PUBLIC  
`TY_059` | `TeamDriveReference` | PUBLIC  
`TY_060` | `Text` | PUBLIC  
`TY_061` | `TextList` | PUBLIC  
`TY_062` | `TimeRange` | PUBLIC  
`TY_065` | `User` | PUBLIC  
`TY_066` | `UserList` | PUBLIC  
`TY_T_001` | `Action` | PUBLIC  
`TY_T_003` | `Actor` | PUBLIC  
`TY_T_009` | `AppliedLabelChangeDetail` | PUBLIC  
`TY_T_021` | `DriveActivity` | PUBLIC  
`TY_T_029` | `FieldValueChange` | PUBLIC  
`TY_T_042` | `Permission` | PUBLIC  
`TY_T_049` | `RestrictionChange` | PUBLIC  
`TY_T_050` | `Selection` | PUBLIC  
`TY_T_053` | `SingleUser` | PUBLIC  
`TY_T_056` | `Target` | PUBLIC  
`TY_T_057` | `TargetReference` | PUBLIC  
`TY_T_060` | `Text` | PUBLIC  
`TY_T_065` | `User` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | driveactivity:v2 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://driveactivity.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250304 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#api_method). 

### CONSTRUCTOR

  * Description: Constructor 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_KEY_NAME` | IMPORTING | `/GOOG/KEYNAME` | Google Cloud Key Name  
`IV_LOG_OBJ` | IMPORTING | `BALOBJ_D` | Application log: Object name (Application code)  
`IV_LOG_SUBOBJ` | IMPORTING | `BALSUBOBJ` | Application Log: Subobject  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_ACTIVITY

  * Description: driveactivity.activity.query 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_045` | QueryDriveActivityRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | QueryDriveActivityResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
