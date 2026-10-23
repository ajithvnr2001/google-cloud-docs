---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_osconfig_v1beta/
title: Class /GOOG/CL_OSCONFIG_V1BETA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:54.584272+00:00
---

# Class /GOOG/CL_OSCONFIG_V1BETA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_osconfig_v1beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_OSCONFIG_V1BETA Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_osconfig_v1beta)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_osconfig_v1beta)



## Class
    
    
    /GOOG/CL_OSCONFIG_V1BETA

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`OS Config API v1beta`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `AptRepository` | PUBLIC  
`TY_002` | `AptSettings` | PUBLIC  
`TY_003` | `Assignment` | PUBLIC  
`TY_004` | `AssignmentGroupLabel` | PUBLIC  
`TY_005` | `AssignmentOsType` | PUBLIC  
`TY_007` | `EffectiveGuestPolicy` | PUBLIC  
`TY_008` | `EffectiveGuestPolicySourcedPackage` | PUBLIC  
`TY_009` | `EffectiveGuestPolicySourcedPackageRepository` | PUBLIC  
`TY_010` | `EffectiveGuestPolicySourcedSoftwareRecipe` | PUBLIC  
`TY_012` | `ExecStep` | PUBLIC  
`TY_013` | `ExecStepConfig` | PUBLIC  
`TY_014` | `ExecutePatchJobRequest` | PUBLIC  
`TY_015` | `FixedOrPercent` | PUBLIC  
`TY_016` | `GcsObject` | PUBLIC  
`TY_017` | `GooRepository` | PUBLIC  
`TY_019` | `GuestPolicy` | PUBLIC  
`TY_020` | `ListGuestPoliciesResponse` | PUBLIC  
`TY_021` | `ListPatchDeploymentsResponse` | PUBLIC  
`TY_022` | `ListPatchJobInstanceDetailsResponse` | PUBLIC  
`TY_023` | `ListPatchJobsResponse` | PUBLIC  
`TY_024` | `LookupEffectiveGuestPolicyRequest` | PUBLIC  
`TY_025` | `MonthlySchedule` | PUBLIC  
`TY_026` | `OneTimeSchedule` | PUBLIC  
`TY_027` | `Package` | PUBLIC  
`TY_028` | `PackageRepository` | PUBLIC  
`TY_029` | `PatchConfig` | PUBLIC  
`TY_030` | `PatchDeployment` | PUBLIC  
`TY_031` | `PatchInstanceFilter` | PUBLIC  
`TY_032` | `PatchInstanceFilterGroupLabel` | PUBLIC  
`TY_033` | `PatchJob` | PUBLIC  
`TY_034` | `PatchJobInstanceDetails` | PUBLIC  
`TY_035` | `PatchJobInstanceDetailsSummary` | PUBLIC  
`TY_036` | `PatchRollout` | PUBLIC  
`TY_038` | `RecurringSchedule` | PUBLIC  
`TY_040` | `SoftwareRecipe` | PUBLIC  
`TY_041` | `SoftwareRecipeArtifact` | PUBLIC  
`TY_042` | `SoftwareRecipeArtifactGcs` | PUBLIC  
`TY_043` | `SoftwareRecipeArtifactRemote` | PUBLIC  
`TY_044` | `SoftwareRecipeStep` | PUBLIC  
`TY_045` | `SoftwareRecipeStepCopyFile` | PUBLIC  
`TY_046` | `SoftwareRecipeStepExecFile` | PUBLIC  
`TY_047` | `SoftwareRecipeStepExtractArchive` | PUBLIC  
`TY_048` | `SoftwareRecipeStepInstallDpkg` | PUBLIC  
`TY_049` | `SoftwareRecipeStepInstallMsi` | PUBLIC  
`TY_050` | `SoftwareRecipeStepInstallRpm` | PUBLIC  
`TY_051` | `SoftwareRecipeStepRunScript` | PUBLIC  
`TY_052` | `TimeOfDay` | PUBLIC  
`TY_053` | `TimeZone` | PUBLIC  
`TY_054` | `WeekDayOfMonth` | PUBLIC  
`TY_055` | `WeeklySchedule` | PUBLIC  
`TY_056` | `WindowsUpdateSettings` | PUBLIC  
`TY_057` | `YumRepository` | PUBLIC  
`TY_058` | `YumSettings` | PUBLIC  
`TY_059` | `ZypperRepository` | PUBLIC  
`TY_060` | `ZypperSettings` | PUBLIC  
`TY_T_004` | `AssignmentGroupLabel` | PUBLIC  
`TY_T_005` | `AssignmentOsType` | PUBLIC  
`TY_T_008` | `EffectiveGuestPolicySourcedPackage` | PUBLIC  
`TY_T_009` | `EffectiveGuestPolicySourcedPackageRepository` | PUBLIC  
`TY_T_010` | `EffectiveGuestPolicySourcedSoftwareRecipe` | PUBLIC  
`TY_T_019` | `GuestPolicy` | PUBLIC  
`TY_T_027` | `Package` | PUBLIC  
`TY_T_028` | `PackageRepository` | PUBLIC  
`TY_T_030` | `PatchDeployment` | PUBLIC  
`TY_T_032` | `PatchInstanceFilterGroupLabel` | PUBLIC  
`TY_T_033` | `PatchJob` | PUBLIC  
`TY_T_034` | `PatchJobInstanceDetails` | PUBLIC  
`TY_T_040` | `SoftwareRecipe` | PUBLIC  
`TY_T_041` | `SoftwareRecipeArtifact` | PUBLIC  
`TY_T_044` | `SoftwareRecipeStep` | PUBLIC  
`TY_T_INT4` | `Table of Integers` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250302 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://osconfig.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | osconfig:v1beta | PUBLIC  
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
  
### CANCEL_PATCH_JOBS

  * Description: osconfig.projects.patchJobs.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_JOBS_ID` | IMPORTING | `STRING` | patchJobsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | PatchJob  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_GUEST_POLICIES

  * Description: osconfig.projects.guestPolicies.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_GUESTPOLICYID` | IMPORTING | `STRING` | guestPolicyId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_019` | GuestPolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | GuestPolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PATCHDEPLOYMENTID` | IMPORTING | `STRING` | patchDeploymentId  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_030` | PatchDeployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PatchDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_GUEST_POLICIES

  * Description: osconfig.projects.guestPolicies.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_GUEST_POLICIES_ID` | IMPORTING | `STRING` | guestPoliciesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_DEPLOYMENTS_ID` | IMPORTING | `STRING` | patchDeploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXECUTE_PATCH_JOBS

  * Description: osconfig.projects.patchJobs.execute 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_014` | ExecutePatchJobRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | PatchJob  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_GUEST_POLICIES

  * Description: osconfig.projects.guestPolicies.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_GUEST_POLICIES_ID` | IMPORTING | `STRING` | guestPoliciesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | GuestPolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_DEPLOYMENTS_ID` | IMPORTING | `STRING` | patchDeploymentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PatchDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PATCH_JOBS

  * Description: osconfig.projects.patchJobs.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_JOBS_ID` | IMPORTING | `STRING` | patchJobsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | PatchJob  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_GUEST_POLICIES

  * Description: osconfig.projects.guestPolicies.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | ListGuestPoliciesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_INSTANCE_DETAILS

  * Description: osconfig.projects.patchJobs.instanceDetails.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_JOBS_ID` | IMPORTING | `STRING` | patchJobsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | ListPatchJobInstanceDetailsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | ListPatchDeploymentsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PATCH_JOBS

  * Description: osconfig.projects.patchJobs.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | ListPatchJobsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LOOKUP_EFFECTIVE_GUEST_POLI

  * Description: projects.zones.instances.lookupEffectiveGuestPolicy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_ZONES_ID` | IMPORTING | `STRING` | zonesId  
`IV_P_INSTANCES_ID` | IMPORTING | `STRING` | instancesId  
`IS_INPUT` | IMPORTING | `TY_024` | LookupEffectiveGuestPolicyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | EffectiveGuestPolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_GUEST_POLICIES

  * Description: osconfig.projects.guestPolicies.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_GUEST_POLICIES_ID` | IMPORTING | `STRING` | guestPoliciesId  
`IS_INPUT` | IMPORTING | `TY_019` | GuestPolicy  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | GuestPolicy  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_DEPLOYMENTS_ID` | IMPORTING | `STRING` | patchDeploymentsId  
`IS_INPUT` | IMPORTING | `TY_030` | PatchDeployment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PatchDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PAUSE_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.pause 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_DEPLOYMENTS_ID` | IMPORTING | `STRING` | patchDeploymentsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PatchDeployment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_PATCH_DEPLOYMENTS

  * Description: osconfig.projects.patchDeployments.resume 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_PATCH_DEPLOYMENTS_ID` | IMPORTING | `STRING` | patchDeploymentsId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PatchDeployment  
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
