---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_chat_v1/
title: Class /GOOG/CL_CHAT_V1 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:29.232497+00:00
---

# Class /GOOG/CL_CHAT_V1  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_chat_v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CHAT_V1 Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_chat_v1)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_chat_v1)



## Class
    
    
    /GOOG/CL_CHAT_V1

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Google Chat API v1`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `ActionParameter` | PUBLIC  
`TY_002` | `ActionResponse` | PUBLIC  
`TY_003` | `ActionStatus` | PUBLIC  
`TY_004` | `Annotation` | PUBLIC  
`TY_005` | `AttachedGif` | PUBLIC  
`TY_006` | `Attachment` | PUBLIC  
`TY_007` | `AttachmentDataRef` | PUBLIC  
`TY_008` | `Button` | PUBLIC  
`TY_009` | `Card` | PUBLIC  
`TY_010` | `CardAction` | PUBLIC  
`TY_011` | `CardHeader` | PUBLIC  
`TY_012` | `CardWithId` | PUBLIC  
`TY_016` | `CustomEmoji` | PUBLIC  
`TY_019` | `DeletionMetadata` | PUBLIC  
`TY_020` | `Dialog` | PUBLIC  
`TY_021` | `DialogAction` | PUBLIC  
`TY_022` | `DriveDataRef` | PUBLIC  
`TY_023` | `Emoji` | PUBLIC  
`TY_024` | `EmojiReactionSummary` | PUBLIC  
`TY_026` | `FormAction` | PUBLIC  
`TY_052` | `GoogleAppsCardV1SelectionItem` | PUBLIC  
`TY_061` | `Image` | PUBLIC  
`TY_062` | `ImageButton` | PUBLIC  
`TY_064` | `KeyValue` | PUBLIC  
`TY_065` | `ListMembershipsResponse` | PUBLIC  
`TY_066` | `ListMessagesResponse` | PUBLIC  
`TY_067` | `ListReactionsResponse` | PUBLIC  
`TY_068` | `ListSpacesResponse` | PUBLIC  
`TY_069` | `MatchedUrl` | PUBLIC  
`TY_070` | `Media` | PUBLIC  
`TY_071` | `Membership` | PUBLIC  
`TY_072` | `Message` | PUBLIC  
`TY_073` | `OnClick` | PUBLIC  
`TY_074` | `OpenLink` | PUBLIC  
`TY_075` | `QuotedMessageMetadata` | PUBLIC  
`TY_076` | `Reaction` | PUBLIC  
`TY_077` | `Section` | PUBLIC  
`TY_078` | `SetUpSpaceRequest` | PUBLIC  
`TY_079` | `SlashCommand` | PUBLIC  
`TY_080` | `SlashCommandMetadata` | PUBLIC  
`TY_081` | `Space` | PUBLIC  
`TY_083` | `SpaceDetails` | PUBLIC  
`TY_086` | `TextButton` | PUBLIC  
`TY_087` | `TextParagraph` | PUBLIC  
`TY_088` | `Thread` | PUBLIC  
`TY_091` | `UploadAttachmentRequest` | PUBLIC  
`TY_092` | `UploadAttachmentResponse` | PUBLIC  
`TY_093` | `User` | PUBLIC  
`TY_094` | `UserMentionMetadata` | PUBLIC  
`TY_095` | `WidgetMarkup` | PUBLIC  
`TY_097` | `CompleteImportSpaceResponse` | PUBLIC  
`TY_098` | `Group` | PUBLIC  
`TY_099` | `SelectionItems` | PUBLIC  
`TY_100` | `UpdatedWidget` | PUBLIC  
`TY_101` | `DriveLinkData` | PUBLIC  
`TY_102` | `RichLinkMetadata` | PUBLIC  
`TY_104` | `AccessoryWidget` | PUBLIC  
`TY_105` | `ListSpaceEventsResponse` | PUBLIC  
`TY_106` | `MembershipBatchCreatedEventData` | PUBLIC  
`TY_107` | `MembershipBatchDeletedEventData` | PUBLIC  
`TY_108` | `MembershipBatchUpdatedEventData` | PUBLIC  
`TY_109` | `MembershipCreatedEventData` | PUBLIC  
`TY_110` | `MembershipDeletedEventData` | PUBLIC  
`TY_111` | `MembershipUpdatedEventData` | PUBLIC  
`TY_112` | `MessageBatchCreatedEventData` | PUBLIC  
`TY_113` | `MessageBatchDeletedEventData` | PUBLIC  
`TY_114` | `MessageBatchUpdatedEventData` | PUBLIC  
`TY_115` | `MessageCreatedEventData` | PUBLIC  
`TY_116` | `MessageDeletedEventData` | PUBLIC  
`TY_117` | `MessageUpdatedEventData` | PUBLIC  
`TY_118` | `ReactionBatchCreatedEventData` | PUBLIC  
`TY_119` | `ReactionBatchDeletedEventData` | PUBLIC  
`TY_120` | `ReactionCreatedEventData` | PUBLIC  
`TY_121` | `ReactionDeletedEventData` | PUBLIC  
`TY_122` | `SpaceBatchUpdatedEventData` | PUBLIC  
`TY_123` | `SpaceEvent` | PUBLIC  
`TY_124` | `SpaceReadState` | PUBLIC  
`TY_125` | `SpaceUpdatedEventData` | PUBLIC  
`TY_126` | `ThreadReadState` | PUBLIC  
`TY_127` | `AccessSettings` | PUBLIC  
`TY_128` | `MembershipCount` | PUBLIC  
`TY_129` | `SearchSpacesResponse` | PUBLIC  
`TY_130` | `ChatSpaceLinkData` | PUBLIC  
`TY_136` | `PermissionSetting` | PUBLIC  
`TY_137` | `PermissionSettings` | PUBLIC  
`TY_T_001` | `ActionParameter` | PUBLIC  
`TY_T_004` | `Annotation` | PUBLIC  
`TY_T_005` | `AttachedGif` | PUBLIC  
`TY_T_006` | `Attachment` | PUBLIC  
`TY_T_008` | `Button` | PUBLIC  
`TY_T_009` | `Card` | PUBLIC  
`TY_T_010` | `CardAction` | PUBLIC  
`TY_T_012` | `CardWithId` | PUBLIC  
`TY_T_024` | `EmojiReactionSummary` | PUBLIC  
`TY_T_052` | `GoogleAppsCardV1SelectionItem` | PUBLIC  
`TY_T_071` | `Membership` | PUBLIC  
`TY_T_072` | `Message` | PUBLIC  
`TY_T_076` | `Reaction` | PUBLIC  
`TY_T_077` | `Section` | PUBLIC  
`TY_T_081` | `Space` | PUBLIC  
`TY_T_095` | `WidgetMarkup` | PUBLIC  
`TY_T_104` | `AccessoryWidget` | PUBLIC  
`TY_T_109` | `MembershipCreatedEventData` | PUBLIC  
`TY_T_110` | `MembershipDeletedEventData` | PUBLIC  
`TY_T_111` | `MembershipUpdatedEventData` | PUBLIC  
`TY_T_115` | `MessageCreatedEventData` | PUBLIC  
`TY_T_116` | `MessageDeletedEventData` | PUBLIC  
`TY_T_117` | `MessageUpdatedEventData` | PUBLIC  
`TY_T_120` | `ReactionCreatedEventData` | PUBLIC  
`TY_T_121` | `ReactionDeletedEventData` | PUBLIC  
`TY_T_123` | `SpaceEvent` | PUBLIC  
`TY_T_125` | `SpaceUpdatedEventData` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version | 1.0 | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.5 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix |  | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20241114 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://chat.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | chat:v1 | PUBLIC  
`C_SUPPORTED_AUTH` | `/GOOG/SUPP_AUTH` | Supported Auth Types | OOOOWW | PUBLIC  
  
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
  
### COMPLETE_IMPORT_SPACES

  * Description: chat.spaces.completeImport 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `DATA` | Input Data  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_097` | CompleteImportSpaceResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_MEMBERS

  * Description: chat.spaces.members.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `TY_071` | Membership  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | Membership  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_MESSAGES

  * Description: chat.spaces.messages.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MESSAGEID` | IMPORTING | `STRING` | messageId  
`IV_Q_MESSAGEREPLYOPTION` | IMPORTING | `STRING` | messageReplyOption  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IV_Q_THREADKEY` | IMPORTING | `STRING` | threadKey  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `TY_072` | Message  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_072` | Message  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_REACTIONS

  * Description: chat.spaces.messages.reactions.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`IS_INPUT` | IMPORTING | `TY_076` | Reaction  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_076` | Reaction  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### CREATE_SPACES

  * Description: chat.spaces.create 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_REQUESTID` | IMPORTING | `STRING` | requestId  
`IS_INPUT` | IMPORTING | `TY_081` | Space  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_081` | Space  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_MEMBERS

  * Description: chat.spaces.members.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MEMBERS_ID` | IMPORTING | `STRING` | membersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | Membership  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_MESSAGES

  * Description: chat.spaces.messages.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FORCE` | IMPORTING | `STRING` | force  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_REACTIONS

  * Description: chat.spaces.messages.reactions.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`IV_P_REACTIONS_ID` | IMPORTING | `STRING` | reactionsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_SPACES

  * Description: chat.spaces.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `DATA` | Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DOWNLOAD_MEDIA

  * Description: chat.media.download 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_MEDIA_ID` | IMPORTING | `STRING` | mediaId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_070` | Media  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### FIND_DIRECT_MESSAGE_SPACES

  * Description: chat.spaces.findDirectMessage 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_NAME` | IMPORTING | `STRING` | name  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_081` | Space  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ATTACHMENTS

  * Description: chat.spaces.messages.attachments.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`IV_P_ATTACHMENTS_ID` | IMPORTING | `STRING` | attachmentsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_006` | Attachment  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_MEMBERS

  * Description: chat.spaces.members.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MEMBERS_ID` | IMPORTING | `STRING` | membersId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | Membership  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_MESSAGES

  * Description: chat.spaces.messages.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_072` | Message  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SPACES

  * Description: chat.spaces.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_081` | Space  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SPACE_EVENTS

  * Description: chat.spaces.spaceEvents.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_SPACE_EVENTS_ID` | IMPORTING | `STRING` | spaceEventsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_123` | SpaceEvent  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SPACE_READ_STATE_SPACES

  * Description: chat.users.spaces.getSpaceReadState 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_124` | SpaceReadState  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_THREAD_READ_STATE_THREA

  * Description: chat.users.spaces.threads.getThreadReadState 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_THREADS_ID` | IMPORTING | `STRING` | threadsId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_126` | ThreadReadState  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MEMBERS

  * Description: chat.spaces.members.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWGROUPS` | IMPORTING | `STRING` | showGroups  
`IV_Q_SHOWINVITED` | IMPORTING | `STRING` | showInvited  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_065` | ListMembershipsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_MESSAGES

  * Description: chat.spaces.messages.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_066` | ListMessagesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_REACTIONS

  * Description: chat.spaces.messages.reactions.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_067` | ListReactionsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SPACES

  * Description: chat.spaces.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_068` | ListSpacesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SPACE_EVENTS

  * Description: chat.spaces.spaceEvents.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_FILTER` | IMPORTING | `STRING` | filter  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_105` | ListSpaceEventsResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_MEMBERS

  * Description: chat.spaces.members.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MEMBERS_ID` | IMPORTING | `STRING` | membersId  
`IS_INPUT` | IMPORTING | `TY_071` | Membership  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_071` | Membership  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_MESSAGES

  * Description: chat.spaces.messages.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`IS_INPUT` | IMPORTING | `TY_072` | Message  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_072` | Message  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_SPACES

  * Description: chat.spaces.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `TY_081` | Space  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_081` | Space  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SEARCH_SPACES

  * Description: chat.spaces.search 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGESIZE` | IMPORTING | `STRING` | pageSize  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_QUERY` | IMPORTING | `STRING` | query  
`IV_Q_USEADMINACCESS` | IMPORTING | `STRING` | useAdminAccess  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_129` | SearchSpacesResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### SETUP_SPACES

  * Description: chat.spaces.setup 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_078` | SetUpSpaceRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_081` | Space  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_MESSAGES

  * Description: chat.spaces.messages.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALLOWMISSING` | IMPORTING | `STRING` | allowMissing  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IV_P_MESSAGES_ID` | IMPORTING | `STRING` | messagesId  
`IS_INPUT` | IMPORTING | `TY_072` | Message  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_072` | Message  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_SPACE_READ_STATE_SPA

  * Description: chat.users.spaces.updateSpaceReadState 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_UPDATEMASK` | IMPORTING | `STRING` | updateMask  
`IV_P_USERS_ID` | IMPORTING | `STRING` | usersId  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `TY_124` | SpaceReadState  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_124` | SpaceReadState  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPLOAD_MEDIA

  * Description: chat.media.upload 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SPACES_ID` | IMPORTING | `STRING` | spacesId  
`IS_INPUT` | IMPORTING | `TY_091` | UploadAttachmentRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_092` | UploadAttachmentResponse  
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
