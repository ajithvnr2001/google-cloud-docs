---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_apigeeregistry_v1/
title: Class /GOOG/CL_APIGEEREGISTRY_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:42.846458+00:00
---

# Class /GOOG/CL_APIGEEREGISTRY_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_apigeeregistry_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_APIGEEREGISTRY_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_apigeeregistry_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_apigeeregistry_v1)



## Class
    
    
    /GOOG/CL_APIGEEREGISTRY_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Apigee Registry API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Api` | PUBLIC  
`TY_002` | `ApiDeployment` | PUBLIC  
`TY_003` | `ApiSpec` | PUBLIC  
`TY_004` | `ApiVersion` | PUBLIC  
`TY_005` | `Artifact` | PUBLIC  
`TY_006` | `Binding` | PUBLIC  
`TY_007` | `Build` | PUBLIC  
`TY_009` | `Config` | PUBLIC  
`TY_011` | `Expr` | PUBLIC  
`TY_012` | `HttpBody` | PUBLIC  
`TY_013` | `Instance` | PUBLIC  
`TY_014` | `ListApiDeploymentRevisionsResponse` | PUBLIC  
`TY_015` | `ListApiDeploymentsResponse` | PUBLIC  
`TY_016` | `ListApiSpecRevisionsResponse` | PUBLIC  
`TY_017` | `ListApiSpecsResponse` | PUBLIC  
`TY_018` | `ListApiVersionsResponse` | PUBLIC  
`TY_019` | `ListApisResponse` | PUBLIC  
`TY_020` | `ListArtifactsResponse` | PUBLIC  
`TY_021` | `ListLocationsResponse` | PUBLIC  
`TY_022` | `ListOperationsResponse` | PUBLIC  
`TY_023` | `Location` | PUBLIC  
`TY_024` | `Operation` | PUBLIC  
`TY_025` | `Policy` | PUBLIC  
`TY_026` | `RollbackApiDeploymentRequest` | PUBLIC  
`TY_027` | `RollbackApiSpecRequest` | PUBLIC  
`TY_028` | `SetIamPolicyRequest` | PUBLIC  
`TY_029` | `Status` | PUBLIC  
`TY_030` | `TagApiDeploymentRevisionRequest` | PUBLIC  
`TY_031` | `TagApiSpecRevisionRequest` | PUBLIC  
`TY_032` | `TestIamPermissionsRequest` | PUBLIC  
`TY_033` | `TestIamPermissionsResponse` | PUBLIC  
`TY_T_001` | `Api` | PUBLIC  
`TY_T_002` | `ApiDeployment` | PUBLIC  
`TY_T_003` | `ApiSpec` | PUBLIC  
`TY_T_004` | `ApiVersion` | PUBLIC  
`TY_T_005` | `Artifact` | PUBLIC  
`TY_T_006` | `Binding` | PUBLIC  
`TY_T_023` | `Location` | PUBLIC  
`TY_T_024` | `Operation` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20231204 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://apigeeregistry.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | apigeeregistry:v1 | PUBLIC  
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

  * Description: apigeeregistry.projects.locations.operations.cancel 
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
  
### CREATE_APIS

  * Description: apigeeregistry.projects.locations.apis.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_APIID` | IMPORTING | `STRING` | apiId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_001` | Api  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Api  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ARTIFACTS

  * Description: apigeeregistry.projects.locations.apis.artifacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ARTIFACTID` | IMPORTING | `STRING` | artifactId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ARTIFACTS1

  * Description: projects.locations.apis.deployments.artifacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ARTIFACTID` | IMPORTING | `STRING` | artifactId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ARTIFACTID` | IMPORTING | `STRING` | artifactId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ARTIFACTS3

  * Description: projects.locations.apis.versions.specs.artifacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ARTIFACTID` | IMPORTING | `STRING` | artifactId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ARTIFACTID` | IMPORTING | `STRING` | artifactId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_APIDEPLOYMENTID` | IMPORTING | `STRING` | apiDeploymentId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IS_INPUT` | IMPORTING | `TY_002` | ApiDeployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_INSTANCES

  * Description: apigeeregistry.projects.locations.instances.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INSTANCEID` | IMPORTING | `STRING` | instanceId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_013` | Instance  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_SPECS

  * Description: projects.locations.apis.versions.specs.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_APISPECID` | IMPORTING | `STRING` | apiSpecId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IS_INPUT` | IMPORTING | `TY_003` | ApiSpec  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_VERSIONS

  * Description: apigeeregistry.projects.locations.apis.versions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_APIVERSIONID` | IMPORTING | `STRING` | apiVersionId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IS_INPUT` | IMPORTING | `TY_004` | ApiVersion  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | ApiVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_APIS

  * Description: apigeeregistry.projects.locations.apis.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ARTIFACTS

  * Description: apigeeregistry.projects.locations.apis.artifacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ARTIFACTS1

  * Description: projects.locations.apis.deployments.artifacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ARTIFACTS3

  * Description: projects.locations.apis.versions.specs.artifacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_INSTANCES

  * Description: apigeeregistry.projects.locations.instances.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATIONS

  * Description: apigeeregistry.projects.locations.operations.delete 
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
  
### DELETE_REVISION_DEPLOYMENTS

  * Description: projects.locations.apis.deployments.deleteRevision 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_REVISION_SPECS

  * Description: projects.locations.apis.versions.specs.deleteRevision 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_SPECS

  * Description: projects.locations.apis.versions.specs.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_VERSIONS

  * Description: apigeeregistry.projects.locations.apis.versions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_APIS

  * Description: apigeeregistry.projects.locations.apis.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Api  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ARTIFACTS

  * Description: apigeeregistry.projects.locations.apis.artifacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ARTIFACTS1

  * Description: projects.locations.apis.deployments.artifacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ARTIFACTS3

  * Description: projects.locations.apis.versions.specs.artifacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_ARTIFACTS

  * Description: projects.locations.apis.artifacts.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_ARTIFACTS1

  * Description: projects.locations.apis.deployments.artifacts.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_ARTIFACTS3

  * Description: locations.apis.versions.specs.artifacts.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTENTS_SPECS

  * Description: projects.locations.apis.versions.specs.getContents 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | HttpBody  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_APIS

  * Description: apigeeregistry.projects.locations.apis.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_ARTIFACTS

  * Description: projects.locations.apis.artifacts.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_ARTIFACTS1

  * Description: projects.locations.apis.versions.artifacts.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_ARTIFACTS2

  * Description: locations.apis.versions.specs.artifacts.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_ARTIFACTS3

  * Description: apigeeregistry.projects.locations.artifacts.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_DEPLOYMENTS

  * Description: projects.locations.apis.deployments.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_DOCUMENTS

  * Description: apigeeregistry.projects.locations.documents.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_INSTANCES

  * Description: apigeeregistry.projects.locations.instances.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_RUNTIME

  * Description: apigeeregistry.projects.locations.runtime.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_SPECS

  * Description: projects.locations.apis.versions.specs.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_VERSIONS

  * Description: projects.locations.apis.versions.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | options.requestedPolicyVersion  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_INSTANCES

  * Description: apigeeregistry.projects.locations.instances.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_013` | Instance  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_LOCATIONS

  * Description: apigeeregistry.projects.locations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Location  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: apigeeregistry.projects.locations.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SPECS

  * Description: apigeeregistry.projects.locations.apis.versions.specs.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VERSIONS

  * Description: apigeeregistry.projects.locations.apis.versions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | ApiVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_APIS

  * Description: apigeeregistry.projects.locations.apis.list 
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
`ES_OUTPUT` | EXPORTING | `TY_019` | ListApisResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ARTIFACTS

  * Description: apigeeregistry.projects.locations.apis.artifacts.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListArtifactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ARTIFACTS1

  * Description: projects.locations.apis.deployments.artifacts.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListArtifactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListArtifactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ARTIFACTS3

  * Description: projects.locations.apis.versions.specs.artifacts.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListArtifactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.list 
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
`ES_OUTPUT` | EXPORTING | `TY_020` | ListArtifactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | ListApiDeploymentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LOCATIONS

  * Description: apigeeregistry.projects.locations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | ListLocationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: apigeeregistry.projects.locations.operations.list 
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
`ES_OUTPUT` | EXPORTING | `TY_022` | ListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_REVISIONS_DEPLOYMENTS

  * Description: projects.locations.apis.deployments.listRevisions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | ListApiDeploymentRevisionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_REVISIONS_SPECS

  * Description: projects.locations.apis.versions.specs.listRevisions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | ListApiSpecRevisionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SPECS

  * Description: apigeeregistry.projects.locations.apis.versions.specs.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | ListApiSpecsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VERSIONS

  * Description: apigeeregistry.projects.locations.apis.versions.list 
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
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | ListApiVersionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_APIS

  * Description: apigeeregistry.projects.locations.apis.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IS_INPUT` | IMPORTING | `TY_001` | Api  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Api  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IS_INPUT` | IMPORTING | `TY_002` | ApiDeployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_SPECS

  * Description: apigeeregistry.projects.locations.apis.versions.specs.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IS_INPUT` | IMPORTING | `TY_003` | ApiSpec  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_VERSIONS

  * Description: apigeeregistry.projects.locations.apis.versions.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IS_INPUT` | IMPORTING | `TY_004` | ApiVersion  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | ApiVersion  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPLACE_ARTIFACT_ARTIFACTS

  * Description: projects.locations.apis.artifacts.replaceArtifact 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPLACE_ARTIFACT_ARTIFACTS1

  * Description: locations.apis.deployments.artifacts.replaceArtifact 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPLACE_ARTIFACT_ARTIFACTS2

  * Description: projects.locations.apis.versions.artifacts.replaceArtifact 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPLACE_ARTIFACT_ARTIFACTS3

  * Description: locations.apis.versions.specs.artifacts.replaceArtifact 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### REPLACE_ARTIFACT_ARTIFACTS4

  * Description: apigeeregistry.projects.locations.artifacts.replaceArtifact 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_005` | Artifact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Artifact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ROLLBACK_DEPLOYMENTS

  * Description: apigeeregistry.projects.locations.apis.deployments.rollback 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IS_INPUT` | IMPORTING | `TY_026` | RollbackApiDeploymentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ROLLBACK_SPECS

  * Description: projects.locations.apis.versions.specs.rollback 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IS_INPUT` | IMPORTING | `TY_027` | RollbackApiSpecRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_APIS

  * Description: apigeeregistry.projects.locations.apis.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_ARTIFACTS

  * Description: projects.locations.apis.artifacts.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_ARTIFACTS1

  * Description: projects.locations.apis.versions.artifacts.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_ARTIFACTS2

  * Description: locations.apis.versions.specs.artifacts.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_ARTIFACTS3

  * Description: apigeeregistry.projects.locations.artifacts.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_DEPLOYMENTS

  * Description: projects.locations.apis.deployments.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_DOCUMENTS

  * Description: apigeeregistry.projects.locations.documents.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_INSTANCES

  * Description: apigeeregistry.projects.locations.instances.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_RUNTIME

  * Description: apigeeregistry.projects.locations.runtime.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_SPECS

  * Description: projects.locations.apis.versions.specs.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_VERSIONS

  * Description: projects.locations.apis.versions.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IS_INPUT` | IMPORTING | `TY_028` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TAG_REVISION_DEPLOYMENTS

  * Description: projects.locations.apis.deployments.tagRevision 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
`IS_INPUT` | IMPORTING | `TY_030` | TagApiDeploymentRevisionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | ApiDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TAG_REVISION_SPECS

  * Description: projects.locations.apis.versions.specs.tagRevision 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IS_INPUT` | IMPORTING | `TY_031` | TagApiSpecRevisionRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ApiSpec  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_APIS

  * Description: apigeeregistry.projects.locations.apis.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
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
  
### TEST_IAM_PERMISSIONS_ARTIFA

  * Description: projects.locations.apis.artifacts.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
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
  
### TEST_IAM_PERMISSIONS_ARTIFA1

  * Description: locations.apis.versions.artifacts.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
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
  
### TEST_IAM_PERMISSIONS_ARTIFA2

  * Description: locations.apis.versions.specs.artifacts.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
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
  
### TEST_IAM_PERMISSIONS_ARTIFA3

  * Description: projects.locations.artifacts.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_ARTIFACTS_ID` | IMPORTING | `STRING` | artifactsId  
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
  
### TEST_IAM_PERMISSIONS_DEPLOY

  * Description: projects.locations.apis.deployments.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_DEPLOYMENTS_ID` | IMPORTING | `STRING` | deploymentsId  
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
  
### TEST_IAM_PERMISSIONS_DOCUME

  * Description: projects.locations.documents.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
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
  
### TEST_IAM_PERMISSIONS_INSTAN

  * Description: projects.locations.instances.testIamPermissions 
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
  
### TEST_IAM_PERMISSIONS_RUNTIM

  * Description: projects.locations.runtime.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
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
  
### TEST_IAM_PERMISSIONS_SPECS

  * Description: projects.locations.apis.versions.specs.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
`IV_P_SPECS_ID` | IMPORTING | `STRING` | specsId  
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
  
### TEST_IAM_PERMISSIONS_VERSIO

  * Description: projects.locations.apis.versions.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_APIS_ID` | IMPORTING | `STRING` | apisId  
`IV_P_VERSIONS_ID` | IMPORTING | `STRING` | versionsId  
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
  
### CLOSE

  * Description: Close Connection 
  * Visibility: PUBLIC 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
