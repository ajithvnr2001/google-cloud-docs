---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_essentialcontacts_v1/
title: Class /GOOG/CL_ESSENTIALCONTACTS_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:24.531557+00:00
---

# Class /GOOG/CL_ESSENTIALCONTACTS_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_essentialcontacts_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_ESSENTIALCONTACTS_V1 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_essentialcontacts_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_essentialcontacts_v1)



## Class
    
    
    /GOOG/CL_ESSENTIALCONTACTS_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Essential Contacts API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `GoogleCloudEssentialcontactsV1ComputeContactsResponse` | PUBLIC  
`TY_002` | `GoogleCloudEssentialcontactsV1Contact` | PUBLIC  
`TY_003` | `GoogleCloudEssentialcontactsV1ListContactsResponse` | PUBLIC  
`TY_004` | `GoogleCloudEssentialcontactsV1SendTestMessageRequest` | PUBLIC  
`TY_T_002` | `GoogleCloudEssentialcontactsV1Contact` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250224 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://essentialcontacts.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | essentialcontacts:v1 | PUBLIC  
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
  
### COMPUTE_CONTACTS

  * Description: essentialcontacts.folders.contacts.compute 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NOTIFICATIONCATEGORIES` | IMPORTING | `STRING` | notificationCategories  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudEssentialcontactsV1ComputeContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COMPUTE_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.compute 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NOTIFICATIONCATEGORIES` | IMPORTING | `STRING` | notificationCategories  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudEssentialcontactsV1ComputeContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COMPUTE_CONTACTS2

  * Description: essentialcontacts.projects.contacts.compute 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NOTIFICATIONCATEGORIES` | IMPORTING | `STRING` | notificationCategories  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | GoogleCloudEssentialcontactsV1ComputeContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CONTACTS

  * Description: essentialcontacts.folders.contacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_CONTACTS2

  * Description: essentialcontacts.projects.contacts.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONTACTS

  * Description: essentialcontacts.folders.contacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CONTACTS2

  * Description: essentialcontacts.projects.contacts.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTACTS

  * Description: essentialcontacts.folders.contacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CONTACTS2

  * Description: essentialcontacts.projects.contacts.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONTACTS

  * Description: essentialcontacts.folders.contacts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | GoogleCloudEssentialcontactsV1ListContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | GoogleCloudEssentialcontactsV1ListContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CONTACTS2

  * Description: essentialcontacts.projects.contacts.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | GoogleCloudEssentialcontactsV1ListContactsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CONTACTS

  * Description: essentialcontacts.folders.contacts.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CONTACTS2

  * Description: essentialcontacts.projects.contacts.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IV_P_CONTACTS_ID` | IMPORTING | `STRING` | contactsId  
`IS_INPUT` | IMPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | GoogleCloudEssentialcontactsV1Contact  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEND_TEST_MESSAGE_CONTACTS

  * Description: essentialcontacts.folders.contacts.sendTestMessage 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FOLDERS_ID` | IMPORTING | `STRING` | foldersId  
`IS_INPUT` | IMPORTING | `TY_004` | GoogleCloudEssentialcontactsV1SendTestMessageRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEND_TEST_MESSAGE_CONTACTS1

  * Description: essentialcontacts.organizations.contacts.sendTestMessage 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_ORGANIZATIONS_ID` | IMPORTING | `STRING` | organizationsId  
`IS_INPUT` | IMPORTING | `TY_004` | GoogleCloudEssentialcontactsV1SendTestMessageRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEND_TEST_MESSAGE_CONTACTS2

  * Description: essentialcontacts.projects.contacts.sendTestMessage 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_PROJECTS_ID` | IMPORTING | `STRING` | projectsId  
`IS_INPUT` | IMPORTING | `TY_004` | GoogleCloudEssentialcontactsV1SendTestMessageRequest  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
