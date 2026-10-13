---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData/
title: OverviewData \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:15.468900+00:00
---

# OverviewData  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  OverviewData Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * OverviewWidgetMetadataResult
    * JSON representation
  * Configuration
    * JSON representation
  * HighlightFieldConfig
    * JSON representation
  * EventData
    * JSON representation
  * CustomFieldFormData
    * JSON representation
  * CaseInsightData
    * JSON representation
  * InsightSeverityEnum
  * InsightTypeEnum
  * WidgetPropertyValue
    * JSON representation
  * CaseWallItemsTimeFilterEnum
  * DataDistributionTypeEnum
  * DataDistributionSetting
    * JSON representation
  * ResultsNumberEnum
  * WallItemTypeEnum
  * WidgetApiWorkflowStepInstanceDataModel
    * JSON representation
  * StepType
  * WidgetApiWorkflowStepParameterDataModel
    * JSON representation
  * CustomActionParameterType
  * ApiActionStatusEnum
  * WidgetApiSecurityEntityDataModel
    * JSON representation
  * WidgetApiActionDefinitionDataModel
    * JSON representation
  * WidgetApiDynamicResultMetadata
    * JSON representation
  * ApiActionParameter
    * JSON representation
  * CustomActionParameterType
  * WidgetApiIntegrationInstanceDataModel
    * JSON representation
  * WidgetApiPendingStepInstanceDataModel
    * JSON representation
  * ApiSlaExpiration
    * JSON representation
  * QuickActionDataModel
    * JSON representation



Case & Alert overview data.

JSON representation  
---  
      
    
    {
      "name": string,
      "creator": string,
      "playbookDefinitionIdentifier": string,
      "widgets": [
        {
          object ([OverviewWidgetMetadataResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#OverviewWidgetMetadataResult))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the overview data.  
`creator` |  `string` Output only. The creator user name.  
`playbookDefinitionIdentifier` |  `string` Output only. The playbook definition identifier.  
`widgets[]` |  `object (`[OverviewWidgetMetadataResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#OverviewWidgetMetadataResult)`)` Output only. Widget metadata result.  
  
## OverviewWidgetMetadataResult

Overview widget metadata result.

JSON representation  
---  
      
    
    {
      "title": string,
      "description": string,
      "identifier": string,
      "templateIdentifier": string,
      "configuration": {
        object ([Configuration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#Configuration))
      },
      "conditionsGroup": {
        object ([WidgetConditionsGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#WidgetConditionsGroup))
      },
      "predefinedWidgetTemplateIdentifier": string,
      "stepIdentifier": string,
      "stepIntegration": string,
      "blockStepIdentifier": string,
      "blockStepInstanceName": string,
      "order": integer,
      "type": enum ([ViewWidgetTemplateTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#ViewWidgetTemplateTypeEnum)),
      "width": enum ([WidgetTemplateGridColumnsEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#WidgetTemplateGridColumnsEnum)),
      "presentIfEmpty": boolean,
      "isConfigured": boolean
    }  
  
Fields  
---  
`title` |  `string` Optional. Widget display title.  
`description` |  `string` Optional. Widget description for display or configuration.  
`identifier` |  `string` Required. Unique widget identifier within the template.  
`templateIdentifier` |  `string` Required. Identifier of the template this widget belongs to.  
`configuration` |  `object (`[Configuration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#Configuration)`)` Output only. The configuration of the widget.  
`conditionsGroup` |  `object (`[WidgetConditionsGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#WidgetConditionsGroup)`)` Required. Dynamic condition logic to control widget display.  
`predefinedWidgetTemplateIdentifier` |  `string` Required. Optional reference to a predefined widget template.  
`stepIdentifier` |  `string` Required. Optional step identifier (e.g., in a playbook).  
`stepIntegration` |  `string` Required. Name of the integration associated with this widget step.  
`blockStepIdentifier` |  `string` Required. Optional nested block step reference.  
`blockStepInstanceName` |  `string` Required. Optional name of block instance in a playbook.  
`order` |  `integer` Required. Order index of the widget in the list.  
`type` |  `enum (`[ViewWidgetTemplateTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#ViewWidgetTemplateTypeEnum)`)` Required. The type of widget (e.g., Graph, Alerts, Text).  
`width` |  `enum (`[WidgetTemplateGridColumnsEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#WidgetTemplateGridColumnsEnum)`)` Required. The visual width of the widget on the layout grid.  
`presentIfEmpty` |  `boolean` Required. Indicates whether to render widget even when no data.  
`isConfigured` |  `boolean` Required. Flag that indicates whether the widget is configured or not.  
  
## Configuration

Optional typed configuration based on widget type.

JSON representation  
---  
      
    
    {
      "type": enum ([ViewWidgetTemplateTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#ViewWidgetTemplateTypeEnum)),
      "widgetDefinitionScope": enum ([TargetScopeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/TargetScopeEnum)),
      "highlightFieldConfigs": [
        {
          object ([HighlightFieldConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#HighlightFieldConfig))
        }
      ],
      "eventSelectedFields": [
        {
          object ([EventData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#EventData))
        }
      ],
      "customFields": [
        {
          object ([CustomFieldFormData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomFieldFormData))
        }
      ],
      "htmlContent": string,
      "htmlHeight": integer,
      "insights": [
        {
          object ([CaseInsightData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CaseInsightData))
        }
      ],
      "dataSource": string,
      "jsonSample": string,
      "keyValue": [
        {
          object ([WidgetPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetPropertyValue))
        }
      ],
      "dataDistributionSettingList": [
        {
          object ([DataDistributionSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#DataDistributionSetting))
        }
      ],
      "text": string,
      "types": [
        enum ([WallItemTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WallItemTypeEnum))
      ],
      "pendingSteps": [
        {
          object ([WidgetApiWorkflowStepInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiWorkflowStepInstanceDataModel))
        }
      ],
      "actions": [
        {
          object ([QuickActionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#QuickActionDataModel))
        }
      ],
      "information": string,
      "targetScope": enum ([TargetScopeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/TargetScopeEnum)),
      "safeRendering": boolean,
      "timeRangeFilter": enum ([CaseWallItemsTimeFilterEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CaseWallItemsTimeFilterEnum)),
      "dataType": enum ([DataDistributionTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#DataDistributionTypeEnum))
    }  
  
Fields  
---  
`type` |  `enum (`[ViewWidgetTemplateTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.views#ViewWidgetTemplateTypeEnum)`)` Required. The type of the widget.  
`widgetDefinitionScope` |  `enum (`[TargetScopeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/TargetScopeEnum)`)` Required. The scope of the widget.  
`highlightFieldConfigs[]` |  `object (`[HighlightFieldConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#HighlightFieldConfig)`)` Output only. The highlight field configurations.  
`eventSelectedFields[]` |  `object (`[EventData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#EventData)`)` Output only. The selected fields of the event data.  
`customFields[]` |  `object (`[CustomFieldFormData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomFieldFormData)`)` Output only. The custom fields of the form widget.  
`htmlContent` |  `string` Output only. The html content of the widget.  
`htmlHeight` |  `integer` Output only. The html height of the widget.  
`insights[]` |  `object (`[CaseInsightData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CaseInsightData)`)` Output only. The insights associated with the case.  
`dataSource` |  `string` Output only. The data source of the widget.  
`jsonSample` |  `string` Output only. The json sample of the widget.  
`keyValue[]` |  `object (`[WidgetPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetPropertyValue)`)` Output only. The key value of the widget.  
`dataDistributionSettingList[]` |  `object (`[DataDistributionSetting](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#DataDistributionSetting)`)` Optional. List of distribution settings.  
`text` |  `string` Output only. The text content of the widget.  
`types[]` |  `enum (`[WallItemTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WallItemTypeEnum)`)` Optional. The wall activity types to include (e.g., Favorites, Comments, Tasks).  
`pendingSteps[]` |  `object (`[WidgetApiWorkflowStepInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiWorkflowStepInstanceDataModel)`)` Output only. Pending steps.  
`actions[]` |  `object (`[QuickActionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#QuickActionDataModel)`)` Output only. The quick actions of the widget.  
`information` |  `string` Output only. The information of the widget.  
`targetScope` |  `enum (`[TargetScopeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/TargetScopeEnum)`)` Output only. The target scope of the widget.  
`safeRendering` |  `boolean` Output only. The html is safe to render.  
`timeRangeFilter` |  `enum (`[CaseWallItemsTimeFilterEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CaseWallItemsTimeFilterEnum)`)` Optional. The time range filter for the widget.  
`dataType` |  `enum (`[DataDistributionTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#DataDistributionTypeEnum)`)` Required. Indicates whether data type is based on events or entities.  
  
## HighlightFieldConfig

Highlight field configuration.

JSON representation  
---  
      
    
    {
      "label": string,
      "key": string,
      "groupName": string
    }  
  
Fields  
---  
`label` |  `string` Output only. The label of the field.  
`key` |  `string` Output only. The key of the field.  
`groupName` |  `string` Output only. The group name of the field.  
  
## EventData

Event data.

JSON representation  
---  
      
    
    {
      "columnName": string,
      "fieldRawValue": string
    }  
  
Fields  
---  
`columnName` |  `string` Output only. The column name of the event data.  
`fieldRawValue` |  `string` Output only. The raw value of the event data.  
  
## CustomFieldFormData

Represents the configuration data for a single custom field in a form widget.

JSON representation  
---  
      
    
    {
      "id": string,
      "mandatory": boolean,
      "order": integer
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The unique identifier of the custom field.  
`mandatory` |  `boolean` Optional. Indicates whether the custom field is mandatory.  
`order` |  `integer` Optional. Display order of the field in the form. Lower values appear earlier.  
  
## CaseInsightData

Represents an insight associated with a case.

JSON representation  
---  
      
    
    {
      "triggeredBy": string,
      "title": string,
      "content": string,
      "entityIdentifier": string,
      "additionalData": string,
      "additionalDataTitle": string,
      "originalRequestingUser": string,
      "entityType": string,
      "alertIdentifier": string,
      "caseId": string,
      "id": string,
      "severity": enum ([InsightSeverityEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightSeverityEnum)),
      "type": enum ([InsightTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightTypeEnum)),
      "additionalDataType": enum ([InsightTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightTypeEnum)),
      "isFavorite": boolean
    }  
  
Fields  
---  
`triggeredBy` |  `string` Optional. The user or system that triggered the insight.  
`title` |  `string` Required. The title of the insight.  
`content` |  `string` Required. The content/body of the insight.  
`entityIdentifier` |  `string` Optional. The identifier of the related entity.  
`additionalData` |  `string` Optional. A serialized string of additional data (JSON, CSV, etc.).  
`additionalDataTitle` |  `string` Optional. A human-readable title for the additional data content.  
`originalRequestingUser` |  `string` Optional. The user that originally requested the insight (if applicable).  
`entityType` |  `string` Optional. The type of entity associated with the insight.  
`alertIdentifier` |  `string` Optional. Identifier of the alert this insight may relate to.  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The case ID this insight is linked to.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The ID of the insight.  
`severity` |  `enum (`[InsightSeverityEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightSeverityEnum)`)` Required. The severity level of the insight.  
`type` |  `enum (`[InsightTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightTypeEnum)`)` Required. The type of insight.  
`additionalDataType` |  `enum (`[InsightTypeEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#InsightTypeEnum)`)` Optional. An optional additional data type enum.  
`isFavorite` |  `boolean` Optional. Indicates whether this insight is marked as a favorite.  
  
## InsightSeverityEnum

Severity levels for insights.

Enums  
---  
`INSIGHT_SEVERITY_UNSPECIFIED` | Unspecified insight severity.  
`INFO` | Info insight severity.  
`WARN` | Warn insight severity.  
`ERROR` | Error insight severity.  
  
## InsightTypeEnum

The type of the insight (general or entity-based).

Enums  
---  
`INSIGHT_TYPE_UNSPECIFIED` | Unspecified insight type.  
`GENERAL` | General insight type.  
`ENTITY` | Entity insight type.  
  
## WidgetPropertyValue

Property value.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Output only. The key of the property value.  
`value` |  `string` Output only. The value of the property value.  
  
## CaseWallItemsTimeFilterEnum

The time range filter for wall activities.

Enums  
---  
`WALL_ITEMS_TIME_FILTER_UNSPECIFIED` | Unspecified wall items time filter.  
`LAST_24_HOURS` | Filter for the last 24 hours.  
`LAST_72_HOURS` | Filter for the last 72 hours.  
`LAST_WEEK` | Filter for the last week.  
`ALL` | Filter for all wall items.  
`LAST_DAY` | Filter for the last 24 hours.  
`LAST_MONTH` | Filter for the last 30 days.  
  
## DataDistributionTypeEnum

Indicates whether statistics are based on events or entities.

Enums  
---  
`DATA_DISTRIBUTION_TYPE_UNSPECIFIED` | Unspecified data distribution type.  
`EVENTS` | Events data distribution type.  
`ENTITIES` | Entities data distribution type.  
  
## DataDistributionSetting

Represents a data distribution setting.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "rawFieldName": string,
      "maxResults": enum ([ResultsNumberEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ResultsNumberEnum))
    }  
  
Fields  
---  
`displayName` |  `string` Required. Display name for the field shown in the UI.  
`rawFieldName` |  `string` Required. Raw field name used for data access.  
`maxResults` |  `enum (`[ResultsNumberEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ResultsNumberEnum)`)` Optional. Max number of results to return for this field.  
  
## ResultsNumberEnum

Allowed numbers of results for a statistic group.

Enums  
---  
`RESULTS_NUMBER_UNSPECIFIED` | Unspecified results number.  
`FIVE` | Five results number.  
`TEN` | Ten results number.  
  
## WallItemTypeEnum

The type of wall item (e.g., favorites, comments, tasks).

Enums  
---  
`WALL_ITEM_TYPE_UNSPECIFIED` | Unspecified wall item type.  
`FAVORITES` | Favorites wall item type.  
`COMMENTS` | Comments wall item type.  
`TASKS` | Tasks wall item type.  
  
## WidgetApiWorkflowStepInstanceDataModel

The data model of the API workflow step instance.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "originalStepIdentifier": string,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string,
      "instanceName": string,
      "name": string,
      "integration": string,
      "description": string,
      "actionProvider": string,
      "actionName": string,
      "parameters": [
        {
          object ([WidgetApiWorkflowStepParameterDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiWorkflowStepParameterDataModel))
        }
      ],
      "workflowIdentifier": string,
      "parentWorkflowIdentifier": string,
      "workflowInstanceIdentifier": string,
      "caseId": string,
      "indicatorIdentifier": string,
      "alertGroupIdentifier": string,
      "executingUser": string,
      "message": string,
      "resultValue": string,
      "results": [
        {
          object ([ScriptResultEntityData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/ScriptResultEntityData))
        }
      ],
      "targetEntities": [
        {
          object ([WidgetApiSecurityEntityDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiSecurityEntityDataModel))
        }
      ],
      "resultEntities": [
        {
          object ([WidgetApiSecurityEntityDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiSecurityEntityDataModel))
        }
      ],
      "properties": {
        string: string,
        ...
      },
      "actionDef": {
        object ([WidgetApiActionDefinitionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiActionDefinitionDataModel))
      },
      "blockStepId": string,
      "jsonResultObject": string,
      "integrationInstanceIdentifier": string,
      "integrationInstanceName": string,
      "integrationInstanceEnvironment": string,
      "pendingStepProperties": {
        object ([WidgetApiPendingStepInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiPendingStepInstanceDataModel))
      },
      "isAutomatic": boolean,
      "isSkippable": boolean,
      "type": enum ([StepType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#StepType)),
      "autoSkipOnFailure": boolean,
      "isDebugMockData": boolean,
      "status": enum ([ApiActionStatusEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiActionStatusEnum)),
      "allowedToExecute": boolean,
      "resultCode": integer,
      "loopIteration": integer,
      "parentWorkflowLoopIteration": integer
    }  
  
Fields  
---  
`identifier` |  `string` Output only. Inherited from ApiWorkflowStepDataModel  
`originalStepIdentifier` |  `string` Output only. The identifier of the original workflow pending step.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the record in milliseconds.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modification time of the record in milliseconds.  
`instanceName` |  `string` Output only. The name of the instance.  
`name` |  `string` Output only. The name of the step.  
`integration` |  `string` Output only. The integration of the step.  
`description` |  `string` Output only. The description of the step.  
`actionProvider` |  `string` Output only. The action provider of the step.  
`actionName` |  `string` Output only. The action name of the step.  
`parameters[]` |  `object (`[WidgetApiWorkflowStepParameterDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiWorkflowStepParameterDataModel)`)` Output only. The parameters of the step.  
`workflowIdentifier` |  `string` Output only. ApiWorkflowStepInstanceDataModel specific  
`parentWorkflowIdentifier` |  `string` Output only. The identifier of the parent workflow pending step.  
`workflowInstanceIdentifier` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The identifier of the workflow instance.  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The identifier of the case.  
`indicatorIdentifier` |  `string` Output only. The identifier of the indicator.  
`alertGroupIdentifier` |  `string` Output only. The identifier of the alert group.  
`executingUser` |  `string` Output only. The user who is executing the API action.  
`message` |  `string` Output only. The message of the API action.  
`resultValue` |  `string` Output only. The result value of the API action.  
`results[]` |  `object (`[ScriptResultEntityData](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/ScriptResultEntityData)`)` Output only. The result entity data of the API action.  
`targetEntities[]` |  `object (`[WidgetApiSecurityEntityDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiSecurityEntityDataModel)`)` Output only. The target entities of the API action.  
`resultEntities[]` |  `object (`[WidgetApiSecurityEntityDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiSecurityEntityDataModel)`)` Output only. The result entities of the API action.  
`properties` |  `map (key: string, value: string)` Output only. The properties of the API action.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`actionDef` |  `object (`[WidgetApiActionDefinitionDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiActionDefinitionDataModel)`)` Output only. The API action definition data model of the action definition.  
`blockStepId` |  `string` Output only. The block step id of the action definition.  
`jsonResultObject` |  `string` Output only. The json result object of the action definition.  
`integrationInstanceIdentifier` |  `string` Output only. The integration instance identifier of the action definition.  
`integrationInstanceName` |  `string` Output only. The integration instance name of the action definition.  
`integrationInstanceEnvironment` |  `string` Output only. The integration instance environment of the action definition.  
`pendingStepProperties` |  `object (`[WidgetApiPendingStepInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiPendingStepInstanceDataModel)`)` Output only. The pending step properties of the action definition.  
`isAutomatic` |  `boolean` Output only. Whether the step is automatic.  
`isSkippable` |  `boolean` Output only. Whether the step is skippable.  
`type` |  `enum (`[StepType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#StepType)`)` Output only. The type of the step.  
`autoSkipOnFailure` |  `boolean` Output only. Whether the step should be skipped on failure.  
`isDebugMockData` |  `boolean` Output only. Whether the step is debug mock data.  
`status` |  `enum (`[ApiActionStatusEnum](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiActionStatusEnum)`)` Output only. The status of the API action.  
`allowedToExecute` |  `boolean` Output only. The flag that indicates whether the API action is allowed to execute.  
`resultCode` |  `integer` Output only. The result code of the API action.  
`loopIteration` |  `integer` Output only. The loop iteration of the action definition.  
`parentWorkflowLoopIteration` |  `integer` Output only. The parent workflow loop iteration of the action definition.  
  
## StepType

The type of the step.

Enums  
---  
`STEP_TYPE_UNSPECIFIED` | Unspecified step type.  
`ACTION` | Action step type.  
`MULTI_CHOICE_QUESTION` | Multi choice question step type.  
`PREVIOUS_ACTION` | Previous action step type.  
`CASE_DATA_CONDITION` | Case data condition step type.  
`CONDITION` | Condition step type.  
`BLOCK` | Block step type.  
`OUTPUT` | Output step type.  
`PARALLEL_ACTIONS_CONTAINER` | Parallel actions container step type.  
`FOR_EACH_START_LOOP` | For each start loop step type.  
`FOR_EACH_END_LOOP` | For each end loop step type.  
  
## WidgetApiWorkflowStepParameterDataModel

The parameter of the step.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "defaultValue": string,
      "type": enum ([CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomActionParameterType)),
      "isMandatory": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the parameter.  
`value` |  `string` Output only. The value of the parameter.  
`defaultValue` |  `string` Output only. The default value of the parameter.  
`type` |  `enum (`[CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomActionParameterType)`)` Output only. The type of the parameter.  
`isMandatory` |  `boolean` Output only. Whether the parameter is mandatory.  
  
## CustomActionParameterType

The type of the parameter.

Enums  
---  
`CUSTOM_ACTION_PARAMETER_TYPE_UNSPECIFIED` | Unspecified custom action parameter type.  
`STRING` | String custom action parameter type.  
`BOOLEAN` | Boolean custom action parameter type.  
`WFS_REPOSITORY` | WFS repository custom action parameter type.  
`USER_REPOSITORY` | User repository custom action parameter type.  
`STAGES_REPOSITORY` | Stages repository custom action parameter type.  
`CLOSE_CASE_REASON_REPOSITORY` | Close case reason repository custom action parameter type.  
`CLOSE_CASE_ROOT_CAUSE_REPOSITORY` | Close case root cause repository custom action parameter type.  
`PRIORITIES_REPOSITORY` | Priorities repository custom action parameter type.  
`EMAIL_CONTENT` | Email content custom action parameter type.  
`CONTENT` | Content custom action parameter type.  
`PASSWORD` | Password custom action parameter type.  
`ENTITY_TYPE` | Entity type custom action parameter type.  
`MULTI_VALUES` | Multi values custom action parameter type.  
`LIST` | List custom action parameter type.  
`CODE` | Code custom action parameter type.  
`TIME_SPAN_SECONDS` | Time span seconds custom action parameter type.  
`MULTIPLE_CHOICE_PARAMETER` | Multiple choice parameter custom action parameter type.  
  
## ApiActionStatusEnum

The status of the API action.

Enums  
---  
`API_ACTION_STATUS_UNSPECIFIED` | Unspecified API action status.  
`NO_STATUS` | No status API action status.  
`FAULTED` | Faulted API action status.  
`IN_PROGRESS` | In progress API action status.  
`COMPLETED` | Completed API action status.  
`PENDING_USER_INPUT` | Pending user input API action status.  
`PENDING_PREVIOUS_STEPS` | Pending previous steps API action status.  
`STARTED` | Started API action status.  
`FAULTED_AND_SKIPPED` | Faulted and skipped API action status.  
`HANDLED_TIMEDOUT` | Handled timed out API action status.  
`UNHANDLED_TIMEDOUT` | Unhandled timed out API action status.  
`TERMINATED` | Terminated API action status.  
`NOT_RUN_AND_SKIPPED` | Not run and skipped API action status.  
`PENDING_ACTION_TIMEOUT` | Pending action timeout API action status.  
`PENDING_ACTION_TIMEOUT_AND_SKIPPED` | Pending action timeout and skipped API action status.  
`PENDING_RETRY` | Pending retry API action status.  
  
## WidgetApiSecurityEntityDataModel

The security entity data model of the API action.

JSON representation  
---  
      
    
    {
      "caseId": string,
      "identifier": string,
      "entityType": string,
      "environment": string,
      "fields": [
        {
          object ([WidgetPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetPropertyValue))
        }
      ],
      "isInternal": boolean,
      "isSuspicious": boolean,
      "isArtifact": boolean,
      "isEnriched": boolean,
      "isVulnerable": boolean,
      "isPivot": boolean,
      "isManuallyCreated": boolean
    }  
  
Fields  
---  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The case id of the entity.  
`identifier` |  `string` Output only. The entity identifier.  
`entityType` |  `string` Output only. The entity type.  
`environment` |  `string` Output only. The environment of the entity.  
`fields[]` |  `object (`[WidgetPropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetPropertyValue)`)` Output only. The fields of the entity.  
`isInternal` |  `boolean` Output only. The flag that indicates whether the entity is internal.  
`isSuspicious` |  `boolean` Output only. The flag that indicates whether the entity is suspicious.  
`isArtifact` |  `boolean` Output only. The flag that indicates whether the entity is an artifact.  
`isEnriched` |  `boolean` Output only. The flag that indicates whether the entity is enriched.  
`isVulnerable` |  `boolean` Output only. The flag that indicates whether the entity is vulnerable.  
`isPivot` |  `boolean` Output only. The flag that indicates whether the entity is a pivot.  
`isManuallyCreated` |  `boolean` Output only. The flag that indicates whether the entity is manually created.  
  
## WidgetApiActionDefinitionDataModel

The API action definition data model of the API action.

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
          object ([WidgetApiDynamicResultMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiDynamicResultMetadata))
        }
      ],
      "creator": string,
      "parameters": [
        {
          object ([ApiActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiActionParameter))
        }
      ],
      "timeoutSeconds": string,
      "asyncPollingIntervalInSeconds": string,
      "totalIntervalTimeoutForAsyncInSeconds": string,
      "defaultResultValue": string,
      "integrationInstances": [
        {
          object ([WidgetApiIntegrationInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiIntegrationInstanceDataModel))
        }
      ],
      "actionWidgetTemplateIdentifier": string,
      "isEnabled": boolean,
      "version": number,
      "id": string,
      "isAsync": boolean,
      "hasJsonResult": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the action definition.  
`description` |  `string` Output only. The description of the action definition.  
`script` |  `string` Output only. The script of the action definition.  
`integrationIdentifier` |  `string` Output only. The integration identifier of the action definition.  
`scriptResultName` |  `string` Output only. The script result name of the action definition.  
`dynamicResultsMetadata[]` |  `object (`[WidgetApiDynamicResultMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiDynamicResultMetadata)`)` Output only. The dynamic results metadata of the action definition.  
`creator` |  `string` Output only. The creator of the action definition.  
`parameters[]` |  `object (`[ApiActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiActionParameter)`)` Output only. The parameters of the action definition.  
`timeoutSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timeout seconds of the action definition.  
`asyncPollingIntervalInSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The async polling interval in seconds of the action definition.  
`totalIntervalTimeoutForAsyncInSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total interval timeout for async in seconds of the action definition.  
`defaultResultValue` |  `string` Output only. The default result value of the action definition.  
`integrationInstances[]` |  `object (`[WidgetApiIntegrationInstanceDataModel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#WidgetApiIntegrationInstanceDataModel)`)` Output only. The integration instances of the action definition.  
`actionWidgetTemplateIdentifier` |  `string` Output only. The action widget template identifier of the action definition.  
`isEnabled` |  `boolean` Output only. The flag that indicates whether the action definition is enabled.  
`version` |  `number` Output only. The version of the action definition.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the action definition.  
`isAsync` |  `boolean` Output only. The flag that indicates whether the action definition is async.  
`hasJsonResult` |  `boolean` Output only. The flag that indicates whether the action definition has json result.  
  
## WidgetApiDynamicResultMetadata

The API dynamic result metadata of the action definition.

JSON representation  
---  
      
    
    {
      "resultName": string,
      "resultExample": string
    }  
  
Fields  
---  
`resultName` |  `string` Output only. The result name of the dynamic result metadata.  
`resultExample` |  `string` Output only. The result example of the dynamic result metadata.  
  
## ApiActionParameter

The API action parameter of the action definition.

JSON representation  
---  
      
    
    {
      "id": string,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string,
      "customActionId": string,
      "defaultValue": string,
      "description": string,
      "name": string,
      "value": string,
      "optionalValues": [
        string
      ],
      "isMandatory": boolean,
      "type": enum ([CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomActionParameterType_1))
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the action parameter.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The creation time of the action parameter.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The modification time of the action parameter.  
`customActionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The custom action id of the action parameter.  
`defaultValue` |  `string` Output only. The default value of the action parameter.  
`description` |  `string` Output only. The description of the action parameter.  
`name` |  `string` Output only. The name of the action parameter.  
`value` |  `string` Output only. The value of the action parameter.  
`optionalValues[]` |  `string` Output only. The optional values of the action parameter.  
`isMandatory` |  `boolean` Output only. The flag that indicates whether the action parameter is mandatory.  
`type` |  `enum (`[CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#CustomActionParameterType_1)`)` Output only. The type of the action parameter.  
  
## CustomActionParameterType

The custom action parameter type of the action parameter.

Enums  
---  
`CUSTOM_ACTION_PARAMETER_TYPE_UNSPECIFIED` | The custom action parameter type is unspecified.  
`STRING` | The custom action parameter type is string.  
`BOOLEAN` | The custom action parameter type is boolean.  
`WFS_REPOSITORY` | The custom action parameter type is WFS repository.  
`USER_REPOSITORY` | The custom action parameter type is user repository.  
`STAGES_REPOSITORY` | The custom action parameter type is stages repository.  
`CLOSE_CASE_REASON_REPOSITORY` | The custom action parameter type is close case reason repository.  
`CLOSE_CASE_ROOT_CAUSE_REPOSITORY` | The custom action parameter type is close case root cause repository.  
`PRIORITIES_REPOSITORY` | The custom action parameter type is priorities repository.  
`EMAIL_CONTENT` | The custom action parameter type is email content.  
`CONTENT` | The custom action parameter type is content.  
`PASSWORD` | The custom action parameter type is password.  
`ENTITY_TYPE` | The custom action parameter type is entity type.  
`MULTI_VALUES` | The custom action parameter type is multi values.  
`LIST` | The custom action parameter type is list.  
`CODE` | The custom action parameter type is code.  
`TIME_SPAN_SECONDS` | The custom action parameter type is time span seconds.  
`MULTIPLE_CHOICE_PARAMETER` | The custom action parameter type is multiple choice.  
  
## WidgetApiIntegrationInstanceDataModel

The API integration instance data model of the action definition.

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
`integrationIdentifier` |  `string` Output only. The identifier of the integration.  
`environmentIdentifier` |  `string` Output only. The environment identifier of the integration instance.  
`instanceName` |  `string` Output only. The name of the integration instance.  
`instanceDescription` |  `string` Output only. The description of the integration instance.  
`isConfigured` |  `boolean` Output only. The flag that indicates whether the integration instance is configured.  
`isRemote` |  `boolean` Output only. The flag that indicates whether the integration instance is remote.  
`isSystemDefault` |  `boolean` Output only. The flag that indicates whether the integration instance is system default.  
  
## WidgetApiPendingStepInstanceDataModel

The API pending step instance data model of the action definition.

JSON representation  
---  
      
    
    {
      "casePriority": string,
      "alertPriority": string,
      "pendingStepTimeUnixTimeInMs": string,
      "pendingStepExpirationTimeUnixTimeInMs": string,
      "caseTitle": string,
      "alertName": string,
      "messageToAssignee": string,
      "slaExpiration": {
        object ([ApiSlaExpiration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiSlaExpiration))
      }
    }  
  
Fields  
---  
`casePriority` |  `string` Output only. The case priority of the action definition.  
`alertPriority` |  `string` Output only. The alert priority of the action definition.  
`pendingStepTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The pending step time unix time in milliseconds of the action definition.  
`pendingStepExpirationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The pending step expiration time unix time in milliseconds of the action definition.  
`caseTitle` |  `string` Output only. The case title of the action definition.  
`alertName` |  `string` Output only. The alert name of the action definition.  
`messageToAssignee` |  `string` Output only. The message to assignee of the action definition.  
`slaExpiration` |  `object (`[ApiSlaExpiration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/OverviewData#ApiSlaExpiration)`)` The SLA of the action definition.  
  
## ApiSlaExpiration

The API SLA expiration of the action definition.

JSON representation  
---  
      
    
    {
      "field": string,
      "value": string
    }  
  
Fields  
---  
`field` |  `string` The field of the SLA expiration.  
`value` |  `string` The value of the SLA expiration.  
  
## QuickActionDataModel

Quick action data model.

JSON representation  
---  
      
    
    {
      "integrationIdentifier": string,
      "actionName": string,
      "instanceId": string,
      "instanceConfiguration": {
        object ([QuickActionInstanceConfiguration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionInstanceConfiguration))
      },
      "entitiesGroup": string,
      "button": {
        object ([QuickActionButton](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionButton))
      },
      "parametersList": [
        {
          object ([QuickActionParameterValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionParameterValue))
        }
      ],
      "id": string,
      "order": integer
    }  
  
Fields  
---  
`integrationIdentifier` |  `string` Output only. The integration identifier of the quick action.  
`actionName` |  `string` Output only. The action name of the quick action.  
`instanceId` |  `string` Output only. The instance id of the quick action.  
`instanceConfiguration` |  `object (`[QuickActionInstanceConfiguration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionInstanceConfiguration)`)` Output only. The configuration of the quick action.  
`entitiesGroup` |  `string` Output only. The entities group of the quick action.  
`button` |  `object (`[QuickActionButton](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionButton)`)` Output only. The button of the quick action.  
`parametersList[]` |  `object (`[QuickActionParameterValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/QuickActionParameterValue)`)` Output only. The parameters of the quick action.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The id of the quick action.  
`order` |  `integer` Output only. The order of the quick action.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
