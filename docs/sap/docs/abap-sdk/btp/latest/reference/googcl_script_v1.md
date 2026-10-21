---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_script_v1/
title: Class /GOOG/CL_SCRIPT_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:52.697624+00:00
---

# Class /GOOG/CL_SCRIPT_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_script_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_SCRIPT_V1 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_script_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_script_v1)



## Class
    
    
    /GOOG/CL_SCRIPT_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Apps Script API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Content` | PUBLIC  
`TY_002` | `CreateProjectRequest` | PUBLIC  
`TY_003` | `Deployment` | PUBLIC  
`TY_004` | `DeploymentConfig` | PUBLIC  
`TY_006` | `EntryPoint` | PUBLIC  
`TY_007` | `ExecutionRequest` | PUBLIC  
`TY_008` | `File` | PUBLIC  
`TY_009` | `GoogleAppsScriptTypeAddOnEntryPoint` | PUBLIC  
`TY_010` | `GoogleAppsScriptTypeExecutionApiConfig` | PUBLIC  
`TY_011` | `GoogleAppsScriptTypeExecutionApiEntryPoint` | PUBLIC  
`TY_012` | `GoogleAppsScriptTypeFunction` | PUBLIC  
`TY_013` | `GoogleAppsScriptTypeFunctionSet` | PUBLIC  
`TY_014` | `GoogleAppsScriptTypeProcess` | PUBLIC  
`TY_015` | `GoogleAppsScriptTypeUser` | PUBLIC  
`TY_016` | `GoogleAppsScriptTypeWebAppConfig` | PUBLIC  
`TY_017` | `GoogleAppsScriptTypeWebAppEntryPoint` | PUBLIC  
`TY_018` | `ListDeploymentsResponse` | PUBLIC  
`TY_019` | `ListScriptProcessesResponse` | PUBLIC  
`TY_020` | `ListUserProcessesResponse` | PUBLIC  
`TY_022` | `ListVersionsResponse` | PUBLIC  
`TY_023` | `Metrics` | PUBLIC  
`TY_024` | `MetricsValue` | PUBLIC  
`TY_025` | `Operation` | PUBLIC  
`TY_026` | `Project` | PUBLIC  
`TY_029` | `Status` | PUBLIC  
`TY_031` | `UpdateDeploymentRequest` | PUBLIC  
`TY_033` | `Version` | PUBLIC  
`TY_T_003` | `Deployment` | PUBLIC  
`TY_T_006` | `EntryPoint` | PUBLIC  
`TY_T_008` | `File` | PUBLIC  
`TY_T_012` | `GoogleAppsScriptTypeFunction` | PUBLIC  
`TY_T_014` | `GoogleAppsScriptTypeProcess` | PUBLIC  
`TY_T_024` | `MetricsValue` | PUBLIC  
`TY_T_033` | `Version` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | script:v1 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://script.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241103 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.1 | PUBLIC  
  
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
  
### CREATE_DEPLOYMENTS

  * Description: script.projects.deployments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IS_INPUT` | IMPORTING | `TY_004` | DeploymentConfig  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Deployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PROJECTS

  * Description: script.projects.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_002` | CreateProjectRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Project  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VERSIONS

  * Description: script.projects.versions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IS_INPUT` | IMPORTING | `TY_033` | Version  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Version  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DEPLOYMENTS

  * Description: script.projects.deployments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DEPLOYMENT_ID` | IMPORTING | `STRING` | deploymentId  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENT_PROJECTS

  * Description: script.projects.getContent 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VERSIONNUMBER` | IMPORTING | `STRING` | versionNumber  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Content  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEPLOYMENTS

  * Description: script.projects.deployments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DEPLOYMENT_ID` | IMPORTING | `STRING` | deploymentId  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Deployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_METRICS_PROJECTS

  * Description: script.projects.getMetrics 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_METRICSFILTERDEPLOYMENTID` | IMPORTING | `STRING` | metricsFilter.deploymentId  
`IV_Q_METRICSGRANULARITY` | IMPORTING | `STRING` | metricsGranularity  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Metrics  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PROJECTS

  * Description: script.projects.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Project  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VERSIONS

  * Description: script.projects.versions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IV_P_VERSION_NUMBER` | IMPORTING | `STRING` | versionNumber  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Version  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEPLOYMENTS

  * Description: script.projects.deployments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ListDeploymentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PROCESSES

  * Description: script.processes.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_USERPROCESSFILTERDEPLOYME` | IMPORTING | `STRING` | userProcessFilter.deploymentId  
`IV_Q_USERPROCESSFILTERENDTIME` | IMPORTING | `STRING` | userProcessFilter.endTime  
`IV_Q_USERPROCESSFILTERFUNCTION` | IMPORTING | `STRING` | userProcessFilter.functionName  
`IV_Q_USERPROCESSFILTERPROJECTN` | IMPORTING | `STRING` | userProcessFilter.projectName  
`IV_Q_USERPROCESSFILTERSCRIPTID` | IMPORTING | `STRING` | userProcessFilter.scriptId  
`IV_Q_USERPROCESSFILTERSTARTTIM` | IMPORTING | `STRING` | userProcessFilter.startTime  
`IV_Q_USERPROCESSFILTERSTATUSES` | IMPORTING | `STRING` | userProcessFilter.statuses  
`IV_Q_USERPROCESSFILTERTYPES` | IMPORTING | `STRING` | userProcessFilter.types  
`IV_Q_USERPROCESSFILTERUSERACCE` | IMPORTING | `STRING` | userProcessFilter.userAccessLevels  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListUserProcessesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SCRIPT_PROCESSES_PROCE

  * Description: script.processes.listScriptProcesses 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SCRIPTID` | IMPORTING | `STRING` | scriptId  
`IV_Q_SCRIPTPROCESSFILTERDEPLOY` | IMPORTING | `STRING` | scriptProcessFilter.deploymentId  
`IV_Q_SCRIPTPROCESSFILTERENDTIM` | IMPORTING | `STRING` | scriptProcessFilter.endTime  
`IV_Q_SCRIPTPROCESSFILTERFUNCTI` | IMPORTING | `STRING` | scriptProcessFilter.functionName  
`IV_Q_SCRIPTPROCESSFILTERSTARTT` | IMPORTING | `STRING` | scriptProcessFilter.startTime  
`IV_Q_SCRIPTPROCESSFILTERSTATUS` | IMPORTING | `STRING` | scriptProcessFilter.statuses  
`IV_Q_SCRIPTPROCESSFILTERTYPES` | IMPORTING | `STRING` | scriptProcessFilter.types  
`IV_Q_SCRIPTPROCESSFILTERUSERAC` | IMPORTING | `STRING` | scriptProcessFilter.userAccessLevels  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | ListScriptProcessesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VERSIONS

  * Description: script.projects.versions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | ListVersionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RUN_SCRIPTS

  * Description: script.scripts.run 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IS_INPUT` | IMPORTING | `TY_007` | ExecutionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CONTENT_PROJECTS

  * Description: script.projects.updateContent 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IS_INPUT` | IMPORTING | `TY_001` | Content  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Content  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_DEPLOYMENTS

  * Description: script.projects.deployments.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DEPLOYMENT_ID` | IMPORTING | `STRING` | deploymentId  
`IV_P_SCRIPT_ID` | IMPORTING | `STRING` | scriptId  
`IS_INPUT` | IMPORTING | `TY_031` | UpdateDeploymentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Deployment  
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
