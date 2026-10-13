---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:29.572259+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_case`

Retrieves a single case by its resource name.

Fetches all details for a specific case, including its properties (such as priority, stage, and assignee), as well as any associated tasks, tags, and products. This tool is fundamental for drilling down into a specific incident after identifying it through a list view or search.

**CRITICAL INSTRUCTION:** When using this tool, you **MUST ALWAYS** also call the `list_case_alerts` tool for the same case ID to fetch the associated alerts. You must then synthesize the information from both tools to provide a comprehensive response. The response should include case details, associated alerts, and a summary of comments if available.

Here are the details for Case ID [Case ID]:

Case Details:

Name: [Name] Display Name: [Display Name] Status: [Status] Stage: [Stage] Priority: [Priority] Assignee: [Assignee] Last Modifying User ID: [Last Modifying User ID] Created Time: [Create Time] Updated Time: [Update Time] Alert Count: [Alert Count (calculate from list_case_alerts)] Important: [Important] Incident: [Incident] Type: [Type] Overflow Case: [Overflow Case] Environment: [Environment] Workflow Status: [Workflow Status] Source: [Source] Involved Suspicious Entity: [Involved Suspicious Entity] Move Environment: [Move Environment]

Associated Alerts:

Alert ID: [Alert ID] Display Name: [Alert Display Name] Rule Generator: [Rule Generator] Product: [Product] Vendor: [Vendor] Source System: [Source System (if available)] Priority: [Priority] Status: [Status] Start Time: [Start Time (if available)] End Time: [End Time (if available)] Source URL: [Source URL (if available)]

Comments: There are [Number of comments] comments associated with this case, including notes about [Topic 1], [Topic 2], and entries like "[Comment Snippet]" by [Author].

Example: There are 23 comments associated with this case, including notes about Meta-Analysis Reports, Triage Reports, and entries like "OneMCP works!" by Soary Siem.

**Workflow Integration:** \- Used when an analyst clicks on a case in a queue or dashboard to view its full details in an investigation UI. - Essential for automated playbooks that need to retrieve the current state of a case before taking action, such as enrichment or remediation. - Provides the necessary data to populate a case investigation screen, showing all relevant information in one place. - Can be used to verify the result of an update operation by fetching the case after the update has been applied.

**Use Cases:** \- An analyst retrieves a case to begin an investigation and understand its context. - An automated system fetches a case to extract entities for further enrichment from other threat intelligence sources. - A manager views a case to review its progress, check the SLA status, and see the latest comments. - A reporting script fetches case details to generate a detailed incident report.

Args: project_id (str): Google Cloud project ID (required). customer_id (str): Chronicle customer ID (required). region (str): Chronicle region (e.g., "us", "europe") (required). case_id (str): The numeric ID of the Case to retrieve (e.g., '12345'). This is a required field. expand (str, optional): A comma-separated list of related resources to include in the response. This allows you to get a more complete picture of the case in a single call. Supported values: 'tasks', 'tags', 'products'.

Returns: Case: The full Case object with all its details. If the 'expand' parameter is used, the corresponding related resources will be included. The Case object contains the following key fields: - `Name` (str): The full resource name of the case. - `Id` (int): The unique identifier for the case. - `DisplayName` (str): The title or display name of the case. - `Stage` (str): The current stage of the case (e.g., "Triage", "Investigation"). - `Priority` (str): The priority of the case (e.g., "PRIORITY_HIGH"). - `Assignee` (str): The user or group assigned to the case. - `Description` (str): A detailed description of the case. - `Status` (str): The current status of the case (e.g., "OPENED", "CLOSED"). - `CreateTime` (int): The creation timestamp of the case in milliseconds. - `UpdateTime` (int): The last update timestamp of the case in milliseconds. - `Tags` (list of str): A list of tags associated with the case. - `Products` (list of str): A list of products associated with the case. Returns an error message if the case is not found or the user does not have permission to view it.

Example Usage: # Get basic details for a specific case (and automatically fetch alerts as per instruction) get_case(project_id='123', region='us', customer_id='abc', case_id='456')
    
    
    # Get a case and include its associated tasks and tags
            get_case(project_id='123', region='us', customer_id='abc', case_id='456', expand='tasks,tags')
            

Next Steps (using MCP-enabled tools): - Use 'list_case_alerts' to fetch the details of all alerts associated with this case. - Use 'list_case_comments' to see the full history of comments and actions taken on the case.

The following sample demonstrate how to use `curl` to invoke the `get_case` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_case",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for GetCase. Next ID: 6

### GetCaseRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "caseId": string,
      "expand": string
    }  
  
Fields  
---  
`projectId` |  `string` Project ID of the customer.  
`customerId` |  `string` Customer ID of the customer.  
`region` |  `string` Region of the customer.  
`caseId` |  `string` Case ID of the case to get.  
`expand` |  `string` Expand the case to include all the related cases.  
  
## Output Schema

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Cases provides analysts a way to investigate incoming security alerts and safeguard workstations. Cases are generated by alerts from the SIEM platform. Further alerts linked to the same entities may be grouped into an existing case based on a flexible configuration. In addition, analysts can create manual cases and simulated cases and ingest specific data.

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
      "priority": enum (Priority),
      "assignee": string,
      "assignedUser": string,
      "description": string,
      "type": enum (CaseType),
      "environment": string,
      "moveEnvironment": {
        object ([MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.MoveEnvironment))
      },
      "status": enum (CaseStatus),
      "score": number,
      "workflowStatus": enum (WorkflowStatus),
      "sla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Sla))
      },
      "alertsSla": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Sla))
      },
      "source": string,
      "tags": [
        {
          object ([CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseTag))
        }
      ],
      "products": [
        {
          object ([CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseProduct))
        }
      ],
      "closureDetails": {
        object ([CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseClosureDetails))
      },
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Task))
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
`priority` |  `enum (`Priority`)` Required. Default value is HIGH. Case priority. For example, "Informative", "Low", "Medium", "High", "Critical".  
`assignee` |  `string` Optional. This can be a user or a @SocRole, default value is the default soc-role defined in Settings.  
`assignedUser` |  `string` Output only. Resource association for the assignee.  
`description` |  `string` Optional. Case description. Limit chars to 1000.  
`type` |  `enum (`CaseType`)` Required. Case type.  
`environment` |  `string` Required. Case logical environments.  
`moveEnvironment` |  `object (`[MoveEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.MoveEnvironment)`)` Optional. Case environment move details.  
`status` |  `enum (`CaseStatus`)` Output only. Case data status.  
`score` |  `number` Optional. Attack exposure score, how risky the case.  
`workflowStatus` |  `enum (`WorkflowStatus`)` Output only. Case playbook status.  
`sla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Sla)`)` Optional. SLA for the case.  
`alertsSla` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Sla)`)` Optional. Aggregated alerts SLA. (alert has SLA as well).  
`source` |  `string` Output only. The source that created the case. Possible values: "Server", "User", "Simulated", "Merge", "AlertMove"  
`tags[]` |  `object (`[CaseTag](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseTag)`)` Optional. CaseTags associated with the case.  
`products[]` |  `object (`[CaseProduct](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseProduct)`)` Optional. Products associated with the case. Contains Name of product (e.g. WinEventLog:Security/DLP_Product). Replaces old property: "Product".  
`closureDetails` |  `object (`[CaseClosureDetails](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.CaseClosureDetails)`)` Optional. Case closure details.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/chronicle/docs/reference/mcp/get_case#Output.Schema.Task)`)` Output only. Tasks associated with the case.  
Union field `_important`.`_important` can be only one of the following:  
`important` |  `boolean` Optional. Additional way to specify case importance. The default is false.  
Union field `_incident`.`_incident` can be only one of the following:  
`incident` |  `boolean` Optional. Additional way to specify if the case marked as incident. The default is false.  
Union field `_overflow_case`.`_overflow_case` can be only one of the following:  
`overflowCase` |  `boolean` Output only. Case without events, was reduced by the connector service due to a large amount of data. During ingestion if the "alert package" crosses a specific threshold, the alert will be trimmed due to security reasons (DDOS attacks, etc..)  
Union field `_involved_suspicious_entity`.`_involved_suspicious_entity` can be only one of the following:  
`involvedSuspiciousEntity` |  `boolean` Optional. If has involved suspicious entity in the case.  
  
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
      "expirationStatus": enum (SlaExpirationStatus),
      "remainingTimeSinceLastPause": integer
    }  
  
Fields  
---  
`expirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA expiration time in unix format as milliseconds. Old prop: SlaExpiration.  
`criticalExpirationTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. SLA critical expiration time in unix format as milliseconds, old prop: SlaCriticalExpiration.  
`expirationStatus` |  `enum (`SlaExpirationStatus`)` Output only. SLA expiration status.  
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
      "reason": enum (CloseReason),
      "rootCause": string,
      "caseClosedAction": enum (CaseClosedAction),
      "comment": string
    }  
  
Fields  
---  
`reason` |  `enum (`CloseReason`)` Output only. Case closure reason.  
`rootCause` |  `string` Output only. Case closure root cause.  
`caseClosedAction` |  `enum (`CaseClosedAction`)` Output only. Case closed action.  
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
      "status": enum (Status),
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
`status` |  `enum (`Status`)` Required. The status of the task. todo change to task startus enum  
`resolver` |  `string` Output only. The user who resolved the task.  
`comment` |  `string` Required. Comment added during task resolution, limited to 4096 characters.  
`resolutionTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The resolution time of the task in ms.  
`caseId` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Optional. Associated case id (if task is related to a specific case) Can be optional as tasks may exist independently or be associated with a specific case.  
Union field `_favorite`.`_favorite` can be only one of the following:  
`favorite` |  `boolean` Optional. Determines whether the task is marked as favorite.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
