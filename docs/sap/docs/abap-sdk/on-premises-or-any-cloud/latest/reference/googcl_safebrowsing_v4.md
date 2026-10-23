---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_safebrowsing_v4/
title: Class /GOOG/CL_SAFEBROWSING_V4 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:45.561561+00:00
---

# Class /GOOG/CL_SAFEBROWSING_V4  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_safebrowsing_v4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SAFEBROWSING_V4 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_safebrowsing_v4)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_safebrowsing_v4)



## Class
    
    
    /GOOG/CL_SAFEBROWSING_V4

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Safe Browsing API v4`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_002` | `GoogleSecuritySafebrowsingV4Checksum` | PUBLIC  
`TY_003` | `GoogleSecuritySafebrowsingV4ClientInfo` | PUBLIC  
`TY_004` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequest` | PUBLIC  
`TY_005` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestLis` | PUBLIC  
`TY_006` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestLis` | PUBLIC  
`TY_007` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponse` | PUBLIC  
`TY_008` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseLi` | PUBLIC  
`TY_009` | `GoogleSecuritySafebrowsingV4FindFullHashesRequest` | PUBLIC  
`TY_010` | `GoogleSecuritySafebrowsingV4FindFullHashesResponse` | PUBLIC  
`TY_011` | `GoogleSecuritySafebrowsingV4FindThreatMatchesRequest` | PUBLIC  
`TY_012` | `GoogleSecuritySafebrowsingV4FindThreatMatchesResponse` | PUBLIC  
`TY_013` | `GoogleSecuritySafebrowsingV4ListThreatListsResponse` | PUBLIC  
`TY_014` | `GoogleSecuritySafebrowsingV4RawHashes` | PUBLIC  
`TY_015` | `GoogleSecuritySafebrowsingV4RawIndices` | PUBLIC  
`TY_016` | `GoogleSecuritySafebrowsingV4RiceDeltaEncoding` | PUBLIC  
`TY_017` | `GoogleSecuritySafebrowsingV4ThreatEntry` | PUBLIC  
`TY_018` | `GoogleSecuritySafebrowsingV4ThreatEntryMetadata` | PUBLIC  
`TY_019` | `GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntry` | PUBLIC  
`TY_020` | `GoogleSecuritySafebrowsingV4ThreatEntrySet` | PUBLIC  
`TY_021` | `GoogleSecuritySafebrowsingV4ThreatHit` | PUBLIC  
`TY_022` | `GoogleSecuritySafebrowsingV4ThreatHitThreatSource` | PUBLIC  
`TY_023` | `GoogleSecuritySafebrowsingV4ThreatHitUserInfo` | PUBLIC  
`TY_024` | `GoogleSecuritySafebrowsingV4ThreatInfo` | PUBLIC  
`TY_025` | `GoogleSecuritySafebrowsingV4ThreatListDescriptor` | PUBLIC  
`TY_026` | `GoogleSecuritySafebrowsingV4ThreatMatch` | PUBLIC  
`TY_T_005` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestLis` | PUBLIC  
`TY_T_008` | `GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseLi` | PUBLIC  
`TY_T_017` | `GoogleSecuritySafebrowsingV4ThreatEntry` | PUBLIC  
`TY_T_019` | `GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntry` | PUBLIC  
`TY_T_020` | `GoogleSecuritySafebrowsingV4ThreatEntrySet` | PUBLIC  
`TY_T_022` | `GoogleSecuritySafebrowsingV4ThreatHitThreatSource` | PUBLIC  
`TY_T_025` | `GoogleSecuritySafebrowsingV4ThreatListDescriptor` | PUBLIC  
`TY_T_026` | `GoogleSecuritySafebrowsingV4ThreatMatch` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250302 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://safebrowsing.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | safebrowsing:v4 | PUBLIC  
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
  
### CREATE_THREAT_HITS

  * Description: safebrowsing.threatHits.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_021` | GoogleSecuritySafebrowsingV4ThreatHit  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### FETCH_THREAT_LIST_UPDATES

  * Description: safebrowsing.threatListUpdates.fetch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_004` | GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### FIND_FULL_HASHES

  * Description: safebrowsing.fullHashes.find 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_009` | GoogleSecuritySafebrowsingV4FindFullHashesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | GoogleSecuritySafebrowsingV4FindFullHashesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### FIND_THREAT_MATCHES

  * Description: safebrowsing.threatMatches.find 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_011` | GoogleSecuritySafebrowsingV4FindThreatMatchesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GoogleSecuritySafebrowsingV4FindThreatMatchesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ENCODED_FULL_HASHES

  * Description: safebrowsing.encodedFullHashes.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CLIENTID` | IMPORTING | `STRING` | clientId  
`IV_Q_CLIENTVERSION` | IMPORTING | `STRING` | clientVersion  
`IV_P_ENCODED_REQUEST` | IMPORTING | `STRING` | encodedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | GoogleSecuritySafebrowsingV4FindFullHashesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ENCODED_UPDATES

  * Description: safebrowsing.encodedUpdates.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CLIENTID` | IMPORTING | `STRING` | clientId  
`IV_Q_CLIENTVERSION` | IMPORTING | `STRING` | clientVersion  
`IV_P_ENCODED_REQUEST` | IMPORTING | `STRING` | encodedRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_THREAT_LISTS

  * Description: safebrowsing.threatLists.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | GoogleSecuritySafebrowsingV4ListThreatListsResponse  
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
