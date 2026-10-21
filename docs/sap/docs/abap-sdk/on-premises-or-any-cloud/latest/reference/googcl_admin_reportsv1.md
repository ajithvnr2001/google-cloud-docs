---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_reportsv1/
title: Class /GOOG/CL_ADMIN_REPORTSV1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:59.017782+00:00
---

# Class /GOOG/CL_ADMIN_REPORTSV1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_reportsv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ADMIN_REPORTSV1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_admin_reportsv1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admin_reportsv1)



## Class
    
    
    /GOOG/CL_ADMIN_REPORTSV1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Admin SDK API reports_v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Activities` | PUBLIC  
`TY_002` | `Activity` | PUBLIC  
`TY_003` | `Channel` | PUBLIC  
`TY_004` | `NestedParameter` | PUBLIC  
`TY_005` | `UsageReport` | PUBLIC  
`TY_006` | `UsageReports` | PUBLIC  
`TY_007` | `Actor` | PUBLIC  
`TY_008` | `MessageValue` | PUBLIC  
`TY_009` | `MultiMessageValue` | PUBLIC  
`TY_010` | `Parameters` | PUBLIC  
`TY_011` | `Events` | PUBLIC  
`TY_012` | `Id` | PUBLIC  
`TY_013` | `Entity` | PUBLIC  
`TY_014` | `Parameters` | PUBLIC  
`TY_015` | `Data` | PUBLIC  
`TY_016` | `Warnings` | PUBLIC  
`TY_T_002` | `Activity` | PUBLIC  
`TY_T_004` | `NestedParameter` | PUBLIC  
`TY_T_005` | `UsageReport` | PUBLIC  
`TY_T_009` | `MultiMessageValue` | PUBLIC  
`TY_T_010` | `Parameters` | PUBLIC  
`TY_T_011` | `Events` | PUBLIC  
`TY_T_014` | `Parameters` | PUBLIC  
`TY_T_015` | `Data` | PUBLIC  
`TY_T_016` | `Warnings` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
`TY_T_ABAP_BOOL` | `` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250304 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://admin.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | admin:reports_v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
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
  
### GET_CUSTOMER_USAGE_REPORTS

  * Description: reports.customerUsageReports.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PARAMETERS` | IMPORTING | `STRING` | parameters  
`IV_P_DATE` | IMPORTING | `STRING` | date  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | UsageReports  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ENTITY_USAGE_REPORTS

  * Description: reports.entityUsageReports.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_FILTERS` | IMPORTING | `STRING` | filters  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PARAMETERS` | IMPORTING | `STRING` | parameters  
`IV_P_DATE` | IMPORTING | `STRING` | date  
`IV_P_ENTITY_KEY` | IMPORTING | `STRING` | entityKey  
`IV_P_ENTITY_TYPE` | IMPORTING | `STRING` | entityType  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | UsageReports  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_USER_USAGE_REPORT

  * Description: reports.userUsageReport.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_FILTERS` | IMPORTING | `STRING` | filters  
`IV_Q_GROUPIDFILTER` | IMPORTING | `STRING` | groupIdFilter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORGUNITID` | IMPORTING | `STRING` | orgUnitID  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PARAMETERS` | IMPORTING | `STRING` | parameters  
`IV_P_DATE` | IMPORTING | `STRING` | date  
`IV_P_USER_KEY` | IMPORTING | `STRING` | userKey  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | UsageReports  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ACTIVITIES

  * Description: reports.activities.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACTORIPADDRESS` | IMPORTING | `STRING` | actorIpAddress  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_ENDTIME` | IMPORTING | `STRING` | endTime  
`IV_Q_EVENTNAME` | IMPORTING | `STRING` | eventName  
`IV_Q_FILTERS` | IMPORTING | `STRING` | filters  
`IV_Q_GROUPIDFILTER` | IMPORTING | `STRING` | groupIdFilter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORGUNITID` | IMPORTING | `STRING` | orgUnitID  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTTIME` | IMPORTING | `STRING` | startTime  
`IV_P_APPLICATION_NAME` | IMPORTING | `STRING` | applicationName  
`IV_P_USER_KEY` | IMPORTING | `STRING` | userKey  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Activities  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_CHANNELS

  * Description: admin.channels.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_003` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_ACTIVITIES

  * Description: reports.activities.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACTORIPADDRESS` | IMPORTING | `STRING` | actorIpAddress  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_ENDTIME` | IMPORTING | `STRING` | endTime  
`IV_Q_EVENTNAME` | IMPORTING | `STRING` | eventName  
`IV_Q_FILTERS` | IMPORTING | `STRING` | filters  
`IV_Q_GROUPIDFILTER` | IMPORTING | `STRING` | groupIdFilter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORGUNITID` | IMPORTING | `STRING` | orgUnitID  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTTIME` | IMPORTING | `STRING` | startTime  
`IV_P_APPLICATION_NAME` | IMPORTING | `STRING` | applicationName  
`IV_P_USER_KEY` | IMPORTING | `STRING` | userKey  
`IS_INPUT` | IMPORTING | `TY_003` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Channel  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
