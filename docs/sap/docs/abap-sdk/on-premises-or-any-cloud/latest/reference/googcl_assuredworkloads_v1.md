---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_assuredworkloads_v1/
title: Class /GOOG/CL_ASSUREDWORKLOADS_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:13.805292+00:00
---

# Class /GOOG/CL_ASSUREDWORKLOADS_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_assuredworkloads_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ASSUREDWORKLOADS_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_assuredworkloads_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_assuredworkloads_v1)



## Class
    
    
    /GOOG/CL_ASSUREDWORKLOADS_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Assured Workloads API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequest` | PUBLIC  
`TY_003` | `GoogleCloudAssuredworkloadsV1ListViolationsResponse` | PUBLIC  
`TY_004` | `GoogleCloudAssuredworkloadsV1ListWorkloadsResponse` | PUBLIC  
`TY_005` | `GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequest` | PUBLIC  
`TY_006` | `GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest` | PUBLIC  
`TY_008` | `GoogleCloudAssuredworkloadsV1Violation` | PUBLIC  
`TY_009` | `GoogleCloudAssuredworkloadsV1ViolationExceptionContext` | PUBLIC  
`TY_010` | `GoogleCloudAssuredworkloadsV1ViolationRemediation` | PUBLIC  
`TY_011` | `GoogleCloudAssuredworkloadsV1ViolationRemediationInstruction` | PUBLIC  
`TY_012` | `GoogleCloudAssuredworkloadsV1ViolationRemediationInstruction` | PUBLIC  
`TY_013` | `GoogleCloudAssuredworkloadsV1ViolationRemediationInstruction` | PUBLIC  
`TY_014` | `GoogleCloudAssuredworkloadsV1Workload` | PUBLIC  
`TY_015` | `GoogleCloudAssuredworkloadsV1WorkloadComplianceStatus` | PUBLIC  
`TY_016` | `GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponse` | PUBLIC  
`TY_017` | `GoogleCloudAssuredworkloadsV1WorkloadKMSSettings` | PUBLIC  
`TY_018` | `GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissions` | PUBLIC  
`TY_019` | `GoogleCloudAssuredworkloadsV1WorkloadResourceInfo` | PUBLIC  
`TY_020` | `GoogleCloudAssuredworkloadsV1WorkloadResourceSettings` | PUBLIC  
`TY_021` | `GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponse` | PUBLIC  
`TY_022` | `GoogleLongrunningListOperationsResponse` | PUBLIC  
`TY_023` | `GoogleLongrunningOperation` | PUBLIC  
`TY_025` | `GoogleRpcStatus` | PUBLIC  
`TY_026` | `GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponse` | PUBLIC  
`TY_027` | `GoogleCloudAssuredworkloadsV1AssetMoveAnalysis` | PUBLIC  
`TY_029` | `GoogleCloudAssuredworkloadsV1MoveAnalysisGroup` | PUBLIC  
`TY_030` | `GoogleCloudAssuredworkloadsV1MoveAnalysisResult` | PUBLIC  
`TY_031` | `GoogleCloudAssuredworkloadsV1MoveImpact` | PUBLIC  
`TY_032` | `GoogleCloudAssuredworkloadsV1WorkloadWorkloadOptions` | PUBLIC  
`TY_T_008` | `GoogleCloudAssuredworkloadsV1Violation` | PUBLIC  
`TY_T_009` | `GoogleCloudAssuredworkloadsV1ViolationExceptionContext` | PUBLIC  
`TY_T_014` | `GoogleCloudAssuredworkloadsV1Workload` | PUBLIC  
`TY_T_019` | `GoogleCloudAssuredworkloadsV1WorkloadResourceInfo` | PUBLIC  
`TY_T_020` | `GoogleCloudAssuredworkloadsV1WorkloadResourceSettings` | PUBLIC  
`TY_T_023` | `GoogleLongrunningOperation` | PUBLIC  
`TY_T_027` | `GoogleCloudAssuredworkloadsV1AssetMoveAnalysis` | PUBLIC  
`TY_T_029` | `GoogleCloudAssuredworkloadsV1MoveAnalysisGroup` | PUBLIC  
`TY_T_031` | `GoogleCloudAssuredworkloadsV1MoveImpact` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250220 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://assuredworkloads.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | assuredworkloads:v1 | PUBLIC  
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
  
### ACKNOWLEDGE_VIOLATIONS

  * Description: organizations.locations.workloads.violations.acknowledge 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`IV_P_VIOLATIONS_ID` | IMPORTING | `STRING` | violationsId  
`IS_INPUT` | IMPORTING | `TY_001` | GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ANALYZE_WORKLOAD_MOVE_WORKL

  * Description: organizations.locations.workloads.analyzeWorkloadMove 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ASSETTYPES` | IMPORTING | `STRING` | assetTypes  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PROJECT` | IMPORTING | `STRING` | project  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_WORKLOADS

  * Description: assuredworkloads.organizations.locations.workloads.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_EXTERNALID` | IMPORTING | `STRING` | externalId  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IS_INPUT` | IMPORTING | `TY_014` | GoogleCloudAssuredworkloadsV1Workload  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_WORKLOADS

  * Description: assuredworkloads.organizations.locations.workloads.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ETAG` | IMPORTING | `STRING` | etag  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### ENABLE_RESOURCE_MONITORING

  * Description: organizations.locations.workloads.enableResourceMonitoring 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: assuredworkloads.organizations.locations.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_OPERATIONS_ID` | IMPORTING | `STRING` | operationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | GoogleLongrunningOperation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_VIOLATIONS

  * Description: organizations.locations.workloads.violations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`IV_P_VIOLATIONS_ID` | IMPORTING | `STRING` | violationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | GoogleCloudAssuredworkloadsV1Violation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_WORKLOADS

  * Description: assuredworkloads.organizations.locations.workloads.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | GoogleCloudAssuredworkloadsV1Workload  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: assuredworkloads.organizations.locations.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | GoogleLongrunningListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_VIOLATIONS

  * Description: organizations.locations.workloads.violations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_INTERVALENDTIME` | IMPORTING | `STRING` | interval.endTime  
`IV_Q_INTERVALSTARTTIME` | IMPORTING | `STRING` | interval.startTime  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | GoogleCloudAssuredworkloadsV1ListViolationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_WORKLOADS

  * Description: assuredworkloads.organizations.locations.workloads.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | GoogleCloudAssuredworkloadsV1ListWorkloadsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MUTATE_PARTNER_PERMISSIONS

  * Description: organizations.locations.workloads.mutatePartnerPermissions 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`IS_INPUT` | IMPORTING | `TY_005` | GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | GoogleCloudAssuredworkloadsV1Workload  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_WORKLOADS

  * Description: assuredworkloads.organizations.locations.workloads.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`IS_INPUT` | IMPORTING | `TY_014` | GoogleCloudAssuredworkloadsV1Workload  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | GoogleCloudAssuredworkloadsV1Workload  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESTRICT_ALLOWED_RESOURCES

  * Description: organizations.locations.workloads.restrictAllowedResources 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_LOCATIONS_ID` | IMPORTING | `STRING` | locationsId  
`IV_P_WORKLOADS_ID` | IMPORTING | `STRING` | workloadsId  
`IS_INPUT` | IMPORTING | `TY_006` | GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
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
