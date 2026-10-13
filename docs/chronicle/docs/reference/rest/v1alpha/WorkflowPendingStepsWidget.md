---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget/
title: WorkflowPendingStepsWidget \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:48.586979+00:00
---

# WorkflowPendingStepsWidget  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  WorkflowPendingStepsWidget Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * WorkflowPendingStep
    * JSON representation
  * PendingStepStatus
  * PendingStepSecurityEntity
    * JSON representation
  * PendingStepSecurityEntityPropertyValue
    * JSON representation
  * PendingStepActionDefinition
    * JSON representation
  * PendingStepActionDefinitionParameter
    * JSON representation
  * PendingStepActionDefinitionParameterType
  * ActionIntegrationInstance
    * JSON representation
  * WorkflowPendingStepInstance
    * JSON representation
  * WorkflowStepType
  * WorkflowStepParameter
    * JSON representation
  * WorkflowStepParameterType



Workflow pending step widget.

JSON representation  
---  
      
    
    {
      "pendingSteps": [
        {
          object ([WorkflowPendingStep](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowPendingStep))
        }
      ],
      "title": string,
      "order": integer,
      "type": enum ([WidgetTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetTemplateType)),
      "gridColumns": enum ([WidgetTemplateGridColumns](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetTemplateGridColumns)),
      "description": string,
      "identifier": string,
      "jsonData": string,
      "errorJsonData": string,
      "resultStatus": enum ([WidgetResultStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetResultStatus))
    }  
  
Fields  
---  
`pendingSteps[]` |  `object (`[WorkflowPendingStep](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowPendingStep)`)` Output only. The list of pending steps.  
`title` |  `string` Output only. The widget title.  
`order` |  `integer` Output only. The widget order.  
`type` |  `enum (`[WidgetTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetTemplateType)`)` Output only. The widget template type.  
`gridColumns` |  `enum (`[WidgetTemplateGridColumns](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetTemplateGridColumns)`)` Output only. The widget template grid columns.  
`description` |  `string` Output only. The widget description.  
`identifier` |  `string` Output only. The widget identifier.  
`jsonData` |  `string` Output only. The widget json data.  
`errorJsonData` |  `string` Output only. The widget error json data.  
`resultStatus` |  `enum (`[WidgetResultStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetResultStatus)`)` Output only. The widget result status.  
  
## WorkflowPendingStep

Workflow pending step.

JSON representation  
---  
      
    
    {
      "workflowIdentifier": string,
      "parentWorkflowIdentifier": string,
      "workflowInstanceIdentifier": integer,
      "caseId": integer,
      "indicatorIdentifier": string,
      "alertGroupIdentifier": string,
      "status": enum ([PendingStepStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepStatus)),
      "executingUser": string,
      "resultCode": integer,
      "message": string,
      "resultValue": string,
      "results": [
        {
          object ([ScriptResultEntityData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ScriptResultEntityData))
        }
      ],
      "targetEntities": [
        {
          object ([PendingStepSecurityEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntity))
        }
      ],
      "resultEntities": [
        {
          object ([PendingStepSecurityEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntity))
        }
      ],
      "properties": {
        string: string,
        ...
      },
      "actionDef": {
        object ([PendingStepActionDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinition))
      },
      "blockStepId": string,
      "jsonResultObject": string,
      "integrationInstanceIdentifier": string,
      "integrationInstanceName": string,
      "integrationInstanceEnvironment": string,
      "description": string,
      "pendingStepProperties": {
        object ([WorkflowPendingStepInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowPendingStepInstance))
      },
      "stepInstanceIdentifier": string,
      "identifier": string,
      "originalStepIdentifier": string,
      "isAutomatic": boolean,
      "isSkippable": boolean,
      "crationTimeUnixTimeInMs": string,
      "modifiedTimeUnixTimeInMs": string,
      "instanceName": string,
      "name": string,
      "integration": string,
      "actionProvider": string,
      "actionName": string,
      "type": enum ([WorkflowStepType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepType)),
      "parameters": [
        {
          object ([WorkflowStepParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepParameter))
        }
      ],
      "autoSkipOnFailure": boolean,
      "isDebugMockData": boolean,
      "allowedToExecute": boolean,
      "loopIteration": integer,
      "parentWorkflowLoopIteration": integer
    }  
  
Fields  
---  
`workflowIdentifier` |  `string` Output only. The workflow identifier associated with the pending step.  
`parentWorkflowIdentifier` |  `string` Output only. The parent workflow identifier associated with the pending step.  
`workflowInstanceIdentifier` |  `integer` Output only. The workflow instance identifier associated with the pending step.  
`caseId` |  `integer` Output only. The case id associated with the pending step.  
`indicatorIdentifier` |  `string` Output only. The identifier of the indicator associated with the pending step.  
`alertGroupIdentifier` |  `string` Output only. The alert group identifier associated with the pending step.  
`status` |  `enum (`[PendingStepStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepStatus)`)` Output only. The pending step status.  
`executingUser` |  `string` Output only. The user who is executing the pending step.  
`resultCode` |  `integer` Output only. The result code of the pending step.  
`message` |  `string` Output only. The result message of the pending step.  
`resultValue` |  `string` Output only. The result value of the pending step.  
`results[]` |  `object (`[ScriptResultEntityData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ScriptResultEntityData)`)` Output only. The result entity data of the pending step.  
`targetEntities[]` |  `object (`[PendingStepSecurityEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntity)`)` Output only. The target entities of the pending step.  
`resultEntities[]` |  `object (`[PendingStepSecurityEntity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntity)`)` Output only. The result entities of the pending step.  
`properties` |  `map (key: string, value: string)` Output only. The properties of the pending step.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`actionDef` |  `object (`[PendingStepActionDefinition](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinition)`)` Output only. The action definition of the pending step.  
`blockStepId` |  `string` Output only. The block step identifier of the workflow pending step.  
`jsonResultObject` |  `string` Output only. The json result object of the workflow pending step.  
`integrationInstanceIdentifier` |  `string` Output only. The integration instance identifier of the workflow pending step.  
`integrationInstanceName` |  `string` Output only. The integration instance name of the workflow pending step.  
`integrationInstanceEnvironment` |  `string` Output only. The integration instance environment of the workflow pending step.  
`description` |  `string` Output only. The integration instance description of workflow pending step.  
`pendingStepProperties` |  `object (`[WorkflowPendingStepInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowPendingStepInstance)`)` Output only. The pending step properties of the workflow pending step.  
`stepInstanceIdentifier` |  `string` Output only. The step instance identifier of the workflow pending step.  
`identifier` |  `string` Output only. The identifier of the workflow pending step.  
`originalStepIdentifier` |  `string` Output only. The identifier of the original workflow pending step.  
`isAutomatic` |  `boolean` Output only. The flag that indicates whether the workflow step is automatic or not.  
`isSkippable` |  `boolean` Output only. The flag that indicates whether the workflow step is skippable or not.  
`crationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time unix time in milliseconds of the workflow step.  
`modifiedTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modified time unix time in milliseconds of the workflow step.  
`instanceName` |  `string` Output only. The instance name of the workflow step.  
`name` |  `string` Output only. The name of the workflow step.  
`integration` |  `string` Output only. The integration of the workflow step.  
`actionProvider` |  `string` Output only. The action provider of the workflow step.  
`actionName` |  `string` Output only. The action name of the workflow step.  
`type` |  `enum (`[WorkflowStepType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepType)`)` Output only. The type of the workflow step.  
`parameters[]` |  `object (`[WorkflowStepParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepParameter)`)` Output only. The workflow step parameters.  
`autoSkipOnFailure` |  `boolean` Output only. The flag that indicates whether the workflow step is auto skip on failure or not.  
`isDebugMockData` |  `boolean` Output only. The flag that indicates whether the workflow step is debug mock data or not.  
`allowedToExecute` |  `boolean` Output only. The flag that indicates whether the pending step is allowed to execute.  
`loopIteration` |  `integer` Output only. The loop iteration of the workflow pending step.  
`parentWorkflowLoopIteration` |  `integer` Output only. The parent workflow loop iteration of the workflow pending step.  
  
## PendingStepStatus

Pending step action status.

Enums  
---  
`ACTION_STATUS_UNSPECIFIED` | Unspecified action status.  
`NO_STATUS` | Action is not started.  
`FAULTED` | Action is faulted.  
`IN_PROGRESS` | Action is in progress.  
`COMPLETED` | Action is completed.  
`PENDING_USER_INPUT` | Action is pending user input.  
`PENDING_PREVIOUS_STEPS` | Action is pending previous steps.  
`STARTED` | Action is started.  
`FAULTED_AND_SKIPPED` | Action is faulted and skipped.  
`HANDLED_TIMEDOUT` | Action is timed out.  
`UNHANDLED_TIMEDOUT` | Action is unhandled timed out.  
`TERMINATED` | Action is terminated.  
`NOT_RUN_AND_SKIPPED` | Action is not run and skipped.  
`PENDING_ACTION_TIMEOUT` | Action is pending action timeout.  
`PENDING_ACTION_TIMEOUT_AND_SKIPPED` | Action is pending action timeout and skipped.  
  
## PendingStepSecurityEntity

The pending step security entity.

JSON representation  
---  
      
    
    {
      "caseId": integer,
      "identifier": string,
      "entityType": string,
      "isInternal": boolean,
      "isSuspicious": boolean,
      "isArtifact": boolean,
      "isEnriched": boolean,
      "isVulnerable": boolean,
      "isPivot": boolean,
      "environment": string,
      "fields": [
        {
          object ([PendingStepSecurityEntityPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntityPropertyValue))
        }
      ],
      "isManuallyCreated": boolean
    }  
  
Fields  
---  
`caseId` |  `integer` Output only. The case id of the pending step.  
`identifier` |  `string` Output only. The identifier of the entity.  
`entityType` |  `string` Output only. The entity type of the entity.  
`isInternal` |  `boolean` Output only. The flag that indicates whether the entity is internal.  
`isSuspicious` |  `boolean` Output only. The flag that indicates whether the entity is suspicious.  
`isArtifact` |  `boolean` Output only. The flag that indicates whether the entity is an artifact.  
`isEnriched` |  `boolean` Output only. The flag that indicates whether the entity is enriched.  
`isVulnerable` |  `boolean` Output only. The flag that indicates whether the entity is vulnerable.  
`isPivot` |  `boolean` Output only. The flag that indicates whether the entity is a pivot.  
`environment` |  `string` Output only. The environment of the entity.  
`fields[]` |  `object (`[PendingStepSecurityEntityPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepSecurityEntityPropertyValue)`)` Output only. The fields of the pending step security entity.  
`isManuallyCreated` |  `boolean` Output only. The flag that indicates whether the entity is manually created.  
  
## PendingStepSecurityEntityPropertyValue

The pending step security entity property value.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Output only. The key of the pending step security entity property value.  
`value` |  `string` Output only. The value of the pending step security entity property value.  
  
## PendingStepActionDefinition

The action definition of the pending step.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "script": string,
      "integrationIdentifier": string,
      "scriptResultName": string,
      "dynamicResultsMetadata": [
        {
          object ([DynamicResultMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.actions#IntegrationAction.DynamicResultMetadata))
        }
      ],
      "creator": string,
      "version": number,
      "id": integer,
      "parameters": [
        {
          object ([PendingStepActionDefinitionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinitionParameter))
        }
      ],
      "timeoutSeconds": integer,
      "asyncPollingIntervalInSeconds": integer,
      "totalIntervalTimeoutForAsyncInSeconds": integer,
      "defaultResultValue": string,
      "integrationInstances": [
        {
          object ([ActionIntegrationInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#ActionIntegrationInstance))
        }
      ],
      "hasJsonResult": boolean,
      "actionWidgetTemplateIdentifier": string,
      "isEnabled": boolean,
      "isAsync": boolean,
      "actionType": enum ([ActionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ActionType))
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the action definition.  
`description` |  `string` Output only. The description of the action definition.  
`script` |  `string` Output only. The script of the action definition.  
`integrationIdentifier` |  `string` Output only. The integration identifier of the action definition.  
`scriptResultName` |  `string` Output only. The script result name of the action definition.  
`dynamicResultsMetadata[]` |  `object (`[DynamicResultMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.integrations.actions#IntegrationAction.DynamicResultMetadata)`)` Output only. The dynamic result metadata of the action definition.  
`creator` |  `string` Output only. The creator of the action definition.  
`version` |  `number` Output only. The version of the action definition.  
`id` |  `integer` Output only. The id of the action definition.  
`parameters[]` |  `object (`[PendingStepActionDefinitionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinitionParameter)`)` Output only. The parameters of the action definition.  
`timeoutSeconds` |  `integer` Output only. The timeout seconds of the action definition.  
`asyncPollingIntervalInSeconds` |  `integer` Output only. The async polling interval seconds of the action definition.  
`totalIntervalTimeoutForAsyncInSeconds` |  `integer` Output only. The total interval timeout for async in seconds of the action definition.  
`defaultResultValue` |  `string` Output only. The default result value of the action definition.  
`integrationInstances[]` |  `object (`[ActionIntegrationInstance](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#ActionIntegrationInstance)`)` Output only. The integration instances of the action definition.  
`hasJsonResult` |  `boolean` Output only. The flag that indicates whether the action definition has json result or not.  
`actionWidgetTemplateIdentifier` |  `string` Output only. The action widget template identifier of the action definition.  
`isEnabled` |  `boolean` Output only. The flag that indicates whether the action definition is enabled.  
`isAsync` |  `boolean` Output only. The flag that indicates whether the action definition is async.  
`actionType` |  `enum (`[ActionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ActionType)`)` Output only. Action type.  
  
## PendingStepActionDefinitionParameter

The action parameters of the action definition.

JSON representation  
---  
      
    
    {
      "id": integer,
      "creationTimeUnixTimeInMs": string,
      "modifiedTimeUnixTimeInMs": string,
      "customActionId": string,
      "isMandatory": boolean,
      "defaultValue": string,
      "description": string,
      "name": string,
      "value": string,
      "type": enum ([PendingStepActionDefinitionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinitionParameterType)),
      "optionalValues": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `integer` Output only. The id of the action parameter.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the action parameter.  
`modifiedTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modified time of the action parameter.  
`customActionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The custom action id of the action parameter.  
`isMandatory` |  `boolean` Output only. The flag that indicates whether the action parameter is mandatory.  
`defaultValue` |  `string` Output only. The default value of the action parameter.  
`description` |  `string` Output only. The description of the action parameter.  
`name` |  `string` Output only. The name of the action parameter.  
`value` |  `string` Output only. The value of the action parameter.  
`type` |  `enum (`[PendingStepActionDefinitionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#PendingStepActionDefinitionParameterType)`)` Output only. The type of the action parameter.  
`optionalValues[]` |  `string` Output only. The optional values of the action parameter.  
  
## PendingStepActionDefinitionParameterType

The action parameter type of the action parameter.

Enums  
---  
`PENDING_STEP_ACTION_DEFINITION_PARAMETER_TYPE_UNSPECIFIED` | The action parameter type is unspecified.  
`STRING` | The action parameter type is string.  
`BOOLEAN` | The action parameter type is boolean.  
`WFS_REPOSITORY` | The action parameter type is WFS repository.  
`USER_REPOSITORY` | The action parameter type is user repository.  
`STAGES_REPOSITORY` | The action parameter type is stages repository.  
`CLOSE_CASE_REASON_REPOSITORY` | The action parameter type is close case reason repository.  
`CLOSE_CASE_ROOT_CAUSE_REPOSITORY` | The action parameter type is close case root cause repository.  
`PRIORITIES_REPOSITORY` | The action parameter type is priorities repository.  
`EMAIL_CONTENT` | The action parameter type is email content.  
`CONTENT` | The action parameter type is content.  
`PASSWORD` | The action parameter type is password.  
`ENTITY_TYPE` | The action parameter type is entity type.  
`MULTI_VALUES` | The action parameter type is multi values.  
`LIST` | The action parameter type is list.  
`CODE` | The action parameter type is code.  
`TIME_SPAN_SECONDS` | The action parameter type is time span seconds.  
`MULTIPLE_CHOICE_PARAMETER` | The action parameter type is multiple choice.  
  
## ActionIntegrationInstance

The integration instance of the action definition.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "integrationIdentifier": string,
      "environmentIdentifier": string,
      "instanceName": string,
      "instanceDescription": string,
      "isConfigured": boolean,
      "isRemote": boolean,
      "isSystemDefault": boolean
    }  
  
Fields  
---  
`identifier` |  `string` Output only. The identifier of the integration instance.  
`integrationIdentifier` |  `string` Output only. The identifier of the integration instance.  
`environmentIdentifier` |  `string` Output only. The environment identifier of the integration instance.  
`instanceName` |  `string` Output only. The instance name of the integration instance.  
`instanceDescription` |  `string` Output only. The instance description of the integration instance.  
`isConfigured` |  `boolean` Output only. The flag that indicates whether the integration instance is configured or not.  
`isRemote` |  `boolean` Output only. The flag that indicates whether the integration instance is remote or not.  
`isSystemDefault` |  `boolean` Output only. The flag that indicates whether the integration instance is system default or not.  
  
## WorkflowPendingStepInstance

The workflow pending step instance.

JSON representation  
---  
      
    
    {
      "pendingStepTimeUnixTimeInMs": string,
      "caseTitle": string,
      "alertName": string,
      "messageToAssignee": string,
      "slaExpiration": {
        object ([Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Sla))
      },
      "casePriority": enum ([LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)),
      "alertPriority": enum ([LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)),
      "pendingStepExpirationTimeUnixTimeInMs": string
    }  
  
Fields  
---  
`pendingStepTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The pending step time unix time in milliseconds of the action definition.  
`caseTitle` |  `string` Output only. The case title of the action definition.  
`alertName` |  `string` Output only. The alert name of the action definition.  
`messageToAssignee` |  `string` Output only. The message to assignee of the action definition.  
`slaExpiration` |  `object (`[Sla](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Sla)`)` Output only. The SLA of the action definition.  
`casePriority` |  `enum (`[LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)`)` Output only. The case priority of the action definition.  
`alertPriority` |  `enum (`[LegacyCasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.caseAlerts#LegacyCasePriority)`)` Output only. The alert priority of the action definition.  
`pendingStepExpirationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The pending step expiration time unix time in milliseconds of the action definition.  
  
## WorkflowStepType

The workflow step type.

Enums  
---  
`WORKFLOW_STEP_TYPE_UNSPECIFIED` | The workflow step type is unspecified.  
`ACTION` | The workflow step type is action.  
`MULTI_CHOICE_QUESTION` | The workflow step type is multi choice question.  
`PREVIOUS_ACTION` | The workflow step type is previous action.  
`CASE_DATA_CONDITION` | The workflow step type is case data condition.  
`CONDITION` | The workflow step type is condition.  
`BLOCK` | The workflow step type is block.  
`OUTPUT` | The workflow step type is output.  
`PARALLEL_ACTIONS_CONTAINER` | The workflow step type is parallel actions container.  
`FOR_EACH_START_LOOP` | The workflow step type is for each start loop.  
`FOR_EACH_END_LOOP` | The workflow step type is for each end loop.  
  
## WorkflowStepParameter

The workflow step parameter.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "type": enum ([WorkflowStepParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepParameterType)),
      "isMandatory": boolean,
      "defaultValue": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the workflow step parameter.  
`value` |  `string` Output only. The value of the workflow step parameter.  
`type` |  `enum (`[WorkflowStepParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WorkflowPendingStepsWidget#WorkflowStepParameterType)`)` Output only. The type of the workflow step parameter.  
`isMandatory` |  `boolean` Output only. The flag that indicates whether the workflow step parameter is mandatory or not.  
`defaultValue` |  `string` Output only. The default value of the workflow step parameter.  
  
## WorkflowStepParameterType

The workflow step parameter type.

Enums  
---  
`WORKFLOW_STEP_PARAMETER_TYPE_UNSPECIFIED` | The action parameter type is unspecified.  
`STRING` | The action parameter type is string.  
`BOOLEAN` | The action parameter type is boolean.  
`WFS_REPOSITORY` | The action parameter type is WFS repository.  
`USER_REPOSITORY` | The action parameter type is user repository.  
`STAGES_REPOSITORY` | The action parameter type is stages repository.  
`CLOSE_CASE_REASON_REPOSITORY` | The action parameter type is close case reason repository.  
`CLOSE_CASE_ROOT_CAUSE_REPOSITORY` | The action parameter type is close case root cause repository.  
`PRIORITIES_REPOSITORY` | The action parameter type is priorities repository.  
`EMAIL_CONTENT` | The action parameter type is email content.  
`CONTENT` | The action parameter type is content.  
`PASSWORD` | The action parameter type is password.  
`ENTITY_TYPE` | The action parameter type is entity type.  
`MULTI_VALUES` | The action parameter type is multi values.  
`LIST` | The action parameter type is list.  
`CODE` | The action parameter type is code.  
`TIME_SPAN_SECONDS` | The action parameter type is time span seconds.  
`MULTIPLE_CHOICE_PARAMETER` | The action parameter type is multiple choice.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
