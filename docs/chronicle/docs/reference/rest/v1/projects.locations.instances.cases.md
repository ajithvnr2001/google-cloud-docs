---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases
title: REST Resource: projects.locations.instances.cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:55.288723+00:00
---

# REST Resource: projects.locations.instances.cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Case
    * JSON representation
  * CaseType
  * CaseStatus
  * WorkflowStatus
  * CaseTag
    * JSON representation
  * CaseProduct
    * JSON representation
  * CaseClosureDetails
    * JSON representation
  * CloseReason
  * CaseClosedAction
  * MoveEnvironment
    * JSON representation
  * CustomFieldValue
    * JSON representation
  * CustomFieldScope
  * CaseMention
    * JSON representation
  * CaseMentionSource
  * CaseObjectRBACSettings
    * JSON representation
  * Methods



## Resource: Case

A Case represents a security investigation in SecOps. Cases group related alerts and provide a central location for analysts to document their findings, track progress, and collaborate on resolving security incidents.

JSON representation  
---  
      
    
    {
      "name": string,
      "creatorUserId": string,
      "creatorUser": string,
      "lastModifyingUserId": string,
      "lastModifyingUser": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "alertCount": integer,
      "stage": string,
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Priority)),
      "assignee": string,
      "assignedUser": string,
      "description": string,
      "type": enum ([CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseType)),
      "environment": string,
      "status": enum ([CaseStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseStatus)),
      "score": number,
      "workflowStatus": enum ([WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#WorkflowStatus)),
      "sla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla))
      },
      "alertsSla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla))
      },
      "source": string,
      "tags": [
        {
          object ([CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseTag))
        }
      ],
      "products": [
        {
          object ([CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseProduct))
        }
      ],
      "closureDetails": {
        object ([CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseClosureDetails))
      },
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.tasks#Task))
        }
      ],
      "moveEnvironment": {
        object ([MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#MoveEnvironment))
      },
      "dataAccessScopes": [
        string
      ],
      "customFieldValues": [
        {
          object ([CustomFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CustomFieldValue))
        }
      ],
      "lastAssigneeChangeTime": string,
      "mentions": [
        {
          object ([CaseMention](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseMention))
        }
      ],
      "caseObjectRbacSettings": {
        object ([CaseObjectRBACSettings](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseObjectRBACSettings))
      },
      "comments": [
        {
          object ([CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment))
        }
      ],
      "important": boolean,
      "incident": boolean,
      "overflowCase": boolean,
      "involvedSuspiciousEntity": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the Case. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}  
`creatorUserId` |  `string` Output only. Case creator id. Used for homepage/requests feature.  
`creatorUser` |  `string` Output only. Resource association for the creator.  
`lastModifyingUserId` |  `string` Output only. Last user who modified the case. replaced old property name: LastModifyingUser.  
`lastModifyingUser` |  `string` Output only. Resource association for the modifying user.  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the record in milliseconds.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modification time of the record in milliseconds.  
`displayName` |  `string` Required. Case title, limited to 200 characters. Replaces old property: Title.  
`alertCount` |  `integer` Output only. Alerts in case.  
`stage` |  `string` Required. The stage of the Case. For example, "Triage", "Incident", "Investigation". Stages are defined in "chronicle.googleapis.com/CaseStageDefinition". The default stage option is "Triage".  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Priority)`)` Required. Default value is HIGH. Case priority. For example, "Informative", "Low", "Medium", "High", "Critical".  
`assignee` |  `string` Optional. This can be a user or a @SocRole, default value is the default soc-role defined in Settings.  
`assignedUser` |  `string` Output only. Resource association for the assignee.  
`description` |  `string` Optional. Case description. Limit chars to 1000.  
`type` |  `enum (`[CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseType)`)` Required. Case type.  
`environment` |  `string` Required. Case logical environments.  
`status` |  `enum (`[CaseStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseStatus)`)` Output only. Case data status.  
`score` |  `number` Optional. Attack exposure score, how risky the case.  
`workflowStatus` |  `enum (`[WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#WorkflowStatus)`)` Output only. Case playbook status.  
`sla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla)`)` Optional. SLA for the case.  
`alertsSla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla)`)` Optional. Aggregated alerts SLA. (alert has SLA as well).  
`source` |  `string` Output only. The source that created the case. Possible values: "Server", "User", "Simulated", "Merge", "AlertMove"  
`tags[]` |  `object (`[CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseTag)`)` Optional. CaseTags associated with the case.  
`products[]` |  `object (`[CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseProduct)`)` Optional. Products associated with the case. Contains Name of product (e.g. WinEventLog:Security/DLP_Product). Replaces old property: "Product".  
`closureDetails` |  `object (`[CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseClosureDetails)`)` Optional. Case closure details.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.tasks#Task)`)` Output only. Tasks associated with the case.  
`moveEnvironment` |  `object (`[MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#MoveEnvironment)`)` Optional. Case environment move details.  
`dataAccessScopes[]` |  `string` Output only. Data Access Scopes.  
`customFieldValues[]` |  `object (`[CustomFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CustomFieldValue)`)` Optional. Custom field values associated with the case.  
`lastAssigneeChangeTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The last assignee change time of the record in milliseconds.  
`mentions[]` |  `object (`[CaseMention](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseMention)`)` Output only. Case mentions associated with the case.  
`caseObjectRbacSettings` |  `object (`[CaseObjectRBACSettings](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseObjectRBACSettings)`)` Optional. RBAC settings for the case.  
`comments[]` |  `object (`[CaseComment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment)`)` Output only. Case comments associated with the case.  
`important` |  `boolean` Optional. Additional way to specify case importance. The default is false.  
`incident` |  `boolean` Optional. Additional way to specify if the case marked as incident. The default is false.  
`overflowCase` |  `boolean` Output only. Case without events, was reduced by the connector service due to a large amount of data. During ingestion if the "alert package" crosses a specific threshold, the alert will be trimmed due to security reasons (DDOS attacks, etc..)  
`involvedSuspiciousEntity` |  `boolean` Optional. If has involved suspicious entity in the case.  
  
## CaseType

Case type. LINT.IfChange(case_type)

Enums  
---  
`CASE_TYPE_UNSPECIFIED` | Unspecified case type.  
`EXTERNAL` | Case created based on alerts from external SIEM.  
`TEST` | Case created based on simulated alerts for testing.  
`REQUEST` | Case created internally through the Homepage feature.  
  
## CaseStatus

Case status.

Enums  
---  
`CASE_DATA_STATE_UNSPECIFIED` | Unspecified case data status.  
`OPENED` | Case data is opened.  
`CLOSED` | Case data is closed.  
`ALL` | Case data is all.  
`MERGED` | Case data is merged.  
`CREATION_PENDING` | Case data is creation pending.  
  
## WorkflowStatus

Workflow status.

Enums  
---  
`WORKFLOW_STATUS_UNSPECIFIED` | Unspecified workflow status.  
`NONE` | Workflow status is none.  
`IN_PROGRESS` | Workflow is running.  
`COMPLETED` | Workflow is completed.  
`FAILED` | Workflow is failed.  
`TERMINATED` | Workflow is terminated.  
`PENDING_IN_QUEUE` | Workflow is pending in queue.  
`PENDING_FOR_USER` | Workflow is pending for user.  
  
## CaseTag

CaseTag associated with the case.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "alert": string,
      "priority": integer
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The name of the tag  
`alert` |  `string` Output only. For tags set by playbook action, this is relevant during MoveAlert. Replaces old property: "Indicator".  
`priority` |  `integer` Output only. During ingestion if more than one tag matches the criteria, the one with the priority will be chosen. Available options: 1-5.  
  
## CaseProduct

Product associated with the case.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "alert": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. Display name of the product.  
`alert` |  `string` Output only. Replaces old property: "AlertIdentifier".  
  
## CaseClosureDetails

Case closure details.

JSON representation  
---  
      
    
    {
      "reason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CloseReason)),
      "rootCause": string,
      "caseClosedAction": enum ([CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseClosedAction)),
      "comment": string
    }  
  
Fields  
---  
`reason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CloseReason)`)` Output only. Case closure reason.  
`rootCause` |  `string` Output only. Case closure root cause.  
`caseClosedAction` |  `enum (`[CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseClosedAction)`)` Output only. Case closed action.  
`comment` |  `string` Output only. Case closure comment.  
  
## CloseReason

Case closure reason. LINT.IfChange(closeReason)

Enums  
---  
`CLOSE_REASON_UNSPECIFIED` | Unspecified close reason.  
`MALICIOUS` | Case is malicious.  
`NOT_MALICIOUS` | Case is not malicious.  
`MAINTENANCE` | Case is in maintenance.  
`INCONCLUSIVE` | Case is inconclusive.  
`UNKNOWN` | Case closure reason is unknown.  
  
## CaseClosedAction

Case closed action. LINT.IfChange(caseClosedAction)

Enums  
---  
`CASE_CLOSED_ACTION_UNSPECIFIED` | Unspecified case closed action.  
`AUTOMATIC` | Case closed action is automatic.  
`MANUALLY` | Case closed action is manually.  
  
## MoveEnvironment

Case environment move details.

JSON representation  
---  
      
    
    {
      "shouldDeleteOldCase": boolean
    }  
  
Fields  
---  
`shouldDeleteOldCase` |  `boolean` Optional. If the case should be deleted on move to the new environment.  
  
## CustomFieldValue

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Custom Fields are fields defined on a global level for alert and/or case scope. Custom fields are values set for a specific identifier and scope

JSON representation  
---  
      
    
    {
      "name": string,
      "customFieldId": string,
      "scope": enum ([CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CustomFieldScope)),
      "scopeId": string,
      "values": [
        string
      ],
      "valuesSearchText": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique identifier of the resource.  
`customFieldId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The id of the parent CustomField that owns this CustomFieldValue  
`scope` |  `enum (`[CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CustomFieldScope)`)` Output only. Scope of the value.  
`scopeId` |  `string` Required. Identifier of the value referencing case or alert.  
`values[]` |  `string` Required. The custom field value.  
`valuesSearchText` |  `string` Output only. Specific field represents the `values` field for faster search.  
  
## CustomFieldScope

Whether the custom field is associated with an alert or a case.

Enums  
---  
`CUSTOM_FIELD_SCOPE_UNSPECIFIED` | Unspecified scope.  
`ALERT` | Belnogs to Alert scope.  
`CASE` | Belongs to Case scope.  
  
## CaseMention

Case mention associated with the case.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "source": enum ([CaseMentionSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseMentionSource)),
      "message": string,
      "authorUserId": string,
      "mentionedUsers": [
        string
      ]
    }  
  
Fields  
---  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the case mention.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The last update time of the case mention.  
`source` |  `enum (`[CaseMentionSource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases#CaseMentionSource)`)` Output only. Case mention source.  
`message` |  `string` Output only. The message content of the case mention.  
`authorUserId` |  `string` Output only. The user who created the case mention.  
`mentionedUsers[]` |  `string` Output only. The users mentioned in the case mention.  
  
## CaseMentionSource

Case mention source.

Enums  
---  
`CASE_MENTION_SOURCE_UNSPECIFIED` | Unspecified case mention source.  
`COMMENT` | Case mention source is comment.  
`CHAT` | Case mention source is chat.  
  
## CaseObjectRBACSettings

RBAC settings for a case object.

JSON representation  
---  
      
    
    {
      "restricted": boolean
    }  
  
Fields  
---  
`restricted` |  `boolean` Optional. Whether access to this case is restricted.  
  
## Methods  
  
---  
  
### `[addTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/addTag)`

|  Adds a tag to a Case.  
  
### `[createInsight](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/createInsight)`

|  Adds an insight to a Case.  
  
### `[executeBulkAddTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkAddTag)`

|  Adds a tag to multiple cases in a single operation.  
  
### `[executeBulkAssign](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkAssign)`

|  Assigns multiple cases to a specific analyst or SOC role in bulk.  
  
### `[executeBulkChangePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkChangePriority)`

|  Changes the priority level for multiple cases in bulk.  
  
### `[executeBulkChangeStage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkChangeStage)`

|  Updates the case stage for multiple cases in bulk.  
  
### `[executeBulkClose](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkClose)`

|  Closes multiple cases in a single operation.  
  
### `[executeBulkReopen](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/executeBulkReopen)`

|  Reopens multiple previously closed cases in a single operation.  
  
### `[generateReport](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/generateReport)`

|  Generates a report for a Case in a specified format (e.g., PDF, HTML).  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/get)`

|  Gets a single Case by its resource name.  
  
### `[getCaseOverviewData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/getCaseOverviewData)`

|  Retrieves the case view metadaata.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/list)`

|  Lists Cases in an instance.  
  
### `[merge](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/merge)`

|  Merges one or more cases into a single destination case.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/patch)`

|  Updates an existing Case.  
  
### `[pauseSla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/pauseSla)`

|  Pauses the Service Level Agreement (SLA) timer for a specific Case.  
  
### `[removeTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/removeTag)`

|  Removes a tag from a Case.  
  
### `[resolveOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/resolveOverviewWidget)`

|  Resolves updated data for a specific case overview widget.  
  
### `[resumeSla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/resumeSla)`

|  Resumes a previously paused SLA timer for a Case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
