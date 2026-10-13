---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/update_case/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:04.956987+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/update_case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_case`

Updates an existing case in Google SecOps.

Modifies various properties of a specific case. Only the fields provided in the arguments will be updated. Note: It is not possible to change the status of a case to 'CLOSED' using this tool. This can only be done via the 'execute_bulk_close_case' tool.

**Workflow Integration:**

  * A core function for managing the lifecycle of a security case, used in both manual and automated workflows.
  * Integrates with UI actions like assigning a case, changing its status, or adding a description.
  * Essential for automated playbooks that need to update a case's status after performing an action, such as "Case moved to 'Remediation' after host was isolated."
  * Can be used to synchronize case status with external ticketing or project management systems.



**Use Cases:**

  * An analyst assigns a case to themselves or another team member.
  * A SOC manager escalates a case by changing its priority from "Medium" to "Critical".
  * A user adds a detailed description or updates the title of a case to better reflect the investigation's findings.
  * Add or modify tags and products associated with the case.



**Example Usage:**

  * `update_case(projectId='123', region='us', customerId='abc', caseId='456', assignee='new_user@example.com', priority='PRIORITY_CRITICAL')`
  * `update_case(projectId='123', region='us', customerId='abc', caseId='789', stage='Investigation', description='Escalated for further investigation due to new IOCs.')`
  * `update_case(projectId='123', region='us', customerId='abc', caseId='101', important=True)`



**Next Steps (using MCP-enabled tools):**

  * Use 'get_case' with the case's resource name to verify that the case has been updated correctly.
  * Use 'list_case_comments' to see if any comments were added as part of the update.
  * Use 'create_case_comment' to add a note explaining why the case was updated.



The following sample demonstrate how to use `curl` to invoke the `update_case` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_case",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for UpdateCase. Next ID: 21

### UpdateCaseRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "caseId": string,
      "tags": [
        {
          object ([CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseTag))
        }
      ],
      "products": [
        {
          object ([CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseProduct))
        }
      ],
    
      // Union field _display_name can be only one of the following:
      "displayName": string
      // End of list of possible types for union field _display_name.
    
      // Union field _stage can be only one of the following:
      "stage": string
      // End of list of possible types for union field _stage.
    
      // Union field _priority can be only one of the following:
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority))
      // End of list of possible types for union field _priority.
    
      // Union field _important can be only one of the following:
      "important": boolean
      // End of list of possible types for union field _important.
    
      // Union field _incident can be only one of the following:
      "incident": boolean
      // End of list of possible types for union field _incident.
    
      // Union field _assignee can be only one of the following:
      "assignee": string
      // End of list of possible types for union field _assignee.
    
      // Union field _description can be only one of the following:
      "description": string
      // End of list of possible types for union field _description.
    
      // Union field _type can be only one of the following:
      "type": enum ([CaseType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseType))
      // End of list of possible types for union field _type.
    
      // Union field _environment can be only one of the following:
      "environment": string
      // End of list of possible types for union field _environment.
    
      // Union field _move_environment can be only one of the following:
      "moveEnvironment": {
        object ([MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.MoveEnvironment))
      }
      // End of list of possible types for union field _move_environment.
    
      // Union field _score can be only one of the following:
      "score": number
      // End of list of possible types for union field _score.
    
      // Union field _sla can be only one of the following:
      "sla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla))
      }
      // End of list of possible types for union field _sla.
    
      // Union field _involved_suspicious_entity can be only one of the following:
      "involvedSuspiciousEntity": boolean
      // End of list of possible types for union field _involved_suspicious_entity.
    
      // Union field _closure_details can be only one of the following:
      "closureDetails": {
        object ([CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosureDetails))
      }
      // End of list of possible types for union field _closure_details.
    }  
  
Fields  
---  
`projectId` |  `string` Required. Google Cloud project ID.  
`customerId` |  `string` Required. Chronicle customer ID.  
`region` |  `string` Required. Chronicle region (e.g., "us", "europe").  
`caseId` |  `string` Required. The numeric ID of the Case to update (e.g., `12345`).  
`tags[]` |  `object (`[CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseTag)`)` CaseTags associated with the case.  
`products[]` |  `object (`[CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseProduct)`)` Products associated with the case.  
Union field `_display_name`.`_display_name` can be only one of the following:  
`displayName` |  `string` The new display name for the case.  
Union field `_stage`.`_stage` can be only one of the following:  
`stage` |  `string` The new stage of the case. The Stage options are: ['Research', 'Improvement', 'Incident', 'Investigation', 'Assessment', 'Triage'].  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority)`)` The new priority of the case (e.g., "PRIORITY_HIGH", "PRIORITY_CRITICAL").  
Union field `_important`.`_important` can be only one of the following:  
`important` |  `boolean` Whether the case is marked as important.  
Union field `_incident`.`_incident` can be only one of the following:  
`incident` |  `boolean` Whether the case is marked as an incident.  
Union field `_assignee`.`_assignee` can be only one of the following:  
`assignee` |  `string` The user or role to assign to the case. This can be a user or a @SocRole, default value is the default soc-role defined in Settings.  
Union field `_description`.`_description` can be only one of the following:  
`description` |  `string` The new description for the case. Limit chars to 1000.  
Union field `_type`.`_type` can be only one of the following:  
`type` |  `enum (`[CaseType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseType)`)` Case type  
Union field `_environment`.`_environment` can be only one of the following:  
`environment` |  `string` The environment associated with the case.  
Union field `_move_environment`.`_move_environment` can be only one of the following:  
`moveEnvironment` |  `object (`[MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.MoveEnvironment)`)` Details about moving the case to a different environment.  
Union field `_score`.`_score` can be only one of the following:  
`score` |  `number` Attack exposure score, how risky the case.  
Union field `_sla`.`_sla` can be only one of the following:  
`sla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla)`)` SLA for the case.  
Union field `_involved_suspicious_entity`.`_involved_suspicious_entity` can be only one of the following:  
`involvedSuspiciousEntity` |  `boolean` If has involved suspicious entity in the case.  
Union field `_closure_details`.`_closure_details` can be only one of the following:  
`closureDetails` |  `object (`[CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosureDetails)`)` Case closure details.  
  
### MoveEnvironment

JSON representation  
---  
      
    
    {
      "shouldDeleteOldCase": boolean
    }  
  
Fields  
---  
`shouldDeleteOldCase` |  `boolean` Optional. If the case should be deleted on move to the new environment.  
  
### Sla

JSON representation  
---  
      
    
    {
      "expirationTime": string,
      "criticalExpirationTime": string,
      "expirationStatus": enum ([SlaExpirationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.SlaExpirationStatus)),
      "remainingTimeSinceLastPause": integer
    }  
  
Fields  
---  
`expirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA expiration time in unix format as milliseconds. Old prop: SlaExpiration.  
`criticalExpirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA critical expiration time in unix format as milliseconds, old prop: SlaCriticalExpiration.  
`expirationStatus` |  `enum (`[SlaExpirationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.SlaExpirationStatus)`)` Output only. SLA expiration status.  
`remainingTimeSinceLastPause` |  `integer` Output only. Remaining time since last pause.  
  
### CaseTag

JSON representation  
---  
      
    
    {
      "displayName": string,
      "alert": string,
    
      // Union field _priority can be only one of the following:
      "priority": integer
      // End of list of possible types for union field _priority.
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The name of the tag  
`alert` |  `string` Output only. For tags set by playbook action, this is relevant during MoveAlert. Replaces old property: "Indicator".  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `integer` Output only. During ingestion if more than one tag matches the criteria, the one with the priority will be chosen. Available options: 1-5.  
  
### CaseProduct

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
  
### CaseClosureDetails

JSON representation  
---  
      
    
    {
      "reason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CloseReason)),
      "rootCause": string,
      "caseClosedAction": enum ([CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosedAction)),
      "comment": string
    }  
  
Fields  
---  
`reason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CloseReason)`)` Output only. Case closure reason.  
`rootCause` |  `string` Output only. Case closure root cause.  
`caseClosedAction` |  `enum (`[CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosedAction)`)` Output only. Case closed action.  
`comment` |  `string` Output only. Case closure comment.  
  
### Priority

Priority that is assigned to a Case or Alert.

Enums  
---  
`PRIORITY_UNSPECIFIED` | Default priority level.  
`PRIORITY_INFO` | Informational priority.  
`PRIORITY_LOW` | Low priority.  
`PRIORITY_MEDIUM` | Medium priority.  
`PRIORITY_HIGH` | High priority.  
`PRIORITY_CRITICAL` | Critical priority.  
  
### CaseType

Case type. LINT.IfChange(case_type)

Enums  
---  
`CASE_TYPE_UNSPECIFIED` | Unspecified case type.  
`EXTERNAL` | Case created based on alerts from external SIEM.  
`TEST` | Case created based on simulated alerts for testing.  
`REQUEST` | Case created internally through the Homepage feature.  
  
### SlaExpirationStatus

SLA status.

Enums  
---  
`SLA_EXPIRATION_STATUS_UNSPECIFIED` | Unspecified SLA status.  
`PASSED_DUE` | SLA has passed due.  
`OPEN_SLA` | SLA is open.  
`NO_SLA` | SLA is not set.  
`CRITICAL_EXPIRED` | SLA is critical and has expired.  
`PAUSED` | SLA is paused.  
  
### CloseReason

Case closure reason. LINT.IfChange(close_reason)

Enums  
---  
`CLOSE_REASON_UNSPECIFIED` | Unspecified close reason.  
`MALICIOUS` | Case is malicious.  
`NOT_MALICIOUS` | Case is not malicious.  
`MAINTENANCE` | Case is in maintenance.  
`INCONCLUSIVE` | Case is inconclusive.  
`UNKNOWN` | Case closure reason is unknown.  
  
### CaseClosedAction

Case closed action. LINT.IfChange(case_closed_action)

Enums  
---  
`CASE_CLOSED_ACTION_UNSPECIFIED` | Unspecified case closed action.  
`AUTOMATIC` | Case closed action is automatic.  
`MANUALLY` | Case closed action is manually.  
  
## Output Schema

A Case represents a security investigation in SecOps. Cases group related alerts and provide a central location for analysts to document their findings, track progress, and collaborate on resolving security incidents.

### Case

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
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority)),
      "assignee": string,
      "assignedUser": string,
      "description": string,
      "type": enum ([CaseType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseType)),
      "environment": string,
      "status": enum ([CaseStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseStatus)),
      "score": number,
      "workflowStatus": enum ([WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.WorkflowStatus)),
      "sla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla))
      },
      "alertsSla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla))
      },
      "source": string,
      "tags": [
        {
          object ([CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseTag))
        }
      ],
      "products": [
        {
          object ([CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseProduct))
        }
      ],
      "closureDetails": {
        object ([CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosureDetails))
      },
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Task))
        }
      ],
      "moveEnvironment": {
        object ([MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.MoveEnvironment))
      },
      "dataAccessScopes": [
        string
      ],
      "customFieldValues": [
        {
          object ([CustomFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CustomFieldValue))
        }
      ],
    
      // Union field _important can be only one of the following:
      "important": boolean
      // End of list of possible types for union field _important.
    
      // Union field _incident can be only one of the following:
      "incident": boolean
      // End of list of possible types for union field _incident.
    
      // Union field _overflow_case can be only one of the following:
      "overflowCase": boolean
      // End of list of possible types for union field _overflow_case.
    
      // Union field _involved_suspicious_entity can be only one of the following:
      "involvedSuspiciousEntity": boolean
      // End of list of possible types for union field _involved_suspicious_entity.
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
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Priority)`)` Required. Default value is HIGH. Case priority. For example, "Informative", "Low", "Medium", "High", "Critical".  
`assignee` |  `string` Optional. This can be a user or a @SocRole, default value is the default soc-role defined in Settings.  
`assignedUser` |  `string` Output only. Resource association for the assignee.  
`description` |  `string` Optional. Case description. Limit chars to 1000.  
`type` |  `enum (`[CaseType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseType)`)` Required. Case type.  
`environment` |  `string` Required. Case logical environments.  
`status` |  `enum (`[CaseStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseStatus)`)` Output only. Case data status.  
`score` |  `number` Optional. Attack exposure score, how risky the case.  
`workflowStatus` |  `enum (`[WorkflowStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.WorkflowStatus)`)` Output only. Case playbook status.  
`sla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla)`)` Optional. SLA for the case.  
`alertsSla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Sla)`)` Optional. Aggregated alerts SLA. (alert has SLA as well).  
`source` |  `string` Output only. The source that created the case. Possible values: "Server", "User", "Simulated", "Merge", "AlertMove"  
`tags[]` |  `object (`[CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseTag)`)` Optional. CaseTags associated with the case.  
`products[]` |  `object (`[CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseProduct)`)` Optional. Products associated with the case. Contains Name of product (e.g. WinEventLog:Security/DLP_Product). Replaces old property: "Product".  
`closureDetails` |  `object (`[CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosureDetails)`)` Optional. Case closure details.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Task)`)` Output only. Tasks associated with the case.  
`moveEnvironment` |  `object (`[MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.MoveEnvironment)`)` Optional. Case environment move details.  
`dataAccessScopes[]` |  `string` Output only. Data Access Scopes.  
`customFieldValues[]` |  `object (`[CustomFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CustomFieldValue)`)` Optional. Custom field values associated with the case.  
Union field `_important`.`_important` can be only one of the following:  
`important` |  `boolean` Optional. Additional way to specify case importance. The default is false.  
Union field `_incident`.`_incident` can be only one of the following:  
`incident` |  `boolean` Optional. Additional way to specify if the case marked as incident. The default is false.  
Union field `_overflow_case`.`_overflow_case` can be only one of the following:  
`overflowCase` |  `boolean` Output only. Case without events, was reduced by the connector service due to a large amount of data. During ingestion if the "alert package" crosses a specific threshold, the alert will be trimmed due to security reasons (DDOS attacks, etc..)  
Union field `_involved_suspicious_entity`.`_involved_suspicious_entity` can be only one of the following:  
`involvedSuspiciousEntity` |  `boolean` Optional. If has involved suspicious entity in the case.  
  
### Sla

JSON representation  
---  
      
    
    {
      "expirationTime": string,
      "criticalExpirationTime": string,
      "expirationStatus": enum ([SlaExpirationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.SlaExpirationStatus)),
      "remainingTimeSinceLastPause": integer
    }  
  
Fields  
---  
`expirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA expiration time in unix format as milliseconds. Old prop: SlaExpiration.  
`criticalExpirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA critical expiration time in unix format as milliseconds, old prop: SlaCriticalExpiration.  
`expirationStatus` |  `enum (`[SlaExpirationStatus](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.SlaExpirationStatus)`)` Output only. SLA expiration status.  
`remainingTimeSinceLastPause` |  `integer` Output only. Remaining time since last pause.  
  
### CaseTag

JSON representation  
---  
      
    
    {
      "displayName": string,
      "alert": string,
    
      // Union field _priority can be only one of the following:
      "priority": integer
      // End of list of possible types for union field _priority.
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The name of the tag  
`alert` |  `string` Output only. For tags set by playbook action, this is relevant during MoveAlert. Replaces old property: "Indicator".  
Union field `_priority`.`_priority` can be only one of the following:  
`priority` |  `integer` Output only. During ingestion if more than one tag matches the criteria, the one with the priority will be chosen. Available options: 1-5.  
  
### CaseProduct

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
  
### CaseClosureDetails

JSON representation  
---  
      
    
    {
      "reason": enum ([CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CloseReason)),
      "rootCause": string,
      "caseClosedAction": enum ([CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosedAction)),
      "comment": string
    }  
  
Fields  
---  
`reason` |  `enum (`[CloseReason](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CloseReason)`)` Output only. Case closure reason.  
`rootCause` |  `string` Output only. Case closure root cause.  
`caseClosedAction` |  `enum (`[CaseClosedAction](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CaseClosedAction)`)` Output only. Case closed action.  
`comment` |  `string` Output only. Case closure comment.  
  
### Task

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "createTime": string,
      "updateTime": string,
      "content": string,
      "dueTime": string,
      "title": string,
      "author": string,
      "lastAuthor": string,
      "assignee": string,
      "status": enum ([Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Status)),
      "resolver": string,
      "comment": string,
      "resolutionTime": string,
      "caseId": integer,
    
      // Union field _favorite can be only one of the following:
      "favorite": boolean
      // End of list of possible types for union field _favorite.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the task. Format: projects/{project}/locations/{location}/instances/{instance}/tasks/{task}  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique ID of the task.  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the task.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The last update time of the task.  
`content` |  `string` Required. The task content, limited to 4096 characters.  
`dueTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The due time for the task in ms. When specified during task creation, must be in the future. Is optional as deadlines can exist without a specific scheduled time.  
`title` |  `string` Required. The task title, minimum length of 3 characters and maximum of 50 characters.  
`author` |  `string` Output only. The user who created the task.  
`lastAuthor` |  `string` Output only. The last editor of the task.  
`assignee` |  `string` Required. The assignee of the task.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.Status)`)` Required. The status of the task. todo change to task startus enum  
`resolver` |  `string` Output only. The user who resolved the task.  
`comment` |  `string` Required. Comment added during task resolution, limited to 4096 characters.  
`resolutionTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The resolution time of the task in ms.  
`caseId` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Optional. Associated case id (if task is related to a specific case) Can be optional as tasks may exist independently or be associated with a specific case.  
Union field `_favorite`.`_favorite` can be only one of the following:  
`favorite` |  `boolean` Optional. Determines whether the task is marked as favorite.  
  
### MoveEnvironment

JSON representation  
---  
      
    
    {
      "shouldDeleteOldCase": boolean
    }  
  
Fields  
---  
`shouldDeleteOldCase` |  `boolean` Optional. If the case should be deleted on move to the new environment.  
  
### CustomFieldValue

JSON representation  
---  
      
    
    {
      "name": string,
      "customFieldId": string,
      "scope": enum ([CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CustomFieldScope)),
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
`scope` |  `enum (`[CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/get_case#Output.Schema.CustomFieldScope)`)` Output only. Scope of the value.  
`scopeId` |  `string` Required. Identifier of the value referencing case or alert.  
`values[]` |  `string` Required. The custom field value.  
`valuesSearchText` |  `string` Output only. Specific field represents the `values` field for faster search.  
  
### Priority

Priority that is assigned to a Case or Alert.

Enums  
---  
`PRIORITY_UNSPECIFIED` | Default priority level.  
`PRIORITY_INFO` | Informational priority.  
`PRIORITY_LOW` | Low priority.  
`PRIORITY_MEDIUM` | Medium priority.  
`PRIORITY_HIGH` | High priority.  
`PRIORITY_CRITICAL` | Critical priority.  
  
### CaseType

Case type. LINT.IfChange(case_type)

Enums  
---  
`CASE_TYPE_UNSPECIFIED` | Unspecified case type.  
`EXTERNAL` | Case created based on alerts from external SIEM.  
`TEST` | Case created based on simulated alerts for testing.  
`REQUEST` | Case created internally through the Homepage feature.  
  
### CaseStatus

Case status.

Enums  
---  
`CASE_DATA_STATE_UNSPECIFIED` | Unspecified case data status.  
`OPENED` | Case data is opened.  
`CLOSED` | Case data is closed.  
`ALL` | Case data is all.  
`MERGED` | Case data is merged.  
`CREATION_PENDING` | Case data is creation pending.  
  
### WorkflowStatus

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
  
### SlaExpirationStatus

SLA status.

Enums  
---  
`SLA_EXPIRATION_STATUS_UNSPECIFIED` | Unspecified SLA status.  
`PASSED_DUE` | SLA has passed due.  
`OPEN_SLA` | SLA is open.  
`NO_SLA` | SLA is not set.  
`CRITICAL_EXPIRED` | SLA is critical and has expired.  
`PAUSED` | SLA is paused.  
  
### CloseReason

Case closure reason. LINT.IfChange(close_reason)

Enums  
---  
`CLOSE_REASON_UNSPECIFIED` | Unspecified close reason.  
`MALICIOUS` | Case is malicious.  
`NOT_MALICIOUS` | Case is not malicious.  
`MAINTENANCE` | Case is in maintenance.  
`INCONCLUSIVE` | Case is inconclusive.  
`UNKNOWN` | Case closure reason is unknown.  
  
### CaseClosedAction

Case closed action. LINT.IfChange(case_closed_action)

Enums  
---  
`CASE_CLOSED_ACTION_UNSPECIFIED` | Unspecified case closed action.  
`AUTOMATIC` | Case closed action is automatic.  
`MANUALLY` | Case closed action is manually.  
  
### Status

The current status of the task.

Enums  
---  
`STATUS_UNSPECIFIED` | The task status is unspecified/unknown.  
`PENDING` | The task status is pending.  
`COMPLETED` | The task status is completed.  
  
### CustomFieldScope

Whether the custom field is associated with an alert or a case.

Enums  
---  
`CUSTOM_FIELD_SCOPE_UNSPECIFIED` | Unspecified scope.  
`ALERT` | Belnogs to Alert scope.  
`CASE` | Belongs to Case scope.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
