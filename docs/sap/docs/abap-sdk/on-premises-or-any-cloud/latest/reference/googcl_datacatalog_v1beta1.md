---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datacatalog_v1beta1/
title: Class /GOOG/CL_DATACATALOG_V1BETA1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:51.005675+00:00
---

# Class /GOOG/CL_DATACATALOG_V1BETA1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datacatalog_v1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DATACATALOG_V1BETA1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_datacatalog_v1beta1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_datacatalog_v1beta1)



## Class
    
    
    /GOOG/CL_DATACATALOG_V1BETA1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Cloud Data Catalog API v1beta1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Binding` | PUBLIC  
`TY_003` | `Expr` | PUBLIC  
`TY_004` | `GetIamPolicyRequest` | PUBLIC  
`TY_005` | `GetPolicyOptions` | PUBLIC  
`TY_069` | `GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse` | PUBLIC  
`TY_075` | `GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest` | PUBLIC  
`TY_076` | `GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse` | PUBLIC  
`TY_077` | `GoogleCloudDatacatalogV1beta1InlineSource` | PUBLIC  
`TY_080` | `GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse` | PUBLIC  
`TY_082` | `GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse` | PUBLIC  
`TY_083` | `GoogleCloudDatacatalogV1beta1PolicyTag` | PUBLIC  
`TY_091` | `GoogleCloudDatacatalogV1beta1SerializedPolicyTag` | PUBLIC  
`TY_092` | `GoogleCloudDatacatalogV1beta1SerializedTaxonomy` | PUBLIC  
`TY_093` | `GoogleCloudDatacatalogV1beta1SystemTimestamps` | PUBLIC  
`TY_100` | `GoogleCloudDatacatalogV1beta1Taxonomy` | PUBLIC  
`TY_101` | `GoogleCloudDatacatalogV1beta1TaxonomyService` | PUBLIC  
`TY_105` | `Policy` | PUBLIC  
`TY_106` | `SetIamPolicyRequest` | PUBLIC  
`TY_108` | `TestIamPermissionsRequest` | PUBLIC  
`TY_109` | `TestIamPermissionsResponse` | PUBLIC  
`TY_T_001` | `Binding` | PUBLIC  
`TY_T_083` | `GoogleCloudDatacatalogV1beta1PolicyTag` | PUBLIC  
`TY_T_091` | `GoogleCloudDatacatalogV1beta1SerializedPolicyTag` | PUBLIC  
`TY_T_092` | `GoogleCloudDatacatalogV1beta1SerializedTaxonomy` | PUBLIC  
`TY_T_100` | `GoogleCloudDatacatalogV1beta1Taxonomy` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250224 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://datacatalog.googleapis.com | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | IJIJWW | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | datacatalog:v1beta1 | PUBLIC  
  
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
  
### CREATE_POLICY_TAGS

  * Description: datacatalog.projects.locations.taxonomies.policyTags.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IS_INPUT` | IMPORTING | `TY_083` | GoogleCloudDatacatalogV1beta1PolicyTag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_083` | GoogleCloudDatacatalogV1beta1PolicyTag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_100` | GoogleCloudDatacatalogV1beta1Taxonomy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_100` | GoogleCloudDatacatalogV1beta1Taxonomy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_POLICY_TAGS

  * Description: datacatalog.projects.locations.taxonomies.policyTags.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXPORT_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.export 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SERIALIZEDTAXONOMIES` | IMPORTING | `STRING` | serializedTaxonomies  
`IV_Q_TAXONOMIES` | IMPORTING | `STRING` | taxonomies  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_069` | GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_POLICY_TAGS

  * Description: projects.locations.taxonomies.policyTags.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`IS_INPUT` | IMPORTING | `TY_004` | GetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_105` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_IAM_POLICY_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.getIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IS_INPUT` | IMPORTING | `TY_004` | GetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_105` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_POLICY_TAGS

  * Description: datacatalog.projects.locations.taxonomies.policyTags.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_083` | GoogleCloudDatacatalogV1beta1PolicyTag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_100` | GoogleCloudDatacatalogV1beta1Taxonomy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.import 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_075` | GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_076` | GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_POLICY_TAGS

  * Description: datacatalog.projects.locations.taxonomies.policyTags.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_080` | GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.list 
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
`ES_OUTPUT` | EXPORTING | `TY_082` | GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_POLICY_TAGS

  * Description: datacatalog.projects.locations.taxonomies.policyTags.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`IS_INPUT` | IMPORTING | `TY_083` | GoogleCloudDatacatalogV1beta1PolicyTag  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_083` | GoogleCloudDatacatalogV1beta1PolicyTag  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IS_INPUT` | IMPORTING | `TY_100` | GoogleCloudDatacatalogV1beta1Taxonomy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_100` | GoogleCloudDatacatalogV1beta1Taxonomy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_POLICY_TAGS

  * Description: projects.locations.taxonomies.policyTags.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`IS_INPUT` | IMPORTING | `TY_106` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_105` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SET_IAM_POLICY_TAXONOMIES

  * Description: datacatalog.projects.locations.taxonomies.setIamPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IS_INPUT` | IMPORTING | `TY_106` | SetIamPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_105` | Policy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_POLICY

  * Description: projects.locations.taxonomies.policyTags.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IV_P_POLICY_TAGS_ID` | IMPORTING | `STRING` | policyTagsId  
`IS_INPUT` | IMPORTING | `TY_108` | TestIamPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_109` | TestIamPermissionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TEST_IAM_PERMISSIONS_TAXONO

  * Description: projects.locations.taxonomies.testIamPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_TAXONOMIES_ID` | IMPORTING | `STRING` | taxonomiesId  
`IS_INPUT` | IMPORTING | `TY_108` | TestIamPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_109` | TestIamPermissionsResponse  
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
