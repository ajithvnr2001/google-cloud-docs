---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_drive_v3/
title: Class /GOOG/CL_DRIVE_V3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:17.855015+00:00
---

# Class /GOOG/CL_DRIVE_V3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_drive_v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DRIVE_V3 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_drive_v3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_drive_v3)



## Class
    
    
    /GOOG/CL_DRIVE_V3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Drive API v3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `About` | PUBLIC  
`TY_002` | `Change` | PUBLIC  
`TY_003` | `ChangeList` | PUBLIC  
`TY_004` | `Channel` | PUBLIC  
`TY_005` | `Comment` | PUBLIC  
`TY_006` | `CommentList` | PUBLIC  
`TY_007` | `ContentRestriction` | PUBLIC  
`TY_008` | `Drive` | PUBLIC  
`TY_009` | `DriveList` | PUBLIC  
`TY_010` | `File` | PUBLIC  
`TY_011` | `FileList` | PUBLIC  
`TY_012` | `GeneratedIds` | PUBLIC  
`TY_013` | `Label` | PUBLIC  
`TY_014` | `LabelField` | PUBLIC  
`TY_015` | `LabelFieldModification` | PUBLIC  
`TY_016` | `LabelList` | PUBLIC  
`TY_017` | `LabelModification` | PUBLIC  
`TY_018` | `ModifyLabelsRequest` | PUBLIC  
`TY_019` | `ModifyLabelsResponse` | PUBLIC  
`TY_020` | `Permission` | PUBLIC  
`TY_021` | `PermissionList` | PUBLIC  
`TY_022` | `Reply` | PUBLIC  
`TY_023` | `ReplyList` | PUBLIC  
`TY_024` | `Revision` | PUBLIC  
`TY_025` | `RevisionList` | PUBLIC  
`TY_026` | `StartPageToken` | PUBLIC  
`TY_027` | `TeamDrive` | PUBLIC  
`TY_028` | `TeamDriveList` | PUBLIC  
`TY_029` | `User` | PUBLIC  
`TY_030` | `DriveThemes` | PUBLIC  
`TY_031` | `StorageQuota` | PUBLIC  
`TY_032` | `TeamDriveThemes` | PUBLIC  
`TY_051` | `QuotedFileContent` | PUBLIC  
`TY_052` | `BackgroundImageFile` | PUBLIC  
`TY_053` | `Capabilities` | PUBLIC  
`TY_054` | `Restrictions` | PUBLIC  
`TY_055` | `Capabilities` | PUBLIC  
`TY_056` | `Thumbnail` | PUBLIC  
`TY_057` | `ContentHints` | PUBLIC  
`TY_058` | `Location` | PUBLIC  
`TY_059` | `ImageMediaMetadata` | PUBLIC  
`TY_060` | `LabelInfo` | PUBLIC  
`TY_061` | `LinkShareMetadata` | PUBLIC  
`TY_064` | `ShortcutDetails` | PUBLIC  
`TY_065` | `VideoMediaMetadata` | PUBLIC  
`TY_066` | `PermissionDetails` | PUBLIC  
`TY_067` | `TeamDrivePermissionDetails` | PUBLIC  
`TY_068` | `BackgroundImageFile` | PUBLIC  
`TY_069` | `Capabilities` | PUBLIC  
`TY_070` | `Restrictions` | PUBLIC  
`TY_071` | `App` | PUBLIC  
`TY_072` | `AppIcons` | PUBLIC  
`TY_073` | `AppList` | PUBLIC  
`TY_074` | `AccessProposal` | PUBLIC  
`TY_075` | `AccessProposalRoleAndView` | PUBLIC  
`TY_076` | `ListAccessProposalsResponse` | PUBLIC  
`TY_077` | `ListOperationsResponse` | PUBLIC  
`TY_078` | `Operation` | PUBLIC  
`TY_079` | `ResolveAccessProposalRequest` | PUBLIC  
`TY_080` | `Status` | PUBLIC  
`TY_T_002` | `Change` | PUBLIC  
`TY_T_005` | `Comment` | PUBLIC  
`TY_T_007` | `ContentRestriction` | PUBLIC  
`TY_T_008` | `Drive` | PUBLIC  
`TY_T_010` | `File` | PUBLIC  
`TY_T_013` | `Label` | PUBLIC  
`TY_T_015` | `LabelFieldModification` | PUBLIC  
`TY_T_017` | `LabelModification` | PUBLIC  
`TY_T_020` | `Permission` | PUBLIC  
`TY_T_022` | `Reply` | PUBLIC  
`TY_T_024` | `Revision` | PUBLIC  
`TY_T_027` | `TeamDrive` | PUBLIC  
`TY_T_029` | `User` | PUBLIC  
`TY_T_030` | `DriveThemes` | PUBLIC  
`TY_T_032` | `TeamDriveThemes` | PUBLIC  
`TY_T_066` | `PermissionDetails` | PUBLIC  
`TY_T_067` | `TeamDrivePermissionDetails` | PUBLIC  
`TY_T_071` | `App` | PUBLIC  
`TY_T_072` | `AppIcons` | PUBLIC  
`TY_T_074` | `AccessProposal` | PUBLIC  
`TY_T_075` | `AccessProposalRoleAndView` | PUBLIC  
`TY_T_078` | `Operation` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /drive/v3/ | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241119 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://www.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | drive:v3 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | OOIJWW | PUBLIC  
  
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
  
### ADD_MULTIPART

  * Description: Add Multipart 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_BODY` | IMPORTING | `STRING` | Body  
`IV_XBODY` | IMPORTING | `XSTRING` | Body  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CANCEL_OPERATION

  * Description: drive.operation.cancel 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_NAME` | IMPORTING | `STRING` | name  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### COPY_FILES

  * Description: drive.files.copy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_IGNOREDEFAULTVISIBILITY` | IMPORTING | `STRING` | ignoreDefaultVisibility  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_KEEPREVISIONFOREVER` | IMPORTING | `STRING` | keepRevisionForever  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_010` | File  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_COMMENTS

  * Description: drive.comments.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_005` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_DRIVES

  * Description: drive.drives.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IS_INPUT` | IMPORTING | `TY_008` | Drive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_FILES

  * Description: drive.files.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_IGNOREDEFAULTVISIBILITY` | IMPORTING | `STRING` | ignoreDefaultVisibility  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_KEEPREVISIONFOREVER` | IMPORTING | `STRING` | keepRevisionForever  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USECONTENTASINDEXABLETEXT` | IMPORTING | `STRING` | useContentAsIndexableText  
`IS_INPUT` | IMPORTING | `TY_010` | File  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_CHUNK_SIZE` | IMPORTING | `I` | Chunk Size  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_PERMISSIONS

  * Description: drive.permissions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_EMAILMESSAGE` | IMPORTING | `STRING` | emailMessage  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_MOVETONEWOWNERSROOT` | IMPORTING | `STRING` | moveToNewOwnersRoot  
`IV_Q_SENDNOTIFICATIONEMAIL` | IMPORTING | `STRING` | sendNotificationEmail  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TRANSFEROWNERSHIP` | IMPORTING | `STRING` | transferOwnership  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_020` | Permission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_REPLIES

  * Description: drive.replies.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_022` | Reply  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | Reply  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_TEAMDRIVES

  * Description: drive.teamdrives.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IS_INPUT` | IMPORTING | `TY_027` | TeamDrive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | TeamDrive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_COMMENTS

  * Description: drive.comments.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_DRIVES

  * Description: drive.drives.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWITEMDELETION` | IMPORTING | `STRING` | allowItemDeletion  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_DRIVE_ID` | IMPORTING | `STRING` | driveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_FILES

  * Description: drive.files.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_OPERATION

  * Description: drive.operation.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_NAME` | IMPORTING | `STRING` | name  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_PERMISSIONS

  * Description: drive.permissions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_REPLIES

  * Description: drive.replies.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REPLY_ID` | IMPORTING | `STRING` | replyId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_REVISIONS

  * Description: drive.revisions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REVISION_ID` | IMPORTING | `STRING` | revisionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_TEAMDRIVES

  * Description: drive.teamdrives.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_TEAM_DRIVE_ID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DOWNLOAD_FILES

  * Description: drive.files.download 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MIMETYPE` | IMPORTING | `STRING` | mimeType  
`IV_Q_REVISIONID` | IMPORTING | `STRING` | revisionId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_078` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EMPTY_TRASH_FILES

  * Description: drive.files.emptyTrash 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### EXPORT_FILES

  * Description: drive.files.export 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MIMETYPE` | IMPORTING | `STRING` | mimeType  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GENERATE_IDS_FILES

  * Description: drive.files.generateIds 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_COUNT` | IMPORTING | `STRING` | count  
`IV_Q_SPACE` | IMPORTING | `STRING` | space  
`IV_Q_TYPE` | IMPORTING | `STRING` | type  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | GeneratedIds  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ABOUT

  * Description: drive.about.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | About  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ACCESSPROPOSALS

  * Description: drive.accessproposals.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPOSAL_ID` | IMPORTING | `STRING` | proposalId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_074` | AccessProposal  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_APPS

  * Description: drive.apps.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_APP_ID` | IMPORTING | `STRING` | appId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | App  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_COMMENTS

  * Description: drive.comments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_DRIVES

  * Description: drive.drives.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_DRIVE_ID` | IMPORTING | `STRING` | driveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_FILES

  * Description: drive.files.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACKNOWLEDGEABUSE` | IMPORTING | `STRING` | acknowledgeAbuse  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_OPERATIONS

  * Description: drive.operations.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_NAME` | IMPORTING | `STRING` | name  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_078` | Operation  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PERMISSIONS

  * Description: drive.permissions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_REPLIES

  * Description: drive.replies.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REPLY_ID` | IMPORTING | `STRING` | replyId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | Reply  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_REVISIONS

  * Description: drive.revisions.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACKNOWLEDGEABUSE` | IMPORTING | `STRING` | acknowledgeAbuse  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REVISION_ID` | IMPORTING | `STRING` | revisionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Revision  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_START_PAGE_TOKEN_CHANGE

  * Description: drive.changes.getStartPageToken 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | StartPageToken  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_TEAMDRIVES

  * Description: drive.teamdrives.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_TEAM_DRIVE_ID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | TeamDrive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### HIDE_DRIVES

  * Description: drive.drives.hide 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DRIVE_ID` | IMPORTING | `STRING` | driveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ACCESSPROPOSALS

  * Description: drive.accessproposals.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_076` | ListAccessProposalsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_APPS

  * Description: drive.apps.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_APPFILTEREXTENSIONS` | IMPORTING | `STRING` | appFilterExtensions  
`IV_Q_APPFILTERMIMETYPES` | IMPORTING | `STRING` | appFilterMimeTypes  
`IV_Q_LANGUAGECODE` | IMPORTING | `STRING` | languageCode  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_073` | AppList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CHANGES

  * Description: drive.changes.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_INCLUDECORPUSREMOVALS` | IMPORTING | `STRING` | includeCorpusRemovals  
`IV_Q_INCLUDEITEMSFROMALLDRIVES` | IMPORTING | `STRING` | includeItemsFromAllDrives  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_INCLUDEREMOVED` | IMPORTING | `STRING` | includeRemoved  
`IV_Q_INCLUDETEAMDRIVEITEMS` | IMPORTING | `STRING` | includeTeamDriveItems  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_RESTRICTTOMYDRIVE` | IMPORTING | `STRING` | restrictToMyDrive  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | ChangeList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_COMMENTS

  * Description: drive.comments.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_STARTMODIFIEDTIME` | IMPORTING | `STRING` | startModifiedTime  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | CommentList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_DRIVES

  * Description: drive.drives.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | DriveList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_FILES

  * Description: drive.files.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CORPORA` | IMPORTING | `STRING` | corpora  
`IV_Q_CORPUS` | IMPORTING | `STRING` | corpus  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_INCLUDEITEMSFROMALLDRIVES` | IMPORTING | `STRING` | includeItemsFromAllDrives  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_INCLUDETEAMDRIVEITEMS` | IMPORTING | `STRING` | includeTeamDriveItems  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | FileList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_LABELS_FILES

  * Description: drive.files.listLabels 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | LabelList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_OPERATIONS

  * Description: drive.operations.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_NAME` | IMPORTING | `STRING` | name  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_077` | ListOperationsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PERMISSIONS

  * Description: drive.permissions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_021` | PermissionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_REPLIES

  * Description: drive.replies.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_023` | ReplyList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_REVISIONS

  * Description: drive.revisions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | RevisionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_TEAMDRIVES

  * Description: drive.teamdrives.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | TeamDriveList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MODIFY_LABELS_FILES

  * Description: drive.files.modifyLabels 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_018` | ModifyLabelsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_019` | ModifyLabelsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESOLVE_ACCESSPROPOSALS

  * Description: drive.accessproposals.resolve 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPOSAL_ID` | IMPORTING | `STRING` | proposalId  
`IS_INPUT` | IMPORTING | `TY_079` | ResolveAccessProposalRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD

  * Description: Resume Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_SESSION_ID` | IMPORTING | `STRING` | Resumable Session Id  
`IV_START_BYTE` | IMPORTING | `I` | Start Byte to upload  
`IV_LAST_BYTE` | IMPORTING | `I` | Last Byte to upload  
`IV_TOT_BYTES` | IMPORTING | `I` | Total Bytes to upload  
`EV_LAST_BYTE` | EXPORTING | `I` | Last Byte to uploaded  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_CREATE_REQ

  * Description: Resume Upload Create Request 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_SESSION_ID` | IMPORTING | `STRING` | Resumable Session Id  
`EO_HTTP_CLIENT` | EXPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_HANDLE_RES

  * Description: Resume Upload Handle Response 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
`EV_LAST_BYTE` | EXPORTING | `I` | Last Byte uploaded  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_RECEIVE_RES

  * Description: Resume Upload Receive Response 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### RESUME_UPLOAD_SEND_REQ

  * Description: Resume Upload Send Request 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IO_HTTP_CLIENT` | IMPORTING | `IF_HTTP_CLIENT` | HTTP Client Abstraction  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_CHANNELS

  * Description: drive.channels.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_004` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNHIDE_DRIVES

  * Description: drive.drives.unhide 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_DRIVE_ID` | IMPORTING | `STRING` | driveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_COMMENTS

  * Description: drive.comments.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_005` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_DRIVES

  * Description: drive.drives.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_DRIVE_ID` | IMPORTING | `STRING` | driveId  
`IS_INPUT` | IMPORTING | `TY_008` | Drive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_FILES

  * Description: drive.files.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADDPARENTS` | IMPORTING | `STRING` | addParents  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_KEEPREVISIONFOREVER` | IMPORTING | `STRING` | keepRevisionForever  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_REMOVEPARENTS` | IMPORTING | `STRING` | removeParents  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USECONTENTASINDEXABLETEXT` | IMPORTING | `STRING` | useContentAsIndexableText  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_010` | File  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_CHUNK_SIZE` | IMPORTING | `I` | Chunk Size  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_PERMISSIONS

  * Description: drive.permissions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REMOVEEXPIRATION` | IMPORTING | `STRING` | removeExpiration  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TRANSFEROWNERSHIP` | IMPORTING | `STRING` | transferOwnership  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`IS_INPUT` | IMPORTING | `TY_020` | Permission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_REPLIES

  * Description: drive.replies.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REPLY_ID` | IMPORTING | `STRING` | replyId  
`IS_INPUT` | IMPORTING | `TY_022` | Reply  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_022` | Reply  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_REVISIONS

  * Description: drive.revisions.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REVISION_ID` | IMPORTING | `STRING` | revisionId  
`IS_INPUT` | IMPORTING | `TY_024` | Revision  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_024` | Revision  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_TEAMDRIVES

  * Description: drive.teamdrives.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_TEAM_DRIVE_ID` | IMPORTING | `STRING` | teamDriveId  
`IS_INPUT` | IMPORTING | `TY_027` | TeamDrive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | TeamDrive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_FILES_MULTIPART

  * Description: Multipart Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_URI` | IMPORTING | `STRING` | URI  
`IS_INPUT` | IMPORTING | `TY_010` | File  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_METHOD_ID` | IMPORTING | `STRING` | Method ID  
`IV_HTTP_METHOD` | IMPORTING | `STRING` | HTTP Method  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_FILES_RESUMABLE

  * Description: Resumable Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_URI` | IMPORTING | `STRING` | Input URI  
`IS_INPUT` | IMPORTING | `TY_010` | File  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_CHUNK_SIZE` | IMPORTING | `I` | Chunk Size  
`IV_METHOD_ID` | IMPORTING | `STRING` | Method ID  
`IV_HTTP_METHOD` | IMPORTING | `STRING` | HTTP Method  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_FILES_SIMPLE

  * Description: Simple Upload 
  * Visibility: PROTECTED 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_URI` | IMPORTING | `STRING` | URI  
`IS_DATA` | IMPORTING | `XSTRING` | Input Data  
`IV_CONTENT_TYPE` | IMPORTING | `STRING` | Content Type  
`IV_HTTP_METHOD` | IMPORTING | `STRING` | HTTP Method  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_CHANGES

  * Description: drive.changes.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_INCLUDECORPUSREMOVALS` | IMPORTING | `STRING` | includeCorpusRemovals  
`IV_Q_INCLUDEITEMSFROMALLDRIVES` | IMPORTING | `STRING` | includeItemsFromAllDrives  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_INCLUDEREMOVED` | IMPORTING | `STRING` | includeRemoved  
`IV_Q_INCLUDETEAMDRIVEITEMS` | IMPORTING | `STRING` | includeTeamDriveItems  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_RESTRICTTOMYDRIVE` | IMPORTING | `STRING` | restrictToMyDrive  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`IS_INPUT` | IMPORTING | `TY_004` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Channel  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_FILES

  * Description: drive.files.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ACKNOWLEDGEABUSE` | IMPORTING | `STRING` | acknowledgeAbuse  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_004` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Channel  
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
