---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authorbuyersmarket_v1/
title: Class /GOOG/CL_AUTHORBUYERSMARKET_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:12.534979+00:00
---

# Class /GOOG/CL_AUTHORBUYERSMARKET_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authorbuyersmarket_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_AUTHORBUYERSMARKET_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_authorbuyersmarket_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_authorbuyersmarket_v1)



## Class
    
    
    /GOOG/CL_AUTHORBUYERSMARKET_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Authorized Buyers Marketplace API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AcceptProposalRequest` | PUBLIC  
`TY_004` | `AdSize` | PUBLIC  
`TY_005` | `AddCreativeRequest` | PUBLIC  
`TY_006` | `AddNoteRequest` | PUBLIC  
`TY_007` | `AuctionPackage` | PUBLIC  
`TY_008` | `BatchUpdateDealsRequest` | PUBLIC  
`TY_009` | `BatchUpdateDealsResponse` | PUBLIC  
`TY_011` | `Client` | PUBLIC  
`TY_012` | `ClientUser` | PUBLIC  
`TY_013` | `Contact` | PUBLIC  
`TY_014` | `CreativeRequirements` | PUBLIC  
`TY_015` | `CriteriaTargeting` | PUBLIC  
`TY_016` | `DayPart` | PUBLIC  
`TY_017` | `DayPartTargeting` | PUBLIC  
`TY_020` | `Deal` | PUBLIC  
`TY_021` | `DealPausingInfo` | PUBLIC  
`TY_022` | `DeliveryControl` | PUBLIC  
`TY_024` | `FinalizedDeal` | PUBLIC  
`TY_025` | `FirstPartyMobileApplicationTargeting` | PUBLIC  
`TY_026` | `FrequencyCap` | PUBLIC  
`TY_027` | `InventorySizeTargeting` | PUBLIC  
`TY_028` | `InventoryTypeTargeting` | PUBLIC  
`TY_029` | `ListAuctionPackagesResponse` | PUBLIC  
`TY_030` | `ListClientUsersResponse` | PUBLIC  
`TY_031` | `ListClientsResponse` | PUBLIC  
`TY_032` | `ListDealsResponse` | PUBLIC  
`TY_033` | `ListFinalizedDealsResponse` | PUBLIC  
`TY_034` | `ListProposalsResponse` | PUBLIC  
`TY_035` | `ListPublisherProfilesResponse` | PUBLIC  
`TY_036` | `MarketplaceTargeting` | PUBLIC  
`TY_037` | `MobileApplicationTargeting` | PUBLIC  
`TY_038` | `Money` | PUBLIC  
`TY_039` | `Note` | PUBLIC  
`TY_040` | `OperatingSystemTargeting` | PUBLIC  
`TY_041` | `PauseFinalizedDealRequest` | PUBLIC  
`TY_042` | `PlacementTargeting` | PUBLIC  
`TY_043` | `PreferredDealTerms` | PUBLIC  
`TY_044` | `Price` | PUBLIC  
`TY_045` | `PrivateAuctionTerms` | PUBLIC  
`TY_046` | `PrivateData` | PUBLIC  
`TY_047` | `ProgrammaticGuaranteedTerms` | PUBLIC  
`TY_048` | `Proposal` | PUBLIC  
`TY_049` | `PublisherProfile` | PUBLIC  
`TY_050` | `PublisherProfileMobileApplication` | PUBLIC  
`TY_052` | `RtbMetrics` | PUBLIC  
`TY_053` | `SendRfpRequest` | PUBLIC  
`TY_056` | `SubscribeClientsRequest` | PUBLIC  
`TY_057` | `TechnologyTargeting` | PUBLIC  
`TY_058` | `TimeOfDay` | PUBLIC  
`TY_059` | `TimeZone` | PUBLIC  
`TY_061` | `UnsubscribeClientsRequest` | PUBLIC  
`TY_062` | `UpdateDealRequest` | PUBLIC  
`TY_063` | `UriTargeting` | PUBLIC  
`TY_064` | `VideoTargeting` | PUBLIC  
`TY_065` | `MediaPlanner` | PUBLIC  
`TY_T_004` | `AdSize` | PUBLIC  
`TY_T_007` | `AuctionPackage` | PUBLIC  
`TY_T_011` | `Client` | PUBLIC  
`TY_T_012` | `ClientUser` | PUBLIC  
`TY_T_013` | `Contact` | PUBLIC  
`TY_T_016` | `DayPart` | PUBLIC  
`TY_T_020` | `Deal` | PUBLIC  
`TY_T_024` | `FinalizedDeal` | PUBLIC  
`TY_T_026` | `FrequencyCap` | PUBLIC  
`TY_T_039` | `Note` | PUBLIC  
`TY_T_048` | `Proposal` | PUBLIC  
`TY_T_049` | `PublisherProfile` | PUBLIC  
`TY_T_050` | `PublisherProfileMobileApplication` | PUBLIC  
`TY_T_062` | `UpdateDealRequest` | PUBLIC  
`TY_T_065` | `MediaPlanner` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250306 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://authorizedbuyersmarketplace.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | authorizedbuyersmarketplace:v1 | PUBLIC  
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
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`ES_OUTPUT` | EXPORTING | `TY_011` | Client  
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
`ES_OUTPUT` | EXPORTING | `TY_012` | ClientUser  
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
`IS_INPUT` | IMPORTING | `TY_005` | AddCreativeRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | FinalizedDeal  
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
`IS_INPUT` | IMPORTING | `TY_006` | AddNoteRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`IS_INPUT` | IMPORTING | `TY_008` | BatchUpdateDealsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | BatchUpdateDealsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`IS_INPUT` | IMPORTING | `TY_011` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Client  
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
`IS_INPUT` | IMPORTING | `TY_012` | ClientUser  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | ClientUser  
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
`ES_OUTPUT` | EXPORTING | `TY_011` | Client  
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
`ES_OUTPUT` | EXPORTING | `TY_012` | ClientUser  
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
`ES_OUTPUT` | EXPORTING | `TY_007` | AuctionPackage  
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
`ES_OUTPUT` | EXPORTING | `TY_011` | Client  
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
`ES_OUTPUT` | EXPORTING | `TY_020` | Deal  
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
`ES_OUTPUT` | EXPORTING | `TY_024` | FinalizedDeal  
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
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`ES_OUTPUT` | EXPORTING | `TY_049` | PublisherProfile  
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
`ES_OUTPUT` | EXPORTING | `TY_012` | ClientUser  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AUCTION_PACKAGES

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
`ES_OUTPUT` | EXPORTING | `TY_029` | ListAuctionPackagesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_AUCTION_PACKAGES1

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
`ES_OUTPUT` | EXPORTING | `TY_029` | ListAuctionPackagesResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_031` | ListClientsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_032` | ListDealsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_033` | ListFinalizedDealsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_033` | ListFinalizedDealsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_034` | ListProposalsResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_035` | ListPublisherProfilesResponse  
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
`ES_OUTPUT` | EXPORTING | `TY_030` | ListClientUsersResponse  
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
`IS_INPUT` | IMPORTING | `TY_011` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Client  
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
`IS_INPUT` | IMPORTING | `TY_020` | Deal  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Deal  
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
`IS_INPUT` | IMPORTING | `TY_048` | Proposal  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`IS_INPUT` | IMPORTING | `TY_041` | PauseFinalizedDealRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | FinalizedDeal  
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
`ES_OUTPUT` | EXPORTING | `TY_024` | FinalizedDeal  
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
`IS_INPUT` | IMPORTING | `TY_053` | SendRfpRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_048` | Proposal  
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
`ES_OUTPUT` | EXPORTING | `TY_024` | FinalizedDeal  
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
`ES_OUTPUT` | EXPORTING | `TY_007` | AuctionPackage  
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
`IS_INPUT` | IMPORTING | `TY_056` | SubscribeClientsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | AuctionPackage  
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
`ES_OUTPUT` | EXPORTING | `TY_007` | AuctionPackage  
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
`IS_INPUT` | IMPORTING | `TY_061` | UnsubscribeClientsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | AuctionPackage  
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
