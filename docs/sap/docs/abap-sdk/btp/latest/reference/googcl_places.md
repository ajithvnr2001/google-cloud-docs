---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_places/
title: Class /GOOG/CL_PLACES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:54.177420+00:00
---

# Class /GOOG/CL_PLACES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_places/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_PLACES Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_places)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_places)



## Class
    
    
    /GOOG/CL_PLACES

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Maps Platform Places API`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_T_STRING` | `Table of String` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://maps.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | places | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | AAAAAA | PUBLIC  
`C_VERSION` | `STRING` | Open API Specification Version | 1.22.5 | PUBLIC  
  
## Methods

For general information about a method in ABAP SDK for Google Cloud, see [API method](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#api_method). 

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
  
### AUTOCOMPLETE

  * Description: autocomplete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INPUT` | IMPORTING | `STRING` | Input  
`IV_Q_RADIUS` | IMPORTING | `/GOOG/NUM_FLOAT` | Radius  
`IV_Q_SESSIONTOKEN` | IMPORTING | `STRING` | Session Token  
`IV_Q_COMPONENTS` | IMPORTING | `STRING` | Components  
`IV_Q_STRICTBOUNDS` | IMPORTING | `ABAP_BOOL` | Strict Bounds  
`IV_Q_OFFSET` | IMPORTING | `/GOOG/NUM_FLOAT` | Offset  
`IV_Q_ORIGIN` | IMPORTING | `STRING` | Origin  
`IV_Q_LOCATION` | IMPORTING | `STRING` | Location  
`IV_Q_LOCATIONBIAS` | IMPORTING | `STRING` | Location Bias  
`IV_Q_LOCATIONRESTRICTION` | IMPORTING | `STRING` | Location Restriction  
`IV_Q_TYPES` | IMPORTING | `STRING` | Types  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`IV_Q_REGION` | IMPORTING | `STRING` | Region  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_066` | PlacesAutocompleteResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### FIND_PLACE_FROM_TEXT

  * Description: findPlaceFromText 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INPUT` | IMPORTING | `STRING` | Input  
`IV_Q_INPUTTYPE` | IMPORTING | `STRING` | Input Type  
`IT_Q_FIELDS` | IMPORTING | `TY_T_STRING` | Fields  
`IV_Q_LOCATIONBIAS` | IMPORTING | `STRING` | Location Bias  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_070` | PlacesFindPlaceFromTextResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### NEARBY_SEARCH

  * Description: nearbySearch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_LOCATION` | IMPORTING | `STRING` | Location  
`IV_Q_RADIUS` | IMPORTING | `/GOOG/NUM_FLOAT` | Radius  
`IV_Q_KEYWORD` | IMPORTING | `STRING` | Keyword  
`IV_Q_MAXPRICE` | IMPORTING | `STRING` | Max Price  
`IV_Q_MINPRICE` | IMPORTING | `STRING` | Min Price  
`IV_Q_NAME` | IMPORTING | `STRING` | Name  
`IV_Q_OPENNOW` | IMPORTING | `ABAP_BOOL` | Open Now  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | Page Token  
`IV_Q_RANKBY` | IMPORTING | `STRING` | Rank By  
`IV_Q_TYPE` | IMPORTING | `STRING` | Type  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_071` | PlacesNearbySearchResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PLACE_DETAILS

  * Description: placeDetails 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PLACE_ID` | IMPORTING | `STRING` | Place ID  
`IT_Q_FIELDS` | IMPORTING | `TY_T_STRING` | Fields  
`IV_Q_SESSIONTOKEN` | IMPORTING | `STRING` | Session Token  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`IV_Q_REGION` | IMPORTING | `STRING` | Region  
`IV_Q_REVIEWS_SORT` | IMPORTING | `STRING` | Reviews Sort  
`IV_Q_REVIEWS_NO_TRANSLATIONS` | IMPORTING | `ABAP_BOOL` | Reviews No Translations  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_068` | PlacesDetailsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PLACE_PHOTO

  * Description: placePhoto 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PHOTO_REFERENCE` | IMPORTING | `STRING` | Photo Reference  
`IV_Q_MAXHEIGHT` | IMPORTING | `/GOOG/NUM_FLOAT` | Max Height  
`IV_Q_MAXWIDTH` | IMPORTING | `/GOOG/NUM_FLOAT` | Max Width  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_AUTOCOMPLETE

  * Description: queryAutocomplete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INPUT` | IMPORTING | `STRING` | Input  
`IV_Q_RADIUS` | IMPORTING | `/GOOG/NUM_FLOAT` | Radius  
`IV_Q_OFFSET` | IMPORTING | `/GOOG/NUM_FLOAT` | Offset  
`IV_Q_LOCATION` | IMPORTING | `STRING` | Location  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_072` | PlacesQueryAutocompleteResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEXT_SEARCH

  * Description: textSearch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_QUERY` | IMPORTING | `STRING` | Query  
`IV_Q_RADIUS` | IMPORTING | `/GOOG/NUM_FLOAT` | Radius  
`IV_Q_LOCATION` | IMPORTING | `STRING` | Location  
`IV_Q_MAXPRICE` | IMPORTING | `STRING` | Max Price  
`IV_Q_MINPRICE` | IMPORTING | `STRING` | Min Price  
`IV_Q_OPENNOW` | IMPORTING | `ABAP_BOOL` | Open Now  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | Page Token  
`IV_Q_TYPE` | IMPORTING | `STRING` | Type  
`IV_Q_LANGUAGE` | IMPORTING | `STRING` | Language  
`IV_Q_REGION` | IMPORTING | `STRING` | Region  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `/GOOG/IF_MAPS~TY_073` | PlacesTextSearchResponse  
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
