---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_manufacturers_v1/
title: Class /GOOG/CL_MANUFACTURERS_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:11.808488+00:00
---

# Class /GOOG/CL_MANUFACTURERS_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_manufacturers_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_MANUFACTURERS_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_manufacturers_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_manufacturers_v1)



## Class
    
    
    /GOOG/CL_MANUFACTURERS_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Manufacturer Center API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Attributes` | PUBLIC  
`TY_002` | `Capacity` | PUBLIC  
`TY_003` | `Certification` | PUBLIC  
`TY_004` | `Count` | PUBLIC  
`TY_005` | `DestinationStatus` | PUBLIC  
`TY_007` | `FeatureDescription` | PUBLIC  
`TY_008` | `FloatUnit` | PUBLIC  
`TY_009` | `Grocery` | PUBLIC  
`TY_010` | `Image` | PUBLIC  
`TY_011` | `Issue` | PUBLIC  
`TY_012` | `ListProductCertificationsResponse` | PUBLIC  
`TY_013` | `ListProductsResponse` | PUBLIC  
`TY_014` | `Nutrition` | PUBLIC  
`TY_015` | `Price` | PUBLIC  
`TY_016` | `Product` | PUBLIC  
`TY_017` | `ProductCertification` | PUBLIC  
`TY_018` | `ProductDetail` | PUBLIC  
`TY_019` | `VoluntaryNutritionFact` | PUBLIC  
`TY_020` | `GoogleShoppingManufacturersV1ProductCertification` | PUBLIC  
`TY_T_003` | `Certification` | PUBLIC  
`TY_T_005` | `DestinationStatus` | PUBLIC  
`TY_T_007` | `FeatureDescription` | PUBLIC  
`TY_T_010` | `Image` | PUBLIC  
`TY_T_011` | `Issue` | PUBLIC  
`TY_T_016` | `Product` | PUBLIC  
`TY_T_017` | `ProductCertification` | PUBLIC  
`TY_T_018` | `ProductDetail` | PUBLIC  
`TY_T_019` | `VoluntaryNutritionFact` | PUBLIC  
`TY_T_020` | `GoogleShoppingManufacturersV1ProductCertification` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | manufacturers:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://manufacturers.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250228 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
  
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
  
### DELETE_PRODUCTS

  * Description: manufacturers.accounts.products.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PRODUCTS_ID` | IMPORTING | `STRING` | productsId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PRODUCT_CERTIFICATIO

  * Description: accounts.languages.productCertifications.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_LANGUAGES_ID` | IMPORTING | `STRING` | languagesId  
`IV_P_PRODUCT_CERTIFICATIONS_ID` | IMPORTING | `STRING` | productCertificationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PRODUCTS

  * Description: manufacturers.accounts.products.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDE` | IMPORTING | `STRING` | include  
`IV_P_PRODUCTS_ID` | IMPORTING | `STRING` | productsId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | Product  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PRODUCT_CERTIFICATIONS

  * Description: manufacturers.accounts.languages.productCertifications.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_LANGUAGES_ID` | IMPORTING | `STRING` | languagesId  
`IV_P_PRODUCT_CERTIFICATIONS_ID` | IMPORTING | `STRING` | productCertificationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ProductCertification  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PRODUCTS

  * Description: manufacturers.accounts.products.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDE` | IMPORTING | `STRING` | include  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ListProductsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PRODUCT_CERTIFICATIONS

  * Description: manufacturers.accounts.languages.productCertifications.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_LANGUAGES_ID` | IMPORTING | `STRING` | languagesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | ListProductCertificationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PRODUCT_CERTIFICATION

  * Description: accounts.languages.productCertifications.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_LANGUAGES_ID` | IMPORTING | `STRING` | languagesId  
`IV_P_PRODUCT_CERTIFICATIONS_ID` | IMPORTING | `STRING` | productCertificationsId  
`IS_INPUT` | IMPORTING | `TY_017` | ProductCertification  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ProductCertification  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_PRODUCTS

  * Description: manufacturers.accounts.products.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PRODUCTS_ID` | IMPORTING | `STRING` | productsId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_001` | Attributes  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
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
