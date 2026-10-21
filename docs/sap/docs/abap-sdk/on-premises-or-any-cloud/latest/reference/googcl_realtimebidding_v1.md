---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_realtimebidding_v1/
title: Class /GOOG/CL_REALTIMEBIDDING_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:46.639728+00:00
---

# Class /GOOG/CL_REALTIMEBIDDING_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_realtimebidding_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_REALTIMEBIDDING_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_realtimebidding_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_realtimebidding_v1)



## Class
    
    
    /GOOG/CL_REALTIMEBIDDING_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Real-time Bidding API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_002` | `AdTechnologyProviders` | PUBLIC  
`TY_003` | `AddTargetedAppsRequest` | PUBLIC  
`TY_004` | `AddTargetedPublishersRequest` | PUBLIC  
`TY_005` | `AddTargetedSitesRequest` | PUBLIC  
`TY_006` | `AdvertiserAndBrand` | PUBLIC  
`TY_007` | `AppTargeting` | PUBLIC  
`TY_008` | `BatchApprovePublisherConnectionsRequest` | PUBLIC  
`TY_009` | `BatchApprovePublisherConnectionsResponse` | PUBLIC  
`TY_010` | `BatchRejectPublisherConnectionsRequest` | PUBLIC  
`TY_011` | `BatchRejectPublisherConnectionsResponse` | PUBLIC  
`TY_012` | `Bidder` | PUBLIC  
`TY_013` | `Buyer` | PUBLIC  
`TY_015` | `Creative` | PUBLIC  
`TY_016` | `CreativeDimensions` | PUBLIC  
`TY_017` | `CreativeServingDecision` | PUBLIC  
`TY_018` | `Date` | PUBLIC  
`TY_019` | `DestinationNotCrawlableEvidence` | PUBLIC  
`TY_020` | `DestinationNotWorkingEvidence` | PUBLIC  
`TY_021` | `DestinationUrlEvidence` | PUBLIC  
`TY_022` | `DomainCallEvidence` | PUBLIC  
`TY_023` | `DomainCalls` | PUBLIC  
`TY_024` | `DownloadSizeEvidence` | PUBLIC  
`TY_026` | `Endpoint` | PUBLIC  
`TY_027` | `GetRemarketingTagResponse` | PUBLIC  
`TY_028` | `HtmlContent` | PUBLIC  
`TY_029` | `HttpCallEvidence` | PUBLIC  
`TY_030` | `HttpCookieEvidence` | PUBLIC  
`TY_031` | `Image` | PUBLIC  
`TY_032` | `ListBiddersResponse` | PUBLIC  
`TY_033` | `ListBuyersResponse` | PUBLIC  
`TY_034` | `ListCreativesResponse` | PUBLIC  
`TY_035` | `ListEndpointsResponse` | PUBLIC  
`TY_036` | `ListPretargetingConfigsResponse` | PUBLIC  
`TY_037` | `ListPublisherConnectionsResponse` | PUBLIC  
`TY_038` | `ListUserListsResponse` | PUBLIC  
`TY_039` | `MediaFile` | PUBLIC  
`TY_040` | `NativeContent` | PUBLIC  
`TY_041` | `NumericTargetingDimension` | PUBLIC  
`TY_043` | `PolicyCompliance` | PUBLIC  
`TY_044` | `PolicyTopicEntry` | PUBLIC  
`TY_045` | `PolicyTopicEvidence` | PUBLIC  
`TY_046` | `PretargetingConfig` | PUBLIC  
`TY_047` | `PublisherConnection` | PUBLIC  
`TY_048` | `RemoveTargetedAppsRequest` | PUBLIC  
`TY_049` | `RemoveTargetedPublishersRequest` | PUBLIC  
`TY_050` | `RemoveTargetedSitesRequest` | PUBLIC  
`TY_051` | `StringTargetingDimension` | PUBLIC  
`TY_053` | `UrlDownloadSize` | PUBLIC  
`TY_054` | `UrlRestriction` | PUBLIC  
`TY_055` | `UserList` | PUBLIC  
`TY_056` | `VideoContent` | PUBLIC  
`TY_057` | `VideoMetadata` | PUBLIC  
`TY_059` | `WatchCreativesResponse` | PUBLIC  
`TY_T_006` | `AdvertiserAndBrand` | PUBLIC  
`TY_T_012` | `Bidder` | PUBLIC  
`TY_T_013` | `Buyer` | PUBLIC  
`TY_T_015` | `Creative` | PUBLIC  
`TY_T_016` | `CreativeDimensions` | PUBLIC  
`TY_T_023` | `DomainCalls` | PUBLIC  
`TY_T_026` | `Endpoint` | PUBLIC  
`TY_T_039` | `MediaFile` | PUBLIC  
`TY_T_044` | `PolicyTopicEntry` | PUBLIC  
`TY_T_045` | `PolicyTopicEvidence` | PUBLIC  
`TY_T_046` | `PretargetingConfig` | PUBLIC  
`TY_T_047` | `PublisherConnection` | PUBLIC  
`TY_T_053` | `UrlDownloadSize` | PUBLIC  
`TY_T_055` | `UserList` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250306 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://realtimebidding.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | realtimebidding:v1 | PUBLIC  
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
  
### ACTIVATE_PRETARGETING_CONFI

  * Description: realtimebidding.bidders.pretargetingConfigs.activate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_TARGETED_APPS_PRETARGET

  * Description: realtimebidding.bidders.pretargetingConfigs.addTargetedApps 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_003` | AddTargetedAppsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_TARGETED_PUBLISHERS_PRE

  * Description: bidders.pretargetingConfigs.addTargetedPublishers 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_004` | AddTargetedPublishersRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_TARGETED_SITES_PRETARGE

  * Description: bidders.pretargetingConfigs.addTargetedSites 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_005` | AddTargetedSitesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_APPROVE_PUBLISHER_CON

  * Description: realtimebidding.bidders.publisherConnections.batchApprove 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IS_INPUT` | IMPORTING | `TY_008` | BatchApprovePublisherConnectionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | BatchApprovePublisherConnectionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_REJECT_PUBLISHER_CONN

  * Description: realtimebidding.bidders.publisherConnections.batchReject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IS_INPUT` | IMPORTING | `TY_010` | BatchRejectPublisherConnectionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | BatchRejectPublisherConnectionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CLOSE_USER_LISTS

  * Description: realtimebidding.buyers.userLists.close 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_USER_LISTS_ID` | IMPORTING | `STRING` | userListsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_055` | UserList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CREATIVES

  * Description: realtimebidding.buyers.creatives.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IS_INPUT` | IMPORTING | `TY_015` | Creative  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | Creative  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PRETARGETING_CONFIGS

  * Description: realtimebidding.bidders.pretargetingConfigs.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IS_INPUT` | IMPORTING | `TY_046` | PretargetingConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_USER_LISTS

  * Description: realtimebidding.buyers.userLists.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IS_INPUT` | IMPORTING | `TY_055` | UserList  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_055` | UserList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PRETARGETING_CONFIGS

  * Description: realtimebidding.bidders.pretargetingConfigs.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BIDDERS

  * Description: realtimebidding.bidders.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Bidder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_BUYERS

  * Description: realtimebidding.buyers.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Buyer  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CREATIVES

  * Description: realtimebidding.buyers.creatives.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CREATIVES_ID` | IMPORTING | `STRING` | creativesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | Creative  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ENDPOINTS

  * Description: realtimebidding.bidders.endpoints.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_ENDPOINTS_ID` | IMPORTING | `STRING` | endpointsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Endpoint  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PRETARGETING_CONFIGS

  * Description: realtimebidding.bidders.pretargetingConfigs.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PUBLISHER_CONNECTIONS

  * Description: realtimebidding.bidders.publisherConnections.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PUBLISHER_CONNECTIONS_ID` | IMPORTING | `STRING` | publisherConnectionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_047` | PublisherConnection  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_REMARKETING_TAG_BUYERS

  * Description: realtimebidding.buyers.getRemarketingTag 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | GetRemarketingTagResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_REMARKETING_TAG_USER_LI

  * Description: realtimebidding.buyers.userLists.getRemarketingTag 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_USER_LISTS_ID` | IMPORTING | `STRING` | userListsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | GetRemarketingTagResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_USER_LISTS

  * Description: realtimebidding.buyers.userLists.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_USER_LISTS_ID` | IMPORTING | `STRING` | userListsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_055` | UserList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BIDDERS

  * Description: realtimebidding.bidders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | ListBiddersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BUYERS

  * Description: realtimebidding.buyers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | ListBuyersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CREATIVES

  * Description: realtimebidding.bidders.creatives.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | ListCreativesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CREATIVES1

  * Description: realtimebidding.buyers.creatives.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_VIEW` | IMPORTING | `STRING` | view  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | ListCreativesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ENDPOINTS

  * Description: realtimebidding.bidders.endpoints.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | ListEndpointsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PRETARGETING_CONFIGS

  * Description: realtimebidding.bidders.pretargetingConfigs.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | ListPretargetingConfigsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PUBLISHER_CONNECTIONS

  * Description: realtimebidding.bidders.publisherConnections.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_037` | ListPublisherConnectionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_USER_LISTS

  * Description: realtimebidding.buyers.userLists.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_038` | ListUserListsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### OPEN_USER_LISTS

  * Description: realtimebidding.buyers.userLists.open 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_USER_LISTS_ID` | IMPORTING | `STRING` | userListsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_055` | UserList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CREATIVES

  * Description: realtimebidding.buyers.creatives.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CREATIVES_ID` | IMPORTING | `STRING` | creativesId  
`IS_INPUT` | IMPORTING | `TY_015` | Creative  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | Creative  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_ENDPOINTS

  * Description: realtimebidding.bidders.endpoints.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_ENDPOINTS_ID` | IMPORTING | `STRING` | endpointsId  
`IS_INPUT` | IMPORTING | `TY_026` | Endpoint  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Endpoint  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PRETARGETING_CONFIGS

  * Description: realtimebidding.bidders.pretargetingConfigs.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_046` | PretargetingConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REMOVE_TARGETED_APPS_PRETAR

  * Description: bidders.pretargetingConfigs.removeTargetedApps 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_048` | RemoveTargetedAppsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REMOVE_TARGETED_PUBLISHERS

  * Description: bidders.pretargetingConfigs.removeTargetedPublishers 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_049` | RemoveTargetedPublishersRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REMOVE_TARGETED_SITES_PRETA

  * Description: bidders.pretargetingConfigs.removeTargetedSites 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `TY_050` | RemoveTargetedSitesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SUSPEND_PRETARGETING_CONFIG

  * Description: realtimebidding.bidders.pretargetingConfigs.suspend 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IV_P_PRETARGETING_CONFIGS_ID` | IMPORTING | `STRING` | pretargetingConfigsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | PretargetingConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_USER_LISTS

  * Description: realtimebidding.buyers.userLists.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_USER_LISTS_ID` | IMPORTING | `STRING` | userListsId  
`IS_INPUT` | IMPORTING | `TY_055` | UserList  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_055` | UserList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_CREATIVES

  * Description: realtimebidding.bidders.creatives.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BIDDERS_ID` | IMPORTING | `STRING` | biddersId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_059` | WatchCreativesResponse  
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
