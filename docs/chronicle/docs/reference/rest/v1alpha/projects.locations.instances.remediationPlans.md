---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans
title: REST Resource: projects.locations.instances.remediationPlans \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:32.044493+00:00
---

# REST Resource: projects.locations.instances.remediationPlans  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.remediationPlans Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RemediationPlan
    * JSON representation
  * RemediationPlanState
  * RemediationPlanTriggerType
  * RemediationPlanExecution
    * JSON representation
  * RemediationPlanExecutionState
  * RemediationPlanExecutionSummaryState
  * Methods



## Resource: RemediationPlan

Represents an AI-driven Remediation Plan for a specific alert or case.

JSON representation  
---  
      
    
    {
      "name": string,
      "alertName": string,
      "caseId": integer,
      "alertId": string,
      "siemAlertId": string,
      "agentSessionId": string,
      "state": enum ([RemediationPlanState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanState)),
      "triggerType": enum ([RemediationPlanTriggerType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanTriggerType)),
      "statusDetails": string,
      "agentClassifiedUseCase": string,
      "planData": {
        object
      },
      "planMetadata": {
        object
      },
      "createTime": string,
      "updateTime": string,
      "actions": [
        {
          object ([RemediationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction))
        }
      ],
      "latestExecution": {
        object ([RemediationPlanExecution](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecution))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the remediation plan.  
`alertName` |  `string` Optional. The name of the alert.  
`caseId` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Optional. The Case identifier.  
`alertId` |  `string` Optional. The Alert identifier.  
`siemAlertId` |  `string` Optional. The SIEM Alert identifier.  
`agentSessionId` |  `string` Optional. The context id of the REMa session.  
`state` |  `enum (`[RemediationPlanState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanState)`)` Output only. Current plan status.  
`triggerType` |  `enum (`[RemediationPlanTriggerType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanTriggerType)`)` Optional. How the plan was triggered.  
`statusDetails` |  `string` Optional. Detailed status information (e.g., error logs).  
`agentClassifiedUseCase` |  `string` Optional. The use cases classified by the agent (e.g. "Phishing", "Malware").  
`planData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Complete plan details presented in the UI (contains 'planning_summary', 'error', etc.).  
`planMetadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Metadata about the plan, such as token usage.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Modification time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`actions[]` |  `object (`[RemediationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction)`)` Optional. The actions defined/suggested for this remediation plan.  
`latestExecution` |  `object (`[RemediationPlanExecution](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecution)`)` Output only. Reference to the most recent execution run for this remediation plan.  
  
## RemediationPlanState

The state Of the Renediation plan.

Enums  
---  
`REMEDIATION_PLAN_STATE_UNSPECIFIED` | Unspecified status.  
`REMEDIATION_PLAN_STATE_INITIALIZED` | Set when initializing the remediation planning process.  
`REMEDIATION_PLAN_STATE_REQUESTED` | Set before calling the REMa planning service in the Python service.  
`REMEDIATION_PLAN_STATE_SUGGESTED` | Plan successfully generated and suggested by REMa.  
`REMEDIATION_PLAN_STATE_ERROR` | Execution or generation failed with an error.  
`REMEDIATION_PLAN_STATE_APPROVED` | Approved by SOC analyst / user.  
`REMEDIATION_PLAN_STATE_DECLINED` | Declined by SOC analyst / user.  
  
## RemediationPlanTriggerType

The trigger type of the Remediation plan.

Enums  
---  
`REMEDIATION_PLAN_TRIGGER_TYPE_UNSPECIFIED` | Unspecified trigger type.  
`REMEDIATION_PLAN_TRIGGER_TYPE_AUTOMATIC` | Process was automatically kicked off by a detection, alert, or system event.  
`REMEDIATION_PLAN_TRIGGER_TYPE_MANUAL` | Process was initialized as a step within a defined Playbook.  
  
## RemediationPlanExecution

Represents a single execution instance of a Remediation Plan.

JSON representation  
---  
      
    
    {
      "remediationPlan": string,
      "state": enum ([RemediationPlanExecutionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecutionState)),
      "summaryStatus": enum ([RemediationPlanExecutionSummaryState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecutionSummaryState)),
      "actionsCount": integer,
      "pendingActionCount": integer,
      "successActionsCount": integer,
      "failureActionsCount": integer,
      "summary": string,
      "additionalData": {
        object
      },
      "metadata": {
        object
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`remediationPlan` |  `string` Required. Foreign key referring to the associated RemediationPlan.  
`state` |  `enum (`[RemediationPlanExecutionState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecutionState)`)` Output only. Execution status of the overall plan.  
`summaryStatus` |  `enum (`[RemediationPlanExecutionSummaryState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans#RemediationPlanExecutionSummaryState)`)` Output only. Summary status of the plan.  
`actionsCount` |  `integer` Output only. Performance counters for actions.  
`pendingActionCount` |  `integer` Output only. Number of actions to execute.  
`successActionsCount` |  `integer` Output only. Successful actions count.  
`failureActionsCount` |  `integer` Output only. Failed actions count.  
`summary` |  `string` Output only. Narrative execution summary.  
`additionalData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional unstructured data.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Metadata for the execution.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RemediationPlanExecutionState

Models the 'RemediationPlanExecutions' database table.

Enums  
---  
`REMEDIATION_PLAN_EXECUTION_STATE_UNSPECIFIED` | Unspecified status.  
`REMEDIATION_PLAN_EXECUTION_STATE_IN_PROGRESS` | plan execution started  
`REMEDIATION_PLAN_EXECUTION_STATE_EXECUTED` | All actions in the plan executed. see action's status for more information  
`REMEDIATION_PLAN_EXECUTION_STATE_REJECTED` | The execution request was rejected (e.g., status declined).  
`REMEDIATION_PLAN_EXECUTION_STATE_ERROR` | Plan execution failed with an error.  
  
## RemediationPlanExecutionSummaryState

Summary state of the Remediation Plan Execution.

Enums  
---  
`REMEDIATION_PLAN_EXECUTION_SUMMARY_STATE_UNSPECIFIED` | Unspecified standard status.  
`REMEDIATION_PLAN_EXECUTION_SUMMARY_STATE_IN_PROGRESS` | plan execution started  
`REMEDIATION_PLAN_EXECUTION_SUMMARY_STATE_EXECUTED` | All actions in the plan executed. see action's status for more information  
`REMEDIATION_PLAN_EXECUTION_SUMMARY_STATE_REJECTED` | The execution request was rejected (e.g., status declined).  
`REMEDIATION_PLAN_EXECUTION_SUMMARY_STATE_ERROR` | Plan execution failed with an error.  
  
## Methods  
  
---  
  
### `[execute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans/execute)`

|  Executes a suggested Remediation Plan.  
  
### `[generate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans/generate)`

|  Triggers Remediation agent and saves its output as a Remediation Plan.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans/get)`

|  Retrieves a specific self-contained Remediation Plan.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans/list)`

|  Lists Remediation Plans with optional filtering.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans/patch)`

|  Updates a Remediation Plan.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
