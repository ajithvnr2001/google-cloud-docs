---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords
title: REST Resource: projects.locations.instances.cases.caseWallRecords \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:28.318453+00:00
---

# REST Resource: projects.locations.instances.cases.caseWallRecords  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.caseWallRecords Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseWallRecord
    * JSON representation
  * WallActivityType
  * ActivityKind
  * CaseActivityTag
    * JSON representation
  * Methods



## Resource: CaseWallRecord

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Case Wall is a repository of all event logs containing "case caseWallRecords" related to a case since the time the case was created until it is closed, taken by a user or a playbook's action.

JSON representation  
---  
      
    
    {
      "name": string,
      "caseId": string,
      "creatorUserId": string,
      "creatorFullName": string,
      "activityId": string,
      "createTime": string,
      "updateTime": string,
      "alertIdentifier": string,
      "activityDataJson": string,
      "tags": [
        {
          object ([CaseActivityTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#CaseActivityTag))
        }
      ],
      "activityType": enum ([WallActivityType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#WallActivityType)),
      "activityKind": enum ([ActivityKind](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#ActivityKind)),
      "favorite": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the CaseWallRecord. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseWallRecords/{caseActivity}  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The ID of the case associated with the activity.  
`creatorUserId` |  `string` Output only. The ID of the user who created the activity, e.g. C7A739D7-E465-4106-9871-18F415D6C3BD  
`creatorFullName` |  `string` Output only. The full name of the user who created the activity.  
`activityId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Id of the Case Wall activity. Replaces old prop: "Id"  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the activity in milliseconds since the Unix epoch.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modification time of the activity in milliseconds since the Unix epoch.  
`alertIdentifier` |  `string` Output only. The identifier of the alert (if any) associated with the activity. for example, "SUSPICIOUS PHISHING EMAIL_C7A739D7-E465-4106-9871-18F415D6C3BD"  
`activityDataJson` |  `string` Output only. Case activity details. Can be customized. e.g. "Message": "Closing case"  
`tags[]` |  `object (`[CaseActivityTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#CaseActivityTag)`)` Output only. Tags associated with the activity.  
`activityType` |  `enum (`[WallActivityType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#WallActivityType)`)` Output only. Activity type.  
`activityKind` |  `enum (`[ActivityKind](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords#ActivityKind)`)` Optional. The kind of the activity.  
`favorite` |  `boolean` Optional. Whether the activity is was marked as favorite.  
  
## WallActivityType

The type of the activity.

Enums  
---  
`WALL_ACTIVITY_TYPE_UNSPECIFIED` | Unspecified wall activity type.  
`CASE_ALERT_DATA` | Case alert data activity type.  
`CASE_STATUS_CHANGE` | Case status change activity type.  
`CASE_TASK` | Case task activity type.  
`CASE_ACTION` | Case action activity type.  
`CASE_EVIDENCE` | Case evidence activity type.  
`CASE_COMMENT` | Case comment activity type.  
`CASE_INSIGHT` | Case insight activity type.  
`CASE_CREATION` | Case creation activity type.  
`CASE_EXTERNAL_CHANNEL_MESSAGE` | Case external channel message activity type.  
`PINNED_CASE_CHAT_MESSAGE` | Pinned case chat message activity type.  
`CASE_LINK` | Case link activity type.  
  
## ActivityKind

The kind of the activity - relates to the type of the activity, represents the actual action that was performed.

Enums  
---  
`ACTIVITY_KIND_UNSPECIFIED` | Unspecified activity kind.  
`COMMENT` | Comment activity kind.  
`WORKFLOW_ACTIVITY` | Workflow activity kind.  
`EMAIL` | Email activity kind.  
`TASK` | Task activity kind.  
`CASE_CREATED` | Case created activity kind.  
`CASE_UPDATED` | Case updated activity kind.  
`CASE_REOPENED` | Case reopened activity kind.  
`CASE_ASSIGNED` | Case assigned activity kind.  
`CASE_CLOSED` | Case closed activity kind.  
`CASE_STAGE_CHANGED` | Case stage changed activity kind.  
`IS_IMPORTANT_CHANGED` | Case is important changed activity kind.  
`PRIORITY_CHANGED` | Case priority changed activity kind.  
`INCIDENT_RAISED` | Incident raised activity kind.  
`ESCALATED` | Case escalated activity kind.  
`TAG_CHANGE` | Case tag changed activity kind.  
`CASE_RENAMED` | Case renamed activity kind.  
`SLA_CHANGED` | SLA changed activity kind.  
`MOVED_ALERT` | Alert moved activity kind.  
`MERGE_CASES` | Case merged activity kind.  
`CUSTOM_FORM_CHANGES` | Custom form changes activity kind.  
`PLAYBOOK_ATTACHED` | Playbook attached activity kind.  
`ENTITY_ADDED` | Entity added activity kind.  
`PLAYBOOK_RERUN` | Playbook rerun activity kind.  
`BLOCK_RERUN` | Block rerun activity kind.  
`ACTION` | Action activity kind.  
`ENRICHMENT_ACTION` | Enrichment action activity kind.  
  
## CaseActivityTag

Case activity tag.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the tag.  
`displayName` |  `string` Required. The display name of the tag.  
  
## Methods  
  
---  
  
### `[favorite](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/favorite)`

|  Sets or unsets (toggles) the favorite status of a wall record.  
  
### `[fetchActivitiesCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/fetchActivitiesCount)`

|  Returns the count of case activities, optionally filtered by type.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/get)`

|  Gets a single CaseWallRecord by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseWallRecords/list)`

|  Lists CaseWallRecords for a specific Case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
