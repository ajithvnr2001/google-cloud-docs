---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_civicinfo_v2/
title: Class /GOOG/CL_CIVICINFO_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:34.122976+00:00
---

# Class /GOOG/CL_CIVICINFO_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_civicinfo_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CIVICINFO_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_civicinfo_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_civicinfo_v2)



## Class
    
    
    /GOOG/CL_CIVICINFO_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Civic Information API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AdministrationRegion` | PUBLIC  
`TY_002` | `AdministrativeBody` | PUBLIC  
`TY_003` | `Candidate` | PUBLIC  
`TY_004` | `Channel` | PUBLIC  
`TY_005` | `Contest` | PUBLIC  
`TY_006` | `DivisionSearchResponse` | PUBLIC  
`TY_007` | `DivisionSearchResult` | PUBLIC  
`TY_008` | `Election` | PUBLIC  
`TY_009` | `ElectionOfficial` | PUBLIC  
`TY_010` | `ElectionsQueryResponse` | PUBLIC  
`TY_011` | `ElectoralDistrict` | PUBLIC  
`TY_012` | `GeographicDivision` | PUBLIC  
`TY_013` | `Office` | PUBLIC  
`TY_014` | `Official` | PUBLIC  
`TY_015` | `PollingLocation` | PUBLIC  
`TY_016` | `Precinct` | PUBLIC  
`TY_017` | `RepresentativeInfoData` | PUBLIC  
`TY_018` | `RepresentativeInfoResponse` | PUBLIC  
`TY_019` | `SimpleAddressType` | PUBLIC  
`TY_020` | `Source` | PUBLIC  
`TY_021` | `VoterInfoResponse` | PUBLIC  
`TY_022` | `DivisionByAddressResponse` | PUBLIC  
`TY_T_001` | `AdministrationRegion` | PUBLIC  
`TY_T_003` | `Candidate` | PUBLIC  
`TY_T_004` | `Channel` | PUBLIC  
`TY_T_005` | `Contest` | PUBLIC  
`TY_T_007` | `DivisionSearchResult` | PUBLIC  
`TY_T_008` | `Election` | PUBLIC  
`TY_T_009` | `ElectionOfficial` | PUBLIC  
`TY_T_013` | `Office` | PUBLIC  
`TY_T_014` | `Official` | PUBLIC  
`TY_T_015` | `PollingLocation` | PUBLIC  
`TY_T_016` | `Precinct` | PUBLIC  
`TY_T_019` | `SimpleAddressType` | PUBLIC  
`TY_T_020` | `Source` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | civicinfo:v2 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://civicinfo.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241209 | PUBLIC  
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
  
### ELECTION_QUERY_ELECTIONS

  * Description: civicinfo.elections.electionQuery 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PRODUCTIONDATAONLY` | IMPORTING | `STRING` | productionDataOnly  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ElectionsQueryResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_DIVISION_BY_ADDRESS_D

  * Description: civicinfo.divisions.queryDivisionByAddress 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADDRESS` | IMPORTING | `STRING` | address  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | DivisionByAddressResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPRESENTATIVE_INFO_BY_ADDR

  * Description: civicinfo.representatives.representativeInfoByAddress 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADDRESS` | IMPORTING | `STRING` | address  
`IV_Q_INCLUDEOFFICES` | IMPORTING | `STRING` | includeOffices  
`IV_Q_LEVELS` | IMPORTING | `STRING` | levels  
`IV_Q_ROLES` | IMPORTING | `STRING` | roles  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | RepresentativeInfoResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPRESENTATIVE_INFO_BY_DIVI

  * Description: civicinfo.representatives.representativeInfoByDivision 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_LEVELS` | IMPORTING | `STRING` | levels  
`IV_Q_RECURSIVE` | IMPORTING | `STRING` | recursive  
`IV_Q_ROLES` | IMPORTING | `STRING` | roles  
`IV_P_OCD_ID` | IMPORTING | `STRING` | ocdId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | RepresentativeInfoData  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_DIVISIONS

  * Description: civicinfo.divisions.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | DivisionSearchResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### VOTER_INFO_QUERY_ELECTIONS

  * Description: civicinfo.elections.voterInfoQuery 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADDRESS` | IMPORTING | `STRING` | address  
`IV_Q_ELECTIONID` | IMPORTING | `STRING` | electionId  
`IV_Q_OFFICIALONLY` | IMPORTING | `STRING` | officialOnly  
`IV_Q_PRODUCTIONDATAONLY` | IMPORTING | `STRING` | productionDataOnly  
`IV_Q_RETURNALLAVAILABLEDATA` | IMPORTING | `STRING` | returnAllAvailableData  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | VoterInfoResponse  
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
