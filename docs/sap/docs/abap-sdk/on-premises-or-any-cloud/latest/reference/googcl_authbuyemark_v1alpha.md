---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authbuyemark_v1alpha/
title: Class /GOOG/CL_AUTHBUYEMARK_V1ALPHA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:11.831469+00:00
---

# Class /GOOG/CL_AUTHBUYEMARK_V1ALPHA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authbuyemark_v1alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_AUTHBUYEMARK_V1ALPHA Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_authbuyemark_v1alpha)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authbuyemark_v1alpha)



## Class
    
    
    /GOOG/CL_AUTHBUYEMARK_V1ALPHA

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Authorized Buyers Marketplace API v1alpha`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AcceptProposalRequest` | PUBLIC  
`TY_005` | `AdSize` | PUBLIC  
`TY_006` | `AddCreativeRequest` | PUBLIC  
`TY_007` | `AddNoteRequest` | PUBLIC  
`TY_008` | `AuctionPackage` | PUBLIC  
`TY_009` | `BatchUpdateDealsRequest` | PUBLIC  
`TY_010` | `BatchUpdateDealsResponse` | PUBLIC  
`TY_012` | `Client` | PUBLIC  
`TY_013` | `ClientUser` | PUBLIC  
`TY_014` | `Contact` | PUBLIC  
`TY_015` | `CreativeRequirements` | PUBLIC  
`TY_016` | `CriteriaTargeting` | PUBLIC  
`TY_017` | `DataSegment` | PUBLIC  
`TY_018` | `DayPart` | PUBLIC  
`TY_019` | `DayPartTargeting` | PUBLIC  
`TY_023` | `Deal` | PUBLIC  
`TY_024` | `DealPausingInfo` | PUBLIC  
`TY_025` | `DeliveryControl` | PUBLIC  
`TY_027` | `FinalizedDeal` | PUBLIC  
`TY_028` | `FirstPartyMobileApplicationTargeting` | PUBLIC  
`TY_029` | `FrequencyCap` | PUBLIC  
`TY_030` | `InventorySizeTargeting` | PUBLIC  
`TY_031` | `InventoryTypeTargeting` | PUBLIC  
`TY_032` | `ListAuctionPackagesResponse` | PUBLIC  
`TY_033` | `ListClientUsersResponse` | PUBLIC  
`TY_034` | `ListClientsResponse` | PUBLIC  
`TY_035` | `ListDataSegmentsResponse` | PUBLIC  
`TY_036` | `ListDealsResponse` | PUBLIC  
`TY_037` | `ListFinalizedDealsResponse` | PUBLIC  
`TY_038` | `ListProposalsResponse` | PUBLIC  
`TY_039` | `ListPublisherProfilesResponse` | PUBLIC  
`TY_040` | `MarketplaceTargeting` | PUBLIC  
`TY_041` | `MediaPlanner` | PUBLIC  
`TY_042` | `MobileApplicationTargeting` | PUBLIC  
`TY_043` | `Money` | PUBLIC  
`TY_044` | `Note` | PUBLIC  
`TY_045` | `OperatingSystemTargeting` | PUBLIC  
`TY_046` | `PauseFinalizedDealRequest` | PUBLIC  
`TY_047` | `PlacementTargeting` | PUBLIC  
`TY_048` | `PreferredDealTerms` | PUBLIC  
`TY_049` | `Price` | PUBLIC  
`TY_050` | `PrivateAuctionTerms` | PUBLIC  
`TY_051` | `PrivateData` | PUBLIC  
`TY_052` | `ProgrammaticGuaranteedTerms` | PUBLIC  
`TY_053` | `Proposal` | PUBLIC  
`TY_054` | `PublisherProfile` | PUBLIC  
`TY_055` | `PublisherProfileMobileApplication` | PUBLIC  
`TY_057` | `RtbMetrics` | PUBLIC  
`TY_058` | `SendRfpRequest` | PUBLIC  
`TY_061` | `SubscribeClientsRequest` | PUBLIC  
`TY_062` | `TechnologyTargeting` | PUBLIC  
`TY_063` | `TimeOfDay` | PUBLIC  
`TY_064` | `TimeZone` | PUBLIC  
`TY_066` | `UnsubscribeClientsRequest` | PUBLIC  
`TY_067` | `UpdateDealRequest` | PUBLIC  
`TY_068` | `UriTargeting` | PUBLIC  
`TY_069` | `VideoTargeting` | PUBLIC  
`TY_T_005` | `AdSize` | PUBLIC  
`TY_T_008` | `AuctionPackage` | PUBLIC  
`TY_T_012` | `Client` | PUBLIC  
`TY_T_013` | `ClientUser` | PUBLIC  
`TY_T_014` | `Contact` | PUBLIC  
`TY_T_017` | `DataSegment` | PUBLIC  
`TY_T_018` | `DayPart` | PUBLIC  
`TY_T_023` | `Deal` | PUBLIC  
`TY_T_027` | `FinalizedDeal` | PUBLIC  
`TY_T_029` | `FrequencyCap` | PUBLIC  
`TY_T_041` | `MediaPlanner` | PUBLIC  
`TY_T_044` | `Note` | PUBLIC  
`TY_T_053` | `Proposal` | PUBLIC  
`TY_T_054` | `PublisherProfile` | PUBLIC  
`TY_T_055` | `PublisherProfileMobileApplication` | PUBLIC  
`TY_T_067` | `UpdateDealRequest` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | authorizedbuyersmarketplace:v1alpha | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://authorizedbuyersmarketplace.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250306 | PUBLIC  
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
  
### ACCEPT_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.accept 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IS_INPUT` | IMPORTING | `TY_001` | AcceptProposalRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ACTIVATE_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.activate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ACTIVATE_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.activate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_DATA_SEGMENTS_ID` | IMPORTING | `STRING` | dataSegmentsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | DataSegment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ACTIVATE_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.activate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ClientUser  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_CREATIVE_FINALIZED_DEAL

  * Description: buyers.finalizedDeals.addCreative 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_FINALIZED_DEALS_ID` | IMPORTING | `STRING` | finalizedDealsId  
`IS_INPUT` | IMPORTING | `TY_006` | AddCreativeRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | FinalizedDeal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ADD_NOTE_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.addNote 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IS_INPUT` | IMPORTING | `TY_007` | AddNoteRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### BATCH_UPDATE_DEALS

  * Description: buyers.proposals.deals.batchUpdate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IS_INPUT` | IMPORTING | `TY_009` | BatchUpdateDealsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | BatchUpdateDealsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CANCEL_NEGOTIATION_PROPOSAL

  * Description: buyers.proposals.cancelNegotiation 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IS_INPUT` | IMPORTING | `TY_012` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IS_INPUT` | IMPORTING | `TY_017` | DataSegment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | DataSegment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IS_INPUT` | IMPORTING | `TY_013` | ClientUser  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ClientUser  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DEACTIVATE_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.deactivate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DEACTIVATE_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.deactivate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_DATA_SEGMENTS_ID` | IMPORTING | `STRING` | dataSegmentsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | DataSegment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DEACTIVATE_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.deactivate 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ClientUser  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_AUCTION_PACKAGES

  * Description: authorizedbuyersmarketplace.buyers.auctionPackages.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_AUCTION_PACKAGES_ID` | IMPORTING | `STRING` | auctionPackagesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | AuctionPackage  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_DATA_SEGMENTS_ID` | IMPORTING | `STRING` | dataSegmentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | DataSegment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.deals.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IV_P_DEALS_ID` | IMPORTING | `STRING` | dealsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Deal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FINALIZED_DEALS

  * Description: authorizedbuyersmarketplace.buyers.finalizedDeals.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_FINALIZED_DEALS_ID` | IMPORTING | `STRING` | finalizedDealsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | FinalizedDeal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PUBLISHER_PROFILES

  * Description: authorizedbuyersmarketplace.buyers.publisherProfiles.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PUBLISHER_PROFILES_ID` | IMPORTING | `STRING` | publisherProfilesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_054` | PublisherProfile  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ClientUser  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AUCTION_PACKAGES

  * Description: authorizedbuyersmarketplace.bidders.auctionPackages.list 
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
`ES_OUTPUT` | EXPORTING | `TY_032` | ListAuctionPackagesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AUCTION_PACKAGES1

  * Description: authorizedbuyersmarketplace.buyers.auctionPackages.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | ListAuctionPackagesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | ListClientsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | ListDataSegmentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.deals.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | ListDealsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FINALIZED_DEALS

  * Description: authorizedbuyersmarketplace.bidders.finalizedDeals.list 
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
`ES_OUTPUT` | EXPORTING | `TY_037` | ListFinalizedDealsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FINALIZED_DEALS1

  * Description: authorizedbuyersmarketplace.buyers.finalizedDeals.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_037` | ListFinalizedDealsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_038` | ListProposalsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PUBLISHER_PROFILES

  * Description: authorizedbuyersmarketplace.buyers.publisherProfiles.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | ListPublisherProfilesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_USERS

  * Description: authorizedbuyersmarketplace.buyers.clients.users.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | ListClientUsersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CLIENTS

  * Description: authorizedbuyersmarketplace.buyers.clients.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IS_INPUT` | IMPORTING | `TY_012` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DATA_SEGMENTS

  * Description: authorizedbuyersmarketplace.buyers.dataSegments.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_DATA_SEGMENTS_ID` | IMPORTING | `STRING` | dataSegmentsId  
`IS_INPUT` | IMPORTING | `TY_017` | DataSegment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | DataSegment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.deals.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IV_P_DEALS_ID` | IMPORTING | `STRING` | dealsId  
`IS_INPUT` | IMPORTING | `TY_023` | Deal  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Deal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_PROPOSALS_ID` | IMPORTING | `STRING` | proposalsId  
`IS_INPUT` | IMPORTING | `TY_053` | Proposal  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PAUSE_FINALIZED_DEALS

  * Description: authorizedbuyersmarketplace.buyers.finalizedDeals.pause 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_FINALIZED_DEALS_ID` | IMPORTING | `STRING` | finalizedDealsId  
`IS_INPUT` | IMPORTING | `TY_046` | PauseFinalizedDealRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | FinalizedDeal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_FINALIZED_DEALS

  * Description: authorizedbuyersmarketplace.buyers.finalizedDeals.resume 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_FINALIZED_DEALS_ID` | IMPORTING | `STRING` | finalizedDealsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | FinalizedDeal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEND_RFP_PROPOSALS

  * Description: authorizedbuyersmarketplace.buyers.proposals.sendRfp 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IS_INPUT` | IMPORTING | `TY_058` | SendRfpRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | Proposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_READY_TO_SERVE_FINALIZE

  * Description: buyers.finalizedDeals.setReadyToServe 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_FINALIZED_DEALS_ID` | IMPORTING | `STRING` | finalizedDealsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | FinalizedDeal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SUBSCRIBE_AUCTION_PACKAGES

  * Description: buyers.auctionPackages.subscribe 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_AUCTION_PACKAGES_ID` | IMPORTING | `STRING` | auctionPackagesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | AuctionPackage  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SUBSCRIBE_CLIENTS_AUCTION_P

  * Description: buyers.auctionPackages.subscribeClients 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_AUCTION_PACKAGES_ID` | IMPORTING | `STRING` | auctionPackagesId  
`IS_INPUT` | IMPORTING | `TY_061` | SubscribeClientsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | AuctionPackage  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNSUBSCRIBE_AUCTION_PACKAGE

  * Description: buyers.auctionPackages.unsubscribe 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_AUCTION_PACKAGES_ID` | IMPORTING | `STRING` | auctionPackagesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | AuctionPackage  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNSUBSCRIBE_CLIENTS_AUCTION

  * Description: buyers.auctionPackages.unsubscribeClients 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_BUYERS_ID` | IMPORTING | `STRING` | buyersId  
`IV_P_AUCTION_PACKAGES_ID` | IMPORTING | `STRING` | auctionPackagesId  
`IS_INPUT` | IMPORTING | `TY_066` | UnsubscribeClientsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | AuctionPackage  
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
