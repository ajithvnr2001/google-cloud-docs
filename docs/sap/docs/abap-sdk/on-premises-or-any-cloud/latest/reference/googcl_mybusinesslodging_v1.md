---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_mybusinesslodging_v1/
title: Class /GOOG/CL_MYBUSINESSLODGING_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:05.404183+00:00
---

# Class /GOOG/CL_MYBUSINESSLODGING_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_mybusinesslodging_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_MYBUSINESSLODGING_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_mybusinesslodging_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_mybusinesslodging_v1)



## Class
    
    
    /GOOG/CL_MYBUSINESSLODGING_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`My Business Lodging API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Accessibility` | PUBLIC  
`TY_002` | `Activities` | PUBLIC  
`TY_003` | `Business` | PUBLIC  
`TY_004` | `Connectivity` | PUBLIC  
`TY_005` | `EcoCertification` | PUBLIC  
`TY_006` | `EnergyEfficiency` | PUBLIC  
`TY_007` | `EnhancedCleaning` | PUBLIC  
`TY_008` | `Families` | PUBLIC  
`TY_009` | `FoodAndDrink` | PUBLIC  
`TY_010` | `GetGoogleUpdatedLodgingResponse` | PUBLIC  
`TY_011` | `GuestUnitFeatures` | PUBLIC  
`TY_012` | `GuestUnitType` | PUBLIC  
`TY_013` | `HealthAndSafety` | PUBLIC  
`TY_014` | `Housekeeping` | PUBLIC  
`TY_015` | `IncreasedFoodSafety` | PUBLIC  
`TY_016` | `LanguageSpoken` | PUBLIC  
`TY_017` | `LivingArea` | PUBLIC  
`TY_018` | `LivingAreaAccessibility` | PUBLIC  
`TY_019` | `LivingAreaEating` | PUBLIC  
`TY_020` | `LivingAreaFeatures` | PUBLIC  
`TY_021` | `LivingAreaLayout` | PUBLIC  
`TY_022` | `LivingAreaSleeping` | PUBLIC  
`TY_023` | `Lodging` | PUBLIC  
`TY_024` | `LodgingMetadata` | PUBLIC  
`TY_025` | `MinimizedContact` | PUBLIC  
`TY_026` | `Parking` | PUBLIC  
`TY_027` | `PaymentOptions` | PUBLIC  
`TY_028` | `PersonalProtection` | PUBLIC  
`TY_029` | `Pets` | PUBLIC  
`TY_030` | `PhysicalDistancing` | PUBLIC  
`TY_031` | `Policies` | PUBLIC  
`TY_032` | `Pools` | PUBLIC  
`TY_033` | `Property` | PUBLIC  
`TY_034` | `Services` | PUBLIC  
`TY_035` | `Sustainability` | PUBLIC  
`TY_036` | `SustainabilityCertifications` | PUBLIC  
`TY_037` | `SustainableSourcing` | PUBLIC  
`TY_038` | `TimeOfDay` | PUBLIC  
`TY_039` | `Transportation` | PUBLIC  
`TY_040` | `ViewsFromUnit` | PUBLIC  
`TY_041` | `WasteReduction` | PUBLIC  
`TY_042` | `WaterConservation` | PUBLIC  
`TY_043` | `Wellness` | PUBLIC  
`TY_T_005` | `EcoCertification` | PUBLIC  
`TY_T_012` | `GuestUnitType` | PUBLIC  
`TY_T_016` | `LanguageSpoken` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://mybusinesslodging.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | mybusinesslodging:v1 | PUBLIC  
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
  
### GET_GOOGLE_UPDATED_LODGING

  * Description: mybusinesslodging.locations.lodging.getGoogleUpdated 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_READMASK` | IMPORTING | `STRING` | readMask  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | GetGoogleUpdatedLodgingResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_LODGING_LOCATIONS

  * Description: mybusinesslodging.locations.getLodging 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_READMASK` | IMPORTING | `STRING` | readMask  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Lodging  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_LODGING_LOCATIONS

  * Description: mybusinesslodging.locations.updateLodging 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_023` | Lodging  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Lodging  
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
