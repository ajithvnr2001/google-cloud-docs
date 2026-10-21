---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_localservices_v1/
title: Class /GOOG/CL_LOCALSERVICES_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:25.641774+00:00
---

# Class /GOOG/CL_LOCALSERVICES_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_localservices_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_LOCALSERVICES_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_localservices_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_localservices_v1)



## Class
    
    
    /GOOG/CL_LOCALSERVICES_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Local Services API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleAdsHomeservicesLocalservicesV1AccountReport` | PUBLIC  
`TY_002` | `GoogleAdsHomeservicesLocalservicesV1AggregatorInfo` | PUBLIC  
`TY_003` | `GoogleAdsHomeservicesLocalservicesV1BookingLead` | PUBLIC  
`TY_004` | `GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport` | PUBLIC  
`TY_005` | `GoogleAdsHomeservicesLocalservicesV1MessageLead` | PUBLIC  
`TY_006` | `GoogleAdsHomeservicesLocalservicesV1PhoneLead` | PUBLIC  
`TY_007` | `GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResp` | PUBLIC  
`TY_008` | `GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReport` | PUBLIC  
`TY_009` | `GoogleTypeTimeZone` | PUBLIC  
`TY_T_001` | `GoogleAdsHomeservicesLocalservicesV1AccountReport` | PUBLIC  
`TY_T_004` | `GoogleAdsHomeservicesLocalservicesV1DetailedLeadReport` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241219 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://localservices.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | localservices:v1 | PUBLIC  
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
  
### SEARCH_ACCOUNT_REPORTS

  * Description: localservices.accountReports.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATEDAY` | IMPORTING | `STRING` | endDate.day  
`IV_Q_ENDDATEMONTH` | IMPORTING | `STRING` | endDate.month  
`IV_Q_ENDDATEYEAR` | IMPORTING | `STRING` | endDate.year  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`IV_Q_STARTDATEDAY` | IMPORTING | `STRING` | startDate.day  
`IV_Q_STARTDATEMONTH` | IMPORTING | `STRING` | startDate.month  
`IV_Q_STARTDATEYEAR` | IMPORTING | `STRING` | startDate.year  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResp  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_DETAILED_LEAD_REPORT

  * Description: localservices.detailedLeadReports.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENDDATEDAY` | IMPORTING | `STRING` | endDate.day  
`IV_Q_ENDDATEMONTH` | IMPORTING | `STRING` | endDate.month  
`IV_Q_ENDDATEYEAR` | IMPORTING | `STRING` | endDate.year  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`IV_Q_STARTDATEDAY` | IMPORTING | `STRING` | startDate.day  
`IV_Q_STARTDATEMONTH` | IMPORTING | `STRING` | startDate.month  
`IV_Q_STARTDATEYEAR` | IMPORTING | `STRING` | startDate.year  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReport  
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
