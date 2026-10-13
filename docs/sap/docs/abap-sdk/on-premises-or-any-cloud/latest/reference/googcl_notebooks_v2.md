---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_notebooks_v2/
title: Class /GOOG/CL_NOTEBOOKS_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:47.524994+00:00
---

# Class /GOOG/CL_NOTEBOOKS_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_notebooks_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_NOTEBOOKS_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_notebooks_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_notebooks_v2)



## Class
    
    
    /GOOG/CL_NOTEBOOKS_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Notebooks API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AcceleratorConfig` | PUBLIC  
`TY_002` | `Binding` | PUBLIC  
`TY_003` | `BootDisk` | PUBLIC  
`TY_005` | `CheckInstanceUpgradabilityResponse` | PUBLIC  
`TY_006` | `ContainerImage` | PUBLIC  
`TY_007` | `DataDisk` | PUBLIC  
`TY_008` | `DiagnoseInstanceRequest` | PUBLIC  
`TY_009` | `DiagnosticConfig` | PUBLIC  
`TY_011` | `Event` | PUBLIC  
`TY_012` | `Expr` | PUBLIC  
`TY_013` | `GPUDriverConfig` | PUBLIC  
`TY_014` | `GceSetup` | PUBLIC  
`TY_015` | `Instance` | PUBLIC  
`TY_016` | `ListInstancesResponse` | PUBLIC  
`TY_017` | `ListLocationsResponse` | PUBLIC  
`TY_018` | `ListOperationsResponse` | PUBLIC  
`TY_019` | `Location` | PUBLIC  
`TY_020` | `NetworkInterface` | PUBLIC  
`TY_021` | `Operation` | PUBLIC  
`TY_022` | `Policy` | PUBLIC  
`TY_023` | `ReportInstanceInfoSystemRequest` | PUBLIC  
`TY_025` | `RollbackInstanceRequest` | PUBLIC  
`TY_026` | `ServiceAccount` | PUBLIC  
`TY_027` | `SetIamPolicyRequest` | PUBLIC  
`TY_028` | `ShieldedInstanceConfig` | PUBLIC  
`TY_030` | `Status` | PUBLIC  
`TY_032` | `TestIamPermissionsRequest` | PUBLIC  
`TY_033` | `TestIamPermissionsResponse` | PUBLIC  
`TY_034` | `UpgradeHistoryEntry` | PUBLIC  
`TY_036` | `UpgradeInstanceSystemRequest` | PUBLIC  
`TY_037` | `VmImage` | PUBLIC  
`TY_038` | `AccessConfig` | PUBLIC  
`TY_039` | `Config` | PUBLIC  
`TY_040` | `DefaultValues` | PUBLIC  
`TY_041` | `ImageRelease` | PUBLIC  
`TY_042` | `ResizeDiskRequest` | PUBLIC  
`TY_043` | `SupportedValues` | PUBLIC  
`TY_044` | `RestoreInstanceRequest` | PUBLIC  
`TY_045` | `Snapshot` | PUBLIC  
`TY_T_001` | `AcceleratorConfig` | PUBLIC  
`TY_T_002` | `Binding` | PUBLIC  
`TY_T_007` | `DataDisk` | PUBLIC  
`TY_T_015` | `Instance` | PUBLIC  
`TY_T_019` | `Location` | PUBLIC  
`TY_T_020` | `NetworkInterface` | PUBLIC  
`TY_T_021` | `Operation` | PUBLIC  
`TY_T_026` | `ServiceAccount` | PUBLIC  
`TY_T_034` | `UpgradeHistoryEntry` | PUBLIC  
`TY_T_038` | `AccessConfig` | PUBLIC  
`TY_T_041` | `ImageRelease` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250224 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://notebooks.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | notebooks:v2 | PUBLIC  
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
  
### CANCEL_OPERATIONS

  * Description: notebooks.projects.locations.operations.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
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
  
### CHECK_UPGRADABILITY_INSTANC

  * Description: notebooks.projects.locations.instances.checkUpgradability 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | CheckInstanceUpgradabilityResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_INSTANCES

  * Description: notebooks.projects.locations.instances.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INSTANCEID` | IMPORTING | `STRING` | instanceId  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_015` | Instance  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_INSTANCES

  * Description: notebooks.projects.locations.instances.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATIONS

  * Description: notebooks.projects.locations.operations.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
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
  
### DIAGNOSE_INSTANCES

  * Description: notebooks.projects.locations.instances.diagnose 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_008` | DiagnoseInstanceRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONFIG_INSTANCES

  * Description: notebooks.projects.locations.instances.getConfig 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_039` | Config  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_INSTANCES

  * Description: notebooks.projects.locations.instances.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSTANCES

  * Description: notebooks.projects.locations.instances.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | Instance  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_LOCATIONS

  * Description: notebooks.projects.locations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Location  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: notebooks.projects.locations.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSTANCES

  * Description: notebooks.projects.locations.instances.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | ListInstancesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS

  * Description: notebooks.projects.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: notebooks.projects.locations.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_INSTANCES

  * Description: notebooks.projects.locations.instances.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_015` | Instance  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPORT_INFO_SYSTEM_INSTANCE

  * Description: notebooks.projects.locations.instances.reportInfoSystem 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_023` | ReportInstanceInfoSystemRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESET_INSTANCES

  * Description: notebooks.projects.locations.instances.reset 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESIZE_DISK_INSTANCES

  * Description: notebooks.projects.locations.instances.resizeDisk 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_042` | ResizeDiskRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESTORE_INSTANCES

  * Description: notebooks.projects.locations.instances.restore 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_044` | RestoreInstanceRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ROLLBACK_INSTANCES

  * Description: notebooks.projects.locations.instances.rollback 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_025` | RollbackInstanceRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_INSTANCES

  * Description: notebooks.projects.locations.instances.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_027` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### START_INSTANCES

  * Description: notebooks.projects.locations.instances.start 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_INSTANCES

  * Description: notebooks.projects.locations.instances.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_INSTAN

  * Description: notebooks.projects.locations.instances.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_032` | TestIamPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | TestIamPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPGRADE_INSTANCES

  * Description: notebooks.projects.locations.instances.upgrade 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPGRADE_SYSTEM_INSTANCES

  * Description: notebooks.projects.locations.instances.upgradeSystem 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_036` | UpgradeInstanceSystemRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | Operation  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
