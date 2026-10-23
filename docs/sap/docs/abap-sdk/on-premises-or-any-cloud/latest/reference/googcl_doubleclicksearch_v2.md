---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_doubleclicksearch_v2/
title: Class /GOOG/CL_DOUBLECLICKSEARCH_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:24.362284+00:00
---

# Class /GOOG/CL_DOUBLECLICKSEARCH_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_doubleclicksearch_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DOUBLECLICKSEARCH_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_doubleclicksearch_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_doubleclicksearch_v2)



## Class
    
    
    /GOOG/CL_DOUBLECLICKSEARCH_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Search Ads 360 API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Availability` | PUBLIC  
`TY_002` | `Conversion` | PUBLIC  
`TY_003` | `ConversionList` | PUBLIC  
`TY_004` | `CustomDimension` | PUBLIC  
`TY_005` | `CustomMetric` | PUBLIC  
`TY_007` | `Report` | PUBLIC  
`TY_008` | `ReportApiColumnSpec` | PUBLIC  
`TY_009` | `ReportRequest` | PUBLIC  
`TY_011` | `SavedColumn` | PUBLIC  
`TY_012` | `SavedColumnList` | PUBLIC  
`TY_013` | `UpdateAvailabilityRequest` | PUBLIC  
`TY_014` | `UpdateAvailabilityResponse` | PUBLIC  
`TY_019` | `Files` | PUBLIC  
`TY_020` | `Filters` | PUBLIC  
`TY_021` | `OrderBy` | PUBLIC  
`TY_022` | `ReportScope` | PUBLIC  
`TY_023` | `TimeRange` | PUBLIC  
`TY_T_001` | `Availability` | PUBLIC  
`TY_T_002` | `Conversion` | PUBLIC  
`TY_T_004` | `CustomDimension` | PUBLIC  
`TY_T_005` | `CustomMetric` | PUBLIC  
`TY_T_008` | `ReportApiColumnSpec` | PUBLIC  
`TY_T_011` | `SavedColumn` | PUBLIC  
`TY_T_019` | `Files` | PUBLIC  
`TY_T_020` | `Filters` | PUBLIC  
`TY_T_021` | `OrderBy` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250225 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://doubleclicksearch.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | doubleclicksearch:v2 | PUBLIC  
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
  
### GENERATE_REPORTS

  * Description: doubleclicksearch.reports.generate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_009` | ReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Report  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BY_CUSTOMER_ID_CONVERSI

  * Description: doubleclicksearch.conversion.getByCustomerId 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADGROUPID` | IMPORTING | `STRING` | adGroupId  
`IV_Q_ADID` | IMPORTING | `STRING` | adId  
`IV_Q_ADVERTISERID` | IMPORTING | `STRING` | advertiserId  
`IV_Q_AGENCYID` | IMPORTING | `STRING` | agencyId  
`IV_Q_CAMPAIGNID` | IMPORTING | `STRING` | campaignId  
`IV_Q_CRITERIONID` | IMPORTING | `STRING` | criterionId  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_ENGINEACCOUNTID` | IMPORTING | `STRING` | engineAccountId  
`IV_Q_ROWCOUNT` | IMPORTING | `STRING` | rowCount  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STARTROW` | IMPORTING | `STRING` | startRow  
`IV_P_CUSTOMER_ID` | IMPORTING | `STRING` | customerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ConversionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONVERSION

  * Description: doubleclicksearch.conversion.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADGROUPID` | IMPORTING | `STRING` | adGroupId  
`IV_Q_ADID` | IMPORTING | `STRING` | adId  
`IV_Q_CAMPAIGNID` | IMPORTING | `STRING` | campaignId  
`IV_Q_CRITERIONID` | IMPORTING | `STRING` | criterionId  
`IV_Q_CUSTOMERID` | IMPORTING | `STRING` | customerId  
`IV_Q_ENDDATE` | IMPORTING | `STRING` | endDate  
`IV_Q_ROWCOUNT` | IMPORTING | `STRING` | rowCount  
`IV_Q_STARTDATE` | IMPORTING | `STRING` | startDate  
`IV_Q_STARTROW` | IMPORTING | `STRING` | startRow  
`IV_P_ADVERTISER_ID` | IMPORTING | `STRING` | advertiserId  
`IV_P_AGENCY_ID` | IMPORTING | `STRING` | agencyId  
`IV_P_ENGINE_ACCOUNT_ID` | IMPORTING | `STRING` | engineAccountId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ConversionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FILE_REPORTS

  * Description: doubleclicksearch.reports.getFile 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_REPORT_FRAGMENT` | IMPORTING | `STRING` | reportFragment  
`IV_P_REPORT_ID` | IMPORTING | `STRING` | reportId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ID_MAPPING_FILE_REPORTS

  * Description: doubleclicksearch.reports.getIdMappingFile 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ADVERTISER_ID` | IMPORTING | `STRING` | advertiserId  
`IV_P_AGENCY_ID` | IMPORTING | `STRING` | agencyId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_REPORTS

  * Description: doubleclicksearch.reports.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_REPORT_ID` | IMPORTING | `STRING` | reportId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Report  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_CONVERSION

  * Description: doubleclicksearch.conversion.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_003` | ConversionList  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ConversionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SAVED_COLUMNS

  * Description: doubleclicksearch.savedColumns.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ADVERTISER_ID` | IMPORTING | `STRING` | advertiserId  
`IV_P_AGENCY_ID` | IMPORTING | `STRING` | agencyId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | SavedColumnList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REQUEST_REPORTS

  * Description: doubleclicksearch.reports.request 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_009` | ReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Report  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_AVAILABILITY_CONVERS

  * Description: doubleclicksearch.conversion.updateAvailability 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_013` | UpdateAvailabilityRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | UpdateAvailabilityResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONVERSION

  * Description: doubleclicksearch.conversion.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_003` | ConversionList  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ConversionList  
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
