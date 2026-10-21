---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_busineprofilperfor_v1/
title: Class /GOOG/CL_BUSINEPROFILPERFOR_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:36.828267+00:00
---

# Class /GOOG/CL_BUSINEPROFILPERFOR_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_busineprofilperfor_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_BUSINEPROFILPERFOR_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_busineprofilperfor_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_busineprofilperfor_v1)



## Class
    
    
    /GOOG/CL_BUSINEPROFILPERFOR_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Business Profile Performance API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `DailyMetricTimeSeries` | PUBLIC  
`TY_002` | `DailySubEntityType` | PUBLIC  
`TY_003` | `Date` | PUBLIC  
`TY_004` | `DatedValue` | PUBLIC  
`TY_005` | `FetchMultiDailyMetricsTimeSeriesResponse` | PUBLIC  
`TY_006` | `GetDailyMetricsTimeSeriesResponse` | PUBLIC  
`TY_007` | `InsightsValue` | PUBLIC  
`TY_008` | `ListSearchKeywordImpressionsMonthlyResponse` | PUBLIC  
`TY_009` | `MultiDailyMetricTimeSeries` | PUBLIC  
`TY_010` | `SearchKeywordCount` | PUBLIC  
`TY_011` | `TimeOfDay` | PUBLIC  
`TY_012` | `TimeSeries` | PUBLIC  
`TY_T_001` | `DailyMetricTimeSeries` | PUBLIC  
`TY_T_004` | `DatedValue` | PUBLIC  
`TY_T_009` | `MultiDailyMetricTimeSeries` | PUBLIC  
`TY_T_010` | `SearchKeywordCount` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://businessprofileperformance.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | businessprofileperformance:v1 | PUBLIC  
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
  
### FETCH_MULTI_DAILY_METRICS_T

  * Description: locations.fetchMultiDailyMetricsTimeSeries 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DAILYMETRICS` | IMPORTING | `STRING` | dailyMetrics  
`IV_Q_DAILYRANGEENDDATEDAY` | IMPORTING | `STRING` | dailyRange.endDate.day  
`IV_Q_DAILYRANGEENDDATEMONTH` | IMPORTING | `STRING` | dailyRange.endDate.month  
`IV_Q_DAILYRANGEENDDATEYEAR` | IMPORTING | `STRING` | dailyRange.endDate.year  
`IV_Q_DAILYRANGESTARTDATEDAY` | IMPORTING | `STRING` | dailyRange.startDate.day  
`IV_Q_DAILYRANGESTARTDATEMONTH` | IMPORTING | `STRING` | dailyRange.startDate.month  
`IV_Q_DAILYRANGESTARTDATEYEAR` | IMPORTING | `STRING` | dailyRange.startDate.year  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | FetchMultiDailyMetricsTimeSeriesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DAILY_METRICS_TIME_SERI

  * Description: locations.getDailyMetricsTimeSeries 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DAILYMETRIC` | IMPORTING | `STRING` | dailyMetric  
`IV_Q_DAILYRANGEENDDATEDAY` | IMPORTING | `STRING` | dailyRange.endDate.day  
`IV_Q_DAILYRANGEENDDATEMONTH` | IMPORTING | `STRING` | dailyRange.endDate.month  
`IV_Q_DAILYRANGEENDDATEYEAR` | IMPORTING | `STRING` | dailyRange.endDate.year  
`IV_Q_DAILYRANGESTARTDATEDAY` | IMPORTING | `STRING` | dailyRange.startDate.day  
`IV_Q_DAILYRANGESTARTDATEMONTH` | IMPORTING | `STRING` | dailyRange.startDate.month  
`IV_Q_DAILYRANGESTARTDATEYEAR` | IMPORTING | `STRING` | dailyRange.startDate.year  
`IV_Q_DAILYSUBENTITYTYPEDAYOFW` | IMPORTING | `STRING` | dailySubEntityType.dayOfWeek  
`IV_Q_DAILYSUBENTITYTYPETIMEOF` | IMPORTING | `STRING` | dailySubEntityType.timeOfDay.hours  
`IV_Q_DAILYSUBENTITYTYPETIME01` | IMPORTING | `STRING` | dailySubEntityType.timeOfDay.minutes  
`IV_Q_DAILYSUBENTITYTYPETIME02` | IMPORTING | `STRING` | dailySubEntityType.timeOfDay.nanos  
`IV_Q_DAILYSUBENTITYTYPETIME03` | IMPORTING | `STRING` | dailySubEntityType.timeOfDay.seconds  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | GetDailyMetricsTimeSeriesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MONTHLY

  * Description: locations.searchkeywords.impressions.monthly.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MONTHLYRANGEENDMONTHDAY` | IMPORTING | `STRING` | monthlyRange.endMonth.day  
`IV_Q_MONTHLYRANGEENDMONTHMONTH` | IMPORTING | `STRING` | monthlyRange.endMonth.month  
`IV_Q_MONTHLYRANGEENDMONTHYEAR` | IMPORTING | `STRING` | monthlyRange.endMonth.year  
`IV_Q_MONTHLYRANGESTARTMONTHDAY` | IMPORTING | `STRING` | monthlyRange.startMonth.day  
`IV_Q_MONTHLYRANGESTARTMONTHMON` | IMPORTING | `STRING` | monthlyRange.startMonth.month  
`IV_Q_MONTHLYRANGESTARTMONTHYEA` | IMPORTING | `STRING` | monthlyRange.startMonth.year  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | ListSearchKeywordImpressionsMonthlyResponse  
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
