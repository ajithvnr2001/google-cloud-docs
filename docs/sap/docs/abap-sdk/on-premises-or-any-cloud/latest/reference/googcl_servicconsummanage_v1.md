---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicconsummanage_v1/
title: Class /GOOG/CL_SERVICCONSUMMANAGE_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:42.021038+00:00
---

# Class /GOOG/CL_SERVICCONSUMMANAGE_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicconsummanage_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SERVICCONSUMMANAGE_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_servicconsummanage_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_servicconsummanage_v1)



## Class
    
    
    /GOOG/CL_SERVICCONSUMMANAGE_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Service Consumer Management API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AddTenantProjectRequest` | PUBLIC  
`TY_003` | `ApplyTenantProjectConfigRequest` | PUBLIC  
`TY_004` | `AttachTenantProjectRequest` | PUBLIC  
`TY_012` | `BillingConfig` | PUBLIC  
`TY_021` | `CreateTenancyUnitRequest` | PUBLIC  
`TY_025` | `DeleteTenantProjectRequest` | PUBLIC  
`TY_040` | `ListOperationsResponse` | PUBLIC  
`TY_041` | `ListTenancyUnitsResponse` | PUBLIC  
`TY_057` | `Operation` | PUBLIC  
`TY_061` | `PolicyBinding` | PUBLIC  
`TY_066` | `RemoveTenantProjectRequest` | PUBLIC  
`TY_068` | `SearchTenancyUnitsResponse` | PUBLIC  
`TY_069` | `ServiceAccountConfig` | PUBLIC  
`TY_072` | `Status` | PUBLIC  
`TY_076` | `TenancyUnit` | PUBLIC  
`TY_077` | `TenantProjectConfig` | PUBLIC  
`TY_078` | `TenantProjectPolicy` | PUBLIC  
`TY_079` | `TenantResource` | PUBLIC  
`TY_081` | `UndeleteTenantProjectRequest` | PUBLIC  
`TY_T_057` | `Operation` | PUBLIC  
`TY_T_061` | `PolicyBinding` | PUBLIC  
`TY_T_076` | `TenancyUnit` | PUBLIC  
`TY_T_079` | `TenantResource` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | serviceconsumermanagement:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://serviceconsumermanagement.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250227 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.10 | PUBLIC  
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
  
### ADD_PROJECT_TENANCY_UNITS

  * Description: serviceconsumermanagement.services.tenancyUnits.addProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_001` | AddTenantProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### APPLY_PROJECT_CONFIG_TENANC

  * Description: services.tenancyUnits.applyProjectConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_003` | ApplyTenantProjectConfigRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ATTACH_PROJECT_TENANCY_UNIT

  * Description: services.tenancyUnits.attachProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_004` | AttachTenantProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CANCEL_OPERATIONS

  * Description: serviceconsumermanagement.operations.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TENANCY_UNITS

  * Description: serviceconsumermanagement.services.tenancyUnits.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IS_INPUT` | IMPORTING | `TY_021` | CreateTenancyUnitRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_076` | TenancyUnit  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATIONS

  * Description: serviceconsumermanagement.operations.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PROJECT_TENANCY_UNIT

  * Description: services.tenancyUnits.deleteProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_025` | DeleteTenantProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TENANCY_UNITS

  * Description: serviceconsumermanagement.services.tenancyUnits.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: serviceconsumermanagement.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: serviceconsumermanagement.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_040` | ListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TENANCY_UNITS

  * Description: serviceconsumermanagement.services.tenancyUnits.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | ListTenancyUnitsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REMOVE_PROJECT_TENANCY_UNIT

  * Description: services.tenancyUnits.removeProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_066` | RemoveTenantProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_SERVICES

  * Description: serviceconsumermanagement.services.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_068` | SearchTenancyUnitsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNDELETE_PROJECT_TENANCY_UN

  * Description: services.tenancyUnits.undeleteProject 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SERVICES_ID` | IMPORTING | `STRING` | servicesId  
`IV_P_SERVICES_ID1` | IMPORTING | `STRING` | servicesId1  
`IV_P_SERVICES_ID2` | IMPORTING | `STRING` | servicesId2  
`IV_P_TENANCY_UNITS_ID` | IMPORTING | `STRING` | tenancyUnitsId  
`IS_INPUT` | IMPORTING | `TY_081` | UndeleteTenantProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | Operation  
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
