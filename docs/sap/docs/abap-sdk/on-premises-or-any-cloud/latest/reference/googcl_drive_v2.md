---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_drive_v2/
title: Class /GOOG/CL_DRIVE_V2 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:59:23.102165+00:00
---

# Class /GOOG/CL_DRIVE_V2  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_drive_v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_DRIVE_V2 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_drive_v2)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_drive_v2)



## Class
    
    
    /GOOG/CL_DRIVE_V2

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Drive API v2`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `About` | PUBLIC  
`TY_002` | `App` | PUBLIC  
`TY_003` | `AppList` | PUBLIC  
`TY_004` | `Change` | PUBLIC  
`TY_005` | `ChangeList` | PUBLIC  
`TY_006` | `Channel` | PUBLIC  
`TY_007` | `ChildList` | PUBLIC  
`TY_008` | `ChildReference` | PUBLIC  
`TY_009` | `Comment` | PUBLIC  
`TY_010` | `CommentList` | PUBLIC  
`TY_011` | `CommentReply` | PUBLIC  
`TY_012` | `CommentReplyList` | PUBLIC  
`TY_013` | `ContentRestriction` | PUBLIC  
`TY_014` | `Drive` | PUBLIC  
`TY_015` | `DriveList` | PUBLIC  
`TY_016` | `File` | PUBLIC  
`TY_017` | `FileList` | PUBLIC  
`TY_018` | `GeneratedIds` | PUBLIC  
`TY_019` | `Label` | PUBLIC  
`TY_020` | `LabelField` | PUBLIC  
`TY_021` | `LabelFieldModification` | PUBLIC  
`TY_022` | `LabelList` | PUBLIC  
`TY_023` | `LabelModification` | PUBLIC  
`TY_024` | `ModifyLabelsRequest` | PUBLIC  
`TY_025` | `ModifyLabelsResponse` | PUBLIC  
`TY_026` | `ParentList` | PUBLIC  
`TY_027` | `ParentReference` | PUBLIC  
`TY_028` | `Permission` | PUBLIC  
`TY_029` | `PermissionId` | PUBLIC  
`TY_030` | `PermissionList` | PUBLIC  
`TY_031` | `Property` | PUBLIC  
`TY_032` | `PropertyList` | PUBLIC  
`TY_033` | `Revision` | PUBLIC  
`TY_034` | `RevisionList` | PUBLIC  
`TY_035` | `StartPageToken` | PUBLIC  
`TY_036` | `TeamDrive` | PUBLIC  
`TY_037` | `TeamDriveList` | PUBLIC  
`TY_038` | `User` | PUBLIC  
`TY_039` | `RoleSets` | PUBLIC  
`TY_040` | `AdditionalRoleInfo` | PUBLIC  
`TY_041` | `DriveThemes` | PUBLIC  
`TY_042` | `ExportFormats` | PUBLIC  
`TY_043` | `Features` | PUBLIC  
`TY_044` | `ImportFormats` | PUBLIC  
`TY_045` | `MaxUploadSizes` | PUBLIC  
`TY_046` | `QuotaBytesByService` | PUBLIC  
`TY_047` | `TeamDriveThemes` | PUBLIC  
`TY_050` | `Icons` | PUBLIC  
`TY_106` | `Context` | PUBLIC  
`TY_108` | `BackgroundImageFile` | PUBLIC  
`TY_109` | `Capabilities` | PUBLIC  
`TY_110` | `Restrictions` | PUBLIC  
`TY_111` | `Capabilities` | PUBLIC  
`TY_113` | `Location` | PUBLIC  
`TY_114` | `ImageMediaMetadata` | PUBLIC  
`TY_115` | `IndexableText` | PUBLIC  
`TY_116` | `LabelInfo` | PUBLIC  
`TY_117` | `Labels` | PUBLIC  
`TY_119` | `LinkShareMetadata` | PUBLIC  
`TY_124` | `ShortcutDetails` | PUBLIC  
`TY_125` | `Thumbnail` | PUBLIC  
`TY_129` | `VideoMediaMetadata` | PUBLIC  
`TY_130` | `PermissionDetails` | PUBLIC  
`TY_131` | `TeamDrivePermissionDetails` | PUBLIC  
`TY_134` | `Picture` | PUBLIC  
`TY_135` | `BackgroundImageFile` | PUBLIC  
`TY_136` | `Capabilities` | PUBLIC  
`TY_137` | `Restrictions` | PUBLIC  
`TY_T_002` | `App` | PUBLIC  
`TY_T_004` | `Change` | PUBLIC  
`TY_T_008` | `ChildReference` | PUBLIC  
`TY_T_009` | `Comment` | PUBLIC  
`TY_T_011` | `CommentReply` | PUBLIC  
`TY_T_013` | `ContentRestriction` | PUBLIC  
`TY_T_014` | `Drive` | PUBLIC  
`TY_T_016` | `File` | PUBLIC  
`TY_T_019` | `Label` | PUBLIC  
`TY_T_021` | `LabelFieldModification` | PUBLIC  
`TY_T_023` | `LabelModification` | PUBLIC  
`TY_T_027` | `ParentReference` | PUBLIC  
`TY_T_028` | `Permission` | PUBLIC  
`TY_T_031` | `Property` | PUBLIC  
`TY_T_033` | `Revision` | PUBLIC  
`TY_T_036` | `TeamDrive` | PUBLIC  
`TY_T_038` | `User` | PUBLIC  
`TY_T_039` | `RoleSets` | PUBLIC  
`TY_T_040` | `AdditionalRoleInfo` | PUBLIC  
`TY_T_041` | `DriveThemes` | PUBLIC  
`TY_T_042` | `ExportFormats` | PUBLIC  
`TY_T_043` | `Features` | PUBLIC  
`TY_T_044` | `ImportFormats` | PUBLIC  
`TY_T_045` | `MaxUploadSizes` | PUBLIC  
`TY_T_046` | `QuotaBytesByService` | PUBLIC  
`TY_T_047` | `TeamDriveThemes` | PUBLIC  
`TY_T_050` | `Icons` | PUBLIC  
`TY_T_130` | `PermissionDetails` | PUBLIC  
`TY_T_131` | `TeamDrivePermissionDetails` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /drive/v2/ | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250305 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://www.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | drive:v2 | PUBLIC  
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
  
### COPY_FILES

  * Description: drive.files.copy 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONVERT` | IMPORTING | `STRING` | convert  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_OCR` | IMPORTING | `STRING` | ocr  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_PINNED` | IMPORTING | `STRING` | pinned  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TIMEDTEXTLANGUAGE` | IMPORTING | `STRING` | timedTextLanguage  
`IV_Q_TIMEDTEXTTRACKNAME` | IMPORTING | `STRING` | timedTextTrackName  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_016` | File  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CHILDREN

  * Description: drive.children.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_P_CHILD_ID` | IMPORTING | `STRING` | childId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
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
  
### DELETE_PARENTS

  * Description: drive.parents.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PARENT_ID` | IMPORTING | `STRING` | parentId  
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
`IV_Q_ENFORCEEXPANSIVEACCESS` | IMPORTING | `STRING` | enforceExpansiveAccess  
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
  
### DELETE_PROPERTIES

  * Description: drive.properties.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPERTY_KEY` | IMPORTING | `STRING` | propertyKey  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_SPACE` | IMPORTING | `STRING` | space  
`IV_Q_TYPE` | IMPORTING | `STRING` | type  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_018` | GeneratedIds  
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
`IV_Q_INCLUDESUBSCRIBED` | IMPORTING | `STRING` | includeSubscribed  
`IV_Q_MAXCHANGEIDCOUNT` | IMPORTING | `STRING` | maxChangeIdCount  
`IV_Q_STARTCHANGEID` | IMPORTING | `STRING` | startChangeId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | About  
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
`ES_OUTPUT` | EXPORTING | `TY_002` | App  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CHANGES

  * Description: drive.changes.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DRIVEID` | IMPORTING | `STRING` | driveId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`IV_P_CHANGE_ID` | IMPORTING | `STRING` | changeId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | Change  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CHILDREN

  * Description: drive.children.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CHILD_ID` | IMPORTING | `STRING` | childId  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | ChildReference  
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
`ES_OUTPUT` | EXPORTING | `TY_009` | Comment  
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
`ES_OUTPUT` | EXPORTING | `TY_014` | Drive  
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
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_REVISIONID` | IMPORTING | `STRING` | revisionId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_UPDATEVIEWEDDATE` | IMPORTING | `STRING` | updateViewedDate  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ID_FOR_EMAIL_PERMISSION

  * Description: drive.permissions.getIdForEmail 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_EMAIL` | IMPORTING | `STRING` | email  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_029` | PermissionId  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PARENTS

  * Description: drive.parents.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PARENT_ID` | IMPORTING | `STRING` | parentId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | ParentReference  
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
`ES_OUTPUT` | EXPORTING | `TY_028` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_PROPERTIES

  * Description: drive.properties.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPERTY_KEY` | IMPORTING | `STRING` | propertyKey  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Property  
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
`ES_OUTPUT` | EXPORTING | `TY_011` | CommentReply  
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
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REVISION_ID` | IMPORTING | `STRING` | revisionId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Revision  
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
`ES_OUTPUT` | EXPORTING | `TY_035` | StartPageToken  
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
`ES_OUTPUT` | EXPORTING | `TY_036` | TeamDrive  
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
`ES_OUTPUT` | EXPORTING | `TY_014` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_CHILDREN

  * Description: drive.children.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`IS_INPUT` | IMPORTING | `TY_008` | ChildReference  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_008` | ChildReference  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_COMMENTS

  * Description: drive.comments.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_009` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_DRIVES

  * Description: drive.drives.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IS_INPUT` | IMPORTING | `TY_014` | Drive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_FILES

  * Description: drive.files.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONVERT` | IMPORTING | `STRING` | convert  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_OCR` | IMPORTING | `STRING` | ocr  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_PINNED` | IMPORTING | `STRING` | pinned  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TIMEDTEXTLANGUAGE` | IMPORTING | `STRING` | timedTextLanguage  
`IV_Q_TIMEDTEXTTRACKNAME` | IMPORTING | `STRING` | timedTextTrackName  
`IV_Q_USECONTENTASINDEXABLETEXT` | IMPORTING | `STRING` | useContentAsIndexableText  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IS_INPUT` | IMPORTING | `TY_016` | File  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_PARENTS

  * Description: drive.parents.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_027` | ParentReference  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_027` | ParentReference  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_PERMISSIONS

  * Description: drive.permissions.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_EMAILMESSAGE` | IMPORTING | `STRING` | emailMessage  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_MOVETONEWOWNERSROOT` | IMPORTING | `STRING` | moveToNewOwnersRoot  
`IV_Q_SENDNOTIFICATIONEMAILS` | IMPORTING | `STRING` | sendNotificationEmails  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_028` | Permission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_PROPERTIES

  * Description: drive.properties.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_031` | Property  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Property  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_REPLIES

  * Description: drive.replies.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_011` | CommentReply  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | CommentReply  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_TEAMDRIVES

  * Description: drive.teamdrives.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IS_INPUT` | IMPORTING | `TY_036` | TeamDrive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | TeamDrive  
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
`ES_OUTPUT` | EXPORTING | `TY_003` | AppList  
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
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_INCLUDEITEMSFROMALLDRIVES` | IMPORTING | `STRING` | includeItemsFromAllDrives  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_INCLUDESUBSCRIBED` | IMPORTING | `STRING` | includeSubscribed  
`IV_Q_INCLUDETEAMDRIVEITEMS` | IMPORTING | `STRING` | includeTeamDriveItems  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_STARTCHANGEID` | IMPORTING | `STRING` | startChangeId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | ChangeList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CHILDREN

  * Description: drive.children.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_P_FOLDER_ID` | IMPORTING | `STRING` | folderId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | ChildList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_UPDATEDMIN` | IMPORTING | `STRING` | updatedMin  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_010` | CommentList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_015` | DriveList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_017` | FileList  
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
`ES_OUTPUT` | EXPORTING | `TY_022` | LabelList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PARENTS

  * Description: drive.parents.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | ParentList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_030` | PermissionList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_PROPERTIES

  * Description: drive.properties.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | PropertyList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_012` | CommentReplyList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_034` | RevisionList  
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
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_037` | TeamDriveList  
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
`IS_INPUT` | IMPORTING | `TY_024` | ModifyLabelsRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_025` | ModifyLabelsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_COMMENTS

  * Description: drive.comments.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_009` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | Comment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_FILES

  * Description: drive.files.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ADDPARENTS` | IMPORTING | `STRING` | addParents  
`IV_Q_CONVERT` | IMPORTING | `STRING` | convert  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_MODIFIEDDATEBEHAVIOR` | IMPORTING | `STRING` | modifiedDateBehavior  
`IV_Q_NEWREVISION` | IMPORTING | `STRING` | newRevision  
`IV_Q_OCR` | IMPORTING | `STRING` | ocr  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_PINNED` | IMPORTING | `STRING` | pinned  
`IV_Q_REMOVEPARENTS` | IMPORTING | `STRING` | removeParents  
`IV_Q_SETMODIFIEDDATE` | IMPORTING | `STRING` | setModifiedDate  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TIMEDTEXTLANGUAGE` | IMPORTING | `STRING` | timedTextLanguage  
`IV_Q_TIMEDTEXTTRACKNAME` | IMPORTING | `STRING` | timedTextTrackName  
`IV_Q_UPDATEVIEWEDDATE` | IMPORTING | `STRING` | updateViewedDate  
`IV_Q_USECONTENTASINDEXABLETEXT` | IMPORTING | `STRING` | useContentAsIndexableText  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_016` | File  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PERMISSIONS

  * Description: drive.permissions.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ENFORCEEXPANSIVEACCESS` | IMPORTING | `STRING` | enforceExpansiveAccess  
`IV_Q_REMOVEEXPIRATION` | IMPORTING | `STRING` | removeExpiration  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TRANSFEROWNERSHIP` | IMPORTING | `STRING` | transferOwnership  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`IS_INPUT` | IMPORTING | `TY_028` | Permission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_PROPERTIES

  * Description: drive.properties.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPERTY_KEY` | IMPORTING | `STRING` | propertyKey  
`IS_INPUT` | IMPORTING | `TY_031` | Property  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Property  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_REPLIES

  * Description: drive.replies.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_COMMENT_ID` | IMPORTING | `STRING` | commentId  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REPLY_ID` | IMPORTING | `STRING` | replyId  
`IS_INPUT` | IMPORTING | `TY_011` | CommentReply  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | CommentReply  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_REVISIONS

  * Description: drive.revisions.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_REVISION_ID` | IMPORTING | `STRING` | revisionId  
`IS_INPUT` | IMPORTING | `TY_033` | Revision  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Revision  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
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
`IS_INPUT` | IMPORTING | `TY_006` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TOUCH_FILES

  * Description: drive.files.touch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### TRASH_FILES

  * Description: drive.files.trash 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
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
`ES_OUTPUT` | EXPORTING | `TY_014` | Drive  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UNTRASH_FILES

  * Description: drive.files.untrash 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
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
`IS_INPUT` | IMPORTING | `TY_009` | Comment  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | Comment  
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
`IS_INPUT` | IMPORTING | `TY_014` | Drive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_014` | Drive  
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
`IV_Q_CONVERT` | IMPORTING | `STRING` | convert  
`IV_Q_ENFORCESINGLEPARENT` | IMPORTING | `STRING` | enforceSingleParent  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_MODIFIEDDATEBEHAVIOR` | IMPORTING | `STRING` | modifiedDateBehavior  
`IV_Q_NEWREVISION` | IMPORTING | `STRING` | newRevision  
`IV_Q_OCR` | IMPORTING | `STRING` | ocr  
`IV_Q_OCRLANGUAGE` | IMPORTING | `STRING` | ocrLanguage  
`IV_Q_PINNED` | IMPORTING | `STRING` | pinned  
`IV_Q_REMOVEPARENTS` | IMPORTING | `STRING` | removeParents  
`IV_Q_SETMODIFIEDDATE` | IMPORTING | `STRING` | setModifiedDate  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TIMEDTEXTLANGUAGE` | IMPORTING | `STRING` | timedTextLanguage  
`IV_Q_TIMEDTEXTTRACKNAME` | IMPORTING | `STRING` | timedTextTrackName  
`IV_Q_UPDATEVIEWEDDATE` | IMPORTING | `STRING` | updateViewedDate  
`IV_Q_USECONTENTASINDEXABLETEXT` | IMPORTING | `STRING` | useContentAsIndexableText  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_016` | File  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_016` | File  
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
`IV_Q_ENFORCEEXPANSIVEACCESS` | IMPORTING | `STRING` | enforceExpansiveAccess  
`IV_Q_REMOVEEXPIRATION` | IMPORTING | `STRING` | removeExpiration  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TRANSFEROWNERSHIP` | IMPORTING | `STRING` | transferOwnership  
`IV_Q_USEDOMAINADMINACCESS` | IMPORTING | `STRING` | useDomainAdminAccess  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PERMISSION_ID` | IMPORTING | `STRING` | permissionId  
`IS_INPUT` | IMPORTING | `TY_028` | Permission  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_028` | Permission  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_PROPERTIES

  * Description: drive.properties.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_VISIBILITY` | IMPORTING | `STRING` | visibility  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IV_P_PROPERTY_KEY` | IMPORTING | `STRING` | propertyKey  
`IS_INPUT` | IMPORTING | `TY_031` | Property  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | Property  
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
`IS_INPUT` | IMPORTING | `TY_011` | CommentReply  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_011` | CommentReply  
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
`IS_INPUT` | IMPORTING | `TY_033` | Revision  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Revision  
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
`IS_INPUT` | IMPORTING | `TY_036` | TeamDrive  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_036` | TeamDrive  
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
`IV_Q_INCLUDEDELETED` | IMPORTING | `STRING` | includeDeleted  
`IV_Q_INCLUDEITEMSFROMALLDRIVES` | IMPORTING | `STRING` | includeItemsFromAllDrives  
`IV_Q_INCLUDELABELS` | IMPORTING | `STRING` | includeLabels  
`IV_Q_INCLUDEPERMISSIONSFORVIEW` | IMPORTING | `STRING` | includePermissionsForView  
`IV_Q_INCLUDESUBSCRIBED` | IMPORTING | `STRING` | includeSubscribed  
`IV_Q_INCLUDETEAMDRIVEITEMS` | IMPORTING | `STRING` | includeTeamDriveItems  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SPACES` | IMPORTING | `STRING` | spaces  
`IV_Q_STARTCHANGEID` | IMPORTING | `STRING` | startChangeId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_TEAMDRIVEID` | IMPORTING | `STRING` | teamDriveId  
`IS_INPUT` | IMPORTING | `TY_006` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | Channel  
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
`IV_Q_PROJECTION` | IMPORTING | `STRING` | projection  
`IV_Q_REVISIONID` | IMPORTING | `STRING` | revisionId  
`IV_Q_SUPPORTSALLDRIVES` | IMPORTING | `STRING` | supportsAllDrives  
`IV_Q_SUPPORTSTEAMDRIVES` | IMPORTING | `STRING` | supportsTeamDrives  
`IV_Q_UPDATEVIEWEDDATE` | IMPORTING | `STRING` | updateViewedDate  
`IV_P_FILE_ID` | IMPORTING | `STRING` | fileId  
`IS_INPUT` | IMPORTING | `TY_006` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | Channel  
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
