---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_tagmanager_v1/
title: Class /GOOG/CL_TAGMANAGER_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:36.693757+00:00
---

# Class /GOOG/CL_TAGMANAGER_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_tagmanager_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_TAGMANAGER_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_tagmanager_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_tagmanager_v1)



## Class
    
    
    /GOOG/CL_TAGMANAGER_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Tag Manager API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Account` | PUBLIC  
`TY_002` | `AccountAccess` | PUBLIC  
`TY_003` | `Condition` | PUBLIC  
`TY_004` | `Container` | PUBLIC  
`TY_005` | `ContainerAccess` | PUBLIC  
`TY_006` | `ContainerVersion` | PUBLIC  
`TY_007` | `ContainerVersionHeader` | PUBLIC  
`TY_008` | `CreateContainerVersionRequestVersionOptions` | PUBLIC  
`TY_009` | `CreateContainerVersionResponse` | PUBLIC  
`TY_010` | `Environment` | PUBLIC  
`TY_011` | `Folder` | PUBLIC  
`TY_012` | `FolderEntities` | PUBLIC  
`TY_013` | `ListAccountUsersResponse` | PUBLIC  
`TY_014` | `ListAccountsResponse` | PUBLIC  
`TY_015` | `ListContainerVersionsResponse` | PUBLIC  
`TY_016` | `ListContainersResponse` | PUBLIC  
`TY_017` | `ListEnvironmentsResponse` | PUBLIC  
`TY_018` | `ListFoldersResponse` | PUBLIC  
`TY_019` | `ListTagsResponse` | PUBLIC  
`TY_020` | `ListTriggersResponse` | PUBLIC  
`TY_021` | `ListVariablesResponse` | PUBLIC  
`TY_022` | `Macro` | PUBLIC  
`TY_023` | `Parameter` | PUBLIC  
`TY_024` | `PublishContainerVersionResponse` | PUBLIC  
`TY_025` | `Rule` | PUBLIC  
`TY_026` | `SetupTag` | PUBLIC  
`TY_027` | `Tag` | PUBLIC  
`TY_028` | `TeardownTag` | PUBLIC  
`TY_029` | `Trigger` | PUBLIC  
`TY_030` | `UserAccess` | PUBLIC  
`TY_031` | `Variable` | PUBLIC  
`TY_T_001` | `Account` | PUBLIC  
`TY_T_003` | `Condition` | PUBLIC  
`TY_T_004` | `Container` | PUBLIC  
`TY_T_005` | `ContainerAccess` | PUBLIC  
`TY_T_006` | `ContainerVersion` | PUBLIC  
`TY_T_007` | `ContainerVersionHeader` | PUBLIC  
`TY_T_010` | `Environment` | PUBLIC  
`TY_T_011` | `Folder` | PUBLIC  
`TY_T_022` | `Macro` | PUBLIC  
`TY_T_023` | `Parameter` | PUBLIC  
`TY_T_025` | `Rule` | PUBLIC  
`TY_T_026` | `SetupTag` | PUBLIC  
`TY_T_027` | `Tag` | PUBLIC  
`TY_T_028` | `TeardownTag` | PUBLIC  
`TY_T_029` | `Trigger` | PUBLIC  
`TY_T_030` | `UserAccess` | PUBLIC  
`TY_T_031` | `Variable` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | tagmanager:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://tagmanager.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
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
  
### CREATE_CONTAINERS

  * Description: tagmanager.accounts.containers.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IS_INPUT` | IMPORTING | `TY_004` | Container  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_010` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_FOLDERS

  * Description: tagmanager.accounts.containers.folders.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_011` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PERMISSIONS

  * Description: tagmanager.accounts.permissions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IS_INPUT` | IMPORTING | `TY_030` | UserAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | UserAccess  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TAGS

  * Description: tagmanager.accounts.containers.tags.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_027` | Tag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TRIGGERS

  * Description: tagmanager.accounts.containers.triggers.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_029` | Trigger  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VARIABLES

  * Description: tagmanager.accounts.containers.variables.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_031` | Variable  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Variable  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_008` | CreateContainerVersionRequestVersionOptions  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | CreateContainerVersionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONTAINERS

  * Description: tagmanager.accounts.containers.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_ENVIRONMENT_ID` | IMPORTING | `STRING` | environmentId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_FOLDERS

  * Description: tagmanager.accounts.containers.folders.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PERMISSIONS

  * Description: tagmanager.accounts.permissions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TAGS

  * Description: tagmanager.accounts.containers.tags.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TAG_ID` | IMPORTING | `STRING` | tagId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TRIGGERS

  * Description: tagmanager.accounts.containers.triggers.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TRIGGER_ID` | IMPORTING | `STRING` | triggerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_VARIABLES

  * Description: tagmanager.accounts.containers.variables.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_VARIABLE_ID` | IMPORTING | `STRING` | variableId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ACCOUNTS

  * Description: tagmanager.accounts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Account  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTAINERS

  * Description: tagmanager.accounts.containers.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_ENVIRONMENT_ID` | IMPORTING | `STRING` | environmentId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FOLDERS

  * Description: tagmanager.accounts.containers.folders.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PERMISSIONS

  * Description: tagmanager.accounts.permissions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | UserAccess  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TAGS

  * Description: tagmanager.accounts.containers.tags.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TAG_ID` | IMPORTING | `STRING` | tagId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TRIGGERS

  * Description: tagmanager.accounts.containers.triggers.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TRIGGER_ID` | IMPORTING | `STRING` | triggerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VARIABLES

  * Description: tagmanager.accounts.containers.variables.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_VARIABLE_ID` | IMPORTING | `STRING` | variableId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Variable  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VERSIONS

  * Description: tagmanager.accounts.containers.versions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ACCOUNTS

  * Description: tagmanager.accounts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ListAccountsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONTAINERS

  * Description: tagmanager.accounts.containers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | ListContainersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ENTITIES

  * Description: tagmanager.accounts.containers.folders.entities.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | FolderEntities  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ListEnvironmentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FOLDERS

  * Description: tagmanager.accounts.containers.folders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ListFoldersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PERMISSIONS

  * Description: tagmanager.accounts.permissions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | ListAccountUsersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TAGS

  * Description: tagmanager.accounts.containers.tags.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | ListTagsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TRIGGERS

  * Description: tagmanager.accounts.containers.triggers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListTriggersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VARIABLES

  * Description: tagmanager.accounts.containers.variables.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | ListVariablesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VERSIONS

  * Description: tagmanager.accounts.containers.versions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERS` | IMPORTING | `STRING` | headers  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | ListContainerVersionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PUBLISH_VERSIONS

  * Description: tagmanager.accounts.containers.versions.publish 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | PublishContainerVersionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESTORE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.restore 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNDELETE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.undelete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_ACCOUNTS

  * Description: tagmanager.accounts.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IS_INPUT` | IMPORTING | `TY_001` | Account  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Account  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONTAINERS

  * Description: tagmanager.accounts.containers.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IS_INPUT` | IMPORTING | `TY_004` | Container  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_ENVIRONMENT_ID` | IMPORTING | `STRING` | environmentId  
`IS_INPUT` | IMPORTING | `TY_010` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_FOLDERS

  * Description: tagmanager.accounts.containers.folders.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`IS_INPUT` | IMPORTING | `TY_011` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_MOVE_FOLDERS

  * Description: tagmanager.accounts.containers.move_folders.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_TAGID` | IMPORTING | `STRING` | tagId  
`IV_Q_TRIGGERID` | IMPORTING | `STRING` | triggerId  
`IV_Q_VARIABLEID` | IMPORTING | `STRING` | variableId  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`IS_INPUT` | IMPORTING | `TY_011` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_PERMISSIONS

  * Description: tagmanager.accounts.permissions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`IS_INPUT` | IMPORTING | `TY_030` | UserAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | UserAccess  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_REAUTHORIZE_ENVIRONM

  * Description: accounts.containers.reauthorize_environments.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_ENVIRONMENT_ID` | IMPORTING | `STRING` | environmentId  
`IS_INPUT` | IMPORTING | `TY_010` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TAGS

  * Description: tagmanager.accounts.containers.tags.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TAG_ID` | IMPORTING | `STRING` | tagId  
`IS_INPUT` | IMPORTING | `TY_027` | Tag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TRIGGERS

  * Description: tagmanager.accounts.containers.triggers.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_TRIGGER_ID` | IMPORTING | `STRING` | triggerId  
`IS_INPUT` | IMPORTING | `TY_029` | Trigger  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_VARIABLES

  * Description: tagmanager.accounts.containers.variables.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_VARIABLE_ID` | IMPORTING | `STRING` | variableId  
`IS_INPUT` | IMPORTING | `TY_031` | Variable  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Variable  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNT_ID` | IMPORTING | `STRING` | accountId  
`IV_P_CONTAINER_ID` | IMPORTING | `STRING` | containerId  
`IV_P_CONTAINER_VERSION_ID` | IMPORTING | `STRING` | containerVersionId  
`IS_INPUT` | IMPORTING | `TY_006` | ContainerVersion  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | ContainerVersion  
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
