---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_searchconsole_v1/
title: Class /GOOG/CL_SEARCHCONSOLE_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:44.709283+00:00
---

# Class /GOOG/CL_SEARCHCONSOLE_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_searchconsole_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SEARCHCONSOLE_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_searchconsole_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_searchconsole_v1)



## Class
    
    
    /GOOG/CL_SEARCHCONSOLE_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Search Console API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AmpInspectionResult` | PUBLIC  
`TY_002` | `AmpIssue` | PUBLIC  
`TY_003` | `ApiDataRow` | PUBLIC  
`TY_004` | `ApiDimensionFilter` | PUBLIC  
`TY_005` | `ApiDimensionFilterGroup` | PUBLIC  
`TY_006` | `BlockedResource` | PUBLIC  
`TY_007` | `DetectedItems` | PUBLIC  
`TY_008` | `Image` | PUBLIC  
`TY_009` | `IndexStatusInspectionResult` | PUBLIC  
`TY_010` | `InspectUrlIndexRequest` | PUBLIC  
`TY_011` | `InspectUrlIndexResponse` | PUBLIC  
`TY_012` | `Item` | PUBLIC  
`TY_013` | `MobileFriendlyIssue` | PUBLIC  
`TY_014` | `MobileUsabilityInspectionResult` | PUBLIC  
`TY_015` | `MobileUsabilityIssue` | PUBLIC  
`TY_016` | `ResourceIssue` | PUBLIC  
`TY_017` | `RichResultsInspectionResult` | PUBLIC  
`TY_018` | `RichResultsIssue` | PUBLIC  
`TY_019` | `RunMobileFriendlyTestRequest` | PUBLIC  
`TY_020` | `RunMobileFriendlyTestResponse` | PUBLIC  
`TY_021` | `SearchAnalyticsQueryRequest` | PUBLIC  
`TY_022` | `SearchAnalyticsQueryResponse` | PUBLIC  
`TY_023` | `SitemapsListResponse` | PUBLIC  
`TY_024` | `SitesListResponse` | PUBLIC  
`TY_025` | `TestStatus` | PUBLIC  
`TY_026` | `UrlInspectionResult` | PUBLIC  
`TY_027` | `WmxSite` | PUBLIC  
`TY_028` | `WmxSitemap` | PUBLIC  
`TY_029` | `WmxSitemapContent` | PUBLIC  
`TY_T_002` | `AmpIssue` | PUBLIC  
`TY_T_003` | `ApiDataRow` | PUBLIC  
`TY_T_004` | `ApiDimensionFilter` | PUBLIC  
`TY_T_005` | `ApiDimensionFilterGroup` | PUBLIC  
`TY_T_007` | `DetectedItems` | PUBLIC  
`TY_T_012` | `Item` | PUBLIC  
`TY_T_013` | `MobileFriendlyIssue` | PUBLIC  
`TY_T_015` | `MobileUsabilityIssue` | PUBLIC  
`TY_T_016` | `ResourceIssue` | PUBLIC  
`TY_T_018` | `RichResultsIssue` | PUBLIC  
`TY_T_027` | `WmxSite` | PUBLIC  
`TY_T_028` | `WmxSitemap` | PUBLIC  
`TY_T_029` | `WmxSitemapContent` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | searchconsole:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://searchconsole.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
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
  
### ADD_SITES

  * Description: webmasters.sites.add 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_SITEMAPS

  * Description: webmasters.sitemaps.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FEEDPATH` | IMPORTING | `STRING` | feedpath  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_SITES

  * Description: webmasters.sites.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SITEMAPS

  * Description: webmasters.sitemaps.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FEEDPATH` | IMPORTING | `STRING` | feedpath  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | WmxSitemap  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SITES

  * Description: webmasters.sites.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | WmxSite  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSPECT_INDEX

  * Description: searchconsole.urlInspection.index.inspect 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_010` | InspectUrlIndexRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | InspectUrlIndexResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SITEMAPS

  * Description: webmasters.sitemaps.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SITEMAPINDEX` | IMPORTING | `STRING` | sitemapIndex  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | SitemapsListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SITES

  * Description: webmasters.sites.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | SitesListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_SEARCHANALYTICS

  * Description: webmasters.searchanalytics.query 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`IS_INPUT` | IMPORTING | `TY_021` | SearchAnalyticsQueryRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | SearchAnalyticsQueryResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RUN_MOBILE_FRIENDLY_TEST

  * Description: searchconsole.urlTestingTools.mobileFriendlyTest.run 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_019` | RunMobileFriendlyTestRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | RunMobileFriendlyTestResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SUBMIT_SITEMAPS

  * Description: webmasters.sitemaps.submit 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FEEDPATH` | IMPORTING | `STRING` | feedpath  
`IV_P_SITE_URL` | IMPORTING | `STRING` | siteUrl  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
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
