---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_calendar_v3/
title: Class /GOOG/CL_CALENDAR_V3 \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:37.499137+00:00
---

# Class /GOOG/CL_CALENDAR_V3  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_calendar_v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Reference ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview)



Send feedback 

#  Class /GOOG/CL_CALENDAR_V3 Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_calendar_v3)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_calendar_v3)



## Class
    
    
    /GOOG/CL_CALENDAR_V3

  * Inheriting from:`/GOOG/CL_HTTP_CLIENT`
  * Description:`Calendar API v3`

For general information about a class in ABAP SDK for Google Cloud, see [API client stub](https://docs.cloud.google.com/sap/docs/abap-sdk/latest/developer#client_stub). 

## Types

Type | Description | Visibility  
---|---|---  
`TY_001` | `Acl` | PUBLIC  
`TY_002` | `AclRule` | PUBLIC  
`TY_003` | `Calendar` | PUBLIC  
`TY_004` | `CalendarList` | PUBLIC  
`TY_005` | `CalendarListEntry` | PUBLIC  
`TY_006` | `CalendarNotification` | PUBLIC  
`TY_007` | `Channel` | PUBLIC  
`TY_008` | `ColorDefinition` | PUBLIC  
`TY_009` | `Colors` | PUBLIC  
`TY_010` | `ConferenceData` | PUBLIC  
`TY_011` | `ConferenceParameters` | PUBLIC  
`TY_012` | `ConferenceParametersAddOnParameters` | PUBLIC  
`TY_013` | `ConferenceProperties` | PUBLIC  
`TY_014` | `ConferenceRequestStatus` | PUBLIC  
`TY_015` | `ConferenceSolution` | PUBLIC  
`TY_016` | `ConferenceSolutionKey` | PUBLIC  
`TY_017` | `CreateConferenceRequest` | PUBLIC  
`TY_018` | `EntryPoint` | PUBLIC  
`TY_019` | `Error` | PUBLIC  
`TY_020` | `Event` | PUBLIC  
`TY_021` | `EventAttachment` | PUBLIC  
`TY_022` | `EventAttendee` | PUBLIC  
`TY_023` | `EventDateTime` | PUBLIC  
`TY_024` | `EventReminder` | PUBLIC  
`TY_025` | `EventWorkingLocationProperties` | PUBLIC  
`TY_026` | `Events` | PUBLIC  
`TY_027` | `FreeBusyCalendar` | PUBLIC  
`TY_028` | `FreeBusyGroup` | PUBLIC  
`TY_029` | `FreeBusyRequest` | PUBLIC  
`TY_030` | `FreeBusyRequestItem` | PUBLIC  
`TY_031` | `FreeBusyResponse` | PUBLIC  
`TY_032` | `Setting` | PUBLIC  
`TY_033` | `Settings` | PUBLIC  
`TY_034` | `TimePeriod` | PUBLIC  
`TY_036` | `Scope` | PUBLIC  
`TY_038` | `NotificationSettings` | PUBLIC  
`TY_047` | `Creator` | PUBLIC  
`TY_048` | `ExtendedProperties` | PUBLIC  
`TY_049` | `Gadget` | PUBLIC  
`TY_050` | `Organizer` | PUBLIC  
`TY_051` | `Reminders` | PUBLIC  
`TY_052` | `Source` | PUBLIC  
`TY_053` | `CustomLocation` | PUBLIC  
`TY_054` | `OfficeLocation` | PUBLIC  
`TY_055` | `EventFocusTimeProperties` | PUBLIC  
`TY_056` | `EventOutOfOfficeProperties` | PUBLIC  
`TY_057` | `EventBirthdayProperties` | PUBLIC  
`TY_T_002` | `AclRule` | PUBLIC  
`TY_T_005` | `CalendarListEntry` | PUBLIC  
`TY_T_006` | `CalendarNotification` | PUBLIC  
`TY_T_018` | `EntryPoint` | PUBLIC  
`TY_T_019` | `Error` | PUBLIC  
`TY_T_020` | `Event` | PUBLIC  
`TY_T_021` | `EventAttachment` | PUBLIC  
`TY_T_022` | `EventAttendee` | PUBLIC  
`TY_T_024` | `EventReminder` | PUBLIC  
`TY_T_030` | `FreeBusyRequestItem` | PUBLIC  
`TY_T_032` | `Setting` | PUBLIC  
`TY_T_034` | `TimePeriod` | PUBLIC  
`TY_T_STRING` | `Table of Strings` | PUBLIC  
  
## Constants

Name | Type | Description | Value | Visibility  
---|---|---|---|---  
`C_CLOUD_VERSION` | `/GOOG/SDK_VERSION` | Lowest Cloud Version |  | PUBLIC  
`C_ON_PREM_VERSION` | `/GOOG/SDK_VERSION` | Lowest On-premises Version | 1.7 | PUBLIC  
`C_PATH_PREFIX` | `STRING` | API Path Prefix | /calendar/v3/ | PUBLIC  
`C_REVISION_DATE` | `DATUM` | Discovery Document revision Date | 20250220 | PUBLIC  
`C_ROOT_URL` | `STRING` | API Root URL | https://www.googleapis.com | PUBLIC  
`C_SERVICE_NAME` | `/GOOG/SERVICE_NAME` | Google Service Name | calendar:v3 | PUBLIC  
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
  
### CLEAR_CALENDARS

  * Description: calendar.calendars.clear 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_ACL

  * Description: calendar.acl.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_RULE_ID` | IMPORTING | `STRING` | ruleId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CALENDARS

  * Description: calendar.calendars.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_CALENDAR_LIST

  * Description: calendar.calendarList.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### DELETE_EVENTS

  * Description: calendar.events.delete 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_ACL

  * Description: calendar.acl.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_RULE_ID` | IMPORTING | `STRING` | ruleId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AclRule  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CALENDARS

  * Description: calendar.calendars.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Calendar  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_CALENDAR_LIST

  * Description: calendar.calendarList.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | CalendarListEntry  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_COLORS

  * Description: calendar.colors.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_009` | Colors  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_EVENTS

  * Description: calendar.events.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_TIMEZONE` | IMPORTING | `STRING` | timeZone  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### GET_SETTINGS

  * Description: calendar.settings.get 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_SETTING` | IMPORTING | `STRING` | setting  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_032` | Setting  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### IMPORT_EVENTS

  * Description: calendar.events.import 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONFERENCEDATAVERSION` | IMPORTING | `STRING` | conferenceDataVersion  
`IV_Q_SUPPORTSATTACHMENTS` | IMPORTING | `STRING` | supportsAttachments  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_020` | Event  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_ACL

  * Description: calendar.acl.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_002` | AclRule  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AclRule  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_CALENDARS

  * Description: calendar.calendars.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_003` | Calendar  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Calendar  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_CALENDAR_LIST

  * Description: calendar.calendarList.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_COLORRGBFORMAT` | IMPORTING | `STRING` | colorRgbFormat  
`IS_INPUT` | IMPORTING | `TY_005` | CalendarListEntry  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | CalendarListEntry  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSERT_EVENTS

  * Description: calendar.events.insert 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_CONFERENCEDATAVERSION` | IMPORTING | `STRING` | conferenceDataVersion  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_Q_SUPPORTSATTACHMENTS` | IMPORTING | `STRING` | supportsAttachments  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_020` | Event  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### INSTANCES_EVENTS

  * Description: calendar.events.instances 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORIGINALSTART` | IMPORTING | `STRING` | originalStart  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_TIMEMAX` | IMPORTING | `STRING` | timeMax  
`IV_Q_TIMEMIN` | IMPORTING | `STRING` | timeMin  
`IV_Q_TIMEZONE` | IMPORTING | `STRING` | timeZone  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Events  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_ACL

  * Description: calendar.acl.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_001` | Acl  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_CALENDAR_LIST

  * Description: calendar.calendarList.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_MINACCESSROLE` | IMPORTING | `STRING` | minAccessRole  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SHOWHIDDEN` | IMPORTING | `STRING` | showHidden  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_004` | CalendarList  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_EVENTS

  * Description: calendar.events.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_EVENTTYPES` | IMPORTING | `STRING` | eventTypes  
`IV_Q_ICALUID` | IMPORTING | `STRING` | iCalUID  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PRIVATEEXTENDEDPROPERTY` | IMPORTING | `STRING` | privateExtendedProperty  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_SHAREDEXTENDEDPROPERTY` | IMPORTING | `STRING` | sharedExtendedProperty  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SHOWHIDDENINVITATIONS` | IMPORTING | `STRING` | showHiddenInvitations  
`IV_Q_SINGLEEVENTS` | IMPORTING | `STRING` | singleEvents  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IV_Q_TIMEMAX` | IMPORTING | `STRING` | timeMax  
`IV_Q_TIMEMIN` | IMPORTING | `STRING` | timeMin  
`IV_Q_TIMEZONE` | IMPORTING | `STRING` | timeZone  
`IV_Q_UPDATEDMIN` | IMPORTING | `STRING` | updatedMin  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_026` | Events  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### LIST_SETTINGS

  * Description: calendar.settings.list 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_033` | Settings  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### MOVE_EVENTS

  * Description: calendar.events.move 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_DESTINATION` | IMPORTING | `STRING` | destination  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_ACL

  * Description: calendar.acl.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_RULE_ID` | IMPORTING | `STRING` | ruleId  
`IS_INPUT` | IMPORTING | `TY_002` | AclRule  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AclRule  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CALENDARS

  * Description: calendar.calendars.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_003` | Calendar  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Calendar  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_CALENDAR_LIST

  * Description: calendar.calendarList.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_COLORRGBFORMAT` | IMPORTING | `STRING` | colorRgbFormat  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_005` | CalendarListEntry  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | CalendarListEntry  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### PATCH_EVENTS

  * Description: calendar.events.patch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_CONFERENCEDATAVERSION` | IMPORTING | `STRING` | conferenceDataVersion  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_Q_SUPPORTSATTACHMENTS` | IMPORTING | `STRING` | supportsAttachments  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`IS_INPUT` | IMPORTING | `TY_020` | Event  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUERY_FREEBUSY

  * Description: calendar.freebusy.query 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_029` | FreeBusyRequest  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_031` | FreeBusyResponse  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### QUICK_ADD_EVENTS

  * Description: calendar.events.quickAdd 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_Q_TEXT` | IMPORTING | `STRING` | text  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### STOP_CHANNELS

  * Description: calendar.channels.stop 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IS_INPUT` | IMPORTING | `TY_007` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_ACL

  * Description: calendar.acl.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_RULE_ID` | IMPORTING | `STRING` | ruleId  
`IS_INPUT` | IMPORTING | `TY_002` | AclRule  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_002` | AclRule  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CALENDARS

  * Description: calendar.calendars.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_003` | Calendar  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_003` | Calendar  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_CALENDAR_LIST

  * Description: calendar.calendarList.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_COLORRGBFORMAT` | IMPORTING | `STRING` | colorRgbFormat  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_005` | CalendarListEntry  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_005` | CalendarListEntry  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### UPDATE_EVENTS

  * Description: calendar.events.update 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_CONFERENCEDATAVERSION` | IMPORTING | `STRING` | conferenceDataVersion  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_SENDNOTIFICATIONS` | IMPORTING | `STRING` | sendNotifications  
`IV_Q_SENDUPDATES` | IMPORTING | `STRING` | sendUpdates  
`IV_Q_SUPPORTSATTACHMENTS` | IMPORTING | `STRING` | supportsAttachments  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IV_P_EVENT_ID` | IMPORTING | `STRING` | eventId  
`IS_INPUT` | IMPORTING | `TY_020` | Event  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_020` | Event  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_ACL

  * Description: calendar.acl.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_007` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Channel  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_CALENDAR_LIST

  * Description: calendar.calendarList.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_MINACCESSROLE` | IMPORTING | `STRING` | minAccessRole  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SHOWHIDDEN` | IMPORTING | `STRING` | showHidden  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IS_INPUT` | IMPORTING | `TY_007` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Channel  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_EVENTS

  * Description: calendar.events.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_ALWAYSINCLUDEEMAIL` | IMPORTING | `STRING` | alwaysIncludeEmail  
`IV_Q_EVENTTYPES` | IMPORTING | `STRING` | eventTypes  
`IV_Q_ICALUID` | IMPORTING | `STRING` | iCalUID  
`IV_Q_MAXATTENDEES` | IMPORTING | `STRING` | maxAttendees  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_ORDERBY` | IMPORTING | `STRING` | orderBy  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_PRIVATEEXTENDEDPROPERTY` | IMPORTING | `STRING` | privateExtendedProperty  
`IV_Q_Q` | IMPORTING | `STRING` | q  
`IV_Q_SHAREDEXTENDEDPROPERTY` | IMPORTING | `STRING` | sharedExtendedProperty  
`IV_Q_SHOWDELETED` | IMPORTING | `STRING` | showDeleted  
`IV_Q_SHOWHIDDENINVITATIONS` | IMPORTING | `STRING` | showHiddenInvitations  
`IV_Q_SINGLEEVENTS` | IMPORTING | `STRING` | singleEvents  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IV_Q_TIMEMAX` | IMPORTING | `STRING` | timeMax  
`IV_Q_TIMEMIN` | IMPORTING | `STRING` | timeMin  
`IV_Q_TIMEZONE` | IMPORTING | `STRING` | timeZone  
`IV_Q_UPDATEDMIN` | IMPORTING | `STRING` | updatedMin  
`IV_P_CALENDAR_ID` | IMPORTING | `STRING` | calendarId  
`IS_INPUT` | IMPORTING | `TY_007` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Channel  
`EV_RET_CODE` | EXPORTING | `I` | Return Code  
`EV_ERR_TEXT` | EXPORTING | `STRING` | Error Text  
`ES_ERR_RESP` | EXPORTING | `/GOOG/ERR_RESP` | Error Response  
  
#### Exception

Name | Description  
---|---  
`/GOOG/CX_SDK` | ABAP SDK for Google Cloud: Exception Class  
  
### WATCH_SETTINGS

  * Description: calendar.settings.watch 
  * Visibility: PUBLIC 



#### Parameters

Name | Category | Type | Description  
---|---|---|---  
`IV_Q_MAXRESULTS` | IMPORTING | `STRING` | maxResults  
`IV_Q_PAGETOKEN` | IMPORTING | `STRING` | pageToken  
`IV_Q_SYNCTOKEN` | IMPORTING | `STRING` | syncToken  
`IS_INPUT` | IMPORTING | `TY_007` | Channel  
`ES_RAW` | EXPORTING | `DATA` | Raw Output Data  
`ES_OUTPUT` | EXPORTING | `TY_007` | Channel  
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
