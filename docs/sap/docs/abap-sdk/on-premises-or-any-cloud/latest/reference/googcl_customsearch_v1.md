---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_customsearch_v1/
title: Class /GOOG/CL_CUSTOMSEARCH_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:50.318339+00:00
---

# Class /GOOG/CL_CUSTOMSEARCH_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_customsearch_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CUSTOMSEARCH_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_customsearch_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_customsearch_v1)



## Class
    
    
    /GOOG/CL_CUSTOMSEARCH_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Custom Search API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Promotion` | PUBLIC  
`TY_002` | `Result` | PUBLIC  
`TY_003` | `Search` | PUBLIC  
`TY_004` | `Image` | PUBLIC  
`TY_005` | `Labels` | PUBLIC  
`TY_006` | `BodyLines` | PUBLIC  
`TY_007` | `Image` | PUBLIC  
`TY_008` | `NextPage` | PUBLIC  
`TY_009` | `PreviousPage` | PUBLIC  
`TY_010` | `Request` | PUBLIC  
`TY_011` | `Queries` | PUBLIC  
`TY_012` | `SearchInformation` | PUBLIC  
`TY_013` | `Spelling` | PUBLIC  
`TY_014` | `Url` | PUBLIC  
`TY_T_001` | `Promotion` | PUBLIC  
`TY_T_002` | `Result` | PUBLIC  
`TY_T_005` | `Labels` | PUBLIC  
`TY_T_006` | `BodyLines` | PUBLIC  
`TY_T_008` | `NextPage` | PUBLIC  
`TY_T_009` | `PreviousPage` | PUBLIC  
`TY_T_010` | `Request` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | customsearch:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://customsearch.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250302 | PUBLIC  
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
  
### LIST_CSE

  * Description: search.cse.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_C2COFF` | IMPORTING | `STRING` | c2coff  
`IV_Q_CR` | IMPORTING | `STRING` | cr  
`IV_Q_CX` | IMPORTING | `STRING` | cx  
`IV_Q_DATERESTRICT` | IMPORTING | `STRING` | dateRestrict  
`IV_Q_ENABLEALTERNATESEARCHHAND` | IMPORTING | `STRING` | enableAlternateSearchHandler  
`IV_Q_EXACTTERMS` | IMPORTING | `STRING` | exactTerms  
`IV_Q_EXCLUDETERMS` | IMPORTING | `STRING` | excludeTerms  
`IV_Q_FILETYPE` | IMPORTING | `STRING` | fileType  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_GL` | IMPORTING | `STRING` | gl  
`IV_Q_GOOGLEHOST` | IMPORTING | `STRING` | googlehost  
`IV_Q_HIGHRANGE` | IMPORTING | `STRING` | highRange  
`IV_Q_HL` | IMPORTING | `STRING` | hl  
`IV_Q_HQ` | IMPORTING | `STRING` | hq  
`IV_Q_IMGCOLORTYPE` | IMPORTING | `STRING` | imgColorType  
`IV_Q_IMGDOMINANTCOLOR` | IMPORTING | `STRING` | imgDominantColor  
`IV_Q_IMGSIZE` | IMPORTING | `STRING` | imgSize  
`IV_Q_IMGTYPE` | IMPORTING | `STRING` | imgType  
`IV_Q_LINKSITE` | IMPORTING | `STRING` | linkSite  
`IV_Q_LOWRANGE` | IMPORTING | `STRING` | lowRange  
`IV_Q_LR` | IMPORTING | `STRING` | lr  
`IV_Q_NUM` | IMPORTING | `STRING` | num  
`IV_Q_ORTERMS` | IMPORTING | `STRING` | orTerms  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_RELATEDSITE` | IMPORTING | `STRING` | relatedSite  
`IV_Q_RIGHTS` | IMPORTING | `STRING` | rights  
`IV_Q_SAFE` | IMPORTING | `STRING` | safe  
`IV_Q_SEARCHTYPE` | IMPORTING | `STRING` | searchType  
`IV_Q_SITESEARCH` | IMPORTING | `STRING` | siteSearch  
`IV_Q_SITESEARCHFILTER` | IMPORTING | `STRING` | siteSearchFilter  
`IV_Q_SNIPPETLENGTH` | IMPORTING | `STRING` | snippetLength  
`IV_Q_SORT` | IMPORTING | `STRING` | sort  
`IV_Q_START` | IMPORTING | `STRING` | start  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Search  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SITERESTRICT

  * Description: search.cse.siterestrict.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_C2COFF` | IMPORTING | `STRING` | c2coff  
`IV_Q_CR` | IMPORTING | `STRING` | cr  
`IV_Q_CX` | IMPORTING | `STRING` | cx  
`IV_Q_DATERESTRICT` | IMPORTING | `STRING` | dateRestrict  
`IV_Q_ENABLEALTERNATESEARCHHAND` | IMPORTING | `STRING` | enableAlternateSearchHandler  
`IV_Q_EXACTTERMS` | IMPORTING | `STRING` | exactTerms  
`IV_Q_EXCLUDETERMS` | IMPORTING | `STRING` | excludeTerms  
`IV_Q_FILETYPE` | IMPORTING | `STRING` | fileType  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_GL` | IMPORTING | `STRING` | gl  
`IV_Q_GOOGLEHOST` | IMPORTING | `STRING` | googlehost  
`IV_Q_HIGHRANGE` | IMPORTING | `STRING` | highRange  
`IV_Q_HL` | IMPORTING | `STRING` | hl  
`IV_Q_HQ` | IMPORTING | `STRING` | hq  
`IV_Q_IMGCOLORTYPE` | IMPORTING | `STRING` | imgColorType  
`IV_Q_IMGDOMINANTCOLOR` | IMPORTING | `STRING` | imgDominantColor  
`IV_Q_IMGSIZE` | IMPORTING | `STRING` | imgSize  
`IV_Q_IMGTYPE` | IMPORTING | `STRING` | imgType  
`IV_Q_LINKSITE` | IMPORTING | `STRING` | linkSite  
`IV_Q_LOWRANGE` | IMPORTING | `STRING` | lowRange  
`IV_Q_LR` | IMPORTING | `STRING` | lr  
`IV_Q_NUM` | IMPORTING | `STRING` | num  
`IV_Q_ORTERMS` | IMPORTING | `STRING` | orTerms  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_RELATEDSITE` | IMPORTING | `STRING` | relatedSite  
`IV_Q_RIGHTS` | IMPORTING | `STRING` | rights  
`IV_Q_SAFE` | IMPORTING | `STRING` | safe  
`IV_Q_SEARCHTYPE` | IMPORTING | `STRING` | searchType  
`IV_Q_SITESEARCH` | IMPORTING | `STRING` | siteSearch  
`IV_Q_SITESEARCHFILTER` | IMPORTING | `STRING` | siteSearchFilter  
`IV_Q_SNIPPETLENGTH` | IMPORTING | `STRING` | snippetLength  
`IV_Q_SORT` | IMPORTING | `STRING` | sort  
`IV_Q_START` | IMPORTING | `STRING` | start  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Search  
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
