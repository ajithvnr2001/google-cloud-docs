---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_deploymentmanager_v2/
title: Class /GOOG/CL_DEPLOYMENTMANAGER_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:43.005258+00:00
---

# Class /GOOG/CL_DEPLOYMENTMANAGER_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_deploymentmanager_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DEPLOYMENTMANAGER_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_deploymentmanager_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_deploymentmanager_v2)



## Class
    
    
    /GOOG/CL_DEPLOYMENTMANAGER_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Deployment Manager V2 API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AuditConfig` | PUBLIC  
`TY_002` | `AuditLogConfig` | PUBLIC  
`TY_003` | `Binding` | PUBLIC  
`TY_004` | `ConfigFile` | PUBLIC  
`TY_005` | `Deployment` | PUBLIC  
`TY_006` | `DeploymentLabelEntry` | PUBLIC  
`TY_007` | `DeploymentUpdate` | PUBLIC  
`TY_008` | `DeploymentUpdateLabelEntry` | PUBLIC  
`TY_009` | `DeploymentsCancelPreviewRequest` | PUBLIC  
`TY_010` | `DeploymentsListResponse` | PUBLIC  
`TY_011` | `DeploymentsStopRequest` | PUBLIC  
`TY_012` | `Expr` | PUBLIC  
`TY_013` | `GlobalSetPolicyRequest` | PUBLIC  
`TY_014` | `ImportFile` | PUBLIC  
`TY_015` | `Manifest` | PUBLIC  
`TY_016` | `ManifestsListResponse` | PUBLIC  
`TY_017` | `Operation` | PUBLIC  
`TY_018` | `OperationsListResponse` | PUBLIC  
`TY_019` | `Policy` | PUBLIC  
`TY_020` | `Resource` | PUBLIC  
`TY_021` | `ResourceAccessControl` | PUBLIC  
`TY_022` | `ResourceUpdate` | PUBLIC  
`TY_023` | `ResourcesListResponse` | PUBLIC  
`TY_024` | `TargetConfiguration` | PUBLIC  
`TY_025` | `TestPermissionsRequest` | PUBLIC  
`TY_026` | `TestPermissionsResponse` | PUBLIC  
`TY_027` | `Type` | PUBLIC  
`TY_028` | `TypesListResponse` | PUBLIC  
`TY_051` | `Errors` | PUBLIC  
`TY_052` | `Error` | PUBLIC  
`TY_053` | `Data` | PUBLIC  
`TY_054` | `Warnings` | PUBLIC  
`TY_055` | `Data` | PUBLIC  
`TY_056` | `Warnings` | PUBLIC  
`TY_057` | `Errors` | PUBLIC  
`TY_058` | `Error` | PUBLIC  
`TY_059` | `Data` | PUBLIC  
`TY_060` | `Warnings` | PUBLIC  
`TY_061` | `BulkInsertOperationStatus` | PUBLIC  
`TY_062` | `InstancesBulkInsertOperationMetadata` | PUBLIC  
`TY_063` | `SetCommonInstanceMetadataOperationMetadata` | PUBLIC  
`TY_064` | `SetCommonInstanceMetadataOperationMetadataPerLocationOperati` | PUBLIC  
`TY_065` | `Status` | PUBLIC  
`TY_066` | `DebugInfo` | PUBLIC  
`TY_067` | `ErrorInfo` | PUBLIC  
`TY_068` | `Help` | PUBLIC  
`TY_069` | `HelpLink` | PUBLIC  
`TY_070` | `LocalizedMessage` | PUBLIC  
`TY_071` | `QuotaExceededInfo` | PUBLIC  
`TY_072` | `ErrorDetails` | PUBLIC  
`TY_073` | `ErrorDetails` | PUBLIC  
`TY_074` | `ErrorDetails` | PUBLIC  
`TY_075` | `ErrorDetails` | PUBLIC  
`TY_076` | `ErrorDetails` | PUBLIC  
`TY_077` | `ErrorDetails` | PUBLIC  
`TY_078` | `ErrorDetails` | PUBLIC  
`TY_T_001` | `AuditConfig` | PUBLIC  
`TY_T_002` | `AuditLogConfig` | PUBLIC  
`TY_T_003` | `Binding` | PUBLIC  
`TY_T_005` | `Deployment` | PUBLIC  
`TY_T_006` | `DeploymentLabelEntry` | PUBLIC  
`TY_T_008` | `DeploymentUpdateLabelEntry` | PUBLIC  
`TY_T_014` | `ImportFile` | PUBLIC  
`TY_T_015` | `Manifest` | PUBLIC  
`TY_T_017` | `Operation` | PUBLIC  
`TY_T_020` | `Resource` | PUBLIC  
`TY_T_027` | `Type` | PUBLIC  
`TY_T_051` | `Errors` | PUBLIC  
`TY_T_053` | `Data` | PUBLIC  
`TY_T_054` | `Warnings` | PUBLIC  
`TY_T_055` | `Data` | PUBLIC  
`TY_T_056` | `Warnings` | PUBLIC  
`TY_T_057` | `Errors` | PUBLIC  
`TY_T_059` | `Data` | PUBLIC  
`TY_T_060` | `Warnings` | PUBLIC  
`TY_T_069` | `HelpLink` | PUBLIC  
`TY_T_072` | `ErrorDetails` | PUBLIC  
`TY_T_073` | `ErrorDetails` | PUBLIC  
`TY_T_074` | `ErrorDetails` | PUBLIC  
`TY_T_075` | `ErrorDetails` | PUBLIC  
`TY_T_076` | `ErrorDetails` | PUBLIC  
`TY_T_077` | `ErrorDetails` | PUBLIC  
`TY_T_078` | `ErrorDetails` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | deploymentmanager:v2 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://deploymentmanager.googleapis.com | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250303 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
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
  
### CANCEL_PREVIEW_DEPLOYMENTS

  * Description: deploymentmanager.deployments.cancelPreview 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IS_INPUT` | IMPORTING | `TY_009` | DeploymentsCancelPreviewRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DEPLOYMENTS

  * Description: deploymentmanager.deployments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DELETEPOLICY` | IMPORTING | `STRING` | deletePolicy  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DEPLOYMENTS

  * Description: deploymentmanager.deployments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Deployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_DEPLOYMENTS

  * Description: deploymentmanager.deployments.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_Q_OPTIONSREQUESTEDPOLICYVER` | IMPORTING | `STRING` | optionsRequestedPolicyVersion  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IV_P_RESOURCE` | IMPORTING | `STRING` | resource  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_MANIFESTS

  * Description: deploymentmanager.manifests.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_MANIFEST` | IMPORTING | `STRING` | manifest  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | Manifest  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: deploymentmanager.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_OPERATION` | IMPORTING | `STRING` | operation  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_RESOURCES

  * Description: deploymentmanager.resources.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IV_P_RESOURCE` | IMPORTING | `STRING` | resource  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Resource  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_DEPLOYMENTS

  * Description: deploymentmanager.deployments.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CREATEPOLICY` | IMPORTING | `STRING` | createPolicy  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_Q_PREVIEW` | IMPORTING | `STRING` | preview  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IS_INPUT` | IMPORTING | `TY_005` | Deployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DEPLOYMENTS

  * Description: deploymentmanager.deployments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | DeploymentsListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MANIFESTS

  * Description: deploymentmanager.manifests.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | ManifestsListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: deploymentmanager.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | OperationsListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_RESOURCES

  * Description: deploymentmanager.resources.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | ResourcesListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TYPES

  * Description: deploymentmanager.types.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | TypesListResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_DEPLOYMENTS

  * Description: deploymentmanager.deployments.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CREATEPOLICY` | IMPORTING | `STRING` | createPolicy  
`IV_Q_DELETEPOLICY` | IMPORTING | `STRING` | deletePolicy  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_Q_PREVIEW` | IMPORTING | `STRING` | preview  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IS_INPUT` | IMPORTING | `TY_005` | Deployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_DEPLOYMENTS

  * Description: deploymentmanager.deployments.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IV_P_RESOURCE` | IMPORTING | `STRING` | resource  
`IS_INPUT` | IMPORTING | `TY_013` | GlobalSetPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_DEPLOYMENTS

  * Description: deploymentmanager.deployments.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IS_INPUT` | IMPORTING | `TY_011` | DeploymentsStopRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_DEPLOY

  * Description: deploymentmanager.deployments.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IV_P_RESOURCE` | IMPORTING | `STRING` | resource  
`IS_INPUT` | IMPORTING | `TY_025` | TestPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | TestPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_DEPLOYMENTS

  * Description: deploymentmanager.deployments.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CREATEPOLICY` | IMPORTING | `STRING` | createPolicy  
`IV_Q_DELETEPOLICY` | IMPORTING | `STRING` | deletePolicy  
`IV_Q_HEADERBYPASSBILLINGFILTER` | IMPORTING | `STRING` | header.bypassBillingFilter  
`IV_Q_PREVIEW` | IMPORTING | `STRING` | preview  
`IV_P_DEPLOYMENT` | IMPORTING | `STRING` | deployment  
`IV_P_PROJECT` | IMPORTING | `STRING` | project  
`IS_INPUT` | IMPORTING | `TY_005` | Deployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | Operation  
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
