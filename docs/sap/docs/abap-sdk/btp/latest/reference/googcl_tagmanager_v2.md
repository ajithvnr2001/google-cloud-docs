---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_tagmanager_v2/
title: Class /GOOG/CL_TAGMANAGER_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:35.405013+00:00
---

# Class /GOOG/CL_TAGMANAGER_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_tagmanager_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_TAGMANAGER_V2 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_tagmanager_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_tagmanager_v2)



## Class
    
    
    /GOOG/CL_TAGMANAGER_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Tag Manager API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Account` | PUBLIC  
`TY_002` | `AccountAccess` | PUBLIC  
`TY_003` | `AccountFeatures` | PUBLIC  
`TY_004` | `BuiltInVariable` | PUBLIC  
`TY_005` | `Client` | PUBLIC  
`TY_006` | `Condition` | PUBLIC  
`TY_007` | `Container` | PUBLIC  
`TY_008` | `ContainerAccess` | PUBLIC  
`TY_009` | `ContainerFeatures` | PUBLIC  
`TY_010` | `ContainerVersion` | PUBLIC  
`TY_011` | `ContainerVersionHeader` | PUBLIC  
`TY_012` | `CreateBuiltInVariableResponse` | PUBLIC  
`TY_013` | `CreateContainerVersionRequestVersionOptions` | PUBLIC  
`TY_014` | `CreateContainerVersionResponse` | PUBLIC  
`TY_015` | `CustomTemplate` | PUBLIC  
`TY_016` | `Destination` | PUBLIC  
`TY_017` | `Entity` | PUBLIC  
`TY_018` | `Environment` | PUBLIC  
`TY_019` | `Folder` | PUBLIC  
`TY_020` | `FolderEntities` | PUBLIC  
`TY_021` | `GalleryReference` | PUBLIC  
`TY_022` | `GetContainerSnippetResponse` | PUBLIC  
`TY_023` | `GetWorkspaceStatusResponse` | PUBLIC  
`TY_024` | `GtagConfig` | PUBLIC  
`TY_025` | `ListAccountsResponse` | PUBLIC  
`TY_026` | `ListClientsResponse` | PUBLIC  
`TY_027` | `ListContainerVersionsResponse` | PUBLIC  
`TY_028` | `ListContainersResponse` | PUBLIC  
`TY_029` | `ListDestinationsResponse` | PUBLIC  
`TY_030` | `ListEnabledBuiltInVariablesResponse` | PUBLIC  
`TY_031` | `ListEnvironmentsResponse` | PUBLIC  
`TY_032` | `ListFoldersResponse` | PUBLIC  
`TY_033` | `ListGtagConfigResponse` | PUBLIC  
`TY_034` | `ListTagsResponse` | PUBLIC  
`TY_035` | `ListTemplatesResponse` | PUBLIC  
`TY_036` | `ListTransformationsResponse` | PUBLIC  
`TY_037` | `ListTriggersResponse` | PUBLIC  
`TY_038` | `ListUserPermissionsResponse` | PUBLIC  
`TY_039` | `ListVariablesResponse` | PUBLIC  
`TY_040` | `ListWorkspacesResponse` | PUBLIC  
`TY_041` | `ListZonesResponse` | PUBLIC  
`TY_042` | `MergeConflict` | PUBLIC  
`TY_043` | `Parameter` | PUBLIC  
`TY_044` | `PublishContainerVersionResponse` | PUBLIC  
`TY_045` | `QuickPreviewResponse` | PUBLIC  
`TY_046` | `RevertBuiltInVariableResponse` | PUBLIC  
`TY_047` | `RevertClientResponse` | PUBLIC  
`TY_048` | `RevertFolderResponse` | PUBLIC  
`TY_049` | `RevertTagResponse` | PUBLIC  
`TY_050` | `RevertTemplateResponse` | PUBLIC  
`TY_051` | `RevertTransformationResponse` | PUBLIC  
`TY_052` | `RevertTriggerResponse` | PUBLIC  
`TY_053` | `RevertVariableResponse` | PUBLIC  
`TY_054` | `RevertZoneResponse` | PUBLIC  
`TY_055` | `SetupTag` | PUBLIC  
`TY_056` | `SyncStatus` | PUBLIC  
`TY_057` | `SyncWorkspaceResponse` | PUBLIC  
`TY_058` | `Tag` | PUBLIC  
`TY_059` | `TagConsentSetting` | PUBLIC  
`TY_060` | `TeardownTag` | PUBLIC  
`TY_061` | `Transformation` | PUBLIC  
`TY_062` | `Trigger` | PUBLIC  
`TY_063` | `UserPermission` | PUBLIC  
`TY_064` | `Variable` | PUBLIC  
`TY_065` | `VariableFormatValue` | PUBLIC  
`TY_066` | `Workspace` | PUBLIC  
`TY_067` | `Zone` | PUBLIC  
`TY_068` | `ZoneBoundary` | PUBLIC  
`TY_069` | `ZoneChildContainer` | PUBLIC  
`TY_070` | `ZoneTypeRestriction` | PUBLIC  
`TY_T_001` | `Account` | PUBLIC  
`TY_T_004` | `BuiltInVariable` | PUBLIC  
`TY_T_005` | `Client` | PUBLIC  
`TY_T_006` | `Condition` | PUBLIC  
`TY_T_007` | `Container` | PUBLIC  
`TY_T_008` | `ContainerAccess` | PUBLIC  
`TY_T_011` | `ContainerVersionHeader` | PUBLIC  
`TY_T_015` | `CustomTemplate` | PUBLIC  
`TY_T_016` | `Destination` | PUBLIC  
`TY_T_017` | `Entity` | PUBLIC  
`TY_T_018` | `Environment` | PUBLIC  
`TY_T_019` | `Folder` | PUBLIC  
`TY_T_024` | `GtagConfig` | PUBLIC  
`TY_T_042` | `MergeConflict` | PUBLIC  
`TY_T_043` | `Parameter` | PUBLIC  
`TY_T_055` | `SetupTag` | PUBLIC  
`TY_T_058` | `Tag` | PUBLIC  
`TY_T_060` | `TeardownTag` | PUBLIC  
`TY_T_061` | `Transformation` | PUBLIC  
`TY_T_062` | `Trigger` | PUBLIC  
`TY_T_063` | `UserPermission` | PUBLIC  
`TY_T_064` | `Variable` | PUBLIC  
`TY_T_066` | `Workspace` | PUBLIC  
`TY_T_067` | `Zone` | PUBLIC  
`TY_T_069` | `ZoneChildContainer` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.1 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241111 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://tagmanager.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | tagmanager:v2 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
  
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
  
### COMBINE_CONTAINERS

  * Description: tagmanager.accounts.containers.combine 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWUSERPERMISSIONFEATUR` | IMPORTING | `STRING` | allowUserPermissionFeatureUpdate  
`IV_Q_CONTAINERID` | IMPORTING | `STRING` | containerId  
`IV_Q_SETTINGSOURCE` | IMPORTING | `STRING` | settingSource  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_BUILT_IN_VARIABLES

  * Description: accounts.containers.workspaces.built_in_variables.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_TYPE` | IMPORTING | `STRING` | type  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | CreateBuiltInVariableResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_005` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Client  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_007` | Container  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IS_INPUT` | IMPORTING | `TY_018` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_019` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_GTAG_CONFIG

  * Description: accounts.containers.workspaces.gtag_config.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_024` | GtagConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GtagConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_058` | Tag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_015` | CustomTemplate  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | CustomTemplate  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_061` | Transformation  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_061` | Transformation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_062` | Trigger  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_062` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_USER_PERMISSIONS

  * Description: tagmanager.accounts.user_permissions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IS_INPUT` | IMPORTING | `TY_063` | UserPermission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_063` | UserPermission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_064` | Variable  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_064` | Variable  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VERSION_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.create_version 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_013` | CreateContainerVersionRequestVersionOptions  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | CreateContainerVersionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IS_INPUT` | IMPORTING | `TY_066` | Workspace  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_066` | Workspace  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_067` | Zone  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_067` | Zone  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_BUILT_IN_VARIABLES

  * Description: accounts.containers.workspaces.built_in_variables.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_TYPE` | IMPORTING | `STRING` | type  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_ENVIRONMENTS_ID` | IMPORTING | `STRING` | environmentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_GTAG_CONFIG

  * Description: accounts.containers.workspaces.gtag_config.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_GTAG_CONFIG_ID` | IMPORTING | `STRING` | gtag_configId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TAGS_ID` | IMPORTING | `STRING` | tagsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TEMPLATES_ID` | IMPORTING | `STRING` | templatesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRANSFORMATIONS_ID` | IMPORTING | `STRING` | transformationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRIGGERS_ID` | IMPORTING | `STRING` | triggersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_USER_PERMISSIONS

  * Description: tagmanager.accounts.user_permissions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_USER_PERMISSIONS_ID` | IMPORTING | `STRING` | user_permissionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_VARIABLES_ID` | IMPORTING | `STRING` | variablesId  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_ZONES_ID` | IMPORTING | `STRING` | zonesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ENTITIES_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.entities 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | FolderEntities  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Account  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Client  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DESTINATIONS

  * Description: tagmanager.accounts.containers.destinations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_DESTINATIONS_ID` | IMPORTING | `STRING` | destinationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | Destination  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_ENVIRONMENTS_ID` | IMPORTING | `STRING` | environmentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_GTAG_CONFIG

  * Description: tagmanager.accounts.containers.workspaces.gtag_config.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_GTAG_CONFIG_ID` | IMPORTING | `STRING` | gtag_configId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GtagConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_STATUS_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.getStatus 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | GetWorkspaceStatusResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TAGS_ID` | IMPORTING | `STRING` | tagsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TEMPLATES_ID` | IMPORTING | `STRING` | templatesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | CustomTemplate  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRANSFORMATIONS_ID` | IMPORTING | `STRING` | transformationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_061` | Transformation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRIGGERS_ID` | IMPORTING | `STRING` | triggersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_062` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_USER_PERMISSIONS

  * Description: tagmanager.accounts.user_permissions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_USER_PERMISSIONS_ID` | IMPORTING | `STRING` | user_permissionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_063` | UserPermission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_VARIABLES_ID` | IMPORTING | `STRING` | variablesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_064` | Variable  
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
`IV_Q_CONTAINERVERSIONID` | IMPORTING | `STRING` | containerVersionId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_066` | Workspace  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_ZONES_ID` | IMPORTING | `STRING` | zonesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_067` | Zone  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LATEST_VERSION_HEADERS

  * Description: tagmanager.accounts.containers.version_headers.latest 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | ContainerVersionHeader  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LINK_DESTINATIONS

  * Description: tagmanager.accounts.containers.destinations.link 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWUSERPERMISSIONFEATUR` | IMPORTING | `STRING` | allowUserPermissionFeatureUpdate  
`IV_Q_DESTINATIONID` | IMPORTING | `STRING` | destinationId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | Destination  
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
`IV_Q_INCLUDEGOOGLETAGS` | IMPORTING | `STRING` | includeGoogleTags  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | ListAccountsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_BUILT_IN_VARIABLES

  * Description: accounts.containers.workspaces.built_in_variables.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | ListEnabledBuiltInVariablesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | ListClientsResponse  
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
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | ListContainersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DESTINATIONS

  * Description: tagmanager.accounts.containers.destinations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | ListDestinationsResponse  
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
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | ListEnvironmentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | ListFoldersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_GTAG_CONFIG

  * Description: tagmanager.accounts.containers.workspaces.gtag_config.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | ListGtagConfigResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | ListTagsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_035` | ListTemplatesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | ListTransformationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_037` | ListTriggersResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_USER_PERMISSIONS

  * Description: tagmanager.accounts.user_permissions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_038` | ListUserPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | ListVariablesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VERSION_HEADERS

  * Description: tagmanager.accounts.containers.version_headers.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | ListContainerVersionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_040` | ListWorkspacesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_041` | ListZonesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIVE_VERSIONS

  * Description: tagmanager.accounts.containers.versions.live 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LOOKUP_CONTAINERS

  * Description: tagmanager.accounts.containers.lookup 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DESTINATIONID` | IMPORTING | `STRING` | destinationId  
`IV_Q_TAGID` | IMPORTING | `STRING` | tagId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MOVE_ENTITIES_TO_FOLDER_FOL

  * Description: containers.workspaces.folders.move_entities_to_folder 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_TAGID` | IMPORTING | `STRING` | tagId  
`IV_Q_TRIGGERID` | IMPORTING | `STRING` | triggerId  
`IV_Q_VARIABLEID` | IMPORTING | `STRING` | variableId  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IS_INPUT` | IMPORTING | `TY_019` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MOVE_TAG_ID_CONTAINERS

  * Description: tagmanager.accounts.containers.move_tag_id 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWUSERPERMISSIONFEATUR` | IMPORTING | `STRING` | allowUserPermissionFeatureUpdate  
`IV_Q_COPYSETTINGS` | IMPORTING | `STRING` | copySettings  
`IV_Q_COPYTERMSOFSERVICE` | IMPORTING | `STRING` | copyTermsOfService  
`IV_Q_COPYUSERS` | IMPORTING | `STRING` | copyUsers  
`IV_Q_TAGID` | IMPORTING | `STRING` | tagId  
`IV_Q_TAGNAME` | IMPORTING | `STRING` | tagName  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_044` | PublishContainerVersionResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUICK_PREVIEW_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.quick_preview 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_045` | QuickPreviewResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REAUTHORIZE_ENVIRONMENTS

  * Description: tagmanager.accounts.containers.environments.reauthorize 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_ENVIRONMENTS_ID` | IMPORTING | `STRING` | environmentsId  
`IS_INPUT` | IMPORTING | `TY_018` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESOLVE_CONFLICT_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.resolve_conflict 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_017` | Entity  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_BUILT_IN_VARIABLES

  * Description: accounts.containers.workspaces.built_in_variables.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_TYPE` | IMPORTING | `STRING` | type  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_046` | RevertBuiltInVariableResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_047` | RevertClientResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_048` | RevertFolderResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TAGS_ID` | IMPORTING | `STRING` | tagsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_049` | RevertTagResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TEMPLATES_ID` | IMPORTING | `STRING` | templatesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_050` | RevertTemplateResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRANSFORMATIONS_ID` | IMPORTING | `STRING` | transformationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_051` | RevertTransformationResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRIGGERS_ID` | IMPORTING | `STRING` | triggersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_052` | RevertTriggerResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_VARIABLES_ID` | IMPORTING | `STRING` | variablesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_053` | RevertVariableResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REVERT_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.revert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_ZONES_ID` | IMPORTING | `STRING` | zonesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_054` | RevertZoneResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_LATEST_VERSIONS

  * Description: tagmanager.accounts.containers.versions.set_latest 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SNIPPET_CONTAINERS

  * Description: tagmanager.accounts.containers.snippet 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GetContainerSnippetResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SYNC_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.sync 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_057` | SyncWorkspaceResponse  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ContainerVersion  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
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
  
### UPDATE_CLIENTS

  * Description: tagmanager.accounts.containers.workspaces.clients.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_CLIENTS_ID` | IMPORTING | `STRING` | clientsId  
`IS_INPUT` | IMPORTING | `TY_005` | Client  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Client  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IS_INPUT` | IMPORTING | `TY_007` | Container  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Container  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_ENVIRONMENTS_ID` | IMPORTING | `STRING` | environmentsId  
`IS_INPUT` | IMPORTING | `TY_018` | Environment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | Environment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_FOLDERS

  * Description: tagmanager.accounts.containers.workspaces.folders.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IS_INPUT` | IMPORTING | `TY_019` | Folder  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Folder  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_GTAG_CONFIG

  * Description: accounts.containers.workspaces.gtag_config.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_GTAG_CONFIG_ID` | IMPORTING | `STRING` | gtag_configId  
`IS_INPUT` | IMPORTING | `TY_024` | GtagConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | GtagConfig  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TAGS

  * Description: tagmanager.accounts.containers.workspaces.tags.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TAGS_ID` | IMPORTING | `STRING` | tagsId  
`IS_INPUT` | IMPORTING | `TY_058` | Tag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_058` | Tag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TEMPLATES

  * Description: tagmanager.accounts.containers.workspaces.templates.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TEMPLATES_ID` | IMPORTING | `STRING` | templatesId  
`IS_INPUT` | IMPORTING | `TY_015` | CustomTemplate  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | CustomTemplate  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TRANSFORMATIONS

  * Description: accounts.containers.workspaces.transformations.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRANSFORMATIONS_ID` | IMPORTING | `STRING` | transformationsId  
`IS_INPUT` | IMPORTING | `TY_061` | Transformation  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_061` | Transformation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TRIGGERS

  * Description: tagmanager.accounts.containers.workspaces.triggers.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_TRIGGERS_ID` | IMPORTING | `STRING` | triggersId  
`IS_INPUT` | IMPORTING | `TY_062` | Trigger  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_062` | Trigger  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_USER_PERMISSIONS

  * Description: tagmanager.accounts.user_permissions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_USER_PERMISSIONS_ID` | IMPORTING | `STRING` | user_permissionsId  
`IS_INPUT` | IMPORTING | `TY_063` | UserPermission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_063` | UserPermission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_VARIABLES

  * Description: tagmanager.accounts.containers.workspaces.variables.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_VARIABLES_ID` | IMPORTING | `STRING` | variablesId  
`IS_INPUT` | IMPORTING | `TY_064` | Variable  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_064` | Variable  
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
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IS_INPUT` | IMPORTING | `TY_010` | ContainerVersion  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | ContainerVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_WORKSPACES

  * Description: tagmanager.accounts.containers.workspaces.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IS_INPUT` | IMPORTING | `TY_066` | Workspace  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_066` | Workspace  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_ZONES

  * Description: tagmanager.accounts.containers.workspaces.zones.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FINGERPRINT` | IMPORTING | `STRING` | fingerprint  
`IV_P_ACCOUNTS_ID` | IMPORTING | `STRING` | accountsId  
`IV_P_CONTAINERS_ID` | IMPORTING | `STRING` | containersId  
`IV_P_WORKSPACES_ID` | IMPORTING | `STRING` | workspacesId  
`IV_P_ZONES_ID` | IMPORTING | `STRING` | zonesId  
`IS_INPUT` | IMPORTING | `TY_067` | Zone  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_067` | Zone  
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
