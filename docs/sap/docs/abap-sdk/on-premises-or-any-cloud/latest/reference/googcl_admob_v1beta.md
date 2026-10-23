---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admob_v1beta/
title: Class /GOOG/CL_ADMOB_V1BETA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:59.121886+00:00
---

# Class /GOOG/CL_ADMOB_V1BETA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admob_v1beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ADMOB_V1BETA Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_admob_v1beta)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_admob_v1beta)



## Class
    
    
    /GOOG/CL_ADMOB_V1BETA

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`AdMob API v1beta`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AdSource` | PUBLIC  
`TY_002` | `AdUnit` | PUBLIC  
`TY_003` | `AdUnitMapping` | PUBLIC  
`TY_004` | `AdUnitRewardSettings` | PUBLIC  
`TY_005` | `Adapter` | PUBLIC  
`TY_006` | `AdapterAdapterConfigMetadata` | PUBLIC  
`TY_007` | `App` | PUBLIC  
`TY_008` | `AppLinkedAppInfo` | PUBLIC  
`TY_009` | `AppManualAppInfo` | PUBLIC  
`TY_010` | `BatchCreateAdUnitMappingsRequest` | PUBLIC  
`TY_011` | `BatchCreateAdUnitMappingsResponse` | PUBLIC  
`TY_012` | `CampaignReportSpec` | PUBLIC  
`TY_013` | `CreateAdUnitMappingRequest` | PUBLIC  
`TY_014` | `Date` | PUBLIC  
`TY_015` | `DateRange` | PUBLIC  
`TY_016` | `GenerateCampaignReportRequest` | PUBLIC  
`TY_017` | `GenerateCampaignReportResponse` | PUBLIC  
`TY_018` | `GenerateMediationReportRequest` | PUBLIC  
`TY_019` | `GenerateMediationReportResponse` | PUBLIC  
`TY_020` | `GenerateNetworkReportRequest` | PUBLIC  
`TY_021` | `GenerateNetworkReportResponse` | PUBLIC  
`TY_022` | `ListAdSourcesResponse` | PUBLIC  
`TY_023` | `ListAdUnitMappingsResponse` | PUBLIC  
`TY_024` | `ListAdUnitsResponse` | PUBLIC  
`TY_025` | `ListAdaptersResponse` | PUBLIC  
`TY_026` | `ListAppsResponse` | PUBLIC  
`TY_027` | `ListMediationGroupsResponse` | PUBLIC  
`TY_028` | `ListPublisherAccountsResponse` | PUBLIC  
`TY_029` | `LocalizationSettings` | PUBLIC  
`TY_030` | `MediationAbExperiment` | PUBLIC  
`TY_031` | `MediationAbExperimentExperimentMediationLine` | PUBLIC  
`TY_032` | `MediationGroup` | PUBLIC  
`TY_033` | `MediationGroupMediationGroupLine` | PUBLIC  
`TY_034` | `MediationGroupTargeting` | PUBLIC  
`TY_035` | `MediationReportSpec` | PUBLIC  
`TY_036` | `MediationReportSpecDimensionFilter` | PUBLIC  
`TY_037` | `MediationReportSpecSortCondition` | PUBLIC  
`TY_038` | `NetworkReportSpec` | PUBLIC  
`TY_039` | `NetworkReportSpecDimensionFilter` | PUBLIC  
`TY_040` | `NetworkReportSpecSortCondition` | PUBLIC  
`TY_041` | `PublisherAccount` | PUBLIC  
`TY_042` | `ReportFooter` | PUBLIC  
`TY_043` | `ReportHeader` | PUBLIC  
`TY_044` | `ReportRow` | PUBLIC  
`TY_045` | `ReportRowDimensionValue` | PUBLIC  
`TY_046` | `ReportRowMetricValue` | PUBLIC  
`TY_047` | `ReportWarning` | PUBLIC  
`TY_048` | `StopMediationAbExperimentRequest` | PUBLIC  
`TY_049` | `StringList` | PUBLIC  
`TY_T_001` | `AdSource` | PUBLIC  
`TY_T_002` | `AdUnit` | PUBLIC  
`TY_T_003` | `AdUnitMapping` | PUBLIC  
`TY_T_005` | `Adapter` | PUBLIC  
`TY_T_006` | `AdapterAdapterConfigMetadata` | PUBLIC  
`TY_T_007` | `App` | PUBLIC  
`TY_T_013` | `CreateAdUnitMappingRequest` | PUBLIC  
`TY_T_031` | `MediationAbExperimentExperimentMediationLine` | PUBLIC  
`TY_T_032` | `MediationGroup` | PUBLIC  
`TY_T_036` | `MediationReportSpecDimensionFilter` | PUBLIC  
`TY_T_037` | `MediationReportSpecSortCondition` | PUBLIC  
`TY_T_039` | `NetworkReportSpecDimensionFilter` | PUBLIC  
`TY_T_040` | `NetworkReportSpecSortCondition` | PUBLIC  
`TY_T_041` | `PublisherAccount` | PUBLIC  
`TY_T_044` | `ReportRow` | PUBLIC  
`TY_T_047` | `ReportWarning` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | admob:v1beta | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://admob.googleapis.com | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
  
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
  
### BATCH_CREATE_AD_UNIT_MAPPIN

  * Description: admob.accounts.adUnitMappings.batchCreate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_010` | BatchCreateAdUnitMappingsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | BatchCreateAdUnitMappingsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_AD_UNITS

  * Description: admob.accounts.adUnits.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_002` | AdUnit  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AdUnit  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_AD_UNIT_MAPPINGS

  * Description: admob.accounts.adUnits.adUnitMappings.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_AD_UNITS_ID` | IMPORTING | `STRING` | adUnitsId  
`IS_INPUT` | IMPORTING | `TY_003` | AdUnitMapping  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | AdUnitMapping  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_APPS

  * Description: admob.accounts.apps.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_007` | App  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | App  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_MEDIATION_AB_EXPERIM

  * Description: accounts.mediationGroups.mediationAbExperiments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_MEDIATION_GROUPS_ID` | IMPORTING | `STRING` | mediationGroupsId  
`IS_INPUT` | IMPORTING | `TY_030` | MediationAbExperiment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | MediationAbExperiment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_MEDIATION_GROUPS

  * Description: admob.accounts.mediationGroups.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_032` | MediationGroup  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | MediationGroup  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_CAMPAIGN_REPORT

  * Description: admob.accounts.campaignReport.generate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_016` | GenerateCampaignReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | GenerateCampaignReportResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_MEDIATION_REPORT

  * Description: admob.accounts.mediationReport.generate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_018` | GenerateMediationReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | GenerateMediationReportResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_NETWORK_REPORT

  * Description: admob.accounts.networkReport.generate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_020` | GenerateNetworkReportRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | GenerateNetworkReportResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ACCOUNTS

  * Description: admob.accounts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | PublisherAccount  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ACCOUNTS

  * Description: admob.accounts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | ListPublisherAccountsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ADAPTERS

  * Description: admob.accounts.adSources.adapters.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_AD_SOURCES_ID` | IMPORTING | `STRING` | adSourcesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | ListAdaptersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AD_SOURCES

  * Description: admob.accounts.adSources.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | ListAdSourcesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AD_UNITS

  * Description: admob.accounts.adUnits.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | ListAdUnitsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AD_UNIT_MAPPINGS

  * Description: admob.accounts.adUnits.adUnitMappings.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_AD_UNITS_ID` | IMPORTING | `STRING` | adUnitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | ListAdUnitMappingsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_APPS

  * Description: admob.accounts.apps.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | ListAppsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MEDIATION_GROUPS

  * Description: admob.accounts.mediationGroups.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | ListMediationGroupsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_MEDIATION_GROUPS

  * Description: admob.accounts.mediationGroups.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_MEDIATION_GROUPS_ID` | IMPORTING | `STRING` | mediationGroupsId  
`IS_INPUT` | IMPORTING | `TY_032` | MediationGroup  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | MediationGroup  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_MEDIATION_AB_EXPERIMEN

  * Description: admob.accounts.mediationGroups.mediationAbExperiments.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_MEDIATION_GROUPS_ID` | IMPORTING | `STRING` | mediationGroupsId  
`IS_INPUT` | IMPORTING | `TY_048` | StopMediationAbExperimentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | MediationAbExperiment  
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
