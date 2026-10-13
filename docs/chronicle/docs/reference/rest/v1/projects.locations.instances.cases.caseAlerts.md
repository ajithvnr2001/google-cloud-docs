---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts
title: REST Resource: projects.locations.instances.cases.caseAlerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:07.398550+00:00
---

# REST Resource: projects.locations.instances.cases.caseAlerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.caseAlerts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseAlert
    * JSON representation
  * AlertClosureDetails
    * JSON representation
  * CloseReason
  * LegacyCasePriority
  * AlertStatus
  * InvolvedRelation
    * JSON representation
  * EntityKey
    * JSON representation
  * WorkflowStatus
  * AlertTag
    * JSON representation
  * Methods



## Resource: CaseAlert

Security notifications tied to specific data identified as a potential threat by security systems. In SecOps, investigating alerts provides critical context about the underlying activity and its relationships to entities and other security events.

JSON representation  
---  
      
    
    {
      "name": string,
      "identifier": string,
      "caseId": integer,
      "createTime": string,
      "updateTime": string,
      "ruleGenerator": string,
      "sourceGroupingIdentifier": string,
      "product": string,
      "displayName": string,
      "vendor": string,
      "environment": string,
      "ticketId": string,
      "sourceSystemName": string,
      "closureDetails": {
        object ([AlertClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertClosureDetails))
      },
      "sla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla))
      },
      "manual": boolean,
      "priority": enum ([LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)),
      "sourceIdentifier": string,
      "additionalProperties": string,
      "status": enum ([AlertStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertStatus)),
      "startTime": string,
      "endTime": string,
      "involvedRelations": [
        {
          object ([InvolvedRelation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#InvolvedRelation))
        }
      ],
      "siemAlertId": string,
      "sourceUrl": string,
      "sourceRuleUrl": string,
      "sourceSystemUrl": string,
      "sourceRuleIdentifier": string,
      "playbookStatus": enum ([WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#WorkflowStatus)),
      "attachedPlaybookName": string,
      "nestingDepth": integer,
      "alertGroupIdentifier": string,
      "eventCount": integer,
      "tags": [
        {
          object ([AlertTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertTag))
        }
      ],
      "playbookRunCount": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the CaseAlert. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseAlerts/{caseAlert}  
`identifier` |  `string` Output only. Title + Guid, e.g. ACCESS DISABLED ACCOUNTS_3A0C90F9-A87E-4E94-8727-7884F686ECDA Legacy identifier of alert used across the legacy modules in the system. Char limit: 2100  
`caseId` |  `integer` Output only. Case associated with the alert. Added for convenience to be used by the UI.  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the record in milliseconds.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modification time of the record in milliseconds.  
`ruleGenerator` |  `string` Output only. Which rule triggered the alert on the third party. This can be any rule defined in the third party Such SIEM, Splunk, CrowdStrike. Characters limit: 250.  
`sourceGroupingIdentifier` |  `string` Output only. A key on the alert that can be used to group alerts to the same case. Characters limit: 2100  
`product` |  `string` Output only. The product associated with the alert. E.g. DLP, WinEventLog:Security  
`displayName` |  `string` Output only. The display name of the alert. E.g. "DATA EXFILTRATION"  
`vendor` |  `string` Output only. The vendor of the alert. E.g. "Microsoft". Characters limit: 2100  
`environment` |  `string` Output only. The environment of the alert.  
`ticketId` |  `string` Output only. Third party ticket id, can be originated from SIEM or other tools. E.g. "3a0c90f9-a87e-4e94-8727-7884f686ecda"  
`sourceSystemName` |  `string` Output only. Which alerting system raises the alert. E.g. "QRadar", "Arcsight", "Microsoft CASB". The Integration Name in soar.  
`closureDetails` |  `object (`[AlertClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertClosureDetails)`)` Optional. Defines the close reason of an alert if any.  
`sla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Sla)`)` Optional. SLA (Service Level Agreement) for the specific alert, used also to calculate aggregate case sla.  
`manual` |  `boolean` Output only. Whether the alert was created manually.  
`priority` |  `enum (`[LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)`)` Optional. Default value is HIGH.  
`sourceIdentifier` |  `string` Output only. Stores the identifier of the source of the alert, could be a connector identifier etc.  
`additionalProperties` |  `string` Output only. Stores additional data on specific alerts, currently used by connectors, in JSON format.  
`status` |  `enum (`[AlertStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertStatus)`)` Optional. Alert status. Default value is OPEN.  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. When the alert was created on the third party product (SIEM, IPS, etc).  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. When the alert was closed on the third party product (SIEM, IPS, etc).  
`involvedRelations[]` |  `object (`[InvolvedRelation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#InvolvedRelation)`)` Output only. All involved relations for the alert. Directional connection between entities in a given alert.  
`siemAlertId` |  `string` Output only. The identifier of the alert int SIEM.  
`sourceUrl` |  `string` Output only. The source URL of the alert.  
`sourceRuleUrl` |  `string` Output only. The source rule URL of the alert.  
`sourceSystemUrl` |  `string` Output only. The source system URL.  
`sourceRuleIdentifier` |  `string` Output only. The source rule identifier.  
`playbookStatus` |  `enum (`[WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#WorkflowStatus)`)` Output only. Alert playbook status.  
`attachedPlaybookName` |  `string` Output only. The attached playbook name.  
`nestingDepth` |  `integer` Output only. The nesting depth of the alert.  
`alertGroupIdentifier` |  `string` Output only. The alert group identifier.  
`eventCount` |  `integer` Output only. The number of events that triggered the alert.  
`tags[]` |  `object (`[AlertTag](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#AlertTag)`)` Optional. AlertTags associated with the alert.  
`playbookRunCount` |  `integer` Output only. The number of times the first playbook was run on the alert.  
  
## AlertClosureDetails

Alert closure details.

JSON representation  
---  
      
    
    {
      "reason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#CloseReason)),
      "comment": string,
      "rootCause": string,
      "closingTimeMs": string
    }  
  
Fields  
---  
`reason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#CloseReason)`)` Output only. Alert closure reason.  
`comment` |  `string` Output only. Alert closure comment.  
`rootCause` |  `string` Output only. Alert closure root cause.  
`closingTimeMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Alert closure time in unix format as milliseconds.  
  
## CloseReason

Alert closure reason.

Enums  
---  
`CLOSE_REASON_UNSPECIFIED` | Unspecified close reason.  
`MALICIOUS` | Case is malicious.  
`NOT_MALICIOUS` | Case is not malicious.  
`MAINTENANCE` | Case is in maintenance.  
`INCONCLUSIVE` | Case is inconclusive.  
`UNKNOWN` | Case closure reason is unknown.  
  
## LegacyCasePriority

Legacy Case priority.

Enums  
---  
`LEGACY_CASE_PRIORITY_UNSPECIFIED` | Case priority is unspecified.  
`UNCHANGED` | Unchanged case priority.  
`INFORMATIVE` | Informative case priority.  
`LOW` | Low case priority.  
`MEDIUM` | Medium case priority.  
`HIGH` | High case priority.  
`CRITICAL` | Critical case priority.  
  
## AlertStatus

Alert status.

Enums  
---  
`ALERT_STATUS_UNSPECIFIED` | The alert status is unspecified.  
`OPEN` | The alert is open  
`CLOSE` | The alert is closed.  
  
## InvolvedRelation

Displays a connection between entities for a given alert.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "alertIdentifier": string,
      "caseId": integer,
      "relationType": string,
      "from": {
        object ([EntityKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#EntityKey))
      },
      "to": {
        object ([EntityKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#EntityKey))
      },
      "deviceProduct": string,
      "deviceVendor": string,
      "categoryOutcome": string,
      "destinationPort": string,
      "eventClassId": string,
      "startTime": string,
      "endTime": string,
      "additionalProperties": string
    }  
  
Fields  
---  
`identifier` |  `string` Required. The identifier of the relation.  
`alertIdentifier` |  `string` Output only. The identifier of the alert the relation belongs to.  
`caseId` |  `integer` Output only. The id of the case the relation belongs to.  
`relationType` |  `string` Output only. The type of the relation.  
`from` |  `object (`[EntityKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#EntityKey)`)` Output only. The source of the relation.  
`to` |  `object (`[EntityKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts#EntityKey)`)` Output only. The destination of the relation.  
`deviceProduct` |  `string` Output only. The product.  
`deviceVendor` |  `string` Output only. The vendor.  
`categoryOutcome` |  `string` Output only. The category outcome. Blocked/Allowed/null.  
`destinationPort` |  `string` Output only. The destination port, if relevant  
`eventClassId` |  `string` Output only. Event display name. For example: Email Check, Data Exfiltration, IRC etc.  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Start time of the involved relation.  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. End time of the involved relation.  
`additionalProperties` |  `string` Output only. Additional data, stored in JSON format.  
  
## EntityKey

Identifies an entity, used to display connections between entities for a given alert.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "type": string
    }  
  
Fields  
---  
`identifier` |  `string` Output only. The identifier of the entity.  
`type` |  `string` Output only. The type of the entity.  
  
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
`PENDING_PREVIOUS_COMPLETION` | Workflow is pending previous completion.  
  
## AlertTag

AlertTag associated with the alert.

JSON representation  
---  
      
    
    {
      "tag": string
    }  
  
Fields  
---  
`tag` |  `string` Output only. The name of the tag  
  
## Methods  
  
---  
  
### `[createRecommendationLongRunning](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/createRecommendationLongRunning)`

|  Initiates an asynchronous request to generate a new AI recommendation for an alert.  
  
### `[fetchRecommendation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/fetchRecommendation)`

|  Fetches a previously generated AI-driven recommendation for an alert.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/get)`

|  Gets a single CaseAlert.  
  
### `[getAlertOverviewData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/getAlertOverviewData)`

|  Retrieves a view of widgets for a specific alert.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/list)`

|  Lists CaseAlerts within a specific Case.  
  
### `[move](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/move)`

|  Moves a CaseAlert to a different Case.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/patch)`

|  Updates an existing CaseAlert.  
  
### `[pauseSla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/pauseSla)`

|  Pauses the SLA timer for a CaseAlert.  
  
### `[resolveOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/resolveOverviewWidget)`

|  Resolves the data for a specific alert overview widget.  
  
### `[resumeSla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/resumeSla)`

|  Resumes a previously paused SLA timer for a CaseAlert.  
  
### `[setSla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/setSla)`

|  Sets the Service Level Agreement (SLA) for a specific CaseAlert.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
