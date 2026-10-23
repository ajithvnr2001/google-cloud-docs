---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudasset_v1p5beta1/
title: Class /GOOG/CL_CLOUDASSET_V1P5BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:01.939582+00:00
---

# Class /GOOG/CL_CLOUDASSET_V1P5BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudasset_v1p5beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CLOUDASSET_V1P5BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_cloudasset_v1p5beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_cloudasset_v1p5beta1)



## Class
    
    
    /GOOG/CL_CLOUDASSET_V1P5BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Cloud Asset API v1p5beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Asset` | PUBLIC  
`TY_002` | `AuditConfig` | PUBLIC  
`TY_003` | `AuditLogConfig` | PUBLIC  
`TY_004` | `Binding` | PUBLIC  
`TY_005` | `Expr` | PUBLIC  
`TY_010` | `GoogleCloudOrgpolicyV1BooleanPolicy` | PUBLIC  
`TY_011` | `GoogleCloudOrgpolicyV1ListPolicy` | PUBLIC  
`TY_012` | `GoogleCloudOrgpolicyV1Policy` | PUBLIC  
`TY_014` | `GoogleIdentityAccesscontextmanagerV1AccessLevel` | PUBLIC  
`TY_015` | `GoogleIdentityAccesscontextmanagerV1AccessPolicy` | PUBLIC  
`TY_016` | `GoogleIdentityAccesscontextmanagerV1ApiOperation` | PUBLIC  
`TY_017` | `GoogleIdentityAccesscontextmanagerV1BasicLevel` | PUBLIC  
`TY_018` | `GoogleIdentityAccesscontextmanagerV1Condition` | PUBLIC  
`TY_019` | `GoogleIdentityAccesscontextmanagerV1CustomLevel` | PUBLIC  
`TY_020` | `GoogleIdentityAccesscontextmanagerV1DevicePolicy` | PUBLIC  
`TY_021` | `GoogleIdentityAccesscontextmanagerV1EgressFrom` | PUBLIC  
`TY_022` | `GoogleIdentityAccesscontextmanagerV1EgressPolicy` | PUBLIC  
`TY_023` | `GoogleIdentityAccesscontextmanagerV1EgressSource` | PUBLIC  
`TY_024` | `GoogleIdentityAccesscontextmanagerV1EgressTo` | PUBLIC  
`TY_025` | `GoogleIdentityAccesscontextmanagerV1IngressFrom` | PUBLIC  
`TY_026` | `GoogleIdentityAccesscontextmanagerV1IngressPolicy` | PUBLIC  
`TY_027` | `GoogleIdentityAccesscontextmanagerV1IngressSource` | PUBLIC  
`TY_028` | `GoogleIdentityAccesscontextmanagerV1IngressTo` | PUBLIC  
`TY_029` | `GoogleIdentityAccesscontextmanagerV1MethodSelector` | PUBLIC  
`TY_030` | `GoogleIdentityAccesscontextmanagerV1OsConstraint` | PUBLIC  
`TY_031` | `GoogleIdentityAccesscontextmanagerV1ServicePerimeter` | PUBLIC  
`TY_032` | `GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig` | PUBLIC  
`TY_033` | `GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices` | PUBLIC  
`TY_034` | `GoogleIdentityAccesscontextmanagerV1VpcNetworkSource` | PUBLIC  
`TY_035` | `GoogleIdentityAccesscontextmanagerV1VpcSubNetwork` | PUBLIC  
`TY_036` | `ListAssetsResponse` | PUBLIC  
`TY_037` | `Policy` | PUBLIC  
`TY_038` | `Resource` | PUBLIC  
`TY_T_001` | `Asset` | PUBLIC  
`TY_T_002` | `AuditConfig` | PUBLIC  
`TY_T_003` | `AuditLogConfig` | PUBLIC  
`TY_T_004` | `Binding` | PUBLIC  
`TY_T_012` | `GoogleCloudOrgpolicyV1Policy` | PUBLIC  
`TY_T_016` | `GoogleIdentityAccesscontextmanagerV1ApiOperation` | PUBLIC  
`TY_T_018` | `GoogleIdentityAccesscontextmanagerV1Condition` | PUBLIC  
`TY_T_022` | `GoogleIdentityAccesscontextmanagerV1EgressPolicy` | PUBLIC  
`TY_T_023` | `GoogleIdentityAccesscontextmanagerV1EgressSource` | PUBLIC  
`TY_T_026` | `GoogleIdentityAccesscontextmanagerV1IngressPolicy` | PUBLIC  
`TY_T_027` | `GoogleIdentityAccesscontextmanagerV1IngressSource` | PUBLIC  
`TY_T_029` | `GoogleIdentityAccesscontextmanagerV1MethodSelector` | PUBLIC  
`TY_T_030` | `GoogleIdentityAccesscontextmanagerV1OsConstraint` | PUBLIC  
`TY_T_034` | `GoogleIdentityAccesscontextmanagerV1VpcNetworkSource` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250228 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://cloudasset.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | cloudasset:v1p5beta1 | PUBLIC  
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
  
### LIST_ASSETS

  * Description: cloudasset.assets.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ASSETTYPES` | IMPORTING | `STRING` | assetTypes  
`IV_Q_CONTENTTYPE` | IMPORTING | `STRING` | contentType  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_READTIME` | IMPORTING | `STRING` | readTime  
`IV_P_V1P5BETA1ID` | IMPORTING | `STRING` | v1p5beta1Id  
`IV_P_V1P5BETA1ID1` | IMPORTING | `STRING` | v1p5beta1Id1  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | ListAssetsResponse  
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
