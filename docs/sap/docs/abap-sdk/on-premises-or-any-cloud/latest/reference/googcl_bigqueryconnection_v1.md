---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigqueryconnection_v1/
title: Class /GOOG/CL_BIGQUERYCONNECTION_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:07.697414+00:00
---

# Class /GOOG/CL_BIGQUERYCONNECTION_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigqueryconnection_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_BIGQUERYCONNECTION_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_bigqueryconnection_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigqueryconnection_v1)



## Class
    
    
    /GOOG/CL_BIGQUERYCONNECTION_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`BigQuery Connection API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AuditConfig` | PUBLIC  
`TY_002` | `AuditLogConfig` | PUBLIC  
`TY_003` | `AwsAccessRole` | PUBLIC  
`TY_004` | `AwsProperties` | PUBLIC  
`TY_005` | `AzureProperties` | PUBLIC  
`TY_006` | `Binding` | PUBLIC  
`TY_007` | `CloudResourceProperties` | PUBLIC  
`TY_008` | `CloudSpannerProperties` | PUBLIC  
`TY_009` | `CloudSqlCredential` | PUBLIC  
`TY_010` | `CloudSqlProperties` | PUBLIC  
`TY_011` | `Connection` | PUBLIC  
`TY_012` | `ConnectorConfiguration` | PUBLIC  
`TY_013` | `ConnectorConfigurationAuthentication` | PUBLIC  
`TY_014` | `ConnectorConfigurationEndpoint` | PUBLIC  
`TY_015` | `ConnectorConfigurationSecret` | PUBLIC  
`TY_016` | `ConnectorConfigurationUsernamePassword` | PUBLIC  
`TY_018` | `Expr` | PUBLIC  
`TY_019` | `GetIamPolicyRequest` | PUBLIC  
`TY_020` | `GetPolicyOptions` | PUBLIC  
`TY_021` | `ListConnectionsResponse` | PUBLIC  
`TY_022` | `MetastoreServiceConfig` | PUBLIC  
`TY_023` | `Policy` | PUBLIC  
`TY_024` | `SalesforceDataCloudProperties` | PUBLIC  
`TY_025` | `SetIamPolicyRequest` | PUBLIC  
`TY_026` | `SparkHistoryServerConfig` | PUBLIC  
`TY_027` | `SparkProperties` | PUBLIC  
`TY_028` | `TestIamPermissionsRequest` | PUBLIC  
`TY_029` | `TestIamPermissionsResponse` | PUBLIC  
`TY_030` | `ConnectorConfigurationAsset` | PUBLIC  
`TY_031` | `ConnectorConfigurationNetwork` | PUBLIC  
`TY_032` | `ConnectorConfigurationPrivateServiceConnect` | PUBLIC  
`TY_T_001` | `AuditConfig` | PUBLIC  
`TY_T_002` | `AuditLogConfig` | PUBLIC  
`TY_T_006` | `Binding` | PUBLIC  
`TY_T_011` | `Connection` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250216 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://bigqueryconnection.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | bigqueryconnection:v1 | PUBLIC  
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
  
### CREATE_CONNECTIONS

  * Description: bigqueryconnection.projects.locations.connections.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONNECTIONID` | IMPORTING | `STRING` | connectionId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_011` | Connection  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Connection  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONNECTIONS

  * Description: bigqueryconnection.projects.locations.connections.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONNECTIONS

  * Description: bigqueryconnection.projects.locations.connections.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Connection  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_CONNECTIONS

  * Description: projects.locations.connections.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`IS_INPUT` | IMPORTING | `TY_019` | GetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONNECTIONS

  * Description: bigqueryconnection.projects.locations.connections.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | ListConnectionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CONNECTIONS

  * Description: bigqueryconnection.projects.locations.connections.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`IS_INPUT` | IMPORTING | `TY_011` | Connection  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | Connection  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_CONNECTIONS

  * Description: projects.locations.connections.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`IS_INPUT` | IMPORTING | `TY_025` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_CONNEC

  * Description: projects.locations.connections.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_CONNECTIONS_ID` | IMPORTING | `STRING` | connectionsId  
`IS_INPUT` | IMPORTING | `TY_028` | TestIamPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | TestIamPermissionsResponse  
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
